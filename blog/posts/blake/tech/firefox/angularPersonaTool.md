<!--
.. title: Using Persona in Angular apps.
.. date: 2013-06-28 15:16:50
.. author: Blake Winton
.. tags: persona, angular, mozilla
-->

In my [previous blog post](
http://weblog.latte.ca/blake/tech/firefox/cssLines.html), I mentioned a tool
I’m writing to make it easy for designers to link mockups to live bugs.  But I
didn’t mention that I had a reasonably-working version of the tool written in
[Backbone](http://backbonejs.org/) which I’ve decided to port to [Angular](
http://angularjs.org/).  The reasons why are largely beside the point of this
blog post, but I’ll try to sum them up by saying that I reached a point where
Backbone seemed to be confusing me more than helping me, and Angular got a
_lot_ of good press at [FluentConf](http://fluentconf.com/fluent2013) this
year.

So this morning’s task in [the re-write](
https://github.com/bwinton/arewecreatingyet/commits/feature/angular) was to
re-hook up the [Persona](https://login.persona.org/about) integration.  I had
read recently that when you had a lot of dom-manipulation functions, you should
probably put that code in a directive, and since I hadn’t written an Angular
directive yet, I figured this would be a great time to learn how.  Writing [the
html](
https://github.com/bwinton/arewecreatingyet/blob/feature/angular/views/index.html#L30)
was pretty easy, of course, and most of the code from the existing
implementation (which was largely based on the code from the [express-persona
readme](https://github.com/jbuck/express-persona/blob/master/README.md)) could
be ported over fairly quickly.  The only tricky part I ran into was figuring
out that I needed to include [`restrict: 'E'`](
https://github.com/bwinton/angular-tools/blob/master/persona.js#L36) in the
[Directive Definition Object](
http://docs.angularjs.org/guide/directive#directivedefinitionobject).  After I
was done, I noticed that there really wasn’t that much in the code that had
anything to do with the tool I’m writing, and thus I pulled it out into a
separate repo so that other people can use it.

And with that, I announce [Angular-Tools](
https://github.com/bwinton/angular-tools/), a repo containing one or more tools
which you might find useful if you build Angular apps.  As always, pull
requests and bug reports welcome!

