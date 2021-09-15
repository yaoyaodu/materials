WDT 



本词条缺少**概述图**，补充相关内容使词条更完整，还能快速升级，赶紧来编辑吧！

WDT是英语Watchdog Timer的缩写字母，Watchdog Timer 中文名[看门狗](https://baike.baidu.com/item/看门狗/75814)，是一个[定时器](https://baike.baidu.com/item/定时器/5109454)电路。

- 中文名

  看门狗

- 外文名

  WatchDog Timer

- 简  称

  WDT

- 类  别

  一个定时器电路

- 输  入

  喂狗

- RST端

  输出到MCU

- 价  格

  4~10元不等.

- WDT芯片

  如MAX813,5045,IMP 813等

## 目录

1. 1 [WatchDog Timer看门狗](https://baike.baidu.com/item/WDT/5196641#1)
2. 2 [WDT气象决策技术](https://baike.baidu.com/item/WDT/5196641#2)

## WatchDog Timer看门狗

[编辑](javascript:;)[ 语音](javascript:;)

WDT是英语Watchdog Timer的缩写字母。

Watchdog Timer 中文名看门狗。是一个[定时器](https://baike.baidu.com/item/定时器/5109454)电路，一般有一个输入，叫[喂狗](https://baike.baidu.com/item/喂狗)，一个输出到MCU的RST端，MCU正常工作的时候，每隔一段时间输出一个信号到喂狗端，给 WDT 清零，如果超过规定的时间不喂狗，（一般在程序跑飞时），WDT 定时超过，就会给出一个[复位信号](https://baike.baidu.com/item/复位信号)到MCU，使MCU复位. 防止MCU死机. 看门狗的作用就是防止程序发生[死循环](https://baike.baidu.com/item/死循环/4141007)，或者说程序跑飞。

工作原理：在系统运行以后也就启动了看门狗的计数器，[看门狗](https://baike.baidu.com/item/看门狗/75814)就开始自动计数，如果到了一定的时间还不去清看门狗，那么看门狗计数器就会溢出从而引起看门狗中断，造成系统复位。所以在使用有[看门狗](https://baike.baidu.com/item/看门狗)的芯片时要注意清看门狗。

硬件看门狗是利用了一个[定时器](https://baike.baidu.com/item/定时器/5109454)，来监控主程序的运行，也就是说在主程序的运行过程中，我们要在定时时间到之前对定时器进行复位如果出现死循环，或者说PC指针不能回来。那么定时时间到后就会使[单片机](https://baike.baidu.com/item/单片机)复位。常用的WDT芯片如MAX813,5045,IMP 813等，价格4~10元不等.

软件[看门狗技术](https://baike.baidu.com/item/看门狗技术)的原理和这差不多，只不过是用软件的方法实现，我们还是以51系列来讲，我们知道在51单片机中有两个定时器，我们就可以用这两个定时器来对主程序的运行进行监控。我们可以对T0设定一定的定时时间，当产生定时中断的时候对一个变量进行赋值，而这个变量在主程序运行的开始已经有了一个初值，在这里我们要设定的定时值要小于主程序的运行时间，这样在主程序的尾部对变量的值进行判断，如果值发生了预期的变化，就说明T0中断正常，如果没有发生变化则使程序复位。对于T1我们用来监控主程序的运行，我们给T1设定一定的定时时间，在主程序中对其进行复位，如果不能在一定的时间里对其进行复位，T1 的定时中断就会使[单片机](https://baike.baidu.com/item/单片机)复位。在这里T1的定时时间要设的大于主程序的运行时间，给主程序留有一定的的裕量。而T1的中断正常与否我们再由T0定时中断子程序来监视。这样就够成了一个循环，T0监视T1，T1监视主程序，主程序又来监视T0，从而保证系统的稳定运行。

51 系列有专门的[看门狗定时器](https://baike.baidu.com/item/看门狗定时器)，对系统频率进行分频计数，[定时器](https://baike.baidu.com/item/定时器/5109454)溢出时，将引起复位.看门狗可设定溢出率，也可单独用来作为定时器使用.

看门狗使用注意：大多数51 系列单片机都有看门狗，当看门狗没有被定时清零时，将引起复位。这可防止程序跑飞。设计者必须清楚看门狗的溢出时间以决定在合适的时候，清看门狗。清看门狗也不能太过频繁否则会造成资源浪费。程序正常运行时，软件每隔一定的时间（小于定时器的溢出周期）给定时器置数，即可预防溢出中断而引起的误复位。

看门狗运用：看门狗是恢复系统的正常运行及有效的监视管理器（具有锁定光驱，锁定任何指定程序的作用，可用在家庭中防止小孩无节制地玩游戏、上网、看录像）等具有很好的应用价值.

系统软件"看门狗"的设计思路：

⒈[看门狗定时器](https://baike.baidu.com/item/看门狗定时器)T0的设置。在初始化程序块中设置T0的工作方式，并开启中断和计数功能。系统Fosc=12 MHz，T0为16位计数器，最大计数值为（2的16次方）-1=65 535，T0输入计数频率是．Fosc/12，溢出周期为（65 535+1）/1=65 536（μs）。

⒉计算主控程序循环一次的耗时。考虑系统各功能模块及其循环次数，本系统主控制程序的运行时间约为16．6 ms。系统设置"看门狗"[定时器](https://baike.baidu.com/item/定时器/5109454)T0定时30 ms(T0的初值为65 536-30 000=35 536）。主控程序的每次循环都将刷新T0的初值。如程序进入"[死循环](https://baike.baidu.com/item/死循环/4141007)"而T0的初值在30 ms内未被刷新，这时"看门狗"定时器T0将溢出并申请中断。

⒊设计T0溢出所对应的[中断服务程序](https://baike.baidu.com/item/中断服务程序)。此子程序只须一条指令，即在T0对应的[中断向量地址](https://baike.baidu.com/item/中断向量地址)(000BH）写入"[无条件转移](https://baike.baidu.com/item/无条件转移/3009236)"命令，把计算机拖回整个程序的第一行，对[单片机](https://baike.baidu.com/item/单片机)重新进行初始化并获得正确的执行顺序。

WDT例句及翻译

⒈**When&how to use watchdog(WDT)&constant ramp time for RAMP command?**

[看门狗](https://baike.baidu.com/item/看门狗)（WDT）、RAMP指令对固定斜率时间，何时以及如何使用？

⒉**In order to improve the reliability and ability of fault-tolerance of CX- 1micro-satellite,hardware fault-tolerance technology such as WDT,EDAC,multi-computer system etc**

根据小卫星[硬件冗余](https://baike.baidu.com/item/硬件冗余/12730199)结构的特点，采用了以多版本编程、恢复块技术、前向恢复和后向恢复技术等软件[容错技术](https://baike.baidu.com/item/容错技术)来提高现代小卫星系统的[容错能力](https://baike.baidu.com/item/容错能力/4357104)。

⒊**At the same time the clock chip PCF8563 and serial EEPROM chip CSI24C01 with Reset and WDT circuit of I2C bus are used hi the system. They have not only provided the non- volatility data storage area,the supervision ability of power supply and MCU and the RTC,and its I2C bus structure has been simplified the circuit design.**

同时在系统中还使用了护C[总线结构](https://baike.baidu.com/item/总线结构)的[时钟芯片](https://baike.baidu.com/item/时钟芯片)[PcF8563](https://baike.baidu.com/item/PcF8563/9535254)和内置[Reset](https://baike.baidu.com/item/Reset/8602402)、wDT电路的串行[EEPROM](https://baike.baidu.com/item/EEPROM/1690980)芯片CSI24COI，它们不仅提供了电源和[微控制器](https://baike.baidu.com/item/微控制器/6688343)的监控功能、不挥发性的数据存储区、[实时时钟](https://baike.baidu.com/item/实时时钟)，而且其护C总线结构简化了电路设计。