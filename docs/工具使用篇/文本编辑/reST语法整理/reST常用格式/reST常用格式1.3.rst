reST常用格式供参考
=======================

Sphinx官网资料：
https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

原格式和生成效果对照：
https://docutils.sourceforge.io/docs/user/rst/quickref.html



章节序号和标题鏈接
-----------------

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ`
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values.

:numref:`equ` `Equation Example <#equ>`__ is okay,

:numref:`equ` `Equation Example <#equation-example>`__ is okay.

:numref:`equ` `Equation Example <#equationexample>`__ is not okay.

:numref:`equ` `Equation Example <#Equation Example>`__ is not okay.

:numref:`equ` `Equation Example <#equation_example>`__ is not okay.

refer to :numref:`dmas` `DMA Support <#dmas>`__.


鏈接2
-----------------

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in
:numref:`err` `Error <#error>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values.



.. _equ:

Equation Example
-------------------------

.. _err:

Error
*************
說明：如果text大括號內有短線，這個命令的使用會導致報錯。在前面加上反斜線就okay.

.. math::
   \frac{\text{Rate of SSI data transmission}}{Rate of DW\_ahb\_dmac response to destination burst requests}


.. math::
   \frac{\text{Rate of SSI data transmission}}{\text{Rate of DW\_ahb\_dmac response to destination burst requests}}

空格的寫法
***************************

.. math::
   14\ (roundoff\ value)

.. math::
   \text{14 (roundoff value)}



短線的寫法
***************
前面加slash

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

Now the error is calculated as follows:

.. math::
   Error = \frac{\text{GBR - RBR}}{RBR} = 0.004729

The error percentage is as follows:

.. math::
   Error \% = 0.004729 × 100 = 0.473


斜体

*start time* + *data bits* + *parity* + *stop bits*.

*x*

DMA.CTL\ *x*.DEST_MSIZE = FIFO_DEPTH - UART.FCR[5:4]

DMA.CTL*x*.DEST_MSIZE = FIFO_DEPTH - UART.FCR[5:4]





试试表格中无序、有序列表
----------------------------
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | **Symbol**    | **Parameter** | **Conditions**    | **Min**  | **Typ**  | **Max**   | **Unit** |
   +===============+===============+===================+==========+==========+===========+==========+
   | V\ :sub:`IL`  | Standard IO   | 2.7 V             | -0.3     |          | 0.8       | V        |
   |               | low-level     | :math:`\leqslant` |          |          |           |          |
   |               | input         | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+



For information about I/O Static characteristics, refer to :ref:`Table 5.2 <Table5-2>`.

.. _Table5-2:

.. table:: I/O Static Characteristics

   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | **Symbol**    | **Parameter** | **Conditions**    | **Min**  | **Typ**  | **Max**   | **Unit** |
   +===============+===============+===================+==========+==========+===========+==========+
   | V\ :sub:`IL`  | Standard IO   | 2.7 V             | -0.3     |          | 0.8       | V        |
   |               | low-level     | :math:`\leqslant` |          |          |           |          |
   |               | input         | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`IH`  | Standard IO   | 2.7 V ≤           | 2        |          | 5.5       | V        |
   |               | high-level    | V\ :sub:`CCIN`    |          |          |           |          |
   |               | input         | ≤ 5.5 V           |          |          |           |          |
   |               | voltage       |                   |          |          |           |          |
   |               | (port A)      | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`IH`  | Standard IO   | 2.7 V ≤           | 2        |          | 3.6       | V        |
   |               | high-level    | V\ :sub:`CCIN`    |          |          |           |          |
   |               | input         | ≤ 5.5 V           |          |          |           |          |
   |               | voltage       |                   |          |          |           |          |
   |               | (port B)      | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`hys` | Standard IO   | 2.7 V ≤           |          | 220      |           | mV       |
   |               | Schmitt       | V\ :sub:`CCIN`    |          |          |           |          |
   |               | trigger       | ≤ 5.5 V           |          |          |           |          |
   |               | voltage       |                   |          |          |           |          |
   |               | hysteresis    | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`OL`  | Low-level     | 2.7 V ≤           |          |          | 0.4       | V        |
   |               | output        | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | ≤ 5.5 V           |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`OH`  | High-level    | 2.7 V ≤           | 2.4      |          |           | V        |
   |               | output        | V\ :sub:`CCIN`    |          |          |           |          |
   |               | Voltage       | ≤ 5.5 V           |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`OL`  | Low-level     | 2.7 V ≤           |          | 15       |           | mA       |
   |               | output        | V\ :sub:`CCIN`    |          |          |           |          |
   |               | current       | ≤ 5.5 V           |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`OH`  | High-level    | 2.7 V ≤           |          | 22       |           | mA       |
   |               | output        | V\ :sub:`CCIN`    |          |          |           |          |
   |               | Current       | ≤ 5.5 V           |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`Ikg` | Input         | 2.7 V ≤           |          | 1        |           | μA       |
   |               | leakage       | V\ :sub:`CCIN`    |          |          |           |          |
   |               | current       | ≤ 5.5 V           |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | R\ :sub:`PU`  | Pull-up       |                   | 74 k     | 80 k     | 158 k     | Ω        |
   |               | equivalent    |                   |          |          |           |          |
   |               | resistor      |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | R\ :sub:`PD`  | Pull-down     |                   | 62 k     | 75 k     | 203 k     | Ω        |
   |               | equivalent    |                   |          |          |           |          |
   |               | resistor      |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | C\ :sub:`IO`  | I/O pin       |                   |          | 5        |           | pF       |
   |               | capacitance   |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+



大于等于 小于等于号
-------------------

:math:`((SCLK\_DIV+1)*2)*(\text{Period of the SPI clock s})`

:math:`((SCLK_DIV+1)*2)*(Period of the SPI clock s)`

:math:`((SCLK\text{_}DIV+1)*2)*(Period of the SPI clock s)`

:math:`((SCLK\underline{~}DIV+1)*2)*(Period of the SPI clock s)`

小于等于 :math:`\leqslant`

大于等于 :math:`\geqslant`

:math:`\frac{1}{n(n+1)}`

:math:`\frac{SCLK period}{2} x (CS2SCLK + 1)`

Unless otherwise specified, typical data are based on T\ :sub:`A` = 25 掳C, V\ :sub:`CCIN`
= 5 V (for the 2.7 V :math:`\leqslant` V\ :sub:`CCIN` :math:`\leqslant` 5 V voltage range). They are given only
as design guidelines and are not tested.


:math:`&lt`

&lt；  左尖角号

&gt;   右尖角号

&copy；  ©版权

&trade;  ™商标

&reg;   ®商标

无序列表（间距不一样）
--------------------------

-  ADC channel selection
-  External/internal VREF selection
-  | Real voltage caculation:
   | Reg\ :sub:`adc_value` = ADC register value
   | Voltage = (Reg\ :sub:`adc_value` - 2048)/2048*3.3

调整
----------
-  ADC channel selection

-  External/internal VREF selection

-  | Real voltage caculation:
   | Reg\ :sub:`adc_value` = ADC register value
   | Voltage = (Reg\ :sub:`adc_value` - 2048)/2048*3.3


公式
--------


The abbreviation **Re**\ (.) and **Im**\ (.) will stand for the
real and imaginary part of a number, respectively. Since
imaginary part of a real number does not exist, we will
consider it to be zero and can usually simply discard it from
the equation where it is being used. Also, the
:math:`\bar{\alpha}`
will denote the complex conjugate of
:math:`\alpha`
.
In general throughout the documentation, the lower case Greek
symbols :math:`\alpha`
and :math:`\beta`
will denote scalars, lower case English letters in bold type
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
will denote vectors and capital English letters
:math:`A`
, :math:`B`
and :math:`C`
will denote matrices.

This function finds the (smallest) index of the element of
the maximum magnitude. Hence, the result is the first
:math:`i`
such that
:math:`\left| \mathbf{Im}\left( {x\lbrack j\rbrack} \right) \middle| + \middle| \mathbf{Re}\left( {x\lbrack j\rbrack} \right) \right|`
is maximum for
:math:`i = 1,\ldots,n`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{ incx}`
. Notice that the last equation reflects 1-based indexing
used for compatibility with Fortran.



This function constructs the Givens rotation matrix

.. math::
   G = \begin{pmatrix}
   c & s \\
   {- s} & c \\
   \end{pmatrix}

that zeros out the second entry of a
:math:`2 \times 1`
vector
:math:`\left( {a,b} \right)^{T}`
.
Then, for real numbers we can write

.. math::
   \begin{pmatrix}
   c & s \\
   {- s} & c \\
   \end{pmatrix}\begin{pmatrix}
   a \\
   b \\
   \end{pmatrix} = \begin{pmatrix}
   r \\
   0 \\
   \end{pmatrix}

where :math:`c^{2} + s^{2} = 1`
and :math:`r = a^{2} + b^{2}`
. The parameters :math:`a`
and :math:`b`
are overwritten with :math:`r`
and :math:`z`
, respectively. The value of :math:`z`
is such that :math:`c`
and :math:`s`
may be recovered using the following rules:

.. math::
   \left( {c,s} \right) = \begin{cases}
   \left( {\sqrt{1 - z^{2}},z} \right) & {\text{if}\left| z \middle| < 1 \right.} \\
   \left( {0.0,1.0} \right) & {\text{if}\left| z \middle| = 1 \right.} \\
   \left( 1/z,\sqrt{1 - z^{2}} \right) & {\text{if}\left| z \middle| > 1 \right.} \\
   \end{cases}

For complex numbers we can write

.. math::
   \begin{pmatrix}
   c & s \\
   {- \bar{s}} & c \\
   \end{pmatrix}\begin{pmatrix}
   a \\
   b \\
   \end{pmatrix} = \begin{pmatrix}
   r \\
   0 \\
   \end{pmatrix}

where
:math:`c^{2} + \left( {\bar{s} \times s} \right) = 1`
and
:math:`r = \frac{a}{|a|} \times \parallel \left( {a,b} \right)^{T} \parallel_{2}`
with
:math:`\parallel \left( {a,b} \right)^{T} \parallel_{2} = \sqrt{\left| a|^{2} + \middle| b|^{2} \right.}`
for :math:`a \neq 0`
and :math:`r = b`
for :math:`a = 0`
. Finally, the parameter :math:`a`
is overwritten with :math:`r`
on exit.




行间公式
--------------
.. math::
   \exp_a b = a^b, \exp b = e^b, 10^m

.. math:: exp_a b = a^b, exp b = e^b, 10^m

.. math:: \dim p, \deg q, \det m, \ker\phi

.. math:: dim p, deg q, det m, ker\phi

.. math:: T_J max = T_A max + (P_D max * θ_{JA})

.. math:: T_J max = T_A max + (P_D max * \theta_{JA})

.. math::
   \text{T}_\text{J} \text{max} = \text{T}_\text{A} \text{max} + (\text{P}_\text{D} \text{max} * \text{θ}_{\text{JA}})


行内公式
----------
This function computes the sum of the absolute values of the
elements of vector ``x``. Hence, the result is
:math:`\left. \sum_{i = 1}^{n} \middle| \mathbf{Im}\left( {x\lbrack j\rbrack} \right) \middle| + \middle| \mathbf{Re}\left( {x\lbrack j\rbrack} \right) \right|`
where
:math:`j = 1 + \left( {i - 1} \right)*\text{incx}`
. Notice that the last equation reflects 1-based indexing
used for compatibility with Fortran.


P\ :sub:`I/O`\max represents the maximum power dissipation on output pins.
:math:`P_{I/O} max = \sum (V_{OL} * I_{OL}) + ((V_{DD} – V_{OH}) * I_{OH})`

P\ :sub:`I/O`\max = ∑(V\ :sub:`OL` × I\ :sub:`OL`) + ((V\ :sub:`DD` –
V\ :sub:`OH`) × I\ :sub:`OH`)



The maximum chip junction temperature (T\ :sub:`J`\max) in degrees
Celsius can be calculated through equation
:math:`T_J max = T_A max + (P_D max * \theta_{JA})`

T\ :sub:`J` max = T\ :sub:`A` max + (P\ :sub:`D` max x θ\ :sub:`JA`)

where:

-  T\ :sub:`A`\max is the maximum ambient temperature in °C.

-  θ\ :sub:`JA` is the package junction-to-ambient thermal resistance in °C/W.

-  P\ :sub:`D`\max is the sum of P\ :sub:`INT`\max and P\ :sub:`I/O`\max
   (P\ :sub:`D`\max = P\ :sub:`INT`\max + P\ :sub:`I/O`\max).

-  P\ :sub:`INT`\max is the product of I\ :sub:`DD` and V\ :sub:`DD` in Watts.
   This is the maximum chip internal power.




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

上标(subscript)：

* H\ :sub:`2`\ O
* HO\ :sub:`2`

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


强调
---------

*斜体强调*

**粗体强调**


注释
---------

..
 我是注释内容
 你们看不到我


自动生成序号
--------------------
#. 有序序号
#. 无序列表
#. 有序列表



引用
---------
引用不同文档中章节标题
++++++++++++++++++++++++++

参见 :ref:`图片引用语法`。

|vspace| |br|

(即使要引用的章节不在本文档中也是用这种格式。
要引用的章节标题前加".. _图片引用语法:")

.. _图片引用语法:

插入图片+图片引用语法
+++++++++++++++++++++++++++

参见 :ref:`图片21` （html显示为：参见 图 2-1 MetaX软件栈）（即图片标题）

参见 :ref:`图 2-1 <图片21>` 

参见 :ref:`表 2-1 <API函数和数据类型>` 。

.. _图片21:

.. figure:: MetaX软件栈.png
   :scale: 50 %
   :alt: MetaX
   :align: center

   **图 2-1 MetaX软件栈**
   

表格引用
+++++++++++++++++++++++
``.. 后面有空格，然后_。note, danger都是如此。``


mcDNN X.X.0 中添加、弃用和删除的 API 函数，参见 :ref:`表 2-1 <API函数和数据类型>`。

.. _API函数和数据类型:

.. table:: 表 2-1 添加的API函数和数据类型

    +------------------+
    | 后端描述符类型   |
    +==================+
    | XXXXXXX          |
    +------------------+
    | XXXXXXX          |
    +------------------+


引用其他文档
----------------------

1. 引用当前文件夹下的文件
++++++++++++++++++++++++++++++++
参见 :doc:`沐曦软件栈<软件栈>`。

参见 :doc:`软件栈`。

参见 :download:`csv表格引用 <表格.csv>`。

说明：

* :doc：前面要有空格，后面没有空格。

* :ref:同样，前面有空格，后面不要加空格。空格多加或少加生成出来的HTML链接会显示不出来。

* <>中为文件名称，<>前面为显示的文件名，为空的话则默认为文档title。 



2. 引用其他文件夹下的文件
++++++++++++++++++++++++++++++++

1. 引用根目录下的文件夹中的文件：参见：doc:`/api_reference/api_reference`。

2. 引用上一层目录下的文件夹：参见 :doc:`../api_reference/api_reference`。

* "./"：代表目前所在的目录。

* " ../"代表上一层目录。

* "/"：代表根目录。



警告标示：危险、注解、说明
-------------------------------------
资料：

https://docutils.sourceforge.io/docs/ref/rst/directives.html#attention

https://learningos.github.io/uCore-Tutorial-Book/rest-example.html  编译后的效果

.. NOTE::
   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.


.. DANGER::
   危险请勿靠近！


.. Error::
   错误

.. Attention::
   注意

.. Caution::
   小心

.. Hint::
   提示

.. Important::
   重要

.. Tip::
   小提示

.. Warning::
   警告


代码块
----------------------

行内代码：``vip_create_buffer()``

代码格式：

Use the `printf()` function. （注意不是引号）

针对在代码区段内插入反引号的情况：

``There is a literal backtick (`) here.``

这是个什么东西：.. c:function:: MXKW_STATUA MXKWAPI mxkwOpenMXCD(void)
(生成出来是加粗的效果)

引用包含代码的文件：

.. literalinclude:: ../media/decode_example.C
    :caption: decode_example
    :language: c 
    :linenos:
    :name: example.c


::

  代码块
  代码块

.. code-block:: c 
   :linenos: （行号？？？）

    git add XXXX
    git commit -s --amend --date=now

.. code-block:: bash

    git add XXXX
    git commit -s --amend --date=now

.. code:: C

   int mxgpu 

.. code-block:: c 
   :linenos: （行号？？？）

   代码内容

超链接
-------------------
1. 直接嵌入网址：`野火公司官网 <http://www.embedfire.com>`_

2. 使用引用的方式把具体网址定义在其它地方： `野火公司官网`_

.. _野火公司官网: http://www.embedfire.com

例如：

`百度 <https://search.chongbuluo.com/>`_

`百度公司官网`_

.. _百度公司官网: https://search.chongbuluo.com/

3. 链接的另一种写法：这种写法可提高可读性。

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

This is a paragraph that contains `域名网址`_.

.. _域名网址: https://domain.invalid/


表格
----------------

.. table:: 表 1-1 UMD API Interface Table

   ==========    =============     =========    ========
   MARC0         API               Parameter    Other
   ==========    =============     =========    ========
   MX1           neural1           Para1        E = mc\ :sup:`2`
   MX2           neural2           Para2        H\ :sub:`2`\O
   MX3           neural3           Para3
   ==========    =============     =========    ========


::

  .. csv-table:: Frozen Delights!
     :header: "Treat", "Quantity", "Description"
     :widths: 15, 10, 30

     , 2.99, "On a stick!"
     , 1.49, "If we took the bones out, it wouldn't be
     crunchy, now would it?"
     , 1.99, "On a stick!"



.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   , 2.99, "On a stick!"
   , 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   , 1.99, "On a stick!"


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+




List Table
++++++++++++++++++++++++



List Table 1: 去掉align就能正确显示(上下标+无序列表)
*******************************************************

.. list-table:: 表 2-1 协议格式
    :widths: 50 50 50 50 50 50 50 50
    :header-rows: 1

    *
       - Major Version
       - Minor Version
       - Master ID
       - Slave ID
       - Category
       - Command Data
       - Send/Receive
       - H\ :sub:`2`\O
    *
        - * b[31:30]
          * good
        - b[29:28]
        - b[27:24]
        - b[23:20]
        - b[19:12]
        - b[11:4]
        - b[3:0]
        - H\ :sub:`2`\O

List Table 2：设置了align，显示不正确
***************************************
.. list-table:: 表 2-1 协议格式
    :widths: 50 50 50 50 50 50 50
    :header-rows: 1
    :align: left

    *
        - Major Version
        - Minor Version
        - Master ID
        - Slave ID
        - Category
        - Command Data
        - Send/Receive

    *
        - b[31:30]
        - b[29:28]
        - b[27:24]
        - b[23:20]
        - b[19:12]
        - b[11:4]
        - b[3:0]



.. table:: Table 5‑1 Voltage Characteristics

    +-------------------------------+------------------------+------+-----+------+
    | Symbol                        | Ratings                | Min  | Max | Unit |
    +===============================+========================+======+=====+======+
    | V\ :sub:`CCIN`-V\ :sub:`SS`   | External supply        | 0.3 | 5.5 | V    |
    |                               | voltage                |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IL`                  | Input Low Voltage on   | -0.3 | 0.8 | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IH`                  | Input High Voltage on  | 2    | 5.5 | V    |
    |                               | signal pin(PortA)      |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IH`                  | Input High Voltage on  | 2    | 3.6 | V    |
    |                               | signal pin(PortB)      |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OL`                  | Output Low Voltage on  |      | 0.4 | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OH`                  | Output High Voltage on | 2.4  |     | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+



不支持html标签
----------------------------------------------------------
<font size=3 color="red">字体颜色为红色，大小为3</font> 不识别

问题：
--------------

1. 文本缩进

定义1
 这是定义1的内容

定义2
 这是定义2的内容



行块：
 | 行块
 | 行块


参考资料:
------------------
交叉引用： https://www.sphinx.org.cn/usage/restructuredtext/roles.html#ref-role

官网（很多资料）：
https://www.sphinx.org.cn/usage/configuration.html#options-for-latex-output

https://ebf-contribute-guide.readthedocs.io/zh_CN/latest/rest-syntax/cross-reference.html#id7

