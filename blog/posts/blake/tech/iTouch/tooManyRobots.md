<!--
.. title: Too many robots!  A newbie lesson about alertView:clickedButtonAtIndex:
.. date: 2009-03-23 21:55:30
.. author: Blake Winton
-->

(With thanks to [Bunnyhero](http://twitter.com/bunnyhero/), both for the
title, and the inspiration to get blogging again.)

As you can probably guess, if you’ve read Bunnyhero’s [blog post](
http://www.bunnyhero.org/2009/03/23/too-many-monkeys-a-newbie-lesson-about-viewdidload/
), I recently learned that the AlertView delegate method
<tt>alertView:clickedButtonAtIndex:</tt> can be called _multiple times
for one AlertView_, much to my surprise.

And here’s how I found that out.  A couple of weeks ago, I ran across a
bug in my still-in-development iPhone game.  I was displaying an alert
when the game ended, and when the user clicked “Okay” it would go to the
next level.  And it all seemed fine until one day, when instead of
clicking the “Okay” button, I hit the home button to exit the game while
the dialog was displayed, and the next time I entered the app, there
were, like, 40 robots where I was expecting 8!

As a favour to a [friend of mine](http://pyre.third-bit.com/blog/) who’s
a prof, I let the bug sit until I could debug the code in front of a
room full of undergrads, as a part of [the software engineering class](
https://stanley.cdf.toronto.edu/drproject/csc301-2009-01 ) he teaches.
(The whole experience turned out to not only be something that I wished
I could have seen when I was an undergrad, but also something really fun
to do from the the industry-type person side of things!  Anyone who has
a laptop, and some code with a small bug that they don’t mind showing to
a bunch of students should _really_ give it a try!).  Debugging the
problem led me not to the archiver/unarchiver as I was expecting, but
instead to the observation that when I hit the home button, my delegate
method was being called up to 5 times!

This is why I saw way too many robots, because I was advancing 4 more
levels than I should have been.  And so when I re-entered the game, it
happily put me on level 5-ish, instead of level 2.

The fix was fairly simple, if slightly inelegant.  I merely added in a
flag to tell me when I was handling an alert, and would only advance the
level when I thought I had popped the alert up.  (Now that I write it, I
wonder if I can set the alert’s delegate to nil when I’m done handling
it instead.  Thoughts, anyone?)

