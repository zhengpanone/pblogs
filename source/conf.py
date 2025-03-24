# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = "Python Blog"
copyright = '2019, 郑攀'
author = 'PanZheng'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

simplepdf_vars = {
    'primary': '#333333',
    'links': '#FF3333',
}

extensions = [
    'chinese_search', 
    'recommonmark', 
    'sphinx_markdown_tables',
    # 'sphinxcontrib.inkscapeconverter',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    ]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.rst', '.md']
source_encoding = 'utf-8'
# The master toctree document.
master_doc = 'index'

language = 'zh_CN'


exclude_patterns = []

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
htmlhelp_basename = 'Python BLOG'

formats = ["htmlzip", "pdf", "epub"]

latex_engine = 'xelatex'

latex_elements = {  
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',  
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '16pt',
    'preamble': '',
    'figure_align': 'htbp',
    'preamble': r'\usepackage{bookmark}'
    } 
# Additional stuff for the LaTeX preamble.
# 'preamble': """\usepackage{xeCJK} \setlength{\parindent}{2em}\setCJKmainfont{WenQuanYi Micro Hei} \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}  \setCJKfamilyfont{song}{WenQuanYi Micro Hei} \setCJKfamilyfont{sf}{WenQuanYi Micro Hei} \XeTeXlinebreaklocale "zh"\XeTeXlinebreakskip = 0pt plus 1pt"""


# 'preamble': r"""\usepackage{xeCJK}\usepackage{indentfirst}\setlength{\parindent}{2em}\setCJKmainfont{WenQuanYi Micro Hei}\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}\setCJKfamilyfont{song}{WenQuanYi Micro Hei}\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}\XeTeXlinebreaklocale "zh"\XeTeXlinebreakskip = 0pt plus 1pt

latex_documents = [
    ('index', 'mkdocs.tex', u'《Python博客》',
     u'郑攀', 'howto'),
]

man_pages = [
    ('index', 'python3-blog', '《Python博客》',
     ['郑攀'], 1)
]

texinfo_documents = [
    ('index', 'Python-blog', '《Python博客》',
     '郑攀', 'Python-blog', '《Python博客》',
     'Miscellaneous'),
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


highlight_langeuage = "python,go,javascript,html"
_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
