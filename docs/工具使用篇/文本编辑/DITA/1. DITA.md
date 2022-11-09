# DITA

[The DITA Style Guide Best Practices for Authors (oxygenxml.com)](https://www.oxygenxml.com/dita/styleguide/webhelp-feedback/#Artefact/Authoring_Concepts/c_About_the_Style_Guide.html)

[Resources (learningdita.com)](https://learningdita.com/resources/)

# [Structured Writing](https://ireneontheway.github.io/TC_Paper/Structured_writing/index.html#structured-writing)

DITA信息开发流程

![DITA](https://i.loli.net/2021/08/03/Qb7q3rtFWcY86Ep.png)

结构化写作特点：

- 模块化
- 内容与样式分离
- 元数据
- 多格式发布
- 内容重用

DITA的特点：

- 应用领域广
- 融合信息开发理念
- 信息架构可进化
- 重用灵活
- 兼容性强

## [基本术语]

### [建筑图纸 -> DITA标准]

### [房子 -> map]

DITA map，用于组织topic的DITA文件

### [房间 -> topic]

DITA topic,DITA topic是构建内容的基本模块，不同类型的内容用不同的载体（topic类型）

### [窗户、门 -> 内容组件element]

DITA元素类型的XML元素，其@class属性值必须是符合DITA规范或符合专门化层级的元素名

### [对组件的描述 -> 属性attribute]

描述元素属性的元数据，用@表示

### [其他](https://ireneontheway.github.io/TC_Paper/Structured_writing/StructuredWriting_DITA_Intro.html#其他)

#### [DITA文件]

符合DITA规范的XML文件，根元素必须为 , , 或 之一，后缀名是.xml或.dita

#### [元数据（metadata）]

提供有关信息的信息，可以是属性或元素

#### [DITA专门化（specialization）]

对现有的DITA架构（topic，元素和属性）进行扩展，使之更加适合内容需求，DITA专门化是DITA定制的一种形式.



[技术写作理论知识- DITA - 简书 (jianshu.com)](https://www.jianshu.com/p/66acac5aa747)

## DITA的基本概念

- Topic：内容的载体，DITA一般将Topic分为Concept、Reference和Task三类，也**可以使用DTD扩充Topic的类型。**

- ditamap：可以简单理解为链接文档具体Topic的XML目录。

- DTD：文档类型定义，用于定义Topic的模板，实际使用时不同团队可以根据自身需求定义自己的DTD。

  ![img](https://upload-images.jianshu.io/upload_images/47580-ec8c6f98c0c6acbf.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)

* ditaval：条件文本，用于发布时过滤文档内容。

  ![img](https://upload-images.jianshu.io/upload_images/47580-f38bfbe5f28401ab.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)



[OASIS Darwin Information Typing Architecture (DITA) TC | OASIS (oasis-open.org)](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=dita)

## DITA Open Toolkit

[(3条消息) xml源文件的文档生成工具--DITA Open Toolkit（DITA-OT）的使用入门_兰陵小晨的博客-CSDN博客](https://blog.csdn.net/qq_38250687/article/details/78652256)

XML源文件的文档生成工具。

Oxygen XML Editor不带有文档生成工具，请安装tool chain工具来执行生成场景。文档生成场景由DITA Open Toolkit提供。

## OXygen XML Editor 

官网：[Oxygen XML Editor](https://www.oxygenxml.com/)

[Oxygen XML Editor(XML编辑器) v21.0专业破解版下载 - zd423 (zdfans.com)](https://www.zdfans.com/html/27117.html)

[Oxygen XML Editor 23.1 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/366481392)

Oxygen XML Editor 是一款基于Java的XML编辑器，支持XML, XSL, TXT, XSD, DTD文档，能自行校验XML, XSL, XSD代码，提示脚本错误。

Oxygen能自动完成结束标签，代码高亮显示，支持Unicode。
Oxygen XML Editor是一款简洁并且功能一流的集XML察看和编辑等功能为一体的软件。由于它提供了对XML编辑特性的完整覆盖，因此，无论在企业界还是学术界，该软件的应用都很普及。它能工作在XML Schemas/ DTDs/Relax NG schemas和NRL Schemas.强大的转换支持让你不仅能编辑XSLT和XSL-FO文档,也能把它们转换成为你想要的如HTML/PS/PDF等文件。

## DITA （体系结构）

 DITA 是“Darwin Information Typing Architecture”**（达尔文信息类型化体系结构）**的缩写，它是**IBM** 公司为OASIS 所支持的团体贡献的发明。OASIS 的全称为“Organization for the Advancement of Structured Information Standards”（结构信息标准化促进组织）。公司名称IBM

目录1 主题化2 定制化3 重用和过滤4 协作和共享
DITA 是基于XML的体系结构，用于编写、制作、交付面向主题的信息类型的内容。DITA的单源内容可以通过不同的方法进行重用，生成不同的交付内容。由于DITA过去用于大型技术手册的编写、管理和交付，它能够满足所有可能呈现给读者的信息发布类型的要求。DITA可用于技术手册、交互培训，教材、标准、报告、商业文档、贸易书籍、旅游和自然指南等书籍的编写。[1]   主题化DITA 定义主题DTD，**它支持主题化的信息创建方法**。**主题是信息的组成部分**，而不是完整的文档。主题根据信息类型的不同，可以分为**concept（概念）、task（任务）、reference（参考）**，和troubleshooting（故障处理）等基本类型，这些主题通过**Map文件组织起来形成文档**。Map可被认为是文档目录结构，根据文档不同类型，有不同的章节划分方式。具体可以参见Darwin Information Typing Architecture (DITA) v1.3[1] 中对topic、Map、以及topic中的元素和属性的详细描述。  定制化不同的主题都由DTD来定义的。只需掌握简单的DTD语法规则，就可以快速简单地定义适合本组织文档需求的主题。DITA 规范提供了一个**开源工具DITA Open Toolkit**，该工具可方便地发布DITA格式内容，生成各种格式的输出。同时，可以很容易的定制该工具的发布过程，根据需要对输出样式进行定制化。  重用和过滤DITA提供了各种机制，包括conref和keyref等内容引用，对内容进行重用。同时通过DITAVAL文件，对不同的读者对象、平台、产品、版本等进行内容过滤。  协作和共享**将内容主题化，将格式统一到样式表，**通过Map组织内容章节目录。这些方法使得文档的开发任务可以很方便地分解到各个文档编写人员手中，生成格式统一，内容规范的文档。**由于DITA文件是基于XML的文本文件，又可以很方便地进行存储和传输，实现文档的异地共享，协同作业**。

