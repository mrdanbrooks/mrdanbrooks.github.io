---
layout: post
title: Copy Path Service in Finder
tags: osx
category: notes
icon: beer # file-text, tools, code, home, lock, device-desktop - more @ weaselpipe.com/icons
year: 2017
month: 11
day: 30
published: true
summary: How to add a service to finder that copies the path of a file to the clip board.
---
# Adding a Copy Path Service to OSX

I need to capture the path of a file from finder on a regular basis, to create links within documents on my desktop. Finder does not have built-in functionality to copy a files path to the clipboard. I decided to create a service to allow me to do this.



- Launch Automator and create a new “Service”
- Use the search function to look for “Copy to Clipboard” and drag that into the rightside panel of the Service
- Set ‘Service recieves selected’ to “files or folders” and ‘in’ to “Finder” as shown in the screen shot below
- Save the Service with a name like Copy Path



Credit

http://osxdaily.com/2013/06/19/copy-file-folder-path-mac-os-x/
