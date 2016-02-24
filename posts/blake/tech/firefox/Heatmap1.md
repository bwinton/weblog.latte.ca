<!--
.. title: Figuring out where things are in an image.
.. date: 2014-07-07 11:53:31
.. author: Blake Winton
.. tags: tributary, heatmap, mozilla
-->

People love [heatmaps](https://blog.mozilla.org/ux/2012/06/firefox-heatmap-study-2012-results-are-in/).

They’re a great way to show how much various UI elements are used in relation
to each other, and are much easier to read at a glance than a table of click-
counts would be.  They can also reveal hidden patterns of usage based on the
locations of elements, let us know if we’re focusing our efforts on the
correct elements, and tell us how effective our communication about new
features is.  Because they’re so useful, one of the things I am doing in my
new role is setting up the framework to provide our UX team with automatically
updating heatmaps for both Desktop and Android Firefox.
<!-- TEASER_END -->

Unfortunately, we can’t just wave our wands and have a heatmap magically
appear.  Creating them takes work, and one of the most tedious processes is
figuring out where each element starts and stops.  Even worse, we need to
repeat the process for each platform we’re planning on displaying. This is one
of the primary reasons we haven’t run a heatmap study since 2012.

In order to not spend all my time generating the heatmaps, I had to reduce the
effort involved in producing these visualizations.

Being a programmer, my first inclination was to [write a
program](https://github.com/bwinton/d3Experiments/blob/gh-pages/heatmap.scratchpad.js)
to calculate them, and that sort of worked for the first version of the
heatmap, but there were some difficulties.  To collect locations for all the
elements, we had to display all the elements.

![Firefox in the process of being customized](https://raw.githubusercontent.com/bwinton/d3Experiments/gh-pages/images/Darwin/HeatmapCustomize.png Firefox in the process of being customized.)

Customize mode (as shown above) was an obvious choice since it shows
everything you could click on almost by definition, but it led people to think
that we weren’t showing which elements were being clicked the most, but
instead which elements people customized the most.  So that was out.

Next we tried putting everything in the toolbar, or the menu, but those were a
little too cluttered even without leaving room for labels, and too wide (or
too tall, in the case of the menu).

![A shockingly busy toolbar](https://raw.githubusercontent.com/bwinton/d3Experiments/gh-pages/images/Darwin/HeatmapToolbar.png A shockingly busy toolbar.)

Similarly, I couldn’t fit everything into the menu panel either.  The only
solution was to resort to some [Photoshop](http://flyingmeat.com/acorn/)-trickery
to fit all the buttons in, but that ended up breaking the script I was using
to locate the various elements in the UI.

<style>
img[alt="A surprisingly tall menu panel"] {
  width: 270px;
  height: 915px;
  margin-left: calc(50% - 135px);
}
</style>

![A surprisingly tall menu panel](https://raw.githubusercontent.com/bwinton/d3Experiments/gh-pages/images/Darwin/HeatmapMenu.png A surprisingly tall menu panel.)

Since I couldn’t automatically figure out where everything was, I figured we
might as well use a nicely-laid out, partially generated image, and calculate
the positions (mostly-)manually.

![The current version of the heatmap (Note: This is not the real data.)](http://weblog.latte.ca/images/blake/SampleHeatmap.png The current version of the heatmap.  Note: This is not the real data.)

I had foreseen the need for different positions for the widgets when the
project started, and so I put [the widget
locations](https://github.com/bwinton/d3Experiments/blob/gh-pages/data/Darwin/widgets.csv)
in their own file from the start.  This meant that I could update them without
changing the code, which made it a little nicer to see what’s changed between
versions, but still required me to reload the whole page every time I changed
a position or size, which would just have taken way too long.  I needed
something that could give me much more immediate feedback.

Fortunately, I had recently finished watching a
[series](https://www.youtube.com/watch?v=PFxWmjiUWII&index=1&list=PLI_sHchSmdCDLfLl5uTnsaRB54tDlRubK)
[of](https://www.youtube.com/watch?v=sK6fLTJ9vf0&index=1&list=PLI_sHchSmdCC2Yg2IXzhGUc2V6dfZK_dV)
[videos](https://www.youtube.com/watch?v=h60j8k3SOrA&list=PLI_sHchSmdCBa3CrSwobdZWU-tV_ZeaCO&index=1)
from [Ian Johnson](http://enja.org/) ([@enjalot](https://twitter.com/enjalot)
on twitter) where he used a tool he made called
[Tributary](http://tributary.io/) to do some rapid prototyping of data
visualization code.  It seemed like a good fit for the quick moving around of
elements I was trying to do, and so I copied a bunch of the code and data in,
and got to work moving things around.

I did encounter a few problems: Tributary wasn’t functional in Firefox Nightly
(but I could use Chrome as a workaround) and occasionally sometimes trying to
move the cursor would change the value slider instead.  Even with these
glitches it only took me an hour or two to get from set-up to having all the
numbers for the final result!  And the best part is that since it's all open
source, you can take a look at
[the final result](http://tributary.io/inlet/2ba87a4bc8d56f3b4cfc), or
[fork it yourself](https://github.com/bwinton/d3Experiments/tree/gh-pages)!

