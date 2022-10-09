安装库和模块：

1. 找到pip3.exe所在的文件夹，复制路径。
2. 按键盘上的Win+R, 输入cmd。
3. 输入 cd 和刚才的路径。
4. 输入pip3 install requests, 回车。
5. 输入pip3 install lxml, 回车。
6. 打开Python编译器，即IDLE (Python 3.6.5 Shell)，输入import requests和import lxml。

Python学习网络爬虫主要分三个大的板块：

* **抓取**
* **分析**
* **存储**

当我们在浏览器中输入一个url后回车，这段过程发生了以下四个步骤：

* 查找域名对应的IP地址
* 向IP对应的服务器发送请求，服务器响应请求，发回网页内容
* 浏览器**解析**网页内容





有道词典翻译【体验输入式翻页】

网址：[在线翻译_有道 (youdao.com)](https://fanyi.youdao.com/)

右击“检查”，选择“Network”/"网络"，选择"Fetch/XHR",点击“translate_o?smartresult”（其他都是图片），**Headers(标头)**显示以下信息：

* 请求 URL: `https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule`
* 请求方法：POST
* `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34`

