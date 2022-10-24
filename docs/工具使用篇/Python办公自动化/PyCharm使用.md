# PyCharm使用

资料：

- [PyCharm使用(完全图解(最新经典)) - 火星小编 - 博客园 (cnblogs.com)](https://www.cnblogs.com/programmer-tlh/p/5733689.html)
- https://blog.csdn.net/cnds123/article/details/107656496
- PyCharm下载地址：[Download PyCharm: Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/download/#section=windows)
- 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
- **JetBrains Toolbox**

## 问题：

Q1：利用PyCharm打开rst文档，rst文档中的中文字符显示为乱码。

A1：[解决用pycharm书写README.rst汉字乱码问题_pycharm rst文件](https://blog.csdn.net/chianti_cv/article/details/125219356)

1. 在设置中，把所有的文件编码都改成**UTF-8**。
2. 如果问题没有解决，点击**Help**菜单栏选择“**Edit Custom VM Options**”。
3. 在打开的文件最后增加一行`-Dfile.encoding=UTF-8`。

## Win10中PyCharm2020.1.4安装使用入门（修订版）

Win10中要安装PyCharm，**需要先安装Python**，免费、开源。

PyCharm是**JetBrains** 打造的一款Python **IDE**（集成开发环境，**Integrated Development Environment**），具备强劲的功能： 

* 调试
* 语法高亮
* Project管理
* 代码跳转
* 智能提示
* 自动完成
* 单元测试
* **版本控制**

该IDE还提供了一些高级功能，**支持Django框架下的专业Web开发**。

PyCharm分专业版（Professional）和社区版（Community）。

* **专业版是收费的需要激活**，但可以先评估试用30天。

* **社区版是免费的**，社区版的功能不如专业版全。

**PyCharm专业版**增加了**科学工具、Web开发、Python Web框架、Python分析器、远程开发、支持数据库与SQL**等更多高级功能。一般来说，我们使用Community版本就够了。

## PyChram常用快捷键

alt+ctrl+s     　　     #打开保存界面

tab            　　    #选择要缩进的代码，按键缩进

shift+tab       　　    #选择要缩进的代码，按键减少缩进

ctrl+d        　　     #**复制本行粘贴到下一行**

ctrl+/                  #**选择要添加注释的行，按键进行#添加或去除**

双按shift              #全局搜索

ctrl+f                  #查找

**ctrl+r**                  #查找替换

CTRL + F1                     #显示错误或警告的描述

## PyChram中使用插件

File->**settings-> Plugins**
