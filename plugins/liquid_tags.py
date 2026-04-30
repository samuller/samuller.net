"""
Python-Markdown extension: Jekyll-compatible Liquid tag support.

Handles two constructs found in Jekyll/Kramdown markdown files:

  {% comment %}...{% endcomment %}
      Stripped entirely — used for author notes not meant for output.

  {% include template.html key="value" ... %}
      Expanded to HTML. Supported templates mirror _includes/:
        image.html                  — <figure> with image and caption
        header-with-image-link.html — page header with optional ref-toggle
                                      and optional PDF link
      The header template respects the page's Style metadata to decide
      whether to render the ref_toggle button.
"""
import re
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

_COMMENT_RE = re.compile(
    r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', re.DOTALL
)
_INCLUDE_RE = re.compile(
    r'\{%-?\s*include\s+(\S+)\s*(.*?)-?%\}', re.DOTALL
)
_ARG_RE = re.compile(r'(\w+)="([^"]*)"')


def _parse_args(s):
    return {m.group(1): m.group(2) for m in _ARG_RE.finditer(s)}


def _render_image(args, _page_style):
    url = args.get('url', '')
    alt = args.get('alt', '')
    desc = args.get('description', '')
    return (
        '<figure class="image">\n'
        f'    <img src="{url}" alt="{alt}" class="hover-highlight">\n'
        f'    <figcaption>{desc}</figcaption>\n'
        '</figure>'
    )


def _render_header_with_image_link(args, page_style):
    text = args.get('text', '')
    img_src = args.get('img_src', '')
    img_alt = args.get('img_alt', '')
    title = args.get('title', '')
    link = args.get('link', '')

    parts = ['<span style="height: 1.8em; margin: 0.5em;" class="float-right">']
    if 'ref_toggle' in page_style:
        parts.append(
            '<span title="Hide/show references"\n'
            '    style="vertical-align: middle; padding: 0.5em;'
            ' background-color: rgba(255,255,255,0.1);" class="darken-till-hover"\n'
            '    onclick="toggleRefLinks()">\n'
            '    <strong>[ ]</strong>\n'
            '</span>'
        )
    if img_src:
        parts.append(
            f'<a href="{link}" title="{title}">\n'
            f'    <img src="{img_src}" alt="{img_alt}" style="height: 1.8em"'
            f' class="float-right darken-till-hover">\n'
            '</a>'
        )
    parts.append('</span>')
    parts.append(f'<h1 style="clear:none">{text}</h1>')
    return '\n'.join(parts)


_HANDLERS = {
    'image.html': _render_image,
    'header-with-image-link.html': _render_header_with_image_link,
}


class _LiquidPreprocessor(Preprocessor):
    def run(self, lines):
        text = '\n'.join(lines)

        # Read page style from Pelican frontmatter so include handlers can use it
        m = re.search(r'^[Ss]tyle\s*:\s*(.+)$', text, re.MULTILINE)
        page_style = m.group(1).strip() if m else ''

        text = _COMMENT_RE.sub('', text)

        def _expand(m):
            handler = _HANDLERS.get(m.group(1))
            if handler:
                return handler(_parse_args(m.group(2)), page_style)
            return f'<!-- unknown include: {m.group(1)} -->'

        text = _INCLUDE_RE.sub(_expand, text)
        return text.split('\n')


class LiquidTagsExtension(Extension):
    def extendMarkdown(self, md):
        # Priority 35: run before kramdown_ial preprocessor (32) so comment/include
        # lines are resolved before the IAL preprocessor sees them.
        md.preprocessors.register(_LiquidPreprocessor(md), 'liquid_tags', 35)


def makeExtension(**kwargs):
    return LiquidTagsExtension(**kwargs)
