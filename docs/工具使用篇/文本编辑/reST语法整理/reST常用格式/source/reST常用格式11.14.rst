reST常用格式供参考
=======================

Sphinx官网资料：
https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

原格式和生成效果对照：
https://docutils.sourceforge.io/docs/user/rst/quickref.html

上标/下标
----------------
上标(superscript)：

* E = mc\ :sup:`2`
* E = m\ :sup:`2`\ c

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

参见 :ref:`表 2-1 <API函数和数据类型>`。

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

