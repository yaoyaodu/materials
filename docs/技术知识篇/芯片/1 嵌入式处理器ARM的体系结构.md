# 嵌入式处理器ARM的体系结构

## 6.3.1 概述

ARM是国际上广泛使用的一种嵌入式RSIC处理器核。1983.10—1985.4，在英国剑桥的Acron Computer公司开发了一种32位嵌入式RSIC处理器，命名为Acron RISC Machine（ARM），以后又将ARM的含义修改为**Advanced RISC Machine**，并于**1990成立了Advanced RISC Machine Limited（ARM公司）**，专门致力于**嵌入式RSIC处理器核的研发**。

30多年来，嵌入式RSIC处理器核ARM的体系结构在其发展过程中经历了多次修订，从1983年ARM体系结构的第一个版本—ARMv1，到2000年的ARMv6。表6-3给出了ARM体系结构的概况，ARMv3是ARM公司成为独立的公司后提出的第一个ARM体系结构。目前，ARM v3之前各种体系结构的处理器核已不再生产。

自1990年ARM公司成立以来，共开发了七个系列的ARM处理器产品，即：ARM7系列，ARM9系列，ARM9E系列，ARM10系列，ARM11系列，SecurCore系列和ARM Cortex系列。

此外，ARM公司与DEC公司合作开发了基于ARMv4的StrongARM（后为Intel公司所收购），授权Intel公司开发生产基于ARMv5TE体系结构的32位嵌入式RSIC处理器Xscal。

下文给出了ARM公司的发展历程，图6-11是各ARM处理器核的工作性能发展概况。

ARM开发了架构扩展，从而为Java加速（Jazelle）、安全性（TrustZone）、SIMD和高级SIMD（NEONTM）技术提供支持。ARMv8-A架构还增加了密码扩展作为可选功能。

表6-3 ARM体系结构一览表

<img src="https://i.loli.net/2021/09/08/VwIifQBlbConAJg.png" alt="image-20210908133951734" style="zoom:50%;" />



<img src="https://i.loli.net/2021/09/08/8COJhpKGUZfD1yA.png" alt="image-20210908134036490" style="zoom:50%;" />



图 6-11 ARM处理器的性能及工作速度发展概况

