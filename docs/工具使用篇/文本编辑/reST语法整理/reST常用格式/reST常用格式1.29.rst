.. epigraph::
   
   No matter where you go, there you are. 
   
   -- Banzai

版權所有
----------------

Copyright |copy| 2023, |MACAMACA (TM)| |---| all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign

.. |MACAMACA (TM)| unicode:: MACAMACA U+2122 .. with trademark sign

.. |---|  unicode:: U+02014 .. em dash
   :trim:





章節自動編號
--------------------

``.. sectnum::``

Topic
-------------

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 

.. container:: custom
   
   This paragraph might be rendered in a custom way.



.. header:: This space for rent.

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 

.. topic:: 試試行不行
   
   If CLOCK_MODE equals 1, there is no idle time between back-to-back
   characters if data is ready in the transmit FIFO. In this case,
   because *sync_delay* equals one pclk as described in  :numref:`equ` 
   `Equation Example <#equ>`__, the requirement to avoid idle time
   between consecutive characters is met for all {DLH,DLL} values. 
   
   
.. sidebar:: 出現的位置
   
   出現在哪裏呢
   這個sidebar
   



分（不管用？）
----------------


.. hlist::
   :columns: 4
   
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified
   * good
   * bad 
   * excellent
   * normal
   * qualified


加粗居中
----------------

confidential

.. centered:: Confidential

.. centered:: **Confidential**

鏈接1
-----------------

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case,
because *sync_delay* equals one pclk as described in  :numref:`equ` 
`Equation Example <#equ>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 

:numref:`equ` `Equation Example <#equ>`__ is okay,

:numref:`equ` `Equation Example <#equation-example>`__ is okay.

:numref:`equ` `Equation Example <#equationexample>`__ is not okay.

:numref:`equ` `Equation Example <#Equation Example>`__ is not okay.

:numref:`equ` `Equation Example <#equation_example>`__ is not okay.

refer to :numref:`dmas` `DMA Support <#dmas>`__.


鏈接2
-----------------

If CLOCK_MODE equals 1, there is no idle time between back-to-back
characters if data is ready in the transmit FIFO. In this case, 
because *sync_delay* equals one pclk as described in 
:numref:`err` `Error <#error>`__, the requirement to avoid idle time
between consecutive characters is met for all {DLH,DLL} values. 



.. _equ:

Equation Example
-------------------------

.. _err:

Error
*************
說明：如果text大括號內有短線，這個命令的使用會導致報錯。在前面加上反斜線就okay.

.. math::
   \frac{\text{Rate of SSI data transmission}}{Rate of DW\_ahb\_dmac response to destination burst requests}


.. math::
   \frac{\text{Rate of SSI data transmission}}{\text{Rate of DW\_ahb\_dmac response to destination burst requests}}

空格的寫法
***************************

.. math::
   14\ (roundoff\ value)

.. math::
   \text{14 (roundoff value)}



短線的寫法
***************
前面加slash

.. math::
   \text{DLF} = BRD_F * 2^{DLF\_SIZE} 
   
   
.. math::
   BRD_F * 2^{DLF\underline{~}SIZE}
   
.. math:: \label{equ1}
   \text{DLF} = BRD_F * 2^{DLF\underline{~}SIZE} 

This equation \ref{equ1} is not okay?
   
.. math::
   \text{DLF} = BRD_F * 2^{DLF\_SIZE} = 0.866132364 * 16 = 13.858117824 = \text{14 (roundoff value)}

 


Therefore, the Generated Baud Rate (GBR) is as follows:

.. math::
   GBR = \frac{\text{Serial Clock}}{(16 × GD)} = \frac{133}{16 × 1.875} = 4433333.333 

Now the error is calculated as follows:

.. math::
   Error = \frac{\text{GBR - RBR}}{RBR} = 0.004729 

The error percentage is as follows:

.. math::
   Error \% = 0.004729 × 100 = 0.473 





