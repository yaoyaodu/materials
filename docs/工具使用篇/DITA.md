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

