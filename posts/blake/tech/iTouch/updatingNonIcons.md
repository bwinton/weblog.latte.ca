<!--
.. title: Other dynamically-changing stuff.
.. date: 2008-03-04 16:09:59
.. author: Blake Winton
.. tags: itouch, programming, ledbanner
-->

Last night I was browsing the newest iTouch apps, and I saw one called
[LEDBanner](http://www.iamas.ac.jp/%7Eaka/iphone/#LEDBanner.app).  It
allowed you to scroll text across your screen as if your screen was a
set of LEDs.  My only problem with it was that I couldn’t
programmatically change the text.  Fortunately the source was
available, and so, with only minor changes, I now have [a
version](/static/blake/LEDBanner.zip) which
lets me change the text to whatever I want.

For instance, the following scheme code:

    #! /usr/bin/gsi
    (define (flmod x y) (fl- x (fl* (floor (fl/ x y)) y)))
    (define (%100 time) (flmod (floor (time->seconds time))
    (fixnum->flonum 100)))
    (define (f)
      (begin
        (with-output-to-file
          (list
            path: "~/Library/Preferences/org.akamatsu.LEDBanner.msg"
            truncate: #t)
          (lambda () (display (%100 (current-time)))))
        (thread-sleep! 3)
        (f)))
    (f)

changes the text every three seconds to the number of seconds, modulo
100.  Which turns out to be a mostly-random number, as shown below.

![The number 8.](/images/blake/led.png "Ocho!")

