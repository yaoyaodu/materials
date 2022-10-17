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

### 1 读取Word所有内容

```python
from docx import Document
文件 = Document('D:\Python_Test\zh1.docx')
for 段落 in 文件.paragraphs:
	print(段落.text)
```

### 2 读取一级标题、二级标题或正文

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
for 段落 in 文件.paragraphs:
	if 段落.style.name == 'Heading 1':   #读取二级标题，则改为Heading 2；读取正文，则改成Normal
		print(段落.text)    
        
# D:\Python_Test\NDA.docx 用\会报错，改成D:/Python_Test/NDA.docx就没问题
```

### 3 读取所有标题（使用正则表达式）

```python
from docx import Document
import re
文件 = Document('D:/Python_Test/NDA.docx')
for 段落 in 文件.paragraphs:
	if re.match("^Heading \d+$",段落.style.name):
		print(段落.text)
```

### 4 读取文档中用到的样式名称

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

### 1 添加标题

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_heading("我是新增的一级标题",level=1)
文件.save('D:/Python_Test/NDA.docx')

#标题默认是加到了版权页的后面，怎么解决呢？
#标题的样式是对的。
```

### 2 添加正文

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_paragraph("我是正文1234567")
文件.save('D:/Python_Test/NDA.docx')
```

### 3 添加分页符

```python
from docx import Document
文件 = Document('D:/Python_Test/NDA.docx')
文件.add_page_break()
文件.save('D:/Python_Test/NDA.docx')
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

p3 = doc.add_paragraph('新段落')

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















