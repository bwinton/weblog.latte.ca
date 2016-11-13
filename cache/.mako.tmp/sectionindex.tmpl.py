# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479067713.9872544
_enable_loop = True
_template_filename = '/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/nikola/data/themes/base/templates/sectionindex.tmpl'
_template_uri = 'sectionindex.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        generate_atom = context.get('generate_atom', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_atom = context.get('generate_atom', UNDEFINED)
        def content():
            return render_content(context)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="sectionindex">\n    <header>\n        <h2><a href="')
        __M_writer(str(_link('section_index', posts[0].section_slug())))
        __M_writer('">')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</a></h2>\n')
        if generate_atom:
            __M_writer('            <p class="feedlink"><a href="')
            __M_writer(str(_link('section_index_atom', posts[0].section_slug())))
            __M_writer('" type="application/atom+xml">')
            __M_writer(str(messages('Updates')))
            __M_writer('</a></p>\n')
        __M_writer('    </header>    \n    ')
        __M_writer(str(parent.content()))
        __M_writer('\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_atom = context.get('generate_atom', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if generate_atom:
            __M_writer('        <link rel="alternate" type="application/atom+xml" title="Atom for the ')
            __M_writer(filters.html_escape(str(posts[0].section_name())))
            __M_writer(' section" href="')
            __M_writer(str(_link('section_index_atom', posts[0].section_slug())))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/nikola/data/themes/base/templates/sectionindex.tmpl", "line_map": {"70": 11, "71": 14, "72": 14, "73": 14, "74": 14, "75": 15, "76": 16, "77": 16, "78": 16, "79": 16, "80": 16, "81": 18, "82": 19, "83": 19, "89": 4, "27": 0, "99": 4, "100": 5, "101": 5, "102": 6, "103": 7, "104": 7, "105": 7, "42": 2, "107": 7, "47": 9, "113": 107, "52": 21, "58": 11, "106": 7}, "uri": "sectionindex.tmpl"}
__M_END_METADATA
"""
