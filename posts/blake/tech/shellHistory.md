<!--
.. title: What I do on my Mac.
.. date: 2008-04-16 17:53:04
.. author: Blake Winton
.. tags: shell, history, top_ten
-->

From [André Roberge](http://aroberge.blogspot.com/2008/04/shell-meme.html)

    jennifer:~ bwinton$ history|awk '{a[$2]++ } END{for(i in a){print a[i] " " i}}'|sort -rn | head
    86 ls
    80 bzr
    60 cd
    56 scp
    46 vi
    38 exit
    37 sudo
    25 xcodebuild
    13 spam
    7 ssh

I’m not sad about that set of commands.  I look around a lot, and
check stuff in a lot, and copy it to my iTouch most of the time.  I’m
sure xcodebuild would be higher in the list if I didn’t use Command-B
from inside the IDE.

