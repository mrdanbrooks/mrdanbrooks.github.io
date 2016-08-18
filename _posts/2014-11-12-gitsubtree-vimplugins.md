---
layout: post
title: Installing Vim Plugins using Git Subtrees
tags: vim programming
category: notes
year: 2014
month: 11
day: 12
published: true
summary: How to keep Vim plugins up to date using git subtrees
---

These instructions were based off of [this](http://blogs.atlassian.com/2013/05/alternatives-to-git-submodule-git-subtree/) blog post.

Go to the root directory of your dot files.

```
cd ~/.dan
```

Add the git repository of the plugin you want as a remote

```
git remote add someplugin https://github.com/someguy/someplugin.git
git subtree add --prefix .vim/bundle/someplugin someplugin master --squash
```

And to updated later

```
git subtree pull --prefix .vim/bundle/someplugin someplugin master --squash
```



Messing up
----------

If you screw up and do a `git fetch someplugin master`, here is how to undo it.

First, remove all branch references to the bad tree.

```
git remote remove someplugin
```

There may be tags - if you don't have any tags and all the tags belong to the bad tree kill them all like so

```
git tag | xargs git tag -d
```

Now when you look at `git lg` you should not see any of the bad commits.
To remove all these commits do the following

```
git reflog expire --all --expire-unreachable=0
git repack -A -d
git prune
```

And that should fix it
