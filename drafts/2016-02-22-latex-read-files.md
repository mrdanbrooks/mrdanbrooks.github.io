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
\def\inputAllFiles#1{
  \app@exe{ls #1/*.tex | xargs cat >> \jobname.tmp}
  \InputIfFileExists{\jobname.tmp}{
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
      \typeout{Inputting "#1\@currentfilename".}
      \input{#1\@currentfilename}
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
