---
layout: post
title: How to create a restricted SSH user for port forwarding?
tags: linux
category: security
year: 2011
month: 06
day: 22
published: true
summary: an askubuntu.com response!
---

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
   * ``PermitOpen``:

   * > Specifies the destinations to which TCP port forwarding is permitted. The forwarding specification must be one of the following forms:
   * > ``PermitOpen host:port``
     > ``PermitOpen IPv4_addr:port``
     > ``PermitOpen [IPv6_addr]:port``
     > Multiple forwards may be specified by separating them with whitespace. An argument of 'any' can be used to remove all restrictions and permit any forwarding requests. By default all port forwarding requests are permitted.
     > 

 * 
   * ``PermitTunnel`` - Specifies whether tun(4) device forwarding is allowed. The default is 'no'
   * ``X11Forwarding`` - Specifies whether X11 forwarding is permitted. The default is 'no'

----------------------------------------

To use this template:
=====================

 - Make a copy
 - Change the file name
 - Update the header info
  * change published to `true'
 - Delete these quick notes!

Add a tag!
----------

Its fast and easy!

Just go to `~/Source/notes/tags/` and add a file.md with the following content

    ---
    layout: blog_by_tag
    title: <tagnamegoeshere> posts
    tag: <tagnamegoeshere>
    permalink: <tagnamegoeshere>/
    ---

Don't forget to add the tag file when you commit!

Formatting
----------

_Italic_

**bold**

`FixedSpace`

Links
-----

Make [External Links](www.google.com) like this.

Make [Post Links]({% post_url 2014-09-04-udev-usb-mounting %}) like this.

Make [Static internal Links](/about/) would go to weaselpipe.com/about/.

Making [Reference Style Links][google] can be done [like][yahoo] so. Later on there should be a line like this

[google]: http://www.google.com/ "This is google"
[yahoo]: http://www.yahoo.com/ "Yahoo"


Writing code
------------

Description of what you are looking at

``` 
Code Here
```

Quoting Text
------------

I like to quote other peoples websites

-----------------------------
> Line one
> line two
> line three
> > Indented quote
> > line two of indented quote
> Line four
> line five
> line six
-----------------------------


Markdown lets you be lazy

-----------------------------
> Line one
line two
line three
> > Indented quote
> > line two of indented quote
Line four
line five
> line six
-----------------------------


Lists
-----

 * Red
 * Green
 * Blue

 - The number one
 - second thing
 - three


Images
------

![Alt Text](/path/to/image.jpg "optional title")

Alternatively, you can just use html syntax.
