---
layout: post
title: Disable Google Chrome Automatic Software Update in OSX
tags: osx
category: notes
icon: device-desktop
year: 2014
month: 6
day: 11
summary: Disable google autoupdates for osx     
---

Disable Google Chrome Automatic Software Update
Apr 6, 2012 - 8 Comments

Google Chrome automatic update

Google Chrome automatically updates itself in the background when a new version is out, this takes responsibility out of user hands and makes it simple to keep up to date with the latest version of the app. Generally you should leave automatic update enabled, if not for its ease than for the security benefits of having the freshest browser version pushed to you automatically, but if you want to disable the sizable automatic updates to reduce Personal Hotspot data use or something similar you can do so with a defaults write command.
Disabling Google Chrome Automatic Updates

    Launch the Terminal, found in /Applications/Utilities/
    Enter the following defaults write command and hit return:

```
    defaults write com.google.Keystone.Agent checkInterval 0
    Exit out of Terminal and restart Google Chrome
```

Note that this disables all automatic updates for all Google applications on the computer, not just for Chrome. There may be a way to disable Chromes automatic updating only but I haven’t found it, even Google offers the more broad solution outlined above.
Manually Updating Chrome After Automatic Update is Disabled

Now that you’ve disabled Chrome’s automatic updates, you’ll want to manually update. The easiest way would be to just download the latest version of Chrome from the website, but you can also initiate the update process from the command line by following the steps outlined below:

    From the OS X Finder, hit Command+Shift+G to bring up the Go To Folder window, enter the following path:

    /Library/Google/GoogleSoftwareUpdate/GoogleSoftwareUpdate.bundle/Contents/Resources/
    Locate “CheckForUpdatesNow.command” and double-click on it to launch the Terminal and start the Google software update manually

If you get tired of dealing with manual updates, it’s easy to turn back on again:
Re-Enable Google Chrome Auto Updates

    Launch the Terminal, found in /Applications/Utilities/ and enter the following defaults write command:

```
    defaults write com.google.Keystone.Agent checkInterval 18000
    Exit Terminal and restart Google Chrome to reactive automatic updates
```

The number on the end is the number of seconds between version checking intervals, 18000 is the default setting but if you want to be more or less aggressive select a higher or lower number accordingly.

As mentioned earlier, it’s generally recommended as a maintenance tip to leave automatic updates turned on for all applications, Chrome included.
