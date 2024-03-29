# reST语法整理

资料：[reStructuredText入门 — Sphinx 1.2 documentation (pythondoc.com)](http://www.pythondoc.com/sphinx/rest.html)

rst转PDF：工具rst2pdf [rst2pdf | Use a text editor. Make a PDF](https://rst2pdf.org/)

## 数学公式

### 表格

源码：

* 第一个表格：grid
* 第二个表格：auto

![image-20220719112229623](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719112229623.png)

生成效果：

* 第一个表格：grid
* 第二个表格：auto

![image-20220719112324342](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719112324342.png)

源码：设置width: 1.0 （属性里面写的是整个表格的宽度，好像没什么作用，和只设置auto效果一样。是不是对内容少的表格有效？）

![image-20220719154319503](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719154319503.png)

生成效果：

![image-20220719154743614](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719154743614.png)

源码：

![image-20220719155900484](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719155900484.png)



生成效果：

![image-20220719155642904](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719155642904.png)



#### 表格双竖线

单竖线是自动换行不固定。双竖线是所见即所得。

![双竖线](C:\Users\杜瑶瑶\Desktop\新建文件夹\双竖线.png)

#### 表格里面表示矩阵

英伟达文档矩阵格式供参考：

![image-20220719103946697](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719103946697.png)

源码：表格里面math 后面的公式只能在一行才可以。

* 第一个表格：设置列宽的表格。注意列宽要比单元格内容的最长字符数大一些，这样更保险些。
* 第二个表格：未设置列宽。生成出来的PDF中表格默认是居中显示的。

   注意：如果是多个矩阵的话可以参考第一个表格来设置列宽，不然生成出来是居中的不太好看。

![image-20220719101619619](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719101619619.png)

生成的PDF：

* 第一个表格：有设置列宽。
* 第二个表格：未设置列宽，会居中显示。

![image-20220719101802127](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719101802127.png)

查看字符数：

* 选中单元格内容，在最下面信息栏一栏可以看到字符数。设置列宽的时候要比最长字符数大一些。

![最长的字符数](C:\Users\杜瑶瑶\Desktop\新建文件夹\最长的字符数.png)



反向生成：

html 反向生成出来的样子。反向出来math是多行的，多行显示不了。表格里面math 后面的公式只能在一行才可以

![image-20220719103040087](C:\Users\杜瑶瑶\AppData\Roaming\Typora\typora-user-images\image-20220719103040087.png)



## 代码块过长问题

rest 解决代码过长问题的脚本。

其实比较粗糙，而且我们的定位单行的方式可能不一样。就是读出开之后往里面插入字符。而且我定位的是我们自己的函数，所以还是比较好处理的。



## 两万个无序列表没有缩进问题

这是个 shell 脚本，还要安装个 rst2pdf，最好是用 pip 安装这个工具。要安装了rst2pdf   才能用这个脚本，他要靠rst2pdf来找哪一行需要再开头加缩进。

```shell
#/bin/bash

filename=mc_thrust.rst

rst2pdf ${filename} > r.txt 2>&1

sed -i "s/${filename}:/sed -i '/g" r.txt
sed -i "s/: (WARNING\/2) Bullet list ends without a blank line; unexpected unindent./ s\/\^\/   \&\/g' ${filename}/g" r.txt

sh r.txt

rm r.txt
```

多跑两遍，等rst2pdf不报错了就都换好了，我那堆问题是跑了8次，一共换了快2w个。
