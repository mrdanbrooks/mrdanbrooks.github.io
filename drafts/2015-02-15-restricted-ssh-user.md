---
layout: post
title: How to create a restricted SSH user for port forwarding?
tags: linux
category: security
year: 2011
month: 06
day: 22
published: true
summary: An excellent article on creating a restricted SSH user.
---

This is a repost of a very helpful article on [askubuntu.com](http://askubuntu.com/questions/48129/how-to-create-a-restricted-ssh-user-for-port-forwarding), written by [Lekensteyn](http://askubuntu.com/users/6969/lekensteyn) on June 22nd, 2011. 

I am reposting it so that it doesn't disappear on me!

-----

Adding a restricted user consists of two parts: 1. Creating the user 2. Configuring the SSH daemon (sshd)

## Configuring sshd

The best place to get known to the possibilities of SSH is by reading the related manual pages:

 * [ssh(1)](http://manpages.ubuntu.com/manpages/natty/en/man1/ssh.1.html)
 * [ssh_config(5)](http://manpages.ubuntu.com/manpages/natty/en/man5/ssh_config.5.html)
 * [sshd(8)](http://manpages.ubuntu.com/manpages/natty/en/man8/sshd.8.html)
 * [sshd_config(5)](http://manpages.ubuntu.com/manpages/natty/en/man5/sshd_config.5.html)

### Where can SSH client perform actions?

Before you can restrict something, you need to know the features of SSH. Spitting through the manual pages yields:

 * Shell commands execution
 * File upload through sftp
 * Port forwarding
   * The client forwards an (un)used port to the server
   * The server forwards his port to the client
   * The server forwards a port of another host to the client (proxy-ish)
 * X11 forwarding (display forwarding)
 * Authentication agent forwarding
 * Forwarding of a tunnel device

From the _Authentication_ section of the [manual page of sshd(8)](http://manpages.ubuntu.com/manpages/natty/en/man8/sshd.8.html):

> If the client successfully authenticates itself, a dialog for preparing the session is entered.
> At this time the client may request things like allocating a pseudo-tty, forwarding X11 connections, forwarding TCP connections, or forwarding the authentication agent connection over the secure channel.
>
> After this, the client either requests a shell or execution of a command. 
> The sides then enter session mode. 
> In this mode, either side may send data at any time, and such data is forwarded to/from the shell or command on the server side, and the user terminal in the client side.

### Options for restricting SSH features

Files and their options that alter behavior are:

 * ``~/.ssh/authorized_keys`` - contains keys which are allowed to connect which can be given options:
   * ``command="command"`` - The command supplied by the user (if any) is ignored. Note that the client may specify TCP and/or X11 forwarding unless they are explicitly prohibited. Note that this option applies to shell, command or subsystem execution.
   * ``no-agent-forwarding`` - Forbids authentication agent forwarding when this key is used for authentication.
   * ``no-port-forwarding`` - Forbids TCP forwarding when this key is used for authentication
   * ``no-X11-forwarding`` - "Forbids X11 forwarding when this key is used for authentication."
   * ``permitopen="host:port"`` - Limit local 'ssh -L' port forwarding such that it may only connect to the specified host and port.
 * ``~/.ssh/environment`` - This file is read into the environment at login (if it exists). Environment processing is disabled by default and is controlled via the PermitUserEnvironment option
 * ``~/.ssh/rc`` - Contains initialization routines to be run before the user's home directory becomes accessible.
 * ``/etc/ssh/sshd_config`` - the system-wide configuration file
   * ``AllowAgentForwarding`` - Specifies whether ssh-agent(1) forwarding is permitted.
   * ``AllowTcpForwarding``
   * ``ForceCommand`` - "Forces the execution of the command specified by ForceCommand, ignoring any command supplied by the client and ~/.ssh/rc if present. The command is invoked by using the user's login shell with the -c option."
   * ``GatewayPorts`` - "Specifies whether remote hosts are allowed to connect to ports forwarded for the client. By default, sshd(8) binds remote port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports. GatewayPorts can be used to specify that sshd should allow remote port forwardings to bind to non-loopback addresses, thus allowing other hosts to connect."
   * ``PermitOpen``: Specifies the destinations to which TCP port forwarding is permitted. The forwarding specification must be one of the following forms: <br/>
     ``PermitOpen host:port`` <br/>
     ``PermitOpen IPv4_addr:port`` <br/>
     ``PermitOpen [IPv6_addr]:port`` <br/>
     Multiple forwards may be specified by separating them with whitespace. An argument of 'any' can be used to remove all restrictions and permit any forwarding requests. By default all port forwarding requests are permitted.
   * ``PermitTunnel`` - Specifies whether tun(4) device forwarding is allowed. The default is 'no'
   * ``X11Forwarding`` - Specifies whether X11 forwarding is permitted. The default is 'no'

## Applying the restrictions

Modifying the system-wide configuration file ``/etc/ssh/sshd_config`` allows the configuration be applied even if password-based authentication is applied or if the restrictions in ``~/.ssh/authorized_keys`` are accidentally removed. 
If you've modified the global defaults, you should uncomment the options accordingly.

```
Match User limited-user
   #AllowTcpForwarding yes
   #X11Forwarding no
   #PermitTunnel no
   #GatewayPorts no
   AllowAgentForwarding no
   PermitOpen localhost:62222
   ForceCommand echo 'This account can only be used for [reason]'
```

Now add a user:

```
sudo useradd -m limited-user
```

The option ``ForceCommand`` can be omitted if the shell is set to a non-shell like ``/bin/false`` (or ``/bin/true``) as ``/bin/false -c [command]`` won't do anything.

Now the client can only connect to port 62222 on the loopback address of the server over SSH (it will not listen on the public IP address)

Disabling ``AllowTcpForwarding`` would also disallow the use of ``-R``, thus defeating the use of such a restricted account for forwarding a single port. ``PermitOpen localhost:62222`` assumes that port 62222 on the server is never in use because the client can happily connect to it and listen on it too.

If TCP forwarding is allowed in the system-wide configuration and disabled password-based authentication, you can use per-key settings as well. Edit ``~/.ssh/authorized_keys`` and add the next options before the ``ssh-`` (with a space between the options and ssh-):

```
command="echo 'This account can only be used for [reason]'",no-agent-forwarding,no-X11-forwarding,permitopen="localhost:62222"
```

### Verify

To be sure that it works as expected, some test cases need to be run. 
In the below commands, ``host`` should be replaced by the actual login if it's not set in ``~/.ssh/config``. 
Behind the command, a command is shown that should be executed on either the client or server (as specified).

```
# connection closed:
ssh host
# connection closed (/bin/date is not executed):
ssh host /bin/date
# administratively prohibited (2x):
ssh host -N -D 62222 # client: curl -I --socks5 localhost:62222 example.com
ssh host -N -L 8080:example.com:80 # client: curl -I localhost:8080
sftp host
# should be possible because the client should forward his SSH server
ssh host -N -R 8080:example.com:80 # server: curl -I localhost:8080
# This works, it forwards the client SSH to the server
ssh host -N -R 62222:localhost:22
# unfortunately, the client can listen on that port too. Not a big issue
ssh host -N -L 1234:localhost:62222
```

## Conclusion

Checklist: The SSH user should not able to:

 * execute shell commands - done
 * access files or upload files to the server - done
 * use the server as proxy (e.g. webproxy) - done
access local services which were otherwise not publicly accessible due to a firewall - partially, the client cannot access other ports than 62222, but can listen and connect to port 62222 on the server
 * kill the server - done (note that these checks are limited to the SSH server. If you've an other vulnerable service on the machine, it could allow a possible attacker to run commands, kill the server, etc. )

