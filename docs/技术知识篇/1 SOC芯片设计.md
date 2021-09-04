###### SoC系统芯片设计

系统芯片实现的两种基本途径：

* 半定制的高密度可编程逻辑器件（HDPLD）
* 全定制的专用集成电路（Application Specific Integrated Circuit专用集成电路）

ASIC即专用集成电路，是指应特定用户要求和特定电子系统的需要而设计、制造的[集成电路](https://baike.baidu.com/item/集成电路/108211)。 目前用[CPLD](https://baike.baidu.com/item/CPLD/2527470)（[复杂可编程逻辑器件](https://baike.baidu.com/item/复杂可编程逻辑器件/12583489)）和 [FPGA](https://baike.baidu.com/item/FPGA/935826)（现场可编程逻辑门阵列）来进行ASIC设计是最为流行的方式之一，它们的共性是都具有用户现场可编程特性，都支持[边界扫描](https://baike.baidu.com/item/边界扫描/1150543)技术，但两者在集成度、速度以及编程方式上具有各自的特点。



“从电路集成到系统集成”是对集成电路产品发展过程的最好总结，即整个集成电路产品的发展经历了从传统的板上系统（System on Board）到片上系统（System on Chip）的过程。

SoC设计技术始于20世纪90年代中期，随着半导体工艺技术的发展，IC设计者能够将愈来愈复杂的功能集成到单硅片上，SOC正是在集成电路向集成系统转变的大方向下产生的。

由于SoC可以充分利用已有的设计积累，显著



