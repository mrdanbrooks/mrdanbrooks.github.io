---
layout: post
title: Sharing a networked scanner from raspberry pi to OS X
tags: linux osx
category: notes
published: true
summary: How to use TWAIN/SANE to share a scanner to an osx machine.
---
So I wanted to be able to connect my scanner to my network and not have to plug it in every time I wanted to use it. In the end, it worked but was kind of silly. I still have to plug in a usb device, although it doesn't have to be the scanner anymore. Directions below.

SANE is the API linux uses for scanners. It is split into backends (drivers) and frontends (access programs). A saned server can share devices across the network with a sane 'net' backend driver on another machine. TWAIN is a driver API used by OSX to access hardware. So we use a TWAIN driver that provides access to SANE to get at our networked scanner. 

Server (RPI) Installation
-------------------------
First we need to configure the raspberry pi.

```
sudo apt get install sane-utils
```

edit /etc/default/saned

```
# Defaults for the saned initscript, from sane-utils

# Set to yes to start saned
RUN=yes

# Set to the user saned should run as
RUN_AS_USER=saned
```

Then edit /etc/sane.d/saned.conf

```
## Access list
# A list of host names, IP addresses or IP subnets (CIDR notation) that
# are permitted to use local SANE devices. IPv6 addresses must be enclosed
# in brackets, and should always be specified in their compressed form.
#
10.10.1.0/24
```

Restart the saned server

```
sudo service saned restart
```

And add the saned user to the lp group so it can access the scanner

```
sudo adduser saned lp
```

Client OSX Configuring
----------------------
You should be able to install the twain/sane services using macports

```
sudo port install twain-sane
```

Otherwise you can grab some installers from here ``http://www.ellert.se/twain-sane/``. Using this option you need to first install the libusb, then the backend, the twain-sane, and finally the preference pane.

Next, you need to enable the backend to communicate with the saned server on the rpi. 

If you installed via macports edit /opt/local/etc/sane.d/net.conf or if you used the installers go to "System Preferences", "SANE", "drivers", and configure net. Add the name of your server to that file (in my case, I added ``mrtusks.local``).

You should now be able to see your scanner show up when you type in the command:

```
scanimage -L
```

Finally, to make it work with image capture. Someone at apple decided you have to have a usb device plugged in for image capture to work. And that usb device cannot be an apple device. So find a USB stick that you want to pretend to be a scanner. Use the following command to get the Vendor ID and Product IDs.

```
system_profiler SPUSBDataType
```

Then edit /Library/Image\ Capture\TWAIN\ Data\ Sources/SANE.ds/Contents/Info.plist:

```
<dict>
       <key>device type</key>
       <string>scanner</string>
       <key>product</key>
       <string>0x5406</string>
       <key>vendor</key>
       <string>0x0781</string>
</dict>
```

Be sure to replace the vendor and product ids with the ones you just looked up. 

Somewhere along the way you probably need to reboot the osx machine.

Future Work
-----------

It would be nice to have a virtual usb device that was always "inserted" that could be added to Image Capture's nice list so that I didn't have to have a particular usb drive plugged in.

References
----------

```
http://ubuntuforums.org/showthread.php?t=1519201
http://www.ellert.se/twain-sane/faq.html
```


