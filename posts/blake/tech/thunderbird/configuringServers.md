<!--
.. title: Adventures in Mail Servers (or, how I wasted my Sunday afternoon)
.. date: 2012-03-25 21:52:11
.. author: Blake Winton
.. tags: email, postbox, dovecot, osx, server, wtf, fml
-->

I think what I want is pretty simple, or at least, reasonably common.
I’m just looking for a couple of programs.

An SMTP server which will accept mail for the accounts at latte.ca, and deliver
it to a Maildir of my choosing, and let me send mail through it if, and only if,
I’ve logged in with the password to that account.  (Being able to define a few
aliases would also be nice.)

And an IMAP server which will expose the previously-mentioned Maildir, after
I’ve logged in with the password to that account.

And yet, every time I try to set that up, something completely falls over for no
particularly understandable reason, and I end up wasting an afternoon (or more)
of my life.  I had hoped this time would be different, since I decided not to
install and configure everything myself, but instead bought a copy of OS X Lion
Server which was supposed to do all the hard work for me.  I’m not going to
enumerate all the problems I ran into, but I will say that I still haven’t
managed to get there.  I’m just done for tonight.

Anyways, if anyone reading this has a working setup that meets the requirements
(and the added requirement of needing to use Dovecot and Postfix, since those
are what’s installed), I would love to get a copy of their config files.  And in
the meantime, I might seriously look into getting a refund for Lion Server,
given how badly it’s failed me.  :P

