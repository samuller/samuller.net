"""Markdown extension that protects LaTeX inside $$...$$ blocks from HTML escaping.

Python-Markdown's serializer always escapes & to &amp; in text nodes, which
breaks align environments that use & as a column separator. This preprocessor
replaces & with a safe placeholder before any processing, and a postprocessor
restores it in the final HTML so MathJax receives valid LaTeX.
"""

import markdown
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor

_PLACEHOLDER = "XMATHAMPERSANDX"


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
                new_lines.append(line)
        return new_lines


class _MathRestorePostprocessor(Postprocessor):
    def run(self, text):
        return text.replace(_PLACEHOLDER, "&")


class MathBlockProtectExtension(markdown.Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(_MathProtectPreprocessor(md), "math_protect", 200)
        md.postprocessors.register(_MathRestorePostprocessor(), "math_restore", 200)


def makeExtension(**kwargs):
    return MathBlockProtectExtension(**kwargs)
