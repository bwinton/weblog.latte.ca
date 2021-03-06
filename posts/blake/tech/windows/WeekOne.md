<!--
.. title: It’s here!
.. date: 2016-11-28 13:41
.. author: Blake Winton
.. tags: windows, moving, arrival
-->

It arrived!

![Dude.  I got a Dell.  Not as much dragon, though…](/images/blake/MyDell.jpg)

<!-- TEASER_END -->

So, here are some initial thoughts on it as I was setting it up and using it for the first few days.

The power cord has a pair of nice white bars that light up to show you when itʼs charging!  But it turns out that itʼs not actually when itʼs charging, but rahter when itʼs plugged in, so thatʼs much less useful.  (Although there is a light on the front of the computer that shows you when itʼs charging, so thatʼs okay.)  But, better yet, you can unplug the power adapter, and the bars will still be lit, which is just freaky looking!  (Thank you, capacitors.  O_o)

I couldʼnt connect to Mozilla wifi during setup for some unknown reason.  Fortunately, Mozilla Guest worked just fine, but I think that ended up coming back to bite me later when I tried to set up Firefox Sync, and the confirmation email didnʼt send (or took several hours to arrive). 

Another oddity that I quickly ran into was Windowsʼ choice to turn tap-to-click on by default!  Further, when I went to turn it off, I found out that I also needed to separately turn off the two-finger-tap-to-right-click, for some reason.

Obviously the first thing I did, after fixing the touchpad, was download Firefox (Developer Edition, both because Iʼm developing stuff with web technologies, and because I feel the flat rectangular look fits better in Windows 10 than the curvy tabs of Australis).  And then I got a little discouraged, because there are soooooo many things left to install and change before this computer is set up the way I like it…

Well, nothing to do but get on with it, I guess.  Next up on the install list are some communication tools.  Slackʼs beta client (which I think is just the regular Slack client on Windows) is great.  Twitter, on the other hand, really isnʼt app-ish.  Thereʼs no menu.  It doesnʼt let me use ctrl-number to switch between sections.  The refresh is really odd.  Itʼs almost like itʼs their mobile site in a tiny embedded browser, which isnʼt what I was looking for.  (I was hoping for something more like the Mac app, which I complain about often enough, but as bad as it is, itʼs much better than the Windows one.)  The next app I started setting up was Microsoft Mail.  It took me a while before I figured out how to show all the Inboxes in one merged view, and Iʼm still not sure I got a folder that shows me all my unread mail, but I think thatʼs something I can continue to use the Mac for for a while…

After that I got back to work-related stuff, by enabling the Windows Subsystem for Linux (which still canʼt quite run Windows apps yet, but I can work around that for a while), and using apt to install git, fish.  I ended up going with ConEMU over Cmder, because I donʼt use cmd.exe, so I donʼt need clink, and Iʼm using the Linux version of git, so I donʼt need the git-for-windows, and those are the only two things that Cmder adds…

At this point, I wanted to create an SSH key for the new machine (and maybe I started to get tired of typing in my password everywhere 😉), so I thought I would give the Windows version of 1Password a try.  Since 1Password uses Dropbox to sync, that kinda meant I needed to install Dropbox, too, so thatʼs what I did, but I turned on Selective Sync, and only chose the folders I needed, skipping the really large shared Mozilla UX folder that weʼre migrating to Google Drive.  Of course, that still left a lot of stuff to sync, so it was a few hours before I could access my 1Password vault, and access all my old passwords, and add a new SSH key and passphrase.

I think this might be a good time to take a break and mention something that Iʼm enjoying about using Windows so far.  I very much missed using `Fn` with the arrow keys to move to the home, end, page up, and page down, and while Iʼm still getting used to remembering them as I move my cursor around, I get a tiny bit of joy every time I type them.  On the reverse side, I try to type `Fn-;` for “…”, and `Fn-]` for “ʼ” all the time, and eventually it disappointed me enough that I searched for a program that would help, and found [PhraseExpress][phraseexpress], which, while it doesnʼt handle the `Fn` key, does let me use `Ctrl-Shift-;`, which is close enough for me.  (One thing to note, you need to set it to use the Windows Clipboard instead of the keystroke simulation, or stuff like `:smile:` for 🙂 wonʼt work.)

And the last couple things I installed before the weekend were some apps to play media.  [VLC][vlc] for movies, and the Spotify app for music.  I had used VLC in the past, but completely forgot about it.  And while Spotify did work in Edge, I found that by installing the app, I could use the play/pause and next/previous track buttons on the keyboard, which was something I was missing a lot even back when I was using it on Chrome on MacOS.  Also, `rsync` is an amazing program if you want to copy a lot of files from one computer to another!  Just set it up, and let it go, and if it fails halfway through, you can run the same command, and itʼll pick up where it left off!

Thereʼs still a bunch of stuff Iʼm missing, and Iʼm going on a trip to Hawaii in the next week or two, so Iʼll probably write another update while Iʼm there, describing what itʼs like with only the one computer.  Well, the stuff I notice, anyways.

[phraseexpress]: http://www.phraseexpress.com/
[vlc]: http://www.videolan.org/vlc/