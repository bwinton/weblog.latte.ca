<!--
.. title: Building Thunderbird Faster
.. date: 2009-09-26 13:57:39
.. author: Blake Winton
.. tags: thunderbird, building, secrets, mozilla
-->

I’m always looking for ways to speed up my Mozilla build, since it allows
me to test my changes even quicker.  I was really excited when I found out
about <tt>make -s tier_app</tt>, since it sped up my compiles by a huge
amount.

    make
    real    10m22.630s
    user    4m28.072s
    sys     1m27.807s

vs.

    make -s tier_app
    real    0m14.426s
    user    0m6.502s
    sys     0m3.957s

But yesterday, on IRC, I heard about <tt>libs_tier_app</tt>, which is ever
faster, if you haven’t changed any IDL files (which I usually don’t).

    make -s libs_tier_app
    real    0m9.407s
    user    0m5.440s
    sys     0m3.065s

Okay, it’s not nearly as good as going from 10 and a half minutes to 15
seconds, but a 30% (or is it 50%) speedup is still nothing to sneer at.

