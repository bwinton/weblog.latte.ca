<!--
.. title: Isn't that just the way of it...
.. date: 2007-05-09 17:29:00
.. author: Blake Winton
.. tags: scheme
-->

I mentioned in the previous entry that I was missing Python's List
Comprehensions.  Well, I've gotten a little closer to having them.
For some reason, LispMe doesn't come with a <tt>zip</tt> method,
and you can only get <tt>map</tt> by importing a "<tt>Standard
Library</tt>" memo.  So, I had to write my own version of zip, and
here it is, for anyone else who might find it useful.

    #!scheme
    (define (zip s1 s2)
      (if (or (null? s1) (null? s2)) '()
        (cons (list (car s1) (car s2))
          (z (cdr s1) (cdr s2)))))

Along with my halfway function, redefined to be <tt>(define
(halfway x) (/ (+ (car x) (cadr x)) 2))</tt>, I can now write
<tt>(map halfway (zip current-point next-point))</tt> to get the
point halfway between where I am, and where I am going to.

I also came to another realization.  I was planning on defining a
<tt>current-point</tt>, and using <tt>set!</tt> to update it
to the new halfway point, but when I think about it, I don't really
care what the current point is at any time other than processing, so
there's no particular need to set it, and instead I should just pass
it around as a parameter, making my iter function (and I just made up
the name "iter function", based on the <a href=
"http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.7"
><tt>sqrt-iter</tt></a> function in "Structure and Interpretation
of Computer Programs") look something like this:

    #!scheme
    (define (triangle-iter start num-iters)
      (if (positive? num-iters)
        (begin (draw-point start)
        (triangle-iter
          (map halfway (zip current-point next-point))
          (- num-iters 1)))))

Does that look appropriately Scheme-ish, do you think?

