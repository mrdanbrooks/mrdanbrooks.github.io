---
layout: post
title: Downloading an Entire Web Site with wget
tags: linux
category: random
year: 2015
month: 09
day: 17
published: true
summary: If you ever need to download an entire Web site, perhaps for off-line viewing, wget can do the job.
---

Below is an article I found to be particularly useful that was written by [Dashamir Hoxha on September 5th, 2008 for www.linuxjournal.com](http://www.linuxjournal.com/content/downloading-entire-web-site-wget).
I take no credit for the article or contents.
Websites have a tendency to disappear over time and links die even faster, so I have copied it here to preserve the knowledge.
Please support the original content provider by clicking on the link above (if it still works) and then on some of their advertisements.

----------------------------------------

If you ever need to download an entire Web site, perhaps for off-line viewing, wget can do the job. 
For example:

```
$ wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains website.org \
     --no-parent \
         www.website.org/tutorials/html/
```

This command downloads the Web site www.website.org/tutorials/html/.

The options are:

 * ``--recursive``: download the entire Web site.
 * ``--domains website.org``: don't follow links outside website.org.
 * ``--no-parent``: don't follow links outside the directory tutorials/html/.
 * ``--page-requisites``: get all the elements that compose the page (images, CSS and so on).
 * ``--html-extension``: save files with the .html extension.
 * ``--convert-links``: convert links so that they work locally, off-line.
 * ``--restrict-file-names=windows``: modify filenames so that they will work in Windows as well.
 * ``--no-clobber``: don't overwrite any existing files (used in case the download is interrupted and
    resumed).


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
