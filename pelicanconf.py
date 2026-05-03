import csv
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'))

AUTHOR = 'Simon Müller'
SITENAME = 'Simon Müller'
SITESUBTITLE = 'Quotes and notes'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
THEME_STATIC_DIR = ''  # copy theme/static/* to output root (keeps /css/, /js/, /fonts/ paths)

TIMEZONE = 'Africa/Johannesburg'
DEFAULT_LANG = 'en'

MENUITEMS = [
    ('Home', '/'),
    ('Quotes', '/quotes/'),
    ('Notes', '/notes/'),
    ('About', '/about/'),
]

# Mirror Jekyll URL structure — extract path without 'pages/' prefix or extension
PATH_METADATA = r'pages/(?P<page_path>.+?)(?:\.[^.]+)?$'
PAGE_URL = '{page_path}/'
PAGE_SAVE_AS = '{page_path}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Disable auto-generated listing pages we don't use
INDEX_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

STATIC_PATHS = ['extra']
# Exclude the extra dir from page/article processing — it's static files only
PAGE_EXCLUDES = ['extra']
ARTICLE_EXCLUDES = ['extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME':     {'path': 'CNAME'},
    'extra/.nojekyll': {'path': '.nojekyll'},
}

# Quotes page and its JS bundle are rendered as Jinja2 templates so that
# quotes_data (loaded below) is available when they render.
TEMPLATE_PAGES = {
    'quotes/index.html':  'quotes/index.html',
    'quotes/quotes.json': 'quotes/quotes.json',
    'workout/a.html':     'workout/a.html',
    'workout/b.html':     'workout/b.html',
}

PLUGINS = ['pelican.plugins.sitemap', 'jinja2content']

SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/', 'author/', 'archives/'],
}

GOOGLE_ANALYTICS = 'UA-120258429-1'

# Load quote TSV files at config time so they're available as quotes_data
# in every Jinja2 template (including the TEMPLATE_PAGES quotes.json).
def _load_quotes():
    data_dir = os.path.join(os.path.dirname(__file__), '_data', 'quotes')
    quotes = {}
    if os.path.isdir(data_dir):
        for fname in sorted(os.listdir(data_dir)):
            if fname.endswith('.tsv'):
                with open(os.path.join(data_dir, fname), newline='', encoding='utf-8') as f:
                    quotes[fname[:-4]] = list(csv.DictReader(f, delimiter='\t'))
    return quotes

def _strip_style_blocks(text):
    return re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)

JINJA_FILTERS = {
    'strip_style_blocks': _strip_style_blocks,
}

JINJA_GLOBALS = {
    'now': datetime.now,
    'quotes_data': _load_quotes(),
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.attr_list': {},
        'kramdown_ial': {},
        'math_block_protect': {},
    },
    'output_format': 'html5',
}
