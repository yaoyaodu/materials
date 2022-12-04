from docx import Document
文件 = Document('D:\Python_Test\zh1.docx')
计数 = 0
for 段落 in 文件.paragraphs:
	if '芯片' in 段落.text:
		计数 += 1
print(计数)