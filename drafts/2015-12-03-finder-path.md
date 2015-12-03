---
layout: post
title: Show full path in Finder title bar
tags: osx 
category: systems
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
