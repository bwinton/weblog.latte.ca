<!--
.. title: More notes on Mercurial.
.. date: 2009-09-21 11:48:34
.. author: Blake Winton
.. tags: mercurial, hg, mq, pbranch, work, mozilla
-->

Recently, I made some changes to [my work flow](
http://weblog.latte.ca/blake/tech/thunderbird/mercurial) to get around
some slight annoyances.  Specifically, I switched from using [mq](
http://mercurial.selenic.com/wiki/MqExtension) to using [pbranch](
http://arrenbrecht.ch/mercurial/pbranch/).  The features that pbranch
gives me that mq didn’t basically boil down to two main things;
sharing, and tracking.

With pbranch, it’s way easier for me to share my changes, both with
other people, and with myself in a virtual machine.  It _is_ possible
to share the patch with mq, by cloning the patch repo if I remembered
to run qinit -C, but with pbranch all I have to do is clone the main
repo, and my changes are right there, waiting for me.

For tracking, when I’m nearing the end of a patch, and it mostly
works, I get really nervous if I can’t check in my changes.  With mq,
I set up an alias to let me commit the patch queue, so that I could go
back, but it was really hard to tell what I had changed between any
two commits, since it was showing me the diff of my diffs.  And so I
didn’t use it as much as I would like to.  With pbranch, I just commit
the code, like I want to, and it keeps track of what the patch should
look like.

So, my day-to-day workflow now looks more like this:<br/>
If I’m working on a bug that I’ve already got a patch started for, I
cd to the appropriate branch, type <tt>hg pgraph</tt> to see where I
am, and <tt>hq update branchname</tt> to get to the pbranch I want to
work on.  Then I make my changes, and when I’m happy with the results
of <tt>hg diff</tt>, I type <tt>hg commit</tt> to put the changes into
the pbranch.  After that, I use <tt>hg pdiff &gt;
../branch-name-bugnum-description.diff</tt> to get a patch that I can
upload to bugzilla.  At this point, I usually load the patch into Vim,
and search for some of the mistakes I’ve made in the past.
(<tt>/^+.*[[:space:]]\+$</tt>, and <tt>/dump</tt> caught a lot of my
initial mistakes.  Now I’ve moved on to things that are tougher to
check for, like putting open-parens on a new line instead of on the
previous line.)  I usually go through a couple of cycles of <tt>hg
commit</tt>/<tt>hg pdiff …</tt> before I’m happy with the patch.  Once
I am, I don’t have to type anything before I upload it, since it’s
already committed.

