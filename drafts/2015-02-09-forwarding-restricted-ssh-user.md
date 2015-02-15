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

http://askubuntu.com/questions/48129/how-to-create-a-restricted-ssh-user-for-port-forwarding

## Adding a user without /home or a shell.

By default the ``useradd`` command doesnt create home directories. 
We also don't want them to have a shell, so we point them towards ``/bin/false`` instead of ``/bin/sh``. [reference][1]

```
sudo useradd -s /bin/false USERNAME
```

 * **-r** Optionally makes this a system user
 * **-s** Shell command to execute


## References

[1]: http://askubuntu.com/questions/29359/how-to-add-user-without-home



