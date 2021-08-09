# CSS (Cascading Style Sheets) 叠层样式表

推荐教程：[CSS 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-tutorial.html)

颜色代码：[十六进制颜色代码表，图表及调色板 - Encycolorpedia](https://encycolorpedia.cn/)

CSS层叠样式表是一种用来表现[HTML](https://baike.baidu.com/item/HTML)（[标准通用标记语言](https://baike.baidu.com/item/标准通用标记语言/6805073)的一个应用）或[XML](https://baike.baidu.com/item/XML)（标准通用标记语言的一个子集）等文件样式的计算机语言。CSS不仅可以静态地修饰网页，还可以配合各种**脚本语言**动态地对网页各元素进行格式化。 CSS 能够对网页中元素位置的排版进行像素级精确控制，支持几乎所有的字体字号样式，拥有对网页对象和模型样式编辑的能力。

## 前端最核心的三个技术

- HTML: 用于控制网页的结构
- CSS：用于控制网页的外观（给HTML标记添加的样式）
- Javascript: 用于控制网页的行为



## 引入CSS的方法

* 嵌入式
  * 通过`<style>`标记，来引入CSS样式。
  * 语法格式：`<style type = “text/css"></style>`
  * `<style>`中的CSS样式，只能给当前网页来使用。同一个网页中，`<style>`标记可以多次出现。

- 外联式
  - 通过`<link>`标记，来入引一个外部的CSS文件(.css)，这样可以实现公共的CSS代码被多个网页共享。
  - `<link>`标记放在`<head>`标记中。同一个网页，可以使用多个`<link>`来链入多个外部样式。
  - `<link rel = “stylesheet" type = “text/css" href = “css/public.css" />`
  - `<link>`标记的常用属性
    - rel：引入的是什么类型的文件。取值：stylesheet
    - type：内容类型
    - **href：引入的CSS文件地址**
- 行内式(主要用于JS控制元素的样式)
  - **每一个HTML标记，都有一些公共的属性：class、id、title、style。**
  - **HTML标记中的style属性的值，与CSS中样式一模一样。**
  - **行内样式中，CSS代码不能写的过多；行内样式中，多个CSS属性不能换行，也就是一行写完。**
  - **行内样式优先级是最高的，比ID选择器还要高。**



## CSS语法

![img](https://i.loli.net/2021/08/02/b5Uu9zgCM7o8isx.png)



* **选择器**：
  * 选择**HTML标记**，给哪个HTML标记加样式
  * 给多个标记添加同一个样式，标记之间用逗号,隔开：h1,p,div,body{color:red;} 
* **格式声明语句：{}**
  * 每一条格式语句构成：**属性名:属性值**
  * 每一条格式语句，必须用英文下的;结束
  * CSS中的数字单位都是px，不能省略

CSS注释: `/*CSS注释内容*/`

HTML注释：`<!--HTML注释-->`



### CSS选择器

* 基本选择器
  * *选择器：通配符

    * 描述：将匹配所有的HTML标签，所有的标签都会改变的。
    * 语法：*{ color:red; }
    * 注：“*”尽量少用，因为IE6不支持。

  * 标签选择器：

    * 描述：将匹配指定的HTML标签。
    * 语法：h1{ color:red; }
    * 注：CSS标签选择器，与HTML标签的名称一样，但不能加尖括号。

  * **class选择器: .**

    * 描述：**给一类HTML标签加样式**。这里所指的“一类”是：每个HTML标签都有一个class属性，且class的值一样。class属性是公共属性，每个HTML标签都有。

    * 语法：.box{ color:red; }

      类选择器的名称，**必须以“.”开头**，后跟HTML标签的class属性的值。

    * 注： **HTML标签的class属性的值，不能以数字开头。**

  * id选择器:#

    * **描述：**给指定id的元素添加样式。
    * 注：网页中HTML标签的id属性的值，必须是唯一的。每一个HTML标签都有一个id的公共属性。
    * **id属性一般是给JS使用的，不是让你来加样式的。class属性只能给CSS用，不能给JS用的。**
    * id选择器的名称，必须以“#”开头，**后跟HTML标记的id属性的值。**
    * ID与class的优先级不同优先级来看： Style ＞ ID ＞ Class ＞ 缺省的Html元素
  
* 组合选择器

  * 多元素选择器
    * **描述：给多个元素加同一个样式，**多个选择器之间用逗号“,”隔开。
    * 举例：
      * h1,p,div,body{color:red;} 
      * h1,p,.NO1{color:red;} 
  * 后代元素选择器(最常用)
    * 描述：给某个标签的某一个后代元素**加样式。**选择器之间用“空格”隔开。
    * **举例：div .title{ color:red;}**
  * 子元素选择器 (>)
    * 描述：给某个元素的子元素添加样式。
    * 举例：div > h1.title{color:red;}
    * 子元素：子元素就是儿子。后代元素：后代元素是指孙子、曾孙子、曾曾孙子等等。
  
* CSS伪类选择器：给超链接加的样式(链接的不同状态加样式)

  * 一个超链接，有四个状态：
    * 正常状态(:link)：鼠标没放上之前链接的样式。
    * 放上状态(:hover)：鼠标放到链接上时的样式。
    * 激活状态(:active)：按住鼠标左键不松开的样式，这个状态特殊短暂。访
    * 问过的状态(:visited)：按下鼠标左键，并弹起，这时的样式效果。
  * 给链接加不同的样式：
    * a:link, a:visited{ color:#444; text-decoration:none; } //将“正常状态”和“访问过的状态”合二为一。
    * a:hover{ color:#990000; text-decoration:underline; } //“鼠标放上”单做一种效果

### CSS属性

详细信息参见[CSS属性](CSS属性.md)。

#### CSS边框、内边距、外边距属性

![padding margin](https://i.loli.net/2021/08/05/42gcGrmNKIbS9Qv.png)

##### CSS边框属性：每个元素都可以加边框线

border-left：左边框线。

border-right：右边框线。

border-top：上边框线。

border-bottom：下边框线。

border：同时给四个边加边框线。

**格式：border-left：粗细  线型  线的颜色;** 

举例：border-left：5px  dashed  red;

线型：

* none(无线)
* solid(实线)
* dashed(虚线)
* dotted(点状线) 



##### **CSS内边距属性：边框线到内容间的距离**

注：平常我们所说的**width和height**属性，它们指**内容的宽度和高度**，不含内、外边距、边框线。

padding-left：左内填充距离，左边线到内容间的距离。

padding-right：右内填充距离，右边线到内容间的距离。

padding-top：上内填充距离，上边线到内容间的距离。

padding-bottom：下内填充距离，下边线到内容间的距离。

缩写形式：

padding:10px;                 				  //四个边的内填充分别为10px

padding:10px 20px;         				//上下为10px，左右为20px

padding:5px 10px 20px;  				//上为5px，左右为10px，下为20px

padding:5px 10px 15px 20px; 		 //顺序一定是“上右下左”



##### **CSS外边距属性：边线往外的距离**

margin-left：左边线往外的距离。

margin-right：右边线往外的距离

margin-top：上边线往外的距离。

margin-bottom：下边线往外的距离。

缩写形式：

margin:10px;  								  //四个外边距分别为10px

margin:10px 20px;  						//上下外边距10px，左右外边距20px

margin:5px 10px 15px;  				//上外边距5px，左右外边距10px，下外边距15px

margin:5px 10px 15px 20px;     	//顺序一定是“上右下左”



#### **CSS尺寸、字体及文本属性**

CSS尺寸属性

width：元素宽度，一定要加px单位。

height：元素高度。



CSS字体属性

font-size：文字大小。如：font-size:14px;

font-family：字体。如：font-family:微软雅黑;

font-style：斜体，取值：italic。如：font-style:italic;

font-weight：粗体，取值：bold。如：font-weight:bold;



CSS文本属性

color：文本颜色

text-decoration：文本修饰线，取值：

* none(无)、
* underline(下划线)、
* overline(上划线)、line-through(删除线)

text-align：文本水平对齐方式，取值：left、center、right

line-height：行高，可以用固定值，也可以用百分比。如：line-height:24px;  line-height:150%;

text-indent：首行缩进。如：text-indent:28px;

letter-spacing：字间距。



#### CSS背景属性

background-color：背景颜色。

background-image：背景图片地址。如：background-image:url(images/bg.gif)

**background-repeat：背景平铺方式**，取值：

* no-repeat(不平铺)
* repeat-x(水平方向)
* repeat-y(垂直方向)

background-position：背景定位。格式：background-position:水平方向定位 垂直方向定位。

- 用英文单词定位：background-position: left|center|right  top|center|bottom;
- 用固定值定位：background-position: 50px  50px; 				//背景距离容器的左边50px，容器顶端50px
- 用百分比定位：background-position: 50%  50%; 			 	/水平居中，垂直居中
- 用混合定位：background-position: left  10px;  					//背景靠左边齐，距离容器顶端10px

简写方式

**background：背景色  背景图  平铺方式  定位方式；**

**举例：background:url(images/bg.gif) no-repeat center center;**

**举例：background: #ccc url(images/bg.gif) no-repeat left 10px;**



##### display属性

规定网页元素如何显示的问题。取值：

* none(隐藏)
* block(以块元素显示)：可以实现将行内元素转成块元素。
* inline(以行内元素显示)：可以实现将块元素转成行内元素。



##### overflow属性

当内容溢出时，溢出的内容该如何显示。取值：

* visible(可见)
* hidden(隐藏)
* scroll(出现滚动条)
* auto(自动)

举例：p{border:1px solid #f0f0f0;width:300px;height:100px;overflow:scroll;cursor:pointer}





更详细信息参见：

* [CSS 选择器 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cssref/css-selectors.html)
* [CSS 实例 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-examples.html) （实用，重点看）
* [CSS 参考手册 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cssref/css-reference.html)
* [CSS 表格 (w3school.com.cn)](https://www.w3school.com.cn/css/css_table.asp)
