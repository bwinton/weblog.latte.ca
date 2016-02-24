<!--
.. title: Programming Thunderbird in Visual Studio.
.. date: 2010-03-30 10:11:05
.. author: Blake Winton
.. tags: mozilla, thunderbird, ucosp
-->

For your reading pleasure this week, we have a guest post from [Wei Xian
Woo](mailto:wxwoo@uwaterloo.ca).  Wei is a student working on
[Thunderbird](http://www.mozillamessaging.com/) as part of
[UCOSP](http://ucosp.wordpress.com/), and has just had [his first
bug](https://bugzilla.mozilla.org/show_bug.cgi?id=408338) marked as
FIXED.  Anyways, that’s enough out of me.  Here’s Wei’s post:

> ###Programming Thunderbird in Visual Studio.###
> 
> During this term’s Undergraduate Capstone Open Source Projects (UCOSP)
> Code Sprint held at the University of Toronto in January, I wrote a
> simple Python script for the Thunderbird team to make setting up a
> Visual C++ project for Thunderbird slightly easier for those of us
> working on Windows. Blake suggested making this script public so others
> could benefit from it, so here it is! The script is generic enough to be
> used for any project, not just Thunderbird. Feel free to use it and make
> modifications as you see fit :)
> 
> ###Using the script to create a Visual C++ project for Thunderbird###
> 
> Create an empty Visual C++ project in Visual Studio.
> 
> From the command prompt launched by mozilla-build\start-msvc9.bat, do:
> 
>     python /path/to/refreshvcproj.py
>     --vcproj=/path/to/thunderbird.vcproj --dir=/path/to/gecko-sdk
>     --dir=/path/to/mozilla/comm-central/mozilla/xpcom
>     --dir=/path/to/mozilla/comm-central/mail
> 
> All files in the specified directories will be included in the project.
> I suggest including only the directories you will be working with.
> 
> ###Configuring the project for debugging:###
> 
> Open the VC++ project file in Visual Studio, and then open the project's
> Properties.
> 
> Go to: Configuration Properties -&gt; Debugging.
> 
> Set Command to \path\to\objdir\mozilla\dist\bin\thunderbird.exe
> 
> Set Environment to XPCOM_DEBUG_BREAK=warn
> 
> ###And… you’re done!###
> 
> For better C++ IntelliSense, you might also want to consider getting
> Visual Assist X (an add-on for VS).
> 
> ###Happy coding!###

And you can find the script [over here](/static/blake/refreshvcproj.py).

Thanks, Wei!

