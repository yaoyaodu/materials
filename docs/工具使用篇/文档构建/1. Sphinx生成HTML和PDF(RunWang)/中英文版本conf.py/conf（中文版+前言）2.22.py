# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CSK6\_AI\_SoC\_硬件开发指南\_V0.1'
copyright = '2023, ydu'
author = 'ydu'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

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

\usepackage{titletoc}
\titlecontents{subsubsection}[11.5em]{\small}{\color{blue}\contentslabel{4.3em}}{}{\titlerule*[.5pc]{$\cdot$}\contentspage}
\titlecontents{paragraph}[16.3em]{\small}{\color{blue}\contentslabel{5.3em}}{}{\titlerule*[.5pc]{$\cdot$}\contentspage}


\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[LE,LO]{{CSHD-23001-020\_V0.1}}
    \fancyfoot[RO]{{\thepage}}
    \fancyfoot[RE]{{\thepage}}
    \fancyhead[LE,LO]{{CSK6 AI SoC 硬件开发指南}}
    \fancyhead[RE,RO]{{\includegraphics[scale=0.03]{logo_grey.png}}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,LO]{{CSHD-23001-020\_V0.1}} 
    \fancyfoot[RO]{{\thepage}}
    \fancyfoot[RE]{{\thepage}}
    \fancyhead[LE,LO]{{CSK6 AI SoC 硬件开发指南}}
    \fancyhead[RE,RO]{{\includegraphics[scale=0.03]{logo_grey.png}}}
    \renewcommand{\headrulewidth}{0.8pt}
    \renewcommand{\footrulewidth}{0.4pt}
}


 
 
\usepackage{enumitem}
\setenumerate[1]{leftmargin=10pt}
\setitemize[1]{leftmargin=10pt}

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
    \Huge\bfseries\color{blue} CSK6 AI SoC\par
    \Huge\bfseries\color{blue} 硬件开发指南\par
    \vspace{0.4em}
    \Large\bfseries CSHD-23001-020\_V0.1 \hspace{1cm} February 22, 2023\par
    \small\bfseries 聆思科技专有和保密信息\par
    \small\bfseries 本文档受NDA管控
  \end{flushleft}
  
  \vspace{47.0em}
  
  \begin{center}
  \bfseries\color{blue}  版权所有 © 安徽聆思智能科技有限公司
  \end{center}
   
  
  \newpage\restoregeometry{{\Huge\bfseries\color{blue} 声明}\par \vspace{2ex} 版权所有 © 安徽聆思智能科技有限公司2023。保留一切权利。\par 本文档提供的信息属于安徽聆思智能科技有限公司和/或其关联公司（“聆思科技”）所有，非经聆思科技事先书面许可，任何单位和个人不得以任何方式复制、修改或传播本文档的部分或全部。
\par 本文档内容仅供参考。聆思科技不对本文档所含信息的准确性或完整性作任何明示或暗示的陈述或保证，也不对本文档中存在的任何错误承担责任。\par 聆思科技保留不经通知随时对本文档信息做出修改的权利。聆思科技对本文档享有最终解释权。\par LISTENAI、聆思科技、聆思科技徽标均为安徽聆思智能科技有限公司在中国和其他国家及地区的商标或注册商标。其他所有商标和版权均为其各自所有者的资产。}
  \pagecolor{white}
  
  \renewcommand*\contentsname{目录}



  \newpage
  {\Huge\bfseries\color{blue} 前言} \par \vspace{2ex} 
  {\huge\bfseries\color{blue} 概述} \par \vspace{2ex} 
  本文档主要介绍CSK6处理器硬件设计的要点及注意事项，旨在帮助聆思客户缩短产品的设计周期、提高产品的设计稳定性及降低故障率。请客户参考本指南的要求进行硬件设计，如因特殊原因需要更改的，请严格按照文档中的设计要求进行设计，如有疑问请及时和我司工程师联系。\par   \vspace{2ex} 
  {\huge\bfseries\color{blue} 芯片型号} \par \vspace{2ex} 
  本文档对应的芯片型号为：CSK6002、CSK6012、CSK6011A，后文统一称为CSK6。\par   \vspace{2ex} 
  {\huge\bfseries\color{blue} 适用对象} \par \vspace{2ex} 
  
  本文档主要适用于以下工程师： \par

  -  硬件研发工程师 \par

  -  FAE工程师 \par

  -  产品测试工程师 \par



  \newpage
  {\Huge\bfseries\color{blue} 更新记录}\par
  \begin{figure}[htbp]
    \hspace*{-0.1cm}
    \includegraphics[scale=0.9]{recordEN.png}
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


#  \chapter*{附录1}
#  \addcontentsline{toc}{chapter}{附录1}


#  \renewcommand{\sphinxtableofcontents}{
#    \begingroup
#      \parskip = 0mm
#      \tableofcontents{
#        \chapter*{附录1}
#        \addcontentsline{toc}{chapter}{附录1}
#      }
#    \endgroup
#    \rule{\textwidth}{1pt}
#    \vspace{12pt}
#}




#    \sphinxlogo

#\usepackage{enumitem}
#\setnumerate[1]{leftmargin=10pt}
#\setitemize[1]{leftmargin=10pt}
