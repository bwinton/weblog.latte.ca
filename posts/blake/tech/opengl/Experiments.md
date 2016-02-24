<!--
.. title: Experiments in OpenGL (on the iPhone 3GS).
.. date: 2009-12-10 13:16:05
.. author: Blake Winton
-->

While I was at the Toronto iPhone Tech Talks, I attended the OpenGL ES
sessions by [Allan Schaffer](http://twitter.com/funnest).  Seeing the
“Shock” demo was really inspiring, and caused me to want to try my
hand at some simple OpenGL Shader demos.

The base XCode OpenGL ES Application template sets you up pretty
nicely for some simple experimentation, the only things that gave me
any trouble were:

1. remembering to set the identifier to ca.latte.whatever so that I
could build, and

2. remembering that the OpenGL ES 2.0 path only ran on the device, so
of course none of the changes I was making were showing up on the
simulator[^1], and finally

3. Figuring out that depth was position.w, and not position.z.  (Did I
mention that I’m a bit of a newbie at this?)

Anyways, after it was all up and running, I made the x and w
co-ordinates vary on a different period than the y co-ordinate, and
now the square moves around in 3 dimensions in a pleasing (to me) way.

![A pretty square.](/images/blake/iTouch/OpenGL/1-square.jpg A square,
that’s all.)

Since this is intended for me to play around with shaders, I’m not
going to bother updating the OpenGL ES 1.0 code path, but if you’ve
got an iPhone 3GS, or a 3rd generation iTouch, feel free to grab the
code at [BitBucket](http://bitbucket.org/bwinton/opengl/), and play
around.  I'll be adding branches and tags and keeping it updated as I
play with new stuff.

[^1]: [Rune](http://twitter.com/runmad) let me know that Open GL ES
    2.0 is supported in the latest version of the simulator.  I guess I
    must have been testing with an earlier version of the SDK, or XCode,
    or something.

