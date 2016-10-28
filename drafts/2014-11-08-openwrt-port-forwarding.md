---
layout: post
title: Port Forwarding in OpenWRT
tags: linux
category: notes
year: 2014
month: 11
day: 08
published: true
summary: Setting up port forwarding in OpenWRT from the command line.
---

Instructions from the [OpenWRT website](http://wiki.openwrt.org/doc/howto/port.forwarding).

```
config 'redirect'
        option 'name' 'ssh'
        option 'src' 'wan'
        option 'proto' 'tcp'
        option 'src_dport' '5555'
        option 'dest_ip' '192.168.1.100'
        option 'dest_port' '22'
        option 'target' 'DNAT'
        option 'dest' 'lan'
```
