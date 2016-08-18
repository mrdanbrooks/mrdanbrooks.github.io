---
layout: post
title: Moving buffers in vim
category: notes
tags: vim, systems
year: 2013
month: 6
day: 3
published: true
summary: How to move vim buffers around
---
Starting with this:

```
____________________
| one       | two  |
|           |      |
|           |______|
|           | three|
|           |      |
|___________|______|
```

Make 'three' the active window, then issue the command ``ctrl-w J``. This moves the current window to fill the bottom of the screen, leaving you with:

```
____________________
| one       | two  |
|           |      |
|___________|______|
| three            |
|                  |
|__________________|
```

Now make either 'one' or 'two' the active window, then issue the command ``ctrl-w r``. This 'rotates' the windows in the current row, leaving you with:

```
____________________
| two       | one  |
|           |      |
|___________|______|
| three            |
|                  |
|__________________|
```

Now make 'two' the active window, and issue the command ``ctrl-w H``. This moves the current window to fill the left of the screen, leaving you with:

```
____________________
| two       | one  |
|           |      |
|           |______|
|           | three|
|           |      |
|___________|______|
```

As you can see, the manouevre is a bit of a shuffle. With 3 windows, it's a bit like one of those 'tile game' puzzles. I don't recommand trying this if you have 4 or more windows - you'd be better off closing them then opening them again in the desired positions. 

answered Apr 7 '10 at 11:25 by nelstrom
http://stackoverflow.com/questions/2586984/how-can-i-swap-positions-of-two-open-files-in-splits-in-vim

