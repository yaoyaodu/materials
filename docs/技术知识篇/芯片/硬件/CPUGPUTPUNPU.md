# CPU GPU TPU NPU

来源：[CPU/GPU/TPU/NPU傻傻分不清楚 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/101550272)

## CPU

CPU英文全称是Central Processing Unit，中文全称是中央处理器，是计算机的核心器件，CPU通常由三个部分组成：**计算单元、控制单元和存储单元。**

<img src="https://pic2.zhimg.com/v2-d65f155a80f7a1d6e6227d01c7f414a1_r.jpg" alt="preview" style="zoom: 67%;" />

<img src="https://i.loli.net/2021/08/25/MiC7gJOvsKFRN49.jpg" alt="preview" style="zoom:50%;" />

## GPU

GPU全称是Graphics Processing Unit，中文全称叫图形处理器，它也是由三个部分组成：**计算单元、控制单元和存储单元。**

<img src="https://i.loli.net/2021/08/25/db2DQwWXm7LveKg.jpg" alt="preview" style="zoom: 50%;" />

<font color="yellow">黄色用来表示控制单元</font>，<font color="green">绿色用来表示计算单元</font>，<font color="orange">橙色用来表示存储单元</font>

![preview](https://pic4.zhimg.com/v2-005d784787c6e72d75214c3cbe1ea303_r.jpg)

CPU 30%都是用在了控制单元，各个单元占比还算均衡，而**GPU 80%以上都用在了计算单元**。

正是由于这种区别，导致**CPU精于控制和复杂运算，而GPU精于简单且重复的运算**。

另外CPU和GPU还有一个最大的区别：**CPU是顺序执行运算，而GPU是可以大量并发的执行运算**，通俗的说就是**CPU做事情是一件一件来做，而GPU是很多件事情同时做**。

但很多件事情同时做，一定是简单的事情，就像一个人一样，我们没法同时做两件复杂的事情。借用知乎上某大神的说法，**就像你有个工作需要计算几亿次一百以内加减乘除一样，最好的办法就是雇上几十个小学生一起算，一人算一部分，反正这些计算也没什么技术含量，纯粹体力活而已**；而**CPU就像老教授，积分微分都会算，就是工资高，**一个老教授资顶二十个小学生，你要是富士康你雇哪个？

**GPU就是用很多简单的计算单元去完成大量的计算任务，纯粹的人海战术**。这种策略基于一个前提，就是小学生A和小学生B的工作没有什么依赖性，是互相独立的。

但有一点需要强调，虽然GPU是为了图像处理而生的，但是我们通过前面的介绍可以发现，**它在结构上并没有专门为图像服务的部件，只是对CPU的结构进行了优化与调整，所以现在GPU不仅可以在图像处理领域大显身手，它还被用来科学计算、密码破解、数值分析，海量数据处理（排序，Map-Reduce等），金融分析等需要大规模并行计算的领域。**

CPU和GPU都是通用芯片。

但古语有云：工欲善其事必先利其器。

一块石头，是通用的，但如果我专门打磨打磨，让它变成锋利的，是不是就可以用来切割东西了呢？

有了这个概念后，对于TPU，NPU等等众多的PU们，你把它们当成都是专门打磨过的石头，就很好理解了。

其中Control是控制器、ALU算术逻辑单元、Cache是cpu内部缓存、DRAM就是内存。可以看到GPU设计者将更多的晶体管用作执行单元，而不是像CPU那样用作复杂的控制单元和缓存。
从实际来看，CPU芯片空间的5%是ALU，而GPU空间的40%是ALU。这也是导致GPU计算能力超强的原因。

CPU和GPU的主要区别：

* CPU是一个**有多种功能的优秀领导者**。它的优点在于调度、管理、协调能力强，计算能力则位于其次。

* GPU相当于一个**接受CPU调度的“拥有大量计算能力”的员工**。

  

* **GPU可以利用多个CUDA核心来做并行计算**。

* CPU只能**按照顺序进行串行计算**，同样运行3000次的简单运算，CPU需要3000个时钟周期，而配有3000个**CUDA核心**的GPU运行只需要1个时钟周期。

说明：

CUDA核心：**CUDA核心数量决定了GPU并行处理的能力**，在深度学习、机器学习等并行计算类业务下，CUDA核心多意味着性能好一些。

**GPU 比 CPU 擅长并行计算**。一个 3D 图形最终会被分解为许多个像素点来计算，如果要渲染速度快，这就要求 **GPU 的硬件结构是满足同时进行大量的简单计算**的，这个需求导致了 GPU 与 CPU 的硬件架构不同。

从芯片设计思路看，CPU是**以低延迟为导向的计算单元**，通常由专为**串行处理**而优化的**几个核心**组成，而 GPU 是**以吞吐量为导向的计算单元**，由**数以千计**的更小、更高效的核心组成，专为**并行多任务**设计。

微架构的不同最终导致 CPU 中**大部分的晶体管用于构建控制电路和缓存**，只有少部分的晶体管完成实际的运算工作，功能模块很多，擅长分支预测等复杂操作。

GPU的流处理器（承担简单计算任务）和显存控制器占据了绝大部分晶体管，而控制器相对简单，擅长对大量数据进行简单操作，**拥有远胜于 CPU 的强大浮点计算能力**，从而更**擅长并行计算，比如图像处理计算，物理仿真，深度学习**等。

通用图形处理器（GPGPU (general purpose graphic processing unit)）：可执行通用计算任务的图形处理器。即**利用图形处理器内部的大量并行运算部件，辅助CPU进行密集的数据并行计算**。

## TPU 

针对谷歌的深度学习框架TensorFlow专门定制的芯片诞生了，英文全称就叫**Tensor Processing Unit**，中文是**张量处理单元**。

**TPU与同期的CPU和GPU相比，可以提供15-30倍的性能提升，以及30-80倍的效率（性能/瓦特）提升。**

## **NPU**

NPU英文全称是**Neural network** Processing Unit， 中文叫神经网络处理器。

神经网络就是你**大脑里面的神经元连接成的网络**，错综复杂，据说**越复杂越聪明**。

NPU就是要**模仿人的大脑神经网络，使之具备智能。**

NPU工作原理是**在电路层模拟人类神经元和突触，并且用深度学习指令集直接处理大规模的神经元和突触，一条指令完成一组神经元的处理。**

相比于CPU和GPU，NPU通过**突触权重**实现**存储和计算一体化**，从而**提高运行效率**。

## 各种PU（进行**专门运算**的芯片）

**这些处理器都是研发来进行专门的计算的芯片，同样也需要CPU调用。**

IPU (Intelligence Processing Unit)，Deep Mind投资的Graphcore公司出品的AI处理器产品。

MPU/MCU (Microprocessor/Micro controller Unit)， 微处理器/微控制器，一般用于**低计算应用**的**RISC计算机体系架构产品**，如ARM-M系列处理器。

NPU (Neural Network Processing Unit)，神经网络处理器，是基于神经网络算法与加速的新型处理器总称，如中科院计算所/寒武纪公司出品的diannao系列。

RPU (Radio Processing Unit), 无线电处理器， Imagination Technologies 公司推出的集合集Wifi/蓝牙/FM/处理器为单片的处理器。

TPU (Tensor Processing Unit), 张量处理器， Google 公司推出的加速人工智能算法的专用处理器。目前**一代TPU面向推理Inference，二代面向训练**。

VPU (Vector Processing Unit), 矢量处理器，Intel收购的Movidius公司推出的图像处理与人工智能的专用芯片的加速计算核心。

WPU (Wearable Processing Unit)， 可穿戴处理器，Ineda Systems公司推出的可穿戴片上系统产品，包含GPU/MIPS CPU等IP。

XPU: 百度与Xilinx公司在2017年Hotchips大会上发布的FPGA智能云加速，含256核。

ZPU (Zylin Processing Unit), 由挪威Zylin 公司推出的一款32位开源处理器。

TPU（Tensor Processing Unit）是谷歌公司专门为加速深层神经网络运算能力研发的芯片。

NPU（Neural Processing Unit）叫神经网络处理器，是用电路来模仿人类的神经元和突触结构，目前主要是国内的寒武纪芯片和IBM的TrueNorth芯片。

除此之外，常见的还有BPU（Brain Processing Unit）大脑处理器和DPU（Deep Learning Processing Unit）深度学习处理器。**这些处理器都是研发来进行专门的计算的芯片，同样也需要CPU调用。**

还没有完，除了上述的这些芯片，我们还有APU、FPU、HPU、IPU、MPU、RPU、VPU、WPU、XPU、ZPU……无一例外，这些处理器也都是来进行**专门运算**的芯片。



