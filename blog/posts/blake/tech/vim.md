<!--
.. title: Home again…
.. date: 2009-02-02 15:48:35
.. author: Blake Winton
.. tags: emacs, vim, editors, switching, python, lisp
-->

A while ago, I downloaded Aquamacs, an emacs port for OSX, and tried
to switch to it as my default editor.  I mainly did it because I
wanted an editor I could add functionality to, à la [Steve Yegge](
http://steve.yegge.googlepages.com/effective-emacs).  I used it for a
while, and got fairly proficient at it.  There were a lot of things
about it I really liked, like the [Markdown mode](
http://jblevins.org/projects/markdown-mode/), and the ability to edit
files [on a remote host](
http://jeremy.zawodny.com/blog/archives/000983.html), and the way I
could write small functions in [elisp](
http://www.gnu.org/software/emacs/manual/html_mono/elisp.html) and use
them to make me more productive.

But while it worked, and worked well, I didn’t really write all that
much extra elisp, and whenever I did, I didn’t really enjoy it.  So
the other day, when I found myself [reading a weblog](
http://weblog.jamisbuck.org/2005/4/10/text-editing-dilemma) about the
lack of a good graphical text editor on OSX, I found myself agreeing
with him.  So when I read [a later article](
http://weblog.jamisbuck.org/2008/10/10/coming-home-to-vim) on how the
author had finally switched back to vim, I thought that I might give
vim another chance.

Well, it turns out that vim is actually pretty close to a perfect text
editor for me.  It’s got [Markdown support](
http://plasticboy.com/markdown-vim-mode/), [remote file editing](
http://www.petersblog.org/node/466), and not only can I write
functions for it, I can [write them](
http://www.vim.org/htmldoc/if_pyth.html) in
[Python](http://python.org/)!  As an example, here’s Steve Yegge’s
blog-check function in vim/python:

    #!vim
    function! BlogCheck()
      python << END
    :::python
    import re
    import vim
    pattern = re.compile( r"\s" )
    count = 0
    for line in vim.current.buffer:
      line = pattern.sub( "", line )
      count += len(line)
    if count <= 5000:
      message = "Okay so far"
    else:
      message = "Dude, too long"
    print "%s:  %d chars, %d words" % (message, count, count/5)
    :::vim
    END
    endfunction

