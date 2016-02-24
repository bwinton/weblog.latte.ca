<!--
.. title: What the heck am I pushing, anyways?
.. date: 2011-12-08 13:04:17
.. author: Blake Winton
.. tags: git, outgoing, mozilla
-->

Much of the new work I’m doing these days is being stored in git
repositories.  Now, I’m not the biggest fan of git, particularly its UI,
but the advantages of [GitHub](https://github.com/) and [GitX](
http://gitx.frim.nl/) are hard to ignore.  Despite that, I still really
missed being able to type `hg out` to see which patches I would be pushing,
so, after a short chat with (and demo from) [Ben](
http://blog.mozilla.com/bhearsum/), I came up with the following:

Somewhere in your path, add a file named `git-outgoing` which contains the
following contents:

    # !/bin/sh
    # Uh, there shouldn’t be a space between the # and ! in the previous
    # line, but the highlighter I’m using seems to require it…
    git push --dry-run $1 2>&1 | awk '/^ / {print $1}' | xargs git log

(Make sure it’s executable by whomever needs to use it!)

Then, in your git config, add the following section:

    [alias]
        out = outgoing

And finally, you should be able to type `git out`, and see something like:

    commit 7d4c9b89a4663a07bed030669bae2d3c73ec78dc
    Author: Blake Winton <bwinton@latte.ca>
    Date:   Thu Dec 8 12:22:41 2011 -0500

        Blear 2

    commit a4e8c6627bc26d7371fb2614a1c47aaf694957bd
    Author: Blake Winton <bwinton@latte.ca>
    Date:   Thu Dec 8 12:18:04 2011 -0500

        Bleah.

So, hopefully some of the rest of you will find this helpful, too, and if you know of a better way to do this, *please* let me know in the comments!

