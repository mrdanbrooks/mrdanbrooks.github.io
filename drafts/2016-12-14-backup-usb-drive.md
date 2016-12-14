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


## Backing up

To create a backup of a USB drive, you first need to determine the device handle as listed in ``/dev``.
Then, you can use ``dd`` to create a bit-by-bit copy.

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd1       956M  289M  668M  31% /media/myusbdrive

$ sudo dd if=/dev/sdd of=~/usbdrive.img
```

After creating the backup image, take a look at what you made.
Remember, you just copied the WHOLE disk, not just a single filesystem.

```
$ file usbdrive.img
usbdrive.img: x86 boot sector

$ fdisk -l usbdrive.img
Disk usbdrive.img: 1004 MB, 1004535808 bytes
7 heads, 38 sectors/track, 7375 cylinders, total 1961984 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000

               Device Boot      Start         End      Blocks   Id  System
usbdrive.img1          *          255     1961983      980864+   b  W95 FAT32
```

## Testing the backup

Now, to convince yourself that the backup image is good by mounting it.
Trying to just mount the device straight up is unlikely to work.

```
$ sudo mkdir /mnt/usbdrive
$ sudo mount ~/usbdrive.img /mnt/usbdrive -o loop
mount: wrong fs type, bad option, bad superblock on /dev/loop0,
       missing codepage or helper program, or other error
       In some cases useful info is found in syslog - try
       dmesg | tail  or so
```

Adding ``-t vfat`` won't solve this problem (if it were that simple, mount could have figured it out by itself).
The real problem is that ``mount`` is looking for a filesystem, but what we just gave it was an entire disk devices worth of information.
Since the filesystem we are looking for is not necessarily the very first thing on the disk, ``mount`` doesn't know how to handle it.
The trick is to figure out where the filesystem starts and specify the offset.
Looking at the information from ``fdisk``, we can see the the FAT32 filesystem starts at sector 255, and each sector is 512 bytes.
So, if we tell mount to look at an offset of 130560 into the file, it should find its filesystem.

```
$ sudo mount -o ro,loop,offset=130560 usbdrive.img /mnt/usbdrive
$ mount | grep usbdrive.img
usbdrive.img on /mnt/usbdrive type vfat (ro)
```

## Restoring

Restoring the USB device to its previous state can be done by running 
You can then use this image to restore the same drive to its previous state, or put the data onto a new drive (of the same size or larger).

```
$ sudo dd if=~/usbdrive.img of=/dev/sdd
```

If for some reason the device is damaged, it is probably better to use a tool like ``ddrescue`` which will not fail on errors.
The disk may need to be checked and repaired before it can be mounted.
This can be accomplished by creating a device loop

```
$ sudo losetup --offset 130560 /dev/loop2 usbdrive.img
$ sudo fsck /dev/loop2
$ sudo mount /dev/loop2 /mnt/usbdrive
```
----------------------------------------

Sources: <http://askubuntu.com/a/318897> and <https://major.io/2010/12/14/mounting-a-raw-partition-file-made-with-dd-or-dd_rescue-in-linux/>
