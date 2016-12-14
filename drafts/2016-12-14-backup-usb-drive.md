---
layout: post
title: Backing up USB drives
tags: linux systems
category: notes
icon: beer #weaselpipe.com/icons
year: 2016
month: 12
day: 14
published: true
summary: Linux commands for backing up a USB Drive
---

If you care about the contents of your disks, you should be making backups of them.
Making backups is easy, but I'm always paranoid that I won't do something correctly and be left with an unusable file blob on the fatefull day I end up needing to restore some data.
Thus, I am documenting the process I found to be reliable (if not the most efficient) using linux systems.


To create a backup of a USB drive, you first need to determine the device handle as listed in ``/dev``.
Then, you can use ``dd`` to create a bit-by-bit copy.

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd1       956M  289M  668M  31% /media/myusbdrive

$ sudo dd if=/dev/sdd of=~/usbdrive.img
```

Restoring the USB device to its previous state can be done by running 
You can then use this image to restore the same drive to its previous state, or put the data onto a new drive (of the same size or larger).

```
$ sudo dd if=~/usbdrive.img of=/dev/sdd
```

Finally, you can test that the disk image you made is good by mounting it!

```
mount ~/usbdrive.img /mnt/usbdrive -o loop
```

If for some reason the device is damaged, it is probably better to use a tool like ``ddrescue`` which will not fail on errors.

----------------------------------------

Source: <http://askubuntu.com/a/318897>
