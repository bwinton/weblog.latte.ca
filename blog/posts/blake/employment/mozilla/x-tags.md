<!--
.. title: X-Tag: or how to cut your html in half by adding 28 lines of Javascript…
.. date: 2012-07-12 21:39:32
.. author: Blake Winton
.. tags: xtag, mozilla, html
-->

 As a side-project, I’ve been working on a prototype which is heavily based on
[a demo page](
https://people.mozilla.com/~bwinton/australis-customization/customizationMode-liveDemo-i02.html
) from Stephen Horlander.  Now, that page is
pretty amazing, but if you look at the source (using command-u or control-u in
Firefox, and command-alt-u or control-alt-u in Chrome), you’ll see a lot of code
that looks like this:

    <div class="menuPanelButton subscribeButton">
      <div class="button"></div>
      <div class="label">Subscribe</div>
    </div>

and:

    <div class="customizeToolbarItem">
      <div class="customizeToolbarItemIcon share"></div>
      <div class="customizeToolbarItemLabel">Share</div>
    </div>

Now, one or two of those would be fine, but when we get into more than that, the
repetition really starts to bug me, and I think “Wouldn’t it be better if I
could just write stuff like:

    <panel-button type="subscribe">Subscribe</panel-button>
    …
    <toolbar-item type="share">Share</toolbar-item>

instead?”  And it turns out I can, using a new library called
[x-tag](http://mozilla.github.com/x-tag/)!  The first thing I need to do is
register the new tags I’ll be using.  That’s done with code like this:

    :::javascript
    // These first two lines are here because I’m using require.js, which I’ll
    // talk about in a future blog post…
    define(function (require) {
      require(["jquery", "x-tag"], function($, xtag) {

        // And this is the meat of the functionality.
        // First, we’ll register the new "panel-button" tag.
        xtag.register("panel-button", {
          onCreate: function(){
            var self = $(this);
            // When the tag is first seen, make the innerHTML be this stuff below.
            self.html("<div class='menuPanelButton " + self.attr("type") + "'>" +
                        "<img src='images/button-" + self.attr("type") + ".png'" +
                        "     class='button'>" +
                        "<div class='label'>" + self.text() + "</div>" + 
                      "</div>");
          },
        });

        // And then, we’ll register the new "toolbar-item" tag.
        xtag.register("toolbar-item", {
          onCreate: function(){
            var self = $(this);
            // We could also replace this element with the html below, but I
            // haven’t done that here because I haven’t needed to yet.
            self.html("<div class='customizeToolbarItem'>" +
                        "<div class='customizeToolbarItemIcon " + (self.attr("type") || "") + "'></div>" +
                        "<div class='customizeToolbarItemLabel'>" + self.text() + "</div>" +
                      "</div>");
          },
        });

      });
    });

The second step is to replace all the old html with the new tags.  (I did
that, too, of course.)  And there we go.  That’s it.  In the file I was
modifying, the combination of that and moving the javascript out into a
separate file took the html from 275 lines down to 146 lines, and let me more
easily change the buttons around, and add new ones.  I call that a win, and
from now on, whenever I see large blocks of repeated html, I’m going to be
seriously tempted to switch them to an x-tag!

One caveat I will mention is that in my first attempt, I tried to use both the
`content` property, and the `onCreate` method, and that totally didn’t work,
since the content would be replaced by the value of the content property long
before I had a chance to muck around with it in the onCreate.  So in the future,
I think I’ll just jump straight into using the onCreate method, since it’s not
that much harder.

