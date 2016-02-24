<!--
.. title: Starting Scheme.
.. date: 2007-05-09 17:28:58
.. author: Blake Winton
.. tags: scheme
-->

(Posted to the LispMe@YahooGroups.com list)
Hello.

Let me start with a brief introduction.  My name is Blake Winton,
and I’ve owned a PalmPilot since back when they were called PalmPilots
and made by USRobotics.  I’ve been programming for them for years,
mostly in C and C++, with brief excursions into Lua, Python, and
Forth.  My day job consists mainly of Java (J2EE), with some Python
when I get the chance, and some JavaScript when I shouldn’t be using
Python.  On my off hours, I read a lot about other languages (recently
Objective C, OCaml, and Ruby).  Now I want to learn Scheme, and
thought that LispMe would be a good way to do it.  I’m finding some
things are tripping me up, mainly due to my attempts to transfer my
knowledge from other areas into LispMe.  (One piece I miss in
particular are something like Python’s List Comprehensions, which I
believe they sole from Haskell.)

So, I’m going through SICP, but while I’m doing that, I thought I
would try to do a "Real World" (tm) task, and write a program that
drew the Serpinsky Triangle, using an iterative, random, approach,
(Details available upon request,) and I’ve run into some small
questions about best practices, or basically how to do some simple
things.  In return for this help, I’ll create a sort of Tutorial
document for LispMe that will be able to help other people get up to
speed.  (If such a document already exists, please, someone, point me
to it!)

So, here’s what I’ve got so far.  It doesn’t work at all, but it’s
starting to take shape.

    #!scheme
    ; Triangle
    (define points
      #((80,10) (10,150) (150,150)))
    
    (define (next-point p) (
      (vector-ref points
        (random (vector-length points)))
      ))
    
    (define current-point '(80 80) )
    (define (halfway a b) (/ (+ a b) 2))

And we’re done.  Any comments on it, from spacing to indentation to
whether I should use a vector or a list for the points themselves,
would be greatly appreciated.  If it matters, I plan on extending the
point to include red, green, and blue data as well, possibly with
accessors, looking something like this:

    #!scheme
    (define current-point '(80 80 255 0 0))
    (define (x pt) (car pt))
    (define (y pt) (cadr pt))
    (define (r pt) (caddr pt))
    (define (g pt) (cadddr pt))
    (define (b pt) (caddddr pt))

Oh, and I suspect I’ll be blogging my progress at <a
href="http://weblog.latte.ca/blake/tech/scheme/">http://weblog.latte.ca/blake/tech/scheme/</a>
(Nothing exists there at the moment, though.  Give it time.)

Thanks,<br />
Blake.


