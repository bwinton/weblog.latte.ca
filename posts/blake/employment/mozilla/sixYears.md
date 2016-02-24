<!--
.. title: A long time ago, on a computer far far away…
.. date: 2015-02-27 14:04
.. author: Blake Winton
.. tags: mozilla, thunderbird, employment, anniversary
-->

Six years ago, I started contributing to Mozilla.

<!-- TEASER_END -->

The startup I was working for ran out of money and everyone was let go, so
while I was doing some freelance work I found myself with some spare time
between tasks and thought I could use it, along with my programming skills, to
make the world (and my life) a little bit better.  You see, I had been using
email for around 16 years by that point, and during that time had accidentally
*twice* sent personal replies to mailing lists, because the mailing list
administrators had set the Reply-To header to point to the list instead of
leaving it pointing to the original person.  Fortunately both of them were
embarassing rather than catastrophic, but the sense of embarassment was acute
and remained with me for a long time.  Changing the Reply-To header in this
way is obviously wrong
([citation 1](http://www.unicom.com/pw/reply-to-harmful.html),
[citation 2](http://woozle.org/~neale/papers/reply-to-still-harmful.html) ;)
but one of the more common excuses I hear from mailing-list adminstrators is
that it makes it easier for people to reply to the list if the header is
changed.  To help counter that at <span title="2009-02-27 21:14">9:15pm (EST)
on February 27th, 2009</span>, I
[added a reply-to-list button](https://bugzilla.mozilla.org/show_bug.cgi?id=45715#c159)
to Thunderbird.<img align="right" style="margin: 5px"
src="https://dl.dropboxusercontent.com/u/2301433/Screenshots/ReplyButtons.png">
To be fair, all the back-end code to implement the feature
was already there, but the person who wrote those patches gave up on the
front-end because of UI-[bikeshedding](http://steelblue.bikeshed.org/).  I
remember thinking that if I added the button, even if it didn’t do the right
thing, then at least we would have something concrete to improve upon.

<span title="2009-02-27 21:29">Fourteen minutes later</span>, I posted
[the first patch](https://bugzilla.mozilla.org/show_bug.cgi?id=45715#c161)
(of twenty-four)!  I hope that it’s inspiring to novice programmers to realize
that even after 17 years of programming professionally it still took me 24
attempts to get a patch that was landable, not because I’m particularly
stupid, but because programming is difficult, and you need to stick with it to
get stuff done.

<img align="left" width="200px" style="margin: 5px"
src="https://dl.dropboxusercontent.com/u/2301433/Screenshots/AccountProvisioner/Providers2.png">
A little while after that, and perhaps in part because of the work I did with
other contributors on that bug, I was hired at Mozilla Messaging, to work on
Thunderbird’s front-end code.  First as a contractor and then later as a
full-time employee.  It was an exciting time, and I got to work with a lot of
amazing people on some interesting old bugs and new features.

It took <span title="2009-07-30 10:41">another five months</span> after that
patch before I got my first code into mozilla-central (the repository that
Firefox is built from).  I noticed that we had a bug in Thunderbird that was
[caused by a semicolon](https://bugzilla.mozilla.org/attachment.cgi?id=396438&action=diff#a/mailnews/base/prefs/content/accountcreation/createInBackend.js_sec2)
at the end of an if-statement, and I thought that if that kind of
easily-overlooked bug could creep into Thunderbird, it could probably creep
into Firefox, too.  So I searched through the code in mozilla-central, patched
the couple of occurrences that I found that could be a problem, and
[filed a bug](https://bugzilla.mozilla.org/show_bug.cgi?id=507386) letting
people know about the potential problems and the patch.  Soon thereafter the
bug got a very positive comment from none other than Brendan Eich, and after a
quick review by [Dietrich](https://twitter.com/dietrich), the patch was
landed.  Did it fix any visible problems?  After five years, I’m still not
sure, but the code definitely wasn’t doing what we thought it was, and now it
is, so I think it was a good fix.

<img align="right" width="200px" style="margin: 5px"
src="https://dl.dropboxusercontent.com/u/2301433/HeatmapDefaultPlus.png">
A couple of years later Mozilla Messaging was merged back into Mozilla
Corporation, and when we decided to transition Thunderbird to community-
leadership I took the opportunity to move over to the Firefox UX Team as a
Design Engineer, where I continue making tools, prototyping designs, and
helping the community to this day.  My journey with Mozilla has been a long
and enjoyable trip so far, and <span
title="even despite recent departures…  :)">I’m excited to see what the future
brings</span>!

*<span title="It’s about ethics in bugzilla history.">Addendum</span>* -
To be totally honest, that wasn’t actually my first bugzilla interaction.
<span title="2009-02-26 16:49">The day before</span> that I reported
[a crash in Shredder](https://bugzilla.mozilla.org/show_bug.cgi?id=480401)
(now known as “Daily”).  It turned out that it had been fixed
[about 24 hours earlier](http://hg.mozilla.org/comm-central/rev/9c3f21f04cf0).

<br clear="all">
