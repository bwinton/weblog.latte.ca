<!--
.. title: Thunderbird’s UI Directions.
.. date: 2011-09-27 11:02:38
.. author: Blake Winton
.. tags: thunderbird, ui, future, mozilla
-->

<link rel="stylesheet" type="text/css" href="bugzilla.css"></link>
<script type="text/javascript" src="bugzilla.js"></script>

On a [previous post](
http://breakingtheegg.tumblr.com/post/10525122364/cooking-up-some-tabs-on-top-for-thunderbird
) in a different blog, some commenters were asking us if we were
considering doing things that we have planned to do for a while now, and
that led me to realize that I haven’t been communicating the future of
Thunderbird’s UI nearly well enough.  I mainly blame it on my trying to do
too many other things, and thus failing to cover all the bases.  So, having
said all that, here is the list of things, in no particular order, that I
would like to see worked on in the next few versions of Thunderbird.  But
first, I’ld like to say a little bit about why I want them.

I recently heard about someone who said “Thunderbird looks like iTunes”,
and while that’s rather complimentary given the amount of time Apple puts
into making things look good, it doesn’t really lead me to believe that
people can pick our product out of a screenshot.  And so one of the overall
goals is to make Thunderbird iconic.  You can always tell when a screenshot
is of Apple mail, based on the layout and the lack of colour, and Firefox
is similarly immediately recognizable because of the big circular back
button and smaller rectangular forward button.  Similarly, I’m hoping to
have Thunderbird look different to other apps, while still fitting in on
the platform, and maintaining a little consistency with Firefox.  Of
course, that’s not the only goal, nor even the main goal.  My main idea for
Thunderbird is to let you focus on the content that’s important to you, and
not be distracted by things you don’t care about.  Hopefully most of the
changes I talk about here will help that, and as a side benefit also help
to give us a more unique style.

* A simple thing that will make the product nicer to use is just to line
  things up.  We’re all over the place, and it should be fairly simple to
  make this better.  There are a couple of bugs that are related to this,
  and I suspect we could file a few more for various other parts.
  <div id="bug-667235"></div>
  <div id="bug-689543"></div>

* We want to put the tabs on top, because they let us put the compose and
  address book into tabs, while still having the appropriate toolbars.  (As
  well, having everything be a tab makes the application more consistent,
  as described in the next point.)
  <div id="bug-644169"></div>
  <div id="bug-449299"></div>
  <div id="bug-457270"></div>

* This leads into removing the standalone Compose and Address Book windows.
  You’ll still be able to open a window for those functions, but it will
  just be a regular window with a Compose or Address Book tab.  (No bugs
  for this yet.  Removals are sensitive things, and we want to get the
  replacement UI working well before we remove the existing UI.)

* We really want the Thunderbird button, so that we can hide the menus, and
  have less Glass on Windows, and make the most common actions easier to
  find and use.
  <div id="bug-650170"></div>

* But, to add that button, we first need to see what the most common menu
  items people use are, therefore we need Test Pilot.
  <div id="bug-679513"></div>

* We would like to add a HomeTab, to give people a personalized place to
  land when they start Thunderbird, or open a new window.
  <div id="bug-605652"></div>

* We would like to merge the Gloda bar and Quick Filter bar, cause duh.
  <div id="bug-667246"></div>

* Having two different settings locations is too confusing for me, let
  alone people who don’t care about the details of the product. We want to
  merge those into a single searchable place for all the settings, a la Mac
  System Prefs.
  <div id="bug-509397"></div>

* This next change is more a small, personal thing, rather than part of a
  grand plan.  It was originally suggested by [Mike Beltzner](
  http://beltzner.ca/mike/), and while I’ve had some time to work on it, I
  haven’t had enough to push it through to completion.  Basically, I’ld
  like to be able to order my email by date, while grouping it by subject.
  (This is different than threading, because I don’t care about which
  replies are to which messages.  I just want a single group for the
  subject, with the messages ordered by date within that group, and the
  groups ordered by the date of the most recent message.)  There’s no bug
  for this yet, but as mentioned, I started to write [an extension](
  http://hg.mozilla.org/users/bwinton_latte.ca/bmode/file/65d446ca2d54),
  before hitting some annoying bugs that made it hard.

* Compactify the header.  It’s really too big.  Well, that’s a bit of a
  lie.  What I really mean here is that we should move the buttons and
  their toolbar out of the header, to float just above it.  This would
  allow people to easily turn them off (by removing the entire toolbar),
  and for those of us who like to keep them, it would make them more
  visually distinct.  As an added bonus, in vertical mode, we could merge
  that toolbar with the other toolbars, to get something like [the
  pictures]( http://www.flickr.com/photos/asadotzler/6137086055/) of what
  Thunderbird could look like posted by [Asa Dotzler](
  http://weblogs.mozillazine.org/asa/).

* And finally, I think we should remove the Migration Assistant.  It was
  very useful in the 2.0⇒3.0 transition, but it’s been less and less useful
  as time goes on, and as people have moved more and more onto Thunderbird
  3, and 4, and 5…  (No bug for this one either, again, because removals
  are sensitive things.)

See <a href="" class="all-bugs">all the bugs</a> in one big list.

<small>Many thank-yous to [Alex Faaborg](
http://blog.mozilla.com/faaborg/), and [areweprettyyet](
http://www.areweprettyyet.com/) for the code to link the bugs, and the
basis of the styling to make them stand out.</small>

