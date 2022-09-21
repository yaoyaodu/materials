Python
===================

资料：

* [Problems - LeetCode](https://leetcode.com/problemset/all/)
* https://leetcode.com/problem-list/top-100-liked-questions/
* https://leetcode.com/
* 内容很不错：https://realpython.com/tutorials/all/

重点概念：

* **方法是Python可对数据执行的操作**。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。
* 在Python中，注释用井号（#）标识。

## .py：函数程序

编写程序时，编辑器会以各种方式突出程序的不同部分。语法突出：

* print是函数名称，因此将其显示为蓝色。
* "Hello world"不是Python代码，因此将其显示为橙色。

## 变量

````python
message = "Hello Python World!"
print(message)
````

变量message，每个变量都存储了一个值，即与变量相关联的信息。此处存储的值为文本“Hello Python World!”。

## 字符串（一系列字符，一种数据类型，用括号括起来）

字符串就是**一系列字符**。在Python中，**用引号括起来的都是字符串**。

引号可以是**单引号**，也可以是**双引号**。

### 使用方法（title()、lower()、upper()）修改字符串（单词）的大小写

大小写处理方法：

* 全部大写：`name.upper()`
* 全部小写：`name.lower()`
* 首字母大写：`name.title()`

```python
name = "ada lovelace"
print(name.title())
```

方法：`title()`。title()以首字母大写的方式显示每个单词。（函数title()不需要额外的信息，因此它后面的括号是空的。）

**方法是Python可对数据执行的操作**。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。

在name.title()中，**name后面的.让Python对变量name执行方法title()指定的操作**。

### 拼接字符串（+）

Python使用+来合并字符串。这种合并字符串的方法称为拼接。

```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")
```

显示：Hello, Ada Lovelace!



### 使用制表符`\t`或换行符`\n`来添加空白

- 要在字符串中添加制表符（缩进），前面加`\t`。

- 要在字符串中添加换行符，前面加`\n`。

- 同时添加制表符和换行符，前面加`\n\t`。让Python换到下一行，并在下一行开头添加一个制表符。


```
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```



### 删除空白（方法rstrip()、lstrip()、strip()）

在实际程序中，这些**剥除函数**最常用于在存储用户输入前对齐进行清理。

Python能够找出字符串开头和末尾多余的空白。

- 方法`rstrip()`：要确保字符串**末尾**没有空白，可使用方法`rstrip()`。这种删除只是暂时的。

```
favorite_language = 'Python '
favorite_language.rstrip()
```

- 要永久删除这个字符串中的空白，**必须将删除操作的结果存回到变量中**：

```
favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
```

- 方法`lstrip()`：删除字符串**开头**的空白。
- 方法`strip()`：删除字符串**两端**的空白。

### 语法错误：单引号和双引号

```
message = "One of Python's strength is its diverse community."
print(message)
```

编写程序时，编辑器的**语法突出功能**可帮助你快速找出某些语法错误。

看到Python代码以普通句子的颜色显示，或者普通句子以Python代码的颜色显示时，就可能意味着文件中存在引号不匹配的情况。

### Python 2中的print语句

在Python 2中，无需将打印的内容放在括号内。



## 数字

### 整数（+、-、*、/、**）

- 加：+

- 减：-

- 乘：*

- 除：/

- 乘方运算：**


### 浮点数

Python将**带小数点的数字**都称为浮点数。

### 函数str()：将非字符串值表示为字符串

```
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)
```



## 列表[]

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引。

第一个索引是0，第二个索引是1，依此类推。

**Python有6个序列的内置类型，但最常见的是列表和元组。**

序列都可以进行的操作包括**索引，切片，加，乘，检查成员**。

此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

**列表的数据项不需要具有相同的类型**。

列表：存储成组的信息。

列表是新手可直接使用的最强大的Python功能之一，它融合了众多重要的编程概念。

列表由一系列按特定顺序排列的元素组成。为列表指定一个复数名称。

```
bicycles = ['trek', 'cannondale', 'redlines', 'specialized']
print(bicycles)
```

Python将打印列表的内部表示，包括方括号：

```
['trek', 'cannondale', 'redlines', 'specialized']
```



### 访问列表元素（print(bicycles[-1].title())）

- 第一个列表元素：索引为0，而不是1。
- 最后一个列表元素：索引为-1。方便在不知道列表长度的情况下访问最后的元素。
- 倒数第二个列表元素：-2。
- 倒数第三个列表元素：-3。

```
bicycles = ['trek', 'cannondale', 'redlines', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
```

返回

```python
trek #只返回该元素，而不包括方括号和引号
Trek
```

可以像使用其他**变量**一样使用列表中的各个值。

```
bicycles = ['trek', 'cannondale', 'redlines', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() +"."

print(message)
```

### 修改（bicycles[0] = 'A'）、添加（append()方法）和删除（del 语句）元素

随着程序的运行增删元素。

示例1：修改列表元素

```python
bicycles = ['trek', 'cannondale', 'redlines', 'specialized']
print(bicycles)

bicycles[0] = 'A'
print(bicycles)

-----------------------
['trek', 'cannondale', 'redlines', 'specialized']
['A', 'cannondale', 'redlines', 'specialized']
```

示例2：在列表中添加元素



## 用户输入（函数input()）

### 函数input()

**input()让程序暂停运行**，等待用户输入一些文本。

**获取用户输入后，Python将其存储在一个变量中**，以方便你使用。

使用函数input()时，**Python将用户输入解读为字符串**。

通过在提示末尾（冒号后面）包含一个**空格**，可**将提示与用户输入分开**，让用户清楚地知道其输入始于何处。

示例1：

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

------------------------------------------------------
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

1. 函数input()接受一个参数。
2. Python运行第一行代码时，用户将看到提示Tell me something, and I will repeat it back to you:。
3. **程序暂停运行，等待用户输入，并在用户按回车后继续运行**。
4. 输入存储在变量message中，接下来的print(message)将输入呈现给用户。



示例2：将提示存储在一个变量中，再将该变量传递给函数input()。

```
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?" 

name = input(prompt)
print("\nHello, " + name + "!")
```

该示例演示了一种创建多行字符串的方式：

* 第一行将消息的前半部分存储在变量prompt中
* 第二行运算符+=在存储在prompt中的字符串末尾加一个字符串。



示例3：

```python
print``(``'请在以下四个选项中【A.1;B.5;C.0;D.2】选出你的选项'``)
choice=input(``'请问你的选项是:'``)
if` `choice==``'A'``:
  ``print``(``'恭喜你，回答正确!!!'``)
else``:
  ``print``(``'很遗憾，回答错误!!!'``)
 
------------------------------------------------------
 
请在以下四个选项中【A.1;B.5;C.0;D.2】选出你的选项
请问你的选项是:A
恭喜你，回答正确!!!
```

### 函数int()来获取数值输入

使用函数input()时，**Python将用户输入解读为字符串**。

当你试图将输入用于数值比较时，Python会引发错误。因为它无法将字符串和整数进行比较：不能将存储在age中的字符串'21'与数值18进行比较。

**函数int()让Python将输入视为数值**，将**数字的字符串表示**转化为**数值表示**。

示例1：

```
age = input("How old are you? ")
How old are you? 21
age = int(age)
# 是否大于等于18
age >= 18 
True
```

示例2：

```
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
else: 
	print("\nYou'll be able to ride when you're a little older.")
```

### 求模运算符（%）

%：处理**数值**信息时，求模运算符%将两个数相除并**返回余数**。

求模运算符%不会指出一个数是另一个数的多少倍，而**只指出余数是多少**。

```python
4 % 3
5 % 3
--------------------
1 
2
```

如果一个数可被另一个数整除，余数就是0。因此将返回0。可利用这一点来判断一个数是奇数还是偶数。偶数都能被2整除。

even_or_odd.py

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + "is even.")
else:
    print("\nThe number " + str(number) + "is odd.")    
```



## while循环

while循环不断地运行，直到指定的条件不满足为止。

示例1：

```python
current_number = 1
while current_number <= 5:  # 只要小于等于5，就接着运行这个循环。一旦大于5，循环将停止，整个程序也将到此结束。
	print(current_number)
	current_number += 1
```

示例2：退出值。只要用户输入的不是这个值，程序就接着运行。

只要message的值不是'quit'，这个循环就会不断运行。

**特别注意：如果message是quit，循环会停止，但还会打印message。**

```python
#定义一条提示消息，告诉用户他有两个选择：要么输入一条消息，要么输入退出值（quit）。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program. "
#将变量的初始值设置为空字符串""，让Python首次执行while代码行时有可供检查的东西。
#必须给变量message指定一个初始值，让Python能够执行while循环所需的比较。
message = ""
while message != 'quit':
	message = input(prompt) #执行到此行代码，Python显示提示消息，并等待用户输入。
    print(message)
    
---------------------------
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
```

等到用户终于输入'quit'后，python停止执行while循环，而整个程序也到此结束。

示例3：不打印'quit'

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt) 
    
    if message != 'quit':#仅在消息不是退出值时才打印它
    	print(message)
    
---------------------------
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello.
Hello.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```





## 正则表达式（待整理）

## 函数

函数是**带名字的代码块**，用于完成具体的工作。

将函数存储在**被称为模块的独立文件**中，让**主程序文件**的组织更为有序。

### 函数定义和函数调用

```python
def greet_user():
    """"显示简单的问候语"""
    print("Hello")
    
greet_user()
```



#### 函数定义：def greet_user():

- **关键字def**：定义一个函数。函数定义，向Python指出了函数名，还可能在括号中指出函数为完成其任务需要什么样的信息。
- 函数名：greet_user()。它不需要任何信息就能完成其工作，因此括号内是空的。即便如此，括号内也必不可少。

- ()：函数为完成其任务需要什么样的信息。

- : 定义以冒号结尾。

- **函数体：所有缩进构成函数体**。

- 注释：文档字符串（docstring）：描述函数是做什么的。用三个引号括起，Python使用它们来生成有关程序中函数的文档。

- 代码行：print("Hello!")

#### 函数调用：函数名+（函数为完成其任务需要的信息）

要调用函数，可依次指定函数名以及用括号括起的必要信息。



### 传递实参

像函数传递实参的方式很多：

* 位置实参：顺序
* 关键字实参：传递给函数的**名称-值对**。直接在实参中将名称和值关联起来了。
* 默认值：使用默认值可简化函数的调用。还可清楚地指出函数的典型用法。实参关联到函数定义中的第一个形参。


注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。

positional arguments位置参数。



### 返回值

函数并非总是直接显示输出。相反，它可以处理一些数据，并返回一个或一组值。

**函数返回的值被称为返回值**。

在函数中，可**使用return语句**将值返回到调用函数的代码行。

返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

#### 返回简单值

可选值：让实参变成可选的，可有可无的

有时候需要让实参编程可选的，这样使用函数的人就只需在必要时才提供额外的信息。

给实参指定一个空字符串的默认值，并将其移到形参列表的末尾。在用户没有提供相应信息时，不使用这个参数。

#### 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

这个函数接受简单的文本信息，将其放在一个更合适的数据结构中。让你不仅能打印这些信息，还能以其他方式处理它们。

你可以轻松地扩展这个函数，使其接受可选值。

### 结合使用函数和while循环

### 将函数存储在模块中（import语句）

**模块：扩展名为.py的文件**，包含要导入到程序中的代码。

函数的优点：使用它们可将代码块与主程序分离。

将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。

**import语句**允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。

#### 导入整个模块（import module_name；module_name.function_name()）

语法：`import module_name`，则Python打开该模块文件，就可在程序中使用该模块中的所有函数。

使用其中任何一个函数：`module_name.function_name()`

#### 导入特定的函数（from module_name import function_name）

语法：`from module_name import function_name`

导入多个函数：`from module_name import function_0, function_1, function_2 `

#### 使用关键字as给函数指定别名（from module_name import function_name as fn）

关键字as将函数重命名为指定的别名。

语法：`from module_name import function_name as fn`

示例：`from pizza import make_pizza as mp`

#### 使用关键字as给模块指定别名（import module_name as mn）

通过给模块指定简短的别名，让你能够更轻松地调用模块中的函数。

语法：`import module_name as mn`

示例：`import pizza as p`

```python
import pizza as p

p.make_pizza(16, 'mushrooms')
```

#### 导入模块中的所有函数（*运算符）（from module_name import *）

使用*运算符可让python导入模块中的所有函数。**之后可通过名称来调用每个函数，而无需使用句点表示法**。

语法：`from module_name import *`

示例：`from pizza import *`

然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法。

最佳做法是：

* 只导入你需要使用的函数
* 导入整个模块并使用句点表示法

### 函数编写指南

* 应给函数指定描述性名称，且只在其中使用小写字母和下划线。给模块命名时也应遵循上述约定。
* 



## 方法

定义和用法

title() 方法返回一个字符串，其中每个单词的第一个字符均为大写。比如标题。

如果单词包含数字或符号，则其后的第一个字母将转换为大写字母。

语法：string.title()
