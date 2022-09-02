# Handle和Handler

- **A handle is an abstract reference to a resource. Handle**是对某个资源的抽象引用。
- **A handler is an asynchronous callback subroutine. Handler**则是一个异步的回调函数(子程序)。

## Handle

handle在计算机世界里的含义：

A handle is an **abstract reference to a resource**.

A handle is a **unique identifier** for an object managed by Windows.

A handle can be anything from an **integer index** to a **pointer** to **a resource in kernel space**. The idea is that they provide an abstraction of a resource, so you don't need to know much about the resource itself to use it.

