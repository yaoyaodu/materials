# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LS2100\_BLE\_SoC\_Datasheet\_V0.1'
copyright = '2023, ydu'
author = 'ydu'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

master_doc = 'index'

latex_engine = 'xelatex'
#latex_engine = 'lualatex'
latex_logo = 'logo_grey.png'
# latex_logo = 'logo_white.png'

numfig = True
#numfig_secnum_depth=1
#numfig_format={'figure': 'Figure %S'}


latex_elements = {
    'preamble': r'''
    
\usepackage{xeCJK}
\setCJKmainfont{Source Han Sans CN}
\setCJKsansfont{Source Han Sans CN}
\setCJKmonofont{Source Han Sans CN}    
    

\usepackage{titlesec}
\titleformat{\chapter}{\raggedright\Huge\bfseries\color{blue}}{\thechapter}{1em}{}

\usepackage{color}
\definecolor{blue}{RGB}{5,104,255}
\definecolor{grey}{RGB}{218,218,218}
\definecolor{dark}{RGB}{137,137,137}
\definecolor{grey1}{RGB}{182,182,182}
\definecolor{grey2}{RGB}{200,200,200}


\usepackage[]{caption2}
\renewcommand{\captionlabeldelim}{}




\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[LE,LO]{{CSDS-23001-031\_V0.1}}
    \fancyfoot[RO]{{\thepage}}
    \fancyfoot[RE]{{\thepage}}
    \fancyhead[LE,LO]{{LS2100 BLE SoC Datasheet}}
    \fancyhead[RE,RO]{{\includegraphics[scale=0.03]{logo_grey.png}}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,LO]{{CSDS-23001-031\_V0.1}} 
    \fancyfoot[RO]{{\thepage}}
    \fancyfoot[RE]{{\thepage}}
    \fancyhead[LE,LO]{{LS2100 BLE SoC Datasheet}}
    \fancyhead[RE,RO]{{\includegraphics[scale=0.03]{logo_grey.png}}}
    \renewcommand{\headrulewidth}{0.8pt}
    \renewcommand{\footrulewidth}{0.4pt}
}


 
\usepackage{enumitem}
\setenumerate[1]{leftmargin=10pt}
\setitemize[1]{leftmargin=10pt}
\setenumerate[2]{leftmargin=12pt}
\setitemize[2]{leftmargin=12pt}



\usepackage{titletoc}
\titlecontents{subsubsection}[11.5em]{\small}{\color{blue}\contentslabel{4.3em}}{}{\titlerule*[.5pc]{$\cdot$}\contentspage}
\titlecontents{subsubsubsection}[15.5em]{\small}{\color{blue}\contentslabel{2.3em}}{}{\titlerule*[.5pc]{$\cdot$}\contentspage}




\usepackage{amsmath}

\usepackage{amssymb}



\usepackage{draftwatermark}
\SetWatermarkText{LISTENAI Confidential}
\SetWatermarkColor{grey}
\SetWatermarkScale{0.4}

\usepackage{graphicx}

\renewcommand{\sphinxmaketitle}{
  \newgeometry{top=1.5cm,bottom=0cm}

  \begin{flushleft}
    \begin{figure}[htbp]
      \hspace*{-0.1cm}
      \includegraphics[scale=0.1]{logo_grey.png}
    \end{figure} 
    \vspace{1.8cm}
    \Huge\bfseries\color{blue} LS2100 BLE SoC Datasheet\par
    \vspace{0.4em}
    \Large\bfseries CSDS-23001-031\_V0.1 \hspace{1cm} February 13, 2023\par
    \small\bfseries LISTENAI Proprietary and Confidential\par
    \small\bfseries Prepared and Provided Under NDA
  \end{flushleft}
   
  
  \newpage\restoregeometry{{\Huge\bfseries\color{blue} DISCLAIMER}\par \vspace{2ex} Copyright © 2023 Anhui LISTENAI Co., Ltd. All rights reserved.\par 
The information presented in this document belongs to Anhui LISTENAI Co., Ltd. and/or its affiliates (LISTENAI). Without prior written permission of LISTENAI, no entity or individual shall copy, modify, or distribute part or all of the document in any way.\par
The information provided in this document is for reference only. LISTENAI does not give any representations or warranties, expressed or implied, as to the accuracy or completeness of such information. LISTENAI shall have no liability for any errors contained in this document.\par
LISTENAI reserves the right to make corrections, modifications, enhancements, improvements, and other changes to the content at any time without notice. LISTENAI reserves all the right for the final explanation.\par
LISTENAI, \includegraphics[scale=0.46]{lingsikeji.png}, and other LISTENAI icons are trademarks of Anhui LISTENAI Co., Ltd. All other trademarks and trade names mentioned in this document are the property of their respective holders.}
  \pagecolor{white}
  
\renewcommand*\contentsname{Table of Contents}




  \newpage
  {\Huge\bfseries\color{blue} Update History}\par
  \begin{figure}[htbp]
    \hspace*{-0.1cm}
    \includegraphics[scale=1.16]{recordEN.png}
  \end{figure} 
}   
''',


    'papersize': 'a4paper',
    'pointsize': '10pt',
    'releasename': 'Release',
    'extraclassoptions': 'openany',
    'figure_align': 'H',
    'sphinxsetup': 'VerbatimColor={RGB}{218,218,218}, TitleColor={RGB}{5,104,255}, verbatimwithframe=false, verbatimhintsturnover=false, InnerLinkColor={RGB}{5,104,255}, OuterLinkColor={RGB}{5,104,255}',
    'passoptionstopackages': r'\PassOptionsToPackage{numfigreset=1}{sphinx}'

}

latex_additional_files=["logo_grey.png", "logo_white.png", "lingsikeji.png", "recordEN.png"]

# numfig_format = {'figure':'Figure %s'}

#    

#    \sphinxlogo

#\usepackage{enumitem}
#\setnumerate[1]{leftmargin=10pt}
#\setitemize[1]{leftmargin=10pt}
