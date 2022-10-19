# Python办公自动化之Word篇

在命令行输入pip3 list，会显示所有已经安装的库

```python
from docx import Document  #导入Document文档对象
from docx.enum.text import WD_ALIGN_PARAGRAPH #设置对象居中、对齐等
from docx.enum.text import WD_TAB_ALIGNMENT,WD_TAB_LEADER #设置制表符等
from docx.shared import Inches #设置图像大小
from docx.shared import Pt #设置像素、缩进等
from docx.shared import RGBColor #设置字体颜色
from docx.shared import Length #设置宽度
```



```python
from docx import Document

文件 = Document('D:\Python_Test\zh1.docx')
# print(文件.paragraphs)
print(文件.paragraphs[0:2])
for i in 文件.paragraphs[0:2]:
    print(i)
```



搜索XXX出现的次数

```python
from docx import Document
文件 = Document('D:\Python_Test\zh1.docx')
计数 = 0
for 段落 in 文件.paragraphs:
	if '芯片' in 段落.text:
		计数 += 1
print(计数)


##统计出来的数字和Word统计出来的数字不一样呢？？？
```

## 读取

### 1 读取Word所有内容（段落.text）

```python
from docx import Document
文件 = Document('D:\Python_Test\zh1.docx')
for 段落 in 文件.paragraphs:
	print(段落.text)
```

### 2 读取一级标题、二级标题或正文（if 段落.style.name == 'Heading 1/Normal'）

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
for 段落 in 文件.paragraphs:
	if 段落.style.name == 'Heading 1':   #读取二级标题，则改为Heading 2；读取正文，则改成Normal
		print(段落.text)    
        
# D:\Python_Test\NDA.docx 用\会报错，改成D:/Python_Test/NDA.docx就没问题
```

### 3 读取所有标题（使用正则表达式）(if re.match("^Heading \d+$",段落.style.name))

```python
from docx import Document
import re
文件 = Document('D:/Python_Test/NDA.docx')
for 段落 in 文件.paragraphs:
	if re.match("^Heading \d+$",段落.style.name):
		print(段落.text)
```

### 4 读取文档中用到的样式名称(if i.type==WD_STYLE_TYPE.PARAGRAPH)

```python
from docx.enum.style import WD_STYLE_TYPE
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
样式 = 文件.styles
for i in 样式:
	if i.type==WD_STYLE_TYPE.PARAGRAPH:
		print(i.name)
```

## 写入

### 1 添加标题(文件.add_heading)

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_heading("我是新增的一级标题",level=1)
文件.save('D:/Python_Test/NDA.docx')

#标题默认是加到了版权页的后面，怎么解决呢？
#标题的样式是对的。
```

### 2 添加正文(文件.add_paragraph)

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_paragraph("我是正文1234567")
文件.save('D:/Python_Test/NDA.docx')

#默认是加在文档最后。前面有空白页，也不会加到空白页中。加到文档最后一页。
```

### 3 添加分页符(文件.add_page_break)

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_page_break()
文件.save('D:/Python_Test/NDA.docx')

#默认是加在文档最后
```

### 4 添加文字块

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
a = 文件.add_paragraph('我是正文在我后面添加的文字会被设置格式：')      #''里面可以为空字符串
a.add_run('加粗').bold = True
a.add_run('普通')
a.add_run('斜体').italic = True
文件.save('D:/Python_Test/NDA.docx')

#默认是加在文档最后
```

## 段落的定位

```python
from docx import Document
文件 = Document('D:/Python_Test/zh1.docx')
print(len(文件.paragraphs))
# 段落很多的话，怎么快速找到段落的index呢？？？？
段落 = 文件.paragraphs[19]
# print(段落.text)
# 将段落.text赋新值，达到修改段落的目的
段落.text = "直到20世纪70年代，硅谷都是这场革命的中心，因为它们结合了科学知识、制造技术和有远见的商业思维。后面的删除"
文件.save('D:/Python_Test/zh1.docx')

# 问题：段落很多的话，怎么快速找到段落的index呢？？？？
```

## 指定段落处添加段落

通过选择段落，获取段落的对象，可以使用insert_paragraph_before()函数进行设置，其参数同add_paragraph()。

```python
from docx import Document
文件 = Document('D:/Python_Test/zh1.docx')
第二个段落 = 文件.paragraphs[1] # 获取第二个段落
第二个段落.insert_paragraph_before('这是添加的新的第二个段落')# 在第二个段落处插入
文件.save('D:/Python_Test/zh1.docx')

#添加新段落后，段落默认居中。这个问题怎么解决呢？
```

## 文字样式调整

对文字字体样式进行修改：run.font.样式= xxx

```python
from docx import Document
from docx.shared import Pt, RGBColor              # 字号，颜色
from docx.oxml.ns import qn                       # 中文字体

文件 = Document('D:/Python_Test/zh1.docx')
for 段落 in 文件.paragraphs:
	for 块 in 段落.runs:
		块.font.bold = True # 加粗
		块.font.italic = True # 斜体
		块.font.underline = True # 下划线
		块.font.strike = True # 删除线
		块.font.shadow = True # 阴影
		块.font.size = Pt(12)
		块.font.color.rgb = RGBColor(255,0,0)# 颜色
		块.font.name = 'Arial' # 英文字体设置
		块._element.rPr.rFonts.set(qn('w:eastAsia'),'思源黑体 CN Normal')   # 设置中文字体：微软雅黑
文件.save('D:/Python_Test/zh1.docx')
#只要文本设置了格式，直接打印段落.text就会显示为空是吗
```

## 修改正文字体

文件.styles['Normal'] ：文件样式中的正文。

```python
from docx import Document
from docx.oxml.ns import qn # 中文字体
文件 = Document('D:/Python_Test/zh2.docx')
文件.styles['Normal'].font.name = 'Arial'# 设置英文字体
文件.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '思源黑体 CN Normal')  #设置中文字体
文件.save('D:/Python_Test/zh2.docx')


#有格式的话不管用？要用run?
```

有格式的正文：不生效！！！！

```python
from docx import Document
from docx.shared import Pt, RGBColor              # 字号，颜色
from docx.oxml.ns import qn                       # 中文字体

文件 = Document('D:/Python_Test/zh1.docx')
for 段落 in 文件.paragraphs:
	for 块 in 段落.runs:
        if 块.style.name == 'Normal': 
			块.font.name = 'Arial' # 英文字体设置
			块._element.rPr.rFonts.set(qn('w:eastAsia'),'思源黑体 CN Normal')   # 设置中文字体：微软雅黑
文件.save('D:/Python_Test/zh1.docx')
```

## 修改标题字体

```python
from docx import Document
from docx.oxml.ns import qn # 中文字体
文件 = Document('D:/Python_Test/zh2.docx')
文件.styles['Heading 1'].font.name = 'Arial'# 设置英文字体
文件.styles['Heading 1']._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  #设置中文字体
文件.save('D:/Python_Test/zh2.docx')

#问题：一级标题能修改成功，二级标题修改不成功？三级标题也能修改成功。
#解决方案：默认标题2是“宋体（中文标题）”，这个字体的话修改不成功。改成“宋体”就能修改成功。
```



## 段落样式修改

paragraph.alignment = 对齐方式

```python
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx import Document
文件 = Document('D:/Python_Test/zh2.docx')
for 段落 in 文件.paragraphs:
	if 段落.style.name=='Normal':
		段落.alignment = WD_ALIGN_PARAGRAPH.CENTER
文件.save('D:/Python_Test/zh2.docx')
```



## 读写Word文档

From书(《Python办公自动化》)

安装：pip3 install python-docx

Word文档有两种不同的文件格式。python-docx只支持操作*.docx文件格式。

* 2003版或更早之前的版本使用*.doc文件格式。
* 2007版及之后的版本使用*.docx文件格式。
  * *.docx格式基于XML（Extensible Markup Language，可扩展标记语言）。在相同数据量下，其占用空间更小，兼容性更高。

### 新建Word文档

1. 新建文档。filename = Document()

2. 指定路径来保存文档。

```python
#导入Document文档对象
from docx import Document   
#1 新建文档
filename = Document()
#2 保存文档
filename.save('D:/filename.docx')
```

### .doc转化为.docx

安装：pip3 install pypiwin32

就像平时另存为一样：

1. 文件的路径。
2. 获取Word应用程序。

3. 打开文档。
4. 另存为其他格式。

```python
#通过win32com使用pypiwin32第三方库
from win32com import client

#*.doc文件的路径
doc_path = 'D:/filename.doc'
docx_path = 'D:/filename_new.docx'

#获取Word应用程序
Word = client.Dispatch('Word.Application')

#打开Word文档
doc = Word.Documents.Open(doc_path)

#另存为*.docx格式，参数12表示*.docx格式
doc.SaveAs(docx_path, 12)

#关闭原来的Word文档
doc.Close()

#退出Word软件
Word.Quit()
```

### 读取段落

```python
#导入Document文档对象
from docx import Document   

#利用Document方法获取Word文档对象
doc = Document('D:/filename.docx')

#遍历Word文档中的段落
for p in doc.paragraphs:
    print(p.text)

```

### 写入

### (doc.add_paragraph、p2.insert_paragraph_before)

```python
from docx import Document 
doc = Document()
#添加标题。标题的等级通过level参数指定
doc.add_heading('一级标题', level=1)
#添加段落
p2 = doc.add_paragraph('第二个段落')
#将新段落添加到已有段落之前
p1 = p2.insert_paragraph_before('第一个段落')

p3 = doc.add_paragraph('新段落')    #''里面可以为空字符串

#追加内容
p3.add_run('加粗').bold = True
p3.add_run('以及')
p3.add_run('斜体').italic = True

doc.save('D:/Friday.docx')
```



### 读取表格

```python
from docx import Document   

doc = Document('D:/filename.docx')

#获取Word文档中的所有表格
tables = doc.tables
#选择第一个表格
table = tables[0]

values = []

#遍历表格中的每一行
for row in table.rows
	#遍历每一行中的单元格
    for cell in row.cells:
        #将单元格中的内容添加到list中
        values.append(cell.text)
    value = ''.join(values)
    print(value)
    values = []
```

主流编程语言

| 语言名称     | 主要场景                          |
| ------------ | --------------------------------- |
| Javascript   | Web开发、动态脚本、客户端和服务端 |
| Java         | 企业应用                          |
| Bash/Shell   | 自动化和系统管理                  |
| Python       | 通用                              |
| PHP          | Web开发、服务端                   |
| C            | 通用、底层开发语言                |
| C++          | 通用                              |
| Ruby         | Web开发                           |
| R            | 统计计算                          |
| Objective  C | 通用                              |



### 使用Word模板文件

pip3 install docx-mailmerge

```python
from mailmerge import MailMerge
template = 'D:/入职证明.docx'
doc = MailMerge(template)

#将内容添加到Word模板中，参数名与Word模板中的域名相同
doc.merge(name='瑶瑶',
          id='451',
          year='2020'
          month='9',
          department_name='平台技术部',
          job_name='高级工程师')

doc.write('D:/入职证明_new.docx')

```



### 快速生成千份劳动合同

1. 将合同文件转为Word模板文件，将要填写信息的位置转为域。注意域只能使用英文命名。
2. 从Excel文件中读取姓名并生成1000份合同。















