# 操作步骤    

操作步骤的写作对于写好任务型主题（task topic）极为重要，在此单列出来重点进行说明。

## 概述

步骤用于描述完成一个任务必须遵循的操作过程。

## 要求

* 每个步骤必须含有明确的操作动作。一个步骤，仅包含一个独立的动作或一个命令。对于连贯的动作，可以作为一个步骤，主要是指以下三种情况：

  情况一： “右击**××**，选择快捷菜单［**××**→**××**］”。 

  情况二：“单击××按钮，在弹出的××提示框中单击××按钮”。

  情况三：“在××对话框中，输入如下表所示的参数”。

* 操作步骤中的界面截图，旨在介绍复杂的配置项或者配置举例。对于路径选择、菜单选择、简单的提示信息框、用户确认对话框、信息量较少的截图，在步骤描述中不需要截图。对于配置界面图，尽可能截取有配置数据的图示。

*   类似的步骤使用类似的语法、语句描述。

* 使用短语、单句进行描述。

* 对于任务中仅有一个步骤时，使用有序列表方式。

* 对于非必需的步骤，在步骤前增加“（可选）”字样，如下图所示。

  ![img](https://i.loli.net/2021/08/15/JnvYKI5TuyDpqA8.jpg)

<center>图1-6 非必需步骤</center>


* 步骤的动作描述（cmd标签）简洁清晰，仅含有动作或命令、简短的目的或结果。通常不含有对参数的说明和对步骤辅助性的说明。注意，上一个步骤的结果不要放在下一个步骤中。

  * 对于参数的设置说明和解释，通过Info标签中的正式表或者ul进行分别说明，如图1-7所示。

  * 对于步骤的辅助性说明，通过Info标签中的Note（说明）标签进行说明，如图1-8和图 1-9所示。

    
    
    ![img](https://i.loli.net/2021/08/15/kGNBeVILv6uwPic.jpg)

<center>图1-7 步骤中的参数说明</center>

​				![img](Step.assets\clip_image002-16290276767561.jpg)

<center>图 1-8 步骤中的相关说明实例1</center>

​			![img](Step.assets\clip_image002-16290277223012.jpg)

<center>图 1-9 步骤中的相关说明实例2</center>

## 分类

步骤分为以下5类，应用于Task Topic的步骤分为：

- 固定顺序步骤
- 可选步骤
- 分支步骤 
- 子步骤
- 跳转步骤

固定顺序步骤和可选步骤、分支步骤、子步骤主要应用于Task Topic中。

跳转步骤主要应用于描述单个告警或失败码的处理、某类故障处理的Topic中。

说明:

为了使步骤逻辑关系简单、流畅，在一个步骤中，可选步骤、分支步骤、子步骤和跳转步骤不建议混合使用。

### 1.1.1         固定顺序步骤

固定顺序步骤是需要严格按照顺序执行的步骤，一个步骤一个动作。

### 1.1.2         可选步骤

#### 定义

可选步骤是为了达到某个目的可采取的多种步骤。

#### 实现方式

可选步骤的采用step内插入info标签，在info标签中使用ul标签的方式，如下图所示。

![img](Step.assets\clip_image002.jpg)

<center>图1-11 可选步骤</center>

#### 规范用语

选择下列任一方式打开**××**界面：

*   选择菜单［××→××］。

*   在工具栏中单击![img](https://i.loli.net/2021/08/15/643NAgIUiLJqOMV.jpg)按钮。

*   按××键。

### 1.1.3         分支步骤

#### 定义

分支步骤是指对于不同的目的或者情况，进行不同的操作。

#### 实现方式

分支步骤采用在step内插入Choicetable标签的方式，如下图所示。

![img](Step.assets\clip_image002-16290264931151.jpg)

<center>图 1-12 分支步骤</center>

#### 举例

表 1‑1 分支步骤实例1

| 如果…                                | 那么…                                                        |
| ------------------------------------ | ------------------------------------------------------------ |
| 需要将文件中的图像插入到Word文档中   | 在Word文档中，将光标停留在需要插入图像的位置，通过下列步骤插入图像：   <br>1．选择菜单［插入→图片→来自文件］。   <br>2．选择需要插入的图片文件，单击**插入**按钮。 |
| 需要将剪贴板中的图像插入到Word文档中 | 在Word文档中，将光标停留在需要插入图像的位置，通过下列方式插入图像：   <br><ul><li>选择菜单［编辑→粘贴］。 </li><br><li>按Ctrl+V键。</li>   <br><li>单击右键，选择快捷菜单［粘贴］。</li></ul> |

表 1‑2 分支步骤实例2

| 如果…        | 那么…                                                        |
| ------------ | ------------------------------------------------------------ |
| BSC ID未配置 | 1. 选中自动配置BSC ID前的复选框。 <br>2. 单击确定按钮。   <br>3. 单击下一步按钮。 |
| BSC ID已配置 | 单击下一步按钮。                                             |

### 1.1.4         子步骤

#### 实现方式

子步骤采用在step内插入Substeps标签的方式。

#### 规范用语

1. 进入××界面。

   （1）    在××输入框中输入××。

   （2）  在××下拉列表框中选择××。

   （3）  在××下拉列表框中选择××。

### 1.1.5         跳转步骤

#### 定义

跳转步骤是指实际步骤与描述步骤次序不一致时出现的跳转，主要出现在告警处理、失败项处理的相关步骤中。

#### 实现方式

跳转步骤采用在步骤中的info标签下，进行选择跳转的方式。选择项采用“是”和“否”。

中文跳转步骤示例如下：

![img](Step.assets\clip_image002-16290265979972.jpg)

英文跳转步骤示例如下：

![img](Step.assets\clip_image002-16290266235223.jpg)

