<!--
.. title: Cleaning out your Firefox profile.
.. date: 2012-11-23 13:42:09
.. author: Blake Winton
.. tags: firefox, profile, cleaning, faster, mozilla
-->

For a while now, I’ve been having problems with my Firefox profile.  To be fair,
it’s mostly because of random [about:config](about:config) tweaks I’ve made, but
still, not being able to test the [new SocialAPI](
https://blog.mozilla.org/blog/2012/11/20/firefox-introduces-new-social-api-and-previews-integration-with-facebook/
) stuff was pretty annoying.  So I decided to try [resetting my profile](
http://support.mozilla.org/en-US/kb/reset-firefox-easily-fix-most-problems),
to clear out all the junk, and hopefully even make it a little faster.

But, as the page I linked to just up there mentions, resetting your profile will
lose your open tabs, windows and tab groups, which kinda sucks, because I have
57 open tabs, in various groups, and I really don’t want to lose them!
Fortunately, I’m a programmer, so I hacked on Firefox to get it to save and
restore my tabs, and now I’m a happy camper!

A couple of days later, one of my co-workers had some similar problems, and also
wanted to re-set his profile to try and fix them.  I hadn’t saved the results of
my hacking, so I had to re-create it for him from a combination of memory and
the documentation.  The new code I came up with looked something like this:

    :::javascript
    var x = gBrowser.tabs
    var rv = "var tabs = [\n"
    for (var i = 0; i < x.length; i++) {
      rv += '  "' + x[i].linkedBrowser.contentWindow.location + '",\n';
    }
    rv += '];\nfor (var i = 0; i < tabs.length; i++ ) {\n'
    rv += '  gBrowser.addTab(tabs[i]);\n}\n'

To run it, first open [about:config](about:config), and make sure the
`devtools.chrome.enabled` preference is set to `true` (double-click it if it
isn’t, and it should switch automatically), then go to the `Tools » Web
Developer » Scratchpad` menu item, which should open up a small new window with
some javascript comments in it.  While that window is focused, click on
`Environment » Browser`, to make sure that you’re running the code in the
browser’s chrome (instead of in the page’s content).  Paste the code in, and
click `Execute » Display`.

That should result in a bunch of code in grey surrounded by `/*` and `*/` that
looks like:

    :::javascript
    var tabs = [
    "http://weblog.latte.ca/blake",
    "http://breakingtheegg.tumblr.com/",
    ];
    for (var i = 0; i < tabs.length; i++ ) {
      gBrowser.addTab(tabs[i]);
    }

Copy that out of the scratchpad into your favourite editor, remove the `/*` and
`*/`, and run the profile reset.

Once you’re done resetting your profile, you’ll need to change the
`devtools.chrome.enabled` preference to `true` again, and then re-open the
Scratchpad, paste the new code you saved back in to it, click on the
`Execute » Run` menu item, and **shazam**!  All your tabs should be back
(although they won’t be in their original tab groups.  If anyone needs me to
figure out how to do that, just let me know, and I’ll give it a try).

