# Python爬虫

* 有道翻译API: http://fanyi.youdao.com/openapi?path=data-mode

* 现在这些数据服务都是要钱的（WangRun）：概述-Web服务 API | 高德地图API：https://lbs.amap.com/api/webservice/summary/
* ipython interactive python
* 建议你试下， jupyter notebook,非常好用

## 安装库和模块

1. 找到pip3.exe所在的文件夹，复制路径。
2. 按键盘上的Win+R, 输入cmd。
3. 输入 cd 和刚才的路径。
4. 输入pip3 install requests, 回车。
5. 输入pip3 install lxml, 回车。
6. 打开Python编译器，即IDLE (Python 3.6.5 Shell)，输入import requests和import lxml。

## XPath基本使用方法

XPath是一种用于在XML文档中查找数据的语言，它最初只用于XML文档的信息搜索，现在同样可以用于HTML文档的信息搜索。

XPath提供了非常简单的语法来匹配HTML文档中的元素。通过XPath几乎可以定位出HTML文档中所有的内容。

### XPath常用语法规则

1. 通过**HTML标签名**可以选取**此节点下的所有子节点**。
2. 通过“/”符号可以从当前节点选取**直接子节点**。
3. 通过“//”符号可以从当前节点选取**子孙节点**。
4. 通过“.”符号可以选取**当前节点**。
5. 通过“..”符号可以选取**当前节点的父节点**。
6. 通过“@”符号可以选取**属性**。

示例：//div[@class='username']

该XPath表示：从HTML文档中搜索出所有标签名为`<div>`且class属性值为username的节点。

### 获取XPath

1. 通过Chrome浏览器访问网站。
2. 右击鼠标选择“检查”，或点击浏览器右上角...，点击“更多工具—开发者工具”中的"Elements"标签页，选中需要过滤的HTML元素。
3. 右击，在弹出的快捷菜单中依次选择“复制—复制XPath"。
4. 获取XPath后，结合Selenium的find_element_by_xpath方法轻松定位网页中的元素。

## 浅析HTTP（超文本传输协议）

- HTTP: Hyper Text Transfer Protocol（超文本传输协议）
- HTTPS: Hyper Text Transfer Protocol over Secure Socket Layer（以完全为目标的HTTP）: HTTPS在HTTP之上提供了加密传输信息的功能，是HTTP的升级版。

HTTP是用于从Web服务器中**传输超文本信息**到本地浏览器的**传输协议**。

协议就是一种规范，只有当Web服务器和浏览器都遵循某种规范时，两者才能正常通信。

HTTP规定了信息传输过程中的格式，这样Web服务器与浏览器都可以按照规范去解析数据包中的内容，从而正常地处理其中的信息。

每个网站都要相应的网址：统一资源定位符（Uniform Resource Locator, URL）。

* 通过URL可以在互联网中找到相应的网站
* 通过HTTP或HTTPS来传输网站中的内容

## 浏览器与网站的交互过程

浏览器是如何通过URL获取网站中的信息的：

1. 浏览器向DNS（Domain Name System, 域名系统）服务器**获取URL对应的IP地址**。

   说明：URL本身是无法获取网站信息的，**只有网站对应的IP才可以获取网站信息**。

   URL是由域名与其他内容组成：示例：https://hack***.com/blog/2019/11/18/1.html

   - https: 使用的网络协议

   - hack***.com: 网站域名

   - blog/2019/11/18/1.html：网站中的资源路径

   通过URL获取IP的本质就是通过其中的域名获取网站的IP。

2. 浏览器与对应IP地址的Web服务器进行**TCP连接**。

   TCP：传输控制协议。

   在获取网站IP后，**通过IP就可以定位到Web服务器的具体位置**。随后**浏览器便通过TCP与Web服务器建立连接**。

   Web服务器就是一台计算机，只是该计算机运行着提供Web服务的程序。

3. TCP连接建立后，浏览器构建满足HTTP的数据包去请求Web服务器中的数据。

   * GET请求数据包
   * POST请求数据包

4. Web服务器在接收到请求后，根据请求数据包中的参数返回满足当前请求的数据。

5. 浏览器接收到Web服务器返回的数据后，将其渲染成页面供用户浏览。



## 抓取、分析、存储

Python学习网络爬虫主要分三个大的板块：

* **抓取**
* **分析**
* **存储**

当我们在浏览器中输入一个url后回车，这段过程发生了以下四个步骤：

* 查找**域名**对应的IP地址
* 向IP对应的**服务器**发送请求，服务器响应请求，发回网页内容
* 浏览器**解析**网页内容



## 示例

有道词典翻译【体验输入式翻页】

网址：[在线翻译_有道 (youdao.com)](https://fanyi.youdao.com/)

右击“检查”，选择“Network”/"网络"，选择"Fetch/XHR",点击“translate_o?smartresult”（其他都是图片），**Headers(标头)**显示以下信息：

* 请求 URL: `https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule`
* 请求方法：POST
* `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34`

