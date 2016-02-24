<!--
.. title: DOM appendChild error in Gecko 2.0
.. date: 2010-11-30 10:58:11
.. author: Blake Winton
.. tags: mozilla, firefox, thunderbird
-->

I was recently modifying an add-on for the upcoming Thunderbird 3.3, and
part of what I wanted to do was to run some javascript in a chrome context
that added some DOM nodes to a document in a content context.  But when I
ran the following code:

    #!javascript
    let browser = document.getElementById('tabmail').getBrowserForSelectedTab();
    let doc = browser.contentDocument;
    dump("\n\n\n\nXXXXXXXXXX\n");
    dump("DOM Content loaded for " + doc.location + "\n");
    var topBar = document.createElement("div");
    topBar.innerHTML = "We got it!!!!!";
    dump("iB = "+doc.body.insertBefore+"\n");
    dump("fC = "+doc.body.firstChild+"\n");
    doc.body.insertBefore(topBar, doc.body.firstChild);

I got the following error:

    WARNING: NS_ENSURE_SUCCESS(rv, rv) failed with result 0x80530009: file /Volumes/Devel/thunderbird/src-central/mozilla/content/base/src/nsNodeUtils.h, line 304
    WARNING: NS_ENSURE_SUCCESS(rv, rv) failed with result 0x80530009: file /Volumes/Devel/thunderbird/src-central/mozilla/content/base/src/nsGenericElement.cpp, line 4077
    -- Exception object --
    [snip…]
    + message (string) 'Operation is not supported'
    + result (number) 2152923145
    + name (string) 'NS_ERROR_DOM_NOT_SUPPORTED_ERR'

Poking around a little, it seemed like I had reasonable things for the
<tt>insertBefore</tt> method, the <tt>firstChild</tt> attribute, and the
<tt>topBar</tt> variable, and so since it was late, and I couldn't see what
I had done wrong, I went to bed.


That turned out to be a the best thing for me to do, because this morning
[Jonathan Protzenko](http://blog.xulforum.org) came to the rescue, saying
([in response to a similar problem](
http://groups.google.com/group/mozilla.dev.extensions/browse_thread/thread/cd6f0f02b6bc60f4#)
with a Firefox 4.0 beta 7 extension):

> If you're modifying some content DOM from chrome code, you need to make
> sure the child you're appending was created using the unprivileged
> document, not the global document.
>
>     // This is chrome code, this is wrong because the span is now chrome
>     // and you're trying to insert it into content
>     myContentNode.appendChild(document.createElement("span"))
>
>     // This is right, appending a content node to another content node
>     myContentNode.appendChild(myContentNode.ownerDocument.createElement("span"))
>
> I've hit this issue at least three times when upgrading stuff for Gecko
> 2.0. Might be what you're looking for .

And sure enough, when I changed <tt>var topBar =
document.createElement("div");</tt> to <tt>var topBar =
doc.createElement("div");</tt>
, it all started working beautifully.

Thank you, Jonathan!

