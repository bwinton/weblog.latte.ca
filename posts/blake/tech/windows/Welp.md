<!--
.. title: Welp, I did it.
.. date: 2016-11-17 10:21
.. author: Blake Winton
.. tags: windows, moving, expectation
-->

As I mentioned in a [previous post][disappointment], I wasn’t really excited by the new MacBooks that were announced this year.  And the more I read the less compelling they seemed…  As I talked with my co-workers, I heard some really good reviews of a couple of models of Windows computers, and since 90% of Firefox’s users are using Windows it’s probably not such a bad idea if I use it, too, both to help me understand the problems they’re running into, and to make sure that the code I’m writing will work for them.

<!-- TEASER_END -->

So on Friday I bit the bullet and ordered a Dell [XPS 15][dell] (with Touch screen, 32Gb RAM, and a 1Tb SSD) for my latest laptop refresh.  I _think_ that the recent updates to the [Windows Subsystem for Linux][windows] will let me do all the same Unix-y stuff I’ve been doing on the Mac, and if I use the same keyboard and trackpad, I’m not sure I’ll notice much of a difference, to be honest.

![Dude.  I’m getting a Dell.](/images/blake/Dell.jpg)

It’s going to be a few weeks before it arrives, which is nice because it lets me think about all the stuff I’ll need to transfer over, and because it lets [Mike Hoye][hoye] go through all the pain of switching before I do, so I can hopefully avoid the worst pitfalls.  😉  There is, of course, a [guide to switching][switching] for Mozilla people, but it’s pretty out of date.  I’ll probably be updating it as I run into stuff, and hopefully the other people who are also switching will do the same.

So, here’s the big list of stuff I currently use, and replacements (where I know what they are):

First off, the obvious ones:

* [Slack][slack] ⇒ Slack
* [Firefox][firefox] ⇒ Firefox
* [Twitter][twitter] ⇒ Twitter
* [Crashplan][crashplan] ⇒ Crashplan
* [Chrome][chrome] ⇒ Chrome

Next, the slightly more complicated ones: 

* [iTerm2][iterm] ⇒ [Cmder][cmder]<br>
    Cmder isn’t the same, but it’s the best Windows terminal app I’ve found.<br>
    *Update*: I might go with [ConEMU][conemu], the program underlying Cmder, instead. 
* [Safari][safari] ⇒ Also Chrome.  Or maybe [Edge][edge].<br>
    I use Safari mostly for YouTube.  I used to use Chrome for this; maybe I’ll go back, or maybe it’s time to try a new browser.  I hear Edge has really good battery life while watching video…  🙂
* [Atom][atom] ⇒ Atom (or [Visual Studio Code][code]?)<br>
    I’ve heard not-great things about Atom on Windows, so I’m starting to look into switching to Visual Studio Code.  So far it seems okay…  I do miss the minimap and [Whimsy][atom-whimsy].
* [Dropbox][dropbox] ⇒ Dropbox (or [Google Drive][drive], or [CloudApp][cloudapp]?)<br>
    Mozilla moved to Google Apps for our email, and now we have a big shared space there.  Should we really still be paying for Dropbox Pro accounts for our team?  Maybe not…  Of course, I don’t think Google Drive uploads screenshots automatically, so maybe I’ll also need to install CloudApp for that?
* [Acorn][acorn] ⇒ [Paint.net][paint]<br>
    Totally not the same, but I think paint.net will do _most_ of the stuff I want.

After that is the software I’m unsure about alternatives for:

* [LimeChat][limechat]<br>
    I’ve been looking for a while, but still haven’t found a beautiful IRC client for Windows.  (Please don’t suggest mIRC, or irssi over ssh…  Anyone who considers those “beautiful” clearly doesn’t share my aesthetic. 😝)  The closest I’ve found has been [Foo IRC][foo], but I’m not sure how well it works.  For some reason I had a pinned tab open on [IceChat][icechat]’s page, but I’m not a big fan of how it looks…<br>
    *Update*: [IRC Explorer][ircexplorer] looks pretty nice, too… 
* Mail.app<br>
    I’m not really enthused with Apple’s Mail app, but it’s not terrible.  I hear Microsoft’s Mail app is pretty similar, so I’ll give it a try.
* [XScope][xscope]<br>
    I don’t think there _is_ anything like XScope on Windows 10.  I might just have to go back to my Mac for the kinda stuff I use it for…
    *Update*: [PicPick][picpick] looks like it might do some of the stuff XScope does…

And things I just don’t know about:

* Calendar.app<br>
    I’m sure there’s _something_ on Windows that does calendaring, but will it connect to my home iCal account?
* [Things][things]<br>
    I don’t use this a ton these days, but it’s good for keeping track of what’s on my plate.  I may just continue to use it on my iPhone…
* [iTunes][itunes]<br>
    I don’t think [WinAmp][winamp] or iTunes for Windows are really what I’m looking for here.  I might switch to a combination of [Spotify][spotify] and my iPhone. 
* [Anvil][anvil]<br>
    Do I still need to run folders as websites?  Maybe not so much these days, since I’m using [webpack][webpack]a lot more, and it comes with a dev server. 
* [Quicksilver][quicksilver]<br>
    I think I could probably use the Cortana search menu for most of what I use Quicksilver for…
* [aText][atext]<br>
    This is another one of those “There _has_ to be something like this” apps, but I have no idea what it is.

Suggestions for any of the apps mentioned above would be very appreciated!

[acorn]: https://secure.flyingmeat.com/acorn/ "Acorn"
[anvil]: http://anvilformac.com/ "Anvil for Mac"
[atext]: http://www.trankynam.com/atext/ "aText"
[atom-whimsy]: https://atom.io/packages/atom-whimsy "Atom Whimsy"
[atom]: https://atom.io/ "Atom"
[chrome]: https://www.google.com/chrome/browser/desktop/index.html "Chrome"
[cloudapp]: https://www.getcloudapp.com/ "CloudApp"
[cmder]: http://cmder.net/ "λcmder"
[code]: http://code.visualstudio.com/ "Visual Studio Code"
[conemu]: https://conemu.github.io/ "ConEMU"
[crashplan]: https://www.crashplan.com/en-us/ "Crashplan"
[dell]: http://www.dell.com/ca/p/xps-15-9550-laptop/pd?oc=nxps15550_bt_h1609e&l=en&s=dhs "Link to the Dell Store"
[disappointment]: /blake/tech/mac/disappointment.html "My problems with the new MacBooks"
[drive]: https://drive.google.com/ "Google Drive"
[dropbox]: https://www.dropbox.com/home "Dropbox"
[edge]: http://www.microsoft.com/en-us/windows/microsoft-edge "Microsoft Edge"
[firefox]: https://www.mozilla.org/en-US/firefox/new/ "Firefox"
[foo]: http://fooirc.com/#!index.md "Foo IRC"
[hoye]: http://exple.tive.org/blarg/2016/11/14/switching-sides/ "Switching Sides"
[icechat]: http://www.icechat.net/site/ "IceChat"
[ircexplorer]: https://www.microsoft.com/en-ca/store/p/irc-explorer/9wzdncrdkmgz "IRC Explorer"
[iterm]: https://iterm2.com/ "iTerm 2"
[itunes]: https://www.apple.com/itunes/ "iTunes"
[limechat]: http://limechat.net/mac/ "LimeChat for Mac"
[paint]: http://www.getpaint.net/index.html "Paint.net"
[picpick]: http://ngwin.com/picpick "PicPick"
[quicksilver]: https://qsapp.com/ "Quicksilver"
[safari]: https://www.apple.com/safari/ "Safari"
[slack]: https://slack.com/ "Slack"
[spotify]: https://play.spotify.com/search/hamilton%20mixtape "Spotify"
[switching]: https://wiki.mozilla.org/Transitioning_to_Windows#Applications_.26_tools "Transitioning to Windows"
[things]: https://culturedcode.com/things/ "Things"
[twitter]: https://about.twitter.com/products/twitter-for-windows/ "Twitter for Windows"
[webpack]: http://webpack.github.io/ "Webpack"
[winamp]: http://www.winamp.com/ "WinAmp"
[windows]: https://blogs.msdn.microsoft.com/wsl/2016/04/22/windows-subsystem-for-linux-overview/ "Windows Subsystem for Linux"
[xscope]: http://xscopeapp.com/ "XScope"
