# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479051342.0772002
_enable_loop = True
_template_filename = '/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/nikola/data/themes/base/templates/author.tmpl'
_template_uri = 'author.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        description = context.get('description', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        author = context.get('author', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        author = context.get('author', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(author)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", author, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(author)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", author)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        description = context.get('description', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        len = context.get('len', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        author = context.get('author', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="authorpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        __M_writer('        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", author, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", author)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 21, "129": 21, "130": 21, "131": 23, "132": 24, "133": 25, "134": 26, "135": 27, "136": 27, "137": 27, "138": 27, "139": 27, "140": 27, "141": 27, "142": 27, "143": 30, "144": 31, "145": 31, "146": 31, "147": 31, "148": 31, "149": 33, "150": 35, "151": 36, "152": 37, "153": 38, "154": 38, "27": 0, "156": 38, "157": 38, "158": 38, "159": 38, "160": 38, "161": 38, "162": 38, "155": 38, "164": 40, "163": 38, "171": 165, "49": 2, "54": 13, "59": 43, "65": 4, "79": 4, "80": 5, "81": 5, "82": 6, "83": 7, "84": 8, "85": 8, "86": 8, "87": 8, "88": 8, "89": 8, "90": 8, "91": 8, "92": 8, "93": 10, "94": 11, "95": 11, "96": 11, "97": 11, "98": 11, "99": 11, "100": 11, "165": 42, "106": 16, "124": 16, "125": 19, "126": 19, "127": 20}, "uri": "author.tmpl", "filename": "/home/travis/virtualenv/python3.4.2/lib/python3.4/site-packages/nikola/data/themes/base/templates/author.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
