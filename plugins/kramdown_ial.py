"""
Python-Markdown extension: Kramdown-style block Inline Attribute Lists (IAL).

Kramdown allows applying attributes to a block element by placing an IAL on
the immediately following line (with no blank line between):

    Some paragraph.
    {: .class style="color: red"}

    - list item
    {: #my-list}

This extension replicates that behaviour as a TreeProcessor: after the markdown
tree is built it finds any <p> whose sole content matches the IAL pattern
{: ... } or { ... }, applies the parsed attributes to the immediately preceding
sibling element, then removes the placeholder <p>.
"""
import re
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.treeprocessors import Treeprocessor

_IAL_RE = re.compile(r'^\{:?\s*(.*?)\s*\}$', re.DOTALL)

_ATTR_RE = re.compile(
    r'(\w[\w-]*)="([^"]*)"'    # key="value"
    r"|(\w[\w-]*)='([^']*)'"   # key='value'
    r'|(\w[\w-]*)=([\w-]+)'    # key=barevalue
    r'|\.([\w-]+)'             # .classname
    r'|#([\w-]+)'              # #id
)


def _parse_ial(ial_content):
    attrs = {}
    classes = []
    for m in _ATTR_RE.finditer(ial_content):
        if m.group(1) is not None:
            attrs[m.group(1)] = m.group(2)
        elif m.group(3) is not None:
            attrs[m.group(3)] = m.group(4)
        elif m.group(5) is not None:
            attrs[m.group(5)] = m.group(6)
        elif m.group(7) is not None:
            classes.append(m.group(7))
        elif m.group(8) is not None:
            attrs['id'] = m.group(8)
    if classes:
        attrs['class'] = ' '.join(classes)
    return attrs


def _apply_attrs(element, attrs):
    for key, val in attrs.items():
        if key == 'class':
            existing = element.get('class', '')
            element.set('class', f'{existing} {val}'.strip())
        else:
            element.set(key, val)


_IAL_LINE_RE = re.compile(r'^\{:?\s*.*?\s*\}$')


class _IALPreprocessor(Preprocessor):
    """Ensure every bare IAL line is surrounded by blank lines so the block
    parser sees it as its own paragraph rather than merging it with neighbours."""

    def run(self, lines):
        out = []
        for line in lines:
            if _IAL_LINE_RE.match(line.strip()):
                if out and out[-1] != '':
                    out.append('')
                out.append(line)
                out.append('')
            else:
                out.append(line)
        return out


class _IALTreeProcessor(Treeprocessor):
    def run(self, root):
        self._process(root)

    def _process(self, parent):
        to_remove = []
        prev = None
        for child in parent:
            self._process(child)
            if child.tag == 'p' and child.text and len(child) == 0:
                m = _IAL_RE.match(child.text.strip())
                if m and prev is not None:
                    _apply_attrs(prev, _parse_ial(m.group(1)))
                    to_remove.append(child)
                    continue
            prev = child
        for elem in to_remove:
            parent.remove(elem)


class KramdownIALExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(_IALPreprocessor(md), 'kramdown_ial', 32)
        md.treeprocessors.register(_IALTreeProcessor(md), 'kramdown_ial', 5)


def makeExtension(**kwargs):
    return KramdownIALExtension(**kwargs)
