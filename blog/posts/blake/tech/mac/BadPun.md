<!--
.. title: Snakes on an Apple!
.. date: 2006-08-24 22:23:00
.. author: Blake Winton
.. tags: mac
-->

As I <a href="http://weblog.latte.ca/firstpost.html">mentioned
before</a>, we got a Mac Mini.  It's been a bit of a pain getting it all
set up, but I think we're finally done.  The web server is moved over,
along with all the websites.  The mail server is moved over, and I took
the opportunity to delete my mother's account.  (That's not as bad as it
sounds.  She had it redirecting to GMail anyways, and the error message
says as much.  Of course, since I haven't told her about it yet, this
will probably come as a bit of a surprise.)  Uh, and that turned out to
be all the servers I was running.  Well, I was running CherryPy, and
some other stuff, but it wasn't particularly important, and I've found
better ways of doing it, for the most part.

But that's not really why I'm posting here.  I'm posting here because
I got some cool Python stuff working under the Mac, and I wanted to
share it.  Specifically, I (or rather, my wife and I) wanted to have a
window showing on the login screen, displaying <a
href="http://weatheroffice.ec.gc.ca/city/pages/on-143_metric_e.html">the
weather</a>.  After several bits of trial and error, and liberal
"borrowing" from <a href="http://livingcode.org/">Dethe Elza</a>'s <a
href="http://livingcode.org/project/pastels/">Pastels project</a> I
finally got something which would do what I wanted.  First, the code:

    #!python
    from AppKit import NSObject, NSApplication, NSTimer, NSApp, NSURL
    from AppKit import NSURLRequest, NSWindow, NSTitledWindowMask
    from AppKit import NSClosableWindowMask, NSMiniaturizableWindowMask
    from AppKit import NSResizableWindowMask, NSBackingStoreBuffered
    from BeautifulSoup import BeautifulSoup
    from PyObjCTools import AppHelper
    from WebKit import WebView, WebDataSource
    
    import os
    import stat
    import time
    import urllib
    
    width, height = 620, 540
    
    def Window(title, width, height, view=None):
        window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            ((0,0),(width,height)),
            NSTitledWindowMask |
            NSClosableWindowMask | 
            NSMiniaturizableWindowMask |
            NSResizableWindowMask,
            NSBackingStoreBuffered,
            False)
        window.setTitle_(title)
        if view:
            window.setContentView_(view)
        window.orderFront_(window)
        return window
    
    class MyAppDelegate(NSObject):
        def update( self, timer ):
            y = urllib.urlopen( str(self.wUrl) ).read()
            b = BeautifulSoup( y )
            self.view.mainFrame().loadHTMLString_baseURL_(
                """<html><head><title>test<title>%s<head>
                <body>%s<body><html>""" %
                ("".join( [str(x) for x in b.head.findAll( 'style' )]), b.body.div.div.div.div.div),
                self.wUrl )
    
        def applicationDidFinishLaunching_(self, notification):
            rect = ((0,0),(width, height))
            self.view = WebView.alloc().initWithFrame_(rect)
            self.window = Window('Pastels Test', width, height, self.view)
            self.window_delegate = MyWindowDelegate.alloc().init()
            self.window.setDelegate_(self.window_delegate)
            self.wUrl = NSURL.alloc().initWithString_(
                "http://weatheroffice.ec.gc.ca/city/pages/on-143_metric_e.html")
            self.update( None )
            timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                1800, self, 'update', None, True )
            
    class MyWindowDelegate(NSObject):
        def windowWillClose_(self, notification):
            NSApp().terminate_(self)
    
    def main():
        app_delegate = MyAppDelegate.alloc().init()
        NSApplication.sharedApplication().setDelegate_(app_delegate)   
        AppHelper.runEventLoop(installInterrupt=True)
    
    
    if __name__ == "__main__":
        while True:
            if os.stat( "/dev/console" )[stat.ST_UID] == 0:
                # If the console is owned by root, start the app.
                main()
            else:
                # Otherwise, sleep until it is.
                time.sleep( 10 )

<br/>
And next, the launchd plist file that keeps it running:

    #!xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
    "http://www.apple.
    com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>  
        <key>Label</key>
        <string>ca.latte.update.login.weather</string>
        <key>ProgramArguments</key>
        <array> 
            <string>/path/to/test.py</string>
        </array>
        <key>ServiceDescription</key>
        <string>A program to pop up the weather in a box</string>
        <key>LowPriorityIO</key>
        <true/>
        <key>RunAtLoad</key>
        <true/>
        <key>OnDemand</key>
        <false/>
        <key>Nice</key>
        <integer>1</integer>
        <key>StandardOutPath</key>
        <string>/path/to/loginWeather.out</string>
        <key>StandardErrorPath</key>
        <string>/path/to/loginWeather.err</string>
    </dict>
    </plist>

And there you have it.  Way cooler than my previous attempt, which tried
to write using <tt>sudo defaults write
/Library/Preferences/com.apple.loginwindow LoginwindowText -string
"parsed weather info here"</tt>.

If any of you have any questions, I'ld love to answer them as best I
can. Just comment, and I'll see what I can dig up.  By which I mean
email Dethe, and ask him.  ;)

