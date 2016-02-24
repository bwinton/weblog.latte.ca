<!--
.. title: Another reason to use Mercurial (or Git or Bazaar)
.. date: 2009-09-14 12:12:48
.. author: Blake Winton
.. tags: virtual_machines, programming, hg
-->

A lot of the code I write for [Thunderbird](http://mozillamessaging.com/)
has to work on [all](
http://www.mozillamessaging.com/en-US/thunderbird/all.html) the platforms
it supports.  Since I don’t own a [Linux](http://www.ubuntu.com/) or
[Windows](http://www.microsoft.com/windows/windows-7) box, and don’t really
want to waste the hard drive space on my [MacBook Pro](
http://www.apple.com/ca/macbookpro/specs.html) with a dual- or triple-boot
setup, I’ve decided to install the other operating systems on virtual
machines.  (I’ve chosen [VirtualBox](http://www.virtualbox.org/), because
it’s free, and I’m cheap.  As an added bonus, it works quite well, too.)

If I was forced to use a centralized version control system, this would
lead to a bunch of pain, since I wouldn’t want to check in a half-finished
patch, but I would still really want to see what changes I made for one OS,
to try and figure out what changes I need to make for the others.  And I
would want to be able to keep a record of what I did, step by step, so that
I could undo stuff if it turned out to be a bad idea.  (Hey, that sounds
like a perfect task for a version control system!  ;)

Since Mozilla uses [Mercurial](http://mercurial.selenic.com/), I didn’t
have to deal with any of that.  I had my repository on the host machine,
which I had cloned from the main repo, and I just cloned it into each of
the virtual machines.  Whenever I started a VM, I pulled the latest set of
changes from the host machine; As I fixed stuff on that platform, I
committed to the repository on the virtual machine; And before I shut down
the VM, I pushed my changes back to the host machine.  When I wanted to see
which changes I made to get things working for the platform, it was easy,
and propagating those changes to the other virtual machines was also easy.

When people talk about the advantages of distributed version control, a lot
of the time they mention being able to still commit your changes when
you’re on an airplane, and sharing in-progress changes with other people,
but for people like me who do mainly self-contained stuff and don’t fly
anywhere, supporting multi-platforms with virtual machines and still being
able to track my changes might just be the killer feature.

