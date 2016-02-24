<!--
.. title: How to add Markdown to your PyBlosxom Blog.
.. date: 2008-02-27 12:16:41
.. author: Blake Winton
.. tags: python, markdown, drproject, pyblosxom
-->

Hopefully this all just works.  Include A&B, and 4 < 5.

Headers
=======

## Smaller headers ##

> Blockquotes.

* Lists
* of 
* things

    Blocks of python code could be here.

---

*etc*, **etc**.

Okay, so now that I’ve determined that it works, here’s how I did it:
I added a new entry parser, called pymarkdown.py, to my plugins
directory.  The content of the code looks like this:

    FILE_EXT = 'md'
    
    __version__ = 'pymarkdown 0.1'
    __author__ = 'Blake Winton <bwinton+python@latte.ca>'
    
    import markdown
    
    try:
        from Pyblosxom import tools
    except ImportError:
        pass
    
    def cb_entryparser(entryparsingdict):
           """
           Register self as markdown file handler
           """
           entryparsingdict[FILE_EXT] = parse
           return entryparsingdict
    
    def parse(filename, request):
        """
        We just read everything off the file here, using the filename as
        title
        """
        entrydata = {}
    
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
    
        # strip off the first line and use that as the title.
        title = lines.pop(0).strip()
        entrydata['title'] = title
    
        # absorb meta data lines which begin with a # and consist
        # of a name and a value
        while lines and lines[0].startswith("#"):
            meta = lines.pop(0)
            meta = meta[1:].strip()     # remove the hash
            meta = meta.split(" ", 1)
            entrydata[meta[0].strip()] = meta[1].strip()
    
        # join the rest of the lines as the story
        story = ''.join(lines)
        story = markdown.markdown( story )
        entrydata['body'] = story
    
        return entrydata
And you’re done.

I guess you might be wondering why I would bother doing that, since
both Amy and I are obviously comfortable writing straight HTML.  Well,
[DrProject](http://www.drproject.org/) is switching from a
custom-built Wiki-ish-syntax parser to a [third-party](
http://www.freewisdom.org/projects/python-markdown/ ) Markdown parser,
and I figured this would give me a bit of a headstart on getting used
to the new syntax, and also give me a bit of a playground for testing
out new features that I might want to add.

