# Handle和Handler

- **A handle is an abstract reference to a resource. Handle**是对某个资源的抽象引用。
- **A handler is an asynchronous callback subroutine. Handler**则是一个异步的**回调函数(子程序)**。

## Handle

重点：

- handle（句柄）, 说白了就是**跟一个黑盒子进行通信的密码**。一旦通信密码传给了黑盒子，黑盒子具体怎么操作，对**持有handle的用户**来说，完全不用关心。"**不看过程，只看结果**"就得了。 
- **用户程序拿到的handle，通常并不能够径直通向真实的内核资源**，而是需要"**绕个弯儿**"，也就是**被内核映射成一个指向内核资源的首地址的pointer**才能够访问真实的内核资源。

handle在计算机世界里的含义：

- A handle is an **abstract reference to a resource**. 对某个资源的抽象引用
- A handle is a **unique identifier** for an object managed by Windows.
- A handle can be anything from an **integer index** to a **pointer** to **a resource in kernel space**. The idea is that **they provide an abstraction of a resource**, so you **don't need to know much about the resource itself to use it**. 一种资源的抽象，不了解资源本身就可以使用该资源。

例如： 在Unix/Linux系统中：

- **进程号**pid就是一个handle
- **文件描述符**(fd)也是一个handle
- **系统调用号**(syscall num)仍然是一个handle

在操作系统中，一切对用户来说是透明(注：这里的"透明"指的是"看不见摸不着就如空气一样"而不是"一览无余毫无秘密可言")的但是操作系统内核看得懂的**无符号整数(unsigned int)**都可以被看作是**handle**。

在操作系统设计与实现中，**联系内核态和用户态，靠的就是一个个无符号整数**。因为用数字来做通信密码(比如：操作码，错误码等)实在是太方便了。而且，一个unsigned int占4个字节，可以表征的通信密码总数为2^32(=4G, 约40亿)。 如果不用无符号整数来做通信密码，而是采用可读性很好的明文(字符串"string")来做通信，那是何等的情何以堪？！ 因为，计**算机做字符串比较的代价要远远大于无符号整数的比较**。

handle（句柄）, 说白了就是**跟一个黑盒子进行通信的密码**。一旦通信密码传给了黑盒子，黑盒子具体怎么操作，对持有handle的用户来说，完全不用关心。"**不看过程，只看结果**"就得了。 

**用户程序拿到的handle，通常并不能够径直通向真实的内核资源**，而是需要"**绕个弯儿**"，也就是**被内核映射成一个指向内核资源的首地址的pointer**才能够访问真实的内核资源。



In computer programming, a handle is an abstract reference to a resource. 
Handles are used when **application** software references **blocks of memory or** 
**objects managed by another system**, such as a database or an operating system. 

A resource handle can be an **opaque identifier**, in which case it is often an 
**integer number** (often an array index in an array or "table" that is used to 
manage that type of resource), or it can be a **pointer** that **allows access to** 
**further information**.

Common resource handles are **file descriptors**, network sockets, 
database connections, **process identifiers (PIDs)**, and job IDs. 
Process IDs and job IDs are explicitly visible integers, while file descriptors 
and sockets (which are often implemented as a form of file descriptor) are 
represented as integers, but are typically considered opaque. In traditional 
implementations, file descriptors are indices into a (per-process) file 
descriptor table, thence a (system-wide) file table.



## Handler

hanlder就是一个**回调函数(callback)**。当某个事件到达时，事先注册的handler会被接收到事件的主体所调用。 

Handler, an asynchronous callback (computer programming) subroutine in computing

- Event handler: a routine for processing a programming event
- Interrupt handler: a routine for processing CPU interrupts
- Signal handler: a routine for handling signals sent to a process
- **Exception handler**: a routine for handling **software exceptions**
