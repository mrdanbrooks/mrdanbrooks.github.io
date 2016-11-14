---
layout: post
title: Streamripping
tags: random
category: notes
icon: beer #weaselpipe.com/icons
year: 2016
month: 11
day: 10
published: true
summary: How to keep your interweb music
---

I love listening to SomaFM's Groove Salad. 
Unfortunately, I don't always have access to internet so that is not always possible.
So, I decided to try capturing some of the music they play so that I can listen to it when I'm working offline.

SomaFM sells some [best hit cd's of Groove Salad](https://store.somafm.com/products/groove-salad-vol-3-cd) as part of a fundraising effort. 
This is a great way of supporting them.
However, it actually only comes with a small set of songs.

Enter streamripper. 
Streamripper lets you connect to internet radio stations, and will automatically try to detect track changes and save the streaming music to file.
It even names the files for you.

Installing streamripper is very easy in Ubuntu.

```
$ sudo apt-get install streamripper
```

To start saving SomaFM music, simply run

```
$ streamripper http://somafm.com/groovesalad.pls
```

Now, it should be mentioned that SomaFM has to pay for the number of people who listen to their station, so leaving this connection running 24-7 is kind of a dick move.
Another issue: if you are running streamripper AND listening to SomaFM  at the same time, you actually are connected to them twice - also a dick move.
To prevent this from happening, you can configure streamripper to actually "rebroadcast" the stream to your music player so that you only have one connection open.

```
$ streamripper http://somafm.com/groovesalad.pls -r localhost:8001
```

After running that command, just configure your music player to use the internet radio station address http://localhost:8001 instead of SomaFM.

The system isn't perfect.
Most radio stations use some sort of transition between songs, so the end of one song will overlap slightly with the beginning of the next song.
This is not an issue for me since I am not looking for perfect quality tracks

To see what kind of music you have collected, use the following command to list how many files have been saved from each artist.

```
ls | cut -d "-" -f 1 | uniq -c | sort -n
```
