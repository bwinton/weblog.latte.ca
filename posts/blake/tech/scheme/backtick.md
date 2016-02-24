<!--
.. title: An odd restriction
.. date: 2008-04-09 10:20:43
.. author: Blake Winton
.. tags: itouch, scheme, gambit, macros
-->

As [I mentioned](
http://weblog.latte.ca/blake/tech/iTouch/languages.html ) before, I’ve
ported Gambit Scheme to my iTouch, and have been playing around with
it a little.  It’s pretty nice all in all, but I recently ran into a
small problem while I was trying to play around with macros.  The
problem?  There’s no way to enter a backtick (`) on the iTouch!  That
means that I don’t really have a way to write code like

    #!scheme
    `( a b ,(+ 1 2) d)

which makes writing macros a lot more painful.  Fortunately, I got a
lot of help from the people on [IRC](irc://irc.freenode.net/gambit)
and on the [Gambit mailing list](
https://webmail.iro.umontreal.ca/pipermail/gambit-list/ ).
Specifically, Marc Feeley, the author of Gambit, [posted](
https://webmail.iro.umontreal.ca/pipermail/gambit-list/2008-February/002011.html)
a snippet of code that I could put into my .gambcini file that would
add $ as a synonym for `.  The code looked like this:

    #!scheme
    (begin
      (##readtable-char-class-set!
        (current-readtable)
        #\$  ;; the character to dispatch on
        #t   ;; this character is a delimiter
        (lambda (re c) (##read-quotation re #\`)))  ;; handler
      #f)

and the example, which works, is:

    #!scheme
    $(1 ,(+ 2 3) 4)
    output: (1 5 4)

<p>If you’re trying to write that code on your iTouch, you might notice that it
includes the forbidden `, and so you’re once again out of luck.  Except that
in this case, you can replace #\` with #\u0060, which you can type in on the
iTouch, and then it’ll all work.</p>

