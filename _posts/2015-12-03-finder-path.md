---
layout: post
title: Show full path in Finder title bar
tags: osx systems
category: notes
year: 2015
month: 12
day: 03
published: true
summary: How to enable the full path in Finders window.
---
Disclaimer
----------

Below is an article I found to be particularly useful that was written by [Cory Bohon on December 5th, 2008 for www.engadget.com](http://www.engadget.com/2008/12/05/terminal-tips-enable-path-view-in-finder).
I take no credit for the article or contents.
Websites have a tendency to disappear over time and links die even faster, so I have copied the content here where I can preserve the knowledge.
Please support the original content provider by clicking on the link above (if it still works) and then on some of their advertisements.

----------------------------------------

![FinderWindow](http://www.blogcdn.com/www.tuaw.com/media/2008/12/picture-2_terminal-tips_-enable-path-view-in-finder_cb12793.jpg)

When you open a Finder window and start browsing to a folder, do you lose track of the path to that folder?
If you do, the Terminal command below will enable path view in the Finder -- this means that you will see the directory path to the current folder you are browsing in the title bar, instead of only seeing the name of the current directory.

To make directory paths visible atop Finder windows, open Terminal.app (/Applications/Utilities/) and type the following command:

```
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

Once you run the above command, you will also need to restart the Finder, so you can either type "killall Finder" and hit return, or use the Force Quit option under the Apple menu to relaunch it.
The Finder will restart, and you will start seeing the paths to directories in the title bar.

***Update:*** As some have pointed out in the comments below, this Terminal command will only work with Mac OS X Leopard (version 10.5).
