<!--
.. title: Who should review my change?
.. date: 2011-06-01 20:13:37
.. author: Blake Winton
.. tags: mozilla, thunderbird, review
-->

One of the big questions I had when I started writing patches was who I
should ask to review them.  Now that I’ve been in the community for a
while, I’ve got a much better sense of who I should be talking to for the
type of things I’m likely to write, but there are still times when I want
to make a change in a part of the code that I haven’t touched before, and
I’m not sure who to ask.  In those cases, I usually fall back to a fairly
simple (if non-obvious) set of steps to try and figure out who to pick.

1. Get the list of files I’ve changed.
2. Get the hg log for those files.
3. Check through the log for “r=”, and “sr=”.

Of course, that’s a fairly easy set of steps to automate, and so I present
my first cut at [the automated reviewer chooser](
https://github.com/bwinton/Mozilla-Tools/blob/master/getReviewer.py)!

Of course, there are a lot of things I’ld like to do with this, such as:

* Improving the documentation.
* Checking to see how well this script would have done on previous commits.
* Taking into account the length of the queues for the reviewers.
* Adding some sort of recent-ness calculations.

But I think that this tool is useful enough in its current state that
releasing it and getting feedback on what to actually work on would be a
win.

To use it, be in a mercurial source repo, and type `getReviewer.py` to get
a list of suggested reviewers for the current differences, or
`getReviewer.py temp.diff` or `getReviewer.py
https://bugzilla.mozilla.org/attachment.cgi\?id\=536017` to specify a
different set of changes.

