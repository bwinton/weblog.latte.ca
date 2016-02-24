<!--
.. title: Brokeback Mountain functionality on OS X.
.. date: 2011-03-25 17:48:05
.. author: Blake Winton
.. tags: ehsan, quit, mozilla
-->

[A co-worker](http://ehsanakhgari.org/blog) of mine recently mentioned that
he had a problem where he all-too-often accidentally quit his applications
by hitting ⌘-q (command-q).  Since he has been having problems with
Thunderbird that I can’t fix, I thought I might do a little digging and see
if I could come up with some way of helping him.  And so here’s what I
found:

In the System Preferences application, there’s a “Keyboard” section.

![The Keyboard Preference Pane](/images/blake/Quit/1-Keyboard.png "Keyboard")

One of the things you can choose in that section is “Keyboard Shortcuts”.

![The Keyboard Shortcuts](/images/blake/Quit/2-Shortcuts.png "Shortcuts")

Pick a relatively innocuous function, like turning Zoom on and off.

(Note: DO NOT choose Front Row for this!)

![The Access Shortcuts](/images/blake/Quit/3-Access.png "Access")

And assign that function to ⌘-q.

![The New Shortcut](/images/blake/Quit/4-⌘Q.png "⌘Q")

Now, whenever you hit ⌘-q, it will do whatever you selected, instead of
quitting the application.  Ta-da!

