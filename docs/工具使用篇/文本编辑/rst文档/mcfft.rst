The API reference guide for mcFFT, the MACA Fast Fourier
Transform library.

Introduction
.............

This document describes mcFFT, the MetaX® MACA™ Fast
Fourier Transform (FFT) product. The mcFFT library is 
designed to provide high performance on MetaX GPUs. 

The FFT is a divide-and-conquer algorithm for efficiently
computing discrete Fourier transforms of complex or
real-valued data sets. It is one of the most important and
widely used numerical algorithms in computational physics
and general signal processing. The mcFFT library provides a
simple interface for computing FFTs on an MetaX GPU, which
allows users to quickly leverage the floating-point power
and parallelism of the GPU in a highly optimized and tested
FFT library.

The mcFFT product supports a wide range of FFT inputs and
options efficiently on MetaX GPUs. This version of the
mcFFT library supports the following features:

-  Algorithms highly optimized for input sizes that can be
   written in the form
   :math:`2^{a} \times 3^{b} \times 5^{c} \times 7^{d}`
   . In general the smaller the prime factor, the better the
   performance, i.e., powers of two are fastest.
-  An
   :math:`O\left( n\log n \right)`
   algorithm for every input data size
-  Single-precision
   (32-bit floating point) and double-precision (64-bit
   floating point). Transforms of lower precision have
   higher performance.
-  Complex and real-valued input and output. Real valued
   input or output require less computations and data than
   complex values and often have faster time to solution.
   Types supported are:

   -  C2C - Complex input to complex output
   -  R2C - Real input to complex output
   -  C2R - Symmetric complex input to real output

-  1D, 2D and 3D transforms
-  Execution of multiple 1D, 2D and 3D transforms
   simultaneously. These batched transforms have higher
   performance than single transforms.
-  In-place and out-of-place transforms
-  Arbitrary intra- and inter-dimension element strides
   (strided layout)
-  Streamed execution, enabling asynchronous computation and
   data movement

Installing mcFFT
==================

.. math:: 
   MACA\begin{cases}
         library & \begin{cases}
                     mcFFT \\
                     \vdots
                     \end{cases} \\
         \vdots \\
         \vdots
         \end{cases}

mcFFT is a library released along with the MACA toolkit. The installation of the MACA toolkit refers to MACA Quick Start Guide.
After installation, make sure that the environment variable MACA_PATH is set. 

.. code-block:: shell

   export MACA_PATH=/your/maca/path

The mcFFT API related files are listed as follows. 

.. code-block:: 
   
   #header location:  
   ${MACA_PATH}/include/mcfft

   #lib location:     
   ${MACA_PATH}/lib/libmcfft.so
   ${MACA_PATH}/lib/libmcfft-device-0.so
   ${MACA_PATH}/lib/libmcfft-device-1.so
   ${MACA_PATH}/lib/libmcfft-device-2.so
   ${MACA_PATH}/lib/libmcfft-device-3.so

Please make sure that the environment variable ISU_FASTMODEL is set to 1 before compiling with mcFFT library.

.. code-block:: shell

   export ISU_FASTMODEL=1


Hello mcFFT
=============

For sample code references please see the example below.
They show an application written in C using the mcFFT library
API.

.. code-block:: cmake

   #CMakeLists.txt
   cmake_minimum_required(VERSION 3.16)
   project(mcfft_samples)
   if(NOT DEFINED ENV{MACA_PATH})
       message(FATAL_ERROR "not defined environment variable: MACA_PATH")
   endif()
   INCLUDE_DIRECTORIES($ENV{MACA_PATH}/include/)
   INCLUDE_DIRECTORIES($ENV{MACA_PATH}/include/mcfft/)
   INCLUDE_DIRECTORIES($ENV{MACA_PATH}/mcr/)
   LINK_DIRECTORIES($ENV{MACA_PATH}/lib)
   set(LINK_LIBS
       mc_runtime
       mcfft
       mcfft-device-0
       mcfft-device-1
       mcfft-device-2
       mcfft-device-3
       )
   set(sample_list complex_1d)

   foreach(sample ${sample_list})
     add_executable(mcfft_${sample} ${sample}.cpp)
     target_link_libraries(mcfft_${sample} ${LINK_LIBS})
   endforeach()

::

   //complex_1d.cpp, 1D, C2C, in-place
   //-----------------------------------------------------------
   #include <cassert>
   #include <complex>
   #include <iostream>
   #include <vector>
   #include <random>
   #include <mc_runtime.h>
   #include "mcfft.h"
   #define NX 8
   #define BATCH 1

   int main(int argc, char* argv[])
   {
      std::cout << "mcFFT complex 1d FFT example\n";
      mcfftHandle plan;
      mcError_t err;

      // Initialize data on the host:
      std::vector<std::complex<float>> data(NX*BATCH);
      std::vector<std::complex<float>> outData(NX*BATCH);
      std::cout << "Input:\n";
    
      for(int b = 0; b < BATCH; b++)
      {
         for(int n = 0; b < NX; n++)
         {
            std::mt19937 gen(n);
            const float x = (float)gen() / (float)gen.max();
            const float y = (float)gen() / (float)gen.max();
            const std::complex<float> val(x,y);
            data[NX*b + n] = val;
            std::cout<<data[NX*b + n]<<" ";
         }
      }

      // Create device object and plan:
      mcfftComplex *devPtrData=nullptr;
      err=mcMalloc((void**)&devPtrData, sizeof(mcfftComplex)*NX*BATCH);
      if (err != mcSuccess)
      {
        fprintf(stderr, "Error: Failed to allocate\n");
        return EXIT_FAILURE;
      }

      if (mcfftPlan1d(&plan, NX, MCFFT_C2C, BATCH) != mcSuccess)
      {
        fprintf(stderr, "mcFFT Error: Plan creation failed\n");
        return EXIT_FAILURE;
      }

      //copy data
      err = mcMemcpy(devPtrData, data.data(), sizeof(mcfftComplex)*NX*BATCH, mcMemcpyHostToDevice);
      if (err != mcSuccess)
      {
        fprintf(stderr, "Error: Failed to copy host to device\n");
        return EXIT_FAILURE;
      }

      // Execute the forward transform, in-place
      if (mcfftExecC2C(plan, devPtrData, devPtrData, MCFFT_FORWARD) != mcSuccess)
      {
        fprintf(stderr, "mcFFT error: ExecC2C Forward failed\n");
        return EXIT_FAILURE;
      }

      // Execute the inverse transform, in-place
      if (mcfftExecC2C(plan, devPtrData, devPtrData, MCFFT_INVERSE) != mcSuccess)
      {
        fprintf(stderr, "mcFFT error: ExecC2C Inverse failed\n");
        return EXIT_FAILURE;
      }

      /*
      *   Results may not be immediately available until all
      *   tasks have completed
      */

      if (mcDeviceSynchronize() != mcSuccess)
      {
        fprintf(stderr, "Error: Failed to synchronize\n");
        return EXIT_FAILURE;
      }

      err = mcMemcpy(outData.data(), devPtrData,  sizeof(mcfftComplex)*NX*BATCH, mcMemcpyDeviceToHost);
      if (err != mcSuccess)
      {
        fprintf(stderr, "Error: Failed to copy device to host\n");
        return EXIT_FAILURE;
      }

      const float overN = 1.0f / Nx;
      float       error = 0.0f;
      for(size_t i = 0; i < data.size(); i++)
      {
        float diff = std::max(std::abs(data[i].real() - outData[i].real() * overN),
                              std::abs(data[i].imag() - outData[i].imag() * overN));
        if(diff > error)
        {
            error = diff;
        }
      }

      std::cout << "Transformed back:\n";
      for(size_t i = 0; i < outData.size(); i++)
      {
        std::cout << outData[i]*overN << " ";
      }
      std::cout << std::endl;
      std::cout << "Maximum error: " << error << "\n";

      mcfftDestroy(plan);
      mcFree(devPtrData);
   }

Porting a CUFFT application
============================

Porting a CUDA application which originally calls the cuFFT API to an application calling mcFFT API should be easy.
The MACA toolkit provides a CUDA wrapper tool which can help you to achieve the porting task. 
Basically, you don't need to modify your source code. Using a cuFFT application for example:

::

   //complex_1d.cpp, 1D, C2C, in-place
   //-----------------------------------------------------------
   #include <cassert>
   #include <complex>
   #include <iostream>
   #include <vector>
   #include <random>
   #include <cuda_runtime.h>
   #include "cufft.h"
   #define NX 8
   #define BATCH 1

   int main(int argc, char* argv[])
   {
      std::cout << "cuFFT complex 1d FFT example\n";
      cufftHandle plan;
      cudaError_t err;

      // Initialize data on the host:
      std::vector<std::complex<float>> data(NX*BATCH);
      std::vector<std::complex<float>> outData(NX*BATCH);
      std::cout << "Input:\n";
    
      for(int b = 0; b < BATCH; b++)
      {
         for(int n = 0; b < NX; n++)
         {
            std::mt19937 gen(n);
            const float x = (float)gen() / (float)gen.max();
            const float y = (float)gen() / (float)gen.max();
            const std::complex<float> val(x,y);
            data[NX*b + n] = val;
            std::cout<<data[NX*b + n]<<" ";
         }
      }

      // Create device object and plan:
      cufftComplex *devPtrData=nullptr;
      err = cudaMalloc((void**)&devPtrData, sizeof(cufftComplex)*NX*BATCH);
      if (err != cudaSuccess)
      {
        fprintf(stderr, "Error: Failed to allocate\n");
        return EXIT_FAILURE;
      }

      if (cufftPlan1d(&plan, NX, CUFFT_C2C, BATCH) != CUFFT_SUCCESS)
      {
        fprintf(stderr, "CUFFT Error: Plan creation failed\n");
        return EXIT_FAILURE;
      }

      //copy data
      err = cudaMemcpy(devPtrData, data.data(), sizeof(cufftComplex)*NX*BATCH, cudaMemcpyHostToDevice);
      if (err != cudaSuccess)
      {
        fprintf(stderr, "Cuda error: Failed to copy host to device\n");
        return EXIT_FAILURE;
      }

      // Execute the forward transform, in-place
      if (cufftExecC2C(plan, devPtrData, devPtrData, CUFFT_FORWARD) != CUFFT_SUCCESS)
      {
        fprintf(stderr, "CUFFT error: ExecC2C Forward failed\n");
        return EXIT_FAILURE;
      }

      // Execute the inverse transform, in-place
      if (cufftExecC2C(plan, devPtrData, devPtrData, CUFFT_INVERSE) != CUFFT_SUCCESS)
      {
        fprintf(stderr, "CUFFT error: ExecC2C Inverse failed\n");
        return EXIT_FAILURE;
      }

      /*
      *   Results may not be immediately available until all
      *   tasks have completed
      */

      if (cudaDeviceSynchronize() != cudaSuccess)
      {
        fprintf(stderr, "Cuda error: Failed to synchronize\n");
        return EXIT_FAILURE;
      }

      err = cudaMemcpy(outData.data(), devPtrData,  sizeof(cufftComplex)*NX*BATCH, cudaMemcpyDeviceToHost);
      if (err != cudaSuccess)
      {
        fprintf(stderr, "Cuda error: Failed to copy device to host\n");
        return EXIT_FAILURE;
      }

      const float overN = 1.0f / Nx;
      float       error = 0.0f;
      for(size_t i = 0; i < data.size(); i++)
      {
        float diff = std::max(std::abs(data[i].real() - outData[i].real() * overN),
                              std::abs(data[i].imag() - outData[i].imag() * overN));
        if(diff > error)
        {
            error = diff;
        }
      }

      std::cout << "Transformed back:\n";
      for(size_t i = 0; i < outData.size(); i++)
      {
        std::cout << outData[i]*overN << " ";
      }
      std::cout << std::endl;
      std::cout << "Maximum error: " << error << "\n";

      cufftDestroy(plan);
      cudaFree(devPtrData);
   }

As the upper example is written to a file named complex_1d.cpp, you can compile it using cuFFT on Linux, against the dynamic library, the following command can be used:

::

   nvcc complex_1d.cpp -lcufft -o complex_1d

Now, if you want to porting this example from cuFFT to mcFFT, please set two environment variables.

::
   
   export MACA_PATH=<your maca toolkit dir>
   export CUDA_PATH=${MACA_PATH}/tools/wcuda

Then, using the original way to build your application

::

   nvcc complex_1d.cpp -lcufft -o complex_1d

Now, this complex_1d is a binary running using mcFFT.

using-the-mcfft-api
.............................

This chapter provides a general overview of the mcFFT
library API. Users are encouraged to read this chapter before continuing
with more detailed descriptions.

The Discrete Fourier transform (DFT) maps a complex-valued
vector :math:`x_{k}`
(time domain) into its frequency domain representation given
by:

:math:`X_{k} = \sum\limits_{n = 0}^{N - 1}x_{n}e^{-2\pi i\frac{kn}{N}}`

where : :math:`X_{k}`
is a complex-valued vector of the same size. This is known
as a forward DFT. If the sign on the exponent of e is
changed to be positive, the transform is an inverse
transform. Depending on :math:`N`, different algorithms
are deployed for the best performance.

The mcFFT API is modeled after
`FFTW <http://www.fftw.org/>`__, which is one of the most
popular and efficient CPU-based FFT libraries. mcFFT
provides a simple configuration mechanism called a plan that
uses internal building blocks to optimize the transform for
the given configuration and the particular GPU hardware
selected. Then, when the execution function is called, the
actual transform takes place following the plan of
execution. The advantage of this approach is that once the
user creates a plan, the library retains whatever state is
needed to execute the plan multiple times without
recalculation of the configuration. This model works well
for mcFFT because different kinds of FFTs require different
thread configurations and GPU resources, and the plan
interface provides a simple way of reusing configurations.

Fourier Transform Types
==================================

Apart from the general complex-to-complex (C2C)
transform, mcFFT implements efficiently two other types:
real-to-complex (R2C) and complex-to-real (C2R). In many
practical applications the input vector is real-valued.
It can be easily shown that in this case the output
satisfies Hermitian symmetry (
:math:`X_{k} = X_{N - k}^{\ast}`
, where the star denotes complex conjugation). The
converse is also true: for complex-Hermitian input the
inverse transform will be purely real-valued. mcFFT takes
advantage of this redundancy and works only on the first
half of the Hermitian vector.
Transform execution functions for single and
double-precision are defined separately as:

-  ``mcfftExecC2C() / mcfftExecZ2Z()`` -
   complex-to-complex transforms for single/double
   precision.
-  ``mcfftExecR2C() / mcfftExecD2Z()`` - real-to-complex
   forward transform for single/double precision.
-  ``mcfftExecC2R() / mcfftExecZ2D()`` - complex-to-real
   inverse transform for single/double precision.

Each of those functions demands different input data
layout.

.. container:: tablenoborder

   +-----------------------------------------------------------------------+
   | **Note:** Complex-to-real (C2R) transforms accept complex-Hermitian   |
   | input, which requires the 0th element (and the                        |
   | :math:`\frac{N}{2}`                                                   |
   | th input if N is even) to be real-valued, i.e. its imaginary part     |
   | should be zero. Otherwise, the behavior of the transform is           |
   | undefined.                                                            |
   +-----------------------------------------------------------------------+

Data Layout
==============

In the mcFFT Library, data layout depends strictly on the
configuration and the transform type. In the case of
general complex-to-complex transform both the input and
output data shall be a
``mcfftComplex``/``mcfftDoubleComplex`` array in single-
and double-precision modes respectively. In C2R mode an
input array
:math:`(x_{1},x_{2},\ldots,x_{\lfloor\frac{N}{2}\rfloor + 1})`
of only non-redundant complex elements is required. The
output array
:math:`(X_{1},X_{2},\ldots,X_{N})`
consists of ``mcfftReal``/``mcfftDoubleReal`` elements in
this mode. Finally, R2C demands an input array
:math:`(X_{1},X_{2},\ldots,X_{N})`
of real values and returns an array
:math:`(x_{1},x_{2},\ldots,x_{\lfloor\frac{N}{2}\rfloor + 1})`
of non-redundant complex elements.
In real-to-complex and complex-to-real transforms the
size of input data and the size of output data differ.
For out-of-place transforms a separate array of
appropriate size is created. For in-place transforms the
user should use ``padded`` data layout. This layout is
FFTW compatibile.

In the ``padded`` layout output signals begin at the same
memory addresses as the input data. Therefore input data
for real-to-complex and output data for complex-to-real
must be padded.

Expected sizes of input/output data for 1-d transforms
are summarized in the table below:

.. container:: tablenoborder

   +-----------------------+---------------------------------------------------------+-------------------------------------------------------+
   | FFT type              | input data size                                         | output data size                                      |
   +=======================+=========================================================+=======================================================+
   | C2C                   |                                                         |                                                       |
   |                       | :math:`x` ``mcfftComplex``                              | :math:`x`  ``mcfftComplex``                           |
   +-----------------------+---------------------------------------------------------+-------------------------------------------------------+
   | C2R                   |                                                         |                                                       |
   |                       | :math:`\lfloor\frac{x}{2}\rfloor + 1`  ``mcfftComplex`` | :math:`x`  ``mcfftReal``                              |
   +-----------------------+---------------------------------------------------------+-------------------------------------------------------+
   | R2C*                  |                                                         |                                                       |
   |                       | :math:`x` ``mcfftReal``                                 |:math:`\lfloor\frac{x}{2}\rfloor + 1` ``mcfftComplex`` |
   +-----------------------+---------------------------------------------------------+-------------------------------------------------------+

The real-to-complex transform is implicitly a forward
transform. For an in-place real-to-complex transform
where FFTW compatible output is desired, the input size
must be padded to
:math:`\left( {\lfloor\frac{N}{2}\rfloor + 1} \right)`
complex elements. For out-of-place transforms, input and
output sizes match the logical transform size
:math:`N`
and the non-redundant size
:math:`\lfloor\frac{N}{2}\rfloor + 1`
, respectively.
The complex-to-real transform is implicitly inverse. For
in-place complex-to-real FFTs where FFTW compatible
output is selected (default padding mode), the input size
is assumed to be
:math:`\lfloor\frac{N}{2}\rfloor + 1`
``mcfftComplex`` elements. Note that in-place
complex-to-real FFTs may **overwrite** arbitrary
imaginary input point values when non-unit input and
output strides are chosen. Out-of-place complex-to-real
FFT will always **overwrite** input buffer. For
out-of-place transforms, input and output sizes match the
logical transform non-redundant size
:math:`\lfloor\frac{N}{2}\rfloor + 1`
and size :math:`N`
, respectively.

Multidimensional Transforms
=====================================

Multidimensional DFT map a :math:`d`
-dimensional array
:math:`x_{\mathbf{n}}`
, where
:math:`\mathbf{n} = (n_{1},n_{2},\ldots,n_{d})`
into its frequency domain array given by:

:math:`X_{\mathbf{k}} = \sum\limits_{n = 0}^{N - 1}x_{\mathbf{n}}e^{-2\pi i\frac{\mathbf{k}\mathbf{n}}{\mathbf{N}}}`

where
:math:`\frac{\mathbf{n}}{\mathbf{N}} = (\frac{n_{1}}{N_{1}},\frac{n_{2}}{N_{2}},\ldots,\frac{n_{d}}{N_{d}})`
, and the summation denotes the set of nested summations

:math:`\sum\limits_{n_{1} = 0}^{N_{1} - 1}\sum\limits_{n_{2} = 0}^{N_{2} - 1}\ldots\sum\limits_{n_{d} = 0}^{N_{d} - 1}`

mcFFT supports one-dimensional, two-dimensional and
three-dimensional transforms, which can all be called by
the same ``mcfftExec*`` functions.

Similar to the one-dimensional case, the frequency domain
representation of real-valued input data satisfies
Hermitian symmetry, defined as:
:math:`x_{(n_{1},n_{2},\ldots,n_{d})} = x_{(N_{1} - n_{1},N_{2} - n_{2},\ldots,N_{d} - n_{d})}^{\ast}`
.
C2R and R2C algorithms take advantage of this fact by
operating only on half of the elements of signal array,
namely on: :math:`x_{\mathbf{n}}`
for
:math:`\mathbf{n} \in \{ 1,\ldots,N_{1}\} \times \ldots \times \{ 1,\ldots,N_{d - 1}\} \times \{ 1,\ldots,\lfloor\frac{N_{d}}{2}\rfloor + 1\}`
.
The general rules of data alignment described in ``Data Layout``
apply to higher-dimensional transforms. The following
table summarizes input and output data sizes for
multidimensional DFTs:

.. container:: tablenoborder

   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | Dims            | FFT type        | Input data size                                                                  | Output data size                                                                |
   +=================+=================+==================================================================================+=================================================================================+
   | 1D              | C2C             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}`  ``mcfftComplex``                                         | :math:`\mathbf{N}_{1}` ``mcfftComplex``                                         |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 1D              | C2R             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\lfloor\frac{\mathbf{N}_{1}}{2}\rfloor + 1` ``mcfftComplex``              | :math:`\mathbf{N}_{1}`  ``mcfftReal``                                           |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 1D              | R2C             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}` ``mcfftReal``                                             | :math:`\lfloor\frac{\mathbf{N}_{1}}{2}\rfloor + 1` ``mcfftComplex``             |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 2D              | C2C             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}\mathbf{N}_{2}` ``mcfftComplex``                            | :math:`\mathbf{N}_{1}\mathbf{N}_{2}`  ``mcfftComplex``                          |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 2D              | C2R             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}(\lfloor\frac{\mathbf{N}_{2}}{2}\rfloor + 1)`               | :math:`\mathbf{N}_{1}\mathbf{N}_{2}`  ``mcfftReal``                             |
   |                 |                 | ``mcfftComplex``                                                                 |                                                                                 |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 2D              | R2C             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}\mathbf{N}_{2}` ``mcfftReal``                               | :math:`\mathbf{N}_{1}(\lfloor\frac{\mathbf{N}_{2}}{2}\rfloor + 1)`              |
   |                 |                 |                                                                                  | ``mcfftCompplex``                                                               |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 3D              | C2C             |                                                                                  |                                                                                 |
   |                 |                 |:math:`\mathbf{N}_{1}\mathbf{N}_{2}\mathbf{N}_{3}` ``mcfftComplex``               | :math:`\mathbf{N}_{1}\mathbf{N}_{2}\mathbf{N}_{3}` ``mcfftComplex``             |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 3D              | C2R             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}\mathbf{N}_{2}(\lfloor\frac{\mathbf{N}_{3}}{2}\rfloor + 1)` | :math:`\mathbf{N}_{1}\mathbf{N}_{2}\mathbf{N}_{3}`  ``mcfftReal``               |
   |                 |                 | ``mcfftComplex``                                                                 |                                                                                 |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
   | 3D              | R2C             |                                                                                  |                                                                                 |
   |                 |                 | :math:`\mathbf{N}_{1}\mathbf{N}_{2}\mathbf{N}_{3}`                               | :math:`\mathbf{N}_{1}\mathbf{N}_{2}(\lfloor\frac{\mathbf{N}_{3}}{2}\rfloor + 1)`|
   |                 |                 | ``mcfftReal``                                                                    | ``mcfftComplex``                                                                |
   +-----------------+-----------------+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

For example, static declaration of a three-dimensional
array for the output of an out-of-place real-to-complex
transform will look like this:

::

   mcfftComplex odata[N1][N2][N3/2+1];

mcFFT API Reference
.....................

This chapter specifies the behavior of the mcFFT library
functions by describing their input/output parameters, data
types, and error codes. The mcFFT library is initialized
upon the first invocation of an API function, and mcFFT
shuts down automatically when all user-created FFT plans are
destroyed.

Return value mcfftResult
===========================

All mcFFT Library return values except for
``MCFFT_SUCCESS`` indicate that the current API call
failed and the user should reconfigure to correct the
problem. The possible return values are defined as
follows:

::

   typedef enum mcfftResult_t {
         MCFFT_SUCCESS        = 0,  //  The mcFFT operation was successful
         MCFFT_INVALID_PLAN   = 1,  //  mcFFT was passed an invalid plan handle
         MCFFT_ALLOC_FAILED   = 2,  //  mcFFT failed to allocate GPU or CPU memory
         MCFFT_INVALID_TYPE   = 3,  //  No longer used
         MCFFT_INVALID_VALUE  = 4,  //  User specified an invalid pointer or parameter
         MCFFT_INTERNAL_ERROR = 5,  //  Driver or internal mcFFT library error
         MCFFT_EXEC_FAILED    = 6,  //  Failed to execute an FFT on the GPU
         MCFFT_SETUP_FAILED   = 7,  //  The mcFFT library failed to initialize
         MCFFT_INVALID_SIZE   = 8,  //  User specified an invalid transform size
         MCFFT_UNALIGNED_DATA = 9,  //  No longer used
         MCFFT_INCOMPLETE_PARAMETER_LIST = 10, //  Missing parameters in call
         MCFFT_INVALID_DEVICE = 11, //  Execution of a plan was on different GPU than plan creation
         MCFFT_PARSE_ERROR    = 12, //  Internal plan database error 
         MCFFT_NO_WORKSPACE   = 13  //  No workspace has been provided prior to plan execution
         MCFFT_NOT_IMPLEMENTED = 14, // Function does not implement functionality for parameters given.
         MCFFT_LICENSE_ERROR  = 15, // Used in previous versions.
         MCFFT_NOT_SUPPORTED  = 16  // Operation is not supported for parameters given.
   } mcfftResult;

Users are encouraged to check return values from mcFFT
functions for errors.

mcFFT Basic Plans
=====================

Function mcfftPlan1d()
------------------------

::

   mcfftResult 
         mcfftPlan1d(mcfftHandle *plan, int nx, mcfftType type, int batch);

Creates a 1D FFT plan configuration for a specified
signal size and data type. The ``batch`` input
parameter tells mcFFT how many 1D transforms to
configure.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +-----------+---------------------------------------------------------+
   | ``plan``  | Pointer to a ``mcfftHandle`` object                     |
   +-----------+---------------------------------------------------------+
   | ``nx``    | The transform size (e.g. 256 for a 256-point FFT)       |
   +-----------+---------------------------------------------------------+
   | ``type``  | The transform data type (e.g., ``MCFFT_C2C`` for single |
   |           | precision complex to complex)                           |
   +-----------+---------------------------------------------------------+
   | ``batch`` | Number of transforms of size ``nx``. Please consider    |
   |           | using ``mcfftPlanMany`` for multiple transforms.        |
   +-----------+---------------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ======== =====================================
   ``plan`` Contains a mcFFT 1D plan handle value
   ======== =====================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | The ``nx`` or ``batch`` parameter is not |
   |                          | a supported size.                        |
   +--------------------------+------------------------------------------+

Function mcfftPlan2d()
------------------------

::

   mcfftResult 
         mcfftPlan2d(mcfftHandle *plan, int nx, int ny, mcfftType type);

Creates a 2D FFT plan configuration according to
specified signal sizes and data type.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +----------+----------------------------------------------------------+
   | ``plan`` | Pointer to a ``mcfftHandle`` object                      |
   +----------+----------------------------------------------------------+
   | ``nx``   | The transform size in the x dimension This is slowest    |
   |          | changing dimension of a transform (strided in memory).   |
   +----------+----------------------------------------------------------+
   | ``ny``   | The transform size in the y dimension. This is fastest   |
   |          | changing dimension of a transform (contiguous in         |
   |          | memory).                                                 |
   +----------+----------------------------------------------------------+
   | ``type`` | The transform data type (e.g., ``MCFFT_C2R`` for single  |
   |          | precision complex to real)                               |
   +----------+----------------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ======== =====================================
   ``plan`` Contains a mcFFT 2D plan handle value
   ======== =====================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | Either or both of the ``nx`` or ``ny``   |
   |                          | parameters is not a supported size.      |
   +--------------------------+------------------------------------------+

Function mcfftPlan3d()
-----------------------

::

   mcfftResult 
         mcfftPlan3d(mcfftHandle *plan, int nx, int ny, int nz, mcfftType type);

Creates a 3D FFT plan configuration according to
specified signal sizes and data type. This function is
the same as ``mcfftPlan2d()`` except that it takes a
third size parameter ``nz``.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +----------+----------------------------------------------------------+
   | ``plan`` | Pointer to a ``mcfftHandle`` object                      |
   +----------+----------------------------------------------------------+
   | ``nx``   | The transform size in the x dimension. This is slowest   |
   |          | changing dimension of a transform (strided in memory).   |
   +----------+----------------------------------------------------------+
   | ``ny``   | The transform size in the y dimension                    |
   +----------+----------------------------------------------------------+
   | ``nz``   | The transform size in the z dimension. This is fastest   |
   |          | changing dimension of a transform (contiguous in         |
   |          | memory).                                                 |
   +----------+----------------------------------------------------------+
   | ``type`` | The transform data type (e.g., ``MCFFT_R2C`` for single  |
   |          | precision real to complex)                               |
   +----------+----------------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ======== =====================================
   ``plan`` Contains a mcFFT 3D plan handle value
   ======== =====================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the ``nx``, ``ny``, or    |
   |                          | ``nz`` parameters is not a supported     |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftPlanMany()
---------------------------

::

   mcfftResult 
         mcfftPlanMany(mcfftHandle *plan, int rank, int *n, int *inembed,
            int istride, int idist, int *onembed, int ostride,
            int odist, mcfftType type, int batch);

Creates a FFT plan configuration of dimension
``rank``, with sizes specified in the array ``n``. The
``batch`` input parameter tells mcFFT how many
transforms to configure. With this function, batched
plans of 1, 2, or 3 dimensions may be created.

The ``mcfftPlanMany()`` API supports more complicated
input and output data layouts via the advanced data
layout parameters: ``inembed``, ``istride``,
``idist``, ``onembed``, ``ostride``, and ``odist``.

If ``inembed`` and ``onembed`` are set to ``NULL``,
all other stride information is ignored, and default
strides are used. The default assumes contiguous data
arrays.

All arrays are assumed to be in CPU memory.

Please note that behavior of ``mcfftPlanMany``
function when ``inembed`` and ``onembed`` is ``NULL``
is different than corresponding function in FFTW
library ``fftw_plan_many_dft``.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +-------------+-------------------------------------------------------+
   | ``plan``    | Pointer to a ``mcfftHandle`` object.                  |
   +-------------+-------------------------------------------------------+
   | ``rank``    | Dimensionality of the transform (1, 2, or 3).         |
   +-------------+-------------------------------------------------------+
   | ``n``       | Array of size ``rank``, describing the size of each   |
   |             | dimension, ``n[0]`` being the size of the outermost   |
   |             | and ``n[rank-1]`` innermost (contiguous) dimension of |
   |             | a transform.                                          |
   +-------------+-------------------------------------------------------+
   | ``inembed`` | Pointer of size ``rank`` that indicates the storage   |
   |             | dimensions of the input data in memory. If set to     |
   |             | NULL all other advanced data layout parameters are    |
   |             | ignored.                                              |
   +-------------+-------------------------------------------------------+
   | ``istride`` | Indicates the distance between two successive input   |
   |             | elements in the least significant (i.e., innermost)   |
   |             | dimension.                                            |
   +-------------+-------------------------------------------------------+
   | ``idist``   | Indicates the distance between the first element of   |
   |             | two consecutive signals in a batch of the input data. |
   +-------------+-------------------------------------------------------+
   | ``onembed`` | Pointer of size ``rank`` that indicates the storage   |
   |             | dimensions of the output data in memory. If set to    |
   |             | NULL all other advanced data layout parameters are    |
   |             | ignored.                                              |
   +-------------+-------------------------------------------------------+
   | ``ostride`` | Indicates the distance between two successive output  |
   |             | elements in the output array in the least significant |
   |             | (i.e., innermost) dimension.                          |
   +-------------+-------------------------------------------------------+
   | ``odist``   | Indicates the distance between the first element of   |
   |             | two consecutive signals in a batch of the output      |
   |             | data.                                                 |
   +-------------+-------------------------------------------------------+
   | ``type``    | The transform data type (e.g., ``MCFFT_R2C`` for      |
   |             | single precision real to complex).                    |
   +-------------+-------------------------------------------------------+
   | ``batch``   | Batch size for this transform.                        |
   +-------------+-------------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ======== =============================
   ``plan`` Contains a mcFFT plan handle.
   ======== =============================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

mcFFT Extensible Plans
=======================

This API separates handle creation from plan generation.
This makes it possible to change plan settings, which may
alter the outcome of the plan generation phase, before
the plan is actually generated.

Function mcfftCreate()
------------------------

::

   mcfftResult 
         mcfftCreate(mcfftHandle *plan);

Creates only an opaque handle, and allocates small
data structures on the host. The ``mcfftMakePlan*()``
calls actually do the plan generation.

.. container:: tablenoborder

   **Input**

   ======== ====================================
   ``plan`` Pointer to a ``mcfftHandle`` object.
   ======== ====================================

.. container:: tablenoborder

   **Output**

   ======== ===================================
   ``plan`` Contains a mcFFT plan handle value.
   ======== ===================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of resources for the plan |
   |                          | failed.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+

Function mcfftMakePlan1d()
----------------------------

::

   mcfftResult 
         mcfftMakePlan1d(mcfftHandle plan, int nx, mcfftType type, int batch, 
            size_t *workSize);

Following a call to ``mcfftCreate()`` makes a 1D FFT
plan configuration for a specified signal size and
data type. The ``batch`` input parameter tells mcFFT
how many 1D transforms to configure.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size (e.g. 256 for a 256-point FFT).  |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2C`` for    |
   |               | single precision complex to complex).               |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Number of transforms of size ``nx``. Please         |
   |               | consider using ``mcfftMakePlanMany`` for multiple   |
   |               | transforms.                                         |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =========================================
   ``*workSize`` Pointer to the size(s) of the work areas.
   ============= =========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked or multi-GPU restrictions |
   |                          | are not met.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | The ``nx`` or ``batch`` parameter is not |
   |                          | a supported size.                        |
   +--------------------------+------------------------------------------+

Function mcfftMakePlan2d()
----------------------------

::

   mcfftResult 
         mcfftMakePlan2d(mcfftHandle plan, int nx, int ny, mcfftType type, 
            size_t *workSize);

Following a call to ``mcfftCreate()`` makes a 2D FFT
plan configuration according to specified signal sizes
and data type.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension. This is      |
   |               | slowest changing dimension of a transform (strided  |
   |               | in memory).                                         |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension. This is      |
   |               | fastest changing dimension of a transform           |
   |               | (contiguous in memory).                             |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2R`` for    |
   |               | single precision complex to real).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =========================================
   ``*workSize`` Pointer to the size(s) of the work areas.
   ============= =========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | Either or both of the ``nx`` or ``ny``   |
   |                          | parameters is not a supported size.      |
   +--------------------------+------------------------------------------+

Function mcfftMakePlan3d()
-----------------------------

::

   mcfftResult 
         mcfftMakePlan3d(mcfftHandle plan, int nx, int ny, int nz, mcfftType type,
            size_t *workSize);

Following a call to ``mcfftCreate()`` makes a 3D FFT
plan configuration according to specified signal sizes
and data type. This function is the same as
``mcfftPlan2d()`` except that it takes a third size
parameter ``nz``.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension. This is      |
   |               | slowest changing dimension of a transform (strided  |
   |               | in memory).                                         |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension.              |
   +---------------+-----------------------------------------------------+
   | ``nz``        | The transform size in the z dimension. This is      |
   |               | fastest changing dimension of a transform           |
   |               | (contiguous in memory).                             |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ===========================================
   ``*workSize`` Pointer to the size(s) of the work area(s).
   ============= ===========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the ``nx``, ``ny``, or    |
   |                          | ``nz`` parameters is not a supported     |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftMakePlanMany()
-------------------------------

::

   mcfftResult 
         mcfftMakePlanMany(mcfftHandle plan, int rank, int *n, int *inembed,
            int istride, int idist, int *onembed, int ostride,
            int odist, mcfftType type, int batch, size_t *workSize);

Following a call to ``mcfftCreate()`` makes a FFT plan
configuration of dimension ``rank``, with sizes
specified in the array ``n``. The ``batch`` input
parameter tells mcFFT how many transforms to
configure. With this function, batched plans of 1, 2,
or 3 dimensions may be created.

The ``mcfftPlanMany()`` API supports more complicated
input and output data layouts via the advanced data
layout parameters: ``inembed``, ``istride``,
``idist``, ``onembed``, ``ostride``, and ``odist``.

If ``inembed`` and ``onembed`` are set to ``NULL``,
all other stride information is ignored, and default
strides are used. The default assumes contiguous data
arrays.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

All arrays are assumed to be in CPU memory.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``rank``      | Dimensionality of the transform (1, 2, or 3).       |
   +---------------+-----------------------------------------------------+
   | ``n``         | Array of size ``rank``, describing the size of each |
   |               | dimension, ``n[0]`` being the size of the outermost |
   |               | and ``n[rank-1]`` innermost (contiguous) dimension  |
   |               | of a transform.                                     |
   +---------------+-----------------------------------------------------+
   | ``inembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the input data in memory,             |
   |               | ``inembed[0]`` being the storage dimension of the   |
   |               | outermost dimension. If set to NULL all other       |
   |               | advanced data layout parameters are ignored.        |
   +---------------+-----------------------------------------------------+
   | ``istride``   | Indicates the distance between two successive input |
   |               | elements in the least significant (i.e., innermost) |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``idist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the input     |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``onembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the output data in memory,            |
   |               | ``inembed[0]`` being the storage dimension of the   |
   |               | outermost dimension. If set to NULL all other       |
   |               | advanced data layout parameters are ignored.        |
   +---------------+-----------------------------------------------------+
   | ``ostride``   | Indicates the distance between two successive       |
   |               | output elements in the output array in the least    |
   |               | significant (i.e., innermost) dimension.            |
   +---------------+-----------------------------------------------------+
   | ``odist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the output    |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Batch size for this transform.                      |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =========================================
   ``*workSize`` Pointer to the size(s) of the work areas.
   ============= =========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked or multi-GPU restrictions |
   |                          | are not met.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

Function mcfftMakePlanMany64()
--------------------------------

::

   mcfftResult 
         mcfftMakePlanMany64(mcfftHandle plan, int rank, 
            long long int *n, 
            long long int *inembed, long long int istride, long long int idist, 
            long long int *onembed, long long int ostride, long long int odist, 
            mcfftType type, 
            long long int batch, size_t *workSize);

Following a call to ``mcfftCreate()`` makes a FFT plan
configuration of dimension ``rank``, with sizes
specified in the array ``n``. The ``batch`` input
parameter tells mcFFT how many transforms to
configure. With this function, batched plans of 1, 2,
or 3 dimensions may be created.

This API is identical to ``mcfftMakePlanMany`` except
that the arguments specifying sizes and strides are 64
bit integers. This API makes very large transforms
possible. mcFFT includes kernels that use 32 bit
indexes, and kernels that use 64 bit indexes. mcFFT
planning selects 32 bit kernels whenever possible to
avoid any overhead due to 64 bit arithmetic.

All sizes and types of transform are supported by this
interface, with two exceptions. For transforms whose
size exceeds 4G elements, the dimensions specified in
the array ``n`` must be factorable into primes that
are less than or equal to 17. For real to complex and
complex to real transforms whose size exceeds 4G
elements, the fastest changing dimension must be even.

The ``mcfftPlanMany64()`` API supports more
complicated input and output data layouts via the
advanced data layout parameters: ``inembed``,
``istride``, ``idist``, ``onembed``, ``ostride``, and
``odist``.

If ``inembed`` and ``onembed`` are set to ``NULL``,
all other stride information is ignored, and default
strides are used. The default assumes contiguous data
arrays.

This call can only be used once for a given handle. It
will fail and return ``MCFFT_INVALID_PLAN`` if the
plan is locked, i.e. the handle was previously used
with a different ``mcfftPlan`` or ``mcfftMakePlan``
call.

All arrays are assumed to be in CPU memory.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``rank``      | Dimensionality of the transform (1, 2, or 3).       |
   +---------------+-----------------------------------------------------+
   | ``n``         | Array of size ``rank``, describing the size of each |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``inembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the input data in memory. If set to   |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``istride``   | Indicates the distance between two successive input |
   |               | elements in the least significant (i.e., innermost) |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``idist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the input     |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``onembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the output data in memory. If set to  |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``ostride``   | Indicates the distance between two successive       |
   |               | output elements in the output array in the least    |
   |               | significant (i.e., innermost) dimension.            |
   +---------------+-----------------------------------------------------+
   | ``odist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the output    |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Batch size for this transform.                      |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =========================================
   ``*workSize`` Pointer to the size(s) of the work areas.
   ============= =========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully created the FFT plan. |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle. Handle is not valid when the     |
   |                          | plan is locked or multi-GPU restrictions |
   |                          | are not met.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

mcFFT Estimated Size of Work Area
===================================

During plan execution, mcFFT requires a work area for
temporary storage of intermediate results. The
``mcfftEstimate*()`` calls return an estimate for the
size of the work area required, given the specified
parameters, and assuming default plan settings. Some
problem sizes require much more storage than others. In
particular powers of 2 are very efficient in terms of
temporary storage. Large prime numbers, however, use
different algorithms and may need up to the eight times
that of a similarly sized power of 2. These routines
return estimated ``workSize`` values which may still be
smaller than the actual values needed especially for
values of ``n`` that are not multiples of powers of 2, 3,
5 and 7. More refined values are given by the
``mcfftGetSize*()`` routines, but these values may still
be conservative.

Function mcfftEstimate1d()
----------------------------

::

   mcfftResult 
         mcfftEstimate1d(int nx, mcfftType type, int batch, size_t *workSize);

During plan execution, mcFFT requires a work area for
temporary storage of intermediate results. This call
returns an estimate for the size of the work area
required, given the specified parameters, and assuming
default plan settings.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size (e.g. 256 for a 256-point FFT).  |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2C`` for    |
   |               | single precision complex to complex).               |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Number of transforms of size ``nx``. Please         |
   |               | consider using ``mcfftEstimateMany`` for multiple   |
   |               | transforms.                                         |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size, in bytes, of the work space.   |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | The ``nx`` parameter is not a supported  |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftEstimate2d() 
----------------------------

::

   mcfftResult 
         mcfftEstimate2d(int nx, int ny, mcfftType type, size_t *workSize);

During plan execution, mcFFT requires a work area for
temporary storage of intermediate results. This call
returns an estimate for the size of the work area
required, given the specified parameters, and assuming
default plan settings.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension (number of    |
   |               | rows).                                              |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension (number of    |
   |               | columns).                                           |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2R`` for    |
   |               | single precision complex to real).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size, in bytes, of the work space.   |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =======================================
   ``*workSize`` Pointer to the size, of the work space.
   ============= =======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | Either or both of the ``nx`` or ``ny``   |
   |                          | parameters is not a supported size.      |
   +--------------------------+------------------------------------------+

Function mcfftEstimate3d()
-----------------------------

::

   mcfftResult 
         mcfftEstimate3d(int nx, int ny, int nz, mcfftType type, size_t *workSize);

During plan execution, mcFFT requires a work area for
temporary storage of intermediate results. This call
returns an estimate for the size of the work area
required, given the specified parameters, and assuming
default plan settings.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension.              |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension.              |
   +---------------+-----------------------------------------------------+
   | ``nz``        | The transform size in the z dimension.              |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size, in bytes, of the work space.   |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the ``nx``, ``ny``, or    |
   |                          | ``nz`` parameters is not a supported     |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftEstimateMany()
-------------------------------

::

   mcfftResult 
         mcfftEstimateMany(int rank, int *n, int *inembed,
            int istride, int idist, int *onembed, int ostride,
            int odist, mcfftType type, int batch, size_t *workSize);

During plan execution, mcFFT requires a work area for
temporary storage of intermediate results. This call
returns an estimate for the size of the work area
required, given the specified parameters, and assuming
default plan settings.

The ``mcfftEstimateMany()`` API supports more
complicated input and output data layouts via the
advanced data layout parameters: ``inembed``,
``istride``, ``idist``, ``onembed``, ``ostride``, and
``odist``.

All arrays are assumed to be in CPU memory.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``rank``      | Dimensionality of the transform (1, 2, or 3).       |
   +---------------+-----------------------------------------------------+
   | ``n``         | Array of size ``rank``, describing the size of each |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``inembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the input data in memory. If set to   |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``istride``   | Indicates the distance between two successive input |
   |               | elements in the least significant (i.e., innermost) |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``idist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the input     |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``onembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the output data in memory. If set to  |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``ostride``   | Indicates the distance between two successive       |
   |               | output elements in the output array in the least    |
   |               | significant (i.e., innermost) dimension.            |
   +---------------+-----------------------------------------------------+
   | ``odist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the output    |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Batch size for this transform.                      |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size, in bytes, of the work space.   |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

mcFFT Refined Estimated Size of Work Area
=============================================

The ``mcfftGetSize*()`` routines give a more accurate
estimate of the work area size required for a plan than
the ``mcfftEstimate*()`` routines as they take into
account any plan settings that may have been made. As
discussed in the section ``mcFFT Estimated Size of Work Area``,
the ``workSize`` value(s) returned may be conservative
especially for values of ``n`` that are not multiples of
powers of 2, 3, 5 and 7.

Function mcfftGetSize1d()
---------------------------

::

   mcfftResult 
         mcfftGetSize1d(mcfftHandle plan, int nx, mcfftType type, int batch, 
            size_t *workSize);

This call gives a more accurate estimate of the work
area size required for a plan than
``mcfftEstimate1d()``, given the specified parameters,
and taking into account any plan settings that may
have been made.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size (e.g. 256 for a 256-point FFT).  |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2C`` for    |
   |               | single precision complex to complex).               |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Number of transforms of size ``nx``. Please         |
   |               | consider using ``mcfftGetSizeMany`` for multiple    |
   |               | transforms.                                         |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | The ``nx`` parameter is not a supported  |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftGetSize2d()
------------------------------

::

   mcfftResult 
         mcfftGetSize2d(mcfftHandle plan, int nx, int ny, mcfftType type, 
            size_t *workSize);

This call gives a more accurate estimate of the work
area size required for a plan than
``mcfftEstimate2d()``, given the specified parameters,
and taking into account any plan settings that may
have been made.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension (number of    |
   |               | rows).                                              |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension (number of    |
   |               | columns).                                           |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_C2R`` for    |
   |               | single precision complex to real).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | Either or both of the ``nx`` or ``ny``   |
   |                          | parameters is not a supported size.      |
   +--------------------------+------------------------------------------+

Function mcfftGetSize3d()
------------------------------

::

   mcfftResult 
         mcfftGetSize3d(mcfftHandle plan, int nx, int ny, int nz, mcfftType type,
            size_t *workSize);

This call gives a more accurate estimate of the work
area size required for a plan than
``mcfftEstimate3d()``, given the specified parameters,
and taking into account any plan settings that may
have been made.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``nx``        | The transform size in the x dimension.              |
   +---------------+-----------------------------------------------------+
   | ``ny``        | The transform size in the y dimension.              |
   +---------------+-----------------------------------------------------+
   | ``nz``        | The transform size in the z dimension.              |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the ``nx``, ``ny``, or    |
   |                          | ``nz`` parameters is not a supported     |
   |                          | size.                                    |
   +--------------------------+------------------------------------------+

Function mcfftGetSizeMany()
------------------------------

::

   mcfftResult 
         mcfftGetSizeMany(mcfftHandle plan, int rank, int *n, int *inembed,
            int istride, int idist, int *onembed, int ostride,
            int odist, mcfftType type, int batch, size_t *workSize);

This call gives a more accurate estimate of the work
area size required for a plan than
``mcfftEstimateSizeMany()``, given the specified
parameters, and taking into account any plan settings
that may have been made.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``rank``      | Dimensionality of the transform (1, 2, or 3).       |
   +---------------+-----------------------------------------------------+
   | ``n``         | Array of size ``rank``, describing the size of each |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``inembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the input data in memory. If set to   |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``istride``   | Indicates the distance between two successive input |
   |               | elements in the least significant (i.e., innermost) |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``idist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the input     |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``onembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the output data in memory. If set to  |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``ostride``   | Indicates the distance between two successive       |
   |               | output elements in the output array in the least    |
   |               | significant (i.e., innermost) dimension.            |
   +---------------+-----------------------------------------------------+
   | ``odist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the output    |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Batch size for this transform.                      |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =====================================
   ``*workSize`` Pointer to the size of the work area.
   ============= =====================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

Function mcfftGetSizeMany64()
---------------------------------

::

   mcfftResult 
         mcfftGetSizeMany64(mcfftHandle plan, int rank, 
            long long int *n, 
            long long int *inembed, long long int istride, long long int idist, 
            long long int *onembed, long long int ostride, long long int odist, 
            mcfftType type, 
            long long int batch, size_t *workSize);

This call gives a more accurate estimate of the work
area size required for a plan than
``mcfftEstimateSizeMany()``, given the specified
parameters, and taking into account any plan settings
that may have been made.

This API is identical to ``mcfftMakePlanMany`` except
that the arguments specifying sizes and strides are 64
bit integers. This API makes very large transforms
possible. mcFFT includes kernels that use 32 bit
indexes, and kernels that use 64 bit indexes. mcFFT
planning selects 32 bit kernels whenever possible to
avoid any overhead due to 64 bit arithmetic.

All sizes and types of transform are supported by this
interface, with two exceptions. For transforms whose
total size exceeds 4G elements, the dimensions
specified in the array ``n`` must be factorable into
primes that are less than or equal to 17. For real to
complex and complex to real transforms whose total
size exceeds 4G elements, the fastest changing
dimension must be even.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``rank``      | Dimensionality of the transform (1, 2, or 3).       |
   +---------------+-----------------------------------------------------+
   | ``n``         | Array of size ``rank``, describing the size of each |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``inembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the input data in memory. If set to   |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``istride``   | Indicates the distance between two successive input |
   |               | elements in the least significant (i.e., innermost) |
   |               | dimension.                                          |
   +---------------+-----------------------------------------------------+
   | ``idist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the input     |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``onembed``   | Pointer of size ``rank`` that indicates the storage |
   |               | dimensions of the output data in memory. If set to  |
   |               | NULL all other advanced data layout parameters are  |
   |               | ignored.                                            |
   +---------------+-----------------------------------------------------+
   | ``ostride``   | Indicates the distance between two successive       |
   |               | output elements in the output array in the least    |
   |               | significant (i.e., innermost) dimension.            |
   +---------------+-----------------------------------------------------+
   | ``odist``     | Indicates the distance between the first element of |
   |               | two consecutive signals in a batch of the output    |
   |               | data.                                               |
   +---------------+-----------------------------------------------------+
   | ``type``      | The transform data type (e.g., ``MCFFT_R2C`` for    |
   |               | single precision real to complex).                  |
   +---------------+-----------------------------------------------------+
   | ``batch``     | Batch size for this transform.                      |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= =====================================
   ``*workSize`` Pointer to the size of the work area.
   ============= =====================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_ALLOC_FAILED``   | The allocation of GPU resources for the  |
   |                          | plan failed.                             |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | One or more invalid parameters were      |
   |                          | passed to the API.                       |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_SIZE``   | One or more of the parameters is not a   |
   |                          | supported size.                          |
   +--------------------------+------------------------------------------+

Function mcfftGetSize()
=========================

::

   mcfftResult 
         mcfftGetSize(mcfftHandle plan, size_t *workSize);

Once plan generation has been done, either with the
original API or the extensible API, this call returns the
actual size of the work area required to support the
plan. Callers who choose to manage work area allocation
within their application must use this call after plan
generation, and after any ``mcfftSet*()`` calls
subsequent to plan generation, if those calls might alter
the required work space size.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``*workSize`` | Pointer to the size(s), in bytes, of the work       |
   |               | areas.                                              |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ============= ======================================
   ``*workSize`` Pointer to the size of the work space.
   ============= ======================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully returned the size of  |
   |                          | the work space.                          |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+

mcFFT Caller Allocated Work Area Support
================================================

Function mcfftSetAutoAllocation()
-------------------------------------

::

   mcfftResult 
         mcfftSetAutoAllocation(mcfftHandle plan, int autoAllocate);

``mcfftSetAutoAllocation()`` indicates that the caller
intends to allocate and manage work areas for plans
that have been generated. mcFFT default behavior is to
allocate the work area at plan generation time. If
``mcfftSetAutoAllocation()`` has been called with
autoAllocate set to 0 ("false") prior to one of the
``mcfftMakePlan*()`` calls, mcFFT does not allocate
the work area. This is the preferred sequence for
callers wishing to manage work area allocation.

.. container:: tablenoborder

   **Input**

   ================ ============================================
   ``plan``         ``mcfftHandle`` returned by ``mcfftCreate.``
   ``autoAllocate`` Indicates whether to allocate work area.
   ================ ============================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully allows user to manage |
   |                          | work area.                               |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+

Function mcfftSetWorkArea()
-------------------------------

::

   mcfftResult 
         mcfftSetWorkArea(mcfftHandle plan, void *workArea);

``mcfftSetWorkArea()`` overrides the work area pointer
associated with a plan. If the work area was
auto-allocated, mcFFT frees the auto-allocated space.
The ``mcfftExecute*()`` calls assume that the work
area pointer is valid and that it points to a
contiguous region in device memory that does not
overlap with any other work area. If this is not the
case, results are indeterminate.

.. container:: tablenoborder

   **Input**

   +--------------+------------------------------------------------------+
   | ``plan``     | ``mcfftHandle`` returned by ``mcfftCreate``.         |
   +--------------+------------------------------------------------------+
   | ``workArea`` | Pointer to workArea.                                 |
   +--------------+------------------------------------------------------+

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully allows user to        |
   |                          | override workArea pointer.               |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+

Function mcfftDestroy()
==========================

::

   mcfftResult 
         mcfftDestroy(mcfftHandle plan);

Frees all GPU resources associated with a mcFFT plan and
destroys the internal plan data structure. This function
should be called once a plan is no longer needed, to
avoid wasting GPU memory.

.. container:: tablenoborder

   **Input**

   ======== =======================================================
   ``plan`` The ``mcfftHandle`` object of the plan to be destroyed.
   ======== =======================================================

.. container:: tablenoborder

   **Return Values**

   ====================== =============================================
   ``MCFFT_SUCCESS``      mcFFT successfully destroyed the FFT plan.
   ``MCFFT_INVALID_PLAN`` The ``plan`` parameter is not a valid handle.
   ====================== =============================================

mcFFT Execution
======================

Functions mcfftExecC2C() and mcfftExecZ2Z()
-----------------------------------------------

::

   mcfftResult 
         mcfftExecC2C(mcfftHandle plan, mcfftComplex *idata, 
            mcfftComplex *odata, int direction);
   mcfftResult 
         mcfftExecZ2Z(mcfftHandle plan, mcfftDoubleComplex *idata, 
            mcfftDoubleComplex *odata, int direction);

``mcfftExecC2C()`` (``mcfftExecZ2Z()``) executes a
single-precision (double-precision) complex-to-complex
transform plan in the transform direction as specified
by ``direction`` parameter. mcFFT uses the GPU memory
pointed to by the ``idata`` parameter as input data.
This function stores the Fourier coefficients in the
``odata`` array. If ``idata`` and ``odata`` are the
same, this method does an in-place transform.

.. container:: tablenoborder

   **Input**

   +---------------+-----------------------------------------------------+
   | ``plan``      | ``mcfftHandle`` returned by ``mcfftCreate``.        |
   +---------------+-----------------------------------------------------+
   | ``idata``     | Pointer to the complex input data (in GPU memory)   |
   |               | to transform.                                       |
   +---------------+-----------------------------------------------------+
   | ``odata``     | Pointer to the complex output data (in GPU memory). |
   +---------------+-----------------------------------------------------+
   | ``direction`` | The transform direction: ``MCFFT_FORWARD`` or       |
   |               | ``MCFFT_INVERSE``.                                  |
   +---------------+-----------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ========= ==========================================
   ``odata`` Contains the complex Fourier coefficients.
   ========= ==========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully executed the FFT      |
   |                          | plan.                                    |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | At least one of the parameters           |
   |                          | ``idata``, ``odata``, and ``direction``  |
   |                          | is not valid.                            |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_EXEC_FAILED``    | mcFFT failed to execute the transform on |
   |                          | the GPU.                                 |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+

Functions mcfftExecR2C() and mcfftExecD2Z()
--------------------------------------------------

::

   mcfftResult 
         mcfftExecR2C(mcfftHandle plan, mcfftReal *idata, mcfftComplex *odata);
   mcfftResult 
         mcfftExecD2Z(mcfftHandle plan, mcfftDoubleReal *idata, mcfftDoubleComplex *odata);

``mcfftExecR2C()`` (``mcfftExecD2Z()``) executes a
single-precision (double-precision) real-to-complex,
implicitly forward, mcFFT transform plan. mcFFT uses
as input data the GPU memory pointed to by the
``idata`` parameter. This function stores the
nonredundant Fourier coefficients in the ``odata``
array. Pointers to ``idata`` and ``odata`` are both
required to be aligned to ``mcfftComplex`` data type
in single-precision transforms and
``mcfftDoubleComplex`` data type in double-precision
transforms. If ``idata`` and ``odata`` are the same,
this method does an in-place transform. Note the data
layout differences between in-place and out-of-place
transforms as described in ``Parameter mcfftType``.

.. container:: tablenoborder

   **Input**

   ========= ============================================================
   ``plan``  ``mcfftHandle`` returned by ``mcfftCreate``.
   ``idata`` Pointer to the real input data (in GPU memory) to transform.
   ``odata`` Pointer to the complex output data (in GPU memory).
   ========= ============================================================

.. container:: tablenoborder

   **Output**

   ========= ==========================================
   ``odata`` Contains the complex Fourier coefficients.
   ========= ==========================================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully executed the FFT      |
   |                          | plan.                                    |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | At least one of the parameters ``idata`` |
   |                          | and ``odata`` is not valid.              |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_EXEC_FAILED``    | mcFFT failed to execute the transform on |
   |                          | the GPU.                                 |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+

Functions mcfftExecC2R() and mcfftExecZ2D()
-----------------------------------------------

::

   mcfftResult 
         mcfftExecC2R(mcfftHandle plan, mcfftComplex *idata, mcfftReal *odata);
   mcfftResult 
         mcfftExecZ2D(mcfftHandle plan, mcfftDoubleComplex *idata, mcfftDoubleReal *odata);

``mcfftExecC2R()`` (``mcfftExecZ2D()``) executes a
single-precision (double-precision) complex-to-real,
implicitly inverse, mcFFT transform plan. mcFFT uses
as input data the GPU memory pointed to by the
``idata`` parameter. The input array holds only the
nonredundant complex Fourier coefficients. This
function stores the real output values in the
``odata`` array. and pointers are both required to be
aligned to ``mcfftComplex`` data type in
single-precision transforms and ``mcfftDoubleComplex``
type in double-precision transforms. If ``idata`` and
``odata`` are the same, this method does an in-place
transform.

.. container:: tablenoborder

   **Input**

   +-----------+-----------------------------------------------------------------+
   | ``plan``  | ``mcfftHandle`` returned by ``mcfftCreate``.                    |
   +-----------+-----------------------------------------------------------------+
   | ``idata`` | Pointer to the complex input data (in GPU memory) to transform. |
   +-----------+-----------------------------------------------------------------+
   | ``odata`` | Pointer to the real output data (in GPU memory).                |
   +-----------+-----------------------------------------------------------------+

.. container:: tablenoborder

   **Output**

   ========= ==============================
   ``odata`` Contains the real output data.
   ========= ==============================

.. container:: tablenoborder

   **Return Values**

   +--------------------------+------------------------------------------+
   | ``MCFFT_SUCCESS``        | mcFFT successfully executed the FFT      |
   |                          | plan.                                    |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_PLAN``   | The ``plan`` parameter is not a valid    |
   |                          | handle.                                  |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INVALID_VALUE``  | At least one of the parameters ``idata`` |
   |                          | and ``odata`` is not valid.              |
   +--------------------------+------------------------------------------+
   | ``MCFFT_INTERNAL_ERROR`` | An internal driver error was detected.   |
   +--------------------------+------------------------------------------+
   | ``MCFFT_EXEC_FAILED``    | mcFFT failed to execute the transform on |
   |                          | the GPU.                                 |
   +--------------------------+------------------------------------------+
   | ``MCFFT_SETUP_FAILED``   | The mcFFT library failed to initialize.  |
   +--------------------------+------------------------------------------+

Function mcfftSetStream()
==============================

::

   mcfftResult 
         mcfftSetStream(mcfftHandle plan, mcStream_t stream);

Associates a MACA stream with a mcFFT plan. All kernel
launches made during plan execution are now done through
the associated stream, enabling overlap with activity in
other streams (e.g. data copying). The association
remains until the plan is destroyed or the stream is
changed with another call to ``mcfftSetStream()``.

.. container:: tablenoborder

   **Input**

   +------------+--------------------------------------------------------+
   | ``plan``   | The ``mcfftHandle`` object to associate with the       |
   |            | stream.                                                |
   +------------+--------------------------------------------------------+
   | ``stream`` | A valid MACA stream created with                       |
   |            | ``mcStreamCreate()``; ``0`` for the default stream.    |
   +------------+--------------------------------------------------------+

.. container:: tablenoborder

   **Status Returned**

   +------------------------+--------------------------------------------+
   | ``MCFFT_SUCCESS``      | The stream was associated with the plan.   |
   +------------------------+--------------------------------------------+
   | ``MCFFT_INVALID_PLAN`` | The ``plan`` parameter is not a valid      |
   |                        | handle.                                    |
   +------------------------+--------------------------------------------+

Function mcfftGetVersion()
==================================

::

   mcfftResult 
         mcfftGetVersion(int *version);

Returns the version number of mcFFT.

.. container:: tablenoborder

   **Input**

   =========== ==============================
   ``version`` Pointer to the version number.
   =========== ==============================

.. container:: tablenoborder

   **Output**

   =========== ============================
   ``version`` Contains the version number.
   =========== ============================

.. container:: tablenoborder

   **Return Values**

   ================= ===============================================
   ``MCFFT_SUCCESS`` mcFFT successfully returned the version number.
   ================= ===============================================

Function mcfftGetProperty()
========================================

::

   mcfftResult 
         mcfftGetProperty(mcfftLibraryPropertyType type, int *value);

Return in ``*value`` the number for the property
described by ``type`` of the dynamically linked mcFFT
library.

.. container:: tablenoborder

   **Input**

   ======== =======================
   ``type`` mcFFT library property.
   ======== =======================

.. container:: tablenoborder

   **Output**

   ========= ======================================================
   ``value`` Contains the integer value for the requested property.
   ========= ======================================================

.. container:: tablenoborder

   **Return Values**

   ======================= =============================================
   ``MCFFT_SUCCESS``       The property value was successfully returned.
   ``MCFFT_INVALID_TYPE``  The property type is not recognized.
   ``MCFFT_INVALID_VALUE`` ``value`` is ``NULL``.
   ======================= =============================================

mcFFT Types
==========================================

Parameter mcfftType
------------------------------------------

The mcFFT library supports complex- and real-data
transforms. The ``mcfftType`` data type is an
enumeration of the types of transform data supported
by mcFFT.

::

   typedef enum mcfftType_t {
         MCFFT_R2C = 0x2a,  // Real to complex (interleaved) 
         MCFFT_C2R = 0x2c,  // Complex (interleaved) to real 
         MCFFT_C2C = 0x29,  // Complex to complex (interleaved) 
         MCFFT_D2Z = 0x6a,  // Double to double-complex (interleaved) 
         MCFFT_Z2D = 0x6c,  // Double-complex (interleaved) to double 
         MCFFT_Z2Z = 0x69   // Double-complex to double-complex (interleaved)
   } mcfftType;

Parameters for Transform Direction
---------------------------------------

The mcFFT library defines forward and inverse Fast
Fourier Transforms according to the sign of the
complex exponential term.

::

         #define MCFFT_FORWARD -1
         #define MCFFT_INVERSE 1

mcFFT performs un-normalized FFTs; that is, performing
a forward FFT on an input data set followed by an
inverse FFT on the resulting set yields data that is
equal to the input, scaled by the number of elements.
Scaling either transform by the reciprocal of the size
of the data set is left for the user to perform as
seen fit.

Other mcFFT Types
--------------------------------------------

mcfftHandle
******************************************

A handle type used to store and access mcFFT plans.
The user receives a handle after creating a mcFFT
plan and uses this handle to execute the plan.

::

   typedef unsigned int mcfftHandle;

mcfftReal
*********************************************

A single-precision, floating-point real data type.

::

   typedef float mcfftReal;

mcfftDoubleReal
**********************************************

A double-precision, floating-point real data type.

::

   typedef double mcfftDoubleReal;

mcfftComplex
***********************************************

A single-precision, floating-point complex data
type that consists of interleaved real and
imaginary components.

::

   typedef mcComplex mcfftComplex;

mcfftDoubleComplex
*************************************************

A double-precision, floating-point complex data
type that consists of interleaved real and
imaginary components.

::

   typedef mcDoubleComplex mcfftDoubleComplex;

mcfftLibraryPropertyType
*****************************************

The ``mcfftLibraryPropertyType`` data type is an
enumeration of library property types. (ie. mcFFT
version X.Y.Z would yield ``MCFFT_VER_MAJOR=X``,
``MCFFT_VER_MINOR=Y``, ``MCFFT_VER_PATCH=Z``)

::

   typedef enum mcfftLibraryPropertyType_t
   {
      MCFFT_VER_MAJOR,
      MCFFT_VER_MINOR,
      MCFFT_VER_PATCH
   } mcfftLibraryPropertyType;

Common types
================================================

mcComplex
----------

Class to represent a complex number with single precision real and imaginary parts.

mcDoubleComplex
----------------

Class to represent a complex number with double precision real and imaginary parts.

