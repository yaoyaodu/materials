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

## 读写Word文档

安装：pip3 install python-docx

Word文档有两种不同的文件格式。python-docx只支持操作*.docx文件格式。

* 2003版或更早之前的版本使用*.doc文件格式。
* 2007版及之后的版本使用*.docx文件格式。
  * *.docx格式基于XML（Extensible Markup Language，可扩展标记语言）。在相同数据量下，其占用空间更小，兼容性更高。

### 新建Word文档

1. 新建文档。

2. 保存文档。

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
doc_path = 'D:/exist.doc'
docx_path = 'D:/exist.doc'

#获取Word应用程序
Word = client.Dispatch('Word.Application')

#打开Word文档
doc = Word.Documents.Open(doc_path)


```



