.. epigraph::
   
   No matter where you go, there you are. 
   
   -- Banzai


Pandoc
--------------------------------------

pandoc是一个haskell编写的万能文档转换工具，可以在Markdown、reStructuredText、textile、HTML、DocBook、LaTeX、Word等等多种格式中互相转换。
这里用pandoc把reStructuredText转换成.docx格式的Word文档。基本的用法是这样，把chpater1.rst转换成chapter1.docx。

.. code::

   $ pandoc -o chapter1.docx -f rst+east_asian_line_breaks -s chapter1.rst

默认情况下，pandoc会把换行转换成空格，但这是为西方语言设置的默认值。对于中文，就需要开启east_asian_line_breaks，去除换行引入的空格。


上标/下标
----------------

上标(superscript)：

* E = mc\ :sup:`2`
* E = m\ :sup:`2`\ c
* E = m\ :sup:`2`\c
* E = m\ :sup:`2` c （有空格）
* I\ :sub:`DD` and V\ :sub:`DD`
* I\ :sub:`DD`\ and V\ :sub:`DD`\
* T\ :sub:`J`\max = T\ :sub:`A`\max + (P\ :sub:`D`\max x θ\ :sub:`JA`)
* T\ :sub:`A`\max is the maximum ambient temperature in °C.

下标(subscript)：

* H\ :sub:`2`\ O
* HO\ :sub:`2`


replace
-----------

提高可读性也可使用下面的方式：

The chemical formula for pure water is |H2O|.

.. |H2O| replace:: H\ :sub:`2`\ O

你好吗 |T2H| （注意前后都必须加空格）

.. |T2H| replace:: T\ :sub:`2`\ H

资料来源：https://docutils.sourceforge.io/docs/ref/rst/roles.html#subscript



插入空行
----------------------------------
用空行之前先进行定义：

.. |vspace| raw:: latex

   \vspace{1mm}

.. |br| raw:: html

   <br />

然后在需要插入空行的地方插入：|vspace| |br|




小于等于号、大于等于号
--------------------------------------

小于等于号: Carrier frequency :math:`\leqslant` 60 KHz

大于等于:  :math:`\geqslant`




引用参考(Citation Reference)
--------------------------------------------------

引用参考与上面的脚注有点类似。引用参考的内容通常放在页面结尾处。


引用参考的内容通常放在页面结尾处，比如 [书1]_ ，[书2]_ 。

.. [书1] 参考引用一
.. [书2] 参考引用二



脚注引用(Footnote Reference)
--------------------------------------------------

另外，中文和内联语法如果没有空格之类的字符隔开，则会出现语法错误。如果直接用空格，那么最终文档中也会有额外的空格。
根据reST文档规范，可以用反斜线转义空格，具体处理如下。

天地有\ **大美** \而不言，四时有明法而不议，万物\ [10]_\ 有成理而不说。圣人者，原天地之美而
达万物之理。是故至人无为，大圣不作，观于天地之谓也。
 
.. [10] 这是一个脚注


脚注引用，有这几个方式：有手工序号(标记序号123之类)、自动序号(填入#号会自动填充序号)、自动符号(填入*会自动生成符号)。

手工序号可以和#结合使用，会自动延续手工的序号。

# 表示的方法可以在后面加上一个名称，这个名称就会生成一个链接。



Autonumbered footnotes are possible, like using [#]_ and [#]_.

.. [#] This is the first one.
.. [#] This is the second one.

They may be assigned 'autonumber labels' - for instance, [#fourth]_ and [#third]_.

.. [#third] a.k.a. third_

.. [#fourth] a.k.a. fourth_


Footnote references, like [5]_. Note that footnotes may get rearranged, e.g., to the bottom of the "page".

.. [5] A numerical footnote. Note there's no colon after the ``]``.


Auto-symbol footnotes are also possible, like this: [*]_ and [*]_.

.. [*] This is the first one.
.. [*] This is the second one.


超链接
-------------------------

替换引用(Substitution Reference)
*************************************

替换引用就是用定义的指令替换对应的文字或图片，和内置指令(inline directives)类似。

这是 |logo| github的Logo，我的github用户名是:|name|。

.. |logo| image:: https://help.github.com/assets/images/site/favicon.ico
.. |name| replace:: Who



隐式超链接(Implicit Hyperlink)
*************************************

小节标题、脚注和引用参考会自动生成超链接地址，使用小节标题、脚注或引用参考名称作为超链接名称就可以生成隐式链接。

隐式超链接详细内容，参见 `隐式超链接(Implicit Hyperlink)`_ 。


If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 


If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case, 
because *sync_delay* equals one pclk as described in 
:numref:`err` `Error <#error>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 

空行
-------------

空行1
********************************

MCU芯片是指微控制单元，是把中央处理器的频率与规格做适当缩减，并将内存、计数器、USB、A/D转换、UART、PLC、DMA等周边接口，
甚至LCD驱动电路都整合在单一芯片上，形成芯片级的计算机，为不同的应用场合做不同组合控制，所以MCU芯片就是单片机芯片。

MCU芯片的应用

大多数情况下4位MCU应用于计算器、汽车仪表、汽车防盗装置、呼叫器、无线电话、CD播放器、液晶显示控制器、液晶游戏机、
儿童玩具、磅秤、充电器、胎压仪、温湿度计、遥控器和傻瓜照相机等。

8位MCU应用于电表、电机控制器、电动玩具机、变频冷气机、呼叫器等等。其中，8位、16位单片机主要应用于一般的控制领域，
一般不用操作系统。

| 而16位MCU主要应用于行动电话、数码相机和摄录机等；
| 
| 大多数32位MCU应用于Modem、GPS、PDA、HPC、STB、Hub.Bridge、Router.工作站、ISDN电话、激光打印机及彩色传真机；
  通常使用64位嵌入式操作系统进行网络操作、多媒体处理等复杂处理的情况。

大多数32位MCU应用于Modem、GPS、PDA、HPC、STB、Hub.Bridge、Router.工作站、ISDN电话、激光打印机及彩色传真机；
通常使用64位嵌入式操作系统进行网络操作、多媒体处理等复杂处理的情况。


空行2
********************************

| MCU芯片是指微控制单元，是把中央处理器的频率与规格做适当缩减，并将内存、计数器、USB、A/D转换、UART、PLC、DMA等周边接口，
  甚至LCD驱动电路都整合在单一芯片上，形成芯片级的计算机，为不同的应用场合做不同组合控制，所以MCU芯片就是单片机芯片。
| MCU芯片的应用
| 大多数情况下4位MCU应用于计算器、汽车仪表、汽车防盗装置、呼叫器、无线电话、CD播放器、液晶显示控制器、液晶游戏机、
  儿童玩具、磅秤、充电器、胎压仪、温湿度计、遥控器和傻瓜照相机等。
| 8位MCU应用于电表、电机控制器、电动玩具机、变频冷气机、呼叫器等等。其中，8位、16位单片机主要应用于一般的控制领域，
  一般不用操作系统。
| 而16位MCU主要应用于行动电话、数码相机和摄录机等；
| 
| 大多数32位MCU应用于Modem、GPS、PDA、HPC、STB、Hub.Bridge、Router.工作站、ISDN电话、激光打印机及彩色传真机；
  通常使用64位嵌入式操作系统进行网络操作、多媒体处理等复杂处理的情况。
| 大多数32位MCU应用于Modem、GPS、PDA、HPC、STB、Hub.Bridge、Router.工作站、ISDN电话、激光打印机及彩色传真机；
  通常使用64位嵌入式操作系统进行网络操作、多媒体处理等复杂处理的情况。

表格
-------------------------


网格表(Grid Tables)
*************************************

网格表中使用的符号有： ``-、=、|、+`` 。

``-`` 用来分隔行， = 用来分隔表头和表体行，| 用来分隔列，+ 用来表示行和列相交的节点。

.. _gridtable1:

.. table:: Grid Table 1
   :widths: grid

   +------------+------------+-----------+
   | Header 1   | Header 2   | Header 3  |
   +============+============+===========+
   | body row 1 | column 2   | column 3  |
   +------------+------------+-----------+
   | body row 2 | Cells may span columns.|
   +------------+------------+-----------+
   | body row 3 | Cells may  | - Cells   |
   +------------+ span rows. | - contain |
   | body row 4 |            | - blocks. |
   +------------+------------+-----------+


.. _gridtable2:

.. table:: Grid Table 2 (Line Blocks)
   :widths: grid

   +------------+--------------+-----------+
   | Header 1   | Header 2     | Header 3  |
   +============+==============+===========+
   | body row 1 | column 2     | column 3  |
   +------------+--------------+-----------+
   | body row 2 | Cells may span columns.  |
   +------------+--------------+-----------+
   | body row 3 || Cells may   || Cells    |
   +------------+| span rows.  |  contain  |
   | body row 4 || Span rows   || blocks.  |
   +------------+--------------+-----------+



简单表(Simple Tables)
*************************************

| 简单表相对于网格表，少了 ``|`` 和 + 两个符号，只用 - 和 = 表示。
|               只有在前面有正常的行时，竖线后的缩进才生效。
|               简单表相对于网格表，少了 ``|`` 和 + 两个符号，只用 - 和 = 表示。
|
| 标题可合并单元格

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

行也可以合并单元格

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
    False     True
------------  ------
False  True   True
True   True   True
=====  =====  ======


合并方式？

========  =====  ======
  A        B     A or B
========  =====  ======
False     False  False
False     True   True
False     True   True
|         
          True   True
========  =====  ======




X 
----------

乘号 ×

摄氏度 °C


分隔符
***************************

分隔符就是一条水平的横线，是由 4 个 - 或者更多组成，需要添加换行。

上面部分

------------

下面部分   


定义列表(Definition Lists)
***************************

定义列表可以理解为解释列表，即名词解释。

条目占一行，解释文本要有缩进；多层可根据缩进实现。

定义1
 这是定义1的内容

定义定义2
 这是定义2的内容


文档测试块(Doctest Blocks)
***************************

文档测试块是交互式的Python会话，以 >>> 开始，一个空行结束。

>>> print "This is a doctest block."
This is a doctest block.

新的一行。



文字块(Literal Blocks)
***************************

下面是文字块内容：
::

   这是一段文字块
   同样也是文字块
   还是文字块

这是新的一段。



A paragraph containing only two colons
indicates that the following indented
or quoted text is a literal block.

::

  Whitespace, newlines, blank lines, and
  all kinds of markup (like *this* or
  \this) is preserved by literal blocks.

  The paragraph containing only '::'
  will be omitted from the result.

The ``::`` may be tacked onto the very
end of any paragraph. The ``::`` will be
omitted if it is preceded by whitespace.
The ``::`` will be converted to a single
colon if preceded by text, like this::

  It's very convenient to use this form.

Literal blocks end when text returns to
the preceding paragraph's indentation.
This means that something like this
is possible::

      We start here
    and continue here
  and end here.

Per-line quoting can also be used on
unindented literal blocks::

> Useful for quotes from email and
> for Haskell literate programming.







行块(Line Blocks)
***************************

行块对于地址、诗句以及无装饰列表是非常有用的。

行块是以 | 开头，每一个行块可以是多段文本。

| 前后各有一个空格。

下面是行块内容：
 | 这是一段行块内容
 | 这同样也是行块内容
   还是行块内容

这是新的一段。

 | 从此鲜花赠自己，纵马踏花向自由。
 | 我与旧事归于尽，来年依旧迎花开。


| Line blocks are useful for addresses,
| verse, and adornment-free lists.  （显示为两行）
|
| Each new line begins with a
| vertical bar ("|").
|     Line breaks and initial indents
|     are preserved.
| Continuation lines are wrapped
  portions of long lines; they begin
  with spaces in place of vertical bars. （显示为一行）



   

块引用(Block Quotes)
***************************

块引用是通过缩进来实现的，引用块要在前面的段落基础上缩进。

通常引用结尾会加上出处(attribution)，出处的文字块开头是 --、--- 、—，后面加上出处信息。

块引用可以使用空的注释 .. 分隔上下的块引用。

注意在新的块和出处都要添加一个空行。

下面是引用的内容：

    “真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”

    --- 鲁迅

..

    “人生的意志和劳动将创造奇迹般的奇迹。”

    — 涅克拉索



Block quotes are just:

    Indented paragraphs,

        and they may nest.

   



选项列表(Option Lists)
***************************

选项列表是一个类似两列的表格，左边是参数，右边是描述信息。当参数选项过长时，参数选项和描述信息各占一行。

选项与参数之间有一个空格，参数选项与描述信息之间至少有两个空格。



-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too




字段列表 (Field Lists)
*************************** 

:标题: reStructuredText语法说明

:作者:
 - Alice
 - Hank
 - Wendy

:时间: 2016年06月21日

:概述: 这是一篇
 关于reStructuredText的
 语法说明。


:Authors:
    Tony J. (Tibs) Ibbs,
    David Goodger

    (and sundry other good-natured folks) （上面空一行，此处另起一行）

:Version: 1.0 of 2001/08/08
:Dedication: To my father.



符号列表 (Bullet Lists)
*************************** 

符号列表可以使用 ``-、 *、+`` 来表示。

*不同的符号结尾需要加上空行*，下级列表需要有空格缩进。


- 符号列表1
- 符号列表2

  + 二级符号列表1

  - 二级符号列表2

  * 二级符号列表3

* 符号列表3

+ 符号列表4




Glossary
-------------------------

.. glossary::

   UART 
      Universal Receiver Transmitter


   USB 
      Universal Bus



加粗居中 Right-Aligned
--------------------------------

居中
***************************

.. centered:: Confidential

居中加粗
***************************

.. centered:: **Confidential**


空格
***************************

space ``\``

`` \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ confidential ``

empty math format   :math:`\text{                      Confidential}`

space 

35656     ``space before``

行内代码：   ``                  行内文本(inline literal)通常显示为等宽文本，空格可以保留，但是换行不可以。``

行内代码：``vip_create_buffer()``

行内代码：``space before``


行内代码： ``行内文本(inline literal)通常显示为等宽文本，                  空格可以保留，但是换行不可以。``



版权所有
----------------

::

  Copyright |copy| 2023, |MACAMACA (TM)| |---| all rights reserved.

  .. |copy| unicode:: 0xA9 .. copyright sign

  .. |MACAMACA (TM)| unicode:: MACAMACA U+2122 .. with trademark sign

  .. |---|  unicode:: U+02014 .. em dash
   :trim:


Copyright |copy| 2023, |MACAMACA (TM)| |---| all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign

.. |MACAMACA (TM)| unicode:: MACAMACA U+2122 .. with trademark sign

.. |---|  unicode:: U+02014 .. em dash
   :trim:





章节自动编号
--------------------

``.. numbered::``

``.. sectnum::``

Topic
-------------

:标题: reStructuredText语法说明

:作者:
 - Alice
 - Hank
 - Wendy

:时间: 2016年06月21日

:概述: 这是一篇
 关于reStructuredText的
 语法说明。


If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 


directive todo
***************************

启用了todo扩展，让Sphinx支持 ``.. todo::`` 指令的解析，可以用来标记待办或未完事宜。
如 :numref:`tododirective` 所示。

启用了imgmath扩展，Sphinx会调用系统环境下的latex把数学公式渲染成图片插入到构建好的文档中，这里有一些额外的依赖。
我是在WSL中的Ubuntu中操作的，依赖安装方法如下。

.. code::

   $ sudo apt-get install pdfimages poppler-utils tex-live texstudio texlive \
   texlive-latex-extra dvipng


.. _tododirective:

.. figure:: test_figure/sphinx-quickstart.png
   :scale: 100%

   启用todo扩展


directive rubric
***************************

.. rubric:: paragraph heading 


directive container
***************************


.. container:: custom
   
   This paragraph might be rendered in a custom way.


directive header
***************************

.. header:: This space for rent.

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 

directive topic
***************************

.. topic:: 試試行不行
   
   If CLOCK_MODE equals 1, there is no idle time between back-to-back
   characters if data is ready in the transmit FIFO. In this case,
   because *sync_delay* equals one pclk as described in  :numref:`equ` 
   `Equation Example <#equ>`__, the requirement to avoid idle time
   between consecutive characters is met for all {DLH,DLL} values. 


directive sidebar
***************************
   
.. sidebar:: 出现的位置
   
   出现在哪里呢
   这个sidebar
   


分栏（仅对HTML有效）
--------------------------------


.. hlist::
   :columns: 4
   
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified


   


.. _equ:

Equation Example
-------------------------

公式中空格的实现方式
***************************

``14\ (roundoff\ value)``

``\text{14 (roundoff value)}``

.. math::
   14\ (roundoff\ value)

.. math::
   \text{14 (roundoff value)}


.. _err:

Error
*************

注意：如果text{}內有``_``，这个命令的使用会导致报错。在``_``前面加上反斜线就okay。

``\frac{\text{Rate of SSI data transmission}}{Rate of DW\_ahb\_dmac response to destination burst requests}``

.. math::
   \frac{\text{Rate of SSI data transmission}}{Rate of DW\_ahb\_dmac response to destination burst requests}


.. math::
   \frac{\text{Rate of SSI data transmission}}{\text{Rate of DW\_ahb\_dmac response to destination burst requests}}

公式中短线的实现方式
******************************

前面加slash``\``

.. math::
   \text{DLF} = BRD_F * 2^{DLF\_SIZE} 
   
   
.. math::
   BRD_F * 2^{DLF\underline{~}SIZE}
   
.. math:: \label{equ1}
   \text{DLF} = BRD_F * 2^{DLF\underline{~}SIZE} 

This equation \ref{equ1} is not okay?
   
.. math::
   \text{DLF} = BRD_F * 2^{DLF\_SIZE} = 0.866132364 * 16 = 13.858117824 = \text{14 (roundoff value)}

 


Therefore, the Generated Baud Rate (GBR) is as follows:

.. math::
   GBR = \frac{\text{Serial Clock}}{(16 × GD)} = \frac{133}{16 × 1.875} = 4433333.333 



.. math::
   Error = \frac{\text{GBR - RBR}}{RBR} = 0.004729 




公式中%前面要加slash
******************************

.. math::
   Error \% = 0.004729 × 100 = 0.473 


脚注
******************************

脚注引用一 [1]_

脚注引用二 [2]_

脚注引用三 [#]_

脚注引用四 [#链接]_

脚注引用五 [*]_

脚注引用六 [*]_

脚注引用七 [*]_

.. [1] 脚注内容一
.. [2] 脚注内容二
.. [#] 脚注内容三
.. [#链接] 脚注内容四 链接_
.. [*] 脚注内容五
.. [*] 脚注内容六
.. [*] 脚注内容七



引用参考(Citation Reference)
******************************

引用参考与上面的脚注有点类似。引用参考的内容通常放在页面结尾处。


引用参考的内容通常放在页面结尾处，比如 [One]_ ，[Two]_ 。

.. [One] 参考引用一
.. [Two] 参考引用二

Citation references, like [CIT2002]_. Note that citations may get rearranged, e.g., to the bottom of the "page".

.. [CIT2002] A citation
   (as often used in journals).

Citation labels contain alphanumerics, underlines, hyphens and fullstops. Case is not significant.

Given a citation like [this]_, one can also refer to it like this_.

.. [this] here.


rst转word
******************************

参见 https://zhuanlan.zhihu.com/p/108886400



参考内容：

* https://www.jianshu.com/p/1885d5570b37

* https://docutils.sourceforge.io/docs/user/rst/quickref.html