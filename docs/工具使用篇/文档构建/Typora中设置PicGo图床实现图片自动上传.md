# Typora 中设置PicGo 图床实现图片自动上传

来源：[Typora 中设置PicGo 图床实现图片自动上传 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/378892917)

**图床**一般是指**储存图片的服务器**，有国内和国外之分。国外的图床由于有空间距离等因素决定访问速度很慢影响图片显示速度。国内也分为单线空间、多线空间和cdn加速三种。

PicGo简单点说就是一个**图床上传工具**，我们主要就是借助这个软件进行上传。

下载地址：https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.0-beta.4。

在众多 md 编辑器中，Typora 是大家公认的体验较好的写作软件之一，它最大的特点就是：所见即所得，无须分屏预览，或者开启新页面预览。那么Typora 中能不能直接粘贴图片后，就自动上传到图床呢？下面就来介绍如何配置，以及 PicGo 的使用。实现图片的自动上传。

[Kogoal](https://link.zhihu.com/?target=http%3A//kogoal.com/)介绍了使用 SM.MS 这一种图床，其他图床的配置可以参考PicGo。

## **使用到的工具**

**`SM.MS`**: **免费**图床。

**`PicGo`** 开源的图片管理工具，可以自己上传图片到各种图床。

**`Typora`**: 写Markdown的神器，轻便简洁的Markdown编辑器，支持**即时渲染**技术。

安装步骤不分先后，建议按照上面顺序安装，因为存在token或者设置需要在后续的安装中用到。

## **1 注册SM.MS**

SM.MS 图床用户注册，注册网站：[https://sm.ms/](https://link.zhihu.com/?target=https%3A//sm.ms/)

免费的用户空间是5G,如果是土豪朋友可以选择premium 价格是399 USD



![img](https://pic4.zhimg.com/80/v2-7394dd1dd68b7eb2048eb84c6d3b4413_1440w.jpg)



新注册用户登录之后，点击左侧 API Token 点击 Generate Secret Token 然后复制保存，这个Secret Token 会在第二步PicGo中用到。



![img](https://pic4.zhimg.com/80/v2-14217baea54f13efa2e0a1ae5de6abbb_1440w.jpg)



## **2 安装配置 PicGo**

### **2.1 安装PicGo**

点击此处下载PicGo [应用](https://link.zhihu.com/?target=https%3A//github.com/Molunerfinn/PicGo/releases)[https://github.com/Molunerfinn/PicGo/releases](https://link.zhihu.com/?target=https%3A//github.com/Molunerfinn/PicGo/releases)

**Windows** Windows 用户请下载最新版本的 `exe` 文件。

**macOS** macOS 用户请下载最新版本的 `dmg` 文件。

**Linux** Linux 用户请下载 `AppImage` 文件。

一路next后，安装完成后如下。



![img](https://pic1.zhimg.com/80/v2-94118be84cb59d9f2eb00311b01b16f4_1440w.jpg)



### **2.2 配置PicGo**

### **设定token值**

此处的Token值就是在SM.MS 上生成的Secret Token。点击确定。



![img](https://pic1.zhimg.com/80/v2-72836bb9ebf9cdd5f8890aec57c26bb8_1440w.jpg)



### **2.3 安装插件**

再安装插件之前，确保你已经安装了 Node.js，因为 PicGo 是使用 npm 来安装的。地址：[https://nodejs.org/zh-cn](https://link.zhihu.com/?target=https%3A//nodejs.org/zh-cn)

到 PicGo-插件设置里面搜索一个插件：**picgo-plugin-smms-user**，点击安装。



![img](https://pic2.zhimg.com/80/v2-3495f468126a28712cfd970bb68eddd1_1440w.jpg)





## **3 安装配置Typora**

### **3.1 下载最新版本的 Typora**

下载地址：[https://www.typora.io/](https://link.zhihu.com/?target=https%3A//www.typora.io/)

### **3.2 设置图像上传**

根据个人喜好，我把 Typora 的语言设置为简体中文。



![img](https://pic3.zhimg.com/80/v2-58aa217dd6792bed040aec70739bcf2e_1440w.jpg)



Typora配置图床选项这里标注了三个红框：

- 第一默认不是 上传图片 选项，下拉选择它；
- 第二个红框建议两个都选择，这样你写作所用到的图片无论是本地上传还是网络图片，都会直接上传到你的图床；
- 第三个红框是图床工具，选择刚过安装的PicGo的安装目录。



![img](https://pic1.zhimg.com/80/v2-1b254b287d9b7a936ffe1081e254ada4_1440w.jpg)





点击**验证图片上传**选项，会自动上传一张测试图片，如果提示成功上传图片并获得新的URL。证明上传成功。



![img](https://pic3.zhimg.com/80/v2-88d2f6d22a7196f44dc32674f03b42fe_1440w.jpg)



## **Typora 中测试上传图片**

在markdown文件中需要使用图片的地方，右键选择上传图片。点击后即可上传图片至图床。如果仔细看markdown的图片路径，就会发现已经从本地的路径变成了网页的路径。到这里说明我们的图床工具上传图片已经没有问题了，现在就可以在 Typora 中安心的码字了。

![img](https://pic1.zhimg.com/80/v2-533b51cf336cd4c33316f7aea0eea1fc_1440w.jpg)

