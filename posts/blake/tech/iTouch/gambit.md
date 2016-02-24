<!--
.. title: Some notes on cross-compiling GambitC
.. date: 2008-12-12 17:09:47
.. author: Blake Winton
.. tags: gambit, scheme, itouch
-->

The command to use is:

    $ env CC=/usr/local/bin/arm-apple-darwin-gcc CC_FOR_BUILD=gcc ./configure --host=mac; make
Well, kind of.  First you do that, then you copy gsc/gsc to gsc/gsc.onboard,
then you go to a new directory, and type:

    $ ./configure;make
and copy the gsc/gsc from that directory into the first directory.

To compile a script into an exe:

    $ gsc/gsc -:=. -c euler.scm
    $ gsc/gsc -:=. -link euler.c
    $ /usr/local/bin/arm-apple-darwin-gcc euler.c euler_.c -Iinclude -Llib -lgambc -o euler
It's freaking huge!

    $ ls -alh euler
    -rwxr-xr-x   1 bwinton  bwinton  4M Jan 23 14:22 euler
    $ ls -alh /WifiToggle
    -rwxr-xr-x   1 bwinton  bwinton  17K Jan 16 14:07 /WifiToggle
And it's not a lot faster.
0.1643 seconds for the compiled version, as opposed to 0.1803 seconds for the interpreter. 

But on my Mac:

    $ more m1.c
    power_of_2 (int x) { return 1<<x; }
    $ more m2.scm
    (c-declare "extern int power_of_2 ();")
    (define pow2 (c-lambda (int) int "power_of_2"))
    (define (twice x) (cons x x))
    $ more m3.scm
    (write (map twice (map pow2 '(1 2 3 4)))) (newline)
    $ gsc/gsc -:=. -link -flat -o foo.o1.c m2 m3
    $ /usr/local/bin/arm-apple-darwin-gcc -Iinclude -bundle -D___DYNAMIC m1.c m2.c m3.c foo.o1.c -o foo.o1
    $ ls -alh foo.o1
    -rwxr-xr-x   1 bwinton  bwinton    13K Jan 23 14:45 foo.o1
then on the iTouch,

    # scp bwinton@latte.ca:/Users/bwinton/Programming/Bazaar/iTouch/gambc-v4_1_2/foo.o1 .
    # gsi foo.o1
    ((2 . 2) (4 . 4) (8 . 8) (16 . 16))
    # gsi
    Gambit v4.1.2
    
    > (load "foo")
    ((2 . 2) (4 . 4) (8 . 8) (16 . 16))
    "/private/var/root/foo.o1"
    > (twice 5)
    (5 . 5)
    > (pow2 10)
    1024
    

