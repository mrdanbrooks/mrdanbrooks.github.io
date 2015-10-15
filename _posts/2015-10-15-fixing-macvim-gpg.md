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
For many years I have used the ``gnupg.vim`` plugin for editing GPG encrypted files.
Through carefully setup configuration files I have been able to use this setup on both Linux and Mac machines.
However, it has only ever worked when opening files from the terminal.
The strange thing was it wasn't simply a matter of using regular ``vim`` vs ``GVim/MacVim``, because the graphical versions _would_ decrypt the files as long as they were invoked from the command line. 
Trying to open the same file using the same program, but invoked from Gnome or Finder would fail.

Today I finally decided to fix the problem.
The first step was to add the line ``let g:GPGDebugLevel = 5`` to my ``.vimrc`` file. 
I then tried opening an encrypted file using MacVim from both the command line and from Finder.
This revealed that the GPG executable version being used was actually different.
Below is an example of the output from one of the versions.

```
GnuPG: >>>>>>>> Entering s:GPGInit()
GnuPG: gnupg.vim $Revision: 3026 $
GnuPG: shellredirsave: >%s 2>&1
GnuPG: shellsave: /bin/bash
GnuPG: shell: /bin/sh
GnuPG: shellcmdflag: -c
GnuPG: shellxquote:
GnuPG: shellredir: >%s 2>&1
GnuPG: stderrredirnull: 2>/dev/null
GnuPG: shell implementation: /bin/sh
GnuPG: command: LANG=C LC_ALL=C /usr/local/bin/gpg --no-use-agent --version
GnuPG: output: gpg: WARNING: "--no-use-agent" is an obsolete option - it has no effect^@gpg (GnuPG/MacGPG2)
 2.0.28^@libgcrypt 1.6.3^@Copyright (C) 2015 Free Software Foundation, Inc.^@License GPLv3+: GNU GPL versio
n 3 or later <http://gnu.org/licenses/gpl.html>^@This is free software: you are free to change and redistri
bute it.^@There is NO WARRANTY, to the extent permitted by law.^@^@Home: ~/.gnupg^@Supported algorithms:^@P
ubkey: RSA, RSA, RSA, ELG, DSA^@Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,^@
 CAMELLIA128, CAMELLIA192, CAMELLIA256^@Hash: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224^@Compres
sion: Uncompressed, ZIP, ZLIB, BZIP2^@
GnuPG: public key algorithms: RSA, RSA, RSA, ELG, DSA
GnuPG: cipher algorithms: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
GnuPG: hashing algorithms: MD5, SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
GnuPG: compression algorithms: Uncompressed, ZIP, ZLIB, BZIP2
"~/secret.asc" [noeol][converted] 2L, 310C
GnuPG: >>>>>>>> Entering s:GPGDecrypt()
GnuPG: command: LANG=C LC_ALL=C /usr/local/bin/gpg --no-use-agent --verbose --decrypt --list-only --dry-run
 --batch --no-use-agent --logger-fd 1 "/Users/someguy/secret.asc"
GnuPG: output: gpg: WARNING: "--no-use-agent" is an obsolete option - it has no effect^@gpg: WARNING: "--no
-use-agent" is an obsolete option - it has no effect^@gpg: CAST5 encrypted data^@gpg: encrypted with 1 pass
phrase^@
GnuPG: this file is symmetric encrypted
GnuPG: cipher-algo is CAST5
GnuPG: decrypting file
GnuPG: command: '[,']!LANG=C LC_ALL=C /usr/local/bin/gpg --no-use-agent --quiet --decrypt 2>/dev/null
```

It turns out I had two versions of GPG installed - the MacGPG2 tools suite and a version of GPG that was automatically installed as a dependency of something else from MacPorts.
During the installation of MacGPG2, it adds a file to ``/etc/paths.d/`` that contains the path to it's binaries.
The ``/etc/paths.d/`` directory is then scaned by a tool called ``path_helper`` (see man path_helper) to build the path used by many different tools in the system, including GVim/MacVim.

When MacPorts installed, instead of doing something similar it edited the ``.profile`` file, adding its installation paths to the begining of the $PATH variable (which was set by the ``path_helper`` tool). 
Normally, this would mean that the MacPorts version would always be the default version since it was first on the path.
But the path was somehow being set inconsistently, since in some cases the MacGPG2 version was being detected.

It turns out that my iTerm2 setup was never executing the .profile file.
At some point along the line, I had added the MacPorts paths to the $PATH inside my .bashrc, but had appended them to the end instead of to the begining. 
This meant that the $PATH variable in my iTerm2 window was different from the $PATH everywhere else on the machine, including the built-in Terminal.app.

Editing the ``.profile`` file to rearrange the MacPorts paths fixed the problem, and allowed me to edit the encrypted files directly from Finder in OSX, but I still have a problem in Linux. 
But that will have to wait for another day.



