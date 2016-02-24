<!--
.. title: How to dynamically change your icons.
.. date: 2008-03-01 21:11:56
.. author: Blake Winton
.. tags: itouch, programming, wifitoggle
-->

One of the things I wanted to add to [WifiToggle](
http://www.csse.uwa.edu.au/~chris/iphone/WifiToggle/) was having the
icon show you whether your wifi was on or off, by having the switch be
up or down (and the blue glow be on or off, since in Australia a down
switch means that the light is on, whereas in Canada, it’s the
opposite).  Sadly, it didn’t seem possible, since Springboard[^sb]
seems to cache your icon.png, and ignore any updates you do to it.
And so that was where I left it for a long time…

Recently, however, I was browsing through [AppFlow](
http://ericasadun.com/?p=176) and I noticed that the MobileCalendar
application’s icon was different than the one in Springboard.
Specifically, the one on AppFlow was blank, whereas the one in
Springboard showed me the current day and date (i.e. "Saturday" and
"1" for today).  How did it do that?  I grabbed the source, and
grepped through it for the answer, which turned out to be a special
key in the Info.plist:

    <key>SBIconClass</key>
    <string>SBCalendarApplicationIcon</string>

When I set WifiToggle’s SBIconClass key to be the same, I too had the
day and date drawn on top of my icon!  Partial success!  So now I’m at
the point of trying to figure out if I can use any class that
implements the correct interface (I’m thinking specifically about
adding a class to my application to handle the updates.)  Of course, I
have no idea what that interface is, but hey, I’m way closer than I
was this morning, so that’s got to count for something.

[^sb]: The application launcher on the iTouch.

