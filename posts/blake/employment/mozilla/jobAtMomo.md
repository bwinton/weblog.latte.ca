<!--
.. title: My first couple of days at Mozilla Messaging.
.. date: 2009-07-07 00:04:20
.. author: Blake Winton
.. tags: work, mozilla, thunderbird, new_job
-->

A few weeks ago I started a new full-time contract at [Mozilla
Messaging](http://mozillamessaging.com/) (a.k.a. the people who brought you
Thunderbird).  I meant to post this on the Wednesday after I started, but
didn’t get around to it until now.  So, here you go, my notes from just
after I started a new job.

It has been a pretty crazy couple of days, both because I’m not that used
to working for a full 8 hours on one thing, and because I’m at the point
where there’s still so much to learn that I could spend all my time
researching stuff, and never get anything done.

But even with all the stuff for me to learn, I feel like I’ve made a fair
bit of progress.  There were a few bugs assigned to me, based on [a
previous patch](http://hg.mozilla.org/comm-central/rev/98a7de404c08), as
well as a couple of things left to do to get [the feature](
https://bugzilla.mozilla.org/show_bug.cgi?id=45715) working, so I jumped
right in to those.  After I had new patches up for review on all of those
bugs, I talked with [Bryan Clark](http://clarkbw.net/blog/) about what bugs
I should tackle next.  He and [David Ascher](http://ascher.ca/blog/) both
suggested that the new [automatic mail server config](
https://bugzilla.mozilla.org/show_bug.cgi?id=autoconfig) dialog could use a
bit of love.

This morning, I did some investigation on group email addresses for [one of
the bugs]( https://bugzilla.mozilla.org/show_bug.cgi?id=496440) I’m working
on, and took a look at how the autoconfig dialog was put together so that I
wouldn’t sound like I was completely lost in the meeting.  (XUL, CSS, and
Javascript.  No surprises there.  :)  Then, after the [Status
Meeting](https://wiki.mozilla.org/Thunderbird/StatusMeetings/2009-06-09),
Bryan and I chatted a bit about what the various bugs were that he had
assigned to me, and what sort of things I might look into to try and fix
them.  A few hours later, I had a fix for [one of them](
https://bugzilla.mozilla.org/show_bug.cgi?id=490105), and applied a similar
fix to [another](https://bugzilla.mozilla.org/show_bug.cgi?id=490106).  (As
an aside, you’ve got to love the 3 hour investigation which ends up being a
9-character change.  At least while investigating the bug, I learned a lot
about [hboxes](https://developer.mozilla.org/en/XUL/hbox), [vboxes](
https://developer.mozilla.org/en/XUL/vbox), [flexes](
https://developer.mozilla.org/en/XUL/Attribute/flex), [grids](
https://developer.mozilla.org/en/XUL/grid), and [descriptions](
https://developer.mozilla.org/en/XUL/description), which will hopefully
come in handy in future bugs.  :)  Finally, I ended the day by reading a
review of a patch I submitted on Monday morning, making some tweaks to my
code, and resubmitting it.

The final thing that amazes me is that each day is taking up pretty much a
full page of my log book, which is _way_ more than usual.  Most of the days
last month got a line or two.  Really full days would maybe get half a
page.  But yesterday and today were a solid page, chock full of
information, each.  I wonder how long this trend will continue.  I hope it
keeps on going like this for a long time.

