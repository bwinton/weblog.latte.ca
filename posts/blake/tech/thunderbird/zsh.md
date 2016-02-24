<!--
.. title: A handy zsh function (for OS X)
.. date: 2010-07-19 10:20:13
.. author: Blake Winton
.. tags: thunderbird, zsh, osx, mozilla
-->

A co-worker of mine was having problems remembering where the [makefile](
http://mxr.mozilla.org/comm-central/source/client.mk) puts the binary for
[Thunderbird](http://mozillamessaging.com/) when you build it yourself.
Now, I type in the path far too often, so I know where it is (on my
computer, anyways), but since I type it in far too often, I grabbed
someone's [zsh](http://www.zsh.org/) function that launched [Firefox](
http://www.mozilla.com/), and modified it to launch Thunderbird from either
the build directory or the source directory, but only on Mac OS X.

Anyways, here it is, I hope some of you find it useful.

    #!sh
    thunderbird() {
      local -a currdir;
      currdir=$PWD:t;
      for nm in LanikaiDebug ShredderDebug Lanikai Shredder; do
        if [ -d "./mozilla/dist/$nm.app" ]; then
          ./mozilla/dist/$nm.app/Contents/MacOS/thunderbird-bin $*
          break;
        elif [ -d "../objdir-$currdir/mozilla/dist/$nm.app" ]; then
          ../objdir-$currdir/mozilla/dist/$nm.app/Contents/MacOS/thunderbird-bin $*
          break;
        fi
      done
    }

