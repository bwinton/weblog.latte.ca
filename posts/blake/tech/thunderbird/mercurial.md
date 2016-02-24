<!--
.. title: How I use Mercurial (and the MQ extension).
.. date: 2009-06-30 22:31:48
.. author: Blake Winton
.. tags: mercurial, hg, mq, work, mozilla
-->

I started working for [Mozilla Messaging](http://www.mozillamessaging.com) a
while ago, and since [David Wolever](http://blog.codekills.net/) [asked
me](http://twitter.com/wolever/status/2394705659) how I used Mercurial and the
MQ extension, I thought I would put up some notes on how I’m currently using
them in my day-to-day work.  Of course, the stuff I’m doing now is a little
different than what I’ve done in any of my previous jobs, so I’m not sure how
useful any of the following will be to anyone who isn’t contributing to an open
source project.

First, let’s talk a little bit about how I have my Work directory set up.  The
first thing I did when I started working on the Thunderbird source code was to
pull down a clean copy of the source into a directory named “src-base”.  The
purpose of that directory is to always contain a clean copy of the upstream
source code so that when I want to update the various branches I have (five, at
last count), I only need to download the changes from the Mozilla repo once,
and I can then propagate them from src-base to the other branches.  I got the
idea to do that from the Bazaar-NG developers, and I think it has helped to
keep my bandwidth usage down.  It might cause a problem if I was sharing my
branches, but since Thunderbird seems to revolve around submitting patches to
bugzilla, it works out pretty well.

The next thing I did was to clone src-base into a directory named
“add-reply-list-button” (because I was writing a patch to add a Reply-To-List
button :), go into that directory, and type <tt>hg qinit -c</tt> to create an
mq repository, and put the mq repository itself under version control.  (I
didn’t actually do that the first time, and was quite annoyed that I couldn’t
revert changes I had made in my patch queue.)  The other part of that is that
I’ve aliased <tt>mq</tt> to <tt>hg -R $(hg root)/.hg/patches</tt>.  This lets
me type <tt>mq commit</tt> to commit the changes to the patch.

So, now we’re at my day-to-day work.  If I’m working on a bug that I’ve already
got a patch started for, I cd to the appropriate branch, type <tt>hg
qseries</tt> to see where I am, and <tt>hq qpush</tt> or <tt>hg qpop</tt> to
get to the patch I want to work on.  Then I make my changes, and when I’m happy
with the results of <tt>hg diff</tt>, I type <tt>hg qrefresh</tt> to put the
changes into the patch.  After that, I use <tt>hg qdiff &gt;
../branch-name-bugnum-description.diff</tt> to get a patch that I can upload to
bugzilla.  At this point, I usually load the patch into Vim, and search for
some of the mistakes I’ve made in the past.  (<tt>/^+.*[[:space:]]\+$</tt>, and
<tt>/dump</tt> caught a lot of my initial mistakes.  Now I’ve moved on to
things that are tougher to check for, like putting open-parens on a new line
instead of on the previous line.)  I usually go through a couple of cycles of
<tt>hg qrefresh</tt>/<tt>hg qdiff …</tt> before I’m happy with the patch.  Once
I am, I type <tt>mq commit -m "Updated patch to fix foo and bar."</tt> to save
the state of the patch, and then I upload it.

