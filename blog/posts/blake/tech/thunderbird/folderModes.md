<!--
.. title: How folder modes work.
.. date: 2009-12-20 16:45:00
.. author: Blake Winton
.. tags: mozilla
-->

Earlier today, I was asked by [Andreas Nilsson](
http://www.andreasn.se/blog/) to give him a hand with a [folder pane header
bug](https://bugzilla.mozilla.org/show_bug.cgi?id=535021) he was trying to
fix.  In the middle of digging around in the code, I thought “I should
really write this down, so that I can understand it later.”, and so here it
is.

The main place we’ll need to change is in [this object](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#55).

We start in the [<tt>load</tt>](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#60)
method, which calls [<tt>registerMode</tt>](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#67),
to add the mode with its localized name.  There is also a [default list of
modes](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#984),
which will come into play later.

When the user chooses to [cycle the mode](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#200),
it calls the [setter for <tt>mode</tt>](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#250),
passing it the modename, which comes from the <tt>_modeNames</tt> list
(which contains both the defaults and any newly-registered modes).  Then,
in the setter, if the mode is a default mode, it will fail [the if-test](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#254),
and get the localized name from the “bundle_messenger” string bundle.  If
it’s a newly-registered mode, they will have passed in a localized name
which we will have stored in [<tt>this._modeDisplayNames</tt>](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#178),
and so we will [use that](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#255).

The point of the bug is to switch the label-and-two-buttons to a dropdown
menu, so at this point I think we should start with an empty
<tt>menulist</tt> in the XUL, and in the <tt>load</tt> method add
<tt>menuitems</tt> corresponding to the values in the <tt>_modeNames</tt>
array.  Then, in the <tt>registerMode</tt> and [<tt>unregisterMode</tt>](
http://mxr.mozilla.org/comm-central/source/mail/base/content/folderPane.js#187)
methods, we should add and remove new menuitems, which I’m hoping will just
automatically show up in the dropdown.  Finally, we need to change the
setter for <tt>mode</tt> to not calculate the new name, but just select the
appropriate menuitem set the <tt>mode</tt> attribute on the
<tt>_treeElement</tt>, and call <tt>_rebuild()</tt>.  At that point, I
think we’re done, but only time will tell.

<small>Okay, so this was really posted on Dec 22<sup>nd</sup>, but I wanted
to back-date it so as not to bump Amy’s “Welcome” post off the top a mere
day after she posted it.</small>

