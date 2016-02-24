<!--
.. title: Pushing code to a remote server the volo way.
.. date: 2012-07-22 14:04:39
.. author: Blake Winton
.. tags: volo, deploy, remote, server, rsync, mozilla
-->

The [side-project](
https://github.com/bwinton/australis-customization/) I’m working
on is coming along nicely, and so I figured it was time to let other people
see it.  Now, I could just have everyone huddle around my screen, but since
many of the people who would be interested aren’t in the same city (or even
same timezone) as I am, that wouldn’t work out so well.  We tried screen-
sharing, but a lot of what’s being worked on is animation, and the frame-rates
of the screen-sharing application we were using weren’t up to the task.  To
get around that, I could have recorded a video, but since a lot of the value
of a prototype like this is being able to play around with it, that’s also not
a great solution.  So, obviously, the best thing to do would be to put it on a
publicly available server, and let people run it in their own web browser,
whenever they wanted!

Now, I’m running a server or two that I could put it up on, but since the
project is related to Mozilla, and since Mozilla offers some personal webspace
on [one of their servers](http://people.mozilla.org/), I figured I might as
well put it up [there](
https://people.mozilla.com/~bwinton/australis/customization/mac/?scroll).  :)

So, to make it easy for me to remember to build and upload the code (and to
prevent me from trying to figure out all the correct options to rsync every
time I wanted to upload the code), I took a couple of minutes to [add a
command](
https://github.com/bwinton/australis-customization/blob/master/australis/customization/mac/volofile#L23
) to my volofile, which lets me merely type `volo deploy`, and have it
optimize the code, and copy only the changed files to the remote server.

