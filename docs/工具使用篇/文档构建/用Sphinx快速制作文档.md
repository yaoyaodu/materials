# 用Sphinx快速制作文档

来源：[用Sphinx快速制作文档 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/27544821)

更多资料：

* https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
* https://www.overleaf.com/learn/latex/Understanding_packages_and_class_files
* https://www.overleaf.com/learn/latex/Writing_your_own_class
* [Installing Sphinx — Sphinx documentation (sphinx-doc.org)](https://www.sphinx-doc.org/en/master/usage/installation.html#windows-other-method) Installing Sphinx for Linux (Debian/Ubuntu): `apt-get install python3-sphinx`
* Sphinx官网：[Welcome — Sphinx documentation (sphinx-doc.org)](https://www.sphinx-doc.org/en/master/index.html)

## 简介

Sphinx 是一种文档工具，它可以令人轻松的撰写出清晰且优美的文档, 由 Georg Brandl 在BSD 许可证下开发. [新版的Python文档](https://link.zhihu.com/?target=https%3A//docs.python.org/3/)就是由Sphinx生成的， 并且它已成为Python项目首选的文档工具,同时它对 C/C++ 项目也有很好的支持; 并计划对其它开发语言添加特殊支持. 本站当然也是使用 Sphinx 生成的，它采用reStructuredText! Sphinx还在继续开发. 下面列出了其良好特性,这些特性在Python官方文档中均有体现:

- 丰富的输出格式: 支持 HTML (包括 Windows 帮助文档), LaTeX (可以打印PDF版本), manual pages（man 文档）, 纯文本
- 完备的交叉引用: 语义化的标签,并可以自动化链接函数,类,引文,术语及相似的片段信息
- 明晰的分层结构: 可以轻松的定义文档树,并自动化链接同级/父级/下级文章
- 美观的自动索引: 可自动生成美观的模块索引
- 精确的语法高亮: 基于 Pygments 自动生成语法高亮
- 开放的扩展: 支持代码块的自动测试,并包含Python模块的自述文档(API docs)等

Sphinx 使用 reStructuredText 作为标记语言, 可以享有 Docutils 为reStructuredText提供的分析，转换等多种工具。

## 安装Sphinx
Sphinx官网：https://www.sphinx-doc.org/en/master/usage/installation.html#install-pypi。

Sphinx为Python语言的一个第三方库。

找到pip3.exe所在的文件夹：C:\Users\yydu\AppData\Local\Programs\Python\Python310\Scripts。
点击上方文件路径所在方框，输入cmd。
在终端中输入下列命令进行安装：

```text
pip3 install sphinx
```

安装后如果不进行任何设置，则只能在C:\Users\yydu\AppData\Local\Programs\Python\Python310\Scripts路径下生成HTML。
如果在其他目录下生成HTML则会报错：

需要设置环境变量，在桌面右击计算机->属性->高级系统设置（页面右侧）->环境变量，选择“系统变量”的path，然后点击编辑-新建，将以下文件路径复制过去即可：
C:\Users\yydu\AppData\Local\Programs\Python\Python310\Scripts。

设置环境变量后，则可在任何目录下生成HTML。

## 创建Sphinx项目

创建一个用于存放文档的文件夹，然后在该文件夹路径下运行下列命令快速生成Sphinx项目：

```text
sphinx-quickstart
```

接下来会让你选择一些配置：

\1. 设置文档的根路径（回车，使用默认设置）

```text
Enter the root path for documentation.
> Root path for the documentation [.]:
```

\2. 是否分离source和build目录（输入y,选择分离，方便管理）

```text
You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:
```

\3. 设定模板前缀（回车，使用默认选项）

```text
Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:
```

\4. 输入项目名称和作者

```text
The project name will occur in several places in the built documentation.
> Project name: Sphinx-test
> Author name(s): test
```

\5. 输入项目版本号

```text
Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
just set both to the same value.
> Project version []: 1.0.0
> Project release [1.0.0]:
```

\6. 文档语言（回车，默认即可）

```text
If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]:
```

\7. 设定文档文就按的后缀

```text
The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:
```

\8. 设定首页名称（回车，选择默认index即可）

```text
One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:
```

\9. 根据需要选择是否开启epub输出(一般用不到，回车默认不开启即可)

```text
Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]:
```

\10. 根据需求选择是否开启相应的Sphinx拓展功能

```text
Please indicate if you want to use one of the following Sphinx extensions:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]: y
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]: y
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
Note: imgmath and mathjax cannot be enabled at the same time.
imgmath has been deselected.
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: n
```

\11. 创建项目

```text
A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]: y
> Create Windows command file? (y/n) [y]: y

Creating file ./conf.py.
Creating file ./index.rst,.md.
Creating file ./Makefile.
Creating file ./make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file ./index.rst,.md and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

项目创建以后目录结构如下所示:

```text
.
├── Makefile
├── build
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```

- build:用来存放通过make html生成文档网页文件的目录
- source：存放用于生成文档的源文件
- [conf.py](https://link.zhihu.com/?target=http%3A//conf.py/): Sphinx的配置文件
- index.rst: 主文档

## 定义文档结构

主文档index.rst的主要功能是被转换成欢迎页, 它包含一个目录表（ “table of contents tree”或者 toctree ). Sphinx 主要功能是使用 reStructuredText, 把许多文件组织成一份结构合理的文档.

toctree指令初始值如下：

```text
.. toctree::
   :maxdepth: 2
```

你可以在 content 的位置添加文档列表:

```text
.. toctree::
   :maxdepth: 2

   tutorial.md
   ...
```

注：文档文件放在与index.rst同级目录下。

## 支持markdown文件、更改文档主题

Spinx本身不支持.md文件生成文档，需要我们使用第三方库recommonmark进行转换。 首先分别运行下列命令安装recommonmark与sphinx_rtd_theme库。

```text
pip install recommonmark

pip install sphinx_rtd_theme
```

安装好，在conf.py中修改下列两个配置：

```text
source_suffix = ['.rst', '.md', '.MD']
html_theme = 'sphinx_rtd_theme'
```

并新增：

```text
source_parsers = {
    '.md': CommonMarkParser,
    '.MD': CommonMarkParser,
}
```

## 生成文档

在Sphinx项目所在的文件夹路径下运行下列命令生成文档：

```text
make html
```

生成后的文档位于build/html文件夹内，用浏览器打开index.html即可看到生成后的文档。

## 参考文章

1. [Sphinx 使用手册](https://link.zhihu.com/?target=http%3A//zh-sphinx-doc.readthedocs.io/en/latest/index.html)[使用](https://link.zhihu.com/?target=https%3A//www.ibm.com/developerworks/cn/opensource/os-sphinx-documentation)

2. [sphinx 制作简洁而又美观的文档](https://link.zhihu.com/?target=https%3A//www.ibm.com/developerworks/cn/opensource/os-sphinx-documentation)

3. [使用Sphinx制作说明文档](https://link.zhihu.com/?target=https%3A//www.biaodianfu.com/sphinx-documentation.html)