简介
.............

mcBLAS库是BLAS (Basic Linear
Algebra子程序)。IT
允许用户访问MetaX的计算资源
图形处理单元(GPU)。

要使用mcBLAS API，应用程序必须分配所需的
GPU内存空间中的矩阵和矢量，用数据填充它们，
调用所需的mcBLAS函数序列，然后上载
GPU内存空间返回主机的结果。mcBLAS API
还提供用于写入和检索数据的帮助程序函数
从GPU。

mcBLAS的目标是：

- 功能类似于传统BLAS，经过调整可在GPU上运行

- 高性能稳健实施

mcBLAS以C++14和MACA编写。它使用MetaX的MACA运行时在GPU设备上运行。

mcBLAS API是使用沙漏模式的精简C99 API。它包含：

-[Helper]，[Level1]，[Level2]和[Level3][BLAS-like ] BLAS函数，具有批处理和strided_batched版本

安装mcBLAS
==================

.. math:: 
   MACA\begin{cases}
         library & \begin{cases}
                     mcBLAS \\
                     \vdots
                     \end{cases} \\
         \vdots \\
         \vdots
         \end{cases}

mcBLAS是随MACA工具包一起发布的库。MACA工具包的安装请参阅MACAACA快速入门指南。
安装后，确保环境变量MACA_PATH已设置。 

.. code-block:: shell

   export MACA_PATH=/your/maca/path

The mcBLAS API related files are listed as follows. 

.. code-block:: cmake
   
   #header location:  
   ${MACA_PATH}/include/mcblas

   #lib location:     
   ${MACA_PATH}/lib/libmcblas.so

在使用mcBLAS库进行编译之前，请确保环境变量ISI_FASTMODEL设置为1。

.. code-block:: shell

   export ISU_FASTMODEL=1


您好mcBLAS
=============

有关示例代码引用，请参阅下面的两个示例。
它们显示使用mcBLAS库以C语言编写的应用程序
具有两种索引样式的API (示例1. "Application Using C
and mcBLAS: 1-based indexing" and Example 2. "Application Using
C and mcBLAS: 0-based Indexing").


.. code-block:: cmake

   #CMakeLists.txt
   cmake_minimum_required(VERSION 3.5.0)
   set(PROJECT_NAME example)
   project(${PROJECT_NAME} VERSION 0.1.0)
   set(CMAKE_BUILD_TYPE "Debug")
   set(CMAKE_CXX_STANDARD 14)
   INCLUDE_DIRECTORIES(ENV{MACA_PATH}/include/mcr)
   INCLUDE_DIRECTORIES(ENV{MACA_PATH}/include/mcblas)
   INCLUDE_DIRECTORIES(ENV{MACA_PATH}/include)
   LINK_DIRECTORIES(ENV{MACA_PATH}/lib)

   file(GLOB EXAMPLE_SRCS1 "example1.cpp")
   file(GLOB EXAMPLE_SRCS2 "example2.cpp")

   add_executable("example1" ${EXAMPLE_SRCS1})
   add_executable("example2" ${EXAMPLE_SRCS2})

   target_link_libraries("example1" mcblas mcruntime)
   target_link_libraries("example2" mcblas mcruntime)

::

   //示例1。使用C和mcBLAS的应用程序：基于1的索引
   //example1.cpp
   //-----------------------------------------------------------
   #include <stdio.h>
   #include <stdlib.h>
   #include <math.h>
   #include <mc_runtime.h>
   #include "mcblas.h"
   #define M 6
   #define N 5
   #define IDX2F(i,j,ld) ((((j)-1)*(ld))+((i)-1))

   static __inline__ void modify (mcblasHandle_t handle, float *m, int ldm, int n, int p, int q, float alpha, float beta){
         mcblasSscal (handle, n-q+1, &alpha, &m[IDX2F(p,q,ldm)], ldm);
         mcblasSscal (handle, ldm-p+1, &beta, &m[IDX2F(p,q,ldm)], 1);
   }

   int main (void){
         int mcStat;
         mcblasStatus_t stat;
         mcblasHandle_t handle;
         int i, j;
         float* devPtrA;
         float* a = 0;
         a = (float *)malloc (M * N * sizeof (*a));
         if (!a) {
            printf ("host memory allocation failed");
            return EXIT_FAILURE;
         }
         for (j = 1; j <= N; j++) {
            for (i = 1; i <= M; i++) {
               a[IDX2F(i,j,M)] = (float)((i-1) * N + j);
            }
         }
         mcStat = mcMalloc ((void**)&devPtrA, M*N*sizeof(*a));
         if (mcStat != 0) {
            printf ("device memory allocation failed");
            return EXIT_FAILURE;
         }
         stat = mcblasCreate(&handle);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("MCBLAS initialization failed\n");
            return EXIT_FAILURE;
         }
         stat = mcblasSetMatrix (M, N, sizeof(*a), a, M, devPtrA, M);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("data download failed");
            mcFree (devPtrA);
            mcblasDestroy(handle);
            return EXIT_FAILURE;
         }
         modify (handle, devPtrA, M, N, 2, 3, 16.0f, 12.0f);
         stat = mcblasGetMatrix (M, N, sizeof(*a), devPtrA, M, a, M);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("data upload failed");
            mcFree (devPtrA);
            mcblasDestroy(handle);
            return EXIT_FAILURE;
         }
         mcFree (devPtrA);
         mcblasDestroy(handle);
         for (j = 1; j <= N; j++) {
            for (i = 1; i <= M; i++) {
               printf ("%7.0f", a[IDX2F(i,j,M)]);
            }
            printf ("\n");
         }
         free(a);
         return 0;
   }

::

   //示例2.使用C和mcBLAS的应用程序：基于0的索引
   //example2.cpp
   //-----------------------------------------------------------
   #include <stdio.h>
   #include <stdlib.h>
   #include <math.h>
   #include <mc_runtime.h>
   #include "mcblas.h"
   #define M 6
   #define N 5
   #define IDX2C(i,j,ld) (((j)*(ld))+(i))

   static __inline__ void modify (mcblasHandle_t handle, float *m, int ldm, int n, int p, int q, float alpha, float beta){
         mcblasSscal (handle, n-q, &alpha, &m[IDX2C(p,q,ldm)], ldm);
         mcblasSscal (handle, ldm-p, &beta, &m[IDX2C(p,q,ldm)], 1);
   }

   int main (void){
         int mcStat;
         mcblasStatus_t stat;
         mcblasHandle_t handle;
         int i, j;
         float* devPtrA;
         float* a = 0;
         a = (float *)malloc (M * N * sizeof (*a));
         if (!a) {
            printf ("host memory allocation failed");
            return EXIT_FAILURE;
         }
         for (j = 0; j < N; j++) {
            for (i = 0; i < M; i++) {
               a[IDX2C(i,j,M)] = (float)(i * N + j + 1);
            }
         }
         mcStat = mcMalloc ((void**)&devPtrA, M*N*sizeof(*a));
         if (mcStat != 0) {
            printf ("device memory allocation failed");
            return EXIT_FAILURE;
         }
         stat = mcblasCreate(&handle);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("MCBLAS initialization failed\n");
            return EXIT_FAILURE;
         }
         stat = mcblasSetMatrix (M, N, sizeof(*a), a, M, devPtrA, M);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("data download failed");
            mcFree (devPtrA);
            mcblasDestroy(handle);
            return EXIT_FAILURE;
         }
         modify (handle, devPtrA, M, N, 1, 2, 16.0f, 12.0f);
         stat = mcblasGetMatrix (M, N, sizeof(*a), devPtrA, M, a, M);
         if (stat != MCBLAS_STATUS_SUCCESS) {
            printf ("data upload failed");
            mcFree (devPtrA);
            mcblasDestroy(handle);
            return EXIT_FAILURE;
         }
         mcFree (devPtrA);
         mcblasDestroy(handle);
         for (j = 0; j < N; j++) {
            for (i = 0; i < M; i++) {
               printf ("%7.0f", a[IDX2C(i,j,M)]);
            }
            printf ("\n");
         }
         free(a);
         return EXIT_SUCCESS;
   }

移植CUBLAS应用程序
============================

将最初调用cuBLAS API的CUDA应用程序移植到调用mcBLAS API的应用程序应该很容易。
MACA工具包提供了CUDA包装工具，可帮助您完成移植任务。 
基本上，您不需要修改源代码。使用cuBLAS应用程序，例如：

::

   //示例1。使用C和cuBLAS的应用：基于1的索引
   //-----------------------------------------------------------
   #include <stdio.h>
   #include <stdlib.h>
   #include <math.h>
   #include <cuda_runtime.h>
   #include "cublas_v2.h"
   #define M 6
   #define N 5
   #define IDX2F(i,j,ld) ((((j)-1)*(ld))+((i)-1))

   static __inline__ void modify (cublasHandle_t handle, float *m, int ldm, int n, int p, int q, float alpha, float beta){
       cublasSscal (handle, n-q+1, &alpha, &m[IDX2F(p,q,ldm)], ldm);
       cublasSscal (handle, ldm-p+1, &beta, &m[IDX2F(p,q,ldm)], 1);
   }

   int main (void){
       cudaError_t cudaStat;
       cublasStatus_t stat;
       cublasHandle_t handle;
       int i, j;
       float* devPtrA;
       float* a = 0;
       a = (float *)malloc (M * N * sizeof (*a));
       if (!a) {
           printf ("host memory allocation failed");
           return EXIT_FAILURE;
       }
       for (j = 1; j <= N; j++) {
           for (i = 1; i <= M; i++) {
               a[IDX2F(i,j,M)] = (float)((i-1) * N + j);
           }
       }
       cudaStat = cudaMalloc ((void**)&devPtrA, M*N*sizeof(*a));
       if (cudaStat != cudaSuccess) {
           printf ("device memory allocation failed");
           return EXIT_FAILURE;
       }
       stat = cublasCreate(&handle);
       if (stat != CUBLAS_STATUS_SUCCESS) {
           printf ("CUBLAS initialization failed\n");
           return EXIT_FAILURE;
       }
       stat = cublasSetMatrix (M, N, sizeof(*a), a, M, devPtrA, M);
       if (stat != CUBLAS_STATUS_SUCCESS) {
           printf ("data download failed");
           cudaFree (devPtrA);
           cublasDestroy(handle);
           return EXIT_FAILURE;
       }
       modify (handle, devPtrA, M, N, 2, 3, 16.0f, 12.0f);
       stat = cublasGetMatrix (M, N, sizeof(*a), devPtrA, M, a, M);
       if (stat != CUBLAS_STATUS_SUCCESS) {
           printf ("data upload failed");
           cudaFree (devPtrA);
           cublasDestroy(handle);
           return EXIT_FAILURE;
       }
       cudaFree (devPtrA);
       cublasDestroy(handle);
       for (j = 1; j <= N; j++) {
           for (i = 1; i <= M; i++) {
               printf ("%7.0f", a[IDX2F(i,j,M)]);
           }
           printf ("\n");
       }
       free(a);
       return EXIT_SUCCESS;
   }

当上面的示例写入名为mySample.cpp的文件时，您可以在Linux上使用cualas对动态库进行编译，可以使用以下命令：

::

   nvcc mySample.cpp -lcublas -o mySample

现在，如果要将此示例从cuBLAS迁移到mcBLAS，请设置两个环境变量。

::
   
   export MACA_PATH=<your maca toolkit dir>
   export CUDA_PATH=${MACA_PATH}/tools/wcuda

然后，使用原始方法构建应用程序

::

   nvcc mySample.cpp -lcublas -o mySample

现在，mySample是使用mcBLAS运行的二进制文件。


数据布局
============

为了最大限度地兼容现有的Fortran环境，
mcBLAS库使用基于列的主存储和1
索引。由于C和C++使用行主存储，因此应用程序
用这些语言编写的不能使用本机数组
二维数组的语义。而是宏或内联
应定义函数以在上实现矩阵
一维数组。用于移植到C In的Fortran代码
机械方式，可以选择将基于1的索引保留到
无需转换循环。在这种情况下，是数组
行“i”和列“j”中矩阵元素的索引可以是
通过以下宏计算

::

   #define IDX2F(i,j,ld) ((((j)-1)*(ld))+((i)-1))

此处，ld指的是矩阵的前导维度，即
对于列主存储，是的行数
分配的矩阵(即使只是其子矩阵)
已使用)。对于本机编写的C和C++代码，最容易编写
可能选择基于0的索引，在这种情况下是数组索引
可以计算行“i”和列“j”中矩阵元素的值
通过以下宏

::

   #define IDX2C(i,j,ld) (((j)*(ld))+(i))

使用mcBLAS API
.................

mcBLAS数据类型
=================

mcblasHandle_t
---------------

``mcblasHandle_t`` 类型是指向不透明的指针类型
包含mcBLAS库上下文的结构。mcBLAS
必须使用 ``mcblasCreate()初始化库上下文``
返回的句柄必须传递给所有后续的句柄
库函数调用。上下文应在中销毁
使用 ``mcblasDestroy()结束``。

mcblas_int
----------

::

   typedef int32_t mcblas_int;

根据MetaX的硬件，通过mcBLAS指定int。

mcblas跨步
--------------

::

   typedef int64_t mcblas_stride;

strided_batched函数中矩阵或向量之间的跨距。


mcblas_half
------------

表示16位浮点数字的结构；

mcComplex
----------

类表示具有单精度实数和虚数部分的复数。

mcDoubleComplex
----------------

类表示具有双精度实数和虚数部分的复数。


mcblasStatus_t
---------------

类型用于函数状态返回。
所有mcBLAS库函数调用返回其错误状态 ``mcblasStatus_t``。

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | 值                            | 含义                          |
   +==================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``        | 操作已完成          |
   |                                  | 成功                     |
   +----------------------------------+----------------------------------+
   |                                  | 库未初始化  |
   |``MCBLAS_STATUS_NOT_INITIALIZED`` |                                  |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``   | 资源分配失败   |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``  | 无效的数值为   |
   |                                  | 用作参数              |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_ARCH_MISMATCH``  | 缺少设备体系结构   |
   |                                  | 功能为必填项              |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR``  | 访问GPU内存空间    |
   |                                  | 失败                           |
   +----------------------------------+----------------------------------+
   |                                  | GPU程序无法        |
   |``MCBLAS_STATUS_EXECUTION_FAILED``| 执行                          |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INTERNAL_ERROR`` | 内部操作失败     |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``  | 所需的功能不是      |
   |                                  | 支持                        |
   +----------------------------------+----------------------------------+

mcblasDataType_t
------------------

``mcblasDataType_t`` 类型是指定的枚举符
数据精度。当数据引用不使用时使用
携带类型本身(例如void \*)

例如 ``mcblasSgemmEx``，它在例程中使用。

.. table:: 
   :widths: grid

   +-----------------+---------------------------------------------------+
   | 值           | 含义                                           |
   +=================+===================================================+
   | ``MCBLAS_R_16F``| 数据类型为16位实际半精度       |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_16F``|数据类型为16位复数半精度    |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_R_16BF``|数据类型为16位Real bfloat16             |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_C_16BF``|数据类型为16位复杂bfloat16          |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_R_32F`` | 数据类型为32位实际单精度     |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_32F``|数据类型为32位复杂单精度  |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_64F``|数据类型为64位实际双精度     |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_64F``|数据类型为64位复数双精度  |
   |                 | 浮点                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_8I`` | 数据类型是8位实数带符号整数        |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_8I`` | 数据类型是8位复杂的带符号整数     |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_8U`` | 数据类型是8位实数无符号整数      |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_8U`` | 数据类型是8位复杂无符号整数   |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_32I``|数据类型为32位实数符号整数       |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_32I``|数据类型是32位复杂的带符号整数    |
   +-----------------+---------------------------------------------------+

mcblasOperation_t
------------------

``mcblasOperation_t`` 类型指示哪种操作
需要使用密集矩阵执行。它的价值
对应于Fortran字符 ``'N'`` 或 ``'n'``
(非转置)， ``'T'`` 或 ``'t'`` (转置)和 ``'C'``
或 通常 用作的``'c'``(偶联物转置)
传统BLAS实现的参数。

=============== =============================================
Value           Meaning
=============== =============================================
``MCBLAS_OP_N`` 选择非转置操作
``MCBLAS_OP_T`` 选择转置操作
``MCBLAS_OP_C`` 已选择偶联物转置操作
=============== =============================================

mcblasFillMode_t
-----------------

类型表示密度的哪个部分(较低或较高)
矩阵已填充，因此应由使用
功能。其值对应于Fortran字符
``‘L’`` or ``‘l’`` (lower) and ``‘U’`` or ``‘u’`` (upper)
通常用作传统BLAS的参数
实施。

========================== ======================================
Value                      Meaning
========================== ======================================
``MCBLAS_FILL_MODE_LOWER`` 矩阵的下半部分被填充
``MCBLAS_FILL_MODE_UPPER`` 矩阵的上半部分被填充
``MCBLAS_FILL_MODE_FULL``  填充完整的矩阵
========================== ======================================

mcblasDiagType_t
------------------

类型表示密度的主对角线
矩阵是一个整体，因此不应触及或
由函数修改。其值对应于Fortran
characters ``‘N’`` or ``‘n’`` (non-unit) and ``‘U’`` or
``‘u’`` (unit) that are often used as parameters to legacy
BLAS实现。

======================== =========================================
Value                    Meaning
======================== =========================================
``MCBLAS_DIAG_NON_UNIT`` 矩阵对角线有非单位元素
``MCBLAS_DIAG_UNIT``     矩阵对角线有单位元素
======================== =========================================

mcblasSideMode_t
-------------------

类型指示密集矩阵是否位于左侧
或由特定求解的矩阵方程式的右侧
功能。其值对应于Fortran字符
``‘L’`` or ``‘l’`` (left) and ``‘R’`` or ``‘r’`` (right)
通常用作传统BLAS的参数
实施。

===================== ===============================================
Value                 Meaning
===================== ===============================================
``MCBLAS_SIDE_LEFT``  矩阵位于方程式的左侧
``MCBLAS_SIDE_RIGHT`` 矩阵位于方程式的右侧
===================== ===============================================

mcblasPointerMode_t
--------------------

``mcblasPointerMode_t`` 类型指示是否
标量值通过主机或设备上的引用传递。
必须指出，如果有多个标量值
在函数调用中存在，所有它们都必须符合
到同一个单一指针模式。可以设置指针模式
和使用 ``mcblasSetPointerMode()`` 和检索
``mcblasGetPointerMode()`` 例程。

.. table:: 
   :widths: grid

   +--------------------------------+------------------------------------+
   | Value                          | Meaning                            |
   +================================+====================================+
   | ``MCBLAS_POINTER_MODE_HOST``   | 标量被传递          |
   |                                | 主机上的参考              |
   +--------------------------------+------------------------------------+
   | ``MCBLAS_POINTER_MODE_DEVICE`` | 标量被传递          |
   |                                | 设备上的参考            |
   +--------------------------------+------------------------------------+

mcblasAtomicsMode_t
--------------------

类型指示具有的mcBLAS例程
可以使用使用原子的替代实现。 The
可以使用设置和查询原子模式
``mcblasSetAtomicsMode()`` 和 ``mcblasGetAtomicsMode()``
和例程。

============================== ===================================
Value                          Meaning
============================== ===================================
``MCBLAS_ATOMICS_NOT_ALLOWED`` 不允许使用原子
``MCBLAS_ATOMICS_ALLOWED``     允许使用原子
============================== ===================================

mcblasGemmAlgo_t
-------------------

mcblasGemmAlgo_t type是指定的枚举符
GPU上矩阵-矩阵乘法的算法。mcBLAS具有
以下算法选项：

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Value                             | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_GEMM_DEFAULT``           | 应用启发法以选择    |
   |                                   | gemm算法                    |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_ALGO0`` 至          | 显式选择算法    |
   | ``MCBLAS_GEMM_ALGO23``            | [0,23]. 注意：没有        |
   |                                   | 对MetaX安培的影响            |
   |                                   | GPU和更新的架构。      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_DEFAULT_TENSOR_OP`` | 此模式已过时，将会  |
   | [DEPRECATED]                      | 将在将来的版本中删除。   |
   |                                   | 应用启发法以选择    |
   |                                   | gemm算法，同时允许    |
   |                                   | 使用降低的精度          |
   |                                   | MCBLAS_COMPUTE_32F_FAST_16F       |
   |                                   | 内核(用于向后             |
   |                                   | 兼容性)。                   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_ALGO0_Tensor _OP``   | 这些值已过时，并且   |
   | 至                                | 将在将来删除       |
   | ``MCBLAS_GEMM_ALGO15_TENSOR_OP``  | 释放。显式选择      |
   | [DEPRECATED]                      | Tensor core GEMM Algorithm        |
   |                                   | [0,15]. 允许使用减少的     |
   |                                   | 精度                         |
   |                                   | MCBLAS_COMPUTE_32F_FAST_16F       |
   |                                   | 内核(用于向后             |
   |                                   | 兼容性)。注意：没有     |
   |                                   | 对MetaX安培有影响       |
   |                                   | GPU和更新的架构。      |
   +-----------------------------------+-----------------------------------+

mcblasMath_t
-------------

``mcblasMath_t`` 枚举类型在中使用
``mcblasSetMathMode()`` 以选择计算精度模式
定义如下。 

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | Value                            | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_DEFAULT_MATH``          | 这是默认的和          |
   |                                  | 高性能模式    |
   |                                  | 使用计算和中间    |
   |                                  | 至少具有的存储接收 |
   |                                  | 相同数量的尾数和  |
   |                                  | 所请求的指数位。      |
   |                                  | 将使用Tensor内核        |
   |                                  | 只要有可能。               |
   +----------------------------------+----------------------------------+
  
mcblasComputeType_t
--------------------

``mcblasComputeType_t`` 枚举类型在中使用
``mcblasGemmEx`` 和 ``mcblasLtMatmul`` (包括所有
批处理和条纹批处理变体)以选择计算
精度模式定义如下。

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | Value                            | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_COMPUTE_16F``           | 这是默认的和          |
   |                                  | 的最高性能模式     |
   |                                  | 16位半精密浮动   |
   |                                  | 点和所有计算和        |
   |                                  | 中间存储接收器  |
   |                                  | 至少16位半模        |
   |                                  | 精度。Tensor Cores将为  |
   |                                  | 尽可能使用。          |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_16F_PEDANTIC``  | 此模式使用16位半模       |
   |                                  | 精密浮点         |
   |                                  | 所有的标准化算术  |
   |                                  | 计算和的阶段    |
   |                                  | 主要用于数字 |
   |                                  | 稳健性研究，测试和 |
   |                                  | 调试。此模式可能不会   |
   |                                  | 与其他人一样出色    |
   |                                  | 模式，因为它会禁用   |
   |                                  | Tensor内核。                    |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F``           | 这是默认的32位       |
   |                                  | 单精度浮点  |
   |                                  | 和使用计算和             |
   |                                  | 中间存储接收器  |
   |                                  | 至少32位。             |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_PEDANTIC``  | 使用32位单精度     |
   |                                  | 所有的浮点运算 |
   |                                  | 计算阶段以及  |
   |                                  | 禁用算法             |
   |                                  | 高斯等优化   |
   |                                  | 降低复杂性(3M)。       |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_16F``  | 允许库使用Tensor |
   |                                  | 具有自动功能的模芯             |
   |                                  | 下转换和16位       |
   |                                  | 半精密计算       |
   |                                  | 32位输入和输出          |
   |                                  | 矩阵。                        |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_16BF`` | 允许库使用Tensor |
   |                                  | 具有自动功能的模芯             |
   |                                  | 下拉式和浮式16.      |
   |                                  | 计算32位输入和     |
   |                                  | 输出矩阵。                 |   
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_TF32`` | 允许库使用Tensor |
   |                                  | 采用TF32计算的内核      |
   |                                  | 32位输入和输出          |
   |                                  | 矩阵。                        |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_64F``           | 这是默认的64位       |
   |                                  | 双精度浮点  |
   |                                  | 和使用计算和             |
   |                                  | 中间存储接收器  |
   |                                  | 至少64位。             |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_64F_pedantic``  | 使用64位双精度     |
   |                                  | 所有的浮点运算 |
   |                                  | 计算阶段以及  |
   |                                  | 禁用算法             |
   |                                  | 高斯等优化   |
   |                                  | 降低复杂性(3M)。       |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32I``           | 这是默认的32位       |
   |                                  | 整数模式并使用计算    |
   |                                  | 和中间存储         |
   |                                  | 至少32位精度。  |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32I_pedantic``  | 使用32位整数算术   |
   |                                  | 用于所有计算阶段。  |
   +----------------------------------+----------------------------------+

mcBLAS帮助程序功能
=======================

mcblasCreate()
--------------

::

   mcblasStatus_t
   mcblasCreate(mcblasHandle_t *handle)

此函数初始化mcBLAS库并创建
将控标置于包含mcBLAS库的不透明结构中
上下文。它在主机和上分配硬件资源
在创建任何其他mcBLAS之前，必须调用设备和
库呼叫。mcBLAS库上下文绑定到
当前MACA设备。要在多个设备上使用库，
需要为每个设备创建一个mcBLAS句柄。
此外，对于给定的设备，多个mcBLAS句柄
可以创建不同的配置。因为
``mcblasCreate()`` 分配一些内部资源和
通过调用 ``mcblasDestroy()释放这些资源``
将隐式调用 ``mcblasDeviceSynchronize()``，它是
建议尽量减少的数量
``mcblasCreate()/mcblasDestroy()`` 出现。对于
使用中相同设备的多线程应用程序
不同的线程，建议的编程模型是
为每个线程创建一个mcBLAS句柄并使用该mcBLAS
在螺纹的整个使用寿命内使用手柄。

.. table:: 
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------------+
   | Return Value                      | Meaning                                 |
   +===================================+=========================================+
   | ``MCBLAS_STATUS_SUCCESS``         | 初始化成功            |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | MACA™运行时初始化失败 |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | 无法分配资源    |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | ``handle`` == NULL                      |
   +-----------------------------------+-----------------------------------------+

mcblasDestroy()
---------------

::

   mcblasStatus_t
   mcblasDestroy(mcblasHandle_t handle)

此函数释放mcBLAS使用的硬件资源
库。此函数通常是使用的最后一个调用
mcBLAS库的特定句柄。因为
``mcblasCreate()`` 分配一些内部资源和
通过调用 ``mcblasDestroy()释放这些资源``
将隐式调用 ``mcblasDeviceSynchronize()``，它是
建议尽量减少的数量
``mcblasCreate()/mcblasDestroy()`` 出现。

================================= ===============================
Return Value                      Meaning
================================= ===============================
``MCBLAS_STATUS_SUCCESS``         关闭成功
``MCBLAS_STATUS_NOT_INITIALIZED`` 库未初始化
================================= ===============================
        
mcblasGetVersion()
------------------    

::

   mcblasStatus_t
   mcblasGetVersion(mcblasHandle_t handle, int *version)

此函数返回mcBLAS的版本号
库。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | 为库提供的存储  |
   |                                 | 版本号未初始化 |
   |                                 | (NULL)                            |
   +---------------------------------+-----------------------------------+

mcblasGetProperty()
-------------------


::

   mcblasStatus_t
   mcblasGetProperty(libraryPropertyType type, int *value)

此函数返回中请求的属性的值
按值指向的内存。请参阅 ``libraryPropertyType``
支持的类型。

.. table:: 
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Return Value                      | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | 操作已完成           |
   |                                   | 成功                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | 类型值无效                |
   |                                   |                                   |
   |                                   | -  If invalid ``type`` value or   |
   |                                   |                                   |
   |                                   | -  ``value`` == NULL              |
   +-----------------------------------+-----------------------------------+

mcblasGetStatusName()
---------------------

::

   const char* mcblasGetStatusName(mcblasStatus_t status)

此函数返回给定的字符串表示
状态。

====================== ===========================================
Return Value           Meaning
====================== ===========================================
以null结尾的字符串表示的字符串 ``status``
====================== ===========================================

mcblasGetStatusString()
-----------------------

::

   const char* mcblasGetStatusString(mcblasStatus_t status)

此函数返回给定的描述字符串
状态。

====================== =================================
Return Value           Meaning
====================== =================================
NULL-terminated string The description of the ``status``
====================== =================================

mcblasSetStream()
-----------------

::

   mcblasStatus_t
   mcblasSetStream(mcblasHandle_t handle, mcStream_t streamId)

此函数设置mcBLAS库流，即
用于执行对mcBLAS库的所有后续调用
功能。如果未设置mcBLAS库流，请选择“全部”
内核使用 *默认* ``NULL`` 流。特别是，
此例程可用于更改内核之间的流
启动，然后将mcBLAS库流重置为
``NULL``。此外，此功能无条件重置
mcBLAS库工作空间返回默认工作空间
pool (see ``mcblasSetWorkspace()``).

================================= ===============================
Return Value                      Meaning
================================= ===============================
``MCBLAS_STATUS_SUCCESS``         the stream was set successfully
``MCBLAS_STATUS_NOT_INITIALIZED`` the library was not initialized
================================= ===============================

mcblasSetWorkspace()
--------------------

::

   mcblasStatus_t
   mcblasSetWorkspace(mcblasHandle_t handle, void *workspace, 
                      size_t workspaceSizeInBytes)

此函数将mcBLAS库工作空间设置为
用户拥有的设备缓冲区，将用于执行所有操作
对mcBLAS库函数(在上)的后续调用
当前设置的流)。如果mcBLAS库工作空间为
未设置，所有内核都将使用默认的工作区池
在mcBLAS上下文创建期间分配。特别是，
此例程可用于在之间更改工作区
内核启动。工作空间指针必须对齐
至少256字节，否则
``MCBLAS_STATUS_INVALID_VALUE`` 返回错误。。
``mcblasSetStream()`` 函数无条件重置
mcBLAS库工作空间返回到默认工作空间池。
太小 ``workspaceSizeInBytes`` 可能会导致某些例程
失败， ``MCBLAS_STATUS_ALLOC_FAILED`` 返回错误
或导致性能出现较大的回归。工作空间大小
等于或大于16KiB就足以防止
``MCBLAS_STATUS_ALLOC_FAILED`` 错误，而较大
工作空间可以为某些人提供性能优势
例程。用户提供的工作空间的建议大小为
至少4MiB (以匹配mcBLAS的默认工作空间池)。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | Return Value                       | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | 已成功设置流   |
   +------------------------------------+-----------------------------------+
   |                                    | 库未初始化   |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | ``workspace`` 指针不是  |
   |                                    | 至少对齐256字节     |
   +------------------------------------+-----------------------------------+

mcblasGetStream()
-----------------

::

   mcblasStatus_t
   mcblasGetStream(mcblasHandle_t handle, mcStream_t *streamId)

此函数获取当前的mcBLAS库流
用于执行对mcBLAS库函数的所有调用。
如果未设置mcBLAS库流，则所有内核都使用
*default*\ ``NULL`` stream.

================================= ====================================
Return Value                      Meaning
================================= ====================================
``MCBLAS_STATUS_SUCCESS``         流已成功返回
``MCBLAS_STATUS_NOT_INITIALIZED`` 库未初始化
``MCBLAS_STATUS_INVALID_VALUE``   ``streamId`` == NULL
================================= ====================================

mcblasGetPointerMode()
----------------------

::

   mcblasStatus_t
   mcblasGetPointerMode(mcblasHandle_t handle, mcblasPointerMode_t *mode)

此函数获取mcBLAS使用的指针模式
库。请参阅上的部分
``mcblasPointerMode_t`` 有关详细信息，请键入。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | 已获得指针模式    |
   |                                    | 成功                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | ``mode`` == NULL                 |
   +------------------------------------+----------------------------------+

mcblasSetPointerMode()
----------------------

::

   mcblasStatus_t
   mcblasSetPocinterMode (mcblasHandle_t句柄，mcblasPocinterMode_t模式)

此函数设置mcBLAS使用的指针模式
库。  *默认* 值是要传递的值
主机上的参考。请参阅上的部分
``mcblasPointerMode_t`` 有关详细信息，请键入。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | 指针模式已设置         |
   |                                    | 成功                     |
   +------------------------------------+----------------------------------+
   |                                    | 库未初始化  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | ``mode`` is not                  |
   |                                    | ``MCBLAS_POINTER_MODE_HOST`` or  |
   |                                    | ``MCBLAS_POINTER_MODE_DEVICE``   |
   +------------------------------------+----------------------------------+

mcblasSetVector()
-----------------

::

   mcblasStatus_t
   mcblasSetVector(int n, int elemSize,
                   const void *x, int incx, void *y, int incy)

此函数从 ``n`` 中的引导程序复制元素 ``x`` 
主机内存空间到 ``y`` GPU内存空间中的矢量。
假定两个向量中的元素的大小为
``elemSize`` 字节。连续存储间距
为 ``incx`` 源向量提供元素 ``x``
和用于 ``incy`` 目标引导程序 ``y``。

因为二维矩阵的列主格式为
假设，如果向量是矩阵的一部分，则为向量增量
等于 ``1`` 访问该矩阵的(部分)列。
同样，使用等于前导尺寸的增量
矩阵的结果是访问该矩阵的(部分)行
矩阵。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasGetVector()
------------------

::

   mcblasStatus_t
   mcblasGetVector(int n, int elemSize,
                   const void *x, int incx, void *y, int incy)

此函数从 ``n`` 中的引导程序复制元素 ``x`` 
GPU内存空间到 ``y`` 主机内存空间中的矢量。
假定两个向量中的元素的大小为
``elemSize`` 字节。连续存储间距
为 ``incx`` 源向量和提供元素
``incy`` 用于目标引导程序 ``y``。

因为二维矩阵的列主格式为
假设，如果向量是矩阵的一部分，则为向量增量
等于 ``1`` 访问该矩阵的(部分)列。
同样，使用等于前导尺寸的增量
矩阵的结果是访问该矩阵的(部分)行
矩阵。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasSetMatrix()
-----------------

::

   mcblasStatus_t
   mcblasSetMatrix(int rows, int cols, int elemSize,
                   const void *A, int lda, void *B, int ldb)

此函数从复制 ``行x Cols`` 元素的磁贴
``A`` 主机内存空间中的矩阵到 ``B`` GPU中的矩阵
内存空间。假定每个元素都需要
``elemSize`` 字节存储和两个矩阵都是
以列主要格式存储，具有的前导维度
``A`` ``B`` 给定的源矩阵和目标矩阵
分别在 ``lda`` 和中 ``ldb``。主要维度
指示已分配矩阵的行数，偶数
如果仅使用其子矩阵。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasGetMatrix()
-----------------

::

   mcblasStatus_t
   mcblasGetMatrix(int rows, int cols, int elemSize,
                   const void *A, int lda, void *B, int ldb)

此函数从复制 ``行x Cols`` 元素的磁贴
``A`` GPU内存空间中的矩阵到 ``B`` 主机中的矩阵
内存空间。假定每个元素都需要
``elemSize`` 字节存储和两个矩阵都是
以列主要格式存储，具有的前导维度
``A`` ``B`` 给定的源矩阵和目标矩阵
分别在 ``lda`` 和中 ``ldb``。主要维度
指示已分配矩阵的行数，偶数
如果仅使用其子矩阵。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasSetVectorAsync()
----------------------

::

   mcblasStatus_t
   mcblasSetVectorAsync(int n, int elemSize, const void *hostPtr, int incx,
                        void *devicePtr, int incy, mcStream_t stream)

此功能与具有相同的功能
``mcblasSetVector()``，数据除外
异步传输(相对于主机)
使用给定的MACA™STREAM参数。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasGetVectorAsync()
----------------------

::

   mcblasStatus_t
   mcblasGetVectorAsync(int n, int elemSize, const void *devicePtr, int incx,
                        void *hostPtr, int incy, mcStream_t stream)

此功能与具有相同的功能
``mcblasGetVector()``，数据除外
异步传输(相对于主机)
使用给定的MACA™STREAM参数。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasSetMatrixAsync()
----------------------           

::

   mcblasStatus_t
   mcblasSetMatrixAsync(int rows, int cols, int elemSize, const void *A,
                        int lda, void *B, int ldb, mcStream_t stream)

此功能与具有相同的功能
``mcblasSetMatrix()``，数据除外
异步传输(相对于主机)
使用给定的MACA™STREAM参数。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | 返回值                    | 含义                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasGetMatrixAsync()
----------------------

::

   mcblasStatus_t
   mcblasGetMatrixAsync(int rows, int cols, int elemSize, const void *A,
                        int lda, void *B, int ldb, mcStream_t stream)

此功能与具有相同的功能
``mcblasGetMatrix()``，数据除外
异步传输(相对于主机)
使用给定的MACA™STREAM参数。

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | 返回值                    | 含义                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | 操作已完成           |
   |                                 | 成功                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | 访问GPU时出错  |
   |                                 | 内存                            |
   +---------------------------------+-----------------------------------+

mcblasSetAtomicsMode()
----------------------

::

   mcblasStatus_t mcblasSetAtomicsMode(mcblasHandlet handle, mcblasAtomicsMode_t mode)

Some routines like mcblas<t>symv and mcblas<t>hemv have an
使用原子化进行累积的替代实现
结果。这种执行情况通常很重要
速度更快，但会产生不严格的结果
两个流程相同。从数学角度讲，这些
不同的结果并不重要，但在调试时
这些差异可能是有偏见的。

此功能允许或禁止在中使用原子
具有替代的所有例程的mcBLAS库
执行。在中未显式指定时
记录任何mcBLAS例程，这意味着这一点
例程没有使用的备用实现
原子球。当雾化模式被禁用时，每个mcBLAS例程
应在不同的照射行程之间产生相同的结果
在同一硬件上使用相同的参数调用时。

缺省初始化的缺省原子模式
``mcblasHandle_t`` 对象为 ``MCBLAS_ATOMICS_NOT_ALLOWED``。
有关详细信息，请参阅类型部分。

================================= =====================================
Return Value                      Meaning
================================= =====================================
``MCBLAS_STATUS_SUCCESS``         已成功设置原子模式
``MCBLAS_STATUS_NOT_INITIALIZED`` 库未初始化
================================= =====================================

mcblasGetAtomicsMode()
----------------------

::

   mcblasStatus_t mcblasGetAtomicsMode(mcblasHandle_t handle, 
                                       mcblasAtomicsMode_t *mode)

此函数查询特定mcBLAS的原子模式
上下文。

缺省初始化的缺省原子模式
``mcblasHandle_t`` 对象为 ``MCBLAS_ATOMICS_NOT_ALLOWED``。
有关详细信息，请参阅类型部分。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | 已查询原子模式     |
   |                                    | 成功                     |
   +------------------------------------+----------------------------------+
   |                                    | 库未初始化  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | 参数 ``mode`` 为NULL  |
   |                                    | 指针                          |
   +------------------------------------+----------------------------------+

mcblasSetMathMode()
-------------------

::

   mcblasStatus_t mcblasSetMathMode(mcblasHandle_t handle, mcblasMath_t mode)

``mcblasSetMathMode`` 使用此功能可以选择
定义的计算精度模式 ``mcblasMath_t``。
允许用户将计算精度模式设置为
它们的逻辑组合(已过时的除外
``MCBLAS_TENSOR_OP_MATH``)。例如，
``mcblasSetMathMode(handle, MCBLAS_DEFAULT_MATH | MCBLAS_MATH_DISALLOW_REDUCED_PRECISION_REDUCTION)``.
请注意，默认的数学模式为
``MCBLAS_DEFAULT_MATH``。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | 返回值                       | 含义                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | 已设置数学模式             |
   |                                    | 成功。                     |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | 模式的值无效     |
   |                                    | 指定。                        |
   +------------------------------------+-----------------------------------+
   |                                    | 库未初始化。  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +------------------------------------+-----------------------------------+

mcblasGetMathMode()
-------------------

::

   mcblasStatus_t mcblasGetMathMode(mcblasHandle_t handle, mcblasMath_t *mode)

此函数返回库使用的数学模式
例程。

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | 返回值                       | 含义                           |
   +====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``         |  已返回数学类型       |
   |                                    |  成功。                    |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | if mode is NULL.                  |
   +------------------------------------+-----------------------------------+
   |                                    |  库未初始化。 |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED`` |                                   |
   +------------------------------------+-----------------------------------+

mcblasSetSmCountTarget() 
-------------------------

目前不支持此例程。

mcblasGetSmCountTarget()
-------------------------

目前不支持此例程。

mcblasLoggerConfigure()
--------------------------

目前不支持此例程。

mcblasGetLoggerCallback()
----------------------------

目前不支持此例程。

mcblasSetLoggerCallback()
---------------------------

目前不支持此例程。


