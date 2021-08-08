# CSS (Cascading Style Sheets) 叠层样式表

推荐教程：[CSS 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-tutorial.html)

## 前端最核心的三个技术

- HTML: 用于控制网页的结构
- CSS：用于控制网页的外观（给HTML标记添加的样式）

- Javascript: 用于控制网页的行为

## CSS语法格式

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

示例：加个图片

## CSS选择器

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
  * 在平常工作中，会使用以下写法，来给链接加不同的样式：
    * a:link, a:visited{ color:#444; text-decoration:none; } //将“正常状态”和“访问过的状态”合二为一。
    * a:hover{ color:#990000; text-decoration:underline; } //“鼠标放上”单做一种效果

## 引入CSS的方法

* 嵌入式
  * 通过`<style>`标记，来引入CSS样式。
  * 语法格式：`<style type = “text/css"></style>`
  * `<style>`中的CSS样式，只能给当前网页来使用。同一个网页中，`<style>`标记可以多次出现。

- 外联式
  - 通过`<link>`标记，来入引一个外部的CSS文件(.css)，这样的话，可以实现公共的CSS代码被多个网页共享。
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

更详细信息参见：

* [CSS 选择器 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cssref/css-selectors.html)
* [CSS 实例 | 菜鸟教程 (runoob.com)](https://www.runoob.com/css/css-examples.html) （实用，重点看）
* [CSS 参考手册 | 菜鸟教程 (runoob.com)](https://www.runoob.com/cssref/css-reference.html)
* [CSS 表格 (w3school.com.cn)](https://www.w3school.com.cn/css/css_table.asp)
* [十六进制颜色代码表，图表及调色板 - Encycolorpedia](https://encycolorpedia.cn/)

![padding margin](https://i.loli.net/2021/08/05/42gcGrmNKIbS9Qv.png)

