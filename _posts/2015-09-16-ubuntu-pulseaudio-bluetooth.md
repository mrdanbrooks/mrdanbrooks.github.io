---
layout: post
title: Ubuntu + PulseAudio + Blueman = Fail
tags: linux xfce systems
category: notes
year: 2015
month: 09
day: 16
published: true
summary: How to fix your bluetooth headset.
---

To be fair, it did _just work_ out of the box.
Sort of.

I purchased a bluetooth adapter for my headphones to use with my XUbuntu 14.04 desktop at work.
Bluetooth headphones can work in two different modes: duplex telephony (HSP/HFP) or high fedility playback (A2DP).
The duplex telephony mode is more for being used as a phone headset and uses lower quality audio but also allows for microphone input.
High fedility playback is for listening to music and sounds better.

The headphones adapter worked right away, but it always defaulted to the low quality telephony mode.
After it connected I could then go and change the mode to A2DP manually, but that got annoying.
So I disabled the telephony mode, and afterwords the bluetooth would still connect but the device would no longer show up as an audio device in PulseAudio. 
Awesome.

The fix to get it working again (according to [askubuntu](http://askubuntu.com/q/366032)) was to run the following commands

```
$ sudo pactl load-module module-bluetooth-discover
$ sudo service bluetooth restart
```

and then re-connect the bluetooth device.

So, I then wondered how I could make this happen automatically.
The answer should have been to edit ``/etc/pulse/default.pa`` and add the line 

```
load-module module-bluetooth-discover
```

but when I checked the file, it was already included! 


Apparently, this is a problem with blueman, the bluetooth software.
According to [this bug report](https://github.com/blueman-project/blueman/issues/64), blueman actually _unloads_ the pulse audio bluetooth-discover module. 
The author of that piece of code described the reasoning

> originally when PulseAudio project was young, it did not properly manage bluetooth headsets, so I unloaded the pulseaudio discover module and managed the devices manually inside Blueman.
> i.e. when a headset connects, blueman automatically detects that, loads Pulseaudio module "bluetooth-device", routes active streams to the headset.
> Lately I've tested that functionality in KDE and it appears that Pulseaudio now manges everything correctly.
> So the PulseAudio plugin in Blueman probably needs to be disabled or patched accordingly with the functionality of latest versions of Pulseaudio.

A patch was released about a year ago.

