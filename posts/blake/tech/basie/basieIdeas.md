<!--
.. title: Some ideas for the next version of Basie.
.. date: 2008-12-04 14:35:15
.. author: Blake Winton
.. tags: basie, presentation, ideas, 0.2
-->

Yesterday I went to see a presentation by Kosta Zabashta about the
work he did on Basie.  The presentation went fairly well, but while
listening to it, I had a few ideas that I thought I should write down.

First, since the configurations for Exim and Postfix are so
complicated and so different, it would be nice if we had a program
that could figure out which one you’re running, and generate the lines
to add to your config files to get it all set up.

Second, I think we probably don’t need to add that many boolean or set
operators to the search functionality.  I seem to remember reading a
paper a while ago where Google said that people only used 2 of the
advanced search features, "s to make a phrase, and OR to choose
between two different things.  Sure, some people used all the wacky
operators, but it was a vanishingly small percentage.

Third, do we update the search index when items change, or are we
constantly rebuilding it?  I would have thought that doing the dynamic
updates would have run into many of the same issues as the Events app,
but maybe there was a smarter way to do it that I’m overlooking.

Fourth, and finally, I wonder if there’s a way to use metadata about
the objects we’re searching to influence rankings.  To take the Google
approach, add the number of mail messages/commit logs/wiki
pages/tickets that refer to an item as a factor in determining the
ranking.  Or, push more recent things higher in the search results,
since we know when things were added.  Do we actually want to do
either of those?  Maybe, maybe not, but we’ve got a lot of data about
each item, and it seems like using it might be, well, maybe more
interesting than useful.  :)

So, there are my thoughts on stuff we might want to do for the next
version of Basie.  I suppose the next step will be to get Greg to link
to this, and get other people commenting.  (And now that I’ve written
it all out, I suppose it might have been cleverer to post this to the
Basie blog.  Ah well.  Live and learn.)

