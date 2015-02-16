---
layout: post
title: Restricted a SSH user for port forwarding
tags: 
category: systems
year: 2015
month: 02
day: 09
published: true
summary: Creating a user that can only be used for ssh port forwarding
---


## Adding a user without /home or a shell.

By default the ``useradd`` command doesnt create home directories. 
We also don't want them to have a shell, so we point them towards ``/bin/false`` instead of ``/bin/sh``. [[link]][2]

```
sudo useradd -s /bin/false USERNAME
```

**-r** Optionally makes this a system user<br/>
**-s** Shell command to execute

### Setting up key login

First we need to generate an keypair using the following command.
Note: If you don't want to use a passphrase  don't enter one.

```
ssh-keygen -t rsa
```

If you name the keyfile something strange like *id_rsa.fish*, you might have to add it manually to the clients ``~/.ssh/config`` by adding the following line to the top of the file

```
IdentityFile ~/.ssh/id_rsa.fish
```

Next, we need to install the public key on server so that our restricted user can use it. 
By default, ssh looks in ``~/.ssh/authorized_keys`` for a users keys.
However, we didn't give our user a home directory so that isn't going to work.
This can be changed by setting the ``AuthorizedKeysFile`` directive in ``/etc/ssh/sshd_config``.
We want to do this under the ``Match User`` directive so that this only applies to our special user.
So where could we store the keys? 
Well, anywhere you want, but as an example lets put it in another users ssh directory that we can log into.

Edit the server settings in ``/etc/ssh/sshd_config`` 

```
StrictMode no
...

Match User NEWUSER
   AuthorizedKeysFile /home/ANOTHERUSER/.ssh/NEWUSER_authorized_keys
   ...
```

Note: for this example to work, we need to set ``StrictMode no`` - this sounds really scary but here is what it means (from ``man sshd_config``)

> Specifies whether sshd(8) should check file modes and ownership of the user's files and home directory before accepting login.
> This is normally desirable because novices sometimes accidentally leave their directory or files world-writable.
> The default is "yes".
> Note that this does not apply to ChrootDirectory, whose permissions and ownership are checked unconditionally. 

The reason we need to set ``StrictMode no`` is because we just violated the following statement (from ``man sshd``) when we directed the NEWUSERS authorized_keys file to look in ANOTHERUSER's directory.

> If this file (authorized_keys), the ~/.ssh directory, or the user's home directory are writable by other users, then the file could be modified or replaced by unauthorized users.
> In this case, sshd will not allow it to be used unless the StrictModes option has been set to "no".

Moving on, log in as ANOTHERUSER, create the authorization file and set the group policies such that NEWUSER can read it.

```
$ cat id_rsa.fish.pub >> ~/.ssh/NEWUSER_authorized_keys
$ sudo chgrp NEWUSER ~/.ssh/NEWUSER_authorized_keys
$ sudo chmod 640 ~/.ssh/NEWUSER_authorized_keys
```

!! Locking things down

Here are some additional settings we want to impose upon our NEWUSER. [[link]][1]
We will add these to the ``/etc/ssh/sshd_config`` file.

```
...
Match User NEWUSER
   AllowTcpForwarding yes
   X11Forwarding no
   PermitTunnel no
   GatewayPorts no
   PasswordAuthentication no
#   AllowAgentForwarding no
#   PermitOpen localhost:8080
   ForceCommand echo 'This account can only be used for local access'
```


!! Testing SSHD settings
Before we restart the sshd daemon and potentially break everything and lock ourselves out, lets test to make sure the changes we made to the configuration file are correct.

```
sudo /usr/sbin/sshd -t
```

If there is a problem it will show on the screen like so

```
/etc/ssh/sshd_config: line 26: Bad configuration option: PermitRootLogins
/etc/ssh/sshd_config: terminating, 1 bad configuration options
```

Otherwise, if there are no errors it simply wont display anything.






[[link]][3]

[1]: http://askubuntu.com/questions/48129/how-to-create-a-restricted-ssh-user-for-port-forwarding
[2]: http://askubuntu.com/questions/29359/how-to-add-user-without-home
[3]: http://unix.stackexchange.com/questions/136678/ssh-into-an-account-which-has-no-home-directory


