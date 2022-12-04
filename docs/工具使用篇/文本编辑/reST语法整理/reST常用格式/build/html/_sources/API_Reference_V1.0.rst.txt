Introduction
.............

The mcBLAS library is an implementation of BLAS (Basic Linear
Algebra Subprograms) on top of the CUDA runtime. It
allows the user to access the computational resources of MetaX
Graphics Processing Unit (GPU).

The aim of mcBLAS is to provide:

- functionality similar to Legacy BLAS, adapted to run on GPUs

- high performance robust implementation

Data Layout
============

For maximum compatibility with existing Fortran environments,
the mcBLAS library uses column-major storage, and 1-based
indexing. Since C and C++ use row-major storage, applications
written in these languages can not use the native array
semantics for two-dimensional arrays. Instead, macros or inline
functions should be defined to implement matrices on top of
one-dimensional arrays. For Fortran code ported to C in
mechanical fashion, one may chose to retain 1-based indexing to
avoid the need to transform loops. In this case, the array
index of a matrix element in row “i” and column “j” can be
computed via the following macro

::

   #define IDX2F(i,j,ld) ((((j)-1)*(ld))+((i)-1))

Here, ld refers to the leading dimension of the matrix, which
in the case of column-major storage is the number of rows of
the allocated matrix (even if only a submatrix of it is being
used). For natively written C and C++ code, one would most
likely choose 0-based indexing, in which case the array index
of a matrix element in row “i” and column “j” can be computed
via the following macro

::

   #define IDX2C(i,j,ld) (((j)*(ld))+(i))

Using mcBLAS API
.................

mcBLAS Datatypes
=================

mcblasHandle_t
---------------

The ``mcblasHandle_t`` type is a pointer type to an opaque
structure holding the mcBLAS library context. The mcBLAS
library context must be initialized using ``mcblasCreate()``
and the returned handle must be passed to all subsequent
library function calls. The context should be destroyed at
the end using ``mcblasDestroy()``.

mcblas_int
----------

::

   typedef int32_t mcblas_int;

Specify int by mcBLAS according to the MetaX's hardware.

mcblas_stride
--------------

::

   typedef int64_t mcblas_stride;

Stride between matrices or vectors in strided_batched functions.


mcblas_half
------------

Struct to represent a 16 bit floating-point number;

mcComplex
----------

Class to represent a complex number with single precision real and imaginary parts.

mcDoubleComplex
----------------

Class to represent a complex number with double precision real and imaginary parts.


mcblasStatus_t
---------------

The type is used for function status returns.
All mcBLAS library function calls return their error status ``mcblasStatus_t``.

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | Value                            | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``        | the operation completed          |
   |                                  | successfully                     |
   +----------------------------------+----------------------------------+
   |                                  | the library was not initialized  |
   |``MCBLAS_STATUS_NOT_INITIALIZED`` |                                  |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``   | the resource allocation failed   |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``  | an invalid numerical value was   |
   |                                  | used as an argument              |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_ARCH_MISMATCH``  | an absent device architectural   |
   |                                  | feature is required              |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR``  | an access to GPU memory space    |
   |                                  | failed                           |
   +----------------------------------+----------------------------------+
   |                                  | the GPU program failed to        |
   |``MCBLAS_STATUS_EXECUTION_FAILED``| execute                          |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INTERNAL_ERROR`` | an internal operation failed     |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``  | the feature required is not      |
   |                                  | supported                        |
   +----------------------------------+----------------------------------+

.. list-table:: Table 2-1 Protocol Format
    :widths: 50 50 50 50 50 50 50
    :header-rows: 1

    *
       - Major Version
       - Minor Version
       - Master ID
       - Slave ID
       - Category
       - Command Data
       - Send/Receive
    *
        - b[31:30]
        - b[29:28]
        - b[27:24]
        - b[23:20]
        - b[19:12]
        - b[11:4]
        - b[3:0]


mcblasDataType_t
------------------

The ``mcblasDataType_t`` type is an enumerant to specify the
data precision. It is used when the data reference does not
carry the type itself (e.g void \*)

For example, it is used in the routine ``mcblasSgemmEx``.

.. table:: 
   :widths: grid

   +-----------------+---------------------------------------------------+
   | Value           | Meaning                                           |
   +=================+===================================================+
   | ``MCBLAS_R_16F``| the data type is 16-bit real half precision       |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_16F``| the data type is 16-bit complex half precision    |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_R_16BF``| the data type is 16-bit real bfloat16             |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_C_16BF``| the data type is 16-bit complex bfloat16          |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   |``MCBLAS_R_32F`` | the data type is 32-bit real single precision     |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_32F``| the data type is 32-bit complex single precision  |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_64F``| the data type is 64-bit real double precision     |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_64F``| the data type is 64-bit complex double precision  |
   |                 | floating-point                                    |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_8I`` | the data type is 8-bit real signed integer        |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_8I`` | the data type is 8-bit complex signed integer     |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_8U`` | the data type is 8-bit real unsigned integer      |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_8U`` | the data type is 8-bit complex unsigned integer   |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_R_32I``| the data type is 32-bit real signed integer       |
   +-----------------+---------------------------------------------------+
   | ``MCBLAS_C_32I``| the data type is 32-bit complex signed integer    |
   +-----------------+---------------------------------------------------+

mcblasOperation_t
------------------

The ``mcblasOperation_t`` type indicates which operation
needs to be performed with the dense matrix. Its values
correspond to Fortran characters ``‘N’`` or ``‘n’``
(non-transpose), ``‘T’`` or ``‘t’`` (transpose) and ``‘C’``
or ``‘c’`` (conjugate transpose) that are often used as
parameters to legacy BLAS implementations.

=============== =============================================
Value           Meaning
=============== =============================================
``MCBLAS_OP_N`` the non-transpose operation is selected
``MCBLAS_OP_T`` the transpose operation is selected
``MCBLAS_OP_C`` the conjugate transpose operation is selected
=============== =============================================

mcblasFillMode_t
-----------------

The type indicates which part (lower or upper) of the dense
matrix was filled and consequently should be used by the
function. Its values correspond to Fortran characters
``‘L’`` or ``‘l’`` (lower) and ``‘U’`` or ``‘u’`` (upper)
that are often used as parameters to legacy BLAS
implementations.

========================== ======================================
Value                      Meaning
========================== ======================================
``MCBLAS_FILL_MODE_LOWER`` the lower part of the matrix is filled
``MCBLAS_FILL_MODE_UPPER`` the upper part of the matrix is filled
``MCBLAS_FILL_MODE_FULL``  the full matrix is filled
========================== ======================================

mcblasDiagType_t
------------------

The type indicates whether the main diagonal of the dense
matrix is unity and consequently should not be touched or
modified by the function. Its values correspond to Fortran
characters ``‘N’`` or ``‘n’`` (non-unit) and ``‘U’`` or
``‘u’`` (unit) that are often used as parameters to legacy
BLAS implementations.

======================== =========================================
Value                    Meaning
======================== =========================================
``MCBLAS_DIAG_NON_UNIT`` the matrix diagonal has non-unit elements
``MCBLAS_DIAG_UNIT``     the matrix diagonal has unit elements
======================== =========================================

mcblasSideMode_t
-------------------

The type indicates whether the dense matrix is on the left
or right side in the matrix equation solved by a particular
function. Its values correspond to Fortran characters
``‘L’`` or ``‘l’`` (left) and ``‘R’`` or ``‘r’`` (right)
that are often used as parameters to legacy BLAS
implementations.

===================== ===============================================
Value                 Meaning
===================== ===============================================
``MCBLAS_SIDE_LEFT``  the matrix is on the left side in the equation
``MCBLAS_SIDE_RIGHT`` the matrix is on the right side in the equation
===================== ===============================================

mcblasPointerMode_t
--------------------

The ``mcblasPointerMode_t`` type indicates whether the
scalar values are passed by reference on the host or device.
It is important to point out that if several scalar values
are present in the function call, all of them must conform
to the same single pointer mode. The pointer mode can be set
and retrieved using ``mcblasSetPointerMode()`` and
``mcblasGetPointerMode()`` routines, respectively.

.. table:: 
   :widths: grid

   +--------------------------------+------------------------------------+
   | Value                          | Meaning                            |
   +================================+====================================+
   | ``MCBLAS_POINTER_MODE_HOST``   | the scalars are passed by          |
   |                                | reference on the host              |
   +--------------------------------+------------------------------------+
   | ``MCBLAS_POINTER_MODE_DEVICE`` | the scalars are passed by          |
   |                                | reference on the device            |
   +--------------------------------+------------------------------------+

mcblasAtomicsMode_t
--------------------

The type indicates whether mcBLAS routines which has an
alternate implementation using atomics can be used. The
atomics mode can be set and queried using
``mcblasSetAtomicsMode()`` and ``mcblasGetAtomicsMode()``
and routines, respectively.

============================== ===================================
Value                          Meaning
============================== ===================================
``MCBLAS_ATOMICS_NOT_ALLOWED`` the usage of atomics is not allowed
``MCBLAS_ATOMICS_ALLOWED``     the usage of atomics is allowed
============================== ===================================

mcblasGemmAlgo_t
-------------------

mcblasGemmAlgo_t type is an enumerant to specify the
algorithm for matrix-matrix multiplication on GPU. mcBLAS has the
following algorithm options:

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Value                             | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_GEMM_DEFAULT``           | Apply Heuristics to select the    |
   |                                   | GEMM algorithm                    |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_ALGO0`` to          | Explicitly choose an Algorithm    |
   | ``MCBLAS_GEMM_ALGO23``            | [0,23]. Note: Doesn't have        |
   |                                   | effect on MetaX Ampere            |
   |                                   | architecture GPUs and newer.      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_DEFAULT_TENSOR_OP`` | This mode is deprecated and will  |
   | [DEPRECATED]                      | be removed in a future release.   |
   |                                   | Apply Heuristics to select the    |
   |                                   | GEMM algorithm, while allowing    |
   |                                   | use of reduced precision          |
   |                                   | MCBLAS_COMPUTE_32F_FAST_16F       |
   |                                   | kernels (for backward             |
   |                                   | compatibility).                   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_GEMM_ALGO0_TENSOR_OP``   | Those values are deprecated and   |
   | to                                | will be removed in a future       |
   | ``MCBLAS_GEMM_ALGO15_TENSOR_OP``  | release. Explicitly choose a      |
   | [DEPRECATED]                      | Tensor core GEMM Algorithm        |
   |                                   | [0,15]. Allows use of reduced     |
   |                                   | precision                         |
   |                                   | MCBLAS_COMPUTE_32F_FAST_16F       |
   |                                   | kernels (for backward             |
   |                                   | compatibility). Note: Doesn't     |
   |                                   | have effect on MetaX Ampere       |
   |                                   | architecture GPUs and newer.      |
   +-----------------------------------+-----------------------------------+

mcblasMath_t
-------------

``mcblasMath_t`` enumerate type is used in
``mcblasSetMathMode()`` to choose compute precision modes as
defined below. 

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | Value                            | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_DEFAULT_MATH``          | This is the default and          |
   |                                  | highest-performance mode that    |
   |                                  | uses compute and intermediate    |
   |                                  | storage precisions with at least |
   |                                  | the same number of mantissa and  |
   |                                  | exponent bits as requested.      |
   |                                  | Tensor Cores will be used        |
   |                                  | whenever possible.               |
   +----------------------------------+----------------------------------+
  
mcblasComputeType_t
--------------------

``mcblasComputeType_t`` enumerate type is used in
``mcblasGemmEx`` and ``mcblasLtMatmul`` (including all
batched and strided batched variants) to choose compute
precision modes as defined below.

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | Value                            | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_COMPUTE_16F``           | This is the default and          |
   |                                  | highest-performance mode for     |
   |                                  | 16-bit half precision floating   |
   |                                  | point and all compute and        |
   |                                  | intermediate storage precisions  |
   |                                  | with at least 16-bit half        |
   |                                  | precision. Tensor Cores will be  |
   |                                  | used whenever possible.          |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_16F_PEDANTIC``  | This mode uses 16-bit half       |
   |                                  | precision floating point         |
   |                                  | standardized arithmetic for all  |
   |                                  | phases of calculations and is    |
   |                                  | primarily intended for numerical |
   |                                  | robustness studies, testing, and |
   |                                  | debugging. This mode might not   |
   |                                  | be as performant as the other    |
   |                                  | modes since it disables use of   |
   |                                  | tensor cores.                    |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F``           | This is the default 32-bit       |
   |                                  | single precision floating point  |
   |                                  | and uses compute and             |
   |                                  | intermediate storage precisions  |
   |                                  | of at least 32-bits.             |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_PEDANTIC``  | Uses 32-bit single precision     |
   |                                  | floatin point arithmetic for all |
   |                                  | phases of calculations and also  |
   |                                  | disables algorithmic             |
   |                                  | optimizations such as Gaussian   |
   |                                  | complexity reduction (3M).       |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_16F``  | Allows the library to use Tensor |
   |                                  | Cores with automatic             |
   |                                  | down-conversion and 16-bit       |
   |                                  | half-precision compute for       |
   |                                  | 32-bit input and output          |
   |                                  | matrices.                        |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_16BF`` | Allows the library to use Tensor |
   |                                  | Cores with automatic             |
   |                                  | down-convesion and bfloat16      |
   |                                  | compute for 32-bit input and     |
   |                                  | output matrices.                 |   
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32F_FAST_TF32`` | Allows the library to use Tensor |
   |                                  | Cores with TF32 compute for      |
   |                                  | 32-bit input and output          |
   |                                  | matrices.                        |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_64F``           | This is the default 64-bit       |
   |                                  | double precision floating point  |
   |                                  | and uses compute and             |
   |                                  | intermediate storage precisions  |
   |                                  | of at least 64-bits.             |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_64F_PEDANTIC``  | Uses 64-bit double precision     |
   |                                  | floatin point arithmetic for all |
   |                                  | phases of calculations and also  |
   |                                  | disables algorithmic             |
   |                                  | optimizations such as Gaussian   |
   |                                  | complexity reduction (3M).       |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32I``           | This is the default 32-bit       |
   |                                  | integer mode and uses compute    |
   |                                  | and intermediate storage         |
   |                                  | precisions of at least 32-bits.  |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_COMPUTE_32I_PEDANTIC``  | Uses 32-bit integer arithmetic   |
   |                                  | for all phases of calculations.  |
   +----------------------------------+----------------------------------+

mcBLAS Helper Functions
=======================

mcblasCreate()
--------------

::

   mcblasStatus_t
   mcblasCreate(mcblasHandle_t *handle)

This function initializes the mcBLAS library and creates a
handle to an opaque structure holding the mcBLAS library
context. It allocates hardware resources on the host and
device and must be called prior to making any other mcBLAS
library calls. The mcBLAS library context is tied to the
current MACA device. To use the library on multiple devices,
one mcBLAS handle needs to be created for each device.
Furthermore, for a given device, multiple mcBLAS handles
with different configurations can be created. Because
``mcblasCreate()`` allocates some internal resources and the
release of those resources by calling ``mcblasDestroy()``
will implicitly call ``mcblasDeviceSynchronize()``, it is
recommended to minimize the number of
``mcblasCreate()/mcblasDestroy()`` occurrences. For
multi-threaded applications that use the same device from
different threads, the recommended programming model is to
create one mcBLAS handle per thread and use that mcBLAS
handle for the entire life of the thread.

.. table:: 
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------------+
   | Return Value                      | Meaning                                 |
   +===================================+=========================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the initialization succeeded            |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the MACA™ Runtime initialization failed |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the resources could not be allocated    |
   +-----------------------------------+-----------------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | ``handle`` == NULL                      |
   +-----------------------------------+-----------------------------------------+

mcblasDestroy()
---------------

::

   mcblasStatus_t
   mcblasDestroy(mcblasHandle_t handle)

This function releases hardware resources used by the mcBLAS
library. This function is usually the last call with a
particular handle to the mcBLAS library. Because
``mcblasCreate()`` allocates some internal resources and the
release of those resources by calling ``mcblasDestroy()``
will implicitly call ``mcblasDeviceSynchronize()``, it is
recommended to minimize the number of
``mcblasCreate()/mcblasDestroy()`` occurrences.

================================= ===============================
Return Value                      Meaning
================================= ===============================
``MCBLAS_STATUS_SUCCESS``         the shut down succeeded
``MCBLAS_STATUS_NOT_INITIALIZED`` the library was not initialized
================================= ===============================
        
mcblasGetVersion()
------------------    

::

   mcblasStatus_t
   mcblasGetVersion(mcblasHandle_t handle, int *version)

This function returns the version number of the mcBLAS
library.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the provided storage for library  |
   |                                 | version number is not initialized |
   |                                 | (NULL)                            |
   +---------------------------------+-----------------------------------+

mcblasGetProperty()
-------------------


::

   mcblasStatus_t
   mcblasGetProperty(libraryPropertyType type, int *value)

This function returns the value of the requested property in
memory pointed to by value. Refer to ``libraryPropertyType``
for supported types.

.. table:: 
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Return Value                      | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | The operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | Invalid type value                |
   |                                   |                                   |
   |                                   | -  If invalid ``type`` value or   |
   |                                   |                                   |
   |                                   | -  ``value`` == NULL              |
   +-----------------------------------+-----------------------------------+

mcblasGetStatusName()
---------------------

::

   const char* mcblasGetStatusName(mcblasStatus_t status)

This function returns the string representation of a given
status.

====================== ===========================================
Return Value           Meaning
====================== ===========================================
NULL-terminated string The string representation of the ``status``
====================== ===========================================

mcblasGetStatusString()
-----------------------

::

   const char* mcblasGetStatusString(mcblasStatus_t status)

This function returns the description string for a given
status.

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

This function sets the mcBLAS library stream, which will be
used to execute all subsequent calls to the mcBLAS library
functions. If the mcBLAS library stream is not set, all
kernels use the *default* ``NULL`` stream. In particular,
this routine can be used to change the stream between kernel
launches and then to reset the mcBLAS library stream back to
``NULL``. Additionally this function unconditionally resets
the mcBLAS library workspace back to the default workspace
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

This function sets the mcBLAS library workspace to a
user-owned device buffer, which will be used to execute all
subsequent calls to the mcBLAS library functions (on the
currently set stream). If the mcBLAS library workspace is
not set, all kernels will use the default workspace pool
allocated during the mcBLAS context creation. In particular,
this routine can be used to change the workspace between
kernel launches. The workspace pointer has to be aligned to
at least 256 bytes, otherwise
``MCBLAS_STATUS_INVALID_VALUE`` error is returned. The
``mcblasSetStream()`` function unconditionally resets the
mcBLAS library workspace back to the default workspace pool.
Too small ``workspaceSizeInBytes`` may cause some routines
to fail with ``MCBLAS_STATUS_ALLOC_FAILED`` error returned
or cause large regressions in performance. Workspace size
equal to or larger than 16KiB is enough to prevent
``MCBLAS_STATUS_ALLOC_FAILED`` error, while a larger
workspace can provide performance benefits for some
routines. Recommended size of user-provided workspace is at
least 4MiB (to match mcBLAS’ default workspace pool).

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | Return Value                       | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the stream was set successfully   |
   +------------------------------------+-----------------------------------+
   |                                    | the library was not initialized   |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | the ``workspace`` pointer wasn't  |
   |                                    | aligned to at least 256 bytes     |
   +------------------------------------+-----------------------------------+

mcblasGetStream()
-----------------

::

   mcblasStatus_t
   mcblasGetStream(mcblasHandle_t handle, mcStream_t *streamId)

This function gets the mcBLAS library stream, which is being
used to execute all calls to the mcBLAS library functions.
If the mcBLAS library stream is not set, all kernels use the
*default*\ ``NULL`` stream.

================================= ====================================
Return Value                      Meaning
================================= ====================================
``MCBLAS_STATUS_SUCCESS``         the stream was returned successfully
``MCBLAS_STATUS_NOT_INITIALIZED`` the library was not initialized
``MCBLAS_STATUS_INVALID_VALUE``   ``streamId`` == NULL
================================= ====================================

mcblasGetPointerMode()
----------------------

::

   mcblasStatus_t
   mcblasGetPointerMode(mcblasHandle_t handle, mcblasPointerMode_t *mode)

This function obtains the pointer mode used by the mcBLAS
library. Please see the section on the
``mcblasPointerMode_t`` type for more details.

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the pointer mode was obtained    |
   |                                    | successfully                     |
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
   mcblasSetPointerMode(mcblasHandle_t handle, mcblasPointerMode_t mode)

This function sets the pointer mode used by the mcBLAS
library. The *default* is for the values to be passed by
reference on the host. Please see the section on the
``mcblasPointerMode_t`` type for more details.

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the pointer mode was set         |
   |                                    | successfully                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
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

This function copies ``n`` elements from a vector ``x`` in
host memory space to a vector ``y`` in GPU memory space.
Elements in both vectors are assumed to have a size of
``elemSize`` bytes. The storage spacing between consecutive
elements is given by ``incx`` for the source vector ``x``
and by ``incy`` for the destination vector ``y``.

Since column-major format for two-dimensional matrices is
assumed, if a vector is part of a matrix, a vector increment
equal to ``1`` accesses a (partial) column of that matrix.
Similarly, using an increment equal to the leading dimension
of the matrix results in accesses to a (partial) row of that
matrix.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasGetVector()
------------------

::

   mcblasStatus_t
   mcblasGetVector(int n, int elemSize,
                   const void *x, int incx, void *y, int incy)

This function copies ``n`` elements from a vector ``x`` in
GPU memory space to a vector ``y`` in host memory space.
Elements in both vectors are assumed to have a size of
``elemSize`` bytes. The storage spacing between consecutive
elements is given by ``incx`` for the source vector and
``incy`` for the destination vector ``y``.

Since column-major format for two-dimensional matrices is
assumed, if a vector is part of a matrix, a vector increment
equal to ``1`` accesses a (partial) column of that matrix.
Similarly, using an increment equal to the leading dimension
of the matrix results in accesses to a (partial) row of that
matrix.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasSetMatrix()
-----------------

::

   mcblasStatus_t
   mcblasSetMatrix(int rows, int cols, int elemSize,
                   const void *A, int lda, void *B, int ldb)

This function copies a tile of ``rows x cols`` elements from
a matrix ``A`` in host memory space to a matrix ``B`` in GPU
memory space. It is assumed that each element requires
storage of ``elemSize`` bytes and that both matrices are
stored in column-major format, with the leading dimension of
the source matrix ``A`` and destination matrix ``B`` given
in ``lda`` and ``ldb``, respectively. The leading dimension
indicates the number of rows of the allocated matrix, even
if only a submatrix of it is being used.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
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

This function copies a tile of ``rows x cols`` elements from
a matrix ``A`` in GPU memory space to a matrix ``B`` in host
memory space. It is assumed that each element requires
storage of ``elemSize`` bytes and that both matrices are
stored in column-major format, with the leading dimension of
the source matrix ``A`` and destination matrix ``B`` given
in ``lda`` and ``ldb``, respectively. The leading dimension
indicates the number of rows of the allocated matrix, even
if only a submatrix of it is being used.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasSetVectorAsync()
----------------------

::

   mcblasStatus_t
   mcblasSetVectorAsync(int n, int elemSize, const void *hostPtr, int incx,
                        void *devicePtr, int incy, mcStream_t stream)

This function has the same functionality as
``mcblasSetVector()``, with the exception that the data
transfer is done asynchronously (with respect to the host)
using the given MACA™ stream parameter.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasGetVectorAsync()
----------------------

::

   mcblasStatus_t
   mcblasGetVectorAsync(int n, int elemSize, const void *devicePtr, int incx,
                        void *hostPtr, int incy, mcStream_t stream)

This function has the same functionality as
``mcblasGetVector()``, with the exception that the data
transfer is done asynchronously (with respect to the host)
using the given MACA™ stream parameter.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``incx``,          |
   |                                 | ``incy``, ``elemSize<=0``         |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasSetMatrixAsync()
----------------------           

::

   mcblasStatus_t
   mcblasSetMatrixAsync(int rows, int cols, int elemSize, const void *A,
                        int lda, void *B, int ldb, mcStream_t stream)

This function has the same functionality as
``mcblasSetMatrix()``, with the exception that the data
transfer is done asynchronously (with respect to the host)
using the given MACA™ stream parameter.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasGetMatrixAsync()
----------------------

::

   mcblasStatus_t
   mcblasGetMatrixAsync(int rows, int cols, int elemSize, const void *A,
                        int lda, void *B, int ldb, mcStream_t stream)

This function has the same functionality as
``mcblasGetMatrix()``, with the exception that the data
transfer is done asynchronously (with respect to the host)
using the given MACA™ stream parameter.

.. table:: 
   :widths: grid
   :align: left

   +---------------------------------+-----------------------------------+
   | Return Value                    | Meaning                           |
   +=================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``       | the operation completed           |
   |                                 | successfully                      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE`` | the parameters ``rows, cols<0``   |
   |                                 | or ``elemSize, lda, ldb<=0``      |
   +---------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_MAPPING_ERROR`` | there was an error accessing GPU  |
   |                                 | memory                            |
   +---------------------------------+-----------------------------------+

mcblasSetAtomicsMode()
----------------------

::

   mcblasStatus_t mcblasSetAtomicsMode(mcblasHandlet handle, mcblasAtomicsMode_t mode)

Some routines like mcblas<t>symv and mcblas<t>hemv have an
alternate implementation that use atomics to cumulate
results. This implementation is generally significantly
faster but can generate results that are not strictly
identical from one run to the others. Mathematically, those
different results are not significant but when debugging
those differences can be prejudicial.

This function allows or disallows the usage of atomics in
the mcBLAS library for all routines which have an alternate
implementation. When not explicitly specified in the
documentation of any mcBLAS routine, it means that this
routine does not have an alternate implementation that use
atomics. When atomics mode is disabled, each mcBLAS routine
should produce the same results from one run to the other
when called with identical parameters on the same Hardware.

The default atomics mode of default initialized
``mcblasHandle_t`` object is ``MCBLAS_ATOMICS_NOT_ALLOWED``.
Please see the section on the type for more details.

================================= =====================================
Return Value                      Meaning
================================= =====================================
``MCBLAS_STATUS_SUCCESS``         the atomics mode was set successfully
``MCBLAS_STATUS_NOT_INITIALIZED`` the library was not initialized
================================= =====================================

mcblasGetAtomicsMode()
----------------------

::

   mcblasStatus_t mcblasGetAtomicsMode(mcblasHandle_t handle, 
                                       mcblasAtomicsMode_t *mode)

This function queries the atomic mode of a specific mcBLAS
context.

The default atomics mode of default initialized
``mcblasHandle_t`` object is ``MCBLAS_ATOMICS_NOT_ALLOWED``.
Please see the section on the type for more details.

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+----------------------------------+
   | Return Value                       | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the atomics mode was queried     |
   |                                    | successfully                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | the argument ``mode`` is a NULL  |
   |                                    | pointer                          |
   +------------------------------------+----------------------------------+

mcblasSetMathMode()
-------------------

::

   mcblasStatus_t mcblasSetMathMode(mcblasHandle_t handle, mcblasMath_t mode)

The ``mcblasSetMathMode`` function enables you to choose the
compute precision modes as defined by ``mcblasMath_t``.
Users are allowed to set the compute precision mode as a
logical combination of them (except the deprecated
``MCBLAS_TENSOR_OP_MATH``). For example,
``mcblasSetMathMode(handle, MCBLAS_DEFAULT_MATH | MCBLAS_MATH_DISALLOW_REDUCED_PRECISION_REDUCTION)``.
Please note that the default math mode is
``MCBLAS_DEFAULT_MATH``.

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | Return Value                       | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the math mode was set             |
   |                                    | successfully.                     |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | an invalid value for mode was     |
   |                                    | specified.                        |
   +------------------------------------+-----------------------------------+
   |                                    | the library was not initialized.  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +------------------------------------+-----------------------------------+

mcblasGetMathMode()
-------------------

::

   mcblasStatus_t mcblasGetMathMode(mcblasHandle_t handle, mcblasMath_t *mode)

This function returns the math mode used by the library
routines.

.. table:: 
   :widths: grid
   :align: left

   +------------------------------------+-----------------------------------+
   | Return Value                       | Meaning                           |
   +====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``         |  the math type was returned       |
   |                                    |  successfully.                    |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | if mode is NULL.                  |
   +------------------------------------+-----------------------------------+
   |                                    |  the library was not initialized. |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED`` |                                   |
   +------------------------------------+-----------------------------------+

mcblasSetSmCountTarget() 
-------------------------

This routine is not supported now.

mcblasGetSmCountTarget()
-------------------------

This routine is not supported now.

mcblasLoggerConfigure()
--------------------------

This routine is not supported now.

mcblasGetLoggerCallback()
----------------------------

This routine is not supported now.

mcblasSetLoggerCallback()
---------------------------

This routine is not supported now.

mcBLAS Level-1 Functions
==========================

In this chapter we describe the Level-1 Basic Linear Algebra
Subprograms (BLAS1) functions that perform scalar and vector
based operations. We will use abbreviations <*type*> for type
and <*t*> for the corresponding short type to make a more
concise and clear presentation of the implemented functions.
Unless otherwise specified <*type*> and <*t*> have the
following meanings:

=================== ========== ========================
<type>              <t>        Meaning
=================== ========== ========================
``float``           ‘s’ or ‘S’ real single-precision
``double``          ‘d’ or ‘D’ real double-precision
``mcComplex``       ‘c’ or ‘C’ complex single-precision
``mcDoubleComplex`` ‘z’ or ‘Z’ complex double-precision
=================== ========== ========================

When the parameters and returned values of the function differ,
which sometimes happens for complex input, the <t> can also
have the following meanings ‘Sc’, ‘Cs’, ‘Dz’ and ‘Zd’.

The abbreviation **Re**\ (.) and **Im**\ (.) will stand for the
real and imaginary part of a number, respectively. Since
imaginary part of a real number does not exist, we will
consider it to be zero and can usually simply discard it from
the equation where it is being used. Also, the
:math:`\bar{\alpha}`
will denote the complex conjugate of
:math:`\alpha`
.
In general throughout the documentation, the lower case Greek
symbols :math:`\alpha`
and :math:`\beta`
will denote scalars, lower case English letters in bold type
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
will denote vectors and capital English letters
:math:`A`
, :math:`B`
and :math:`C`
will denote matrices.

mcblasI<t>amax()
-----------------

::

   mcblasStatus_t mcblasIsamax(mcblasHandle_t handle, int n,
                                 const float *x, int incx, int *result)
   mcblasStatus_t mcblasIdamax(mcblasHandle_t handle, int n,
                                 const double *x, int incx, int *result)
   mcblasStatus_t mcblasIcamax(mcblasHandle_t handle, int n,
                                 const mcComplex *x, int incx, int *result)
   mcblasStatus_t mcblasIzamax(mcblasHandle_t handle, int n,
                                 const mcDoubleComplex *x, int incx, int *result)

This function finds the (smallest) index of the element of
the maximum magnitude. Hence, the result is the first
:math:`i`
such that
:math:`\left| \mathbf{Im}\left( {x\lbrack j\rbrack} \right) \middle| + \middle| \mathbf{Re}\left( {x\lbrack j\rbrack} \right) \right|`
is maximum for
:math:`i = 1,\ldots,n`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{ incx}`
. Notice that the last equation reflects 1-based indexing
used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vector ``x``.      |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | elements.              |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | result | host or device | output | the resulting index,   |
   |        |                |        | which is ``0`` if      |
   |        |                |        | ``n,incx<=0``.         |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``           | the operation completed           |
   |                                     | successfully                      |
   +-------------------------------------+-----------------------------------+
   |                                     | the library was not initialized   |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   |                                   |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``      | the reduction buffer could not    |
   |                                     | be allocated                      |
   +-------------------------------------+-----------------------------------+
   |                                     | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``  | the GPU                           |
   +-------------------------------------+-----------------------------------+

mcblasI<t>amin()
-----------------

::

   mcblasStatus_t mcblasIsamin(mcblasHandle_t handle, int n,
                               const float *x, int incx, int *result)
   mcblasStatus_t mcblasIdamin(mcblasHandle_t handle, int n,
                               const double *x, int incx, int *result)
   mcblasStatus_t mcblasIcamin(mcblasHandle_t handle, int n,
                               const mcComplex *x, int incx, int *result)
   mcblasStatus_t mcblasIzamin(mcblasHandle_t handle, int n,
                               const mcDoubleComplex *x, int incx, int *result)

This function finds the (smallest) index of the element of
the minimum magnitude. Hence, the result is the first
:math:`i`
such that
:math:`\left| \mathbf{Im}\left( {x\lbrack j\rbrack} \right) \middle| + \middle| \mathbf{Re}\left( {x\lbrack j\rbrack} \right) \right|`
is minimum for
:math:`i = 1,\ldots,n`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incx}`.
Notice that the last equation reflects 1-based indexing used
for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vector ``x``.      |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | elements.              |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | result | host or device | output | the resulting index,   |
   |        |                |        | which is ``0`` if      |
   |        |                |        | ``n,incx<=0``.         |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the reduction buffer could not be allocated |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>asum()
-----------------

::

   mcblasStatus_t   mcblasSasum(mcblasHandle_t handle, int n,
                                const float           *x, int incx, float  *result)
   mcblasStatus_t   mcblasDasum(mcblasHandle_t handle, int n,
                                const double          *x, int incx, double *result)
   mcblasStatus_t  mcblasScasum(mcblasHandle_t handle, int n,
                                const mcComplex       *x, int incx, float  *result)
   mcblasStatus_t  mcblasDzasum(mcblasHandle_t handle, int n,
                                const mcDoubleComplex *x, int incx, double *result)

This function computes the sum of the absolute values of the
elements of vector ``x``. Hence, the result is
:math:`\left. \sum_{i = 1}^{n} \middle| \mathbf{Im}\left( {x\lbrack j\rbrack} \right) \middle| + \middle| \mathbf{Re}\left( {x\lbrack j\rbrack} \right) \right|`
where
:math:`j = 1 + \left( {i - 1} \right)*\text{incx}`
. Notice that the last equation reflects 1-based indexing
used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vector ``x``.      |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | elements.              |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | result | host or device | output | the resulting index,   |
   |        |                |        | which is ``0.0`` if    |
   |        |                |        | ``n,incx<=0``.         |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the reduction buffer could not be allocated |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>axpy()
-----------------

::

   mcblasStatus_t mcblasSaxpy(mcblasHandle_t handle, int n,
                              const float           *alpha,
                              const float           *x, int incx,
                              float                 *y, int incy)
   mcblasStatus_t mcblasDaxpy(mcblasHandle_t handle, int n,
                              const double          *alpha,
                              const double          *x, int incx,
                              double                *y, int incy)
   mcblasStatus_t mcblasCaxpy(mcblasHandle_t handle, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *x, int incx,
                              mcComplex             *y, int incy)
   mcblasStatus_t mcblasZaxpy(mcblasHandle_t handle, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *x, int incx,
                              mcDoubleComplex       *y, int incy)

This function multiplies the vector ``x`` by the scalar
:math:`\alpha`
and adds it to the vector ``y`` overwriting the latest
vector with the result. Hence, the performed operation is
:math:`\mathbf{y}\lbrack j\rbrack = \alpha \times \mathbf{x}\lbrack k\rbrack + \mathbf{y}\lbrack j\rbrack`
for :math:`i = 1,\ldots,n`
,
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid
      
   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vector ``x`` and   |
   |        |                |        | ``y``.                 |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | in/out | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>copy()
----------------

::

   mcblasStatus_t mcblasScopy(mcblasHandle_t handle, int n,
                              const float           *x, int incx,
                              float                 *y, int incy)
   mcblasStatus_t mcblasDcopy(mcblasHandle_t handle, int n,
                              const double          *x, int incx,
                              double                *y, int incy)
   mcblasStatus_t mcblasCcopy(mcblasHandle_t handle, int n,
                              const mcComplex       *x, int incx,
                              mcComplex             *y, int incy)
   mcblasStatus_t mcblasZcopy(mcblasHandle_t handle, int n,
                              const mcDoubleComplex *x, int incx,
                              mcDoubleComplex       *y, int incy)

This function copies the vector ``x`` into the vector ``y``.
Hence, the performed operation is
:math:`\mathbf{y}\lbrack j\rbrack = \mathbf{x}\lbrack k\rbrack`
for :math:`i = 1,\ldots,n`
,
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

====== ====== ====== =================================================
Param. Memory In/out Meaning
====== ====== ====== =================================================
handle        input  handle to the mcBLAS library context.
n             input  number of elements in the vector ``x`` and ``y``.
x      device input  <type> vector with ``n`` elements.
incx          input  stride between consecutive elements of ``x``.
y      device output <type> vector with ``n`` elements.
incy          input  stride between consecutive elements of ``y``.
====== ====== ====== =================================================

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>dot()
---------------

::

   mcblasStatus_t mcblasSdot (mcblasHandle_t handle, int n,
                              const float           *x, int incx,
                              const float           *y, int incy,
                              float           *result)
   mcblasStatus_t mcblasDdot (mcblasHandle_t handle, int n,
                              const double          *x, int incx,
                              const double          *y, int incy,
                              double          *result)
   mcblasStatus_t mcblasCdotu(mcblasHandle_t handle, int n,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *result)
   mcblasStatus_t mcblasCdotc(mcblasHandle_t handle, int n,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *result)
   mcblasStatus_t mcblasZdotu(mcblasHandle_t handle, int n,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex *result)
   mcblasStatus_t mcblasZdotc(mcblasHandle_t handle, int n,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex       *result)

This function computes the dot product of vectors ``x`` and
``y``. Hence, the result is
:math:`\sum_{i = 1}^{n}\left( {\mathbf{x}\lbrack k\rbrack \times \mathbf{y}\lbrack j\rbrack} \right)`
where
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that in the first equation the conjugate of the
element of vector x should be used if the function name ends
in character ‘c’ and that the last two equations reflect
1-based indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid
      
   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vectors ``x`` and  |
   |        |                |        | ``y``.                 |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | result | host or device | output | the resulting dot      |
   |        |                |        | product, which is      |
   |        |                |        | ``0.0`` if ``n<=0``.   |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the reduction buffer could not be allocated |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>nrm2()
----------------

::

   mcblasStatus_t  mcblasSnrm2(mcblasHandle_t handle, int n,
                               const float           *x, int incx, float  *result)
   mcblasStatus_t  mcblasDnrm2(mcblasHandle_t handle, int n,
                               const double          *x, int incx, double *result)
   mcblasStatus_t mcblasScnrm2(mcblasHandle_t handle, int n,
                               const mcComplex       *x, int incx, float  *result)
   mcblasStatus_t mcblasDznrm2(mcblasHandle_t handle, int n,
                               const mcDoubleComplex *x, int incx, double *result)

This function computes the Euclidean norm of the vector
``x``. The code uses a multiphase model of accumulation to
avoid intermediate underflow and overflow, with the result
being equivalent to
:math:`\sqrt{\sum_{i = 1}^{n}\left( {\mathbf{x}\lbrack j\rbrack \times \mathbf{x}\lbrack j\rbrack} \right)}`
where
:math:`j = 1 + \left( {i - 1} \right)*\text{incx}`
in exact arithmetic. Notice that the last equation reflects
1-based indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vector ``x``.      |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | result | host or device | output | the resulting norm,    |
   |        |                |        | which is ``0.0`` if    |
   |        |                |        | ``n,incx<=0``.         |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the reduction buffer could not be allocated |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>rot()
---------------

::

   mcblasStatus_t  mcblasSrot(mcblasHandle_t handle, int n,
                              float           *x, int incx,
                              float           *y, int incy,
                              const float  *c, const float           *s)
   mcblasStatus_t  mcblasDrot(mcblasHandle_t handle, int n,
                              double          *x, int incx,
                              double          *y, int incy,
                              const double *c, const double          *s)
   mcblasStatus_t  mcblasCrot(mcblasHandle_t handle, int n,
                              mcComplex       *x, int incx,
                              mcComplex       *y, int incy,
                              const float  *c, const mcComplex       *s)
   mcblasStatus_t mcblasCsrot(mcblasHandle_t handle, int n,
                              mcComplex       *x, int incx,
                              mcComplex       *y, int incy,
                              const float  *c, const float           *s)
   mcblasStatus_t  mcblasZrot(mcblasHandle_t handle, int n,
                              mcDoubleComplex *x, int incx,
                              mcDoubleComplex *y, int incy,
                              const double *c, const mcDoubleComplex *s)
   mcblasStatus_t mcblasZdrot(mcblasHandle_t handle, int n,
                              mcDoubleComplex *x, int incx,
                              mcDoubleComplex *y, int incy,
                              const double *c, const double          *s)

This function applies Givens rotation matrix (i.e., rotation
in the x,y plane counter-clockwise by angle defined by
cos(alpha)=c, sin(alpha)=s):

:math:`G = \begin{pmatrix}
c & s \\
{- s} & c \\
\end{pmatrix}`
to vectors ``x`` and ``y``.

Hence, the result is
:math:`\mathbf{x}\lbrack k\rbrack = c \times \mathbf{x}\lbrack k\rbrack + s \times \mathbf{y}\lbrack j\rbrack`
and
:math:`\mathbf{y}\lbrack j\rbrack = - s \times \mathbf{x}\lbrack k\rbrack + c \times \mathbf{y}\lbrack j\rbrack`
where
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of elements in  |
   |        |                |        | the vectors ``x`` and  |
   |        |                |        | ``y``.                 |
   +--------+----------------+--------+------------------------+
   | x      | device         | in/out | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | in/out | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | c      | host or device | input  | cosine element of the  |
   |        |                |        | rotation matrix.       |
   +--------+----------------+--------+------------------------+
   | s      | host or device | input  | sine element of the    |
   |        |                |        | rotation matrix.       |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>rotg()
----------------

::

   mcblasStatus_t mcblasSrotg(mcblasHandle_t handle,
                              float           *a, float           *b,
                              float  *c, float           *s)
   mcblasStatus_t mcblasDrotg(mcblasHandle_t handle,
                              double          *a, double          *b,
                              double *c, double          *s)
   mcblasStatus_t mcblasCrotg(mcblasHandle_t handle,
                              mcComplex       *a, mcComplex       *b,
                              float  *c, mcComplex       *s)
   mcblasStatus_t mcblasZrotg(mcblasHandle_t handle,
                              mcDoubleComplex *a, mcDoubleComplex *b,
                              double *c, mcDoubleComplex *s)

This function constructs the Givens rotation matrix

.. math::
   G = \begin{pmatrix}
   c & s \\
   {- s} & c \\
   \end{pmatrix}

that zeros out the second entry of a
:math:`2 \times 1`
vector
:math:`\left( {a,b} \right)^{T}`
.
Then, for real numbers we can write

.. math::
   \begin{pmatrix}
   c & s \\
   {- s} & c \\
   \end{pmatrix}\begin{pmatrix}
   a \\
   b \\
   \end{pmatrix} = \begin{pmatrix}
   r \\
   0 \\
   \end{pmatrix}

where :math:`c^{2} + s^{2} = 1`
and :math:`r = a^{2} + b^{2}`
. The parameters :math:`a`
and :math:`b`
are overwritten with :math:`r`
and :math:`z`
, respectively. The value of :math:`z`
is such that :math:`c`
and :math:`s`
may be recovered using the following rules:

.. math::
   \left( {c,s} \right) = \begin{cases}
   \left( {\sqrt{1 - z^{2}},z} \right) & {\text{if}\left| z \middle| < 1 \right.} \\
   \left( {0.0,1.0} \right) & {\text{if}\left| z \middle| = 1 \right.} \\
   \left( 1/z,\sqrt{1 - z^{2}} \right) & {\text{if}\left| z \middle| > 1 \right.} \\
   \end{cases}

For complex numbers we can write

.. math::
   \begin{pmatrix}
   c & s \\
   {- \bar{s}} & c \\
   \end{pmatrix}\begin{pmatrix}
   a \\
   b \\
   \end{pmatrix} = \begin{pmatrix}
   r \\
   0 \\
   \end{pmatrix}

where
:math:`c^{2} + \left( {\bar{s} \times s} \right) = 1`
and
:math:`r = \frac{a}{|a|} \times \parallel \left( {a,b} \right)^{T} \parallel_{2}`
with
:math:`\parallel \left( {a,b} \right)^{T} \parallel_{2} = \sqrt{\left| a|^{2} + \middle| b|^{2} \right.}`
for :math:`a \neq 0`
and :math:`r = b`
for :math:`a = 0`
. Finally, the parameter :math:`a`
is overwritten with :math:`r`
on exit.

.. table:: 
   :widths: grid

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | a               | host or device  | in/out          | <type> scalar   |
   |                 |                 |                 | that is         |
   |                 |                 |                 | overwritten     |
   |                 |                 |                 | with :math:`r`. |
   +-----------------+-----------------+-----------------+-----------------+
   | b               | host or device  | in/out          | <type> scalar   |
   |                 |                 |                 | that is         |
   |                 |                 |                 | overwritten     |
   |                 |                 |                 | with            |
   |                 |                 |                 | :math:`z`.      |
   +-----------------+-----------------+-----------------+-----------------+
   | c               | host or device  | output          | cosine element  |
   |                 |                 |                 | of the rotation |
   |                 |                 |                 | matrix.         |
   +-----------------+-----------------+-----------------+-----------------+
   | s               | host or device  | output          | sine element of |
   |                 |                 |                 | the rotation    |
   |                 |                 |                 | matrix.         |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>rotm()
----------------

::

   mcblasStatus_t mcblasSrotm(mcblasHandle_t handle, int n, float  *x, int incx,
                              float  *y, int incy, const float*  param)
   mcblasStatus_t mcblasDrotm(mcblasHandle_t handle, int n, double *x, int incx,
                              double *y, int incy, const double* param)

This function applies the modified Givens transformation

.. math::
   H = \begin{pmatrix}
   h_{11} & h_{12} \\
   h_{21} & h_{22} \\
   \end{pmatrix}
   
to vectors ``x`` and ``y``.

Hence, the result is
:math:`\mathbf{x}\lbrack k\rbrack = h_{11} \times \mathbf{x}\lbrack k\rbrack + h_{12} \times \mathbf{y}\lbrack j\rbrack`
and
:math:`\mathbf{y}\lbrack j\rbrack = h_{21} \times \mathbf{x}\lbrack k\rbrack + h_{22} \times \mathbf{y}\lbrack j\rbrack`
where
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.
The elements , , and of matrix :math:`H`
are stored in ``param[1]``, ``param[2]``, ``param[3]`` and
``param[4]``, respectively. The ``flag=param[0]`` defines
the following predefined values for the matrix
:math:`H`
entries

	+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+
	| ``flag=-1.0``                                                               | ``flag= 0.0``                                                               | ``flag= 1.0``                                                               | ``flag=-2.0``                                                               |
	+=============================================================================+=============================================================================+=============================================================================+=============================================================================+
	| :math:`\begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix}`    | :math:`\begin{pmatrix} 1.0 & h_{12} \\ h_{21} &1.0 \end{pmatrix}`           | :math:`\begin{pmatrix} h_{11} & 1.0 \\ -1.0& h_{22} \end{pmatrix}`          | :math:`\begin{pmatrix} 1.0 & 0.0 \\ 0.0 & 1.0\end{pmatrix}`                 |
	+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Notice that the values -1.0, 0.0 and 1.0 implied by the flag
are not stored in param.

.. table::
   :widths: grid

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | n               |                 | input           | number of       |
   |                 |                 |                 | elements in the |
   |                 |                 |                 | vectors ``x``   |
   |                 |                 |                 | and ``y``.      |
   +-----------------+-----------------+-----------------+-----------------+
   | x               | device          | in/out          | <type> vector   |
   |                 |                 |                 | with ``n``      |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | incx            |                 | input           | stride between  |
   |                 |                 |                 | consecutive     |
   |                 |                 |                 | elements of     |
   |                 |                 |                 | ``x``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | y               | device          | in/out          | <type> vector   |
   |                 |                 |                 | with ``n``      |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | incy            |                 | input           | stride between  |
   |                 |                 |                 | consecutive     |
   |                 |                 |                 | elements of     |
   |                 |                 |                 | ``y``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | param           | host or device  | input           | <type> vector   |
   |                 |                 |                 | of 5 elements,  |
   |                 |                 |                 | where           |
   |                 |                 |                 | ``param[0]``    |
   |                 |                 |                 | and             |
   |                 |                 |                 | ``param[1-4]``  |
   |                 |                 |                 | contain the     |
   |                 |                 |                 | flag and matrix |
   |                 |                 |                 | :math:`H`.      |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>rotmg()
-----------------

::

   mcblasStatus_t mcblasSrotmg(mcblasHandle_t handle, float  *d1, float  *d2,
                                 float  *x1, const float  *y1, float  *param)
   mcblasStatus_t mcblasDrotmg(mcblasHandle_t handle, double *d1, double *d2,
                                 double *x1, const double *y1, double *param)

This function constructs the modified Givens transformation

.. math::
   H = \begin{pmatrix}
   h_{11} & h_{12} \\
   h_{21} & h_{22} \\
   \end{pmatrix}

that zeros out the second entry of a
:math:`2 \times 1`
vector
:math:`\left( {\sqrt{d1}*x1,\sqrt{d2}*y1} \right)^{T}`
.
The ``flag=param[0]`` defines the following predefined
values for the matrix :math:`H`
entries

	+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+
	| ``flag=-1.0``                                                               | ``flag= 0.0``                                                               | ``flag= 1.0``                                                               | ``flag=-2.0``                                                               |
	+=============================================================================+=============================================================================+=============================================================================+=============================================================================+
	| :math:`\begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix}`    | :math:`\begin{pmatrix} 1.0 & h_{12} \\ h_{21} &1.0 \end{pmatrix}`           | :math:`\begin{pmatrix} h_{11} & 1.0 \\ -1.0& h_{22} \end{pmatrix}`          | :math:`\begin{pmatrix} 1.0 & 0.0 \\ 0.0 & 1.0\end{pmatrix}`                 |
	+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Notice that the values -1.0, 0.0 and 1.0 implied by the flag
are not stored in param.

.. table::
   :widths: grid

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | d1              | host or device  | in/out          | <type> scalar   |
   |                 |                 |                 | that is         |
   |                 |                 |                 | overwritten on  |
   |                 |                 |                 | exit.           |
   +-----------------+-----------------+-----------------+-----------------+
   | d2              | host or device  | in/out          | <type> scalar   |
   |                 |                 |                 | that is         |
   |                 |                 |                 | overwritten on  |
   |                 |                 |                 | exit.           |
   +-----------------+-----------------+-----------------+-----------------+
   | x1              | host or device  | in/out          | <type> scalar   |
   |                 |                 |                 | that is         |
   |                 |                 |                 | overwritten on  |
   |                 |                 |                 | exit.           |
   +-----------------+-----------------+-----------------+-----------------+
   | y1              | host or device  | input           | <type> scalar.  |
   +-----------------+-----------------+-----------------+-----------------+
   | param           | host or device  | output          | <type> vector   |
   |                 |                 |                 | of 5 elements,  |
   |                 |                 |                 | where           |
   |                 |                 |                 | ``param[0]``    |
   |                 |                 |                 | and             |
   |                 |                 |                 | ``param[1-4]``  |
   |                 |                 |                 | contain the     |
   |                 |                 |                 | flag and matrix |
   |                 |                 |                 | :math:`H`.      |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>scal()
----------------

::

   mcblasStatus_t  mcblasSscal(mcblasHandle_t handle, int n,
                               const float           *alpha,
                               float           *x, int incx)
   mcblasStatus_t  mcblasDscal(mcblasHandle_t handle, int n,
                               const double          *alpha,
                               double          *x, int incx)
   mcblasStatus_t  mcblasCscal(mcblasHandle_t handle, int n,
                               const mcComplex       *alpha,
                               mcComplex       *x, int incx)
   mcblasStatus_t mcblasCsscal(mcblasHandle_t handle, int n,
                               const float           *alpha,
                               mcComplex       *x, int incx)
   mcblasStatus_t  mcblasZscal(mcblasHandle_t handle, int n,
                               const mcDoubleComplex *alpha,
                               mcDoubleComplex *x, int incx)
   mcblasStatus_t mcblasZdscal(mcblasHandle_t handle, int n,
                               const double          *alpha,
                               mcDoubleComplex *x, int incx)

This function scales the vector ``x`` by the scalar
:math:`\alpha`
and overwrites it with the result. Hence, the performed
operation is
:math:`\mathbf{x}\lbrack j\rbrack = \alpha \times \mathbf{x}\lbrack j\rbrack`
for :math:`i = 1,\ldots,n`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{ incx}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +--------+----------------+--------+-----------------------------------------------+
   | Param. | Memory         | In/out | Meaning                                       |
   +========+================+========+===============================================+
   | handle |                | input  | handle to the mcBLAS library context.         |
   +--------+----------------+--------+-----------------------------------------------+
   | alpha  | host or device | input  | <type> scalar used for multiplication.        |
   +--------+----------------+--------+-----------------------------------------------+
   | n      |                | input  | number of elements in the vector ``x``.       |
   +--------+----------------+--------+-----------------------------------------------+
   | x      | device         | in/out | <type> vector with ``n`` elements.            |
   +--------+----------------+--------+-----------------------------------------------+
   | incx   |                | input  | stride between consecutive elements of ``x``. |
   +--------+----------------+--------+-----------------------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcblas<t>swap()
---------------

::

   mcblasStatus_t mcblasSswap(mcblasHandle_t handle, int n, float           *x,
                              int incx, float           *y, int incy)
   mcblasStatus_t mcblasDswap(mcblasHandle_t handle, int n, double          *x,
                              int incx, double          *y, int incy)
   mcblasStatus_t mcblasCswap(mcblasHandle_t handle, int n, mcComplex       *x,
                              int incx, mcComplex       *y, int incy)
   mcblasStatus_t mcblasZswap(mcblasHandle_t handle, int n, mcDoubleComplex *x,
                              int incx, mcDoubleComplex *y, int incy)

This function interchanges the elements of vector ``x`` and
``y``. Hence, the performed operation is
:math:`\left. \mathbf{y}\lbrack j\rbrack\Leftrightarrow\mathbf{x}\lbrack k\rbrack \right.`
for :math:`i = 1,\ldots,n`
,
:math:`k = 1 + \left( {i - 1} \right)*\text{incx}`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incy}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

====== ====== ====== =================================================
Param. Memory In/out Meaning
====== ====== ====== =================================================
handle        input  handle to the mcBLAS library context.
n             input  number of elements in the vector ``x`` and ``y``.
x      device in/out <type> vector with ``n`` elements.
incx          input  stride between consecutive elements of ``x``.
y      device in/out <type> vector with ``n`` elements.
incy          input  stride between consecutive elements of ``y``.
====== ====== ====== =================================================

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcBLAS Level-2 Functions
========================

In this chapter we describe the Level-2 Basic Linear Algebra
Subprograms (BLAS2) functions that perform matrix-vector
operations.

mcblas<t>gbmv()
----------------
        
::

   mcblasStatus_t mcblasSgbmv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n, int kl, int ku,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *x, int incx,
                              const float           *beta,
                              float           *y, int incy)
   mcblasStatus_t mcblasDgbmv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n, int kl, int ku,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *x, int incx,
                              const double          *beta,
                              double          *y, int incy)
   mcblasStatus_t mcblasCgbmv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n, int kl, int ku,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx,
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZgbmv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n, int kl, int ku,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the banded matrix-vector
multiplication

.. math::
   \mathbf{y} = \alpha\text{ op}(A)\mathbf{x} + \beta\mathbf{y}

where :math:`A`
is a banded matrix with :math:`kl`
subdiagonals and :math:`ku`
superdiagonals, :math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars. Also, for matrix :math:`A`

.. math::
   op(A) = \begin{cases}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{cases}

The banded matrix :math:`A`
is stored column by column, with the main diagonal stored in
row :math:`ku + 1`
(starting in first position), the first superdiagonal stored
in row :math:`ku`
(starting in second position), the first subdiagonal stored
in row :math:`ku + 2`
(starting in first position), etc. So that in general, the
element
:math:`A\left( {i,j} \right)`
is stored in the memory location ``A(ku+1+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \left\lbrack {\max\left( {1,j - ku} \right),\min\left( {m,j + kl} \right)} \right\rbrack`
. Also, the elements in the array
:math:`A`
that do not conceptually correspond to the elements in the
banded matrix (the top left
:math:`ku \times ku`
and bottom right :math:`kl \times kl`
triangles) are not referenced.

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | m      |                | input  | number of rows of      |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of columns of   |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | kl     |                | input  | number of subdiagonals |
   |        |                |        | of matrix ``A``.       |
   +--------+----------------+--------+------------------------+
   | ku     |                | input  | number of              |
   |        |                |        | superdiagonals of      |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x n``  |
   |        |                |        | with ``lda>=kl+ku+1``. |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements if      |
   |        |                |        | ``t                    |
   |        |                |        | ransa == MCBLAS_OP_N`` |
   |        |                |        | and ``m`` elements     |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta == 0`` then     |
   |        |                |        | ``y`` does not have to |
   |        |                |        | be a valid input.      |
   +--------+----------------+--------+------------------------+
   | y      | device         | in/out | <type> vector with     |
   |        |                |        | ``m`` elements if      |
   |        |                |        | ``t                    |
   |        |                |        | ransa == MCBLAS_OP_N`` |
   |        |                |        | and ``n`` elements     |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m, n, kl, ku < 0`` or     |
   |                                   |                                   |
   |                                   | -  if ``lda < (kl+ku+1)`` or      |
   |                                   |                                   |
   |                                   | -  if ``incx, incy == 0`` or      |
   |                                   |                                   |
   |                                   | -  if ``trans`` != MCBLAS_OP_N,   |
   |                                   |    MCBLAS_OP_T, MCBLAS_OP_C or    |
   |                                   |                                   |
   |                                   | -  ``alpha, beta == NULL``        |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>gemv()
----------------

::

   mcblasStatus_t mcblasSgemv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *x, int incx,
                              const float           *beta,
                              float           *y, int incy)
   mcblasStatus_t mcblasDgemv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *x, int incx,
                              const double          *beta,
                              double          *y, int incy)
   mcblasStatus_t mcblasCgemv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx,
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZgemv(mcblasHandle_t handle, mcblasOperation_t trans,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the matrix-vector multiplication

.. math::
    y = \alpha \, op(A)x + \beta \,y

where :math:`A`
is a :math:`m \times n`
matrix stored in column-major format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars. Also, for matrix :math:`A`

.. math::
    op(A) = 
    \begin{cases}
    A & if \enspace trans == MCBLAS\_OP\_N \\
    A^T & if \enspace trans == MCBLAS\_OP\_T \\
    A^H & if \enspace trans == MCBLAS\_OP\_C \\
    \end{cases}

.. table::
   :widths: grid
      
   +---------+-----------------+---------+--------------------------+
   | Param.  | Memory          | In/out  | Meaning                  |
   +=========+=================+=========+==========================+
   |  handle |                 |  input  |  handle to the mcBLAS    |
   |         |                 |         |  library context.        |
   +---------+-----------------+---------+--------------------------+
   |  trans  |                 |  input  |  operation op(``A``)     |
   |         |                 |         |  that is non- or         |
   |         |                 |         |  (conj.) transpose.      |
   +---------+-----------------+---------+--------------------------+
   |  m      |                 |  input  |  number of rows of       |
   |         |                 |         |  matrix ``A``.           |
   +---------+-----------------+---------+--------------------------+
   |  n      |                 |  input  |  number of columns of    |
   |         |                 |         |  matrix ``A``.           |
   +---------+-----------------+---------+--------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for  |
   |         |                 |         |  multiplication.         |
   +---------+-----------------+---------+--------------------------+
   |  A      |  device         |  input  |  <type> array of         |
   |         |                 |         |  dimension ``lda x n``   |
   |         |                 |         |  with                    |
   |         |                 |         |  ``lda >= max(1,m)``.    |
   |         |                 |         |  Before entry, the       |
   |         |                 |         |  leading ``m`` by ``n``  |
   |         |                 |         |  part of the array       |
   |         |                 |         |  ``A`` must contain the  |
   |         |                 |         |  matrix of               |
   |         |                 |         |  coefficients.           |
   |         |                 |         |  Unchanged on exit.      |
   +---------+-----------------+---------+--------------------------+
   |  lda    |                 |  input  |  leading dimension of    |
   |         |                 |         |  two-dimensional array   |
   |         |                 |         |  used to store matrix    |
   |         |                 |         |  ``A``. ``lda`` must be  |
   |         |                 |         |  at least ``max(1,m)``.  |
   +---------+-----------------+---------+--------------------------+
   |  x      |  device         |  input  |  <type> vector at least  |
   |         |                 |         |  `                       |
   |         |                 |         |  `(1+(n-1)*abs(incx))``  |
   |         |                 |         |  elements if             |
   |         |                 |         |  `                       |
   |         |                 |         |  `transa==MCBLAS_OP_N``  |
   |         |                 |         |  and at least            |
   |         |                 |         |  `                       |
   |         |                 |         |  `(1+(m-1)*abs(incx))``  |
   |         |                 |         |  elements otherwise.     |
   +---------+-----------------+---------+--------------------------+
   |  incx   |                 |  input  |  stride between          |
   |         |                 |         |  consecutive elements    |
   |         |                 |         |  of ``x``.               |
   +---------+-----------------+---------+--------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for  |
   |         |                 |         |  multiplication, if      |
   |         |                 |         |  ``beta==0`` then ``y``  |
   |         |                 |         |  does not have to be a   |
   |         |                 |         |  valid input.            |
   +---------+-----------------+---------+--------------------------+
   |  y      |  device         |  in/out |  <type> vector at least  |
   |         |                 |         |                          |
   |         |                 |         |  ``(1+(m-1)*abs(incy))`` |
   |         |                 |         |  elements if             |
   |         |                 |         |                          |
   |         |                 |         |  ``transa==MCBLAS_OP_N`` |
   |         |                 |         |  and at least            |
   |         |                 |         |                          |
   |         |                 |         |  ``(1+(n-1)*abs(incy))`` |
   |         |                 |         |  elements otherwise.     |
   +---------+-----------------+---------+--------------------------+
   |  incy   |                 |  input  |  stride between          |
   |         |                 |         |  consecutive elements    |
   |         |                 |         |  of ``y``                |
   +---------+-----------------+---------+--------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters ``m,n<0`` or      |
   |                                     |  ``incx,incy=0``                  |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>ger()
----------------

::

   mcblasStatus_t  mcblasSger(mcblasHandle_t handle, int m, int n,
                              const float           *alpha,
                              const float           *x, int incx,
                              const float           *y, int incy,
                              float           *A, int lda)
   mcblasStatus_t  mcblasDger(mcblasHandle_t handle, int m, int n,
                              const double          *alpha,
                              const double          *x, int incx,
                              const double          *y, int incy,
                              double          *A, int lda)
   mcblasStatus_t mcblasCgeru(mcblasHandle_t handle, int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *A, int lda)
   mcblasStatus_t mcblasCgerc(mcblasHandle_t handle, int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *A, int lda)
   mcblasStatus_t mcblasZgeru(mcblasHandle_t handle, int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex *A, int lda)
   mcblasStatus_t mcblasZgerc(mcblasHandle_t handle, int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex *A, int lda)

This function performs the rank-1 update

.. math:: 
   A = \begin{cases} 
   {\alpha\mathbf{xy}^{T} + A} & \text{if ger(), geru() is called} \\
   {\alpha\mathbf{xy}^{H} + A} & \text{if gerc() is called} \\
   \end{cases}

where :math:`A`
is a :math:`m \times n`
matrix stored in column-major format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
is a scalar.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | m      |                | input  | number of rows of      |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of columns of   |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``m`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | A      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``lda x n``  |
   |        |                |        | with                   |
   |        |                |        | ``lda >= max(1,m)``.   |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+----------------------------------+
   | Error Value                        | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed          |
   |                                    | successfully                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | the parameters ``m,n<0`` or      |
   |                                    | ``incx,incy=0``                  |
   +------------------------------------+----------------------------------+
   |                                    | the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                          |
   +------------------------------------+----------------------------------+

mcblas<t>sbmv()
----------------

::

   mcblasStatus_t mcblasSsbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, int k, const float  *alpha,
                              const float  *A, int lda,
                              const float  *x, int incx,
                              const float  *beta, float *y, int incy)
   mcblasStatus_t mcblasDsbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, int k, const double *alpha,
                              const double *A, int lda,
                              const double *x, int incx,
                              const double *beta, double *y, int incy)

This function performs the symmetric banded matrix-vector
multiplication

.. math::
    y = \alpha Ax + \beta y

where :math:`A`
is a :math:`n \times n`
symmetric banded matrix with :math:`k`
subdiagonals and superdiagonals,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the symmetric
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row 1, the first subdiagonal in row 2
(starting at first position), the second subdiagonal in row
3 (starting at first position), etc. So that in general, the
element :math:`A(i,j)`
is stored in the memory location ``A(1+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack j,\min(m,j + k)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the bottom right :math:`k \times k`
triangle) are not referenced.

If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the symmetric
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``k+1``, the first superdiagonal in row
``k`` (starting at second position), the second
superdiagonal in row ``k-1`` (starting at third position),
etc. So that in general, the element
:math:`A(i,j)`
is stored in the memory location ``A(1+k+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack\max(1,j - k),j\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the top left :math:`k \times k`
triangle) are not referenced.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other symmetric part   |
   |         |                 |         |  is not referenced and  |
   |         |                 |         |  is inferred from the   |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of rows and     |
   |         |                 |         |  columns of matrix      |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  k      |                 |  input  |  number of sub- and     |
   |         |                 |         |  super-diagonals of     |
   |         |                 |         |  matrix ``A``.          |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x n``  |
   |         |                 |         |  with ``lda >= k+1``.   |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  x      |  device         |  input  |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incx   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``x``.              |
   +---------+-----------------+---------+-------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta==0`` then ``y`` |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  y      |  device         |  in/out |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incy   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``y``.              |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters ``n,k<0`` or      |
   |                                     |  ``incx,incy=0``                  |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>spmv()
-----------------

::

   mcblasStatus_t mcblasSspmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const float  *alpha, const float  *AP,
                              const float  *x, int incx, const float  *beta,
                              float  *y, int incy)
   mcblasStatus_t mcblasDspmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const double *alpha, const double *AP,
                              const double *x, int incx, const double *beta,
                              double *y, int incy)

This function performs the symmetric packed matrix-vector
multiplication

.. math::
    y = \alpha A x + \beta y

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in packed format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table:: 
   :widths: grid

   +---------+-----------------+--------+------------------+
   | Param.  | Memory          | In/out | Meaning          |
   +=========+=================+========+==================+
   |  handle |                 |  input |  handle to the   |
   |         |                 |        |  mcBLAS library  |
   |         |                 |        |  context.        |
   +---------+-----------------+--------+------------------+
   |  uplo   |                 |  input |  indicates if    |
   |         |                 |        |  matrix          |
   |         |                 |        |  :math:`A`       |
   |         |                 |        |  lower or upper  |
   |         |                 |        |  part is stored, |
   |         |                 |        |  the other       |
   |         |                 |        |  symmetric part  |
   |         |                 |        |  is not          |
   |         |                 |        |  referenced and  |
   |         |                 |        |  is inferred     |
   |         |                 |        |  from the stored |
   |         |                 |        |  elements.       |
   +---------+-----------------+--------+------------------+
   |  n      |                 |  input |  number of rows  |
   |         |                 |        |  and columns of  |
   |         |                 |        |  matrix          |
   |         |                 |        |  :math:`A`       |
   |         |                 |        |  .               |
   +---------+-----------------+--------+------------------+
   |  alpha  |  host or device |  input |  <type> scalar   |
   |         |                 |        |  used for        |
   |         |                 |        |  multiplication. |
   +---------+-----------------+--------+------------------+
   |  AP     |  device         |  input |  <type> array    |
   |         |                 |        |  with            |
   |         |                 |        |  :math:`A`       |
   |         |                 |        |  stored in       |
   |         |                 |        |  packed format.  |
   +---------+-----------------+--------+------------------+
   |  x      |  device         |  input |  <type> vector   |
   |         |                 |        |  with ``n``      |
   |         |                 |        |  elements.       |
   +---------+-----------------+--------+------------------+
   |  incx   |                 |  input |  stride between  |
   |         |                 |        |  consecutive     |
   |         |                 |        |  elements of     |
   |         |                 |        |  ``x``.          |
   +---------+-----------------+--------+------------------+
   |  beta   |  host or device |  input |  <type> scalar   |
   |         |                 |        |  used for        |
   |         |                 |        |  multiplication, |
   |         |                 |        |  if ``beta==0``  |
   |         |                 |        |  then ``y`` does |
   |         |                 |        |  not have to be  |
   |         |                 |        |  a valid input.  |
   +---------+-----------------+--------+------------------+
   |  y      |  device         |  input |  <type> vector   |
   |         |                 |        |  with ``n``      |
   |         |                 |        |  elements.       |
   +---------+-----------------+--------+------------------+
   |  incy   |                 |  input |  stride between  |
   |         |                 |        |  consecutive     |
   |         |                 |        |  elements of     |
   |         |                 |        |  ``y``.          |
   +---------+-----------------+--------+------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters ``n<0`` or        |
   |                                     |  ``incx,incy=0``                  |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>spr()
---------------

::

   mcblasStatus_t mcblasSspr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const float  *alpha,
                             const float  *x, int incx, float  *AP)
   mcblasStatus_t mcblasDspr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const double *alpha,
                             const double *x, int incx, double *AP)

This function performs the packed symmetric rank-1 update

.. math::
   A = \alpha\textbf{x}\textbf{x}^{T} + A

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in packed format,
:math:`\mathbf{x}`
is a vector, and :math:`\alpha`
is a scalar.
If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table::
   :widths: grid
   :align: left

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | uplo            |                 | input           | indicates if    |
   |                 |                 |                 | matrix          |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | lower or upper  |
   |                 |                 |                 | part is stored, |
   |                 |                 |                 | the other       |
   |                 |                 |                 | symmetric part  |
   |                 |                 |                 | is not          |
   |                 |                 |                 | referenced and  |
   |                 |                 |                 | is inferred     |
   |                 |                 |                 | from the stored |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | n               |                 | input           | number of rows  |
   |                 |                 |                 | and columns of  |
   |                 |                 |                 | matrix          |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | .               |
   +-----------------+-----------------+-----------------+-----------------+
   | alpha           | host or device  | input           | <type> scalar   |
   |                 |                 |                 | used for        |
   |                 |                 |                 | multiplication. |
   +-----------------+-----------------+-----------------+-----------------+
   | x               | device          | input           | <type> vector   |
   |                 |                 |                 | with ``n``      |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | incx            |                 | input           | stride between  |
   |                 |                 |                 | consecutive     |
   |                 |                 |                 | elements of     |
   |                 |                 |                 | ``x``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | AP              | device          | in/out          | <type> array    |
   |                 |                 |                 | with            |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | stored in       |
   |                 |                 |                 | packed format.  |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``n<0`` or        |
   |                                   | ``incx,incy=0``                  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on |
   |                                   | the GPU                          |
   +-----------------------------------+----------------------------------+

mcblas<t>spr2()
-----------------

::

   mcblasStatus_t mcblasSspr2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const float  *alpha,
                              const float  *x, int incx,
                              const float  *y, int incy, float  *AP)
   mcblasStatus_t mcblasDspr2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const double *alpha,
                              const double *x, int incx,
                              const double *y, int incy, double *AP)

This function performs the packed symmetric rank-2 update

.. math::
   A = \alpha\left( {\textbf{x}\textbf{y}^{T} + \textbf{y}\textbf{x}^{T}} \right) + A

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in packed format,
:math:`\mathbf{x}`
is a vector, and :math:`\alpha`
is a scalar.
If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the symmetric matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table::
   :widths: grid
   :align: left

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | uplo            |                 | input           | indicates if    |
   |                 |                 |                 | matrix          |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | lower or upper  |
   |                 |                 |                 | part is stored, |
   |                 |                 |                 | the other       |
   |                 |                 |                 | symmetric part  |
   |                 |                 |                 | is not          |
   |                 |                 |                 | referenced and  |
   |                 |                 |                 | is inferred     |
   |                 |                 |                 | from the stored |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | n               |                 | input           | number of rows  |
   |                 |                 |                 | and columns of  |
   |                 |                 |                 | matrix          |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | .               |
   +-----------------+-----------------+-----------------+-----------------+
   | alpha           | host or device  | input           | <type> scalar   |
   |                 |                 |                 | used for        |
   |                 |                 |                 | multiplication. |
   +-----------------+-----------------+-----------------+-----------------+
   | x               | device          | input           | <type> vector   |
   |                 |                 |                 | with ``n``      |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | incx            |                 | input           | stride between  |
   |                 |                 |                 | consecutive     |
   |                 |                 |                 | elements of     |
   |                 |                 |                 | ``x``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | y               | device          | input           | <type> vector   |
   |                 |                 |                 | with ``n``      |
   |                 |                 |                 | elements.       |
   +-----------------+-----------------+-----------------+-----------------+
   | incy            |                 | input           | stride between  |
   |                 |                 |                 | consecutive     |
   |                 |                 |                 | elements of     |
   |                 |                 |                 | ``y``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | AP              | device          | in/out          | <type> array    |
   |                 |                 |                 | with            |
   |                 |                 |                 | :math:`A`       |
   |                 |                 |                 | stored in       |
   |                 |                 |                 | packed format.  |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``n<0`` or        |
   |                                   | ``incx,incy=0``                  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on |
   |                                   | the GPU                          |
   +-----------------------------------+----------------------------------+   

mcblas<t>symv()
---------------

::

   mcblasStatus_t mcblasSsymv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const float           *alpha,
                              const float           *A, int lda,
                              const float           *x, int incx, 
                              const float           *beta,
                              float           *y, int incy)
   mcblasStatus_t mcblasDsymv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const double          *alpha,
                              const double          *A, int lda,
                              const double          *x, int incx, 
                              const double          *beta,
                              double          *y, int incy)
   mcblasStatus_t mcblasCsymv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcComplex       *alpha, 
                              /* host or device pointer */
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx, 
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZsymv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx, 
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the symmetric matrix-vector
multiplication.

.. math::
    y = \alpha A x + \beta y

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in lower or upper mode,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.
This function has an alternate faster implementation using
atomics that can be enabled with ``mcblasSetAtomicsMode()``.

Please see the section on the function
``mcblasSetAtomicsMode()`` for more details about the usage
of atomics.

.. table:: 
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  lower or upper part is |
   |         |                 |         |  stored, the other      |
   |         |                 |         |  symmetric part is not  |
   |         |                 |         |  referenced and is      |
   |         |                 |         |  inferred from the      |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of rows and     |
   |         |                 |         |  columns of matrix      |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``lda>=max(1,n)``.     |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  x      |  device         |  input  |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incx   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``x``.              |
   +---------+-----------------+---------+-------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta==0`` then ``y`` |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  y      |  device         |  in/out |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incy   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``y``.              |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters ``n<0`` or        |
   |                                     |  ``incx,incy=0``                  |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>syr()
---------------

::

   mcblasStatus_t mcblasSsyr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const float             *alpha,
                             const float           *x, int incx, 
                             float           *A, int lda)
   mcblasStatus_t mcblasDsyr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const double            *alpha,
                             const double          *x, int incx, 
                             double          *A, int lda)
   mcblasStatus_t mcblasCsyr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const mcComplex         *alpha,
                             const mcComplex       *x, int incx, 
                             mcComplex       *A, int lda)
   mcblasStatus_t mcblasZsyr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                             int n, const mcDoubleComplex   *alpha,
                             const mcDoubleComplex *x, int incx, 
                             mcDoubleComplex *A, int lda)

This function performs the symmetric rank-1 update

.. math::
   A = \alpha\textbf{x}\textbf{x}^{T} + A

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in column-major format,
:math:`\mathbf{x}`
is a vector, and :math:`\alpha`
is a scalar.

.. table::
   :widths: grid
   :align: left

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | :math:`A`              |
   |        |                |        | lower or upper         |
   |        |                |        | part is stored, the    |
   |        |                |        | other symmetric part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | :math:`A` .            |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | A      | device         | in/out | <type> array of        |
   |        |                |        | dimensions             |
   |        |                |        | ``lda x n``, with      |
   |        |                |        | ``lda>=max(1,n)``.     |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | :math:`A` .            |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``n<0`` or        |
   |                                   | ``incx=0``                       |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on |
   |                                   | the GPU                          |
   +-----------------------------------+----------------------------------+

mcblas<t>syr2()
-----------------

::

   mcblasStatus_t mcblasSsyr2(mcblasHandle_t handle, mcblasFillMode_t uplo, 
                              int n,   const float           *alpha, 
                              const float           *x, int incx,
                              const float           *y, int incy, 
                              float           *A, int lda)
   mcblasStatus_t mcblasDsyr2(mcblasHandle_t handle, mcblasFillMode_t uplo, 
                              int n,   const double          *alpha, 
                              const double          *x, int incx,
                              const double          *y, int incy, 
                              double          *A, int lda)
   mcblasStatus_t mcblasCsyr2(mcblasHandle_t handle, mcblasFillMode_t uplo, 
                              int n,   const mcComplex       *alpha, 
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy, 
                              mcComplex       *A, int lda)
   mcblasStatus_t mcblasZsyr2(mcblasHandle_t handle, mcblasFillMode_t uplo, 
                              int n,   const mcDoubleComplex *alpha, 
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy, 
                              mcDoubleComplex *A, int lda)

This function performs the symmetric rank-2 update

.. math::
   A = \alpha\left( {\textbf{x}\textbf{y}^{T} + \textbf{y}\textbf{x}^{T}} \right) + A

where :math:`A`
is a :math:`n \times n`
symmetric matrix stored in column-major format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
is a scalar.

.. table::
   :widths: grid
   :align: left

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | :math:`A`              |
   |        |                |        | lower or upper         |
   |        |                |        | part is stored, the    |
   |        |                |        | other symmetric part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | :math:`A` .            |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | A      | device         | in/out | <type> array of        |
   |        |                |        | dimensions             |
   |        |                |        | ``lda x n``, with      |
   |        |                |        | ``lda>=max(1,n)``.     |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | :math:`A` .            |
   +--------+----------------+--------+------------------------+   

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``n<0`` or        |
   |                                   | ``incx=0,incy=0``                |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on |
   |                                   | the GPU                          |
   +-----------------------------------+----------------------------------+

mcblas<t>tbmv()
----------------

::

   mcblasStatus_t mcblasStbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const float           *A, int lda,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const double          *A, int lda,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const mcComplex       *A, int lda,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const mcDoubleComplex *A, int lda,
                              mcDoubleComplex *x, int incx)

This function performs the triangular banded matrix-vector
multiplication

.. math::
    x = op(A)x

where :math:`A`
is a triangular banded matrix, and
:math:`\mathbf{x}`
is a vector. Also, for matrix :math:`A`

.. math::
    op(A) = \begin{cases}
    A & if \enspace trans == MCBLAS\_OP\_N \\
    A^T & if \enspace trans == MCBLAS\_OP\_T \\
    A^H & if \enspace trans == MCBLAS\_OP\_C \\
    \end{cases}

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the triangular
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``1``, the first subdiagonal in row
``2`` (starting at first position), the second subdiagonal
in row ``3`` (starting at first position), etc. So that in
general, the element :math:`A(i,j)`
is stored in the memory location ``A(1+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack j,\min(m,j + k)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the bottom right :math:`k \times k`
triangle) are not referenced.

If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the triangular
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``k+1``, the first superdiagonal in row
``k`` (starting at second position), the second
superdiagonal in row ``k-1`` (starting at third position),
etc. So that in general, the element
:math:`A(i,j)`
is stored in the memory location ``A(1+k+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack\max(1,j - k,j)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the top left :math:`k \times k`
triangle) are not referenced.

.. table:: 
   :widths: grid

   +--------+---------+--------+-----------------------------------------+
   | Param. | Memory  | In/out | Meaning                                 |
   +========+=========+========+=========================================+
   | handle |         | input  | handle to the mcBLAS library context.   |
   +--------+---------+--------+-----------------------------------------+
   |  uplo  |         |  input |  indicates if matrix ``A`` lower or     |
   |        |         |        |  upper part is stored, the other part   |
   |        |         |        |  is not referenced and is inferred from |
   |        |         |        |  the stored elements.                   |
   +--------+---------+--------+-----------------------------------------+
   |  trans |         |  input |  operation op(``A``) that is non- or    |
   |        |         |        |  (conj.) transpose.                     |
   +--------+---------+--------+-----------------------------------------+
   |  diag  |         |  input |  indicates if the elements on the main  |
   |        |         |        |  diagonal of matrix ``A`` are unity and |
   |        |         |        |  should not be accessed.                |
   +--------+---------+--------+-----------------------------------------+
   |  n     |         |  input |  number of rows and columns of matrix   |
   |        |         |        |  ``A``.                                 |
   +--------+---------+--------+-----------------------------------------+
   |  k     |         |  input |  number of sub- and super-diagonals of  |
   |        |         |        |  matrix .                               |
   +--------+---------+--------+-----------------------------------------+
   |  A     |  device |  input |  <type> array of dimension ``lda x n``, |
   |        |         |        |  with ``lda>=k+1``.                     |
   +--------+---------+--------+-----------------------------------------+
   |  lda   |         |  input |  leading dimension of two-dimensional   |
   |        |         |        |  array used to store matrix ``A``.      |
   +--------+---------+--------+-----------------------------------------+
   | x      | device  | in/out | <type> vector with ``n`` elements.      |
   +--------+---------+--------+-----------------------------------------+
   |  incx  |         |  input |  stride between consecutive elements of |
   |        |         |        |  ``x``.                                 |
   +--------+---------+--------+-----------------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters ``n,k<0`` or      |
   |                                     |  ``incx=0``                       |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_ALLOC_FAILED``     |  the allocation of internal       |
   |                                     |  scratch memory failed            |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>tbsv()
----------------

::

   mcblasStatus_t mcblasStbsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const float           *A, int lda,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtbsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const double          *A, int lda,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtbsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const mcComplex       *A, int lda,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtbsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, int k, const mcDoubleComplex *A, int lda,
                              mcDoubleComplex *x, int incx)

This function solves the triangular banded linear system
with a single right-hand-side

.. math:: 
   \text{op}(A)\textbf{x} = \textbf{b}

where :math:`A`
is a triangular banded matrix, and
:math:`\mathbf{x}`
and :math:`\mathbf{b}`
are vectors. Also, for matrix :math:`A`

.. math:: 
   op(A) = \begin{cases}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{cases}

The solution :math:`\mathbf{x}`
overwrites the right-hand-sides
:math:`\mathbf{b}`
on exit.
No test for singularity or near-singularity is included in
this function.

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the triangular
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``1``, the first subdiagonal in row
``2`` (starting at first position), the second subdiagonal
in row ``3`` (starting at first position), etc. So that in
general, the element :math:`A(i,j)`
is stored in the memory location ``A(1+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack j,\min(m,j + k)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the bottom right :math:`k \times k`
triangle) are not referenced.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the triangular
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``k+1``, the first superdiagonal in row
``k`` (starting at second position), the second
superdiagonal in row ``k-1`` (starting at third position),
etc. So that in general, the element
:math:`A(i,j)`
is stored in the memory location ``A(1+k+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack\max(1,j - k,j)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the top left :math:`k \times k`
triangle) are not referenced.

.. table::
   :widths: grid
   :align: left

   +--------+--------+--------+----------------------------------------+
   | Param. | Memory | In/out | Meaning                                |
   +========+========+========+========================================+
   | handle |        | input  | handle to the mcBLAS library context.  |
   +--------+--------+--------+----------------------------------------+
   | uplo   |        | input  | indicates if matrix :math:`A` lower or |
   |        |        |        | upper part is stored, the other part   |
   |        |        |        | is not referenced and is inferred from |
   |        |        |        | the stored elements.                   |
   +--------+--------+--------+----------------------------------------+
   | trans  |        | input  | operation op(:math:`A`)                |
   |        |        |        | that is non- or                        |
   |        |        |        | (conj.) transpose.                     |
   +--------+--------+--------+----------------------------------------+
   | diag   |        | input  | indicates if the elements on the main  |
   |        |        |        | diagonal of matrix                     |
   |        |        |        | :math:`A` are unity and                |
   |        |        |        | should not be accessed.                |
   +--------+--------+--------+----------------------------------------+
   | n      |        | input  | number of rows and columns of matrix   |
   |        |        |        | :math:`A` .                            |
   +--------+--------+--------+----------------------------------------+
   | k      |        | input  | number of sub- and super-diagonals of  |
   |        |        |        | matrix :math:`A` .                     |
   +--------+--------+--------+----------------------------------------+
   | A      | device | input  | <type> array of dimension ``lda x n``, |
   |        |        |        | with ``lda >= k+1``.                   |
   +--------+--------+--------+----------------------------------------+
   | lda    |        | input  | leading dimension of two-dimensional   |
   |        |        |        | array used to store matrix :math:`A` . |
   +--------+--------+--------+----------------------------------------+
   | x      | device | in/out | <type> vector with ``n`` elements.     |
   +--------+--------+--------+----------------------------------------+
   | incx   |        | input  | stride between consecutive elements of |
   |        |        |        | ``x``.                                 |
   +--------+--------+--------+----------------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``n,k<0`` or      |
   |                                   | ``incx=0``                       |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on |
   |                                   | the GPU                          |
   +-----------------------------------+----------------------------------+

mcblas<t>tpmv()
-----------------

::

   mcblasStatus_t mcblasStpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const float           *AP,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const double          *AP,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcComplex       *AP,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcDoubleComplex *AP,
                              mcDoubleComplex *x, int incx)

This function performs the triangular packed matrix-vector
multiplication

.. math::
    x = op(A)x

where :math:`A`
is a triangular matrix stored in packed format, and
:math:`\mathbf{x}`
is a vector. Also, for matrix :math:`A`

.. math::
    op(A) = 
    \begin{cases}
    A & if \enspace trans == MCBLAS\_OP\_N \\
    A^T & if \enspace trans == MCBLAS\_OP\_T \\
    A^H & if \enspace trans == MCBLAS\_OP\_C \\
    \end{cases}


If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the triangular matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the triangular matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`A(i,j)`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table:: 
   :widths: grid

   +---------+---------+---------+------------------+
   | Param.  | Memory  | In/out  | Meaning          |
   +=========+=========+=========+==================+
   |  handle |         |  input  |  handle to the   |
   |         |         |         |  mcBLAS library  |
   |         |         |         |  context.        |
   +---------+---------+---------+------------------+
   |  uplo   |         |  input  |  indicates if    |
   |         |         |         |  matrix ``A``    |
   |         |         |         |  lower or upper  |
   |         |         |         |  part is stored, |
   |         |         |         |  the other part  |
   |         |         |         |  is not          |
   |         |         |         |  referenced and  |
   |         |         |         |  is inferred     |
   |         |         |         |  from the stored |
   |         |         |         |  elements.       |
   +---------+---------+---------+------------------+
   |  trans  |         |  input  |  operation       |
   |         |         |         |  op(``A``) that  |
   |         |         |         |  is non- or      |
   |         |         |         |  (conj.)         |
   |         |         |         |  transpose.      |
   +---------+---------+---------+------------------+
   |  diag   |         |  input  |  indicates if    |
   |         |         |         |  the elements on |
   |         |         |         |  the main        |
   |         |         |         |  diagonal of     |
   |         |         |         |  matrix ``A``    |
   |         |         |         |  are unity and   |
   |         |         |         |  should not be   |
   |         |         |         |  accessed.       |
   +---------+---------+---------+------------------+
   |  n      |         |  input  |  number of rows  |
   |         |         |         |  and columns of  |
   |         |         |         |  matrix ``A``.   |
   +---------+---------+---------+------------------+
   |  AP     |  device |  input  |  <type> array    |
   |         |         |         |  with :math:`A`  |
   |         |         |         |  stored in       |
   |         |         |         |  packed format.  |
   +---------+---------+---------+------------------+
   |  x      |  device |  in/out |  <type> vector   |
   |         |         |         |  with ``n``      |
   |         |         |         |  elements.       |
   +---------+---------+---------+------------------+
   |  incx   |         |  input  |  stride between  |
   |         |         |         |  consecutive     |
   |         |         |         |  elements of     |
   |         |         |         |  ``x``.          |
   +---------+---------+---------+------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-------------------------------------------------------------+
   | Error Value                         | Meaning                                                     |
   +=====================================+=============================================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed                                    |
   |                                     |  successfully                                               |
   +-------------------------------------+-------------------------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized                             |
   +-------------------------------------+-------------------------------------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  - If ``n < 0`` or                                          |
   |                                     |                                                             |
   |                                     |  - if ``incx == 0`` or                                      |
   |                                     |                                                             |
   |                                     |  - if ``uplo !=                                             |                                
   |                                     |    MCBLAS_FILL_MODE_UPPER, MCBLAS_FILL_MODE_LOWER`` or      |
   |                                     |                                                             |
   |                                     |  - if ``trans != MCBLAS_OP_N, MCBLAS_OP_T, MCBLAS_OP_C`` or |
   |                                     |                                                             |
   |                                     |  - ``diag != MCBLAS_DIAG_UNIT, MCBLAS_DIAG_NON_UNIT``       |
   +-------------------------------------+-------------------------------------------------------------+
   |  ``MCBLAS_STATUS_ALLOC_FAILED``     |  the allocation of internal                                 |
   |                                     |  scratch memory failed                                      |
   +-------------------------------------+-------------------------------------------------------------+
   |                                     |  the function failed to launch on                           |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                                                    |
   +-------------------------------------+-------------------------------------------------------------+

mcblas<t>tpsv()
----------------

::

   mcblasStatus_t mcblasStpsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const float           *AP,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtpsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const double          *AP,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtpsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcComplex       *AP,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtpsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcDoubleComplex *AP,
                              mcDoubleComplex *x, int incx)

This function solves the packed triangular linear system
with a single right-hand-side

.. math:: 
   \text{op}(A)\textbf{x} = \textbf{b}

where :math:`A`
is a triangular matrix stored in packed format, and
:math:`\mathbf{x}`
and :math:`\mathbf{b}`
are vectors. Also, for matrix :math:`A`

.. math:: 
   op(A) = \begin{cases}
   A & if \enspace trans == MCBLAS\_OP\_N \\
   A^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{cases}

The solution :math:`\mathbf{x}`
overwrites the right-hand-sides
:math:`\mathbf{b}`
on exit.
No test for singularity or near-singularity is included in
this function.

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the triangular matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the triangular matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table::
   :widths: grid
   :align: left

   +--------+--------+--------+----------------------------------------+
   | Param. | Memory | In/out | Meaning                                |
   +========+========+========+========================================+
   | handle |        | input  | handle to the mcBLAS library context.  |
   +--------+--------+--------+----------------------------------------+
   | uplo   |        | input  | indicates if matrix :math:`A` lower or |
   |        |        |        | upper part is stored, the other part   |
   |        |        |        | is not referenced and is inferred from |
   |        |        |        | the stored elements.                   |
   +--------+--------+--------+----------------------------------------+
   | trans  |        | input  | operation op(:math:`A`) that is non- or|
   |        |        |        | (conj.) transpose.                     |
   +--------+--------+--------+----------------------------------------+
   | diag   |        | input  | indicates if the elements on the main  |
   |        |        |        | diagonal of matrix are unity and       |
   |        |        |        | should not be accessed.                |
   +--------+--------+--------+----------------------------------------+
   | n      |        | input  | number of rows and columns of matrix   |
   |        |        |        | :math:`A` .                            |
   +--------+--------+--------+----------------------------------------+
   | AP     | device | input  | <type> array with :math:`A` stored in  |
   |        |        |        | packed format.                         |
   +--------+--------+--------+----------------------------------------+
   | x      | device | in/out | <type> vector with ``n`` elements.     |
   +--------+--------+--------+----------------------------------------+
   | incx   |        | input  | stride between consecutive elements of |
   |        |        |        | ``x``.                                 |
   +--------+--------+--------+----------------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or                |
   |                                   |                                   |
   |                                   | -  if ``incx`` = 0 or             |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  ``diag`` !=                    |
   |                                   |    ``MCBLAS_DIAG_UNIT``,          |
   |                                   |    ``MCBLAS_DIAG_NON_UNIT``       |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on  |
   |                                   | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>trmv()
-----------------

::

   mcblasStatus_t mcblasStrmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const float           *A, int lda,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtrmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const double          *A, int lda,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtrmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcComplex       *A, int lda,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtrmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcDoubleComplex *A, int lda,
                              mcDoubleComplex *x, int incx)

This function performs the triangular matrix-vector
multiplication

.. math:: 
   \textbf{x} = \text{op}(A)\textbf{x}

where :math:`A`
is a triangular matrix stored in lower or upper mode with or
without the main diagonal, and
:math:`\mathbf{x}`
is a vector. Also, for matrix :math:`A`

.. math::
   op(A) = \begin{cases} 
   A & if \enspace trans == MCBLAS\_OP\_N \\
   A^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{cases}

.. table::
   :widths: grid
   :align: left

   +--------+--------+--------+----------------------------------------+
   | Param. | Memory | In/out | Meaning                                |
   +========+========+========+========================================+
   | handle |        | input  | handle to the mcBLAS library context.  |
   +--------+--------+--------+----------------------------------------+
   | uplo   |        | input  | indicates if matrix :math:`A` lower or |
   |        |        |        | upper part is stored, the other part   |
   |        |        |        | is not referenced and is inferred from |
   |        |        |        | the stored elements.                   |
   +--------+--------+--------+----------------------------------------+
   | trans  |        | input  | operation op(:math:`A`)                |
   |        |        |        | (that is, non- or                      |
   |        |        |        | conj.) transpose.                      |
   +--------+--------+--------+----------------------------------------+
   | diag   |        | input  | indicates if the elements on the main  |
   |        |        |        | diagonal of matrix :math:`A`           |
   |        |        |        | are unity and                          |
   |        |        |        | should not be accessed.                |
   +--------+--------+--------+----------------------------------------+
   | n      |        | input  | number of rows and columns of matrix   |
   |        |        |        | :math:`A` .                            |
   +--------+--------+--------+----------------------------------------+
   | A      | device | input  | <type> array of dimensions ``lda x n`` |
   |        |        |        | , with ``lda>=max(1,n)``.              |
   +--------+--------+--------+----------------------------------------+
   | lda    |        | input  | leading dimension of two-dimensional   |
   |        |        |        | array used to store matrix :math:`A` . |
   +--------+--------+--------+----------------------------------------+
   | x      | device | in/out | <type> vector with ``n`` elements.     |
   +--------+--------+--------+----------------------------------------+
   | incx   |        | input  | stride between consecutive elements of |
   |        |        |        | ``x``.                                 |
   +--------+--------+--------+----------------------------------------+   

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or                |
   |                                   |                                   |
   |                                   | -  if ``incx`` = 0 or             |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``diag`` !=                 |
   |                                   |    ``MCBLAS_DIAG_UNIT``,          |
   |                                   |    ``MCBLAS_DIAG_NON_UNIT`` or    |
   |                                   |                                   |
   |                                   | -  ``lda`` < max(1, ``n``)        |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the allocation of internal        |
   |                                   | scratch memory failed             |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on  |
   |                                   | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>trsv()
------------------

::

   mcblasStatus_t mcblasStrsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const float           *A, int lda,
                              float           *x, int incx)
   mcblasStatus_t mcblasDtrsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const double          *A, int lda,
                              double          *x, int incx)
   mcblasStatus_t mcblasCtrsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcComplex       *A, int lda,
                              mcComplex       *x, int incx)
   mcblasStatus_t mcblasZtrsv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int n, const mcDoubleComplex *A, int lda,
                              mcDoubleComplex *x, int incx)

This function solves the triangular linear system with a
single right-hand-side

.. math::
   \text{op}(A)\textbf{x} = \textbf{b}

where :math:`A`
is a triangular matrix stored in lower or upper mode with or
without the main diagonal, and
:math:`\mathbf{x}`
and :math:`\mathbf{b}`
are vectors. Also, for matrix :math:`A`

.. math:: 
   op(A) = \begin{cases}
   A & if \enspace trans == MCBLAS\_OP\_N \\
   A^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{cases}

The solution :math:`\mathbf{x}`
overwrites the right-hand-sides
:math:`\mathbf{b}`
on exit.
No test for singularity or near-singularity is included in
this function.

.. table::
   :widths: grid
   :align: left

   +--------+--------+--------+----------------------------------------+
   | Param. | Memory | In/out | Meaning                                |
   +========+========+========+========================================+
   | handle |        | input  | handle to the mcBLAS library context.  |
   +--------+--------+--------+----------------------------------------+
   | uplo   |        | input  | indicates if matrix :math:`A` lower or |
   |        |        |        | upper part is stored, the other part   |
   |        |        |        | is not referenced and is inferred from |
   |        |        |        | the stored elements.                   |
   +--------+--------+--------+----------------------------------------+
   | trans  |        | input  | operation op(:math:`A`) that is non- or|
   |        |        |        | (conj.) transpose.                     |
   +--------+--------+--------+----------------------------------------+
   | diag   |        | input  | indicates if the elements on the main  |
   |        |        |        | diagonal of matrix                     |
   |        |        |        | :math:`A` are unity and                |
   |        |        |        | should not be accessed.                |
   +--------+--------+--------+----------------------------------------+
   | n      |        | input  | number of rows and columns of matrix   |
   |        |        |        | :math:`A` .                            |
   +--------+--------+--------+----------------------------------------+
   | A      | device | input  | <type> array of dimension ``lda x n``, |
   |        |        |        | with ``lda>=max(1,n)``.                |
   +--------+--------+--------+----------------------------------------+
   | lda    |        | input  | leading dimension of two-dimensional   |
   |        |        |        | array used to store matrix :math:`A` . |
   +--------+--------+--------+----------------------------------------+
   | x      | device | in/out | <type> vector with ``n`` elements.     |
   +--------+--------+--------+----------------------------------------+
   | incx   |        | input  | stride between consecutive elements of |
   |        |        |        | ``x``.                                 |
   +--------+--------+--------+----------------------------------------+   

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or                |
   |                                   |                                   |
   |                                   | -  if ``incx`` = 0 or             |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``diag`` !=                 |
   |                                   |    ``MCBLAS_DIAG_UNIT``,          |
   |                                   |    ``MCBLAS_DIAG_NON_UNIT`` or    |
   |                                   |                                   |
   |                                   | -  ``lda`` < max(1, ``n``)        |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on  |
   |                                   | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>hemv()
-----------------

::

   mcblasStatus_t mcblasChemv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx,
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZhemv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the Hermitian matrix-vector
multiplication

.. math::
    y = \alpha \, A \, x + \beta \, y

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in lower or upper mode,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.
This function has an alternate faster implementation using
atomics that can be enabled with

Please see the section on the for more details about the
usage of atomics

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other Hermitian part   |
   |         |                 |         |  is not referenced and  |
   |         |                 |         |  is inferred from the   |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of rows and     |
   |         |                 |         |  columns of matrix      |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x n``, |
   |         |                 |         |  with                   |
   |         |                 |         |  ``lda>=max(1,n)``. The |
   |         |                 |         |  imaginary parts of the |
   |         |                 |         |  diagonal elements are  |
   |         |                 |         |  assumed to be zero.    |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  x      |  device         |  input  |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incx   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``x``.              |
   +---------+-----------------+---------+-------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta==0`` then ``y`` |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  y      |  device         |  in/out |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incy   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``y``.              |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  - If ``n`` < 0 or                |
   |                                     |                                   |
   |                                     |  - if ``incx`` = 0 or ``incy`` =  |
   |                                     |    0 or                           |
   |                                     |  - if ``uplo`` !=                 |
   |                                     |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                     |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                     |                                   |
   |                                     |  - ``lda`` < ``n``                |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>hbmv()
----------------

::

   mcblasStatus_t mcblasChbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, int k, const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx,
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZhbmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, int k, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the Hermitian banded matrix-vector
multiplication

.. math::
    y = \alpha A x + \beta y

where :math:`A`
is a :math:`n \times n`
Hermitian banded matrix with :math:`k`
subdiagonals and superdiagonals,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the Hermitian
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``1``, the first subdiagonal in row
``2`` (starting at first position), the second subdiagonal
in row ``3`` (starting at first position), etc. So that in
general, the element :math:`A(i,j)`
is stored in the memory location ``A(1+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack j,\min(m,j + k)\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the bottom right :math:`k \times k`
triangle) are not referenced.

If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the Hermitian
banded matrix :math:`A`
is stored column by column, with the main diagonal of the
matrix stored in row ``k+1``, the first superdiagonal in row
``k`` (starting at second position), the second
superdiagonal in row ``k-1`` (starting at third position),
etc. So that in general, the element
:math:`A(i,j)`
is stored in the memory location ``A(1+k+i-j,j)`` for
:math:`j = 1,\ldots,n`
and
:math:`i \in \lbrack\max(1,j - k),j\rbrack`
. Also, the elements in the array ``A`` that do not
conceptually correspond to the elements in the banded matrix
(the top left :math:`k \times k`
triangle) are not referenced.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other Hermitian part   |
   |         |                 |         |  is not referenced and  |
   |         |                 |         |  is inferred from the   |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of rows and     |
   |         |                 |         |  columns of matrix      |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  k      |                 |  input  |  number of sub- and     |
   |         |                 |         |  super-diagonals of     |
   |         |                 |         |  matrix ``A``.          |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimensions             |
   |         |                 |         |  ``lda x n``, with      |
   |         |                 |         |  ``lda>=k+1``. The      |
   |         |                 |         |  imaginary parts of the |
   |         |                 |         |  diagonal elements are  |
   |         |                 |         |  assumed to be zero.    |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  x      |  device         |  input  |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incx   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``x``.              |
   +---------+-----------------+---------+-------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta==0`` then does  |
   |         |                 |         |  not have to be a valid |
   |         |                 |         |  input.                 |
   +---------+-----------------+---------+-------------------------+
   |  y      |  device         |  in/out |  <type> vector with     |
   |         |                 |         |  ``n`` elements.        |
   +---------+-----------------+---------+-------------------------+
   |  incy   |                 |  input  |  stride between         |
   |         |                 |         |  consecutive elements   |
   |         |                 |         |  of ``y``.              |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``           |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``     |  - If ``n`` < 0 or ``k`` < 0 or   |
   |                                     |                                   |
   |                                     |  - if ``incx`` = 0 or ``incy`` =  |
   |                                     |    0 or                           |
   |                                     |  - if ``uplo`` !=                 |
   |                                     |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                     |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                     |  - if ``lda`` < (``k`` + 1) or    |
   |                                     |                                   |
   |                                     |  - ``alpha`` == NULL or ``beta``  |
   |                                     |    == NULL                        |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``  |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>hpmv()
----------------

::

   mcblasStatus_t mcblasChpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcComplex       *alpha,
                              const mcComplex       *AP,
                              const mcComplex       *x, int incx,
                              const mcComplex       *beta,
                              mcComplex       *y, int incy)
   mcblasStatus_t mcblasZhpmv(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *AP,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *y, int incy)

This function performs the Hermitian packed matrix-vector
multiplication

.. math:: 
   \textbf{y} = \alpha A\textbf{x} + \beta\textbf{y}

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in packed format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
and :math:`\beta`
are scalars.
If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | AP     | device         | input  | <type> array with      |
   |        |                |        | ``A`` stored in packed |
   |        |                |        | format. The imaginary  |
   |        |                |        | parts of the diagonal  |
   |        |                |        | elements are assumed   |
   |        |                |        | to be zero.            |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0`` then ``y`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | y      | device         | in/out | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+-----------------------------------+
   | Error Value                        | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed           |
   |                                    | successfully                      |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | -  If ``n`` < 0 or                |
   |                                    |                                   |
   |                                    | -  if ``incx`` == 0 or ``incy``   |
   |                                    |    == 0 or                        |
   |                                    |                                   |
   |                                    | -  if ``uplo`` !=                 |
   |                                    |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                    |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                    |                                   |
   |                                    | -  ``alpha`` == NULL or ``beta``  |
   |                                    |    == NULL                        |
   +------------------------------------+-----------------------------------+
   |                                    | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +------------------------------------+-----------------------------------+

mcblas<t>her()
----------------

::

   mcblasStatus_t mcblasCher(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const float  *alpha,
                              const mcComplex       *x, int incx,
                              mcComplex       *A, int lda)
   mcblasStatus_t mcblasZher(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const double *alpha,
                              const mcDoubleComplex *x, int incx,
                              mcDoubleComplex *A, int lda)

This function performs the Hermitian rank-1 update

.. math::
   A = \alpha\textbf{x}\textbf{x}^{H} + A

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in column-major format,
:math:`\mathbf{x}`
is a vector, and :math:`\alpha`
is a scalar.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | A      | device         | in/out | <type> array of        |
   |        |                |        | dimensions             |
   |        |                |        | ``lda x n``, with      |
   |        |                |        | ``lda>=max(1,n)``. The |
   |        |                |        | imaginary parts of the |
   |        |                |        | diagonal elements are  |
   |        |                |        | assumed and set to     |
   |        |                |        | zero.                  |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+-----------------------------------+
   | Error Value                        | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed           |
   |                                    | successfully                      |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | -  If ``n`` < 0 or                |
   |                                    |                                   |
   |                                    | -  if ``incx`` == 0 or            |
   |                                    |                                   |
   |                                    | -  if ``uplo`` !=                 |
   |                                    |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                    |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                    |                                   |
   |                                    | -  if ``lda`` < max(1, ``n``) or  |
   |                                    |                                   |
   |                                    | -  ``alpha`` == NULL              |
   +------------------------------------+-----------------------------------+
   |                                    | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +------------------------------------+-----------------------------------+

mcblas<t>her2()
------------------

::

   mcblasStatus_t mcblasCher2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcComplex       *alpha,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *A, int lda)
   mcblasStatus_t mcblasZher2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex *A, int lda)

This function performs the Hermitian rank-2 update

.. math:: 
   A = \alpha\textbf{x}\textbf{y}^{H} + \overline{\alpha}\textbf{y}\textbf{x}^{H} + A

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in column-major format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
is a scalar.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | A      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``lda x n``  |
   |        |                |        | with                   |
   |        |                |        | ``lda>=max(1,n)``. The |
   |        |                |        | imaginary parts of the |
   |        |                |        | diagonal elements are  |
   |        |                |        | assumed and set to     |
   |        |                |        | zero.                  |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+-----------------------------------+
   | Error Value                        | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed           |
   |                                    | successfully                      |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | -  If ``n`` < 0 or                |
   |                                    |                                   |
   |                                    | -  if ``incx`` == 0 or ``incy``   |
   |                                    |    == 0 or                        |
   |                                    |                                   |
   |                                    | -  if ``uplo`` !=                 |
   |                                    |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                    |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                    |                                   |
   |                                    | -  if ``lda`` < max(1, ``n``) or  |
   |                                    |                                   |
   |                                    | -  ``alpha`` == NULL              |
   +------------------------------------+-----------------------------------+
   |                                    | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +------------------------------------+-----------------------------------+

mcblas<t>hpr()
----------------

::

   mcblasStatus_t mcblasChpr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const float *alpha,
                              const mcComplex       *x, int incx,
                              mcComplex       *AP)
   mcblasStatus_t mcblasZhpr(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const double *alpha,
                              const mcDoubleComplex *x, int incx,
                              mcDoubleComplex *AP)

This function performs the packed Hermitian rank-1 update

.. math::
   A = \alpha\textbf{x}\textbf{x}^{H} + A

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in packed format,
:math:`\mathbf{x}`
is a vector, and :math:`\alpha`
is a scalar.
If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | AP     | device         | in/out | <type> array with      |
   |        |                |        | ``A`` stored in packed |
   |        |                |        | format. The imaginary  |
   |        |                |        | parts of the diagonal  |
   |        |                |        | elements are assumed   |
   |        |                |        | and set to zero.       |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+-----------------------------------+
   | Error Value                        | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed           |
   |                                    | successfully                      |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | -  If ``n`` < 0 or                |
   |                                    |                                   |
   |                                    | -  if ``incx`` == 0 or            |
   |                                    |                                   |
   |                                    | -  if ``uplo`` !=                 |
   |                                    |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                    |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                    |                                   |
   |                                    | -  ``alpha`` == NULL              |
   +------------------------------------+-----------------------------------+
   |                                    | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +------------------------------------+-----------------------------------+

mcblas<t>hpr2()
-----------------

::

   mcblasStatus_t mcblasChpr2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcComplex       *alpha,
                              const mcComplex       *x, int incx,
                              const mcComplex       *y, int incy,
                              mcComplex       *AP)
   mcblasStatus_t mcblasZhpr2(mcblasHandle_t handle, mcblasFillMode_t uplo,
                              int n, const mcDoubleComplex *alpha,
                              const mcDoubleComplex *x, int incx,
                              const mcDoubleComplex *y, int incy,
                              mcDoubleComplex *AP)

This function performs the packed Hermitian rank-2 update

.. math:: 
   A = \alpha\textbf{x}\textbf{y}^{H} + \overline{\alpha}\textbf{y}\textbf{x}^{H} + A

where :math:`A`
is a :math:`n \times n`
Hermitian matrix stored in packed format,
:math:`\mathbf{x}`
and :math:`\mathbf{y}`
are vectors, and :math:`\alpha`
is a scalar.
If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements in
the lower triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+((2*n-j+1)*j)/2]``
for :math:`j = 1,\ldots,n`
and :math:`i \geq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.
If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the elements in
the upper triangular part of the Hermitian matrix
:math:`A`
are packed together column by column without gaps, so that
the element :math:`A(i,j)`
is stored in the memory location ``AP[i+(j*(j+1))/2]`` for
:math:`j = 1,\ldots,n`
and :math:`i \leq j`
. Consequently, the packed format requires only
:math:`\frac{n(n + 1)}{2}`
elements for storage.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows and     |
   |        |                |        | columns of matrix      |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | x      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incx   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``x``.              |
   +--------+----------------+--------+------------------------+
   | y      | device         | input  | <type> vector with     |
   |        |                |        | ``n`` elements.        |
   +--------+----------------+--------+------------------------+
   | incy   |                | input  | stride between         |
   |        |                |        | consecutive elements   |
   |        |                |        | of ``y``.              |
   +--------+----------------+--------+------------------------+
   | AP     | device         | in/out | <type> array with      |
   |        |                |        | ``A`` stored in packed |
   |        |                |        | format. The imaginary  |
   |        |                |        | parts of the diagonal  |
   |        |                |        | elements are assumed   |
   |        |                |        | and set to zero.       |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+-----------------------------------+
   | Error Value                        | Meaning                           |
   +====================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed           |
   |                                    | successfully                      |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | -  If ``n`` < 0 or                |
   |                                    |                                   |
   |                                    | -  if ``incx`` == 0 or ``incy``   |
   |                                    |    == 0 or                        |
   |                                    |                                   |
   |                                    | -  if ``uplo`` !=                 |
   |                                    |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                    |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                    |                                   |
   |                                    | -  ``alpha`` == NULL              |
   +------------------------------------+-----------------------------------+
   |                                    | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +------------------------------------+-----------------------------------+

mcblas<t>gemvBatched()
-----------------------

::

   mcblasStatus_t mcblasSgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                     int m, int n,
                                     const float           *alpha,
                                     const float           *Aarray[], int lda,
                                     const float           *xarray[], int incx,
                                     const float           *beta,
                                     float                 *yarray[], int incy,
                                     int batchCount)
   mcblasStatus_t mcblasDgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                     int m, int n,
                                     const double          *alpha,
                                     const double          *Aarray[], int lda,
                                     const double          *xarray[], int incx,
                                     const double          *beta,
                                     double                *yarray[], int incy,
                                     int batchCount)
   mcblasStatus_t mcblasCgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                     int m, int n,
                                     const mcComplex       *alpha,
                                     const mcComplex       *Aarray[], int lda,
                                     const mcComplex       *xarray[], int incx,
                                     const mcComplex       *beta,
                                     mcComplex             *yarray[], int incy,
                                     int batchCount)
   mcblasStatus_t mcblasZgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                     int m, int n,
                                     const mcDoubleComplex *alpha,
                                     const mcDoubleComplex *Aarray[], int lda,
                                     const mcDoubleComplex *xarray[], int incx,
                                     const mcDoubleComplex *beta,
                                     mcDoubleComplex       *yarray[], int incy,
                                     int batchCount)
   mcblasStatus_t mcblasHSHgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                       int m, int n,
                                       const float           *alpha,
                                       const mcblas_half     *Aarray[], int lda,
                                       const mcblas_half     *xarray[], int incx,
                                       const float           *beta,
                                       mcblas_half           *yarray[], int incy,
                                       int batchCount)
   mcblasStatus_t mcblasHSSgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                       int m, int n,
                                       const float           *alpha,
                                       const mcblas_half     *Aarray[], int lda,
                                       const mcblas_half     *xarray[], int incx,
                                       const float           *beta,
                                       float                 *yarray[], int incy,
                                       int batchCount)
   mcblasStatus_t mcblasTSTgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                       int m, int n,
                                       const float           *alpha,
                                       const mcblas_bfloat16 *Aarray[], int lda,
                                       const mcblas_bfloat16 *xarray[], int incx,
                                       const float           *beta,
                                       mcblas_bfloat16       *yarray[], int incy,
                                       int batchCount)
   mcblasStatus_t mcblasTSSgemvBatched(mcblasHandle_t handle, mcblasOperation_t trans,
                                       int m, int n,
                                       const float           *alpha,
                                       const mcblas_bfloat16 *Aarray[], int lda,
                                       const mcblas_bfloat16 *xarray[], int incx,
                                       const float           *beta,
                                       float                 *yarray[], int incy,
                                       int batchCount)

This function performs the matrix-vector multiplication of a
batch of matrices and vectors. The batch is considered to be
"uniform", i.e. all instances have the same dimensions (m,
n), leading dimension (lda), increments (incx, incy) and
transposition (trans) for their respective A matrix, x and y
vectors. The address of the input matrix and vector, and the
output vector of each instance of the batch are read from
arrays of pointers passed to the function by the caller.

.. math::
   y[i]=\alpha op(A[i])x[i]+\beta y[i],\ for\ i \in [0, batchCount - 1]

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
is an array of pointers to matrice
:math:`A\lbrack i\rbrack`
stored in column-major format with dimension
:math:`m \times n`
, and :math:`\textbf{x}`
and :math:`\textbf{y}`
are arrays of pointers to vectors. Also, for matrix
:math:`A\lbrack i\rbrack`
,

.. math:: 
   op(A[i]) =
   \begin{cases}
   A[i] & if \enspace trans == MCBLAS\_OP\_N \\
   A[i]^T & if \enspace trans == MCBLAS\_OP\_T \\
   A[i]^H & if \enspace trans == MCBLAS\_OP\_C
   \end{cases}

Note:
:math:`\textbf{y}\lbrack i\rbrack`
vectors must not overlap, i.e. the individual gemv
operations must be computable independently; otherwise,
undefined behavior is expected.
On certain problem sizes, it might be advantageous to make
multiple calls to ``mcblas<t>gemv`` in different MACA
streams, rather than use this API.

.. table:: 
   :widths: grid
   :align: left

   +-------------+-----------------+---------+------------------+
   | Param.      | Memory          | In/out  | Meaning          |
   +=============+=================+=========+==================+
   |  handle     |                 |  input  |  handle to the   |
   |             |                 |         |  mcBLAS library  |
   |             |                 |         |  context.        |
   +-------------+-----------------+---------+------------------+
   |  trans      |                 |  input  |  operation       |
   |             |                 |         |  op(``A[i]``)    |
   |             |                 |         |  that is non- or |
   |             |                 |         |  (conj.)         |
   |             |                 |         |  transpose.      |
   +-------------+-----------------+---------+------------------+
   |  m          |                 |  input  |  number of rows  |
   |             |                 |         |  of matrix       |
   |             |                 |         |  ``A[i]``.       |
   +-------------+-----------------+---------+------------------+
   |  n          |                 |  input  |  number of       |
   |             |                 |         |  columns of      |
   |             |                 |         |  matrix          |
   |             |                 |         |  ``A[i]``.       |
   +-------------+-----------------+---------+------------------+
   |  alpha      |  host or device |  input  |  <type> scalar   |
   |             |                 |         |  used for        |
   |             |                 |         |  multiplication. |
   +-------------+-----------------+---------+------------------+
   |  Aarray     |  device         |  input  |  array of        |
   |             |                 |         |  pointers to     |
   |             |                 |         |  <type> array,   |
   |             |                 |         |  with each array |
   |             |                 |         |  of dim.         |
   |             |                 |         |  ``lda x n``     |
   |             |                 |         |  with            |
   |             |                 |         |  ``l             |
   |             |                 |         |  da>=max(1,m)``. |
   |             |                 |         |                  |
   |             |                 |         |  All pointers    |
   |             |                 |         |  must meet       |
   |             |                 |         |  certain         |
   |             |                 |         |  alignment       |
   |             |                 |         |  criteria.       |
   |             |                 |         |  Please see      |
   |             |                 |         |  below for       |
   |             |                 |         |  details.        |
   +-------------+-----------------+---------+------------------+
   |  lda        |                 |  input  |  leading         |
   |             |                 |         |  dimension of    |
   |             |                 |         |  two-dimensional |
   |             |                 |         |  array used to   |
   |             |                 |         |  store each      |
   |             |                 |         |  matrix          |
   |             |                 |         |  ``A[i]``.       |
   +-------------+-----------------+---------+------------------+
   |  xarray     |  device         |  input  |  array of        |
   |             |                 |         |  pointers to     |
   |             |                 |         |  <type> array,   |
   |             |                 |         |  with each       |
   |             |                 |         |  dimension ``n`` |
   |             |                 |         |  if              |
   |             |                 |         |  ``trans         |
   |             |                 |         |  ==MCBLAS_OP_N`` |
   |             |                 |         |  and ``m``       |
   |             |                 |         |  otherwise.      |
   |             |                 |         |                  |
   |             |                 |         |  All pointers    |
   |             |                 |         |  must meet       |
   |             |                 |         |  certain         |
   |             |                 |         |  alignment       |
   |             |                 |         |  criteria.       |
   |             |                 |         |  Please see      |
   |             |                 |         |  below for       |
   |             |                 |         |  details.        |
   +-------------+-----------------+---------+------------------+
   |  incx       |                 |  input  |  stride of each  |
   |             |                 |         |  one-dimensional |
   |             |                 |         |  array x[i].     |
   +-------------+-----------------+---------+------------------+
   |  beta       |  host or device |  input  |  <type> scalar   |
   |             |                 |         |  used for        |
   |             |                 |         |  multiplication. |
   |             |                 |         |  If              |
   |             |                 |         |  ``beta == 0``,  |
   |             |                 |         |  ``y`` does not  |
   |             |                 |         |  have to be a    |
   |             |                 |         |  valid input.    |
   +-------------+-----------------+---------+------------------+
   |  yarray     |  device         |  in/out |  array of        |
   |             |                 |         |  pointers to     |
   |             |                 |         |  <type> array.   |
   |             |                 |         |  It has          |
   |             |                 |         |  dimensions      |
   |             |                 |         |  ``m`` if        |
   |             |                 |         |  ``trans         |
   |             |                 |         |  ==MCBLAS_OP_N`` |
   |             |                 |         |  and ``n``       |
   |             |                 |         |  otherwise.      |
   |             |                 |         |  Vectors         |
   |             |                 |         |  ``y[i]`` should |
   |             |                 |         |  not overlap;    |
   |             |                 |         |  otherwise,      |
   |             |                 |         |  undefined       |
   |             |                 |         |  behavior is     |
   |             |                 |         |  expected.       |
   |             |                 |         |                  |
   |             |                 |         |  All pointers    |
   |             |                 |         |  must meet       |
   |             |                 |         |  certain         |
   |             |                 |         |  alignment       |
   |             |                 |         |  criteria.       |
   |             |                 |         |  Please see      |
   |             |                 |         |  below for       |
   |             |                 |         |  details.        |
   +-------------+-----------------+---------+------------------+
   |  incy       |                 |  input  |  stride of each  |
   |             |                 |         |  one-dimensional |
   |             |                 |         |  array y[i].     |
   +-------------+-----------------+---------+------------------+
   |  batchCount |                 |  input  |  number of       |
   |             |                 |         |  pointers        |
   |             |                 |         |  contained in    |
   |             |                 |         |  Aarray, xarray  |
   |             |                 |         |  and yarray.     |
   +-------------+-----------------+---------+------------------+

If math mode enables fast math modes when using
``mcblasSgemvBatched()``, pointers (not the pointer
arrays) placed in the GPU memory must be properly aligned
to avoid misaligned memory access errors. Ideally all
pointers are aligned to at least 16 Bytes. Otherwise it
is recommended that they meet the following rule:

-  if ``k % 4==0`` then ensure ``intptr_t(ptr) % 16 == 0``,

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid
   :align: left

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |                                     |  the library was not initialized  |
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  the parameters                   |
   |                                     |  ``m,n,batchCount<0``             |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>gemvStridedBatched()
------------------------------
            
::

   mcblasStatus_t mcblasSgemvStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t trans,
                                            int m, int n,
                                            const float           *alpha,
                                            const float           *A, int lda,
                                            mcblas_stride         strideA,
                                            const float           *x, int incx,
                                            mcblas_stride         stridex,
                                            const float           *beta,
                                            float                 *y, int incy,
                                            mcblas_stride         stridey,
                                            int batchCount)
   mcblasStatus_t mcblasDgemvStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t trans,
                                            int m, int n,
                                            const double          *alpha,
                                            const double          *A, int lda,
                                            mcblas_stride         strideA,
                                            const double          *x, int incx,
                                            mcblas_stride         stridex,
                                            const double          *beta,
                                            double                *yarray[], int incy,
                                            mcblas_stride         stridey,
                                            int batchCount)
   mcblasStatus_t mcblasCgemvStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t trans,
                                            int m, int n,
                                            const mcComplex       *alpha,
                                            const mcComplex       *A, int lda,
                                            mcblas_stride         strideA,
                                            const mcComplex       *x, int incx,
                                            mcblas_stride         stridex,
                                            const mcComplex       *beta,
                                            mcComplex             *y, int incy,
                                            mcblas_stride         stridey,
                                            int batchCount)
   mcblasStatus_t mcblasZgemvStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t trans,
                                            int m, int n,
                                            const mcDoubleComplex *alpha,
                                            const mcDoubleComplex *A, int lda,
                                            mcblas_stride         strideA,
                                            const mcDoubleComplex *x, int incx,
                                            mcblas_stride         stridex,
                                            const mcDoubleComplex *beta,
                                            mcDoubleComplex       *y, int incy,
                                            mcblas_stride         stridey,
                                            int batchCount)
   mcblasStatus_t mcblasHSHgemvStridedBatched(mcblasHandle_t handle,
                                              mcblasOperation_t trans,
                                              int m, int n,
                                              const float         *alpha,
                                              const mcblas_half   *A, int lda,
                                              mcblas_stride       strideA,
                                              const mcblas_half   *x, int incx,
                                              mcblas_stride       stridex,
                                              const float         *beta,
                                              mcblas_half         *y, int incy,
                                              mcblas_stride       stridey,
                                              int batchCount)
   mcblasStatus_t mcblasHSSgemvStridedBatched(mcblasHandle_t handle,
                                              mcblasOperation_t trans,
                                              int m, int n,
                                              const float         *alpha,
                                              const mcblas_half   *A, int lda,
                                              mcblas_stride       strideA,
                                              const mcblas_half   *x, int incx,
                                              mcblas_stride       stridex,
                                              const float         *beta,
                                              float               *y, int incy,
                                              mcblas_stride       stridey,
                                              int batchCount)
   mcblasStatus_t mcblasTSTgemvStridedBatched(mcblasHandle_t handle,
                                              mcblasOperation_t trans,
                                              int m, int n,
                                              const float         *alpha,
                                              const mc_bfloat16   *A, int lda,
                                              mcblas_stride       strideA,
                                              const mc_bfloat16   *x, int incx,
                                              mcblas_stride       stridex,
                                              const float         *beta,
                                              mc_bfloat16         *y, int incy,
                                              mcblas_stride       stridey,
                                              int batchCount)
   mcblasStatus_t mcblasTSSgemvStridedBatched(mcblasHandle_t handle,
                                              mcblasOperation_t trans,
                                              int m, int n,
                                              const float         *alpha,
                                              const mc_bfloat16   *A, int lda,
                                              mcblas_stride       strideA,
                                              const mc_bfloat16   *x, int incx,
                                              mcblas_stride       stridex,
                                              const float         *beta,
                                              float               *y, int incy,
                                              mcblas_stride       stridey,
                                              int batchCount)

This function performs the matrix-vector multiplication of a
batch of matrices and vectors. The batch is considered to be
"uniform", i.e. all instances have the same dimensions (m,
n), leading dimension (lda), increments (incx, incy) and
transposition (trans) for their respective A matrix, x and y
vectors. Input matrix A and vector x, and output vector y
for each instance of the batch are located at fixed offsets
in number of elements from their locations in the previous
instance. Pointers to A matrix, x and y vectors for the
first instance are passed to the function by the user along
with offsets in number of elements - strideA, stridex and
stridey that determine the locations of input matrices and
vectors, and output vectors in future instances.

.. math::
   \begin{gathered}
   \textbf{y} + i*{stridey} = \alpha\text{op}(A + i*{strideA})(\textbf{x} + i*{stridex}) + \beta(\textbf{y} + i*{stridey}), \\
   \text{for i} \in \lbrack 0,batchCount - 1\rbrack
   \end{gathered}

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
is an array of pointers to matrix stored in column-major
format with dimension
:math:`A\lbrack i\rbrack`
:math:`m \times n`
, and :math:`\textbf{x}`
and :math:`\textbf{y}`
are arrays of pointers to vectors. Also, for matrix
:math:`A\lbrack i\rbrack`

.. math::
   op(A\left[i \right]) = \begin{cases}
   A\left[i \right] & if \enspace trans == MCBLAS\_OP\_N \\
   A\left[i \right]^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A\left[i \right]^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{cases}

Note:
:math:`\textbf{y}\lbrack i\rbrack`
matrices must not overlap, i.e. the individual gemv
operations must be computable independently; otherwise,
undefined behavior is expected.
On certain problem sizes, it might be advantageous to make
multiple calls to ``mcblas<t>gemv`` in different MACA
streams, rather than use this API.

Note: In the table below, we use ``A[i], x[i], y[i]`` as
notation for A matrix, and x and y vectors in the ith
instance of the batch, implicitly assuming they are
respectively offsets in number of elements
``strideA, stridex, stridey`` away from
``A[i-1], x[i-1], y[i-1]``. The unit for the offset is
number of elements and must not be zero .

.. table:: 
   :widths: grid

   +------------+----------------+--------+------------------------+
   | Param.     | Memory         | In/out | Meaning                |
   +============+================+========+========================+
   | handle     |                | input  | handle to the mcBLAS   |
   |            |                |        | library context.       |
   +------------+----------------+--------+------------------------+
   | trans      |                | input  | operation              |
   |            |                |        | op(``A[i]``) that is   |
   |            |                |        | non- or (conj.)        |
   |            |                |        | transpose.             |
   +------------+----------------+--------+------------------------+
   | m          |                | input  | number of rows of      |
   |            |                |        | matrix ``A[i]``.       |
   +------------+----------------+--------+------------------------+
   | n          |                | input  | number of columns of   |
   |            |                |        | matrix ``A[i]``.       |
   +------------+----------------+--------+------------------------+
   | alpha      | host or device | input  | <type> scalar used     |
   |            |                |        | for multiplication.    |
   +------------+----------------+--------+------------------------+
   | A          | device         | input  | <type>\* pointer to    |
   |            |                |        | the A matrix           |
   |            |                |        | corresponding to the   |
   |            |                |        | first instance of      |
   |            |                |        | the batch, with        |
   |            |                |        | dimensions             |
   |            |                |        | ``lda x n`` with       |
   |            |                |        | ``lda>=max(1,m)``.     |
   +------------+----------------+--------+------------------------+
   | lda        |                | input  | leading dimension of   |
   |            |                |        | two-dimensional        |
   |            |                |        | array used to store    |
   |            |                |        | each matrix            |
   |            |                |        | ``A[i]``.              |
   +------------+----------------+--------+------------------------+
   | strideA    |                | input  | Value of type long     |
   |            |                |        | long int that gives    |
   |            |                |        | the offset in number   |
   |            |                |        | of elements between    |
   |            |                |        | ``A[i]`` and           |
   |            |                |        | ``A[i+1]``             |
   +------------+----------------+--------+------------------------+
   | x          | device         | input  | <type>\* pointer to    |
   |            |                |        | the x vector           |
   |            |                |        | corresponding to the   |
   |            |                |        | first instance of      |
   |            |                |        | the batch, with each   |
   |            |                |        | dimension ``n`` if     |
   |            |                |        | ``trans==MCBLAS_OP_N`` |
   |            |                |        | and ``m`` otherwise.   |
   +------------+----------------+--------+------------------------+
   | incx       |                | input  | stride of each         |
   |            |                |        | one-dimensional        |
   |            |                |        | array x[i].            |
   +------------+----------------+--------+------------------------+
   | stridex    |                | input  | Value of type long     |
   |            |                |        | long int that gives    |
   |            |                |        | the offset in number   |
   |            |                |        | of elements between    |
   |            |                |        | ``x[i]`` and           |
   |            |                |        | ``x[i+1]``             |
   +------------+----------------+--------+------------------------+
   | beta       | host or device | input  | <type> scalar used     |
   |            |                |        | for multiplication.    |
   |            |                |        | If ``beta == 0``,      |
   |            |                |        | ``y`` does not have    |
   |            |                |        | to be a valid input.   |
   +------------+----------------+--------+------------------------+
   | y          | device         | in/out | <type>\* pointer to    |
   |            |                |        | the y vector           |
   |            |                |        | corresponding to the   |
   |            |                |        | first instance of      |
   |            |                |        | the batch, with each   |
   |            |                |        | dimension ``m`` if     |
   |            |                |        | ``trans==MCBLAS_OP_N`` |
   |            |                |        | and ``n`` otherwise.   |
   |            |                |        | Vectors ``y[i]``       |
   |            |                |        | should not overlap;    |
   |            |                |        | otherwise, undefined   |
   |            |                |        | behavior is            |
   |            |                |        | expected.              |
   +------------+----------------+--------+------------------------+
   | incy       |                | input  | stride of each         |
   |            |                |        | one-dimensional        |
   |            |                |        | array y[i].            |
   +------------+----------------+--------+------------------------+
   | stridey    |                | input  | Value of type long     |
   |            |                |        | long int that gives    |
   |            |                |        | the offset in number   |
   |            |                |        | of elements between    |
   |            |                |        | ``y[i]`` and           |
   |            |                |        | ``y[i+1]``             |
   +------------+----------------+--------+------------------------+
   | batchCount |                | input  | number of GEMVs to     |
   |            |                |        | perform in the         |
   |            |                |        | batch.                 |
   +------------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+---------------------------------------------+
   | Error Value                       | Meaning                                     |
   +===================================+=============================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed successfully        |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized             |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | the parameters ``m,n,batchCount<0``         |
   +-----------------------------------+---------------------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on the GPU    |
   +-----------------------------------+---------------------------------------------+

mcBLAS Level-3 Functions
==========================

In this chapter we describe the Level-3 Basic Linear Algebra
Subprograms (BLAS3) functions that perform matrix-matrix
operations.

mcblas<t>gemm()
----------------

::

   mcblasStatus_t mcblasSgemm(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n, int k,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *B, int ldb,
                              const float           *beta,
                              float                 *C, int ldc)
   mcblasStatus_t mcblasDgemm(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n, int k,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *B, int ldb,
                              const double          *beta,
                              double                *C, int ldc)
   mcblasStatus_t mcblasCgemm(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n, int k,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *B, int ldb,
                              const mcComplex       *beta,
                              mcComplex             *C, int ldc)
   mcblasStatus_t mcblasZgemm(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n, int k,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *B, int ldb,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex       *C, int ldc)
   mcblasStatus_t mcblasHgemm(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n, int k,
                              const mcblas_half     *alpha,
                              const mcblas_half     *A, int lda,
                              const mcblas_half     *B, int ldb,
                              const mcblas_half     *beta,
                              mcblas_half           *C, int ldc)

This function performs the matrix-matrix multiplication

.. math::
   C = \alpha\text{op}(A)\text{op}(B) + \beta C

where :math:`\alpha` and :math:`\beta` are scalars, and :math:`A`, :math:`B`
and :math:`C` are matrices stored in column-major format with dimensions
:math:`\text{op}(A)` :math:`m \times k`, :math:`\text{op}(B)` :math:`k \times n`
and :math:`C` :math:`m \times n`, respectively.
Also, for matrix :math:`A`,

.. math::
   op(A) = \left\{ \begin{array}{ll}
   A     & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{array} \right.

and :math:`\text{op}(B)` is defined similarly for matrix :math:`B`.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------------+
   | Param.  | Memory          | In/out  | Meaning                       |
   +=========+=================+=========+===============================+
   | handle  |                 | input   | handle to the mcBLAS          |
   |         |                 |         | library context.              |
   +---------+-----------------+---------+-------------------------------+
   | transa  |                 | input   | operation op(``A``)           |
   |         |                 |         | that is non- or               |
   |         |                 |         | (conj.) transpose.            |
   +---------+-----------------+---------+-------------------------------+
   | transb  |                 | input   |  operation op(``B``)          |
   |         |                 |         |  that is non- or              |
   |         |                 |         |  (conj.) transpose.           |
   +---------+-----------------+---------+-------------------------------+
   |  m      |                 | input   | number of rows of             |
   |         |                 |         | matrix op(``A``) and          |
   |         |                 |         | ``C``.                        |
   +---------+-----------------+---------+-------------------------------+
   |  n      |                 | input   |  number of columns of         |
   |         |                 |         |  matrix op(``B``) and         |
   |         |                 |         |  ``C``.                       |
   +---------+-----------------+---------+-------------------------------+
   |  k      |                 |  input  |  number of columns of         |
   |         |                 |         |  op(``A``) and rows of        |
   |         |                 |         |  op(``B``).                   |
   +---------+-----------------+---------+-------------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for       |
   |         |                 |         |  multiplication.              |
   +---------+-----------------+---------+-------------------------------+
   |  A      |  device         |  input  |  <type> array of              |
   |         |                 |         |  dimensions ``lda x k``       |
   |         |                 |         |  with ``lda>=max(1,m)``       |
   |         |                 |         |  if ``transa == MCBLAS_OP_N`` |
   |         |                 |         |  and ``lda x m`` with         |
   |         |                 |         |  ``lda>=max(1,k)``            |
   |         |                 |         |  otherwise.                   |
   +---------+-----------------+---------+-------------------------------+
   |  lda    |                 |  input  |  leading dimension of         |
   |         |                 |         |  two-dimensional array        |
   |         |                 |         |  used to store the            |
   |         |                 |         |  matrix ``A``.                |
   +---------+-----------------+---------+-------------------------------+
   |  B      |  device         |  input  |  <type> array of              |
   |         |                 |         |  dimensions ``ldb x n``       |
   |         |                 |         |  with ``ldb>=max(1,k)``       |
   |         |                 |         |  if                           |
   |         |                 |         |  ``transb == MCBLAS_OP_N``    |
   |         |                 |         |  and ``ldb x k`` with         |
   |         |                 |         |  ``ldb>=max(1,n)``            |
   |         |                 |         |  otherwise.                   |
   +---------+-----------------+---------+-------------------------------+
   |  ldb    |                 |  input  |  leading dimension of         |
   |         |                 |         |  two-dimensional array        |
   |         |                 |         |  used to store matrix         |
   |         |                 |         |  ``B``.                       |
   +---------+-----------------+---------+-------------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for       |
   |         |                 |         |  multiplication. If           |
   |         |                 |         |  ``beta==0``, ``C``           |
   |         |                 |         |  does not have to be a        |
   |         |                 |         |  valid input.                 |
   +---------+-----------------+---------+-------------------------------+
   |  C      |  device         |  in/out |  <type> array of              |
   |         |                 |         |  dimensions ``ldc x n``       |
   |         |                 |         |  with ``ldc>=max(1,m)``.      |
   +---------+-----------------+---------+-------------------------------+
   |  ldc    |                 |  input  |  leading dimension of a       |
   |         |                 |         |  two-dimensional array        |
   |         |                 |         |  used to store the            |
   |         |                 |         |  matrix ``C``.                |
   +---------+-----------------+---------+-------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_NOT_INITIALIZED``  | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    | - if ``m``, ``n``, ``k`` < 0 or   |
   |                                     | - if ``transa``, ``transb`` !=    |
   |                                     |   ``MCBLAS_OP_N``,                |
   |                                     |   ``MCBLAS_OP_C``,                |
   |                                     |   ``MCBLAS_OP_T`` or              |
   |                                     | - if ``lda`` < max(1, ``m``) if   |
   |                                     |   ``transa`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``lda`` < max(1, ``k``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldb`` < max(1, ``k``) if   |
   |                                     |   ``transb`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``ldb`` < max(1, ``n``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldc`` < max(1, ``m``) or   |
   |                                     | - if ``alpha``, ``beta`` == NULL  |
   |                                     |   or                              |
   |                                     | - ``C`` == NULL if ``C`` needs    |
   |                                     |   to be scaled                    |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_ARCH_MISMATCH``    |  in the case of ``mcblasHgemm``   |
   |                                     |  the device does not support math |
   |                                     |  in half precision                |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>gemm3m()
-------------------

::

   mcblasStatus_t mcblasCgemm3m(mcblasHandle_t handle,
                                mcblasOperation_t transa, mcblasOperation_t transb,
                                int m, int n, int k,
                                const mcComplex       *alpha,
                                const mcComplex       *A, int lda,
                                const mcComplex       *B, int ldb,
                                const mcComplex       *beta,
                                mcComplex             *C, int ldc)
   mcblasStatus_t mcblasZgemm3m(mcblasHandle_t handle,
                                mcblasOperation_t transa, mcblasOperation_t transb,
                                int m, int n, int k,
                                const mcDoubleComplex *alpha,
                                const mcDoubleComplex *A, int lda,
                                const mcDoubleComplex *B, int ldb,
                                const mcDoubleComplex *beta,
                                mcDoubleComplex       *C, int ldc)

This function performs the complex matrix-matrix multiplication,
using Gauss complexity reduction algorithm.
This can lead to an increase in performance up to 25%.

.. math::
   C = \alpha\text{op}(A)\text{op}(B) + \beta C

where :math:`\alpha` and :math:`\beta` are scalars,
and :math:`A`, :math:`B` and :math:`C`
are matrices stored in column-major format with dimensions
:math:`\text{op}(A)` :math:`m \times k`,
:math:`\text{op}(B)` :math:`k \times n` and
:math:`C` :math:`m \times n`, respectively.
Also, for matrix :math:`A`,

.. math::
   op(A) = \left\{ \begin{array}{ll}
   A     &  if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{array} \right.

and :math:`\text{op}(B)` is defined similarly for matrix :math:`B`.

.. table::
   :widths: grid

   +---------+-----------------+---------+----------------------------+
   | Param.  | Memory          | In/out  | Meaning                    |
   +=========+=================+=========+============================+
   |  handle |                 |  input  |  handle to the mcBLAS      |
   |         |                 |         |  library context.          |
   +---------+-----------------+---------+----------------------------+
   |  transa |                 |  input  |  operation op(``A``)       |
   |         |                 |         |  that is non- or           |
   |         |                 |         |  (conj.) transpose.        |
   +---------+-----------------+---------+----------------------------+
   |  transb |                 |  input  |  operation op(``B``)       |
   |         |                 |         |  that is non- or           |
   |         |                 |         |  (conj.) transpose.        |
   +---------+-----------------+---------+----------------------------+
   |  m      |                 |  input  |  number of rows of         |
   |         |                 |         |  matrix op(``A``) and      |
   |         |                 |         |  ``C``.                    |
   +---------+-----------------+---------+----------------------------+
   |  n      |                 |  input  |  number of columns of      |
   |         |                 |         |  matrix op(``B``) and      |
   |         |                 |         |  ``C``.                    |
   +---------+-----------------+---------+----------------------------+
   |  k      |                 |  input  |  number of columns of      |
   |         |                 |         |  op(``A``) and rows of     |
   |         |                 |         |  op(``B``).                |
   +---------+-----------------+---------+----------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for    |
   |         |                 |         |  multiplication.           |
   +---------+-----------------+---------+----------------------------+
   |  A      |  device         |  input  |  <type> array of           |
   |         |                 |         |  dimensions ``lda x k``    |
   |         |                 |         |  with ``lda>=max(1,m)``    |
   |         |                 |         |  if                        |
   |         |                 |         |  ``transa == MCBLAS_OP_N`` |
   |         |                 |         |  and ``lda x m`` with      |
   |         |                 |         |  ``lda>=max(1,k)``         |
   |         |                 |         |  otherwise.                |
   +---------+-----------------+---------+----------------------------+
   |  lda    |                 |  input  |  leading dimension of      |
   |         |                 |         |  two-dimensional array     |
   |         |                 |         |  used to store the         |
   |         |                 |         |  matrix ``A``.             |
   +---------+-----------------+---------+----------------------------+
   |  B      |  device         |  input  |  <type> array of           |
   |         |                 |         |  dimension ``ldb x n``     |
   |         |                 |         |  with ``ldb>=max(1,k)``    |
   |         |                 |         |  if                        |
   |         |                 |         |  ``transb == MCBLAS_OP_N`` |
   |         |                 |         |  and ``ldb x k`` with      |
   |         |                 |         |  ``ldb>=max(1,n)``         |
   |         |                 |         |  otherwise.                |
   +---------+-----------------+---------+----------------------------+
   |  ldb    |                 |  input  |  leading dimension of      |
   |         |                 |         |  two-dimensional array     |
   |         |                 |         |  used to store matrix      |
   |         |                 |         |  ``B``.                    |
   +---------+-----------------+---------+----------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for    |
   |         |                 |         |  multiplication. If        |
   |         |                 |         |  ``beta==0``, ``C``        |
   |         |                 |         |  does not have to be a     |
   |         |                 |         |  valid input.              |
   +---------+-----------------+---------+----------------------------+
   |  C      |  device         |  in/out |  <type> array of           |
   |         |                 |         |  dimensions ``ldc x n``    |
   |         |                 |         |  with                      |
   |         |                 |         |  ``ldc>=max(1,m)``.        |
   +---------+-----------------+---------+----------------------------+
   |  ldc    |                 |  input  |  leading dimension of a    |
   |         |                 |         |  two-dimensional array     |
   |         |                 |         |  used to store the         |
   |         |                 |         |  matrix ``C``.             |
   +---------+-----------------+---------+----------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    | - if ``m``, ``n``, ``k`` < 0 or   |
   |                                     | - if ``transa``, ``transb`` !=    |
   |                                     |   ``MCBLAS_OP_N``,                |
   |                                     |   ``MCBLAS_OP_C``,                |
   |                                     |   ``MCBLAS_OP_T`` or              |
   |                                     | - if ``lda`` < max(1, ``m``) if   |
   |                                     |   ``transa`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``lda`` < max(1, ``k``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldb`` < max(1, ``k``) if   |
   |                                     |   ``transb`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``ldb`` < max(1, ``n``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldc`` < max(1, ``m``) or   |
   |                                     | - if ``alpha``, ``beta`` == NULL  |
   |                                     |   or                              |
   |                                     | - ``C`` == NULL if ``C`` needs    |
   |                                     |   to be scaled                    |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_ARCH_MISMATCH``    |  the device is not supported      |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>gemmBatched()
-----------------------

This routine is not supported now.

mcblas<t>gemmStridedBatched()
------------------------------

::

   mcblasStatus_t mcblasHgemmStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t transa,
                                            mcblasOperation_t transb,
                                            int m, int n, int k,
                                            const mcblas_half     *alpha,
                                            const mcblas_half     *A, int lda,
                                            mcblas_stride          strideA,
                                            const mcblas_half     *B, int ldb,
                                            mcblas_stride          strideB,
                                            const mcblas_half     *beta,
                                            mcblas_half           *C, int ldc,
                                            mcblas_stride          strideC,
                                            int batchCount)
   mcblasStatus_t mcblasSgemmStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t transa,
                                            mcblasOperation_t transb,
                                            int m, int n, int k,
                                            const float           *alpha,
                                            const float           *A, int lda,
                                            mcblas_stride          strideA,
                                            const float           *B, int ldb,
                                            mcblas_stride          strideB,
                                            const float           *beta,
                                            float                 *C, int ldc,
                                            mcblas_stride          strideC,
                                            int batchCount)
   mcblasStatus_t mcblasDgemmStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t transa,
                                            mcblasOperation_t transb,
                                            int m, int n, int k,
                                            const double          *alpha,
                                            const double          *A, int lda,
                                            mcblas_stride          strideA,
                                            const double          *B, int ldb,
                                            mcblas_stride          strideB,
                                            const double          *beta,
                                            double                *C, int ldc,
                                            mcblas_stride          strideC,
                                            int batchCount)
   mcblasStatus_t mcblasCgemmStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t transa,
                                            mcblasOperation_t transb,
                                            int m, int n, int k,
                                            const mcComplex       *alpha,
                                            const mcComplex       *A, int lda,
                                            mcblas_stride          strideA,
                                            const mcComplex       *B, int ldb,
                                            mcblas_stride          strideB,
                                            const mcComplex       *beta,
                                            mcComplex             *C, int ldc,
                                            mcblas_stride          strideC,
                                            int batchCount)
   mcblasStatus_t mcblasCgemm3mStridedBatched(mcblasHandle_t handle,
                                              mcblasOperation_t transa,
                                              mcblasOperation_t transb,
                                              int m, int n, int k,
                                              const mcComplex       *alpha,
                                              const mcComplex       *A, int lda,
                                              mcblas_stride          strideA,
                                              const mcComplex       *B, int ldb,
                                              mcblas_stride          strideB,
                                              const mcComplex       *beta,
                                              mcComplex             *C, int ldc,
                                              mcblas_stride          strideC,
                                              int batchCount)
   mcblasStatus_t mcblasZgemmStridedBatched(mcblasHandle_t handle,
                                            mcblasOperation_t transa,
                                            mcblasOperation_t transb,
                                            int m, int n, int k,
                                            const mcDoubleComplex *alpha,
                                            const mcDoubleComplex *A, int lda,
                                            mcblas_stride          strideA,
                                            const mcDoubleComplex *B, int ldb,
                                            mcblas_stride          strideB,
                                            const mcDoubleComplex *beta,
                                            mcDoubleComplex       *C, int ldc,
                                            mcblas_stride          strideC,
                                            int batchCount)

This function performs the matrix-matrix multiplication of a batch of matrices.
The batch is considered to be "uniform", i.e. all instances have the same dimensions (m, n, k),
leading dimensions (lda, ldb, ldc) and transpositions (transa, transb) for their respective A, B and C matrices.
Input matrices A, B and output matrix C for each instance of the batch are located
at fixed offsets in number of elements from their locations in the previous instance.
Pointers to A, B and C matrices for the first instance are passed to the function by
the user along with offsets in number of elements - strideA, strideB and strideC
that determine the locations of input and output matrices in future instances.

.. math::
   \begin{gathered}
   C + i*{strideC} = \alpha\text{op}(A + i*{strideA})\text{op}(B + i*{strideB}) + \beta(C + i*{strideC}), \\
   \text{for i} \in \lbrack 0, batchCount - 1\rbrack
   \end{gathered}

where :math:`\alpha` and :math:`\beta` are scalars,
and :math:`A`, :math:`B` and :math:`C`
are arrays of pointers to matrices stored in column-major format with dimensions
:math:`\text{op}(A\lbrack i\rbrack)` :math:`m \times k`,
:math:`\text{op}(B\lbrack i\rbrack)` :math:`k \times n` and
:math:`C\lbrack i\rbrack` :math:`m \times n`, respectively.
Also, for matrix :math:`A\lbrack i\rbrack`,

.. math::
   op(A\left[ i \right]) = \left\{ \begin{array}{ll}
   A\left[i \right] &  if \enspace transa == MCBLAS\_OP\_N \\
   A\left[i \right]^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A\left[i \right]^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{array} \right.

and :math:`\text{op}(B\lbrack i\rbrack)`
is defined similarly for matrix :math:`B\lbrack i\rbrack`.

**Note**: :math:`C\lbrack i\rbrack` matrices must not overlap, i.e.
the individual gemm operations must be computable independently;
otherwise, undefined behavior is expected.

On certain problem sizes, it might be advantageous to make
multiple calls to ``mcblas<t>gemm`` in different mcStreams, rather than use this API.

**Note**: In the table below, we use ``A[i], B[i], C[i]`` as
notation for A, B and C matrices in the ith instance of the
batch, implicitly assuming they are respectively offsets in
number of elements ``strideA, strideB, strideC`` away from
``A[i-1], B[i-1], C[i-1]``. The unit for the offset is
number of elements and must not be zero .

.. table::
   :widths: grid

   +-------------+-----------------+---------+----------------------------------+
   | Param.      | Memory          | In/out  | Meaning                          |
   +=============+=================+=========+==================================+
   |  handle     |                 |  input  |  handle to the mcBLAS            |
   |             |                 |         |  library context.                |
   +-------------+-----------------+---------+----------------------------------+
   |  transa     |                 |  input  |  operation                       |
   |             |                 |         |  op(``A[i]``) that is            |
   |             |                 |         |  non- or (conj.)                 |
   |             |                 |         |  transpose.                      |
   +-------------+-----------------+---------+----------------------------------+
   |  transb     |                 |  input  |  operation                       |
   |             |                 |         |  op(``B[i]``) that is            |
   |             |                 |         |  non- or (conj.)                 |
   |             |                 |         |  transpose.                      |
   +-------------+-----------------+---------+----------------------------------+
   |  m          |                 |  input  |  number of rows of               |
   |             |                 |         |  matrix op(``A[i]``)             |
   |             |                 |         |  and ``C[i]``.                   |
   +-------------+-----------------+---------+----------------------------------+
   |  n          |                 |  input  |  number of columns of            |
   |             |                 |         |  op(``B[i]``) and                |
   |             |                 |         |  ``C[i]``.                       |
   +-------------+-----------------+---------+----------------------------------+
   |  k          |                 |  input  |  number of columns of            |
   |             |                 |         |  op(``A[i]``) and                |
   |             |                 |         |  rows of                         |
   |             |                 |         |  op(``B[i]``).                   |
   +-------------+-----------------+---------+----------------------------------+
   |  alpha      |  host or device |  input  |  <type> scalar used              |
   |             |                 |         |  for multiplication.             |
   +-------------+-----------------+---------+----------------------------------+
   |  A          |  device         |  input  |  <type>\* pointer to             |
   |             |                 |         |  the A matrix                    |
   |             |                 |         |  corresponding to the            |
   |             |                 |         |  first instance of               |
   |             |                 |         |  the batch, with                 |
   |             |                 |         |  dimensions                      |
   |             |                 |         |  ``lda x k`` with                |
   |             |                 |         |  ``lda>=max(1,m)`` if            |
   |             |                 |         |  ``transa==MCBLAS_OP_N``         |
   |             |                 |         |  and ``lda x m`` with            |
   |             |                 |         |  ``lda>=max(1,k)``               |
   |             |                 |         |  otherwise.                      |
   +-------------+-----------------+---------+----------------------------------+
   |  lda        |                 |  input  |  leading dimension of            |
   |             |                 |         |  two-dimensional                 |
   |             |                 |         |  array used to store             |
   |             |                 |         |  each matrix                     |
   |             |                 |         |  ``A[i]``.                       |
   +-------------+-----------------+---------+----------------------------------+
   |  strideA    |                 |  input  |  value of type long              |
   |             |                 |         |  long int that gives             |
   |             |                 |         |  the offset in number            |
   |             |                 |         |  of elements between             |
   |             |                 |         |  ``A[i]`` and                    |
   |             |                 |         |  ``A[i+1]``                      |
   +-------------+-----------------+---------+----------------------------------+
   |  B          |  device         |  input  |  <type>\* pointer to             |
   |             |                 |         |  the B matrix                    |
   |             |                 |         |  corresponding to the            |
   |             |                 |         |  first instance of               |
   |             |                 |         |  the batch, with                 |
   |             |                 |         |  dimensions                      |
   |             |                 |         |  ``ldb x n`` with                |
   |             |                 |         |  ``ldb>=max(1,k)`` if            |
   |             |                 |         |  ``transb==MCBLAS_OP_N``         |
   |             |                 |         |  and ``ldb x k`` with            |
   |             |                 |         |  ``ldb>=max(1,n)``               |
   |             |                 |         |  otherwise.                      |
   +-------------+-----------------+---------+----------------------------------+
   |  ldb        |                 |  input  |  leading dimension of            |
   |             |                 |         |  two-dimensional                 |
   |             |                 |         |  array used to store             |
   |             |                 |         |  each matrix                     |
   |             |                 |         |  ``B[i]``.                       |
   +-------------+-----------------+---------+----------------------------------+
   |  strideB    |                 |  input  |  value of type long              |
   |             |                 |         |  long int that gives             |
   |             |                 |         |  the offset in number            |
   |             |                 |         |  of elements between             |
   |             |                 |         |  ``B[i]`` and                    |
   |             |                 |         |  ``B[i+1]``                      |
   +-------------+-----------------+---------+----------------------------------+
   |  beta       |  host or device |  input  |  <type> scalar used              |
   |             |                 |         |  for multiplication.             |
   |             |                 |         |  If ``beta == 0``,               |
   |             |                 |         |  ``C`` does not have             |
   |             |                 |         |  to be a valid input.            |
   +-------------+-----------------+---------+----------------------------------+
   |  C          |  device         |  in/out |  <type>\* pointer to             |
   |             |                 |         |  the C matrix                    |
   |             |                 |         |  corresponding to the            |
   |             |                 |         |  first instance of               |
   |             |                 |         |  the batch, with                 |
   |             |                 |         |  dimensions                      |
   |             |                 |         |  ``ldc x n`` with                |
   |             |                 |         |  ``ldc>=max(1,m)``.              |
   |             |                 |         |  Matrices ``C[i]``               |
   |             |                 |         |  should not overlap;             |
   |             |                 |         |  otherwise, undefined            |
   |             |                 |         |  behavior is                     |
   |             |                 |         |  expected.                       |
   +-------------+-----------------+---------+----------------------------------+
   |  ldc        |                 |  input  |  leading dimension of            |
   |             |                 |         |  two-dimensional                 |
   |             |                 |         |  array used to store             |
   |             |                 |         |  each matrix                     |
   |             |                 |         |  ``C[i]``.                       |
   +-------------+-----------------+---------+----------------------------------+
   |  strideC    |                 |  input  |  value of type long              |
   |             |                 |         |  long int that gives             |
   |             |                 |         |  the offset in number            |
   |             |                 |         |  of elements between             |
   |             |                 |         |  ``C[i]`` and                    |
   |             |                 |         |  ``C[i+1]``                      |
   +-------------+-----------------+---------+----------------------------------+
   |  batchCount |                 |  input  |  number of GEMMs to              |
   |             |                 |         |  perform in the                  |
   |             |                 |         |  batch.                          |
   +-------------+-----------------+---------+----------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    | - if ``m``, ``n``, ``k``,         |
   |                                     |   ``batchCount`` < 0 or           |
   |                                     | - if ``transa``, ``transb`` !=    |
   |                                     |   ``MCBLAS_OP_N``,                |
   |                                     |   ``MCBLAS_OP_C``,                |
   |                                     |   ``MCBLAS_OP_T`` or              |
   |                                     | - if ``lda`` < max(1, ``m``) if   |
   |                                     |   ``transa`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``lda`` < max(1, ``k``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldb`` < max(1, ``k``) if   |
   |                                     |   ``transb`` == ``MCBLAS_OP_N``   |
   |                                     |   and ``ldb`` < max(1, ``n``)     |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldc`` < max(1, ``m``)      |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_ARCH_MISMATCH``    |  the device is not supported      |
   +-------------------------------------+-----------------------------------+

mcblas<t>symm()
-----------------

::

   mcblasStatus_t mcblasSsymm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *B, int ldb,
                              const float           *beta,
                              float                 *C, int ldc)
   mcblasStatus_t mcblasDsymm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *B, int ldb,
                              const double          *beta,
                              double                *C, int ldc)
   mcblasStatus_t mcblasCsymm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *B, int ldb,
                              const mcComplex       *beta,
                              mcComplex             *C, int ldc)
   mcblasStatus_t mcblasZsymm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *B, int ldb,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex       *C, int ldc)

This function performs the symmetric matrix-matrix multiplication

.. math::
   C = \left\{ \begin{array}{ll}
   {\alpha AB + \beta C} & if \enspace side == MCBLAS\_SIDE\_LEFT \\
   {\alpha BA + \beta C} & if \enspace side == MCBLAS\_SIDE\_RIGHT \\
   \end{array} \right.

where :math:`A` is a symmetric matrix stored in lower or upper mode,
:math:`B` and :math:`C` are :math:`m \times n` matrices, and
:math:`\alpha` and :math:`\beta` are scalars.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  side   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` is on the left   |
   |         |                 |         |  or right of ``B``.     |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other symmetric part   |
   |         |                 |         |  is not referenced and  |
   |         |                 |         |  is inferred from the   |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  m      |                 |  input  |  number of rows of      |
   |         |                 |         |  matrix ``C`` and       |
   |         |                 |         |  ``B``, with matrix     |
   |         |                 |         |  ``A`` sized            |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of columns of   |
   |         |                 |         |  matrix ``C`` and       |
   |         |                 |         |  ``B``, with matrix     |
   |         |                 |         |  ``A`` sized            |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x m``  |
   |         |                 |         |  with ``lda>=max(1,m)`` |
   |         |                 |         |  if                     |
   |         |                 |         |  ``side                 |
   |         |                 |         |  == MCBLAS_SIDE_LEFT``  |
   |         |                 |         |  and ``lda x n`` with   |
   |         |                 |         |  ``lda>=max(1,n)``      |
   |         |                 |         |  otherwise.             |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  B      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``ldb x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldb>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldb    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``B``.                 |
   +---------+-----------------+---------+-------------------------+
   |  beta   |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta == 0`` then     |
   |         |                 |         |  ``C`` does not have to |
   |         |                 |         |  be a valid input.      |
   +---------+-----------------+---------+-------------------------+
   |  C      |  device         |  in/out |  <type> array of        |
   |         |                 |         |  dimension ``ldc x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldc>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldc    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``C``.                 |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    | - if ``m``, ``n`` < 0 or          |
   |                                     | - if ``side`` !=                  |
   |                                     |   ``MCBLAS_SIDE_LEFT``,           |
   |                                     |   ``MCBLAS_SIDE_RIGHT`` or        |
   |                                     | - if ``uplo`` !=                  |
   |                                     |   ``MCBLAS_FILL_MODE_LOWER``,     |
   |                                     |   ``MCBLAS_FILL_MODE_UPPER`` or   |
   |                                     | - if ``lda`` < max(1, ``m``) if   |
   |                                     |   ``side`` ==                     |
   |                                     |   ``MCBLAS_SIDE_LEFT`` and        |
   |                                     |   ``lda`` < max(1, ``n``)         |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldb`` < max(1, ``m``) or   |
   |                                     | - if ``ldc`` < max(1, ``m``) or   |
   |                                     | - if ``alpha`` == NULL or         |
   |                                     |   ``beta`` == NULL or             |
   |                                     | - ``C`` == NULL if ``C`` needs    |
   |                                     |   to be scaled                    |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>syrk()
-----------------

::

   mcblasStatus_t mcblasSsyrk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *beta,
                              float           *C, int ldc)
   mcblasStatus_t mcblasDsyrk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *beta,
                              double          *C, int ldc)
   mcblasStatus_t mcblasCsyrk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *beta,
                              mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZsyrk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex *C, int ldc)

This function performs the symmetric rank-
:math:`k`
update
:math:`C = \alpha\text{op}(A)\text{op}(A)^{T} + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a symmetric matrix stored in lower or upper mode, and
:math:`A`
is a matrix with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
. Also, for matrix :math:`A`

.. math::
    op(A) = 
    \begin{cases}
    A & if \ \ transa == MCBLAS\_OP\_N \\
    A^T & if \ \ transa == MCBLAS\_OP\_T \\
    \end{cases}

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``C`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other symmetric part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | transpose.             |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``).      |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``trans ==             |
   |        |                |        | MCBLAS_OP_N``          |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | A.                     |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0`` then ``C`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``ldc x n``, |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``.     |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n``, ``k`` < 0 or         |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL if ``C`` needs   |
   |                                   |    to be scaled                   |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>syr2k()
-----------------

::

   mcblasStatus_t mcblasSsyr2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const float           *alpha,
                               const float           *A, int lda,
                               const float           *B, int ldb,
                               const float           *beta,
                               float           *C, int ldc)
   mcblasStatus_t mcblasDsyr2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const double          *alpha,
                               const double          *A, int lda,
                               const double          *B, int ldb,
                               const double          *beta,
                               double          *C, int ldc)
   mcblasStatus_t mcblasCsyr2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcComplex       *alpha,
                               const mcComplex       *A, int lda,
                               const mcComplex       *B, int ldb,
                               const mcComplex       *beta,
                               mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZsyr2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcDoubleComplex *alpha,
                               const mcDoubleComplex *A, int lda,
                               const mcDoubleComplex *B, int ldb,
                               const mcDoubleComplex *beta,
                               mcDoubleComplex *C, int ldc)

This function performs the symmetric rank-
:math:`2k`
update
:math:`C = \alpha(\text{op}(A)\text{op}(B)^{T} + \text{op}(B)\text{op}(A)^{T}) + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a symmetric matrix stored in lower or upper mode, and
:math:`A`
and :math:`B`
are matrices with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
and :math:`\text{op}(B)`
:math:`n \times k`
, respectively. Also, for matrix
:math:`A`
and :math:`B`

.. math::
    op(A)\ \ and\ \ op(B) = 
    \begin{cases}
    A\ \ and\ \ B & if \ \ trans == MCBLAS\_OP\_N \\
    A^T\ \ and\ \ B^T & if \ \ trans == MCBLAS\_OP\_T \\
    \end{cases}

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``C`` lower or upper   |
   |        |                |        | part, is stored, the   |
   |        |                |        | other symmetric part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | transpose.             |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``),      |
   |        |                |        | op(``B``) and ``C``.   |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | op(``B``).             |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transa               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | B      | device         | input  | <type> array of        |
   |        |                |        | dimensions ``ldb x k`` |
   |        |                |        | with ``ldb>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transb               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``ldb x n`` with   |
   |        |                |        | ``ldb>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | ldb    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``B``.                 |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0``, then      |
   |        |                |        | ``C`` does not have to |
   |        |                |        | be a valid input.      |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimensions ``ldc x n`` |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``.     |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n``, ``k`` < 0 or         |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL if ``C`` needs   |
   |                                   |    to be scaled                   |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>syrkx()
------------------

::

   mcblasStatus_t mcblasSsyrkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const float           *alpha,
                               const float           *A, int lda,
                               const float           *B, int ldb,
                               const float           *beta,
                               float           *C, int ldc)
   mcblasStatus_t mcblasDsyrkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const double          *alpha,
                               const double          *A, int lda,
                               const double          *B, int ldb,
                               const double          *beta,
                               double          *C, int ldc)
   mcblasStatus_t mcblasCsyrkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcComplex       *alpha,
                               const mcComplex       *A, int lda,
                               const mcComplex       *B, int ldb,
                               const mcComplex       *beta,
                               mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZsyrkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcDoubleComplex *alpha,
                               const mcDoubleComplex *A, int lda,
                               const mcDoubleComplex *B, int ldb,
                               const mcDoubleComplex *beta,
                               mcDoubleComplex *C, int ldc)

This function performs a variation of the symmetric rank-
:math:`k`
update
:math:`C = \alpha\text{op}(A)\text{op}(B)^{T} + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a symmetric matrix stored in lower or upper mode, and
:math:`A`
and :math:`B`
are matrices with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
and :math:`\text{op}(B)`
:math:`n \times k`
, respectively. Also, for matrices
:math:`A`
and :math:`B`

.. math::
    op(A)\ \ and\ \ op(B) = 
    \begin{cases}
    A\ \ and\ \ B & if \ \ trans == MCBLAS\_OP\_N \\
    A^T\ \ and\ \ B^T & if \ \ trans == MCBLAS\_OP\_T \\
    \end{cases}

This routine can be used when B is in such way that the
result is guaranteed to be symmetric. A usual example is
when the matrix B is a scaled form of the matrix A : this is
equivalent to B being the product of the matrix A and a
diagonal matrix. For an efficient computation of the product
of a regular matrix with a diagonal matrix, refer to the
routine mcblas<t>dgmm.

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``C`` lower or upper   |
   |        |                |        | part, is stored, the   |
   |        |                |        | other symmetric part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | transpose.             |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``),      |
   |        |                |        | op(``B``) and ``C``.   |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | op(``B``).             |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transa               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | B      | device         | input  | <type> array of        |
   |        |                |        | dimensions ``ldb x k`` |
   |        |                |        | with ``ldb>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transb               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``ldb x n`` with   |
   |        |                |        | ``ldb>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | ldb    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``B``.                 |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0``, then      |
   |        |                |        | ``C`` does not have to |
   |        |                |        | be a valid input.      |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimensions ``ldc x n`` |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``.     |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n``, ``k`` < 0 or         |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL if ``C`` needs   |
   |                                   |    to be scaled                   |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>trmm()
----------------

::

   mcblasStatus_t mcblasStrmm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *B, int ldb,
                              float                 *C, int ldc)
   mcblasStatus_t mcblasDtrmm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *B, int ldb,
                              double                *C, int ldc)
   mcblasStatus_t mcblasCtrmm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *B, int ldb,
                              mcComplex             *C, int ldc)
   mcblasStatus_t mcblasZtrmm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *B, int ldb,
                              mcDoubleComplex       *C, int ldc)

This function performs the triangular matrix-matrix multiplication

.. math::
   C = \left\{ \begin{array}{ll}
   {\alpha op(A)B} & if \enspace side == MCBLAS\_SIDE\_LEFT \\
   {\alpha B op(A)} & if \enspace side == MCBLAS\_SIDE\_RIGHT \\
   \end{array} \right.

where :math:`A` is a triangular matrix stored in lower or upper mode with or
without the main diagonal, :math:`B` and :math:`C` are :math:`m \times n`
matrix, and :math:`\alpha` is a scalar.
Also, for matrix :math:`A`,

.. math::
   op(A) = \left\{ \begin{array}{ll}
   A & if \enspace trans == MCBLAS\_OP\_N \\
   A^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{array} \right.

Notice that in order to achieve better parallelism mcBLAS
differs from the BLAS API only for this routine. The BLAS
API assumes an in-place implementation (with results written
back to B), while the mcBLAS API assumes an out-of-place
implementation (with results written into C). The
application can obtain the in-place functionality of BLAS in
the mcBLAS API by passing the address of the matrix B in
place of the matrix C. No other overlapping in the input
parameters is supported.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  side   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` is on the left   |
   |         |                 |         |  or right of ``B``.     |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other part is not      |
   |         |                 |         |  referenced and is      |
   |         |                 |         |  inferred from the      |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  trans  |                 |  input  |  operation op(``A``)    |
   |         |                 |         |  that is non- or        |
   |         |                 |         |  (conj.) transpose.     |
   +---------+-----------------+---------+-------------------------+
   |  diag   |                 |  input  |  indicates if the       |
   |         |                 |         |  elements on the main   |
   |         |                 |         |  diagonal of matrix     |
   |         |                 |         |  ``A`` are unity and    |
   |         |                 |         |  should not be          |
   |         |                 |         |  accessed.              |
   +---------+-----------------+---------+-------------------------+
   |  m      |                 |  input  |  number of rows of      |
   |         |                 |         |  matrix ``B``, with     |
   |         |                 |         |  matrix ``A`` sized     |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of columns of   |
   |         |                 |         |  matrix ``B``, with     |
   |         |                 |         |  matrix ``A`` sized     |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``alpha==0`` then      |
   |         |                 |         |  ``A`` is not           |
   |         |                 |         |  referenced and ``B``   |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x m``  |
   |         |                 |         |  with ``lda>=max(1,m)`` |
   |         |                 |         |  if                     |
   |         |                 |         |  ``side                 |
   |         |                 |         |  == MCBLAS_SIDE_LEFT``  |
   |         |                 |         |  and ``lda x n`` with   |
   |         |                 |         |  ``lda>=max(1,n)``      |
   |         |                 |         |  otherwise.             |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  B      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``ldb x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldb>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldb    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``B``.                 |
   +---------+-----------------+---------+-------------------------+
   |  C      |  device         |  in/out |  <type> array of        |
   |         |                 |         |  dimension ``ldc x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldc>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldc    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``C``.                 |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    | - if ``m``, ``n`` < 0 or          |
   |                                     | - if ``trans`` !=                 |
   |                                     |   ``MCBLAS_OP_N``,                |
   |                                     |   ``MCBLAS_OP_C``,                |
   |                                     |   ``MCBLAS_OP_T`` or              |
   |                                     | - if ``uplo`` !=                  |
   |                                     |   ``MCBLAS_FILL_MODE_LOWER``,     |
   |                                     |   ``MCBLAS_FILL_MODE_UPPER`` or   |
   |                                     | - if ``side`` !=                  |
   |                                     |   ``MCBLAS_SIDE_LEFT``,           |
   |                                     |   ``MCBLAS_SIDE_RIGHT`` or        |
   |                                     | - if ``lda`` < max(1, ``m``) if   |
   |                                     |   ``side`` ==                     |
   |                                     |   ``MCBLAS_SIDE_LEFT`` and        |
   |                                     |   ``lda`` < max(1, ``n``)         |
   |                                     |   otherwise or                    |
   |                                     | - if ``ldb`` < max(1, ``m``) or   |
   |                                     | - ``C`` == NULL if ``C`` needs    |
   |                                     |   to be scaled                    |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>trsm()
----------------

::

   mcblasStatus_t mcblasStrsm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const float           *alpha,
                              const float           *A, int lda,
                              float                 *B, int ldb)
   mcblasStatus_t mcblasDtrsm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const double          *alpha,
                              const double          *A, int lda,
                              double                *B, int ldb)
   mcblasStatus_t mcblasCtrsm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              mcComplex             *B, int ldb)
   mcblasStatus_t mcblasZtrsm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              mcblasOperation_t trans, mcblasDiagType_t diag,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              mcDoubleComplex       *B, int ldb)

This function solves the triangular linear system with multiple right-hand-sides

.. math::
   \left\{ \begin{array}{ll}
   op(A)X = \alpha B &  if \enspace side == MCBLAS\_SIDE\_LEFT \\
   X op(A) = \alpha B & if \enspace side == MCBLAS\_SIDE\_RIGHT \\
   \end{array} \right.

where :math:`A` is a triangular matrix stored in lower or upper mode with or
without the main diagonal, :math:`X` and :math:`B` are :math:`m \times n`
matrices, and :math:`\alpha` is a scalar. Also, for matrix :math:`A`,

.. math::
   op(A) = \left\{ \begin{array}{ll}
   A & if \enspace trans == MCBLAS\_OP\_N \\
   A^{T} & if \enspace trans == MCBLAS\_OP\_T \\
   A^{H} & if \enspace trans == MCBLAS\_OP\_C \\
   \end{array} \right.

The solution :math:`X` overwrites the right-hand-sides :math:`B` on exit.

No test for singularity or near-singularity is included in this function.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  side   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` is on the left   |
   |         |                 |         |  or right of ``X``.     |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other part is not      |
   |         |                 |         |  referenced and is      |
   |         |                 |         |  inferred from the      |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  trans  |                 |  input  |  operation op(``A``)    |
   |         |                 |         |  that is non- or        |
   |         |                 |         |  (conj.) transpose.     |
   +---------+-----------------+---------+-------------------------+
   |  diag   |                 |  input  |  indicates if the       |
   |         |                 |         |  elements on the main   |
   |         |                 |         |  diagonal of matrix     |
   |         |                 |         |  ``A`` are unity and    |
   |         |                 |         |  should not be          |
   |         |                 |         |  accessed.              |
   +---------+-----------------+---------+-------------------------+
   |  m      |                 |  input  |  number of rows of      |
   |         |                 |         |  matrix ``B``, with     |
   |         |                 |         |  matrix ``A`` sized     |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of columns of   |
   |         |                 |         |  matrix ``B``, with     |
   |         |                 |         |  matrix ``A`` is sized  |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``alpha==0`` then      |
   |         |                 |         |  ``A`` is not           |
   |         |                 |         |  referenced and ``B``   |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x m``  |
   |         |                 |         |  with ``lda>=max(1,m)`` |
   |         |                 |         |  if                     |
   |         |                 |         |  ``side                 |
   |         |                 |         |  == MCBLAS_SIDE_LEFT``  |
   |         |                 |         |  and ``lda x n`` with   |
   |         |                 |         |  ``lda>=max(1,n)``      |
   |         |                 |         |  otherwise.             |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  B      |  device         |  in/out |  <type> array. It has   |
   |         |                 |         |  dimensions ``ldb x n`` |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldb>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldb    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``B``.                 |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   | the library was not initialized   |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  - if ``m`` < 0 or ``n`` < 0 or   |
   |                                     |  - if ``trans`` !=                |
   |                                     |    ``MCBLAS_OP_N``,               |
   |                                     |    ``MCBLAS_OP_C``,               |
   |                                     |    ``MCBLAS_OP_T`` or             |
   |                                     |  - if ``uplo`` !=                 |
   |                                     |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                     |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                     |  - if ``side`` !=                 |
   |                                     |    ``MCBLAS_SIDE_LEFT``,          |
   |                                     |    ``MCBLAS_SIDE_RIGHT`` or       |
   |                                     |  - if ``diag`` !=                 |
   |                                     |    ``MCBLAS_DIAG_NON_UNIT``,      |
   |                                     |    ``MCBLAS_DIAG_UNIT`` or        |
   |                                     |  - if ``lda`` < max(1, ``m``) if  |
   |                                     |    ``side`` ==                    |
   |                                     |    ``MCBLAS_SIDE_LEFT`` and       |
   |                                     |    ``lda`` < max(1, ``n``)        |
   |                                     |    otherwise or                   |
   |                                     |  - if ``ldb`` < max(1, ``m``) or  |
   |                                     |  - ``alpha`` == NULL              |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>trsmBatched()
-----------------------

::

   mcblasStatus_t mcblasStrsmBatched(mcblasHandle_t    handle,
                                     mcblasSideMode_t  side,
                                     mcblasFillMode_t  uplo,
                                     mcblasOperation_t trans,
                                     mcblasDiagType_t  diag,
                                     int m,
                                     int n,
                                     const float *alpha,
                                     const float *const A[],
                                     int lda,
                                     float *const B[],
                                     int ldb,
                                     int batchCount);
   mcblasStatus_t mcblasDtrsmBatched(mcblasHandle_t    handle,
                                     mcblasSideMode_t  side,
                                     mcblasFillMode_t  uplo,
                                     mcblasOperation_t trans,
                                     mcblasDiagType_t  diag,
                                     int m,
                                     int n,
                                     const double *alpha,
                                     const double *const A[],
                                     int lda,
                                     double *const B[],
                                     int ldb,
                                     int batchCount);
   mcblasStatus_t mcblasCtrsmBatched(mcblasHandle_t    handle,
                                     mcblasSideMode_t  side,
                                     mcblasFillMode_t  uplo,
                                     mcblasOperation_t trans,
                                     mcblasDiagType_t  diag,
                                     int m,
                                     int n,
                                     const mcComplex *alpha,
                                     const mcComplex *const A[],
                                     int lda,
                                     mcComplex *const B[],
                                     int ldb,
                                     int batchCount);
   mcblasStatus_t mcblasZtrsmBatched(mcblasHandle_t    handle,
                                     mcblasSideMode_t  side,
                                     mcblasFillMode_t  uplo,
                                     mcblasOperation_t trans,
                                     mcblasDiagType_t  diag,
                                     int m,
                                     int n,
                                     const mcDoubleComplex *alpha,
                                     const mcDoubleComplex *const A[],
                                     int lda,
                                     mcDoubleComplex *const B[],
                                     int ldb,
                                     int batchCount);

This function solves an array of triangular linear systems
with multiple right-hand-sides

.. math::
   \begin{cases}
    op(A)X = \alpha B & if \ \ side == MCBLAS\_SIDE\_LEFT \\
    Xop(A) = \alpha B & if \ \ side == MCBLAS\_SIDE\_RIGHT
   \end{cases}

where :math:`A\lbrack i\rbrack`
is a triangular matrix stored in lower or upper mode with or
without the main diagonal,
:math:`X\lbrack i\rbrack`
and :math:`B\lbrack i\rbrack`
are :math:`m \times n`
matrices, and :math:`\alpha`
is a scalar. Also, for matrix :math:`A`

.. math::
    op(A) = 
    \begin{cases}
    A & if \ \ transa == MCBLAS\_OP\_N \\
    A^T & if \ \ transa == MCBLAS\_OP\_T \\
    A^H & if \ \ transa == MCBLAS\_OP\_C \\
    \end{cases}

The solution :math:`X\lbrack i\rbrack`
overwrites the right-hand-sides
:math:`B\lbrack i\rbrack`
on exit.
No test for singularity or near-singularity is included in
this function.

This function works for any sizes but is intended to be used
for matrices of small sizes where the launch overhead is a
significant factor. For bigger sizes, it might be
advantageous to call ``batchCount`` times the regular
``mcblas<t>trsm`` within a set of MACA streams.

The mcrrent implementation is limited to devices with
compute capability above or equal 2.0.

.. table::
   :widths: grid

   +------------+----------------+--------+----------------------+
   | Param.     | Memory         | In/out | Meaning              |
   +============+================+========+======================+
   | handle     |                | input  | handle to the mcBLAS |
   |            |                |        | library context.     |
   +------------+----------------+--------+----------------------+
   | side       |                | input  | indicates if matrix  |
   |            |                |        | ``A[i]`` is on the   |
   |            |                |        | left or right of     |
   |            |                |        | ``X[i]``.            |
   +------------+----------------+--------+----------------------+
   | uplo       |                | input  | indicates if matrix  |
   |            |                |        | ``A[i]`` lower or    |
   |            |                |        | upper part is        |
   |            |                |        | stored, the other    |
   |            |                |        | part is not          |
   |            |                |        | referenced and is    |
   |            |                |        | inferred from the    |
   |            |                |        | stored elements.     |
   +------------+----------------+--------+----------------------+
   | trans      |                | input  | operation            |
   |            |                |        | op(``A[i]``) that is |
   |            |                |        | non- or (conj.)      |
   |            |                |        | transpose.           |
   +------------+----------------+--------+----------------------+
   | diag       |                | input  | indicates if the     |
   |            |                |        | elements on the main |
   |            |                |        | diagonal of matrix   |
   |            |                |        | ``A[i]`` are unity   |
   |            |                |        | and should not be    |
   |            |                |        | accessed.            |
   +------------+----------------+--------+----------------------+
   | m          |                | input  | number of rows of    |
   |            |                |        | matrix ``B[i]``,     |
   |            |                |        | with matrix ``A[i]`` |
   |            |                |        | sized accordingly.   |
   +------------+----------------+--------+----------------------+
   | n          |                | input  | number of columns of |
   |            |                |        | matrix ``B[i]``,     |
   |            |                |        | with matrix ``A[i]`` |
   |            |                |        | is sized             |
   |            |                |        | accordingly.         |
   +------------+----------------+--------+----------------------+
   | alpha      | host or device | input  | <type> scalar used   |
   |            |                |        | for multiplication,  |
   |            |                |        | if ``alpha==0`` then |
   |            |                |        | ``A[i]`` is not      |
   |            |                |        | referenced and       |
   |            |                |        | ``B[i]`` does not    |
   |            |                |        | have to be a valid   |
   |            |                |        | input.               |
   +------------+----------------+--------+----------------------+
   | A          | device         | input  | array of pointers to |
   |            |                |        | <type> array, with   |
   |            |                |        | each array of dim.   |
   |            |                |        | ``lda x m``          |
   |            |                |        | with                 |
   |            |                |        | ``lda>=max(1,m)`` if |
   |            |                |        | ``side =             |
   |            |                |        | = MCBLAS_SIDE_LEFT`` |
   |            |                |        | and ``lda x n`` with |
   |            |                |        | ``lda>=max(1,n)``    |
   |            |                |        | otherwise.           |
   +------------+----------------+--------+----------------------+
   | lda        |                | input  | leading dimension of |
   |            |                |        | two-dimensional      |
   |            |                |        | array used to store  |
   |            |                |        | matrix ``A[i]``.     |
   +------------+----------------+--------+----------------------+
   | B          | device         | in/out | array of pointers to |
   |            |                |        | <type> array, with   |
   |            |                |        | each array of dim.   |
   |            |                |        | ``ldb x n``          |
   |            |                |        | with                 |
   |            |                |        | ``ldb>=max(1,m)``.   |
   |            |                |        | Matrices ``B[i]``    |
   |            |                |        | should not overlap;  |
   |            |                |        | otherwise, undefined |
   |            |                |        | behavior is          |
   |            |                |        | expected.            |
   +------------+----------------+--------+----------------------+
   | ldb        |                | input  | leading dimension of |
   |            |                |        | two-dimensional      |
   |            |                |        | array used to store  |
   |            |                |        | matrix ``B[i]``.     |
   +------------+----------------+--------+----------------------+
   | batchCount |                | input  | number of pointers   |
   |            |                |        | contained in A and   |
   |            |                |        | B.                   |
   +------------+----------------+--------+----------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   |    ``batchCount`` < 0 or          |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``side`` !=                 |
   |                                   |    ``MCBLAS_SIDE_LEFT``,          |
   |                                   |    ``MCBLAS_SIDE_RIGHT`` or       |
   |                                   |                                   |
   |                                   | -  if ``diag`` !=                 |
   |                                   |    ``MCBLAS_DIAG_NON_UNIT``,      |
   |                                   |    ``MCBLAS_DIAG_UNIT`` or        |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``m``) if  |
   |                                   |    ``side`` ==                    |
   |                                   |    ``MCBLAS_SIDE_LEFT`` and       |
   |                                   |    ``lda`` < max(1, ``n``)        |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  ``ldb`` < max(1, ``m``)        |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>hemm()
-----------------

::

   mcblasStatus_t mcblasChemm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *B, int ldb,
                              const mcComplex       *beta,
                              mcComplex             *C, int ldc)
   mcblasStatus_t mcblasZhemm(mcblasHandle_t handle,
                              mcblasSideMode_t side, mcblasFillMode_t uplo,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *B, int ldb,
                              const mcDoubleComplex *beta,
                              mcDoubleComplex       *C, int ldc)

This function performs the Hermitian matrix-matrix multiplication

.. math::
   C = \left\{ \begin{array}{ll}
   {\alpha AB + \beta C} & if \enspace side == MCBLAS\_SIDE\_LEFT \\
   {\alpha BA + \beta C} & if \enspace side == MCBLAS\_SIDE\_RIGHT \\
   \end{array} \right.

where :math:`A` is a Hermitian matrix stored in lower or upper mode,
:math:`B` and :math:`C` are :math:`m \times n` matrices,
and :math:`\alpha` and :math:`\beta` are scalars.

.. table::
   :widths: grid

   +---------+-----------------+---------+-------------------------+
   | Param.  | Memory          | In/out  | Meaning                 |
   +=========+=================+=========+=========================+
   |  handle |                 |  input  |  handle to the mcBLAS   |
   |         |                 |         |  library context.       |
   +---------+-----------------+---------+-------------------------+
   |  side   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` is on the left   |
   |         |                 |         |  or right of ``B``.     |
   +---------+-----------------+---------+-------------------------+
   |  uplo   |                 |  input  |  indicates if matrix    |
   |         |                 |         |  ``A`` lower or upper   |
   |         |                 |         |  part is stored, the    |
   |         |                 |         |  other Hermitian part   |
   |         |                 |         |  is not referenced and  |
   |         |                 |         |  is inferred from the   |
   |         |                 |         |  stored elements.       |
   +---------+-----------------+---------+-------------------------+
   |  m      |                 |  input  |  number of rows of      |
   |         |                 |         |  matrix ``C`` and       |
   |         |                 |         |  ``B``, with matrix     |
   |         |                 |         |  ``A`` sized            |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  n      |                 |  input  |  number of columns of   |
   |         |                 |         |  matrix ``C`` and       |
   |         |                 |         |  ``B``, with matrix     |
   |         |                 |         |  ``A`` sized            |
   |         |                 |         |  accordingly.           |
   +---------+-----------------+---------+-------------------------+
   |  alpha  |  host or device |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication.        |
   +---------+-----------------+---------+-------------------------+
   |  A      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``lda x m``  |
   |         |                 |         |  with ``lda>=max(1,m)`` |
   |         |                 |         |  if                     |
   |         |                 |         |  ``si                   |
   |         |                 |         |  de==MCBLAS_SIDE_LEFT`` |
   |         |                 |         |  and ``lda x n`` with   |
   |         |                 |         |  ``lda>=max(1,n)``      |
   |         |                 |         |  otherwise. The         |
   |         |                 |         |  imaginary parts of the |
   |         |                 |         |  diagonal elements are  |
   |         |                 |         |  assumed to be zero.    |
   +---------+-----------------+---------+-------------------------+
   |  lda    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``A``.                 |
   +---------+-----------------+---------+-------------------------+
   |  B      |  device         |  input  |  <type> array of        |
   |         |                 |         |  dimension ``ldb x n``  |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldb>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldb    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``B``.                 |
   +---------+-----------------+---------+-------------------------+
   |  beta   |                 |  input  |  <type> scalar used for |
   |         |                 |         |  multiplication, if     |
   |         |                 |         |  ``beta==0`` then ``C`` |
   |         |                 |         |  does not have to be a  |
   |         |                 |         |  valid input.           |
   +---------+-----------------+---------+-------------------------+
   |  C      |  device         |  in/out |  <type> array of        |
   |         |                 |         |  dimensions ``ldc x n`` |
   |         |                 |         |  with                   |
   |         |                 |         |  ``ldc>=max(1,m)``.     |
   +---------+-----------------+---------+-------------------------+
   |  ldc    |                 |  input  |  leading dimension of   |
   |         |                 |         |  two-dimensional array  |
   |         |                 |         |  used to store matrix   |
   |         |                 |         |  ``C``.                 |
   +---------+-----------------+---------+-------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-------------------------------------+-----------------------------------+
   | Error Value                         | Meaning                           |
   +=====================================+===================================+
   |  ``MCBLAS_STATUS_SUCCESS``          |  the operation completed          |
   |                                     |  successfully                     |
   +-------------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED``   |  the library was not initialized  |
   +-------------------------------------+-----------------------------------+
   |  ``MCBLAS_STATUS_INVALID_VALUE``    |  - if ``m`` < 0 or ``n`` < 0 or   |
   |                                     |  - if ``side`` !=                 |
   |                                     |    ``MCBLAS_SIDE_LEFT``,          |
   |                                     |    ``MCBLAS_SIDE_RIGHT`` or       |
   |                                     |  - if ``uplo`` !=                 |
   |                                     |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                     |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                     |  - if ``lda`` < max(1, ``m``) if  |
   |                                     |    ``side`` ==                    |
   |                                     |    ``MCBLAS_SIDE_LEFT`` and       |
   |                                     |    ``lda`` < max(1, ``n``)        |
   |                                     |    otherwise or                   |
   |                                     |  - if ``ldb`` < max(1, ``m``) or  |
   |                                     |  - if ``ldc`` < max(1, ``m``) or  |
   |                                     |  - if ``alpha`` == NULL or        |
   |                                     |    ``beta`` == NULL or            |
   |                                     |  - ``C`` == NULL                  |
   +-------------------------------------+-----------------------------------+
   |                                     |  the function failed to launch on |
   |  ``MCBLAS_STATUS_EXECUTION_FAILED`` |  the GPU                          |
   +-------------------------------------+-----------------------------------+

mcblas<t>herk()
-----------------

::

   mcblasStatus_t mcblasCherk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const float  *alpha,
                              const mcComplex       *A, int lda,
                              const float  *beta,
                              mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZherk(mcblasHandle_t handle,
                              mcblasFillMode_t uplo, mcblasOperation_t trans,
                              int n, int k,
                              const double *alpha,
                              const mcDoubleComplex *A, int lda,
                              const double *beta,
                              mcDoubleComplex *C, int ldc)

This function performs the Hermitian rank-
:math:`k`
update
:math:`C = \alpha\text{op}(A)\text{op}(A)^{H} + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a Hermitian matrix stored in lower or upper mode, and
:math:`A`
is a matrix with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
. Also, for matrix :math:`A`

.. math::
    op(A) = 
    \begin{cases}
    A & if \ \ transa == MCBLAS\_OP\_N \\
    A^T & if \ \ transa == MCBLAS\_OP\_T \\
    \end{cases}

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``).      |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transa               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | beta   |                | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0`` then ``C`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``ldc x n``, |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``. The |
   |        |                |        | imaginary parts of the |
   |        |                |        | diagonal elements are  |
   |        |                |        | assumed and set to     |
   |        |                |        | zero.                  |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or ``k`` < 0 or   |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL                  |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>her2k()
-----------------

::

   mcblasStatus_t mcblasCher2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcComplex       *alpha,
                               const mcComplex       *A, int lda,
                               const mcComplex       *B, int ldb,
                               const float  *beta,
                               mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZher2k(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcDoubleComplex *alpha,
                               const mcDoubleComplex *A, int lda,
                               const mcDoubleComplex *B, int ldb,
                               const double *beta,
                               mcDoubleComplex *C, int ldc)

This function performs the Hermitian rank-
:math:`2k`
update
:math:`C = \alpha\text{op}(A)\text{op}(B)^{H} + \overline{\alpha}\text{op}(B)\text{op}(A)^{H} + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a Hermitian matrix stored in lower or upper mode, and
:math:`A`
and :math:`B`
are matrices with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
and :math:`\text{op}(B)`
:math:`n \times k`
, respectively. Also, for matrix
:math:`A`
and :math:`B`

.. math::
    op(A)\ \ and\ \ op(B) = 
    \begin{cases}
    A\ \ and\ \ B & if \ \ trans == MCBLAS\_OP\_N \\
    A^H\ \ and\ \ B^H & if \ \ trans == MCBLAS\_OP\_C \\
    \end{cases}

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``),      |
   |        |                |        | op(``B``) and ``C``.   |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | op(``B``).             |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transa               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | B      | device         | input  | <type> array of        |
   |        |                |        | dimension ``ldb x k``  |
   |        |                |        | with ``ldb>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transb               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``ldb x n`` with   |
   |        |                |        | ``ldb>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | ldb    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``B``.                 |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0`` then ``C`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``ldc x n``, |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``. The |
   |        |                |        | imaginary parts of the |
   |        |                |        | diagonal elements are  |
   |        |                |        | assumed and set to     |
   |        |                |        | zero.                  |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or ``k`` < 0 or   |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL                  |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>herkx()
-----------------

::

   mcblasStatus_t mcblasCherkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcComplex       *alpha,
                               const mcComplex       *A, int lda,
                               const mcComplex       *B, int ldb,
                               const float  *beta,
                               mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZherkx(mcblasHandle_t handle,
                               mcblasFillMode_t uplo, mcblasOperation_t trans,
                               int n, int k,
                               const mcDoubleComplex *alpha,
                               const mcDoubleComplex *A, int lda,
                               const mcDoubleComplex *B, int ldb,
                               const double *beta,
                               mcDoubleComplex *C, int ldc)

This function performs a variation of the Hermitian rank-
:math:`k`
update
:math:`C = \alpha\text{op}(A)\text{op}(B)^{H} + \beta C`
where :math:`\alpha`
and :math:`\beta`
are scalars, :math:`C`
is a Hermitian matrix stored in lower or upper mode, and
:math:`A`
and :math:`B`
are matrices with dimensions
:math:`\text{op}(A)`
:math:`n \times k`
and :math:`\text{op}(B)`
:math:`n \times k`
, respectively. Also, for matrix
:math:`A`
and :math:`B`

.. math::
    op(A)\ \ and\ \ op(B) = 
    \begin{cases}
    A\ \ and\ \ B & if \ \ trans == MCBLAS\_OP\_N \\
    A^H\ \ and\ \ B^H & if \ \ trans == MCBLAS\_OP\_C \\
    \end{cases}

This routine can be used when the matrix B is in such way
that the result is guaranteed to be hermitian. An usual
example is when the matrix B is a scaled form of the matrix
A : this is equivalent to B being the product of the matrix
A and a diagonal matrix. For an efficient computation of the
product of a regular matrix with a diagonal matrix, refer to
the routine mcblas<t>dgmm.

.. table::
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | uplo   |                | input  | indicates if matrix    |
   |        |                |        | ``A`` lower or upper   |
   |        |                |        | part is stored, the    |
   |        |                |        | other Hermitian part   |
   |        |                |        | is not referenced and  |
   |        |                |        | is inferred from the   |
   |        |                |        | stored elements.       |
   +--------+----------------+--------+------------------------+
   | trans  |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``),      |
   |        |                |        | op(``B``) and ``C``.   |
   +--------+----------------+--------+------------------------+
   | k      |                | input  | number of columns of   |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | op(``B``).             |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication.        |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimension ``lda x k``  |
   |        |                |        | with ``lda>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transa               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``lda x n`` with   |
   |        |                |        | ``lda>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``A``.                 |
   +--------+----------------+--------+------------------------+
   | B      | device         | input  | <type> array of        |
   |        |                |        | dimension ``ldb x k``  |
   |        |                |        | with ``ldb>=max(1,n)`` |
   |        |                |        | if                     |
   |        |                |        | ``transb               |
   |        |                |        | == MCBLAS_OP_N``       |
   |        |                |        | and ``ldb x n`` with   |
   |        |                |        | ``ldb>=max(1,k)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | ldb    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``B``.                 |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | real scalar used for   |
   |        |                |        | multiplication, if     |
   |        |                |        | ``beta==0`` then ``C`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | C      | device         | in/out | <type> array of        |
   |        |                |        | dimension ``ldc x n``, |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,n)``. The |
   |        |                |        | imaginary parts of the |
   |        |                |        | diagonal elements are  |
   |        |                |        | assumed and set to     |
   |        |                |        | zero.                  |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n`` < 0 or ``k`` < 0 or   |
   |                                   |                                   |
   |                                   | -  if ``trans`` !=                |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER`` or  |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``n``) if  |
   |                                   |    ``trans`` == ``MCBLAS_OP_N``   |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``n``) or  |
   |                                   |                                   |
   |                                   | -  if ``alpha`` == NULL or        |
   |                                   |    ``beta`` == NULL or            |
   |                                   |                                   |
   |                                   | -  ``C`` == NULL                  |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

BLAS-Like Extension
====================

In this chapter we describe the BLAS-extension functions that
perform matrix-matrix operations.

mcblas<t>geam()
-----------------

::

   mcblasStatus_t mcblasSgeam(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n,
                              const float           *alpha,
                              const float           *A, int lda,
                              const float           *beta,
                              const float           *B, int ldb,
                              float           *C, int ldc)
   mcblasStatus_t mcblasDgeam(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n,
                              const double          *alpha,
                              const double          *A, int lda,
                              const double          *beta,
                              const double          *B, int ldb,
                              double          *C, int ldc)
   mcblasStatus_t mcblasCgeam(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n,
                              const mcComplex       *alpha,
                              const mcComplex       *A, int lda,
                              const mcComplex       *beta ,
                              const mcComplex       *B, int ldb,
                              mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZgeam(mcblasHandle_t handle,
                              mcblasOperation_t transa, mcblasOperation_t transb,
                              int m, int n,
                              const mcDoubleComplex *alpha,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *beta,
                              const mcDoubleComplex *B, int ldb,
                              mcDoubleComplex *C, int ldc)

This function performs the matrix-matrix
addition/transposition

.. math:: 
   C = \alpha\text{op}(A) + \beta\text{op}(B)

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
, :math:`B`
and :math:`C`
are matrices stored in column-major format with dimensions
:math:`\text{op}(A)`
:math:`m \times n`
, :math:`\text{op}(B)`
:math:`m \times n`
and :math:`C`
:math:`m \times n`
, respectively. Also, for matrix
:math:`A`

.. math::
   op(A) = \left\{\begin{matrix}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{matrix}\right.

and :math:`\text{op}(B)`
is defined similarly for matrix :math:`B`
.
The operation is out-of-place if C does not overlap A or B.

The in-place mode supports the following two operations,

.. math:: 
   C = \alpha\text{*}C + \beta\text{op}(B) \\
   C = \alpha\text{op}(A) + \beta\text{*}C

For in-place mode, if ``C = A``, ``ldc = lda`` and
``transa = MCBLAS_OP_N``. If ``C = B``, ``ldc = ldb`` and
``transb = MCBLAS_OP_N``. If the user does not meet above
requirements, ``MCBLAS_STATUS_INVALID_VALUE`` is returned.

The operation includes the following special cases:

the user can reset matrix C to zero by setting
``*alpha=*beta=0``.

the user can transpose matrix A by setting
``*alpha=1 and *beta=0``.

.. table:: 
   :widths: grid

   +--------+----------------+--------+------------------------+
   | Param. | Memory         | In/out | Meaning                |
   +========+================+========+========================+
   | handle |                | input  | handle to the mcBLAS   |
   |        |                |        | library context.       |
   +--------+----------------+--------+------------------------+
   | transa |                | input  | operation op(``A``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | transb |                | input  | operation op(``B``)    |
   |        |                |        | that is non- or        |
   |        |                |        | (conj.) transpose.     |
   +--------+----------------+--------+------------------------+
   | m      |                | input  | number of rows of      |
   |        |                |        | matrix op(``A``) and   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+
   | n      |                | input  | number of columns of   |
   |        |                |        | matrix op(``B``) and   |
   |        |                |        | ``C``.                 |
   +--------+----------------+--------+------------------------+
   | alpha  | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication. If     |
   |        |                |        | ``*alpha == 0``, ``A`` |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | A      | device         | input  | <type> array of        |
   |        |                |        | dimensions ``lda x n`` |
   |        |                |        | with ``lda>=max(1,m)`` |
   |        |                |        | if                     |
   |        |                |        | ``t                    |
   |        |                |        | ransa == MCBLAS_OP_N`` |
   |        |                |        | and ``lda x m`` with   |
   |        |                |        | ``lda>=max(1,n)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | lda    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store the      |
   |        |                |        | matrix ``A``.          |
   +--------+----------------+--------+------------------------+
   | B      | device         | input  | <type> array of        |
   |        |                |        | dimension ``ldb x n``  |
   |        |                |        | with ``ldb>=max(1,m)`` |
   |        |                |        | if                     |
   |        |                |        | ``t                    |
   |        |                |        | ransb == MCBLAS_OP_N`` |
   |        |                |        | and ``ldb x m`` with   |
   |        |                |        | ``ldb>=max(1,n)``      |
   |        |                |        | otherwise.             |
   +--------+----------------+--------+------------------------+
   | ldb    |                | input  | leading dimension of   |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store matrix   |
   |        |                |        | ``B``.                 |
   +--------+----------------+--------+------------------------+
   | beta   | host or device | input  | <type> scalar used for |
   |        |                |        | multiplication. If     |
   |        |                |        | ``*beta == 0``, ``B``  |
   |        |                |        | does not have to be a  |
   |        |                |        | valid input.           |
   +--------+----------------+--------+------------------------+
   | C      | device         | output | <type> array of        |
   |        |                |        | dimensions ``ldc x n`` |
   |        |                |        | with                   |
   |        |                |        | ``ldc>=max(1,m)``.     |
   +--------+----------------+--------+------------------------+
   | ldc    |                | input  | leading dimension of a |
   |        |                |        | two-dimensional array  |
   |        |                |        | used to store the      |
   |        |                |        | matrix ``C``.          |
   +--------+----------------+--------+------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   |                                   |
   |                                   | -  if ``transa`` !=               |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``transb`` !=               |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``m``) if  |
   |                                   |    ``transa`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``lda`` < max(1, ``n``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``m``) if  |
   |                                   |    ``transb`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``ldb`` < max(1, ``n``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``m``) or  |
   |                                   |                                   |
   |                                   | -  if ``A`` == ``C``,             |
   |                                   |    ((``MCBLAS_OP_N`` !=           |
   |                                   |    ``transa``) \|\| (``lda`` !=   |
   |                                   |    ``ldc``)) or                   |
   |                                   |                                   |
   |                                   | -  if ``B`` == ``C``,             |
   |                                   |    ((``MCBLAS_OP_N`` !=           |
   |                                   |    ``transb``) \|\| (``ldb`` !=   |
   |                                   |    ``ldc``)) or                   |
   |                                   |                                   |
   |                                   | -  ``alpha`` == NULL or ``beta``  |
   |                                   |    == NULL                        |
   +-----------------------------------+-----------------------------------+
   | `                                 | the function failed to launch on  |
   | `MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>dgmm()
-----------------
            
::

   mcblasStatus_t mcblasSdgmm(mcblasHandle_t handle, mcblasSideMode_t mode,
                              int m, int n,
                              const float           *A, int lda,
                              const float           *x, int incx,
                              float           *C, int ldc)
   mcblasStatus_t mcblasDdgmm(mcblasHandle_t handle, mcblasSideMode_t mode,
                              int m, int n,
                              const double          *A, int lda,
                              const double          *x, int incx,
                              double          *C, int ldc)
   mcblasStatus_t mcblasCdgmm(mcblasHandle_t handle, mcblasSideMode_t mode,
                              int m, int n,
                              const mcComplex       *A, int lda,
                              const mcComplex       *x, int incx,
                              mcComplex       *C, int ldc)
   mcblasStatus_t mcblasZdgmm(mcblasHandle_t handle, mcblasSideMode_t mode,
                              int m, int n,
                              const mcDoubleComplex *A, int lda,
                              const mcDoubleComplex *x, int incx,
                              mcDoubleComplex *C, int ldc)

This function performs the matrix-matrix multiplication

.. math::
   C = \left\{ \begin{matrix}
   {A \times diag(X)} & if \enspace mode == MCBLAS\_SIDE\_RIGHT \\
   {diag(X) \times A} & if \enspace mode == MCBLAS\_SIDE\_LEFT \\
   \end{matrix} \right.

where :math:`A`
and :math:`C`
are matrices stored in column-major format with dimensions
:math:`m \times n`
. :math:`X`
is a vector of size :math:`n`
if ``mode == MCBLAS_SIDE_RIGHT`` and of size
:math:`m`
if ``mode == MCBLAS_SIDE_LEFT``.
:math:`X`
is gathered from one-dimensional array x with stride
``incx``. The absolute value of ``incx`` is the stride and
the sign of ``incx`` is direction of the stride. If ``incx``
is positive, then we forward x from the first element.
Otherwise, we backward x from the last element. The formula
of X is

.. math:: 
   X \lbrack j\rbrack = \left\{ \begin{matrix}
   {x\lbrack j \times incx\rbrack} & {\text{if }incx \geq 0} \\
   {x\lbrack(\chi - 1) \times |incx| - j \times |incx|\rbrack} & {\text{if }incx < 0} \\
   \end{matrix} \right.

where :math:`\chi = m`
if ``mode == MCBLAS_SIDE_LEFT`` and
:math:`\chi = n`
if ``mode == MCBLAS_SIDE_RIGHT``.
Example 1: if the user wants to perform
:math:`diag(diag(B)) \times A`
, then :math:`incx = ldb + 1`
where :math:`ldb`
is leading dimension of matrix ``B``, either row-major or
column-major.
Example 2: if the user wants to perform
:math:`\alpha \times A`
, then there are two choices, either mcblasgeam with
``*beta=0`` and ``transa == MCBLAS_OP_N`` or mcblasdgmm with
``incx=0`` and ``x[0]=alpha``.
The operation is out-of-place. The in-place only works if
``lda = ldc``.

.. table:: 
   :widths: grid
   :align: left
   
   +-----------------+-----------------+-----------------+-----------------------+
   | Param.          | Memory          | In/out          | Meaning               |
   +=================+=================+=================+=======================+
   | handle          |                 | input           | handle to the         |
   |                 |                 |                 | mcBLAS library        |
   |                 |                 |                 | context.              |
   +-----------------+-----------------+-----------------+-----------------------+
   | mode            |                 | input           | left multiply         |
   |                 |                 |                 | if                    |
   |                 |                 |                 | ``mode ==             |
   |                 |                 |                 | MCBLAS_SIDE_LEFT``    |
   |                 |                 |                 | or right              |
   |                 |                 |                 | multiply if           |
   |                 |                 |                 | ``mode ==             |
   |                 |                 |                 | MCBLAS_SIDE_RIGHT``   |
   +-----------------+-----------------+-----------------+-----------------------+
   | m               |                 | input           | number of rows        |
   |                 |                 |                 | of matrix ``A``       |
   |                 |                 |                 | and ``C``.            |
   +-----------------+-----------------+-----------------+-----------------------+
   | n               |                 | input           | number of             |
   |                 |                 |                 | columns of            |
   |                 |                 |                 | matrix ``A``          |
   |                 |                 |                 | and ``C``.            |
   +-----------------+-----------------+-----------------+-----------------------+
   | A               | device          | input           | <type> array of       |
   |                 |                 |                 | dimensions            |
   |                 |                 |                 | ``lda x n``           |
   |                 |                 |                 | with                  |
   |                 |                 |                 | ``lda>=max(1,m)``     |
   +-----------------+-----------------+-----------------+-----------------------+
   | lda             |                 | input           | leading               |
   |                 |                 |                 | dimension of          |
   |                 |                 |                 | two-dimensional       |
   |                 |                 |                 | array used to         |
   |                 |                 |                 | store the             |
   |                 |                 |                 | matrix ``A``.         |
   +-----------------+-----------------+-----------------+-----------------------+
   | x               | device          | input           | one-dimensional       |
   |                 |                 |                 | <type> array of       |
   |                 |                 |                 | size                  |
   |                 |                 |                 | :math:`|inc| \times m`|
   |                 |                 |                 | if                    |
   |                 |                 |                 | ``mode ==             |
   |                 |                 |                 | MCBLAS_SIDE_LEFT``    |
   |                 |                 |                 | and                   |
   |                 |                 |                 | :math:`|inc| \times n`|
   |                 |                 |                 | if                    |
   |                 |                 |                 | ``mode ==             |
   |                 |                 |                 | MCBLAS_SIDE_RIGHT``   |
   +-----------------+-----------------+-----------------+-----------------------+
   | incx            |                 | input           | stride of             |
   |                 |                 |                 | one-dimensional       |
   |                 |                 |                 | array ``x``.          |
   +-----------------+-----------------+-----------------+-----------------------+
   | C               | device          | in/out          | <type> array of       |
   |                 |                 |                 | dimensions            |
   |                 |                 |                 | ``ldc x n``           |
   |                 |                 |                 | with                  |
   |                 |                 |                 | ``ldc>=max(1,m)``.    |
   +-----------------+-----------------+-----------------+-----------------------+
   | ldc             |                 | input           | leading               |
   |                 |                 |                 | dimension of a        |
   |                 |                 |                 | two-dimensional       |
   |                 |                 |                 | array used to         |
   |                 |                 |                 | store the             |
   |                 |                 |                 | matrix ``C``.         |
   +-----------------+-----------------+-----------------+-----------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   | -  if ``mode`` !=                 |
   |                                   |    ``MCBLAS_SIDE_LEFT``,          |
   |                                   |    ``MCBLAS_SIDE_RIGHT`` or       |
   |                                   | -  if ``lda < max(1, m)`` or      |
   |                                   |    ``ldc < max(1, m)``            |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the function failed to launch on  |
   |                                   | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>getrfBatched()
------------------------

This routine is not supported now.

mcblas<t>getrsBatched()
-------------------------

This routine is not supported now.

mcblas<t>getriBatched()
------------------------

This routine is not supported now.

mcblas<t>matinvBatched()
--------------------------

This routine is not supported now.

mcblas<t>geqrfBatched()
-------------------------

This routine is not supported now.

mcblas<t>gelsBatched()
-----------------------

This routine is not supported now.

mcblas<t>tpttr()
------------------

::

   mcblasStatus_t mcblasStpttr(mcblasHandle_t handle,
                               mcblasFillMode_t uplo,
                               int n,
                               const float *AP,
                               float *A,
                               int lda );
                                          
   mcblasStatus_t mcblasDtpttr(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo,
                               int n,
                               const double *AP,
                               double *A,
                               int lda );

   mcblasStatus_t mcblasCtpttr(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo, 
                               int n,
                               const mcComplex *AP,
                               mcComplex *A,
                               int lda );
                                          
   mcblasStatus_t mcblasZtpttr(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo
                               int n,
                               const mcDoubleComplex *AP,
                               mcDoubleComplex *A,
                               int lda );

This function performs the conversion from the triangular
packed format to the triangular format

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the elements of
``AP`` are copied into the lower triangular part of the
triangular matrix ``A`` and the upper part of ``A`` is left
untouched. If ``uplo == MCBLAS_FILL_MODE_UPPER`` then the
elements of ``AP`` are copied into the upper triangular part
of the triangular matrix ``A`` and the lower part of ``A``
is left untouched.

.. table:: 
   :align: left

   +-----------------+-----------------+-----------------+-----------------+
   | Param.          | Memory          | In/out          | Meaning         |
   +=================+=================+=================+=================+
   | handle          |                 | input           | handle to the   |
   |                 |                 |                 | mcBLAS library  |
   |                 |                 |                 | context.        |
   +-----------------+-----------------+-----------------+-----------------+
   | uplo            |                 | input           | indicates if    |
   |                 |                 |                 | matrix ``AP``   |
   |                 |                 |                 | contains lower  |
   |                 |                 |                 | or upper part   |
   |                 |                 |                 | of matrix       |
   |                 |                 |                 | ``A``.          |
   +-----------------+-----------------+-----------------+-----------------+
   | n               |                 | input           | number of rows  |
   |                 |                 |                 | and columns of  |
   |                 |                 |                 | matrix ``A``.   |
   +-----------------+-----------------+-----------------+-----------------+
   | AP              | device          | input           | <type> array    |
   |                 |                 |                 | with            |
   |                 |                 |                 | :math:`A``      |
   |                 |                 |                 | stored in       |
   |                 |                 |                 | packed format.  |
   +-----------------+-----------------+-----------------+-----------------+
   | A               | device          | output          | <type> array of |
   |                 |                 |                 | dimensions      |
   |                 |                 |                 | ``lda x n`` ,   |
   |                 |                 |                 | with            |
   |                 |                 |                 | ``lda           |
   |                 |                 |                 | >= max(1,n)``.  |
   |                 |                 |                 | The opposite    |
   |                 |                 |                 | side of A is    |
   |                 |                 |                 | left untouched. |
   +-----------------+-----------------+-----------------+-----------------+
   | lda             |                 | input           | leading         |
   |                 |                 |                 | dimension of    |
   |                 |                 |                 | two-dimensional |
   |                 |                 |                 | array used to   |
   |                 |                 |                 | store matrix    |
   |                 |                 |                 | ``A``.          |
   +-----------------+-----------------+-----------------+-----------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n < 0`` or                |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                   | -  ``lda < max(1, n)``            |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>trttp()
-----------------

::

   mcblasStatus_t mcblasStrttp(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo, 
                               int n,
                               const float *A,
                               int lda,
                               float *AP );

   mcblasStatus_t mcblasDtrttp(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo, 
                               int n, 
                               const double *A,
                               int lda,
                               double *AP );

   mcblasStatus_t mcblasCtrttp(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo, 
                               int n,
                               const mcComplex *A,
                               int lda,
                               mcComplex *AP );
                                 
   mcblasStatus_t mcblasZtrttp(mcblasHandle_t handle, 
                               mcblasFillMode_t uplo, 
                               int n, 
                               const mcDoubleComplex *A,
                               int lda,
                               mcDoubleComplex *AP );

This function performs the conversion from the triangular
format to the triangular packed format

If ``uplo == MCBLAS_FILL_MODE_LOWER`` then the lower
triangular part of the triangular matrix ``A`` is copied
into the array ``AP``. If ``uplo == MCBLAS_FILL_MODE_UPPER``
then then the upper triangular part of the triangular matrix
``A`` is copied into the array ``AP``.

.. table::
   :align: left

   +-----------------+-----------------+-----------------+--------------------+
   | Param.          | Memory          | In/out          | Meaning            |
   +=================+=================+=================+====================+
   | handle          |                 | input           | handle to the      |
   |                 |                 |                 | mcBLAS library     |
   |                 |                 |                 | context.           |
   +-----------------+-----------------+-----------------+--------------------+
   | uplo            |                 | input           | indicates which    |
   |                 |                 |                 | matrix ``A``       |
   |                 |                 |                 | lower or upper     |
   |                 |                 |                 | part is            |
   |                 |                 |                 | referenced.        |
   +-----------------+-----------------+-----------------+--------------------+
   | n               |                 | input           | number of rows     |
   |                 |                 |                 | and columns of     |
   |                 |                 |                 | matrix ``A``.      |
   +-----------------+-----------------+-----------------+--------------------+
   | A               | device          | input           | <type> array of    |
   |                 |                 |                 | dimensions         |
   |                 |                 |                 | ``lda x n`` ,      |
   |                 |                 |                 | with               |
   |                 |                 |                 | ``lda>=max(1,n)``. |
   +-----------------+-----------------+-----------------+--------------------+
   | lda             |                 | input           | leading            |
   |                 |                 |                 | dimension of       |
   |                 |                 |                 | two-dimensional    |
   |                 |                 |                 | array used to      |
   |                 |                 |                 | store matrix       |
   |                 |                 |                 | ``A``.             |
   +-----------------+-----------------+-----------------+--------------------+
   | AP              | device          | output          | <type> array       |
   |                 |                 |                 | with               |
   |                 |                 |                 | :math:`A``         |
   |                 |                 |                 | stored in          |
   |                 |                 |                 | packed format.     |
   +-----------------+-----------------+-----------------+--------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :widths: grid
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``n < 0`` or                |
   |                                   |                                   |
   |                                   | -  if ``uplo`` !=                 |
   |                                   |    ``MCBLAS_FILL_MODE_UPPER``,    |
   |                                   |    ``MCBLAS_FILL_MODE_LOWER`` or  |
   |                                   | -  ``lda < max(1, n)``            |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblas<t>gemmEx()
-------------------

::

   mcblasStatus_t mcblasSgemmEx(mcblasHandle_t handle,
                                mcblasOperation_t transa,
                                mcblasOperation_t transb,
                                int m,
                                int n,
                                int k,
                                const float    *alpha,
                                const void     *A,
                                mcblasDataType Atype,
                                int lda,
                                const void     *B,
                                mcblasDataType Btype,
                                int ldb,
                                const float    *beta,
                                void           *C,
                                mcblasDataType_t Ctype,
                                int ldc)
   mcblasStatus_t mcblasCgemmEx(mcblasHandle_t handle,
                                mcblasOperation_t transa,
                                mcblasOperation_t transb,
                                int m,
                                int n,
                                int k,
                                const mcComplex *alpha,
                                const void      *A,
                                mcblasDataType_t  Atype,
                                int lda,
                                const void      *B,
                                mcblasDataType_t  Btype,
                                int ldb,
                                const mcComplex *beta,
                                void            *C,
                                mcblasDataType_t  Ctype,
                                int ldc)
                           
This function is an extension of ``mcblas<t>gemm.`` In this
function the input matrices and output matrices can have a
lower precision but the computation is still done in the
type ``<t>``. For example, in the type ``float`` for
``mcblasSgemmEx`` and in the type ``mcComplex`` for
``mcblasCgemmEx``.

.. math::
   C = \alpha\text{op}(A)\text{op}(B) + \beta C

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
, :math:`B`
and :math:`C`
are matrices stored in column-major format with dimensions
:math:`\text{op}(A)`
:math:`m \times k`
, :math:`\text{op}(B)`
:math:`k \times n`
and :math:`C`
:math:`m \times n`
, respectively. Also, for matrix
:math:`A`

.. :math::
   op(A) = \left\{ \begin{matrix}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{matrix} \right.

and :math:`\text{op}(B)`
is defined similarly for matrix :math:`B`
.

.. table::
   :align: left

   +--------+----------------+--------+---------------------------+
   | Param. | Memory         | In/out | Meaning                   |
   +========+================+========+===========================+
   | handle |                | input  | handle to the mcBLAS      |
   |        |                |        | library context.          |
   +--------+----------------+--------+---------------------------+
   | transa |                | input  | operation op(``A``)       |
   |        |                |        | that is non- or           |
   |        |                |        | (conj.) transpose.        |
   +--------+----------------+--------+---------------------------+
   | transb |                | input  | operation op(``B``)       |
   |        |                |        | that is non- or           |
   |        |                |        | (conj.) transpose.        |
   +--------+----------------+--------+---------------------------+
   | m      |                | input  | number of rows of         |
   |        |                |        | matrix op(``A``) and      |
   |        |                |        | ``C``.                    |
   +--------+----------------+--------+---------------------------+
   | n      |                | input  | number of columns of      |
   |        |                |        | matrix op(``B``) and      |
   |        |                |        | ``C``.                    |
   +--------+----------------+--------+---------------------------+
   | k      |                | input  | number of columns of      |
   |        |                |        | op(``A``) and rows of     |
   |        |                |        | op(``B``).                |
   +--------+----------------+--------+---------------------------+
   | alpha  | host or device | input  | <type> scalar used for    |
   |        |                |        | multiplication.           |
   +--------+----------------+--------+---------------------------+
   | A      | device         | input  | <type> array of           |
   |        |                |        | dimensions ``lda x k``    |
   |        |                |        | with ``lda>=max(1,m)``    |
   |        |                |        | if                        |
   |        |                |        | ``transa == MCBLAS_OP_N`` |
   |        |                |        | and ``lda x m`` with      |
   |        |                |        | ``lda>=max(1,k)``         |
   |        |                |        | otherwise.                |
   +--------+----------------+--------+---------------------------+
   | Atype  |                | input  | enumerant specifying      |
   |        |                |        | the datatype of matrix    |
   |        |                |        | ``A``.                    |
   +--------+----------------+--------+---------------------------+
   | lda    |                | input  | leading dimension of      |
   |        |                |        | two-dimensional array     |
   |        |                |        | used to store the         |
   |        |                |        | matrix ``A``.             |
   +--------+----------------+--------+---------------------------+
   | B      | device         | input  | <type> array of           |
   |        |                |        | dimension ``ldb x n``     |
   |        |                |        | with ``ldb>=max(1,k)``    |
   |        |                |        | if                        |
   |        |                |        | ``transb == MCBLAS_OP_N`` |
   |        |                |        | and ``ldb x k`` with      |
   |        |                |        | ``ldb>=max(1,n)``         |
   |        |                |        | otherwise.                |
   +--------+----------------+--------+---------------------------+
   | Btype  |                | input  | enumerant specifying      |
   |        |                |        | the datatype of matrix    |
   |        |                |        | ``B``.                    |
   +--------+----------------+--------+---------------------------+
   | ldb    |                | input  | leading dimension of      |
   |        |                |        | two-dimensional array     |
   |        |                |        | used to store matrix      |
   |        |                |        | ``B``.                    |
   +--------+----------------+--------+---------------------------+
   | beta   | host or device | input  | <type> scalar used for    |
   |        |                |        | multiplication. If        |
   |        |                |        | ``beta==0``, ``C``        |
   |        |                |        | does not have to be a     |
   |        |                |        | valid input.              |
   +--------+----------------+--------+---------------------------+
   | C      | device         | in/out | <type> array of           |
   |        |                |        | dimensions ``ldc x n``    |
   |        |                |        | with  ``ldc>=max(1,m)``.  |
   +--------+----------------+--------+---------------------------+
   | Ctype  |                | input  | enumerant specifying      |
   |        |                |        | the datatype of matrix    |
   |        |                |        | ``C``.                    |
   +--------+----------------+--------+---------------------------+
   | ldc    |                | input  | leading dimension of a    |
   |        |                |        | two-dimensional array     |
   |        |                |        | used to store the         |
   |        |                |        | matrix ``C``.             |
   +--------+----------------+--------+---------------------------+

The matrix types combinations supported for
``mcblasSgemmEx`` are listed below:

=================   ===============
C                   A/B
=================   ===============
``MCBLAS_R_16BF``   ``MCBLAS_R_16BF``
``MCBLAS_R_16F``    ``MCBLAS_R_16F``
``MCBLAS_R_32F``    ``MCBLAS_R_8I``
\                   ``MCBLAS_R_16BF``
\                   ``MCBLAS_R_16F``
\                   ``MCBLAS_R_32F``
=================   ===============

The matrix types combinations supported for
``mcblasCgemmEx`` are listed below :

================  ==============
C                 A/B
================  ==============
``MCBLAS_C_32F``  ``MCBLAS_C_8I``
\                 ``MCBLAS_C_32F``
================  ==============

The possible error values returned by this function and
their meanings are listed below.

.. table::
   :align: left

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_ARCH_MISMATCH``   | ``mcblasCgemmEx`` is only         |
   |                                   | supported for GPU with            |
   |                                   | architecture capabilities equal   |
   |                                   | or greater than 5.0               |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``   | the combination of the parameters |
   |                                   | ``Atype``,\ ``Btype`` and         |
   |                                   | ``Ctype`` is not supported        |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   |    ``k`` < 0 or                   |
   |                                   |                                   |
   |                                   | -  if ``transa`` or ``transb`` != |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``m``) if  |
   |                                   |    ``transa`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``k``) if  |
   |                                   |    ``transb`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``ldb`` < max(1, ``n``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  ``ldc`` < max(1, ``m``)        |
   +-----------------------------------+-----------------------------------+
   | `                                 | the function failed to launch on  |
   | `MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblasGemmEx()
----------------

::

   mcblasStatus_t mcblasGemmEx(mcblasHandle_t handle,
                               mcblasOperation_t transa,
                               mcblasOperation_t transb,
                               int m,
                               int n,
                               int k,
                               const void    *alpha,
                               const void     *A,
                               mcblasDataType_t Atype,
                               int lda,
                               const void     *B,
                               mcblasDataType_t Btype,
                               int ldb,
                               const void    *beta,
                               void           *C,
                               mcblasDataType_t Ctype,
                               int ldc,
                               mcblasComputeType_t computeType,
                               mcblasGemmAlgo_t algo)

   #if defined(__cplusplus)
   mcblasStatus_t mcblasGemmEx(mcblasHandle_t handle,
                               mcblasOperation_t transa,
                               mcblasOperation_t transb,
                               int m,
                               int n,
                               int k,
                               const void     *alpha,
                               const void     *A,
                               mcblasDataType_t   Atype,
                               int lda,
                               const void     *B,
                               mcblasDataType_t   Btype,
                               int ldb,
                               const void     *beta,
                               void           *C,
                               mcblasDataType_t   Ctype,
                               int ldc,
                               mcblasComputeType_t   computeType,
                               mcblasGemmAlgo_t algo)
   #endif
                           

This function is an extension of ``mcblas<t>gemm`` that
allows the user to individually specify the data types for
each of the A, B and C matrices, the precision of
computation and the GEMM algorithm to be run. Supported
combinations of arguments are listed further down in this
section.

Note: The second variant of ``mcblasGemmEx`` function is
provided for backward compatibility with C++ applications
code, where the ``computeType`` parameter is of
``mcblasDataType_t`` instead of ``mcblasComputeType_t``. C
applications would still compile with the updated function
signature.

.. math::
   C = \alpha\text{op}(A)\text{op}(B) + \beta C

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
, :math:`B`
and :math:`C`
are matrices stored in column-major format with dimensions
:math:`\text{op}(A)`
:math:`m \times k`
, :math:`\text{op}(B)`
:math:`k \times n`
and :math:`C`
:math:`m \times n`
, respectively. Also, for matrix
:math:`A`

.. math::
   op(A) = \left\{ \begin{matrix}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{matrix} \right.

and :math:`\text{op}(B)`
is defined similarly for matrix :math:`B`
.

.. table:: 
   :widths: grid

   +-------------+----------------+--------+---------------------+
   | Param.      | Memory         | In/out | Meaning             |
   +=============+================+========+=====================+
   | handle      |                | input  | handle to the       |
   |             |                |        | mcBLAS library      |
   |             |                |        | context.            |
   +-------------+----------------+--------+---------------------+
   | transa      |                | input  | operation op(``A``) |
   |             |                |        | that is non- or     |
   |             |                |        | (conj.) transpose.  |
   +-------------+----------------+--------+---------------------+
   | transb      |                | input  | operation op(``B``) |
   |             |                |        | that is non- or     |
   |             |                |        | (conj.) transpose.  |
   +-------------+----------------+--------+---------------------+
   | m           |                | input  | number of rows of   |
   |             |                |        | matrix op(``A``)    |
   |             |                |        | and ``C``.          |
   +-------------+----------------+--------+---------------------+
   | n           |                | input  | number of columns   |
   |             |                |        | of matrix op(``B``) |
   |             |                |        | and ``C``.          |
   +-------------+----------------+--------+---------------------+
   | k           |                | input  | number of columns   |
   |             |                |        | of op(``A``) and    |
   |             |                |        | rows of op(``B``).  |
   +-------------+----------------+--------+---------------------+
   | alpha       | host or device | input  | scaling factor for  |
   |             |                |        | A*B of the type     |
   |             |                |        | that corresponds to |
   |             |                |        | the computeType and |
   |             |                |        | Ctype, see the      |
   |             |                |        | table below for     |
   |             |                |        | details.            |
   +-------------+----------------+--------+---------------------+
   | A           | device         | input  | <type> array of     |
   |             |                |        | dimensions          |
   |             |                |        | ``lda x k`` with    |
   |             |                |        | ``lda>=max(1,m)``   |
   |             |                |        | if                  |
   |             |                |        | ``tran              |
   |             |                |        | sa == MCBLAS_OP_N`` |
   |             |                |        | and ``lda x m``     |
   |             |                |        | with                |
   |             |                |        | ``lda>=max(1,k)``   |
   |             |                |        | otherwise.          |
   +-------------+----------------+--------+---------------------+
   | Atype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of matrix  |
   |             |                |        | ``A``.              |
   +-------------+----------------+--------+---------------------+
   | lda         |                | input  | leading dimension   |
   |             |                |        | of two-dimensional  |
   |             |                |        | array used to store |
   |             |                |        | the matrix ``A``.   |
   +-------------+----------------+--------+---------------------+
   | B           | device         | input  | <type> array of     |
   |             |                |        | dimension           |
   |             |                |        | ``ldb x n`` with    |
   |             |                |        | ``ldb>=max(1,k)``   |
   |             |                |        | if                  |
   |             |                |        | ``tran              |
   |             |                |        | sb == MCBLAS_OP_N`` |
   |             |                |        | and ``ldb x k``     |
   |             |                |        | with                |
   |             |                |        | ``ldb>=max(1,n)``   |
   |             |                |        | otherwise.          |
   +-------------+----------------+--------+---------------------+
   | Btype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of matrix  |
   |             |                |        | ``B``.              |
   +-------------+----------------+--------+---------------------+
   | ldb         |                | input  | leading dimension   |
   |             |                |        | of two-dimensional  |
   |             |                |        | array used to store |
   |             |                |        | matrix ``B``.       |
   +-------------+----------------+--------+---------------------+
   | beta        | host or device | input  | scaling factor for  |
   |             |                |        | C of the type that  |
   |             |                |        | corresponds to the  |
   |             |                |        | computeType and     |
   |             |                |        | Ctype, see the      |
   |             |                |        | table below for     |
   |             |                |        | details. If         |
   |             |                |        | ``beta==0``, ``C``  |
   |             |                |        | does not have to be |
   |             |                |        | a valid input.      |
   +-------------+----------------+--------+---------------------+
   | C           | device         | in/out | <type> array of     |
   |             |                |        | dimensions          |
   |             |                |        | ``ldc x n`` with    |
   |             |                |        | ``ldc>=max(1,m)``.  |
   +-------------+----------------+--------+---------------------+
   | Ctype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of matrix  |
   |             |                |        | ``C``.              |
   +-------------+----------------+--------+---------------------+
   | ldc         |                | input  | leading dimension   |
   |             |                |        | of a                |
   |             |                |        | two-dimensional     |
   |             |                |        | array used to store |
   |             |                |        | the matrix ``C``.   |
   +-------------+----------------+--------+---------------------+
   | computeType |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | computation type.   |
   +-------------+----------------+--------+---------------------+
   | algo        |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | algorithm.          |
   +-------------+----------------+--------+---------------------+

``mcblasGemmEx`` supports the following Compute Type, Scale
Type, Atype/Btype, and Ctype:

.. table:: 
   :widths: grid

   +----------------------------------------+-----------------+-----------------+-----------------+
   | Compute Type                           | Scale Type      | Atype/Btype     | Ctype           |
   |                                        | (alpha and      |                 |                 |
   |                                        | beta)           |                 |                 |
   +========================================+=================+=================+=================+
   | ``MCBLAS_COMPUTE_16F``                 | ``MCBLAS_R_16F``| ``MCBLAS_R_16F``| ``MCBLAS_R_16F``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_16F_PEDANTIC``        |                 |                 |                 |
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_32I``                 | ``MCBLAS_R_32I``| ``MCBLAS_R_8I`` | ``MCBLAS_R_32I``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_32I_PEDANTIC``        |                 |                 |                 |
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_32F``                 | ``MCBLAS_R_32F``|``MCBLAS_R_16BF``|``MCBLAS_R_16BF``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_32F_PEDANTIC``        |                 |                 |                 |
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_16F``| ``MCBLAS_R_16F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_8I`` | ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 |``MCBLAS_R_16BF``| ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_16F``| ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_32F``| ``MCBLAS_R_32F``|
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_32F``| ``MCBLAS_C_8I`` | ``MCBLAS_C_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_C_32F``| ``MCBLAS_C_32F``|
   +----------------------------------------+-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_R_32F``| ``MCBLAS_R_32F``| ``MCBLAS_R_32F``|
   |``MCBLAS_COMPUTE_32F_FAST_16F``         |                 |                 |                 |
   |or                                      |                 |                 |                 |
   |``MCBLAS_COMPUTE_32F_FAST_16BF``        |                 |                 |                 |
   |or                                      |                 |                 |                 |
   |``MCBLAS_COMPUTE_32F_FAST_TF32``        |                 |                 |                 |
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_32F``| ``MCBLAS_C_32F``| ``MCBLAS_C_32F``|
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_64F``                 | ``MCBLAS_R_64F``| ``MCBLAS_R_64F``| ``MCBLAS_R_64F``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_64F_PEDANTIC``        |                 |                 |                 |
   |                                        |                 |                 |                 |
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_64F``| ``MCBLAS_C_64F``| ``MCBLAS_C_64F``|
   +----------------------------------------+-----------------+-----------------+-----------------+

Note: ``MCBLAS_COMPUTE_32I`` and
``MCBLAS_COMPUTE_32I_PEDANTIC`` compute types are only
supported with A, B being 4-byte aligned and lda, ldb being
multiples of 4. 

``mcblasGemmEx`` routine is run for the algorithms in the
following table. Note: for MetaX C500 Architecture GPUs
, the algorithms below are
equivalent to ``MCBLAS_GEMM_DEFAULT`` or
``MCBLAS_GEMM_DEFAULT_TENSOR_OP`` respectively. Specifying
algorithm >= 99 for a single precision operation is
equivalent to using ``MCBLAS_COMPUTE_32F_FAST_16F`` compute
type, even if math mode or compute type are specified to be
``MCBLAS_COMPUTE_32F`` or ``MCBLAS_COMPUTE_32F_FAST_TF32``.

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | mcblasGemmAlgo_t                 | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_GEMM_DEFAULT``          | Apply Heuristics to select the   |
   |                                  | GEMM algorithm                   |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_GEMM_ALGO0``            | Explicitly choose an algorithm   |
   | to                               |                                  |
   | ``MCBLAS_GEMM_ALGO23``           |                                  |
   +----------------------------------+----------------------------------+
   |                                  | Apply Heuristics to select the   |
   | ``MCBLAS_GEMM_DEFAULT_TENSOR_OP``| GEMM algorithm while allowing    |
   |                                  | the use of Tensor Core           |
   |                                  | operations if possible           |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_GEMM_ALGO0_TENSOR_OP``  | Explicitly choose a GEMM         |
   | to                               | algorithm allowing it to use     |
   | ``MCBLAS_GEMM_ALGO15_TENSOR_OP`` | Tensor Core operations if        |
   |                                  | possible, otherwise falls back   |
   |                                  | to ``mcblas<t>gemmBatched``      |
   |                                  | based on computeType             |
   +----------------------------------+----------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_ARCH_MISMATCH``   | ``mcblasGemmEx`` is only          |
   |                                   | supported for GPU with            |
   |                                   | architecture capabilities equal   |
   |                                   | or greater than 5.0               |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``   | the combination of the parameters |
   |                                   | ``Atype``,\ ``Btype`` and         |
   |                                   | ``Ctype`` or the                  |
   |                                   | algorithm,\ ``algo``\ is not      |
   |                                   | supported                         |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   |    ``k`` < 0 or                   |
   |                                   |                                   |
   |                                   | -  if ``transa`` or ``transb`` != |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``m``) if  |
   |                                   |    ``transa`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``k``) if  |
   |                                   |    ``transb`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``ldb`` < max(1, ``n``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``m``) or  |
   |                                   |                                   |
   |                                   | -  ``Atype`` or ``Btype`` or      |
   |                                   |    ``Ctype`` or ``algo`` is not   |
   |                                   |    supported                      |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblasGemmBatchedEx()
----------------------

This routine is not supported now.

mcblasGemmStridedBatchedEx()
------------------------------

::

   mcblasStatus_t mcblasGemmStridedBatchedEx(mcblasHandle_t handle,
                                             mcblasOperation_t transa,
                                             mcblasOperation_t transb,
                                             int m,
                                             int n,
                                             int k,
                                             const void    *alpha,
                                             const void     *A,
                                             mcblasDataType_t Atype,
                                             int lda,
                                             mcblas_stride strideA,
                                             const void     *B,
                                             mcblasDataType_t Btype,
                                             int ldb,
                                             mcblas_stride strideB,
                                             const void    *beta,
                                             void           *C,
                                             mcblasDataType_t Ctype,
                                             int ldc,
                                             mcblas_stride strideC,
                                             int batchCount,
                                             mcblasComputeType_t computeType,
                                             mcblasGemmAlgo_t algo)

   #if defined(__cplusplus)
   mcblasStatus_t mcblasGemmStridedBatchedEx(mcblasHandle_t handle,
                                             mcblasOperation_t transa,
                                             mcblasOperation_t transb,
                                             int m,
                                             int n,
                                             int k,
                                             const void    *alpha,
                                             const void     *A,
                                             mcblasDataType_t Atype,
                                             int lda,
                                             mcblas_stride strideA,
                                             const void     *B,
                                             mcblasDataType_t Btype,
                                             int ldb,
                                             mcblas_stride strideB,
                                             const void    *beta,
                                             void           *C,
                                             mcblasDataType_t Ctype,
                                             int ldc,
                                             mcblas_stride strideC,
                                             int batchCount,
                                             mcblasDataType_t computeType,
                                             mcblasGemmAlgo_t algo)
   #endif
         
This function is an extension of
``mcblas<t>gemmStridedBatched`` that performs the
matrix-matrix multiplication of a batch of matrices and
allows the user to individually specify the data types for
each of the A, B and C matrices, the precision of
computation and the GEMM algorithm to be run. Like
``mcblas<t>gemmStridedBatched``, the batch is considered to
be "uniform", i.e. all instances have the same dimensions
(m, n, k), leading dimensions (lda, ldb, ldc) and
transpositions (transa, transb) for their respective A, B
and C matrices. Input matrices A, B and output matrix C for
each instance of the batch are located at fixed offsets in
number of elements from their locations in the previous
instance. Pointers to A, B and C matrices for the first
instance are passed to the function by the user along with
the offsets in number of elements - strideA, strideB and
strideC that determine the locations of input and output
matrices in future instances.

Note: The second variant of ``mcblasGemmStridedBatchedEx``
function is provided for backward compatibility with C++
applications code, where the ``computeType`` parameter is of
``mcblasDataType_t_`` instead of ``mcblasComputeType_t``. C
applications would still compile with the updated function
signature.

.. math::
   \begin{gathered}
   C + i*{strideC} = \alpha\text{op}(A + i*{strideA})\text{op}(B + i*{strideB}) + \beta(C + i*{strideC}), \\
   \text{ for i } \in \lbrack 0,batchCount - 1\rbrack
   \end{gathered}

where :math:`\alpha`
and :math:`\beta`
are scalars, and :math:`A`
, :math:`B`
and :math:`C`
are arrays of pointers to matrices stored in column-major
format with dimensions
:math:`\text{op}(A\lbrack i\rbrack)`
:math:`m \times k`
,
:math:`\text{op}(B\lbrack i\rbrack)`
:math:`k \times n`
and :math:`C\lbrack i\rbrack`
:math:`m \times n`
, respectively. Also, for matrix
:math:`A`

.. math::
   op(A) = \left\{\begin{matrix}
   A & if \enspace transa == MCBLAS\_OP\_N \\
   A^{T} & if \enspace transa == MCBLAS\_OP\_T \\
   A^{H} & if \enspace transa == MCBLAS\_OP\_C \\
   \end{matrix} \right.

and
:math:`\text{op}(B\lbrack i\rbrack)`
is defined similarly for matrix
:math:`B\lbrack i\rbrack`
.
Note: :math:`C\lbrack i\rbrack`
matrices must not overlap, i.e. the individual gemm
operations must be computable independently; otherwise,
undefined behavior is expected.
On certain problem sizes, it might be advantageous to make
multiple calls to ``mcblas<t>gemm`` in different MACA
streams, rather than use this API.

Note: In the table below, we use ``A[i], B[i], C[i]`` as
notation for A, B and C matrices in the ith instance of the
batch, implicitly assuming they are respectively offsets in
number of elements ``strideA, strideB, strideC`` away from
``A[i-1], B[i-1], C[i-1]``. The unit for the offset is
number of elements and must not be zero .

.. table:: 
   :widths: 15 15 7 60

   +-------------+----------------+--------+---------------------+
   | Param.      | Memory         | In/out | Meaning             |
   +=============+================+========+=====================+
   | handle      |                | input  | handle to the       |
   |             |                |        | mcBLAS library      |
   |             |                |        | context.            |
   +-------------+----------------+--------+---------------------+
   | transa      |                | input  | operation           |
   |             |                |        | op(``A[i]``) that   |
   |             |                |        | is non- or (conj.)  |
   |             |                |        | transpose.          |
   +-------------+----------------+--------+---------------------+
   | transb      |                | input  | operation           |
   |             |                |        | op(``B[i]``) that   |
   |             |                |        | is non- or (conj.)  |
   |             |                |        | transpose.          |
   +-------------+----------------+--------+---------------------+
   | m           |                | input  | number of rows of   |
   |             |                |        | matrix op(``A[i]``) |
   |             |                |        | and ``C[i]``.       |
   +-------------+----------------+--------+---------------------+
   | n           |                | input  | number of columns   |
   |             |                |        | of matrix           |
   |             |                |        | op(``B[i]``) and    |
   |             |                |        | ``C[i]``.           |
   +-------------+----------------+--------+---------------------+
   | k           |                | input  | number of columns   |
   |             |                |        | of op(``A[i]``) and |
   |             |                |        | rows of             |
   |             |                |        | op(``B[i]``).       |
   +-------------+----------------+--------+---------------------+
   | alpha       | host or device | input  | scaling factor for  |
   |             |                |        | A*B of the type     |
   |             |                |        | that corresponds to |
   |             |                |        | the computeType and |
   |             |                |        | Ctype, see the      |
   |             |                |        | table below for     |
   |             |                |        | details.            |
   +-------------+----------------+--------+---------------------+
   | A           | device         | input  | pointer to <Atype>  |
   |             |                |        | matrix, A,          |
   |             |                |        | corresponds to the  |
   |             |                |        | first instance of   |
   |             |                |        | the batch, with     |
   |             |                |        | dimensions          |
   |             |                |        | ``lda x k`` with    |
   |             |                |        | ``lda>=max(1,m)``   |
   |             |                |        | if                  |
   |             |                |        | ``tran              |
   |             |                |        | sa == MCBLAS_OP_N`` |
   |             |                |        | and ``lda x m``     |
   |             |                |        | with                |
   |             |                |        | ``lda>=max(1,k)``   |
   |             |                |        | otherwise.          |
   +-------------+----------------+--------+---------------------+
   | Atype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of ``A``.  |
   +-------------+----------------+--------+---------------------+
   | lda         |                | input  | leading dimension   |
   |             |                |        | of two-dimensional  |
   |             |                |        | array used to store |
   |             |                |        | the matrix          |
   |             |                |        | ``A[i]``.           |
   +-------------+----------------+--------+---------------------+
   | strideA     |                | input  | value of type long  |
   |             |                |        | long int that gives |
   |             |                |        | the offset in       |
   |             |                |        | number of elements  |
   |             |                |        | between ``A[i]``    |
   |             |                |        | and ``A[i+1]``.     |
   +-------------+----------------+--------+---------------------+
   | B           | device         | input  | pointer to <Btype>  |
   |             |                |        | matrix, B,          |
   |             |                |        | corresponds to the  |
   |             |                |        | first instance of   |
   |             |                |        | the batch, with     |
   |             |                |        | dimensions          |
   |             |                |        | ``ldb x n`` with    |
   |             |                |        | ``ldb>=max(1,k)``   |
   |             |                |        | if                  |
   |             |                |        | ``tran              |
   |             |                |        | sb == MCBLAS_OP_N`` |
   |             |                |        | and ``ldb x k``     |
   |             |                |        | with                |
   |             |                |        | ``ldb>=max(1,n)``   |
   |             |                |        | otherwise.          |
   +-------------+----------------+--------+---------------------+
   | Btype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of ``B``.  |
   +-------------+----------------+--------+---------------------+
   | ldb         |                | input  | leading dimension   |
   |             |                |        | of two-dimensional  |
   |             |                |        | array used to store |
   |             |                |        | matrix ``B[i]``.    |
   +-------------+----------------+--------+---------------------+
   | strideB     |                | input  | value of type long  |
   |             |                |        | long int that gives |
   |             |                |        | the offset in       |
   |             |                |        | number of elements  |
   |             |                |        | between ``B[i]``    |
   |             |                |        | and ``B[i+1]``.     |
   +-------------+----------------+--------+---------------------+
   | beta        | host or device | input  | scaling factor for  |
   |             |                |        | C of the type that  |
   |             |                |        | corresponds to the  |
   |             |                |        | computeType and     |
   |             |                |        | Ctype, see the      |
   |             |                |        | table below for     |
   |             |                |        | details. If         |
   |             |                |        | ``beta==0``,        |
   |             |                |        | ``C[i]`` does not   |
   |             |                |        | have to be a valid  |
   |             |                |        | input.              |
   +-------------+----------------+--------+---------------------+
   | C           | device         | in/out | pointer to <Ctype>  |
   |             |                |        | matrix, C,          |
   |             |                |        | corresponds to the  |
   |             |                |        | first instance of   |
   |             |                |        | the batch, with     |
   |             |                |        | dimensions          |
   |             |                |        | ``ldc x n`` with    |
   |             |                |        | ``ldc>=max(1,m)``.  |
   |             |                |        | Matrices ``C[i]``   |
   |             |                |        | should not overlap; |
   |             |                |        | otherwise,          |
   |             |                |        | undefined behavior  |
   |             |                |        | is expected.        |
   +-------------+----------------+--------+---------------------+
   | Ctype       |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | datatype of ``C``.  |
   +-------------+----------------+--------+---------------------+
   | ldc         |                | input  | leading dimension   |
   |             |                |        | of a                |
   |             |                |        | two-dimensional     |
   |             |                |        | array used to store |
   |             |                |        | each matrix         |
   |             |                |        | ``C[i]``.           |
   +-------------+----------------+--------+---------------------+
   | strideC     |                | input  | value of type long  |
   |             |                |        | long int that gives |
   |             |                |        | the offset in       |
   |             |                |        | number of elements  |
   |             |                |        | between ``C[i]``    |
   |             |                |        | and ``C[i+1]``.     |
   +-------------+----------------+--------+---------------------+
   | batchCount  |                | input  | number of GEMMs to  |
   |             |                |        | perform in the      |
   |             |                |        | batch.              |
   +-------------+----------------+--------+---------------------+
   | computeType |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | computation type.   |
   +-------------+----------------+--------+---------------------+
   | algo        |                | input  | enumerant           |
   |             |                |        | specifying the      |
   |             |                |        | algorithm.          |
   +-------------+----------------+--------+---------------------+

``mcblasGemmStridedBatchedEx`` supports the following
Compute Type, Scale Type, Atype/Btype, and Ctype:

.. table:: 
   :widths: grid

   +----------------------------------------+-----------------+-----------------+-----------------+
   | Compute Type                           | Scale Type      | Atype/Btype     | Ctype           |
   |                                        | (alpha and      |                 |                 |
   |                                        | beta)           |                 |                 |
   +========================================+=================+=================+=================+
   | ``MCBLAS_COMPUTE_16F``                 | ``MCBLAS_R_16F``| ``MCBLAS_R_16F``| ``MCBLAS_R_16F``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_16F_PEDANTIC``        |                 |                 |                 |
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_32I``                 | ``MCBLAS_R_32I``| ``MCBLAS_R_8I`` | ``MCBLAS_R_32I``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_32I_PEDANTIC``        |                 |                 |                 |
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_32F``                 | ``MCBLAS_R_32F``|``MCBLAS_R_16BF``|``MCBLAS_R_16BF``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_32F_PEDANTIC``        |                 |                 |                 |
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_16F``| ``MCBLAS_R_16F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_8I`` | ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 |``MCBLAS_R_16BF``| ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_16F``| ``MCBLAS_R_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_R_32F``| ``MCBLAS_R_32F``|
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_32F``| ``MCBLAS_C_8I`` | ``MCBLAS_C_32F``|
   |                                        |                 +-----------------+-----------------+
   |                                        |                 | ``MCBLAS_C_32F``| ``MCBLAS_C_32F``|
   +----------------------------------------+-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_R_32F``| ``MCBLAS_R_32F``| ``MCBLAS_R_32F``|
   |``MCBLAS_COMPUTE_32F_FAST_16F``         |                 |                 |                 |
   |or                                      |                 |                 |                 |
   |``MCBLAS_COMPUTE_32F_FAST_16BF``        |                 |                 |                 |
   |or                                      |                 |                 |                 |
   |``MCBLAS_COMPUTE_32F_FAST_TF32``        |                 |                 |                 |
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_32F``| ``MCBLAS_C_32F``| ``MCBLAS_C_32F``|
   +----------------------------------------+-----------------+-----------------+-----------------+
   | ``MCBLAS_COMPUTE_64F``                 | ``MCBLAS_R_64F``| ``MCBLAS_R_64F``| ``MCBLAS_R_64F``|
   | or                                     |                 |                 |                 |
   | ``MCBLAS_COMPUTE_64F_PEDANTIC``        |                 |                 |                 |
   |                                        |                 |                 |                 |
   |                                        +-----------------+-----------------+-----------------+
   |                                        | ``MCBLAS_C_64F``| ``MCBLAS_C_64F``| ``MCBLAS_C_64F``|
   +----------------------------------------+-----------------+-----------------+-----------------+

Compute types ``MCBLAS_COMPUTE_32I`` and
``MCBLAS_COMPUTE_32I_PEDANTIC`` are only supported with all
pointers ``A[i]``, ``B[i]`` being 4-byte aligned and lda,
ldb being multiples of 4. 

``mcblasGemmStridedBatchedEx`` routine is run for the
algorithms in the following table. Note: for MetaX Ampere
Architecture GPUs and beyond, i.e. SM version >= 80, the
algorithms below are equivalent to ``MCBLAS_GEMM_DEFAULT``
or ``MCBLAS_GEMM_DEFAULT_TENSOR_OP`` respectively.

.. table:: 
   :widths: grid

   +----------------------------------+----------------------------------+
   | mcblasGemmAlgo_t                 | Meaning                          |
   +==================================+==================================+
   | ``MCBLAS_GEMM_DEFAULT``          | Apply Heuristics to select the   |
   |                                  | GEMM algorithm                   |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_GEMM_ALGO0              | Explicitly choose an algorithm   |
   | to MCBLAS_GEMM_ALGO23``          |                                  |
   +----------------------------------+----------------------------------+
   |                                  | Apply Heuristics to select the   |
   | ``MCBLAS_GEMM_DEFAULT_TENSOR_OP``| GEMM algorithm while allowing    |
   |                                  | the use of Tensor Core           |
   |                                  | operations if possible           |
   +----------------------------------+----------------------------------+
   | ``MCBLAS_GEMM_ALGO0_TENSOR_OP    | Explicitly choose a GEMM         |
   | to MCBLAS_GEMM_ALGO15_TENSOR_OP``| algorithm allowing it to use     |
   |                                  | Tensor Core operations if        |
   |                                  | possible, otherwise falls back   |
   |                                  | to ``mcblas<t>gemmBatched``      |
   |                                  | based on computeType             |
   +----------------------------------+----------------------------------+

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+-----------------------------------+
   | Error Value                       | Meaning                           |
   +===================================+===================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed           |
   |                                   | successfully                      |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` | the library was not initialized   |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_ARCH_MISMATCH``   | ``mcBLASGemmBatchedEx`` is only   |
   |                                   | supported for GPU with            |
   |                                   | architecture capabilities equal   |
   |                                   | or greater than 5.0               |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``   | the combination of the parameters |
   |                                   | ``Atype``,\ ``Btype`` and         |
   |                                   | ``Ctype`` or the                  |
   |                                   | algorithm,\ ``algo``\ is not      |
   |                                   | supported                         |
   +-----------------------------------+-----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | -  If ``m`` < 0 or ``n`` < 0 or   |
   |                                   |    ``k`` < 0 or                   |
   |                                   |                                   |
   |                                   | -  if ``transa`` or ``transb`` != |
   |                                   |    ``MCBLAS_OP_N``,               |
   |                                   |    ``MCBLAS_OP_C``,               |
   |                                   |    ``MCBLAS_OP_T`` or             |
   |                                   |                                   |
   |                                   | -  if ``lda`` < max(1, ``m``) if  |
   |                                   |    ``transa`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``lda`` < max(1, ``k``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldb`` < max(1, ``k``) if  |
   |                                   |    ``transb`` == ``MCBLAS_OP_N``  |
   |                                   |    and ``ldb`` < max(1, ``n``)    |
   |                                   |    otherwise or                   |
   |                                   |                                   |
   |                                   | -  if ``ldc`` < max(1, ``m``) or  |
   |                                   |                                   |
   |                                   | -  ``Atype`` or ``Btype`` or      |
   |                                   |    ``Ctype`` or ``algo`` or       |
   |                                   |    ``computeType`` is not         |
   |                                   |    supported                      |
   +-----------------------------------+-----------------------------------+
   |                                   | the function failed to launch on  |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                           |
   +-----------------------------------+-----------------------------------+

mcblasCsyrkEx()
----------------

This routine is not supported now.

mcblasCsyrk3mEx()
------------------

This routine is not supported now.

mcblasCherkEx()
-----------------

This routine is not supported now.

mcblasCherk3mEx()
------------------

This routine is not supported now.


mcblasAxpyEx()
----------------

::

   mcblasStatus_t mcblasAxpyEx(mcblasHandle_t handle,
                               int n,
                               const void *alpha,
                               mcblasDataType_t alphaType,
                               const void *x,
                               mcblasDataType_t xType,
                               int incx,
                               void *y,
                               mcblasDataType_t yType,
                               int incy,
                               mcblasDataType_t executiontype);

.. table:: 
   :widths: grid

   +---------------+----------------+--------+--------------------+
   | Param.        | Memory         | In/out | Meaning            |
   +===============+================+========+====================+
   | handle        |                | input  | handle to the      |
   |               |                |        | mcBLAS library     |
   |               |                |        | context.           |
   +---------------+----------------+--------+--------------------+
   | alpha         | host or device | input  | <type> scalar used |
   |               |                |        | for                |
   |               |                |        | multiplication.    |
   +---------------+----------------+--------+--------------------+
   | n             |                | input  | number of elements |
   |               |                |        | in the vector      |
   |               |                |        | ``x`` and ``y``.   |
   +---------------+----------------+--------+--------------------+
   | x             | device         | input  | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | xType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``x``.             |
   +---------------+----------------+--------+--------------------+
   | incx          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``x``. |
   +---------------+----------------+--------+--------------------+
   | y             | device         | in/out | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | yType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``y``.             |
   +---------------+----------------+--------+--------------------+
   | incy          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``y``. |
   +---------------+----------------+--------+--------------------+
   | executionType |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype in which  |
   |               |                |        | the computation is |
   |               |                |        | executed.          |
   +---------------+----------------+--------+--------------------+

The datatypes combinations currently supported for
``mcblasAxpyEx`` are listed below :

================ ================ ==============
x                y                execution
================ ================ ==============
``MCBLAS_R_16F`` ``MCBLAS_R_16F`` ``MCBLAS_R_32F``
``MCBLAS_R_32F`` ``MCBLAS_R_32F`` ``MCBLAS_R_32F``
``MCBLAS_R_64F`` ``MCBLAS_R_64F`` ``MCBLAS_R_64F``
``MCBLAS_C_32F`` ``MCBLAS_C_32F`` ``MCBLAS_C_32F``
``MCBLAS_C_64F`` ``MCBLAS_C_64F`` ``MCBLAS_C_64F``
================ ================ ==============

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   |                                   | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` |                                  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``   | the combination of the           |
   |                                   | parameters                       |
   |                                   | ``xType``,\ ``yType``, and       |
   |                                   | ``executionType`` is not         |
   |                                   | supported                        |
   +-----------------------------------+----------------------------------+
   |                                   | the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                          |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | ``alphaType`` or ``xType`` or    |
   |                                   | ``yType`` or ``executionType``   |
   |                                   | is not supported                 |
   +-----------------------------------+----------------------------------+

mcblasDotEx()
---------------

::

   mcblasStatus_t mcblasDotEx(mcblasHandle_t handle,
                              int n,
                              const void *x,
                              mcblasDataType_t xType,
                              int incx,
                              const void *y,
                              mcblasDataType_t yType,
                              int incy,
                              void *result,
                              mcblasDataType_t resultType,
                              mcblasDataType_t executionType);

   mcblasStatus_t mcblasDotcEx(mcblasHandle_t handle,
                              int n,
                              const void *x,
                              mcblasDataType_t xType,
                              int incx,
                              const void *y,
                              mcblasDataType_t yType,
                              int incy,
                              void *result,
                              mcblasDataType_t resultType,
                              mcblasDataType_t executionType);

.. table:: 
   :widths: grid

   +---------------+----------------+--------+--------------------+
   | Param.        | Memory         | In/out | Meaning            |
   +===============+================+========+====================+
   | handle        |                | input  | handle to the      |
   |               |                |        | mcBLAS library     |
   |               |                |        | context.           |
   +---------------+----------------+--------+--------------------+
   | n             |                | input  | number of elements |
   |               |                |        | in the vectors     |
   |               |                |        | ``x`` and ``y``.   |
   +---------------+----------------+--------+--------------------+
   | x             | device         | input  | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | xType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``x``.             |
   +---------------+----------------+--------+--------------------+
   | incx          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``x``. |
   +---------------+----------------+--------+--------------------+
   | y             | device         | input  | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | yType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``y``.             |
   +---------------+----------------+--------+--------------------+
   | incy          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``y``. |
   +---------------+----------------+--------+--------------------+
   | result        | host or device | output | the resulting dot  |
   |               |                |        | product, which is  |
   |               |                |        | ``0.0`` if         |
   |               |                |        | ``n<=0``.          |
   +---------------+----------------+--------+--------------------+
   | resultType    |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of the    |
   |               |                |        | ``result``.        |
   +---------------+----------------+--------+--------------------+
   | executionType |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype in which  |
   |               |                |        | the computation is |
   |               |                |        | executed.          |
   +---------------+----------------+--------+--------------------+

The datatypes combinations currently supported for
``mcblasDotEx`` and ``mcblasDotcEx`` are listed below :

================ ================ ================ ==============
x                y                result           execution
================ ================ ================ ==============
``MCBLAS_R_16F`` ``MCBLAS_R_16F`` ``MCBLAS_R_16F`` ``MCBLAS_R_32F``
``MCBLAS_R_32F`` ``MCBLAS_R_32F`` ``MCBLAS_R_32F`` ``MCBLAS_R_32F``
``MCBLAS_R_64F`` ``MCBLAS_R_64F`` ``MCBLAS_R_64F`` ``MCBLAS_R_64F``
``MCBLAS_C_32F`` ``MCBLAS_C_32F`` ``MCBLAS_C_32F`` ``MCBLAS_C_32F``
``MCBLAS_C_64F`` ``MCBLAS_C_64F`` ``MCBLAS_C_64F`` ``MCBLAS_C_64F``
================ ================ ================ ==============

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +-----------------------------------+----------------------------------+
   | Error Value                       | Meaning                          |
   +===================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``         | the operation completed          |
   |                                   | successfully                     |
   +-----------------------------------+----------------------------------+
   |                                   | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED`` |                                  |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_ALLOC_FAILED``    | the reduction buffer could not   |
   |                                   | be allocated                     |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``   | the combination of the           |
   |                                   | parameters                       |
   |                                   | ``xType``,\ ``yType``,           |
   |                                   | ``resultType`` and               |
   |                                   | ``executionType`` is not         |
   |                                   | supported                        |
   +-----------------------------------+----------------------------------+
   |                                   | the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED``| the GPU                          |
   +-----------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``   | ``xType`` or ``yType`` or        |
   |                                   | ``resultType`` or                |
   |                                   | ``executionType`` is not         |
   |                                   | supported                        |
   +-----------------------------------+----------------------------------+

mcblasRotEx()
---------------

::

   mcblasStatus_t mcblasRotEx(mcblasHandle_t handle,
                              int n,
                              void *x,
                              mcblasDataType_t xType,
                              int incx,
                              void *y,
                              mcblasDataType_t yType,
                              int incy,
                              const void *c,  /* host or device pointer */
                              const void *s,
                              mcblasDataType_t csType,
                              mcblasDataType_t executiontype);

This function is an extension to the routine
``mcblas<t>rot`` where input data, output data, cosine/sine
type, and compute type can be specified independently.

.. table:: 
   :widths: grid

   +---------------+----------------+--------+--------------------+
   | Param.        | Memory         | In/out | Meaning            |
   +===============+================+========+====================+
   | handle        |                | input  | handle to the      |
   |               |                |        | mcBLAS library     |
   |               |                |        | context.           |
   +---------------+----------------+--------+--------------------+
   | n             |                | input  | number of elements |
   |               |                |        | in the vectors     |
   |               |                |        | ``x`` and ``y``.   |
   +---------------+----------------+--------+--------------------+
   | x             | device         | in/out | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | xType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``x``.             |
   +---------------+----------------+--------+--------------------+
   | incx          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``x``. |
   +---------------+----------------+--------+--------------------+
   | y             | device         | in/out | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | yType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``y``.             |
   +---------------+----------------+--------+--------------------+
   | incy          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``y``. |
   +---------------+----------------+--------+--------------------+
   | c             | host or device | input  | cosine element of  |
   |               |                |        | the rotation       |
   |               |                |        | matrix.            |
   +---------------+----------------+--------+--------------------+
   | s             | host or device | input  | sine element of    |
   |               |                |        | the rotation       |
   |               |                |        | matrix.            |
   +---------------+----------------+--------+--------------------+
   | csType        |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of ``c``  |
   |               |                |        | and ``s``.         |
   +---------------+----------------+--------+--------------------+
   | executionType |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype in which  |
   |               |                |        | the computation is |
   |               |                |        | executed.          |
   +---------------+----------------+--------+--------------------+

The datatypes combinations currently supported for
``mcblasRotEx`` are listed below :

================   =================   ===============
executionType      xType / yType       csType
================   =================   ===============
``MCBLAS_R_32F``   ``MCBLAS_R_16BF``   ``MCBLAS_R_16BF``
\                  ``MCBLAS_R_16F``    ``MCBLAS_R_16F``
\                  ``MCBLAS_R_32F``    ``MCBLAS_R_32F``
``MCBLAS_R_64F``   ``MCBLAS_R_64F``    ``MCBLAS_R_64F``
``MCBLAS_C_32F``   ``MCBLAS_C_32F``    ``MCBLAS_R_32F``
\                  ``MCBLAS_C_32F``    ``MCBLAS_C_32F``
``MCBLAS_C_64F``   ``MCBLAS_C_64F``    ``MCBLAS_R_64F``
\                  ``MCBLAS_C_64F``    ``MCBLAS_C_64F``
================   =================   ===============

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+----------------------------------+
   | Error Value                        | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed          |
   |                                    | successfully                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   |                                    | the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                          |
   +------------------------------------+----------------------------------+

mcblasScalEx()
---------------

::

   mcblasStatus_t  mcblasScalEx(mcblasHandle_t handle,
                                int n,
                                const void *alpha,
                                mcblasDataType_t alphaType,
                                void *x,
                                mcblasDataType_t xType,
                                int incx,
                                mcblasDataType_t executionType);

This function scales the vector ``x`` by the scalar
:math:`\alpha`
and overwrites it with the result. Hence, the performed
operation is
:math:`\mathbf{x}\lbrack j\rbrack = \alpha \times \mathbf{x}\lbrack j\rbrack`
for :math:`i = 1,\ldots,n`
and
:math:`j = 1 + \left( {i - 1} \right)*\text{incx}`
. Notice that the last two equations reflect 1-based
indexing used for compatibility with Fortran.

.. table:: 
   :widths: grid

   +---------------+----------------+--------+--------------------+
   | Param.        | Memory         | In/out | Meaning            |
   +===============+================+========+====================+
   | handle        |                | input  | handle to the      |
   |               |                |        | mcBLAS library     |
   |               |                |        | context.           |
   +---------------+----------------+--------+--------------------+
   | alpha         | host or device | input  | <type> scalar used |
   |               |                |        | for                |
   |               |                |        | multiplication.    |
   +---------------+----------------+--------+--------------------+
   | n             |                | input  | number of elements |
   |               |                |        | in the vector      |
   |               |                |        | ``x``.             |
   +---------------+----------------+--------+--------------------+
   | x             | device         | in/out | <type> vector with |
   |               |                |        | ``n`` elements.    |
   +---------------+----------------+--------+--------------------+
   | xType         |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype of vector |
   |               |                |        | ``x``.             |
   +---------------+----------------+--------+--------------------+
   | incx          |                | input  | stride between     |
   |               |                |        | consecutive        |
   |               |                |        | elements of ``x``. |
   +---------------+----------------+--------+--------------------+
   | executionType |                | input  | enumerant          |
   |               |                |        | specifying the     |
   |               |                |        | datatype in which  |
   |               |                |        | the computation is |
   |               |                |        | executed.          |
   +---------------+----------------+--------+--------------------+

The datatypes combinations currently supported for
``mcblasScalEx`` are listed below :

================   ==============
x                  execution
================   ==============
``MCBLAS_R_16F``   ``MCBLAS_R_32F``
``MCBLAS_R_32F``   ``MCBLAS_R_32F``
``MCBLAS_R_64F``   ``MCBLAS_R_64F``
``MCBLAS_C_32F``   ``MCBLAS_C_32F``
``MCBLAS_C_64F``   ``MCBLAS_C_64F``
================   ==============

The possible error values returned by this function and
their meanings are listed below.

.. table:: 
   :widths: grid

   +------------------------------------+----------------------------------+
   | Error Value                        | Meaning                          |
   +====================================+==================================+
   | ``MCBLAS_STATUS_SUCCESS``          | the operation completed          |
   |                                    | successfully                     |
   +------------------------------------+----------------------------------+
   |                                    | the library was not initialized  |
   | ``MCBLAS_STATUS_NOT_INITIALIZED``  |                                  |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_NOT_SUPPORTED``    | the combination of the           |
   |                                    | parameters ``xType`` and         |
   |                                    | ``executionType`` is not         |
   |                                    | supported                        |
   +------------------------------------+----------------------------------+
   |                                    | the function failed to launch on |
   | ``MCBLAS_STATUS_EXECUTION_FAILED`` | the GPU                          |
   +------------------------------------+----------------------------------+
   | ``MCBLAS_STATUS_INVALID_VALUE``    | ``alphaType`` or ``xType`` or    |
   |                                    | ``executionType`` is not         |
   |                                    | supported                        |
   +------------------------------------+----------------------------------+
