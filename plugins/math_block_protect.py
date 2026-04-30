"""Markdown extension that protects $...$ and $$...$$ math content.

Two separate problems require two separate fixes:

1. The HTML serializer always escapes & to &amp; in text nodes.
   Fix: a preprocessor replaces & inside math spans with a placeholder before
   any processing; a postprocessor restores it in the final HTML.

2. Python-Markdown's inline processors (emphasis, escape, etc.) would mangle
   _, \\, and other special chars inside math.
   Fix: inline Pattern handlers wrap matched math in AtomicString, which marks
   the text as off-limits to further inline processing.

Together these replace pelican-render-math's markdown handling without
converting \\begin{env}...\\end{env} to block math — MathJax handles those
directly in the browser via the surrounding $...$ delimiters.
"""

import re
from xml.etree.ElementTree import Element

import markdown
from markdown.inlinepatterns import Pattern
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor
from markdown.treeprocessors import Treeprocessor
from markdown.util import AtomicString

_PLACEHOLDER = "XMATHAMPERSANDX"
# Matches $...$ but not $$
_INLINE_MATH_RE = re.compile(r'(?<!\$)\$(?!\$)(.*?)\$')


def _protect_inline_amps(line):
    def replace_amp(m):
        return '$' + m.group(1).replace('&', _PLACEHOLDER) + '$'
    return _INLINE_MATH_RE.sub(replace_amp, line)


class _MathProtectPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        in_block = False
        for line in lines:
            if line.strip() == "$$":
                in_block = not in_block
                new_lines.append(line)
            elif in_block:
                new_lines.append(line.replace("&", _PLACEHOLDER))
            else:
                new_lines.append(_protect_inline_amps(line))
        return new_lines


class _DisplayMathPattern(Pattern):
    """Wraps $$...$$ in <div class="math"> with AtomicString."""

    def handleMatch(self, m):
        node = Element("div")
        node.set("class", "math")
        node.text = AtomicString("$$" + m.group("math") + "$$")
        return node


class _InlineMathPattern(Pattern):
    """Wraps $...$ in <span class="math"> with AtomicString."""

    def handleMatch(self, m):
        node = Element("span")
        node.set("class", "math")
        node.text = AtomicString("$" + m.group("math") + "$")
        return node


class _CorrectDisplayMath(Treeprocessor):
    """Move <div class="math"> elements outside of enclosing <p> tags.

    A block-level <div> inside <p> is invalid HTML. This mirrors what
    pelican-render-math's PelicanMathJaxCorrectDisplayMath treeprocessor does.
    """

    def run(self, root):
        for parent in list(root):
            children = list(parent)
            div_math = [
                i for i, el in enumerate(children)
                if el.tag == "div" and el.get("class") == "math"
            ]
            if not div_math:
                continue

            insert_idx = list(root).index(parent)
            current_idx = 0
            text = parent.text

            for idx in div_math:
                p = Element("p")
                p.text = text
                p.extend(children[current_idx:idx])
                if len(p) != 0 or (p.text and not p.text.isspace()):
                    root.insert(insert_idx, p)
                    insert_idx += 1

                text = children[idx].tail
                children[idx].tail = None
                root.insert(insert_idx, children[idx])
                insert_idx += 1
                current_idx = idx + 1

            p = Element("p")
            p.text = text
            p.extend(children[current_idx:])
            if len(p) != 0 or (p.text and not p.text.isspace()):
                root.insert(insert_idx, p)

            root.remove(parent)

        return root


class _MathRestorePostprocessor(Postprocessor):
    def run(self, text):
        return text.replace(_PLACEHOLDER, "&")


class MathBlockProtectExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(_MathProtectPreprocessor(md), "math_protect", 200)
        # Priority 5 < RawPostprocessor (30), so we run after the HTML stash is
        # restored — otherwise XMATHAMPERSANDX inside raw HTML blocks (e.g. a
        # $$...$$ inside a <div>) would never be replaced.
        md.postprocessors.register(_MathRestorePostprocessor(), "math_restore", 5)
        # Priority 186 > 185 so $$...$$ is claimed before $...$ can match.
        md.inlinePatterns.register(
            _DisplayMathPattern(r"(?P<prefix>\$\$)(?P<math>.+?)(?P<suffix>\$\$)"),
            "math_display",
            186,
        )
        md.inlinePatterns.register(
            _InlineMathPattern(r"(?P<prefix>\$)(?P<math>.+?)(?P<suffix>(?<!\s)\$)"),
            "math_inline",
            185,
        )
        md.treeprocessors.register(_CorrectDisplayMath(md), "math_correct_display", 15)


def makeExtension(**kwargs):
    return MathBlockProtectExtension(**kwargs)
