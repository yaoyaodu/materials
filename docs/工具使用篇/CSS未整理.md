CSS未整理

来源：[CSS（层叠样式表） | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS)

**CSS浮动** 

float：让元素浮动，取值：left(左浮动)、right(右浮动)浮动的元素，将向左或向右浮动，浮动到包围元素的边上，或上一个浮动元素的边上为止。浮动的元素，不再占空间了，并且，浮动元素的层级要高于普通元素。浮动的元素，一定是“块元素”。不管它原来是什么元素。如果浮动的元素，没有指定宽度的话，浮动后它将尽可能的变窄。因此，浮动元素一般要定宽和高。一行的多个元素，要浮动一起浮动。浮动的功能：可以实现将多个块元素并列排版。



**CSS清除浮动的功能有两个：**

(1)可以包围元素从“视觉上”包住浮动元素(2)清除之下的其它元素将恢复默认排版。**注：****有浮动，就得有清除。如果包围元素指定了高度了，那么可以不使用清除功能。**



**CSS定位**

position：元素定位方式，取值static、fixed、relative、absolutestatic：静态定位(默认状态、不定位)。Fixed：固定定位。Relative：相对定位。Absolute：绝对定位。

**定位方式，要与定位属性配合使用**定位坐标：指定定位的元素，偏移目标元素多远的距离。left：定位元素，距离目标元素左边的距离。top：定位元素，距离目标元素上边的距离。right：定位元素，距离目标元素右边的距离。bottom：定位元素，距离目标元素下边的距离。**固定定位，position:fixed**固定定位，是相对于浏览器窗口来进行的定位。固定定位，不占空间，层级要高于普通元素。它不会随着网页的滚动而滚动。如果不指定定位坐标的话，固定定位元素的位置在原地不动。固定定位元素，一定是“块元素”，不管原来它是什么元素。**相对定位，position:relative;**相对定位，是相对于“原来的自己”进行定位。相对定位，依然占空间，层级高于普通元素。如果不指定定位坐标的话，相对定位元素的位置在原地不动。相对定位，原来是行内元素，定位后还是行内元素；原来是块元素，定位后还是块元素。 **注：相对定位和绝对定位，一般情况下是配合使用。****绝对定位，position:absolute**相对于祖先定位元素(相对定位，绝对定位)，来进行的定位。如果它的父元素没有进行任何定位的话，再往上找定位元素。如果一直找到<body>都没有找到定位元素的话，那就相对于<body>来进行定位。绝对定位元素，不占空间，层级要高于普通元素。如果不指定定位坐标的话，绝对定位元素的位置在原地不动。绝对定位元素，是一个“块元素”。

**CSS属性继承**：外层元素的样式，会被内层元素进行继承。多个外层元素的样式，最终都会“叠加”到内层元素上。**什么样的CSS属性能被继承呢？**CSS文本属性都会被继承的：color、 font-size、font-family、font-style、 font-weighttext-align、text-decoration、text-indent、letter-spacing、line-height提示：<body>中的CSS属性，会被所有的子元素继承。**CSS优先级****单个选择器的优先级**行内样式 > id选择器 >  class选择器 > 标签选择器**多个选择器的优先级**多个选择器的优先级，一般情况下，指向越准确，优先级越高。特殊情况下，我们需要假设一些值：标签选择器    优先级为1类选择器     优先级为10Id选择器     优先级为100行内样式     优先级为1000计算以下优先级.news h1{color:red;}   优先级：10 + 1 = 11.title{color:blue;}    优先级：10div.news h1{color:red;}  优先级：1 + 10 + 1 = 12h1.title{color:blue;}   优先级：1 + 10 = 11

**CSS基础教程之背景属性****CSS背景属性****background-color：背景颜色。****background-image：背景图片地址。如：background-image:url(images/bg.gif)****background-repeat：背景平铺方式，取值：no-repeat(不平铺)、repeat-x(水平方向)、repeat-y(垂直方向)****background-position：背景定位。格式：background-position:水平方向定位 垂直方向定位；**用英文单词定位：background-position: left|center|right  top|center|bottom;用固定值定位：background-position: 50px  50px; //背景距离容器的左边50px，容器顶端50px用百分比定位：background-position: 50%  50%;  //水平居中，垂直居中用混合定位：background-position: left  10px;  //背景靠左边齐，距离容器顶端10px**简写方式**background：背景色  背景图  平铺方式  定位方式；举例：background:url(images/bg.gif) no-repeat center center;举例：background: #ccc url(images/bg.gif) no-repeat left 10px;**display属性**功能：规定网页元素如何显示的问题。取值：none(隐藏)、block(以块元素显示)、inline(以行内元素显示)block：可以实现将行内元素转成块元素。inline：可以实现将块元素转成行内元素。

**overflow属性**：当内容溢出时，该如何显示**overflow**：当内容溢出时，溢出的内容该如何显示。取值：visible(可见)、hidden(隐藏)、scroll(出现滚动条)、auto(自动)p{border:1px solid #f0f0f0;width:300px;height:100px;overflow:scroll;cursor:pointer}**CSS基础教程之尺寸、字体及文本属性****CSS尺寸属性**width：元素宽度，一定要加px单位。height：元素高度。**CSS字体属性**font-size：文字大小。如：font-size:14px;font-family：字体。如：font-family:微软雅黑;font-style：斜体，取值：italic。如：font-style:italic;font-weight：粗体，取值：bold。如：font-weight:bold;**CSS文本属性**color：文本颜色text-decoration：文本修饰线，取值：none(无)、underline(下划线)、overline(上划线)、line-through(删除线)text-align：文本水平对齐方式，取值：left、center、rightline-height：行高，可以用固定值，也可以用百分比。如：line-height:24px;  line-height:150%;text-indent：首行缩进。如：text-indent:28px;letter-spacing：字间距。

**CSS基础教程之列表及边框属性****CSS列表属性**项目符号或编号前面的各种符号无法改变样式，所以在实际中我们一般不用。list-style：列表样式，取值：none。去掉项目符号或编号前面的各种符号。<style type="text/css">ul,li{list-style:none;}/*去掉前面的符号*/</style>**CSS边框属性：每个元素都可以加边框线**border-left：左边框线。border-right：右边框线。border-top：上边框线。border-bottom：下边框线。border：同时给四个边加边框线。
 格式：border-left：粗细  线型  线的颜色; 线型：none(无线)、solid(实线)、dashed(虚线)、dotted(点状线) 举例：border-left：5px  dashed  red;

<style type="text/css">.box{background-color:#66ff66;width:200px;height:200px;border-left:6px solid red;border-right:3px dashed blue;border-top:5px dotted black;}</style>**CSS内边距属性：边框线到内容间的距离****注：平常我们所说的width和height属性，它们指内容的宽度和高度，不含内、外边距、边框线。**padding-left：左内填充距离，左边线到内容间的距离。padding-right：右内填充距离，右边线到内容间的距离。padding-top：上内填充距离，上边线到内容间的距离。padding-bottom：下内填充距离，下边线到内容间的距离。缩写形式padding:10px;  //四个边的内填充分别为10pxpadding:10px 20px;  //上下为10px，左右为20pxpadding:5px 10px 20px;  //上为5px，左右为10px，下为20pxpadding:5px 10px 15px 20px;  //顺序一定是“上右下左”**CSS外边距属性：边线往外的距离**margin-left：左边线往外的距离。margin-right：右边线往外的距离margin-top：上边线往外的距离。margin-bottom：下边线往外的距离。缩写形式margin:10px;  //四个外边距分别为10pxmargin:10px 20px  //上下外边距10px，左右外边距20pxmargin:5px 10px 15px;  //上外边距5px，左右外边距10px，下外边距15pxmargin:5px 10px 15px 20px;  //顺序一定是“上右下左”

[CSS（层叠样式表）_百度百科 (baidu.com)](https://baike.baidu.com/item/CSS/5457)层叠样式表(Cascading Style Sheets)是一种用来表现[HTML](https://baike.baidu.com/item/HTML)（[标准通用标记语言](https://baike.baidu.com/item/标准通用标记语言/6805073)的一个应用）或[XML](https://baike.baidu.com/item/XML)（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种**脚本语言**动态地对网页各元素进行格式化。 CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。