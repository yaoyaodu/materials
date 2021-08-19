# Pandoc格式转换

[利用pandoc将markdown转换为word文档 - kofyou - 博客园 (cnblogs.com)](https://www.cnblogs.com/kofyou/p/14932700.html)（详细，重点看）

[Pandoc 实用教程](https://blog.csdn.net/fenghuizhidao/article/details/107202497)

[(4条消息) Pandoc：一个超级强大的文档格式转换工具_Tony.Dong的专栏-CSDN博客_pandoc](https://tonydong.blog.csdn.net/article/details/108536784?utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-7.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-7.control)

[Pandoc - About pandoc](https://pandoc.org/)

==[使用pandoc批量转换文件格式_Tobato-CSDN博客](https://blog.csdn.net/tobato/article/details/84912915?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-4.control&spm=1001.2101.3001.4242)==

==[Python将md批量转为docx_zhaoolee的CSDN博客-CSDN博客](https://blog.csdn.net/zhuoyuedelan/article/details/104153312)==

==[在Windows中使用Pandoc批量转换文件 | 码农家园 (codenong.com)](https://www.codenong.com/27852067/)==

[Pandoc实现批量将md文件转换为其它文件 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/145787589)

[Windows下利用批处理批量调用pandoc转换文件](https://wngamebox.cn/669.html)

![image-20210818145906607](https://i.loli.net/2021/08/18/qQOtS1VEFnkryGe.png)



Pandoc是用于将文件从一种标记语言转换为另一种标记语言的命令行工具。 标记语言使用标签来注释文档的各个部分。 常用的标记语言包括Markdown，ReStructuredText，HTML，LaTex，ePub和Microsoft Word docx。

用简单的英语， Pandoc允许您将一堆文件从一种标记语言转换成另一种标记语言。 典型示例包括将Markdown文件转换为Word, PPT，LaTeX，PDF甚至是ePub。

pandoc是一个软件，是一个能把千奇百怪的文档格式互相转换的神器，是一把文档转换的瑞士军刀（swiss-army knife）。

pandoc官网：https://www.pandoc.org/

pandoc下载链接：https://github.com/jgm/pandoc/releases

pandoc安装：双击安装，打开命令行输入 pandoc -v 看是否安装成功

pandoc手册：https://www.pandoc.org/MANUAL.html





### ==合并多个markdown文件，自动生成目录==

参见：[利用pandoc将markdown转换为word文档 - kofyou - 博客园 (cnblogs.com)](https://www.cnblogs.com/kofyou/p/14932700.html)





## 安装Pandoc

通过 Pandoc 提供的安装包，下载链接见[github](https://github.com/jgm/pandoc/releases)。

## 命令行运行基本参数

- 使用参数`-f` `FORMAT`和`-t` `FORMAT`指定源和目标文件格式。**pandoc支持识别文档后缀，一般可以省略。**
- 使用参数`-o` `FILE`指定输出文件。

命令示例：pandoc filename.md -o filename.docx

## Markdown转Word

1. 打开**命令提示符**工具。
2. 输入`pandoc C:\Users\user\Desktop\文件名.md -o C:\Users\user\Desktop\输出文件名.docx`。

![image-20210818095750059](https://i.loli.net/2021/08/18/z1EyuFIkKTNsZOG.png)

## 导出 Word 文档设置

--toc 												# 生成目录

 --toc-depth=number  				# 生成的目录深度

 --wrap=auto|none|preserve 	# 文字换行方式 

--reference-doc=file 					# 指定输出模板

示例：`--reference-doc=C:\Users\user\Desktop\MarkdownToWordTemplate.docx`

示例：指定了输出模板、目录和目录层级。

pandoc C:\Users\user\Desktop\中文技术文档写作规范.md -o C:\Users\user\Desktop\中文技术文档写作规范.docx --reference-doc=C:\Users\user\Desktop\MarkdownToWordTemplate.docx --toc --toc-depth=1



（也可以将修改后的模板文件放置到 **Pandoc 的数据文件夹**下，并命名为 `reference.docx`，**后续 Pandoc 将把这个文件作为默认模板进行使用。**这里的数据文件夹，可以在 `pandoc -v` 指令的打印信息中，通过 `data-dir` 字段来获取。）

## 修改默认Word模板

1. 默认的 word 模板可以通过命令来查看：pandoc --print-default-data-file reference.docx > custom-reference.docx

2. 执行命令后，默认的模板（custom-reference.docx ）保存在当前目录下，你可以对各个文字样式、默认表格样式进行修改。

3. 如果要修改输出文件中的表格样式，直接给模板中的表格更换样式，不能达成效果。根据Github上的讨论得知，**必须修改名为Table的表格样式**。修改方法：

   1. 开始菜单—样式—右下方三角号—出现样式列表框。

   2. 点击最下方**管理样式**图标。弹出**管理样式**对话框。

   3. 编辑—Table（使用前隐藏）—修改。

      **说明：在样式列表框里找不到Table这个样式，是隐藏的。**



## 设置 metadata

metadata 是导出格式中的一些信息，例如作者、日期、简介等等，在 EPUB、**PDF、Word** 等格式中有一定作用。

- 在命令行中指定 metadata。

  -M KEY[=VAL], --metadata=KEY[:VAL] 		# 将 KEY 的内容设置为 VAL 

  --metadata-file=file 									 # 读取 file 中的内容作为 metadata

- 在文件中顶部对 metadata 进行声明，使用 YAML 语法。

  ---

  *# 该部分必须在文档的顶部* 

  *# 顶部和底部的 三个横线必须保留* 

  title: 标题 

  author: 

  `-作者 1` 

  `- 作者 2` 

  date: 日期 

  keywords: [关键词 1, 关键词 2] 

  abstract: |  

  ​     第一段   

  ​     第二段 

  ---



--metadata-file=C:\Users\user\Desktop\封面.md 不起作用



## Word转Markdown

1. 打开**命令提示符**工具。

2. 输入`pandoc C:\Users\user\Desktop\Datasheet.docx -o C:\Users\user\Desktop\Datasheet.md`。

问题：

- 格式会乱，目录，表格，封面
