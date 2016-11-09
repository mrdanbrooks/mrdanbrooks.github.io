---
layout: post
title: Getting Expose in XFCE4 using Skippy-xd
category: notes
tags: linux xfce systems
icon: device-desktop
year: 2014
month: 6
day: 10
published: true
summary: Skippy-xd in xfce4
---
OSX has an amazing feature called 'expose' that lets you see all your open windows at a glance and select one to refocus on. 
This feature is also available in Ubuntu's Unity interface using the keyboard shortcut ``Ctrl-W``. 
However, it is absent in many other linux window managers, include XFCE. 
Fortunately, there is a clever bit of software we can install to add that functionality back in.
The following insturctions have been tested to work in XFCE4.

```
sudo add-apt-repository ppa:landronimirc/skippy-xd-daily
sudo apt-get update
sudo apt-get install skippy-xd
```

Download the original skippy-xd.rc-default config file from

```
https://wiki.ubuntu.com/Skippy?action=AttachFile&do=view&target=skippy-xd.rc-default 
```

or use the following copy of that file

```

# Copy this to ~/.skippy-xd.rc and edit it to your liking
#
# Notes:
#
# - keysym can be anything XStringToKeysym can handle
#   (like F11, KP_Enter or implementation specific keysyms)
#
# - colors can be anything XAllocNamedColor can handle
#   (like "black" or "#000000")
#
# - distance is a relative number, and is scaled according to the scale
#   factor applied to windows
#
# - fonts are Xft font descriptions
#
# - booleans are "true" or anything but "true" (-> false)
#
# - opacity is an integer in the range of 0-255
#
# - brighness is a floating point number (with 0.0 as neutral)
#
# - if the update frequency is a negative value, the mini-windows will only
#   be updated when they're explicitly rendered (like, when they gain or
#   lose focus).
#
# - the 'shadowText' option can be a color or 'none', in which case the
#   drop-shadow effect is disabled
#

[general]
keysym = F11
distance = 50
useNetWMFullscreen = true
ignoreSkipTaskbar = true
updateFreq = 10.0
lazyTrans = false

[xinerama]
showAll = false

[normal]
tint = black
tintOpacity = 0
opacity = 200

[highlight]
tint = #101020
tintOpacity = 64
opacity = 255

[tooltip]
show = true
border = #e0e0e0
background = #404040
opacity = 128
text = #e0e0e0
textShadow = black
font = fixed-11:weight=bold
```

and copy it to ``~/.config/skippy-xd/skippy-xd.rc``. 

Go to XFCE Settings Menu -> Keyboard -> Application Shortcuts and add a new shortcut. The command is 

```
skippy-xd --toggle-window-picker
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


