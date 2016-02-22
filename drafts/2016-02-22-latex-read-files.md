---
layout: post
title: Reading all tex files in a directory
tags: linux
category: random
year: 2016
month: 02
day: 22
published: true
summary: How to read all the tex files in a directory
---

There are some things latex sucks at, and one of those things is reading in lists of files. 
The bottom line is, it can't.
Instead, you have to make use of the operating system or shell environment to do so.
AND to make things even more frustrating, it doesn't even like you to be able to do that much, so the functionality is disabled by default.

Below I've outlined two different methods that work to read all the .tex files from a directory and include their source in the output.
However, to actually make this code work, you need to compile using ``--shell-escape`` like so:

```
$ pdflatex --shell-escape main.tex
```

Typically, I use the ``rubber`` command to compile my latex because it is easier to use.
Unfortunately, up until rubber 1.2 you could not compile using ``--shell-escape``. 
I don't have any machines that can run the updated version of rubber, but if you do, this is how you would have to call it:

```
$ rubber -c 'setlist arguments --shell-escape' --pdf --warn all main.tex
```

Below are the two methods of including all the tex files in a directory in your document build.

### Method 1

The first method involves reading all the files in the directory and combining their contents into a "well named" file to read in all at once.

Add the following to your preamble.

```
\makeatletter
\def\app@exe{\immediate\write18}
\def\inputAllFiles#1{%
  \app@exe{ls #1/*.tex | xargs cat >> \jobname.tmp}%
  \InputIfFileExists{\jobname.tmp}{%
  }
  \AtEndDocument{\app@exe{rm -f #1/\jobname.tmp}}
  }
\makeatother
```

And call this later

```
\inputAllFiles{parts}
```

Credit: [](http://tex.stackexchange.com/a/166453)

### Method 2

This method uses unix pipes.

Put the following in your preamble:

```
\makeatletter

\@ifdefinable\@fileliststream{\newread\@fileliststream}
\@ifdefinable\@currentfilename{}
\newcommand*\InputAllFilesInSubfolder[1]{
  % #1 <- Path to subfolder: MUST end with the (operating system dependent) 
  %       character for separating path components.
  \openin\@fileliststream |"ls '#1'"\relax
  \loop \unless\ifeof\@fileliststream
    \begingroup
      \endlinechar \m@ne % cf. exercise 20.18
      \global\readline\@fileliststream to\@currentfilename
    \endgroup
    \ifx\@currentfilename\@empty \else
      \typeout{Inputting "#1\@currentfilename".}%
      \input{#1\@currentfilename}%
    \fi
  \repeat
  \closein\@fileliststream
}

\makeatother
```

and then call the function like so later on:

```
\InputAllFilesInSubfolder{parts/}
```

Note that you need the trailing / in this version.
Credit: [](http://tex.stackexchange.com/a/249739)

----------------------------------------

To use this template:
=====================

 - Make a copy
 - Change the file name
 - Update the header info
 - change published to `true'
 - Delete these quick notes!

Add a tag!
----------

Its fast and easy!

Just go to `~/Source/notes/tags/` and add a file.md with the following content

```
---
layout: blog_by_tag
title: <tagnamegoeshere> posts
tag: <tagnamegoeshere>
permalink: <tagnamegoeshere>/
---
```

Don't forget to add the tag file when you commit!

Formatting
----------
 *  _Italic_
 *  **bold**
 *  `FixedSpace`
 *  Abbreviations <abbr title="HYPER TEXT MARKUP">HTML</abbr>
 *  <del>Deleted</del> and <ins>Inserted</ins>
 *  Super<sup>script</sup> and Sub<sub>script</sub>

Links
-----
 *  [External Links](www.google.com)
 *  [Post Links]({% post_url 2014-09-04-udev-usb-mounting %})
 *  [Static internal Links](/about/) would go to weaselpipe.com/about/.
 *  [Reference Style Links][google] 

[google]: http://www.google.com/ "This is google"

Quoting Text
------------

> Curabitur blandit tempus porttitor. 
> Nullam quis risus eget urna mollis ornare vel eu leo. 
> > Nullam id dolor id nibh ultricies vehicula ut id elit.

Example Text
------------

Cum sociis natoque penatibus et magnis <a href="#">dis parturient montes</a>, nascetur ridiculus mus. *Aenean eu leo quam.* Pellentesque ornare sem lacinia quam venenatis vestibulum. Sed posuere consectetur est at lobortis. Cras mattis consectetur purus sit amet fermentum.

> Curabitur blandit tempus porttitor. Nullam quis risus eget urna mollis ornare vel eu leo. Nullam id dolor id nibh ultricies vehicula ut id elit.

Etiam porta **sem malesuada magna** mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.

{% highlight js %}
// Example can be run directly in your JavaScript console

// Create a function that takes two arguments and returns the sum of those arguments
var adder = new Function("a", "b", "return a + b");

// Call the function
adder(2, 6);
// > 8
{% endhighlight %}

### Lists

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean lacinia bibendum nulla sed consectetur. Etiam porta sem malesuada magna mollis euismod. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.

* Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
* Donec id elit non mi porta gravida at eget metus.
* Nulla vitae elit libero, a pharetra augue.

Donec ullamcorper nulla non metus auctor fringilla. Nulla vitae elit libero, a pharetra augue.

1. Vestibulum id ligula porta felis euismod semper.
2. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
3. Maecenas sed diam eget risus varius blandit sit amet non magna.

Cras mattis consectetur purus sit amet fermentum. Sed posuere consectetur est at lobortis.

<dl>
  <dt>HyperText Markup Language (HTML)</dt>
  <dd>The language used to describe and define the content of a Web page</dd>

  <dt>Cascading Style Sheets (CSS)</dt>
  <dd>Used to describe the appearance of Web content</dd>

  <dt>JavaScript (JS)</dt>
  <dd>The programming language used to build advanced Web sites and applications</dd>
</dl>

Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Nullam quis risus eget urna mollis ornare vel eu leo.

### Images

Quisque consequat sapien eget quam rhoncus, sit amet laoreet diam tempus. Aliquam aliquam metus erat, a pulvinar turpis suscipit at.

![placeholder](http://placehold.it/800x400 "Large example image")
![placeholder](http://placehold.it/400x200 "Medium example image")
![placeholder](http://placehold.it/200x200 "Small example image")

### Tables

Aenean lacinia bibendum nulla sed consectetur. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Upvotes</th>
      <th>Downvotes</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td>Totals</td>
      <td>21</td>
      <td>23</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Charlie</td>
      <td>7</td>
      <td>9</td>
    </tr>
  </tbody>
</table>

Nullam id dolor id nibh ultricies vehicula ut id elit. Sed posuere consectetur est at lobortis. Nullam quis risus eget urna mollis ornare vel eu leo.

-----

Want to see something else added? <a href="https://github.com/poole/poole/issues/new">Open an issue.</a>
