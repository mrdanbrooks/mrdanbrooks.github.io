---
layout: post
title: Mount specific USB device to /storage using udev
category: notes
tags: udev linux systems
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

Make a file at ``/home/dan/test.sh`` with the following content

```bash
#!/bin/bash
echo "hello!" > /home/dan/test.log
```

Change the permissions on the file to be executable

```bash
$ chmod 755 /home/dan/test.sh
```

Edit /etc/udev/rules.d/01-myrules.rules

```bash
ATTRS{SERIAL}=="C52404CA, RUN="/home/dan/test.sh"
```

And finally refreshing the udev rule.

```bash
$ sudo udevadm control --reload-rules
```

plugging in the device caused the rule to fire, but so did unplugging it. 
This was solved by adding the ``ACTION=="add"`` option to the rule. 

At this point, my rule looked like the following

```
ATTRS{serial}=="C52404CA", ACTION=="add", RUN+="/bin/mount /dev/%k /storage"
```

**Edit:** I later realized that this mounted the device for user root, so that was not very useful. 
See [mounting permissions]({% post_url 2014-09-28-mounting-permissions %}) for how to fix this.

At this point, add that rule to the rules file, reload the udev rules, and you're done!

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
