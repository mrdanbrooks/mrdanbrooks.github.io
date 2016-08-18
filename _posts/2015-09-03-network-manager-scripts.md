---
layout: post
title: Running custom networking scripts with Network Manager
tags: linux systems
category: notes
year: 2015
month: 09
day: 02
published: true
summary: How to set up custom networking scripts using Network Manager.
---

I run Ubuntu Desktop on my machine at work, and for years I've had trouble with the network connection.
It seems that our IT department is... deficient.
To keep a long story short, the switches they have installed have lots of problems with auto negotiation.
Sometimes, you only get 10Mb/s instead of 100Mb/s (don't even ask about 1000Mb/s).
Other times, you might get 100Mb/s only to find out you are operating at half duplex. 

The fix for these issues is to run the command 

```
ethtool -s ethX autoneg off duplex full speed 100
```

On server installations, you can simply put this in the post-up part of ``/etc/network/interfaces``.
On desktops though, it is better to put them in a script that Network Manager can use.
From the man pages

```
 NetworkManager  will  execute  scripts  in the /etc/NetworkManager/dis‐
 patcher.d directory  in  alphabetical  order  in  response  to  network
 events.  Each script should be:
 (a) a regular file
 (b) owned by root
 (c) not writable by group or other
 (d) not set-uid
 (e) and executable by the owner

 Each  script receives two arguments, the first being the interface name
 of the device just activated, and second an action.
```

The actions are ``up``, ``down``, ``vpn-up``, ``vpn-down``, ``hostname``, and ``dhcp4-change``.

Thus, the following script placed in ``/etc/NetworkManager/dispatcher.d/fixspeed.sh`` will run the magic network fixing command.

```
#!/bin/bash
if [ "$1" = "eth0" ] && [ "$2" = "up" ]; then
   ethtool -s eth0 autoneg off speed 100 duplex full
fi
exit $?
```

