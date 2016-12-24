# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1482613975.559331
_enable_loop = True
_template_filename = 'themes/latte/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_translations', 'html_sourcelink', 'html_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_title():
            return render_html_title(context)
        def html_translations(post):
            return render_html_translations(context,post)
        def html_sourcelink():
            return render_html_sourcelink(context)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
        __M_writer(str(post.author()))
        __M_writer('</span></p>\n            <p class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time></a></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post.permalink(extension='').replace('.html', ''))))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer("                    <p><a href='")
            __M_writer(str(post.meta('link')))
            __M_writer("'>")
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        if post.description():
            __M_writer('                <meta name="description" itemprop="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_header.tmpl", "line_map": {"133": 24, "134": 25, "135": 26, "136": 26, "137": 26, "138": 26, "139": 26, "145": 5, "154": 7, "23": 2, "151": 5, "153": 7, "26": 3, "155": 7, "156": 7, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 49, "45": 30, "152": 6, "157": 7, "163": 157, "60": 30, "61": 32, "62": 32, "63": 34, "64": 34, "65": 35, "66": 35, "67": 35, "68": 35, "69": 35, "70": 35, "71": 35, "72": 35, "73": 36, "74": 37, "75": 37, "76": 37, "77": 39, "78": 39, "79": 39, "80": 40, "81": 41, "82": 41, "83": 41, "84": 41, "85": 41, "86": 43, "87": 44, "88": 44, "89": 44, "90": 46, "91": 47, "92": 47, "98": 11, "106": 11, "107": 12, "108": 13, "109": 14, "110": 14, "111": 15, "112": 16, "113": 17, "114": 17, "115": 17, "116": 17, "117": 17, "118": 17, "119": 17, "120": 20, "126": 24}, "filename": "themes/latte/templates/post_header.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""
