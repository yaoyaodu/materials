# RISC-V

**RISC-V**（发音为“risk-five”）是一个基于[精简指令集](https://baike.baidu.com/item/精简指令集)（RISC）原则的[开源](https://baike.baidu.com/item/开源)[指令集架构](https://baike.baidu.com/item/指令集架构)（ISA）。

与大多数指令集相比，RISC-V指令集可以自由地用于任何目的，允许任何人[设计](https://baike.baidu.com/item/设计)、制造和销售RISC-V[芯片](https://baike.baidu.com/item/芯片)和[软件](https://baike.baidu.com/item/软件)。虽然这不是第一个开源指令集，但它具有重要意义，因为其设计使其适用于现代计算设备（如仓库规模[云计算机](https://baike.baidu.com/item/云计算机)、高端[移动电话](https://baike.baidu.com/item/移动电话)和微小[嵌入式系统](https://baike.baidu.com/item/嵌入式系统)）。设计者考虑到了这些用途中的性能与功率效率。该指令集还具有众多支持的软件，这解决了新指令集通常的弱点。

该项目2010年始于[加州大学伯克利分校](https://baike.baidu.com/item/加州大学伯克利分校)，但许多贡献者是该大学以外的志愿者和行业工作者。

RISC-V指令集的设计考虑了小型、快速、低功耗的现实情况来实做，但并没有对特定的[微架构](https://baike.baidu.com/item/微架构)做过度的设计。

截至2017年5月，RISC-V已经确立了版本2.22的用户空间的指令集(userspace ISA)，而特权指令集(privileged ISA)也处在草案版本1.10。

- 中文名

  RISC-V指令集

- 外文名

  RISC-V instruction set architecture

- 属  性

  指令集架构

- 作  者

  [加利福尼亚大学伯克利分校](https://baike.baidu.com/item/加利福尼亚大学伯克利分校/854061)

- 基  准

  [精简指令集](https://baike.baidu.com/item/精简指令集)

- 应用领域

  仓库规模[云计算机](https://baike.baidu.com/item/云计算机)、高端[移动电话](https://baike.baidu.com/item/移动电话)和微小[嵌入式系统](https://baike.baidu.com/item/嵌入式系统)

## 目录

1. 1 [简介](https://baike.baidu.com/item/RISC-V/22606314#1)
2. 2 [特色：](https://baike.baidu.com/item/RISC-V/22606314#2)
3. ▪ [1 完全开源](https://baike.baidu.com/item/RISC-V/22606314#2_1)

1. ▪ [2 架构简单](https://baike.baidu.com/item/RISC-V/22606314#2_2)
2. ▪ [3 易于移植*nix](https://baike.baidu.com/item/RISC-V/22606314#2_3)
3. ▪ [4 模块化设计](https://baike.baidu.com/item/RISC-V/22606314#2_4)
4. ▪ [5 完整的工具链](https://baike.baidu.com/item/RISC-V/22606314#2_5)

1. ▪ [6 开源实现](https://baike.baidu.com/item/RISC-V/22606314#2_6)
2. ▪ [6 成功的流片案例](https://baike.baidu.com/item/RISC-V/22606314#2_7)
3. ▪ [7 社区贡献](https://baike.baidu.com/item/RISC-V/22606314#2_8)

## 简介

[编辑](javascript:;)[ 语音](javascript:;)

RISC-V(读作“RISC-FIVE”)是基于精简指令集计算(RISC)原理建立的开放[指令集架构](https://baike.baidu.com/item/指令集架构/7029547)(ISA)，V表示为第五代RISC([精简指令集计算机](https://baike.baidu.com/item/精简指令集计算机/661859)),表示此前已经四代RISC处理器原型芯片。每一代RISC处理器都是在同一人带领下完成，那就是加州大学伯克利分校的David A. Patterson教授。与大多数ISA相反，RISC-V ISA可以免费地用于所有希望的设备中，允许任何人设计、制造和销售RISC-V芯片和软件。图1展示了此前的四代RISC处理器原型芯片。它虽然不是第一个开源的的指令集(ISA)，但它很重要，因为它第一个被设计成可以根据具体场景可以选择适合的指令集的指令集架构。基于RISC-V指令集架构可以设计[服务器CPU](https://baike.baidu.com/item/服务器CPU/586695)，家用电器cpu，工控cpu和用在比指头小的传感器中的cpu。

## 特色：

[编辑](javascript:;)[ 语音](javascript:;)

### 1 完全开源

对指令集使用，RISC-V基金会不收取高额的授权费。开源采用宽松的[BSD协议](https://baike.baidu.com/item/BSD协议/8013651)，企业完全自由免费使用，同时也容许企业添加自有指令集拓展而不必开放共享以实现差异化发展。

### 2 架构简单

RISC-V架构秉承简单的设计哲学。体现为：

在处理器领域，主流的架构为x86与[ARM架构](https://baike.baidu.com/item/ARM架构/9154278)。x86与ARM架构的发展的过程也伴随了现代处理器架构技术的不断发展成熟，但作为商用的架构，为了能够保持架构的向后兼容性，其不得不保留许多过时的定义，导致其指令数目多，指令冗余严重，文档数量庞大，所以要在这些架构上开发新的操作系统或者直接开发应用门槛很高。而RISC-V架构则能完全抛弃包袱，借助计算机体系结构经过多年的发展已经成为比较成熟的技术的优势，从轻上路。RISC-V基础指令集则只有40多条，加上其他的模块化扩展指令总共几十条指令。 RISC-V的规范文档仅有145页，而“特权架构文档”的篇幅也仅为91页。

### 3 易于移植*nix

现代操作系统都做了特权级指令和用户级指令的分离，特权指令只能操作系统调用，而用户级指令才能在用户模式调用，保障操作系统的稳定。RISC-V提供了特权级指令和用户级指令，同时提供了详细的RISC-V特权级指令规范和RISC-V用户级指令规范的详细信息，使开发者能非常方便的移植linux和unix系统到RISC-V平台。

### 4 模块化设计

RISC-V架构不仅短小精悍，而且其不同的部分还能以模块化的方式组织在一起，从而试图通过一套统一的架构满足各种不同的应用场景。用户能够灵活选择不同的模块组合，来实现自己定制化设备的需要，比如针对于小面积低功耗嵌入式场景，用户可以选择RV32IC组合的指令集，仅使用Machine Mode（机器模式）；而高性能应用操作系统场景则可以选择譬如RV32IMFDC的指令集，使用Machine Mode（机器模式）与User Mode（用户模式）两种模式。

### 5 完整的工具链

对于设计CPU来说，工具链是软件开发人员和cpu交互的窗口，没有工具链，对软件开发人员开发软件要求很高，甚至软件开发者无法让cpu工作起来。在cpu设计中，工具链的开发是一个需要巨大工作量的工作。如果用RISC-V来设计芯片，芯片设计公司不再担心工具链问题，只需专注于芯片设计，RISC-V社区已经提供了完整的工具链，并且RISC-V基金会持续维护该工具链。当前RISC-V的支持已经合并到主要的工具中，比如编译工具链gcc, 仿真工具qemu等

### 6 开源实现

BOOM: Christopher Celio的RV64乱序处理器实现。Chisel, BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)][[Doc](https://baike.baidu.com/item/Doc)]

BottleRocket: RV32IMC微处理器。Chisel， Apache Licensed。 [[GitHub](https://baike.baidu.com/item/GitHub)]

bwitherspoon: RV32微处理器。SystemVerilog, ISC Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

Clarvi: 剑桥大学教学用RISC-V处理器。SystemVerilog, BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

F32: 针对FPGA的RV32微处理器，VHDL，BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

GRVI: Gray Research LLC. 针对FPGA优化的RV32微处理器，commercial licensed。[[Web](https://baike.baidu.com/item/Web)]

Hummingbird E200. 二级流水线，目标替代Cortex-M0/8051, Verilog, Apache 2.0 licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

invicta: 一级流水线的RV32微处理器。Verilog，BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

Kamikaze: RV32微处理器。Verilog，MIT Liencensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

KCP53000: Samuel A. Falvo II的RV64处理器实现。Verilog, MPL Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

nanorv32: 2机流水线的RV32实现。Verilog, GPLv2 Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

OpenV: 支持RV32的开源微处理器，Verilog，MIT Licensed，OnChipUIS，来源于哥伦比亚的Universidad Industrial de Santander。[[GitHub](https://baike.baidu.com/item/GitHub)]

ORCA: 支持RV32的开源微处理器，VHDL，BSD Licensed，VectorBlox。[[Github](https://baike.baidu.com/item/Github)]

PicoRV32: Clifford Wolf设计的(针对FPGA)RV32微处理器，Verilog，ISC Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

Potato: 针对FPGA的RV32微处理器。VHDL，BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

RI5CY：支持RV32的开源微处理器

- PULPino: SystemVerilog，Solderpad Licensed, 来源于苏黎世理工和博洛尼亚大学的PULP项目。[[GitHub](https://baike.baidu.com/item/GitHub)][[Web](https://baike.baidu.com/item/Web)]

River: GNSS Senor Ltd.基于Rocket架构开发的RV64处理器。VHDL, BSD Licensed。[GitHub]

Rocket: 支持RV64/32的开源处理器

- Rocket-Chip: Chisel，BSD Licensed, Free chips project, UC Berkeley分离的开源工程。[[GitHub](https://baike.baidu.com/item/GitHub)]
- Freedom: Chisel，Apache Licensed, SiFive, UC Berkeley分离的初创企业。[[GitHub](https://baike.baidu.com/item/GitHub)][[Web](https://baike.baidu.com/item/Web)]
- lowRISC：Chisel+SystemVerilog，Solderpad Licensed, 从剑桥大学发起的非盈利组织。[[GitHub](https://baike.baidu.com/item/GitHub)][[Web](https://baike.baidu.com/item/Web)]
- RoCC: the Rocket customized coprocessor interface 和Rocket处理器紧密互联的的协处理器接口。[[BSG](https://baike.baidu.com/item/BSG)]

RV12: RoaLogic的RV32微处理器。Verilog, RoaLogic non-commercial Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

SCR1: Syntacore的RV32开源微处理器。SystemVerilog，Solerpad Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

SHAKTI：印度IIT-Madras的RISC-V处理器系列，Bluespec, BSD Licensed。[[Bitbucket](https://baike.baidu.com/item/Bitbucket)]

Sodor: 教学用的RISC-V处理器。Chisel, BSD Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

uRV: 针对FPGA的RV32微处理器。Verilog，LGPLv3 Licensed.[ohwr]

VexRiscv: 用SpinalHDL编写的针对FPGA的RV32微处理器。SpinalHDL, MIT Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

YARVI: Tommy Thorn设计的RV32I微处理器，Verilog，GPL2v Licensed。[[GitHub](https://baike.baidu.com/item/GitHub)]

### 6 成功的流片案例

已经有机构和商业公司流片的案例。可关注RISC-V社区了解具体信息。

### 7 社区贡献

完整的工具链维护，大量的开源项目。risc-v的google讨论组(名称：RISC-V ISA Dev)吸引各地自愿者参与讨论来不断改进risc-v架构。 [1] 