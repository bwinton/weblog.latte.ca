<!--
.. title: Requiring jQuery UI.
.. date: 2012-07-08 18:14:31
.. author: Blake Winton
.. tags: requirejs, jquery-ui, mozilla
-->

Yesterday afternoon, I watched [a video](https://air.mozilla.org/apps-templates-dev-ecosystem-tools/) from [James Long](https://twitter.com/jlongster) about [Mortar](https://github.com/mozilla/mortar), which is a template for making HTML 5 Open Web Apps.  Now, coincidentally, I’m starting a new project (in my spare time, obviously, since it’s a Sunday), and while it’s not an Open Web App, I saw no reason not to use the [same](https://github.com/volojs/volo) [tools](http://requirejs.org/) they were using.

Of course, since nothing’s easy, I ran into a problem pretty quickly.  My problem was that every time I tried to `require("jquery-ui");`, I got an error of “ReferenceError: jQuery is not defined”.  There wasn’t a lot of information about how to fix it, so after most of an afternoon mucking around, I finally came up with something that seems to work, and thought I would post it.

1. Go into your `www/js/lib` directory.
2. `curl -O https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.js`
3. Edit the jquery-ui.js file.  At the top add the line `define(["jquery"], function (jQuery) {`, and at the bottom, add the line `});`.
4. That’s it.  From there you should be good to go!

Now, I suspect there’s a better way to do this, and hopefully [James](https://twitter.com/jrburke) or [Bryan](https://twitter.com/clarkbw) will jump in the comments and tell me what it is, but for now, at least this works.
