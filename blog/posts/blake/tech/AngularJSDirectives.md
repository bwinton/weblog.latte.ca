<!--
.. title: Angular JS Directives <small>by Alex Vanston</small>.
.. date: 2013-10-12 17:07:52
.. author: Blake Winton
-->

I’ve recently been playing a lot of [Fez](http://www.fezgame.com/), a 2-D
(kinda) platforming/puzzle video game.  Many of the puzzles use a series of
symbols in squares as a [code language](http://evilwallpaper.co.uk/fez/).  I
really liked the way the language looked, and so I decided to write a small
single page app in Angular to transliterate English into the Fezish alphabet.
The first implementation was written as a filter, and it seemed to work okay,
but emitting a bunch of HTML and then forcing the user of the filter to use a
sanitizer to get it to render _as_ HTML was kinda strange. That very same day,
in an odd twist of fate, I got some email from [Packt
Publishing](http://www.packtpub.com/) asking if I would be interested in
featuring their [new Angular JS book](http://bit.ly/13VlkXc) on my blog.  Long
story short, I agreed to post a review of it here in exchange for a free copy
of the eBook.  So on to the review…

The first thing that struck me about Angular JS Directives was the writing.
I’ve read a lot of extremely dry technical books which were hard to get
through, and I’m happy to say that this is _not_ one of them.  I found the
writing both engaging and amusing.  There are a few times where the author
even pokes fun at himself for repeating the same points, which was wonderful
to see.  The examples were clear to read, and ably demonstrated the points
that the accompanying text was making.  The overall flow of the book mostly
made sense, with simpler concepts leading to more complicated concepts.  My
only suggestion is that the chapter on Testing could have been introduced
sooner, and then used in the rest of the examples to prove things were working
the way that the author claimed.

I don’t like to only say positive things about something I’m reviewing, both
because I believe that there’s always something that could be done better, and
because I don’t want to look like a corporate shill.  At least not for $17.
;)  So, on to the bad things I’ve run into.  It took me a lot longer to read
than I would have hoped.  This was partially because of a bunch of work stuff
taking up all my spare time, but also because after every few pages I wanted
to go back and re-write large parts of the projects I’ve done.  :)  My other
concern is that $17 for 87 pages of content might not not be worth it to you.
I found the content very useful, and I’ve certainly gotten $17 worth of
knowledge out of it, but at my previous job, where I didn’t use any JavaScript
much less Angular, it wouldn’t have been money well spent.

Having said all that, after the fourth chapter, I re-wrote the Fezish Filter
as a Directive, and the code became far cleaner.  And now that I’m done
reading the ninth chapter, I think I might spend the rest of this weekend
adding some unit and end-to-end tests.  So in the end, would I recommend [this
book](http://bit.ly/13VlkXc)? Yes.  Yes I would.

(Monday October 14th edit: I’ve also just been informed that Packt is running a
[Columbus Day sale](http://bit.ly/1bqvB29), and if you use the discount code
"**COL50**" in the next four days, you’ll get 50% off this, and any other eBook
or video, so if you’re thinking of buying it, today would be a great day to do
so!)

