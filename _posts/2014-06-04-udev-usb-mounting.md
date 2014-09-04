---
layout: post
title: Mount specific USB device to /storage using udev
category: systems
tags: udev linux
year: 2014
month: 9
day: 4
published: true
summary: How to mount a particular USB drive to a particular location automatically when it is inserted.
---

In Ubuntu, UDev rules are stored in ``/etc/udev/rules.d/``

UDev rules work by matching attributes of a device (such as ``SUBSYSTEM=="usb"`` - note the ==) and then firing off a command when all the rules match (such as ``RUN+="/my/script.sh"``)

To see what attributes a USB device located at ``/dev/sdc1`` has

```
udevadm info -a -n /dev/sdc1
```

My device had a serial number programed into it

```
ATTRS{serial}=="C52404CA"
```

This was sufficient to uniquely identify my USB device, but you could also use other attributes such as the vendor name if necessary.
I created a test rule to make sure things would work the way I wanted them to by making shell script to run when the rule was triggered.

```
$ vim /home/dan/test.sh
```

```bash
#!/bin/bash
echo "hello!" > /home/dan/test.log
```

```
$ chmod 755 /home/dan/test.sh
$ vim /etc/udev/rules.d/01-myrules.rules
```

```
ATTRS{SERIAL}=="C52404CA, RUN="/home/dan/test.sh"
```

And finally refreshing the udev rule.

```
$ sudo udevadm control --reload-rules
```

plugging in the device caused the rule to fire, but so did unplugging it.
So my rule ended up being

```
ATTRS{serial}=="C52404CA", ACTION=="add", RUN+="/bin/mount /dev/%k /storage"
```

Reload the udev rules

Bonus Tip:
To disable automatic device mounting in Gnome

```
install dconf-editor
sudo apt-get install dconf-tools
dconf-editor
```

Note that I did not run the command as root (you need to do it as the current user). Go to org.gnome.desktop.media-handling

and unchceck automount and automount-open

If you use cinnamon you have to go to org.cinnamon.desktop.media-handling.
