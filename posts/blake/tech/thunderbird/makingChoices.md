<!--
.. title: Customization and choice.
.. date: 2011-06-15 10:13:58
.. author: Blake Winton
.. tags: design, ux, choice, mozilla
-->

A friend of mine recently
[said](https://twitter.com/eccentricflower/status/80817396696358913):

> EVERY behavior aspect of EVERY application should be user-settable if
> the user is prepared to drill down far enough. No exceptions.
> Even if the user will be shooting his own foot by messing with it.

I, obviously, disagree with him, and wanted to explain why in a few more
characters than Twitter would allow.

While giving the user complete control over every aspect of an application
seems like a good idea, there are two slightly-hidden downsides to it.

First, every choice you give the user doubles the amount of testing you
have to do.  (Okay, it doesn’t exactly double it, but it certainly adds a
testing, maintenance, and support burden.)  Is it a responsible use of your
time to implement these options if less than 1% of your users will ever
change them (and risk shooting their own feet), or would it be better for
everyone to implement a feature that more people would use?

Second, Emacs notwithstanding, you’ll never get to a great text editor by
customizing a mail reader.  The whole Unix (and iOS, oddly) philosophy is
to write each app to do one thing, and do it well.  Not to do a whole bunch
of optional things.  And if you’re doing only one thing, presenting an
option to the user to do it or not doesn’t make a lot of sense.

And finally, because I can’t count, if you offer people too much choice, it
imposes a cognitive burden on them which can lead to their making no
choices at all, or at least not making them any happier than when they had
fewer choices.

To bring this back to the product I’m working on, we are going out of our
way to make Thunderbird more usable and part of that is simplifying it by
offering fewer, more meaningful choices.

