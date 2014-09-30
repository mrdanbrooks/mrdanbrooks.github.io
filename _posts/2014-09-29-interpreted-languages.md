---
layout: post
title: If python is interpreted, what are pyc files?
tags: python
category: programming
year: 2014
month: 9
day: 29
published: true
summary: A re-post of an excellent answer to this question posted on stack overflow.
---

Here is Alex Martelli's answer to the question, posted on [stackoverflow](http://stackoverflow.com/questions/2998215/if-python-is-interpreted-what-are-pyc-files) on June 8th, 2010.

-------------------------------------
> >    I've been given to understand that Python is an interpreted language...
>
> This popular meme is incorrect, or, rather, constructed upon a misunderstanding of (natural) language levels: a similar mistake would be to say "the Bible is a hardcover book". Let me explain that simile...
> 
> "The Bible" is "a book" in the sense of being a **class** of (actual, physical objects identified as) books; the books identified as "copies of the Bible" are supposed to have something fundamental in common (the contents, although even those can be in different languages, with different acceptable translations, levels of footnotes and other annotations) -- however, those books are perfectly well allowed to differ in a myriad of aspects that are not considered fundamental -- kind of binding, color of binding, font(s) used in the printing, illustrations if any, wide writable margins or not, numbers and kinds of builtin bookmarks, and so on, and so forth.
> 
> It's quite possible that a _typical_ printing of the Bible would indeed be in hardcover binding -- after all, it's a book that's typically meant to be read over and over, bookmarked at several places, thumbed through looking for given chapter-and-verse pointers, etc, etc, and a good hardcover binding can make a given copy last longer under such use. However, these are mundane (practical) issues that cannot be used to determine whether a given actual book object is a copy of the Bible or not: paperback printings are perfectly possible!
> 
> Similarly, Python is "a language" in the sense of defining a class of _language **implementations**_ which must all be similar in some fundamental respects (syntax, most semantics except those parts of those where they're explicitly allowed to differ) but are fully allowed to differ in just about every "implementation" detail -- including how they deal with the source files they're given, whether they compile the sources to some lower level forms (and, if so, which form -- and whether they save such compiled forms, to disk or elsewhere), how they execute said forms, and so forth.
> 
> The classical implementation, CPython, is often called just "Python" for short -- but it's just one of several production-quality implementations, side by side with Microsoft's IronPython (which compiles to CLR codes, i.e., ".NET"), Jython (which compiles to JVM codes), PyPy (which is written in Python itself and can compile to a huge variety of "back-end" forms including "just-in-time" generated machine language). They're all Python (=="implementations of the Python language") just like many superficially different book objects can all be Bibles (=="copies of The Bible").
> 
> If you're interested in CPython specifically: it compiles the source files into a Python-specific lower-level form (known as "bytecode"), does so automatically when needed (when there is no bytecode file corresponding to a source file, or the bytecode file is older than the source or compiled by a different Python version), usually saves the bytecode files to disk (to avoid recompiling them in the future). OTOH IronPython will typically compile to CLR codes (saving them to disk or not, depending) and Jython to JVM codes (saving them to disk or not -- it will use the .javac extension if it does save them).
> 
> These lower level forms are then executed by appropriate "virtual machines" also known as "interpreters" -- the CPython VM, the .Net runtime, the Java VM (aka JVM), as appropriate.
> 
> So, in this sense (what do typical implementations do), Python is an "interpreted language" if and only if C# and Java are: all of them have a typical implementation strategy of producing bytecode first, then executing it via a VM/interpreter.
> 
> More likely the focus is on how "heavy", slow, and high-ceremony the compilation process is. CPython is designed to compile as fast as possible, as lightweight as possible, with as little ceremony as feasible -- the compiler does very little error checking and optimization, so it can run fast and in small amounts of memory, which in turns lets it be run automatically and transparently whenever needed, without the user even needing to be aware that there is a compilation going on, most of the time. Java and C# typically accept more work during compilation (and therefore don't perform automatic compilation) in order to check errors more thoroughly and perform more optimizations. It's a continuum of gray scales, not a black or white situation, and it would be utterly arbitrary to put a threshold at some given level and say that only above that level you call it "compilation"!-)
> 
-------------------------------------
