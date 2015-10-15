---
layout: post
title: Debugging MacVim and GPG
tags: osx vim
category: random
year: 2015
month: 10
day: 15
published: true
summary: Debugging MacVim and GPG
---

Vim and GPG are among the tools I frequenty use.
For many years I have used the ``gnupg.vim`` plugin for editing gpg encrypted files.
Through carefully setup configuration files I have been able to use this setup on both Linux and Mac machines.
However, it has only ever worked when opening files from the terminal.
The strange thing was, it wasn't simply a matter of using regular ``vim`` vs ``GVim/MacVim``, because the graphical versions _would_ decrypt the files as long as they were invoked from the command line. 
Trying to open the same file using the same program, but invoked from gnome or finder would fail.

Today I finally decided to fix the problem.
The first step was to add the line ``let g:GPGDebugLevel = 5`` to my ``.vimrc`` file. 
I then tried opening an encrypted file from both the command line and from Finder.
This revealed that the GPG executable version being used was actually different.

It turns out I had two versions of GPG installed - the MacGPG2 tools suite and a version of gpg that was automatically installed as a dependency of something else from Macports.
During the installation of MacGPG2, it adds a file to ``/etc/paths.d`` that contains the path to it's binaries.
The ``/etc/paths.d/`` directory is then scaned by a tool called ``path_helper`` (see man path_helper) to build the path used by many different tools in the system, including GVim/MacVim.

When MacPorts installed, it edited the ``.profile`` file, adding its installation paths to the begining of the $PATH variable, which is set by the ``path_helper`` tool. 
Normally, this would mean that the MacPorts version would always be the default version since it was first on the path.
However, for some reason my iTerm2 setup was never executing the .profile file.
At some point along the line, I had added the MacPorts paths to the $PATH inside my .bashrc, but had appended them to the end instead of to the begining. 
This meant that the $PATH variable in my iTerm2 window was different from the $PATH everywhere else on the machine.

Editing the ``.profile`` file to rearrange the MacPorts paths fixed the problem, and allowed me to edit the encrypted files directly from Finder in OSX, but I still have a problem in Linux. 
But that will have to wait for another day.





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