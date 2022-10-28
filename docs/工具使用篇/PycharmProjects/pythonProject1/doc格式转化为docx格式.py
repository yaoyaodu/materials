# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

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



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
