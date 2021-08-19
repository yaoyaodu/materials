# Python

更多信息参见：

- [Python2.7.14 中文手册](https://www.runoob.com/manual/pythontutorial/docs/html/)
- [Python IDE(集成开发环境)介绍](https://www.runoob.com/python/python-ide.html)
- [Python 编码规范(Google)](https://www.runoob.com/w3cnote/google-python-styleguide.html)
- [Python 3.X版本的教程](https://www.runoob.com/python3/python3-tutorial.html)

Python自动化办公：

* [Python处理excel自动化办公](https://www.bilibili.com/video/BV1Hy4y1S78a/)

* [Python自动化办公（B站内容最全的！有源代码 适合小白）](https://www.bilibili.com/video/BV1y54y1i78U/)
* [Python办公自动化全套代码](https://blog.csdn.net/xo3ylAF9kGs/article/details/109281438)

## 交互式命令行（>>>）

* 直接打开Python程序，输入`print("Hello, World!")`。

  ![image-20210819092702872](https://i.loli.net/2021/08/19/Wrl6RToMaiQtUO3.png)



* 在命令提示符中输入python，回车，然后输入`print("Hello, World!")`。

  ![image-20210819092116403](https://i.loli.net/2021/08/19/MgUBp5k8KaIhxdY.png)
  
  （执行`exit()`命令退出python）

## Python代码编写及运行

1. 编写：使用文本编辑器记事本或Sublime Text编写保存，命名为XXX.py，保存在桌面。
2. 在命令行模式中，输入python C:\Users\user\Desktop\hello.py。回车。 

![image-20210819112616055](https://i.loli.net/2021/08/19/SArKdwI9sa6iJbo.png)



## 标识符

- 第一个字符必须是字母表中字母或下划线 **_** 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。

在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

## 保留字

即关键字。能把它们用作任何标识符名称。

![image-20210819104212520](https://i.loli.net/2021/08/19/jq7I1eSYynrdQoK.png)

## 注释

Python中单行注释以 **#** 开头。

多行注释可以用多个 **#** 号， **'''** 和 **"""**。

## 行与缩进

python最具特色的就是**使用缩进来表示代码块，不需要使用大括号 {}** 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

## 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 `\`来实现多行语句。

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠。

## 数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- **int** (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
- **bool** (布尔), 如 True。
- **float** (浮点数), 如 1.23、3E-2
- **complex** (复数), 如 1 + 2j、 1.1 + 2.2j



## 字符串(String)

- python中单引号和双引号使用完全相同。
- 使用三引号(**'''** 或 **"""**)可以指定一个多行字符串。
- 转义符 **\**
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：**变量[头下标:尾下标:步长]**

## 空行

Python内置标准模块，标准库

一个模块就是一个文件

互相调用：



## 定义功能def函数

#### 无参定义函数

##### 1. 语法

```python
def function_name():
    expressions
```

Python 使用`def` 开始**函数定义**，紧接着是**函数名**，**括号内部为函数的参数**。

内部为函数的**具体功能实现代码**，如果想要函数有返回值, 在 `expressions` 中的逻辑代码中用`return` 返回。

##### 2. 实例

## 导入模块

![image-20210819113209794](https://i.loli.net/2021/08/19/gWal4MBhFXIDocC.png)

## Excel处理—openpyxl模块

![image-20210819150525214](https://i.loli.net/2021/08/19/SNB2dkugG98wpKr.png)

![image-20210819153239218](https://i.loli.net/2021/08/19/8grVj6zmCJdac5s.png)



wb = load_workbook(“集训营报名人数.xlsx”)

print(wb.sheetnames)

print(wb.get_sheet_names)









## Python之禅

```python
Python之禅 by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```

```swift
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

