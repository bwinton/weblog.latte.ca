<!--
.. title: How to (not quite) fix a bug.
.. date: 2010-03-10 22:17:58
.. author: Blake Winton
.. tags: thunderbird, mozilla, debugging
-->

I’ve run into [a bug](https://bugzilla.mozilla.org/show_bug.cgi?id=545933
).  It’s a really annoying bug, because it prevents me from changing
folders when I try to test any of my Thunderbird changes.

I tried putting dump statements everywhere, to see if I could figure out
what was going on, but they were to no avail.  Then, I thought about
looking for the error code.

So the [error lookup page](
http://silver.warwickcompsoc.co.uk/mozilla/misc/nserror?0x805E0006) says
that the error that’s reported is:

    Module          Severity        Number
    CONTENT (25)	Failure (1)     6

And
[DXR](http://scotland.proximity.on.ca/dxr/mozilla-central/content/base/public/nsContentErrors.h.html#l59)
says that Content Error 6 is:
    NS_ERROR_CONTENT_BLOCKED

Which occurs, among other places,
[here](http://mxr.mozilla.org/comm-central/source/mozilla/content/base/src/nsDocument.cpp#1129)

But when I set a breakpoint there, it didn’t hit it.  So instead of
trusting mxr or dxr, I did a grep (well, an ack, but same thing), and
started setting breakpoints on a few of the hits.

The one that hit my breakpoint ended up being [this
one](http://mxr.mozilla.org/comm-central/source/mozilla/docshell/base/nsDocShell.cpp#7643)
which, weirdly enough, isn’t even listed in the mxr results of [this
search](http://mxr.mozilla.org/comm-central/ident?i=NS_ERROR_CONTENT_BLOCKED)

Now that I’m at the breakpoint, we’re halfway there, I hope.  ;)

How I got there was:

    (gdb) bt
    #0  nsDocShell::InternalLoad (…) at …/mozilla/docshell/base/nsDocShell.cpp:7643
    #1  0x152d9daa in nsDocShell::LoadURI (…) at …/mozilla/docshell/base/nsDocShell.cpp:1369
    #2  0x13dc7581 in nsLocation::SetURI (…) at …/mozilla/dom/base/nsLocation.cpp:316
    #3  0x13dc8af3 in nsLocation::SetHrefWithBase (…) at …/mozilla/dom/base/nsLocation.cpp:595
    #4  0x13dc8cf9 in nsLocation::SetHrefWithContext (…) at …/mozilla/dom/base/nsLocation.cpp:542
    #5  0x13dc9120 in nsLocation::SetHref (…) at …/mozilla/dom/base/nsLocation.cpp:510
    #6  0x003fa28e in NS_InvokeByIndex_P (…) at …/mozilla/xpcom/reflect/xptcall/src/md/unix/xptcinvoke_unixish_x86.cpp:179
    #7  0x120f88bb in XPCWrappedNative::CallMethod (…) at …/mozilla/js/src/xpconnect/src/xpcwrappednative.cpp:2727
    #8  0x1210c0c6 in XPCWrappedNative::SetAttribute (…) at xpcprivate.h:2550
    #9  0x12105530 in XPC_WN_GetterSetter (…) at …/mozilla/js/src/xpconnect/src/xpcwrappednativejsops.cpp:1792
    #10 0x001141a7 in js_Invoke (…) at jsinterp.cpp:1388
    […]

And it looks like we get there because the return value of
NS_CheckContentLoadPolicy is 0x80004003, or NS_ERROR_INVALID_POINTER.

Then, after dinner, I tracked it down a little further, and if you place a
breakpoint on the “\\n\\nAAAAAA\\nrv5=%x\\n” line in [this patch](
https://bug545933.bugzilla.mozilla.org/attachment.cgi?id=427516), you can
see that it’s the folder = do_QueryInterface(subFolder, &amp;rv); line
which is causing the failure, because the subFolder’s mRawPtr is null.

But I have no idea why _that_’s happening, so I posted what I had, and
hoped that someone else could take it and run with it.  And Bienvenu did,
and now it’s much less of a problem for me, and I can go work on other
things.

