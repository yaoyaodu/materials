.. epigraph::
   
   No matter where you go, there you are. 
   
   -- Banzai


Footnotes
-------------------------

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



简单表(Simple Tables)
-------------------------

标题可合并单元格

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
| False   True   True
|         True   True
========  =====  ======




X 
----------

乘号 ×


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





