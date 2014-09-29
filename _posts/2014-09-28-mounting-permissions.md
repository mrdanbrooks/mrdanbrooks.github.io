---
layout: post
title: Setting permissions while mounting a device
category: systems
tags: linux
year: 2014
month: 9
day: 28
published: true
summary: How to set owner and group permissions when mounting a device
---
After I had setup my usb drive to [automatically mount when plugged in]({% post_url 2014-09-04-udev-usb-mounting %}), I realized that the only person who could use it was root. 
I needed to change the permissions so that my user could use it (or any user for that matter), which can be specified in the mount command using the ``-o`` option.

```
mount -t deviceFileFormat -o umask=filePermissons,gid=ownerGroupID,uid=ownerID /device /mountpoint
```

Note that it asks for a umask, which is actually the inverse of the binary permission value (see [wikipedia](http://en.wikipedia.org/wiki/Umask)).
Additionally, it wants user and group _ids_, not the names. 

To find a speific user's user id, use

```bash
$ id -u username
```

To find a specific user's group id, use

```bash
$ id -g username
```

To see all the groups a user belongs too

```bash
$ groups username
```

To get a corresponding list of those group's ids,

```bash
$ id -G username
```

I decided that I wanted the owner to be the "default" user instead of root, and the group to be anyone in the _users_ group.
The "default" user is the first one created on the system, and should have id 1000, and the _users_ group should have id 100.
The owner and group members would have full rwx permissions, while everyone else would just have r-x.

The resulting command was

```bash
$ sudo mount -o umask=0002,uid=1000,gid=100 /dev/sda1 /storage
```


