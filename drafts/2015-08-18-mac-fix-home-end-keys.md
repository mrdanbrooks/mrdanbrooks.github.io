---
layout: post
title: Fixing the behavior of the home, end, pg-up, and pg-down keys in OSX. 
tags: osx
category: systems
year: 2015
month: 08
day: 18
published: true
summary:  How to fix the behavior of the home and end keys in osx.
---

By default, the home and end keys in osx will annoyingly scroll your document, while in the rest of the modern world they move your cursor to the begining or end of the line.
Additionally, in osx the pg-up and pg-down keys simply shift the viewport up or down a page but dont actually move the cursor, while every other computer in the world will move the cursor for you. 

Fortunately, [the fix is easy](http://phatness.com/2007/08/fix-home-and-end-keys-on-mac-os-x/).
Below is a copy of the instructions posted on [phatness.com](http://phatness.com) for fixing your mac.

> 1) Create a new text file at:
> 
> ```
> Users/[your username]/Library/KeyBindings/DefaultKeyBinding.dict
> ```
> 
> (If you have already messed with key bindings, this file might already be present.)
> 
> 2) Copy and paste this code into the file:
> 
> ```
> {
>     "\UF729"  = "moveToBeginningOfLine:";
>     "$\UF729" = "moveToBeginningOfLineAndModifySelection:";
>     "\UF72B"  = "moveToEndOfLine:";
>     "$\UF72B" = "moveToEndOfLineAndModifySelection:";
>     "\UF72C"  = "pageUp:";
>     "\UF72D"  = "pageDown:";
> }
> ```
> 
> 3) Put your junk in that box (err, save DefaultKeyBinding.dict)
> 
> 4) Open that box (err, close and reopen any applications to take affect)
> 

Apparently, some people report having trouble in the terminal even after applying the above fix.
I use iTerm2 instead of Terminal.app, and I have not noticed this problem yet.
For the sake of completeness, here is the suggested fix (from the same source)

> You must setup mappings in Terminal separately. Open up preferences for Terminal.app, and under the Keyboard tab, set the actions for the following keys (Change action to ‘Send string to shell’):
> 
> \033 is the code for escape. Press the Esc key rather than typing it out.
> 
> ```
> Key		Escape Sequence
> Home		\033[1~
> End		\033[4~
> Page Up		\033[5~
> Page Down	\033[6~
> ```
> 
> Setting up terminal only gets you part of the way. You also need to configure bash. Go create or edit ~/.inputrc and add the following:
> 
> ```
> "\e[1~": beginning-of-line
> "\e[4~": end-of-line
> "\e[5~": history-search-backward
> "\e[6~": history-search-forward
> "\e[3~": delete-char
> "\e[2~": quoted-insert
> "\e[5C": forward-word
> "\e[5D": backward-word
> "\e\e[C": forward-word
> "\e\e[D": backward-word
> set completion-ignore-case On
> ```
> 
> Now everything should be working the way you expect. (Except for Firefox, but you can figure that one out on your own.)


----------------------------------------

To use this template:
=====================

 - Make a copy
 - Change the file name
 - Update the header info
  * change published to `true'
 - Delete these quick notes!

Add a tag!
----------

Its fast and easy!

Just go to `~/Source/notes/tags/` and add a file.md with the following content

    ---
    layout: blog_by_tag
    title: <tagnamegoeshere> posts
    tag: <tagnamegoeshere>
    permalink: <tagnamegoeshere>/
    ---

Don't forget to add the tag file when you commit!

Formatting
----------

_Italic_

**bold**

`FixedSpace`

Links
-----

Make [External Links](www.google.com) like this.

Make [Post Links]({% post_url 2014-09-04-udev-usb-mounting %}) like this.

Make [Static internal Links](/about/) would go to weaselpipe.com/about/.

Making [Reference Style Links][google] can be done [like][yahoo] so. Later on there should be a line like this

[google]: http://www.google.com/ "This is google"
[yahoo]: http://www.yahoo.com/ "Yahoo"


Writing code
------------

Description of what you are looking at

``` 
Code Here
```

Quoting Text
------------

I like to quote other peoples websites

-----------------------------
> Line one
> line two
> line three
> > Indented quote
> > line two of indented quote
> Line four
> line five
> line six
-----------------------------


Markdown lets you be lazy

-----------------------------
> Line one
line two
line three
> > Indented quote
> > line two of indented quote
Line four
line five
> line six
-----------------------------


Lists
-----

 * Red
 * Green
 * Blue

 - The number one
 - second thing
 - three


Images
------

![Alt Text](/path/to/image.jpg "optional title")

Alternatively, you can just use html syntax.
