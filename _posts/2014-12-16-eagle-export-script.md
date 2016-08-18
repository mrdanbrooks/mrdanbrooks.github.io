---
layout: post
title: Exporting for etching in Eagle CAD
category: notes
icon: beer
year: 2014
month: 12
day: 16
published: true
summary: A script for exporting PCBs for etching using Eagle CAD
---

The following commands can be entered into eagle cad to produce images suitable for use in etching PCBs.

```
DISPLAY ALL
DISPLAY None
DISPLAY Bottom Pads Vias Dimension
EXPORT IMAGE ~/Desktop/bottom.png MONOCHROME 600;
DISPLAY None
DISPLAY Top Pads Vias Dimension
EXPORT IMAGE ~/Desktop/top.png MONOCHROME 600;
DISPLAY ALL
```

This will produce two monochrome images, one for the top and one for the back of the board.
Each side will consist of the traces, pads, and vias.


These commands can also be put (as is) into a file and saved as a script.
In OSX, these files are located in ``/Applications/Eagle/scr`` as ``.scr`` files.

