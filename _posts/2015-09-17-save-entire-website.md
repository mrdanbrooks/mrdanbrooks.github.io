---
layout: post
title: Downloading an Entire Web Site with wget
tags: linux random
category: notes
icon: beer
year: 2015
month: 09
day: 17
published: true
summary: If you ever need to download an entire Web site, perhaps for off-line viewing, wget can do the job.
---
Disclaimer
----------

Below is an article I found to be particularly useful that was written by [Dashamir Hoxha on September 5th, 2008 for www.linuxjournal.com](http://www.linuxjournal.com/content/downloading-entire-web-site-wget).
I take no credit for the article or contents.
Websites have a tendency to disappear over time and links die even faster, so I have copied the content here where I can preserve the knowledge.
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

### My Notes

To download media materials stored on other servers, include the following options

* ``--span-hosts``: Allows recursion to go to other sites. Note this can be dangerous if not used with ``--domains``.
* ``--domains``: only span hosts in these domains. List should be comma separated with no spaces.
