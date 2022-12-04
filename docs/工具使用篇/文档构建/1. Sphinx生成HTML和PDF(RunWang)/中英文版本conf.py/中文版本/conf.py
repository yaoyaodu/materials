# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'MetaX文档中心'
copyright = '2021, MetaX'
author = 'MetaX'

release = 'V0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'
# html_theme = 'basic'
# html_theme = 'alabaster'
# html_theme = 'sphinxdoc'
# html_theme = 'scrolls'
# html_theme = 'agogo'
# html_theme = 'nature'
# html_theme = 'pyramid'
# html_theme = 'haiku'
# html_theme = 'traditional'
# html_theme = 'epub'

#html_theme = 'sphinx_rtd_theme'
# html_theme = 'bizstyle'

# html_theme_options = {
#    "rightsidebar": "true",
#    "relbarbgcolor": "green"
#}


# html_title = u'沐曦文档中心'
# html_short_title = u'沐曦文档中心'
# html_codeblock_linenos_style

html_favicon = 'favicon.ico'

html_search_language = 'zh_CN'

# html_logo = 'METAX.PNG'
html_logo = 'METAXcolor.PNG'

language = 'zh_CN'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



# -- Options for LateX outout -------------------------------------------------

#字体 Source Han Sans CN Normal
#latex_engine = 'lualatex'
latex_engine = 'xelatex'
latex_logo = 'METAXcolor.PNG'
#latex_logo = 'METAX.PNG'

#设置图片标题（图注）的格式
numfig=True
numfig_secnum_depth=1
numfig_format={'figure': 'Figure %S'}


latex_elements = {
    'fontpkg': r'''
\setmainfont{Source Han Sans CN}
\setsansfont{Source Han Sans CN}
\setmonofont{Source Han Sans CN}    
\setCJKmainfont{Source Han Sans CN}
\setCJKsansfont{Source Han Sans CN}
\setCJKmonofont{Source Han Sans CN}    
''',
    
    'preamble': r'''
\usepackage{titlesec}
\titleformat{\chapter}{\raggedright\Huge\bfseries\color{purple}}{\thechapter}{1em}{}

\usepackage{color}
\definecolor{purple}{RGB}{102,8,116}
\definecolor{grey}{RGB}{218,218,218}
\definecolor{dark}{RGB}{137,137,137}
\definecolor{grey1}{RGB}{182,182,182}
\definecolor{grey2}{RGB}{200,200,200}


将默认的“Figure 1：”中的冒号去掉，即修改图注分隔符，可以用caption2宏包：
#usepackage[]{caption2}
#renewcommand{captionlabeldelim}{.}

#看下下面这个配置是否不起作用
\usepackage[]{caption2}
\renewcommand{\captionlabeldelim}{}

\makeatletter
 \fancypagestyle{plain}{
 \pagestyle{fancy}
 \fancyhf{}
 \lhead{\bfseries MACAMACA PyTorch User Guide}
 \rhead{\includegraphics[scale=0.3]{metaxcolor.png}}
 \lfoot{CSOG-22004-021\_V1.0}
 \cfoot{MetaX Proprietary and Confidential}
 \rfoot{\thepage}
 \renewcommand{\headrulewidth}{0.8pt}
 \renewcommand{\headrulewidth}{0.8pt}
 \renewcommand{\headrule}{\hbox to \headwidth{\color{purple}\leaders\hrule height \headrulewidth\hfill}}
 \renewcommand{\footrule}{\hbox to \headwidth{\color{purple}\leaders\hrule height \footrulewidth\hfill}}
 \setlength{\headheight}{7mm}
 }
\makeatother
 
\usepackage{enumitem}
\setnumerate[1]{leftmargin=10pt}
\setitemize[1]{leftmargin=10pt}

\usepackage{draftwatermark}
\SetWatermarkText{MetaX Confidential}
\SetWatermarkColor{grey}
\SetWatermarkScale{0.4}

\usepackage{graphicx}

\renewcommand{\sphinxmaketitle}{
  \newgeometry{top=1.5cm,bottom=0cm}
  \pagecolor{purple}
  \begin{flushleft}
    \sphinxlogo
    \vspace{1.8cm}
    \Huge\bfseries\color{white} MACAMACA C++编程指南\par
    \vspace{0.4em}
    \Large\bfseries CSPG-22001-000\_V1.0 \hspace{1cm} 2022-07-26\par
    \small\bfseries 沐曦专有和保密信息 \hspace{2.1cm} 本文档受NDA管控
  \end{flushleft}
  \vspace{0.1em}
  \begin{figure}[htbp]
    \hspace*{-2.5cm}
    \includegraphics[scale=3.5]{XlogoEN.png}
  \end{figure}  
  
  \newpage\restoregeometry{{\Huge\bfseries 声明}\par \vspace{2ex} 版权所有  沐曦集成电路（上海）有限公司　2022。保留一切权利。＼par本文档提供的信息...}
  \pagecolor{white}

  \newpage
  {\Huge\bfseries\color{purple} 更新记录}\par
  \begin{figure}[htbp]
    \hspace*{-0.1cm}
    \includegraphics[scale=1.05]{record.png}
  \end{figure} 
}   
''',


    'papersize': 'a4paper',
    'pointsize': '10pt',
    'releasename': '版本',
    'extraclassoptions': 'openany',
    'figure_align': 'H',
    'sphinxsetup': 'VerbatimColor={RGB}{218,218,218}, TitleColor={RGB}{102,8,116}, verbatimwithframe=false, verbatimhintsturnover=false, InnerLinkColor={RGB}{102,8,116}, OuterLinkColor={RGB}{102,8,116}',
    'passoptionstopackages': r'\PassOptionsToPackage{numfigreset=1}{sphinx}'
}

latex_additional_files=["XlogoCN.png", "metaxcolor.png", "record.png"]





