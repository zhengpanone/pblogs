# -*- coding: utf-8 -*-
import os
import sys
import sphinx_rtd_theme
import platform

_exts = "extensions"
sys.path.insert(0,os.path.join(os.path.abspath(os.path.dirname(__file__)) ,_exts))

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

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
# html_logo = '_static/figs/logo1.png'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = 'None'
# html_favicon = '_static/figs/favicon1.ico'

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

# 根据操作系统选择字体
if platform.system() == 'Windows':
    cjk_font = 'SimSun'
elif platform.system() == 'Darwin':  # macOS
    cjk_font = 'Songti SC'
else:  # Linux
    cjk_font = 'Noto Sans CJK SC'


latex_elements = {  
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',  
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '16pt',
    'figure_align': 'htbp',
    'fontpkg': r'''
   \usepackage{fontspec}
    \usepackage{xeCJK}
    \setCJKmainfont{''' + cjk_font + r'''}
    \setmainfont{Times New Roman}
    \setsansfont{Arial}
    \setmonofont{Courier New}
    ''',
    'preamble': r'''
    \usepackage{bookmark}
    \usepackage{fancyvrb}
    \usepackage{ctex}
    \usepackage{bm}
    \usepackage{newunicodechar}
    
    % 定义emoji字符
    \newunicodechar{🚀}{\emoji{🚀}}
    \newunicodechar{✨}{\emoji{✨}}
    \newunicodechar{📝}{\emoji{📝}}
    \newunicodechar{🔥}{\emoji{🔥}}
    \newunicodechar{🤝}{\emoji{🤝}}
    '''
    
    } 

# 使用XeLaTeX引擎
latex_engine = 'xelatex'

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



numfig = True
numfig_secnum_depth = 2

numfig_format = {
    'figure': 'Fig. %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s',
}

numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s',
    'section': '节 %s',
}