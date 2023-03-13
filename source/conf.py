import sphinx_rtd_theme
import os
import sys


# -- Project information -----------------------------------------------------

project = "Python's Blog"
copyright = '2019, PanZheng'
author = 'PanZheng'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# sphinx_copybutton 在每个代码块中自动出现一个复制按钮
extensions = ['chinese_search', 'recommonmark', 'sphinx.ext.autodoc','sphinx_copybutton']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

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
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../build/html/_static']
htmlhelp_basename = 'Python\'S BLOG'


# -- Options for LaTeX output ---------------------------------------------

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

latex_elements = {  # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',  # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '16pt',
    'classoptions': ',oneside', 'babel': '',  # 必须
    'inputenc': '',  # 必须
    'utf8extra': ''}  # 必须
# Additional stuff for the LaTeX preamble.
# 'preamble': """\usepackage{xeCJK} \setlength{\parindent}{2em}\setCJKmainfont{WenQuanYi Micro Hei} \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}  \setCJKfamilyfont{song}{WenQuanYi Micro Hei} \setCJKfamilyfont{sf}{WenQuanYi Micro Hei} \XeTeXlinebreaklocale "zh"\XeTeXlinebreakskip = 0pt plus 1pt"""


# 'preamble': r"""\usepackage{xeCJK}\usepackage{indentfirst}\setlength{\parindent}{2em}\setCJKmainfont{WenQuanYi Micro Hei}\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}\setCJKfamilyfont{song}{WenQuanYi Micro Hei}\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}\XeTeXlinebreaklocale "zh"\XeTeXlinebreakskip = 0pt plus 1pt


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'mkdocs.tex', u'《Python博客》',
     u'郑攀', 'howto'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'python3-blog', '《Python博客》',
     ['郑攀'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Python-blog', '《Python博客》',
     '郑攀', 'Python-blog', '《Python博客》',
     'Miscellaneous'),
]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# otherwise, readthedocs.org uses their theme by default, so no need to specify it
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
highlight_langeuage = "java,javascript,python,html"
_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
