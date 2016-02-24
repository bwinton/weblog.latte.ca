<!--
.. title: How to start developing Basie
.. date: 2008-08-27 17:03:24
.. author: Blake Winton
.. tags: python, drproject, django, basie
-->

So, first off, I think Python developers these days need to use stuff
like virtualenv and zc.buildout in order to develop in a sane manner.
Yeah, this is the first project I’m using them on, but do what I say,
not what I do.

Anyways, on to the instructions.

    sudo easy_install virtualenv
    virtualenv --no-site-packages basie
    cd basie/
    . bin/activate

Then, you’re gonna need a
[buildout.cfg](http://bwinton.latte.ca/Programming/Basie/buildout.cfg).
Mine looks like this:

    #!ini
    [buildout]
    parts = django
    eggs = ipython
    
    [django]
    recipe = djangorecipe
    version = trunk
    settings = development
    eggs = ${buildout:eggs}
    project = basie
    wsgi = true
    
You’ll also need a
[bootstrap.py](http://bwinton.latte.ca/Programming/Basie/bootstrap.py),
which will look a little something like this:


    #!python
    ##############################################################################
    #
    # Copyright (c) 2006 Zope Corporation and Contributors.
    # All Rights Reserved.
    #
    # This software is subject to the provisions of the Zope Public License,
    # Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
    # THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
    # WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    # WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
    # FOR A PARTICULAR PURPOSE.
    #
    ##############################################################################
    """Bootstrap a buildout-based project
    
    Simply run this script in a directory containing a buildout.cfg.
    The script accepts buildout command-line options, so you can
    use the -c option to specify an alternate configuration file.
    
    $Id$
    """
    
    import os, shutil, sys, tempfile, urllib2
    
    tmpeggs = tempfile.mkdtemp()
    
    try:
        import pkg_resources
    except ImportError:
        ez = {}
        exec urllib2.urlopen('http://peak.telecommunity.com/dist/ez_setup.py'
                             ).read() in ez
        ez['use_setuptools'](to_dir=tmpeggs, download_delay=0)
    
        import pkg_resources
    
    if sys.platform == 'win32':
        def quote(c):
            if ' ' in c:
                return '"%s"' % c # work around spawn lamosity on windows
            else:
                return c
    else:
        def quote (c):
            return c
    
    cmd = 'from setuptools.command.easy_install import main; main()'
    ws  = pkg_resources.working_set
    assert os.spawnle(
        os.P_WAIT, sys.executable, quote (sys.executable),
        '-c', quote (cmd), '-mqNxd', quote (tmpeggs), 'zc.buildout',
        dict(os.environ,
             PYTHONPATH=
             ws.find(pkg_resources.Requirement.parse('setuptools')).location
             ),
        ) == 0
    
    ws.add_entry(tmpeggs)
    ws.require('zc.buildout')
    import zc.buildout.buildout
    zc.buildout.buildout.main(sys.argv[1:] + ['bootstrap'])
    shutil.rmtree(tmpeggs)


After you’ve got those, it’s basically:

    python bootstrap.py
    buildout -v
    django help
    django runserver
And when you’re done,
    deactivate

Any comments on things that don’t work would be highly appreciated.

