# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479403432.9861379
_enable_loop = True
_template_filename = 'themes/latte/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_translations', 'html_post_header', 'html_title']


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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def html_title():
            return render_html_title(context)
        messages = context.get('messages', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def html_translations(post):
            return render_html_translations(context,post)
        post = context.get('post', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
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
{"filename": "themes/latte/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"128": 41, "129": 41, "130": 41, "131": 41, "132": 41, "133": 43, "134": 44, "135": 44, "136": 44, "137": 46, "138": 47, "139": 47, "145": 5, "154": 7, "23": 2, "152": 6, "153": 7, "26": 3, "155": 7, "156": 7, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 49, "45": 24, "157": 7, "163": 157, "52": 24, "53": 25, "54": 26, "55": 26, "56": 26, "57": 26, "58": 26, "151": 5, "64": 11, "72": 11, "73": 12, "74": 13, "75": 14, "76": 14, "77": 15, "78": 16, "79": 17, "80": 17, "81": 17, "82": 17, "83": 17, "84": 17, "85": 17, "86": 20, "92": 30, "107": 30, "108": 32, "109": 32, "110": 34, "111": 34, "112": 35, "113": 35, "114": 35, "115": 35, "116": 35, "117": 35, "118": 35, "119": 35, "120": 36, "121": 37, "122": 37, "123": 37, "124": 39, "125": 39, "126": 39, "127": 40}}
__M_END_METADATA
"""
