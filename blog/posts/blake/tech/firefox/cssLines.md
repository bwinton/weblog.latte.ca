<!--
.. title: Drawing lines with CSS.
.. date: 2013-06-14 14:57:43
.. author: Blake Winton
.. tags: css, transform, pixel, line, mozilla
-->

One of the things I’m working on as part of my job[^1] at Mozilla is [a tool](
https://github.com/bwinton/arewecreatingyet) to make it easy for designers to
create mockups that are linked to live bugs, similar to the ones at [Are We
Pretty Yet](http://areweprettyyet.com/4/mainWindow/#).  Now, I’ve got the
background showing up, and the bugs overlayed on top of it, but as it stands,
I’m requiring the designers to draw the lines connecting the bugs to the
various areas in the mockup right on the mockup itself!  This is obviously a
fairly terrible idea, since it makes it much harder than it should to move
stuff around after the fact, and requires a ton of up-front planning when
creating the initial image.  But what are my other options?

I thought for a while about layering a canvas element over the mockup; it would
let me draw whatever shapes I wanted to, but passing the click events through
to the mockup seemed like it would be fairly annoying, and I don’t think the
connecting lines should appear in front of the boxes showing the bug details,
which adds another wrinkle.  Then, over lunch, I started to wonder what it
would look like if a 1px by 1px black square got stretched and rotated with
CSS…  So I took some time after lunch, and played around a little, and it seems
like it just might work!  [Give it a try](http://jsfiddle.net/aBjp7/8/), let me
know if you have any ideas to make it better, and feel free to take the idea
anywhere you think it might be useful!

**Update:** In the comments, Andrew points out that I could use a 1px by 1px
span instead, which would make it _much_ easier to change the colour of the
line, so I’ve linked to his jsfiddle instead.  :)

[^1]: Sometimes I still can’t believe how lucky I am to get to do this stuff all day, and get paid for it!

