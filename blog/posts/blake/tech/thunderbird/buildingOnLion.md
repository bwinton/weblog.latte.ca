<!--
.. title: Building Thunderbird on OS X Lion (10.7) and XCode 4.2
.. date: 2012-03-06 10:34:10
.. author: Blake Winton
.. tags: mozilla, thunderbird, mac
-->

A few people recently asked me about building Thunderbird on the latest version
of Mac OS X.  Since I have it working, and to give myself a place to point to
the next time they ask, I figured it would be a good idea to blog about it.

So, here’s my `.mozconfig`.

    #!sh
    # Debug .mozconfig
    mk_add_options MOZ_MAKE_FLAGS=-j4
    mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../objdir-`basename \`pwd\``-`hg branch`
    # mk_add_options AUTOCONF=autoconf213
    ac_add_options --enable-application=mail
    ac_add_options --enable-extensions=default,inspector
    ac_add_options --enable-inspector-apis

    # Compilation options
    ac_add_options --disable-optimize
    ac_add_options --enable-debug
    ac_add_options --enable-tests
    ac_add_options --disable-jemalloc
    #ac_add_options --enable-trace-malloc
    ac_add_options --enable-chrome-format=symlink

    ac_add_options --with-macos-sdk=/Developer/SDKs/MacOSX10.7.sdk
    ac_add_options --enable-macos-target=10.7

    # For NSS symbols
    export MOZ_DEBUG_SYMBOLS=1
    #ac_add_options --enable-debug-symbols="-gdwarf-2"

    #Use ccache
    #ac_add_options --with-ccache=/usr/local/bin/ccache

    # We don't have GCC anymore, since XCode 4.2, so use clang instead.
    CC=clang
    CXX=clang++

There are probably a bunch of things I don’t really need in there, so if anyone
wants to take it, and cut it down to the minimal set, I would definitely
appreciate it.  But in the meantime, this works for me, and will probably work
for you, too.
