---
layout: post
title: Streaming video to OSX using gstreamer
tags: osx
category: random
year: 2015
month: 05
day: 12
published: true
summary: Using Gstreamer to send webcam images from linux to OSX
---

On a linux server

```
gst-launch-0.10 v4l2src device=/dev/video0 ! videoscale ! video/x-raw-yuv,width=640,height=480 ! ffmpegcolorspace ! jpegenc ! tcpserversink  port=5000
```

On an OSX client

```
gst-launch-1.0 tcpclientsrc host=x.x.x.x port=5000 ! jpegdec ! videoconvert! osxvideosink
```
