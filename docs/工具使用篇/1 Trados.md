[toc]

[SDL Trados Studio 2017 进阶应用01-单文件翻译 - 简书 (jianshu.com)](https://www.jianshu.com/p/9c5e4fae9bca)

[SDL Trados Studio 使用技巧 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/345210165)

[Trados 中文网](https://www.trados.com.cn/portal.php)

[Trados: Trados Studio 翻译软件之母 (sdltrados.cn)](https://www.sdltrados.cn/cn/)



# Trados

来源：[小白教程贴（二）| 你和专业翻译还差一个Trados - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/30256269)

Trados取自三个英语单词Translation、documentation和Software，中文名“塔多思”。是桌面级计算机辅助翻译软件，基于**翻译记忆库和术语库**技术，为快速创建、编辑和审校高质量翻译提供了一套集成的工具。其支持57种语言的双向互译，并完美兼容所有流行文档格式，无需重新排版，堪称译者一大利器。

Trados作为计算机辅助翻译软件，强调的还是“辅助”功能，就是**把做过的工作都记录下来，放到两个主要的数据库中，一个是翻译记忆库，另一个是术语库**。等到再次工作的时候，只要是曾经翻译过的东西，Trados就会调用记忆库和术语库来提醒你、帮助你，甚至直接替你翻译。省去了重复劳动和排版时间，从而提高了翻译效率。



## SDL Trados Multiterm

1. 通过SDL Multiterm Converter插件将包含术语的excel文件转换为xml格式。

2. 将转换好的xml文件中的术语导入到Multiterm已有的术语库中。

   左侧**术语**—术语库—选中某个术语库—右击—导入术语库—导入文件—选择转换好的**xml文件**—排除文件区域点击**另存为**—设置文件名—下一步



## SDL Trados Studio

### 选择术语库

项目设置—术语库—使用—基于文件的Multiterm术语库—选择需要的术语库

右下角点击**确定**。

### 生成译文

菜单栏点击**文件**，选择**译文另存为**。



### **1、“欢迎”一栏为AppStore应用程序**

该栏目中主要展示了经SDL Trados Studio授权的嵌入式应用。例如批处理查找和替换、剪切板、格式转换等。主要是提供一些扩展性服务，一者君觉得在学习软件之初，大家无需专门研究。

### **2、菜单栏目**

○ 对齐文档

对齐指的是将双语文档做成每句话一一对应的形式，生成翻译记忆库，就是制作平行语料库的功能。但业界普遍觉得SDL Trados 2015中的对齐功能灰常不好用，于是纷纷下载Trados 2007版的Winalign使用。为何不尝试Tmxmall在线对齐呢？无需支付任何费用，而且又不用像Winalign去设置断句规则、自己去一 一连线。只需两步，对齐文档嗖嗖嗖就生成了~ 具体操作一者君会在后续另开新帖教大家哦~

○ 术语管理

刚到手的Trados软件就像一张白纸，而翻译记忆库和术语库才是其灵魂所在。术语，包括但不限于专业术语，还有一些普通短语，例如see you again，为了方便下次输入，也可以放进术语库里。Trados将术语管理单独开发成SDL MultiTerm。



**Trados最重要的就是记忆库。学会构建、加载翻译记忆库才是攻克软件的关键。**这过程就好似先建立起一个大仓库（空语料库），在仓库里尽可能多的摆满琳琅满目的优质商品（语料），在有顾客（待翻译文档）光顾的时候，只需从仓库中调取商品匹配即可。