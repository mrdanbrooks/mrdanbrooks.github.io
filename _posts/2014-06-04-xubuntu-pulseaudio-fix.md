---
layout: post
title: Fix Volume Control in Xubuntu
tags: linux xfce
category: systems
year: 2014
month: 6
day: 4
published: true
summary:
---
The answer provided here worked for me

```
http://askubuntu.com/questions/130927/how-to-switch-default-sound-device-controlled-by-hardware-keys-in-xubuntu
```

Try the following line:

```
xfconf-query -c xfce4-mixer -p /active-card -s PlaybackBuiltinAudioAnalogStereoPulseAudioMixer
```
