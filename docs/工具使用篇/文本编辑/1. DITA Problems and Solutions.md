# DITA: Problems and Solutions

Problem:

Solution:



Problem: approve图片：图片和topic是平级的  需要单独approve

Solution:

1. 选中要修改图片的topic, 右击选择View dependencies  



Problem: **topic not licensed** 

Solution:

1. Windows-> Preferences -> oXygen XML Author -> Register

2. In the Standalone Server section, enter below details: 12346

3. Click OK, Apply and Apply and Close



Problem: **Result tab: URI has a fragment component** 

Solution: **change element**



DITA生成PDF：

先release掉，否则生成出来只有标题

右击release相关topic后，单击Generate output 

output format: PDF preview  Create

保存路径：**Network--Client--Users--ezduxya--desktop （以后默认就是这个）**





**Create Document Variants** 
DITA Map View: `<bookmeta>-<bookid>-<booknumber>-<option>` V1



**Ditaval view:** 

Window-Show view-Other-IXISOFT CCMS-General. 

选择Ditaval, 单击OK. 

右击Ditaval folder, 选择New Ditaval。出现Ditaval dialog。



链接到本文档其他topic: 

map中右击-**Oxygen Editor-Insert as XRef**



查看最近更新的文档：**new topic在哪个文档中**

Documents--Recent Documents:View dependencies



导出图片文件路径：

\\Client\C$\Users\ydu\Downloads



打开一个新的窗口同时编辑多个topic:

Window-New Window



Problem：上传全新文档的时候传不上去

Solution: **创建全新的DITA文档的时候删除两个部分：**

1. Right-click the sections `<booktitlealt>` and select **Remove from Map** to delete them.

   If you don't do this step, your bookmap will fail to get included in Eridoc, and hence it will fail to be fetched by the build.

2. Right click the empty `<chapter>` below the containerref and selet **Remove from Map**.



Problem: Upload error![Attachment](https://i.loli.net/2021/08/05/5kAZeXgyEJCfGF4.png)

Solution: 

If you look at the doc number in your error it added V5 and V7. This means you didn’t apply the ditaval correctly when you uploaded your DXP. 

You have to upload your bookmap and add a ditaval to it (once **a V5  DEL for the PCC** and once **a V7 DEL for the PCG library**). This makes sure you uploaded this new document with the correct profiles for the PCC and PCG library. 

Your final DXP output should be: 

- 51/221 02-AXB 250 05/8 -V5 
- 51/221 02-AXB 250 05/8 -V7



Problem: DITA设置

Solution: 

1. 密码更新后要把password这里改成最新的密码。(Preferences–CMS configuration)

2. Document base填CPI。

![Image](https://i.loli.net/2021/08/05/ASPOd7C1R8JihFL.jpg)



条件处理：属性，属性值，设定的处理规则。



**DITA本地编辑器： Oxygen XML Author 20.1**



**approve the development map后：**

open with Oxygen DITA Map Editor: **PA99**





DITA search设置：

- search文档的话选中Documents types: Maps
- Dynamic release management: 
  - click 最左边的图标：Add versions, 然后click Loading all products/libraries
  - PC common
    - PC common delivery
    - PC common development

- search result: 右击选中Primary version
  - update文档：PC common development
  - deliver文档：PC common delivery



![Capture](https://i.loli.net/2021/08/05/sFg5392P48LvCr6.png)



在DEV上新增topic: clone 

在DITA中新增topic：

1. dev 上approve后，search 新增的topic名称
2. 把delivery这个branch lock住，然后把新增的这个topic拖进来到相应的位置。
3. release掉generate output，然后选择最长的那个
4. 在Docmotive上发CCF
