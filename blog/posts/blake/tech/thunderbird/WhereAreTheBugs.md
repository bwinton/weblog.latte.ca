<!--
.. title: What files have the most bugs?
.. date: 2010-12-24 14:59:24
.. author: Blake Winton
.. tags: mozilla, thunderbird, making_software
-->

I was reading [Making Software](http://oreilly.com/catalog/9780596808303)
by Andy Oram and Greg Wilson, and got to the chapter about An Automated
Fault Prediction System.  It’s a pretty neat chapter, and it got me
wondering which files in the [Thunderbird code base](
http://mxr.mozilla.org/comm-central/) had the most bugs.  Now, I don’t have
all the info I need, but I figured an easy first pass would be to go
through the commit logs, and for each commit that started with “bug ”, add
one to the files changed in that commit.  Hmm, that sounded unintuitive.
Let me just paste ([and link](/static/blake/test.py)) the code:


    #!python
    from mercurial import ui, hg
    import operator
    import re
    
    ext = re.compile("(\.c(pp)?|\.js|\.xml)$")
    
    repo = hg.repository(ui.ui(), ".")
    changes = [repo[i] for i in repo
                       if repo[i].description().lower().startswith("bug ")]
    
    master = {}
    
    for change in changes:
      files = [f for f in change.files() if ext.search(f)]
      for f in files:
        master[f] = master.get(f, 0) + 1
    
    
    files = master.items()
    files.sort()
    counts = master.items()
    counts.sort(key=operator.itemgetter(1))
    counts.reverse()
    print "\n".join([c[0] + ":" + str(c[1]) for c in counts[:10]])

And so, without further ado, here are the files that have been changed the
most in bug fixes, and the number of times they've been changed:

* mail/base/content/mailWindowOverlay.js:109
* suite/browser/browser-prefs.js:73
* suite/browser/navigator.js:70
* mail/base/content/msgMail3PaneWindow.js:69
* mail/app/profile/all-thunderbird.js:67
* suite/common/src/nsSessionStore.js:66
* mail/components/compose/content/MsgComposeCommands.js:60
* mailnews/imap/src/nsImapMailFolder.cpp:56
* suite/browser/tabbrowser.xml:53
* mail/base/content/msgHdrViewOverlay.js:52

---

<small>As a side note, for the [mozilla repo](
http://mxr.mozilla.org/mozilla-central/) it looks like this:</small>

* <small>js/src/jstracer.cpp:780</small>
* <small>browser/base/content/browser.js:654</small>
* <small>layout/base/nsCSSFrameConstructor.cpp:410</small>
* <small>layout/base/nsPresShell.cpp:400</small>
* <small>js/src/jsobj.cpp:399</small>
* <small>browser/base/content/tabbrowser.xml:397</small>
* <small>widget/src/windows/nsWindow.cpp:390</small>
* <small>toolkit/components/places/src/nsNavHistory.cpp:374</small>
* <small>js/src/jsinterp.cpp:345</small>
* <small>js/src/jsapi.cpp:343</small>

