---
layout: post
title: Getting Expose in XFCE4 using Skippy-xd
category: systems
tags: linux xfce
year: 2014
month: 6
day: 10
published: true
summary: Skippy-xd in xfce4
---

```
sudo add-apt-repository ppa:landronimirc/skippy-xd-daily
sudo apt-get update
sudo apt-get install skippy-xd
```

Download the original skippy-xd.rc-default config file from

```
https://wiki.ubuntu.com/Skippy?action=AttachFile&do=view&target=skippy-xd.rc-default 
```

and copy it to ``~/.config/skippy-xd/skippy-xd.rc``. 

Go to XFCE Settings Menu -> Keyboard -> Application Shortcuts and add a new shortcut. The command is 

```
skippy-xd --activate-window-picker
```

and choose a key shortcut to assign to it. You will need to copy the value of the shortcut (such as XF86LaunchB) and paste it as the setting for 

```
[general]
keysym = <shortcut>
```

The default is F11.

Finally, execute the following

```
skippy-xd --start-daemon
```

and press your shortcut key!

To get skippy-xd to run automatically go to Settings Menu -> session and startup -> application autostart and add ``skippy-xd --start-daemon``


