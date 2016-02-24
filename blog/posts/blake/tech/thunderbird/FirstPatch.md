<!--
.. title: Hurray!  (A technical diversion.)
.. date: 2009-05-29 10:25:41
.. author: Blake Winton
.. tags: thunderbird, mozilla, hg, patch
-->

It took a while, but my [first patch to Thunderbird](
http://hg.mozilla.org/comm-central/rev/98a7de404c08) was committed today!

    changeset:   2727:98a7de404c08
    user:        Blake Winton <bwinton@latte.ca>
    date:        Fri May 29 10:35:37 2009 +0100
    summary:     Bug 45715 - ""Reply to List" [button/(context) menu item]"
                 [r=mkmelin,sr=bienvenu,ui-review=clarkbw]

The patch started off by adding a “Reply to List” button to the message
header pane as seen below, but after some discussion, the scope was
expanded to change the “Reply” button to “Reply All” or “Reply to List”,
depending on the message you’re currently viewing.

![First cut of the Reply to List button](
https://bug45715.bugzilla.mozilla.org/attachment.cgi?id=364625 "Reply to
List")

Of course, there’s still some things I’ve got to add, but those can go in a
separate patch, which will be much smaller, and so much easier to get
reviewed and committed.  And once it is, we might be able to close a
[9-year old bug]( https://bugzilla.mozilla.org/show_bug.cgi?id=45715),
which would be pretty sweet.

