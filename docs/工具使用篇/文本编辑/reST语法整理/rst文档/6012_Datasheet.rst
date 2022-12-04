Overview
==============

The CSK6 serial is a dual-core microcontroller embedded with an ARM STAR core and
a HiFi4 core. The ARM Star core is designed for 32-bit microcontroller
applications, offering high performance, low power, simple instruction set
and addressing together with reduced code size compared with exiting
solutions. The HiFi4 core is designed for audio coders and decoders such as MP3,
AAC, and FLAC. The independent NPU is designed for neural network operation.

The CSK6 serial applies for smart home appliances.

The CSK6 serial can operate up to 300 MHz. Thus it can afford to support a
variety of industrial control and applications that require high CPU
performance. The CSK6 serial has a built-in 1-MB data SRAM.

The CSK6 serial supports many system-level peripheral functions, such as IO port, DVP, timer,
watchdog timer, UART, SPI, I2C, DMA, PLL, USB1.1 (full speed), RTC, and SDIO.

Block Diagram
==============

For the block diagram, see :ref:`Fig. 2.1 <2-1>`.

.. _2-1:

.. figure:: datasheet_figure/2-1_Block_Diagram.png
   :scale: 40%
   :alt: Block Diagram
   :align: center

   Block Diagram

Pin Mapping and Descriptions
=================================

Pin Mapping
-------------

For the pin mapping diagram, see :ref:`Fig. 3.1 <3-1>`.

.. _3-1:

.. figure:: datasheet_figure/3-1_Pin_Mapping_Diagram.png
   :scale: 40%
   :alt: Pin Mapping Diagram
   :align: center

   Pin Mapping Diagram

Pin Descriptions
----------------

For pin descriptions, refer to :ref:`Table 3.1 <Table3-1>`.

.. _Table3-1:

.. table:: Pin Descriptions
   :widths: grid

   +----------------+--------------------+------------------------------+
   | **Pin Number** | **Pin Name**       | **Description**              |
   +================+====================+==============================+
   | 1              | GPIO_A_14          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 2              | GPIO_A_15          | Multi-purpose digital I/O.   |
   |                |                    | It supports Boot ROM UART    |
   |                |                    | programming.                 |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 3              | GPIO_A_16          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 4              | GPIO_A_17          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 5              | GPIO_A_18          | Multi-purpose digital I/O.   |
   |                |                    | It supports Boot ROM UART    |
   |                |                    | programming.                 |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 6              | GPIO_A_19          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 7              | GPIO_A_20          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 8              | GPIO_B_11/USB_DM   | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 9              | GPIO_B_10/USB_DP   | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 10             | VDD_CORE_2         | Connect with VDD_CORE.       |
   +----------------+--------------------+------------------------------+
   | 11             | GPIO_B_08/GPADC_2  | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 12             | GPIO_B_07/GPADC_1  | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 13             | GPIO_B_06/GPADC_0  | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 14             | TST                | Test pin. Default: pull-up.  |
   |                |                    | 0: test mode.                |
   |                |                    | 1: normal mode.              |
   +----------------+--------------------+------------------------------+
   | 15             | RESETN             | Reset pin input.             |
   |                |                    | Default: pull-up.            |
   +----------------+--------------------+------------------------------+
   | 16             | GPIO_B_05/KEYSENSE | Multi-purpose digital I/O,   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 17             | GPIO_B_04          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 18             | GPIO_B_03          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 19             | GPIO_B_02/CBT_2    | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 20             | GPIO_B_01/CBT_1    | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 21             | GPIO_B_00/CBT_0    | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 22             | XTAL_OUT           | 24-MHz crystal.              |
   +----------------+--------------------+------------------------------+
   | 23             | XTAL_IN            | 24-MHz crystal.              |
   +----------------+--------------------+------------------------------+
   | 24             | VAD_AON            | Internal LDO output.         |
   |                |                    | Recommended capacitance:     |
   |                |                    | 1 μF.                        |
   +----------------+--------------------+------------------------------+
   | 25             | VCC                | Power input: 2.7 V-5.5 V.    |
   +----------------+--------------------+------------------------------+
   | 26             | VDD_IO             | Internal LDO output.         |
   |                |                    | Recommended capacitance:     |
   |                |                    | 4.7 μF.                      |
   +----------------+--------------------+------------------------------+
   | 27             | AVSS_AUD           | GND.                         |
   +----------------+--------------------+------------------------------+
   | 28             | AVDD_AUD           | Internal LDO output.         |
   |                |                    | Recommended capacitance:     |
   |                |                    | 2.2 μF.                      |
   +----------------+--------------------+------------------------------+
   | 29             | VREF               | Audio codec reference input. |
   +----------------+--------------------+------------------------------+
   | 30             | VMID               | Internal LDO output.         |
   |                |                    | Recommended capacitance:     |
   |                |                    | 4.7 μF.                      |
   +----------------+--------------------+------------------------------+
   | 31             | MICBIAS0           | Microphone bias output.      |
   |                |                    | Recommended capacitance:     |
   |                |                    | 2.2 μF.                      |
   +----------------+--------------------+------------------------------+
   | 32             | MICBIAS1           | Microphone bias output.      |
   |                |                    | Recommended capacitance:     |
   |                |                    | 2.2 μF.                      |
   +----------------+--------------------+------------------------------+
   | 33             | LIN_R_P            | Right channel                |
   |                |                    | differential outputs         |
   |                |                    | positive.                    |
   +----------------+--------------------+------------------------------+
   | 34             | LIN_R_N            | Right channel                |
   |                |                    | differential outputs         |
   |                |                    | negative.                    |
   +----------------+--------------------+------------------------------+
   | 35             | LIN_L_P            | Left channel                 |
   |                |                    | differential outputs         |
   |                |                    | positive.                    |
   +----------------+--------------------+------------------------------+
   | 36             | LIN_L_N            | Left channel                 |
   |                |                    | differential outputs         |
   |                |                    | negative.                    |
   +----------------+--------------------+------------------------------+
   | 37             | MIC0_P             | Microphone input positive.   |
   +----------------+--------------------+------------------------------+
   | 38             | MIC0_N             | Microphone input negative.   |
   +----------------+--------------------+------------------------------+
   | 39             | MIC1_P             | Microphone input positive.   |
   +----------------+--------------------+------------------------------+
   | 40             | MIC1_N             | Microphone input negative.   |
   +----------------+--------------------+------------------------------+
   | 41             | MIC2_P             | Microphone input positive.   |
   +----------------+--------------------+------------------------------+
   | 42             | MIC2_N             | Microphone input negative.   |
   +----------------+--------------------+------------------------------+
   | 43             | MIC3_P             | Microphone input positive.   |
   +----------------+--------------------+------------------------------+
   | 44             | MIC3_N             | Microphone input negative.   |
   +----------------+--------------------+------------------------------+
   | 45             | VDD_CORE           | Internal LDO output.         |
   |                |                    | Recommended capacitance:     |
   |                |                    | 4.7 μF.                      |
   |                |                    | Connect with VDD_CORE_2.     |
   +----------------+--------------------+------------------------------+
   | 46             | VDD_IO2            | Internal DC-DC input.        |
   |                |                    | Recommended  capacitance:    |
   |                |                    | 10 μF.                       |
   +----------------+--------------------+------------------------------+
   | 47             | VBK_PVSS           | DC-DC GND.                   |
   +----------------+--------------------+------------------------------+
   | 48             | VBK_SW             | DC-DC switch out. Connected  |
   |                |                    | with a 3.3-μH inductor.      |
   +----------------+--------------------+------------------------------+
   | 49             | VBK_IN             | DC-DC input power:           |
   |                |                    | 2.7 V-5.5 V.                 |           
   +----------------+--------------------+------------------------------+
   | 50             | GPIO_A_00/SWDCLK   | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 51             | GPIO_A_01/SWDTMS   | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 52             | GPIO_A_02          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 53             | GPIO_A_03          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 54             | FLASH_WP_N         | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 55             | FLASH_MISO         | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 56             | FLASH_CS_N         | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 57             | VDD_IO_1           | Input power. Connect with    |
   |                |                    | VDD_IO.                      |
   +----------------+--------------------+------------------------------+
   | 58             | FLASH_HOLD_N       | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 59             | FLASH_CLK          | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 60             | FLASH_MOSI         | Connect with an external     |
   |                |                    | QSPI flash.                  |
   +----------------+--------------------+------------------------------+
   | 61             | GPIO_A_10          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 62             | GPIO_A_11          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 63             | GPIO_A_12          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 64             | GPIO_A_13          | Multi-purpose digital I/O.   |
   |                |                    | Refer to 60XX_IOMUX.xlsx     |
   |                |                    | for details.                 |
   +----------------+--------------------+------------------------------+
   | 65             | EPAD               | Connect with GND.            |
   +----------------+--------------------+------------------------------+

.. Note::   
   The pull-up resistor resistance is set to 80 K. 

Functions
===============

Core
----

-  The ARM STAR and HiFi4 dual-core operates up to 300 MHz.

-  Independent NPU.

-  Hardware multiplier and hardware divider.

-  The embedded debug module supports the serial debug port (2-wire) and the JTAG debug port (4-wire).

Memory
------

-  External flash through the QSPI interface.

-  Totally 1088-KB SRAM shared by ARM and HiFi4 cores.

-  Dedicated 96-KB SRAM for the NPU block.

Clock Control
-------------

-  Programmable system clock source.

-  External 24-MHz high-speed crystal input to provide reference clock for the system.

-  Internal 32-KHz low-speed oscillator with calibration.

-  The PLL allows CPU operation up to 300 MHz with the system oscillator.

IO Port
-------

-  Up to 32 GPIO pins.

-  GPIO configuration.

-  Quasi-bidirectional (pull-up enabled).

-  Pull-down.

-  Push-pull (output).

-  Input only (high-impedance).

-  An I/O pin can be configured as an interrupt source through edge/level configuration.

-  Flexible IO function selection.

-  5-V tolerance IO for GPIOA.

GPT
---

The multi-function timer provides the following 4 usage scenarios
depending on the configuration of the channel mode register bit. The maximum
output frequency of the PWM is 50 MHz.

-  | Timer mode
   | Support 8/16/32-bit timers.

-  | Input capture mode
   | The capture count mode is used to capture the number of input pulses and the capture time mode 
     is used to capture pulse width.

-  | PWM mode
   | PWM can be configured as central-aligned mode (see :ref:`Fig. 4.1 <4-1>`) and
     edge-aligned mode (see :ref:`Fig. 4.2 <4-2>`).

   .. _4-1:

   .. figure:: datasheet_figure/4-1_Center-Aligned_Mode.png
      :scale: 30%
      :align: center

      Center-Aligned Mode

   .. _4-2:

   .. figure:: datasheet_figure/4-2_Edge-Aligned_Mode.png
      :scale: 30%

      Edge-Aligned Mode

-  LEDC output mode

SAR ADC
-------

-  12-bit resolution, up to 3 channels, up to 1 Msps, 24-MHz ADC clock.

-  Configurable hardware ADC trigger sources.

-  Configurable n-times ADC sampling.

-  Dedicated ADC data FIFO for each ADC channel.

-  Configurable ADC sampling duration.

-  Configurable waiting time for the next round of A/D conversion.

-  Switch on/off control.

-  ADC trimming.

-  ADC channel selection.

-  External/internal VREF selection.

-  | Real voltage calculation:
   | Reg\ :sub:`adc_value` = ADC register value
   | Voltage = (Reg\ :sub:`adc_value` - 2048)/2048*3.3

Audio Codec
-----------

-  Audio sample rates support 8 KHz to 96 KHz in the playback (DAC) path.

-  Audio sample rates support 8 KHz, 16 KHz, 44.1 KHz, or 48 KHz in the record (ADC) path.

-  | DAC SNR about 95 dB, THD -85 dB ('A'-weighted @ 8-48 KS/s).
   | ADC SNR about 95 dB, THD -85 dB ('A'-weighted @ 8-48 KS/s).

-  32-bit APB control interface to ADC01 separately.

-  32-bit APB control interface to ADC23 and DAC01 separately.

-  Programmable gain setting and soft mute control in the digital part.

-  | Programmable ALC loop/noise gate configuration in the ADC path.
   | Programmable ADC high-pass filter (wind noise reduction included).
   | The programmable ADC notch filter is selectable.

-  ADC01 and ADC23 support two stereo digital microphones.

-  Output gain/volume and mute control.

DVP
---

-  Designed as an AHB master component that can access the memory without any DMAC service.

-  Image frame completion notice and buffer switching.

-  Support 4:2:2 output format in the line buffer for JPEG encoding.

IWDG
----

-  Clocked from an internal 32-KHz low-speed oscillator or from a 32768-Hz crystal if available.

-  32-bit free-running counter.

-  Selectable timer-out interval.

UART
----

-  Four UART interfaces (1 for debug).

-  Three UARTs support hardware flow control (CTS/RTS) so that WiFi can be supported through UART interfaces.

-  UART0 to UART2 support hardware handshake for DMA.

-  Up to 3-Mb/s baudrate.

SPI
---

-  Three SPI interfaces.

-  Maximumly 50 Mb/s for the master mode.

-  Maximumly 25 Mb/s for the slave mode.

-  An SPI with the QSPI function must be used for the embedded NOR flash or the external flash.

-  Supports the master mode and the slave mode.

-  Supports memory mapped access (read-only) through the AHB bus.

-  Supports hardware handshake for DMA.

-  Supports the dual I/O mode and the quad I/O mode (QSPI).

I2C
---

-  Two I2C interfaces are available.

-  Programmable to be a master or a slave device.

-  Programmable clock/data timing.

-  Supports the I2C-bus standard-mode (100 kb/s), fast-mode (400 kb/s), and fast-mode plus (1 Mb/s).

-  Supports the hardware handshake for DMA.

-  Supports the master-transmit, master-receive, slave-transmit, and slave-receive modes.

-  Supports the multi-master mode.

-  Supports 7-bit and 10-bit addressing.

-  Supports general call addressing.

-  Supports automatic clock stretch.

RTC
---

-  Supports software compensation by setting the frequency compensation register.

-  The frequency of the clock source (before the clock divider) for the counter is 32.768 KHz.

-  Separate second, minute, hour, and day counters.

-  Periodic interrupts: half-second, second, minute, hour, and day interrupts.

-  Programmable alarm interrupt with specified second, minute, and hour numbers.

NPU
---

-  Matrix and vector operation accelerator.

-  AHB master interface for data read and write.

-  APB interface for register configuration.

-  Has interrupt signals.

-  Support reverse order storage, overflow detection, and location shift.

FCC RAM Controller
------------------

-  200 MHz maximumly. 

-  Arbitrate the data access request from the CPU, HiFi4, NPU, and DMAC.

-  Partition the NPU memory into several spaces.

-  If the accesses from different agents are in different spaces, all of them can be done immediately.

-  Flexible priority configuration: If the accesses from different agents are in the same space, the priority can be configured by users through the register.

PDM2PCM
-------

-  Support data conversion of PDM data from digital microphone to standard PCM data.

-  CIC filter in the always-on domain and half-band filter and memory in the main power domain.

CRYPTO
------

-  Support AES128 and SHA256 for secure communication.

-  AHB master interface for data read and write.

-  APB interface for register configuration.

eFuse Controller
----------------

-  Read eFuse content after receiving reset release signal from the reset sequence control.

-  Provide data to the crypto engine for encryption/decryption.

-  Provide data to the QSPI encryption wrapper to protect the content of the NOR flash.

True Random Number Generator
----------------------------

-  True random generator with mixed analog digital implementation to provide true random numbers.

-  Register configuration and generated random numbers can be accessed through the APB bus.

I2S Interface
-------------

-  Support extended microphone inputs.

-  Support I2S audio inputs and outputs.

-  3 independent I2S modules.

-  An input or output signal can be TDM-extended.

-  Register configuration and data operation through the APB bus.

USB1.1 Full Speed Device
------------------------

-  One set of 12-Mbps USB 1.1 FS device.

-  On-chip USB Transceiver.

-  Supports control, ISO in/out, bulk in/out, interrupt in/out transfers.

-  Provides 8 programmable endpoints.

-  Supports maximumly 1 KB for isochronous transfer and maximumly 64 bytes for bulk and interrupt transfer.

-  Each endpoint is configurable.

SDIO
----

-  Maximumly 25-MHz output clock

-  Compliant with the SD host controller standard specification, version 3.0.

-  Supports both DMA and non-DMA data transfer.

-  Compliant with the SD physical layer specification, version 3.0.

-  Supports UHS50/UHS104 SD cards.

-  Supports configurable SD bus modes: 4-bit mode and 8-bit mode.

-  Compliant with the SDIO card specification, version 3.0.

-  Compliant with the mandatory part in the eMMC card specification, version 5.1.

-  Supports configurable 1-bit/4-bit SD card bus and 1-bit/4-bit/8-bit EMMC card bus.

-  Configurable CPRM function for security.

-  Built-in generation and check for 7-bit and 16-bit CRC data.

-  Card detection (insertion/removal).

Power Management Unit
---------------------

-  Supports the sleep mode to reduce power consumption.

-  Supports wake-up through a RTC, timer, and key from IO.

-  Supports wake-up through VAD.

-  Supports system wakeup through touch.

Touch
-----

-  Supports touch point detection.

Audio ADC/DMIC/I2S
------------------

-  The audio ADC shares the internal memory with the DMIC and the I2S. For the restrictions on combination use, refer to :ref:`Table 4.1 <Table4-1>`.

.. _Table4-1:

.. table:: Restrictions on Combination Use

   +----------------------+-------------------+--------------------+-----------------+
   | **Occupied ADC/DAC** | **Available I2S** | **Available DMIC** | **Description** |
   +======================+===================+====================+=================+
   | ADC01 only, no       | I2S1, I2S2        | DMIC2, DMIC3       |                 |
   | DAC                  |                   |                    |                 |
   +----------------------+-------------------+--------------------+-----------------+
   | ADC23 only, no       | I2S0, I2S1 or     | DMIC0, DMIC1       | I2S1 or I2S2    |
   | DAC                  | I2S2              |                    | (either-or)     |
   +----------------------+-------------------+--------------------+-----------------+
   | ADC01+ADC23,         | I2S1 or I2S2      | None               | I2S1 or I2S2    |
   | no DAC               |                   |                    | (either-or)     |
   +----------------------+-------------------+--------------------+-----------------+
   | ADC01 only,          | I2S0, I2S2 (in)   | DMIC2, DMIC3       | I2S2 (in)       |
   | with DAC             |                   |                    |                 |
   +----------------------+-------------------+--------------------+-----------------+
   | ADC23 only,          | I2S0, I2S1 or     | DMIC0, DMIC1       | I2S1 or         |
   | with DAC             | I2S2 (in)         |                    | I2S2 (in)       |
   |                      |                   |                    | (either-or)     |
   +----------------------+-------------------+--------------------+-----------------+
   | ADC01+ADC23,         | I2S1 or           | None               | I2S1 or         |
   | with DAC             | I2S2 (in)         |                    | I2S2 (in)       |
   |                      |                   |                    | (either-or)     |
   +----------------------+-------------------+--------------------+-----------------+

Boot Mode
---------

For descriptions of the GPIOB0 and GPIOB1 boot modes, refer to :ref:`Table 4.2 <Table4-2>`.

.. _Table4-2:

.. table:: Boot Mode
    :widths: grid

    +------------+-------------+----------------------+
    | **GPIOB0** | **GPIOB1**  | **Mode Description** |
    +============+=============+======================+
    | 1          | 1           | NOR flash boot       |
    +------------+-------------+----------------------+
    | 1          | 0           | UART                 |
    +------------+-------------+----------------------+
    | 0          | 1           | Reserved             |
    +------------+-------------+----------------------+
    | 0          | 0           | DSP boot only        |
    +------------+-------------+----------------------+

.. Note::
   GPIOA15 (RXD) and GPIOA18 (TXD) are configured as the UART function in the UART boot mode.



Electrical Characteristics
==========================

Parameter Conditions
--------------------

Unless otherwise specified, all voltages are referred to as V\ :sub:`SS`\.

Minimum and Maximum Values
~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless otherwise specified the minimum and maximum values are guaranteed
in the worst conditions of ambient temperature, supply voltage and
frequencies during test in production on 100% of the devices with an
ambient temperature at 25 °C and the maximum temperature in the range.

Data based on characterization results, design simulation and/or
technology characteristics are indicated in the table footnotes and are
not tested in production. Based on characterization, the minimum and
maximum values are based on sample tests and represent the mean value plus
or minus three times the standard deviation (mean ± 3σ).

Typical Values
~~~~~~~~~~~~~~

Unless otherwise specified, typical data is based on T\ :sub:`A` = 25 °C, V\ :sub:`CCIN`
= 5 V (voltage range: 2.7 V :math:`\leqslant` V\ :sub:`CCIN` :math:`\leqslant` 5 V). They are given only
as design guidelines and are not tested.

Loading Capacitor
~~~~~~~~~~~~~~~~~

The loading capacitor used for pin parameter measurement is 10 pf.

Pin Input Voltage
~~~~~~~~~~~~~~~~~

The input voltage measurement on a pin of the device is through the current source device.

Operation Conditions
--------------------

Absolute Maximum Ratings
~~~~~~~~~~~~~~~~~~~~~~~~

For information about voltage characteristics, refer to :ref:`Table 5.1 <Table5-1>`.

.. _Table5-1:

.. table:: Voltage Characteristics
    :widths: grid

    +----------------------------------+------------------------+----------+---------+----------+
    | **Symbol**                       | **Ratings**            | **Min**  | **Max** | **Unit** |
    +==================================+========================+==========+=========+==========+
    | V\ :sub:`CCIN`-V\ :sub:`SS`      | External supply        | -0.3     | 5.5     | V        |
    |                                  | voltage                |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+
    | V\ :sub:`IL`                     | Low-level input        | -0.3     | 0.8     | V        |
    |                                  | voltage on signal pins |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+
    | V\ :sub:`IH`                     | High-level input       | 2        | 5.5     | V        |
    |                                  | voltage on signal pins |          |         |          |
    |                                  | (port A)               |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+
    | V\ :sub:`IH`                     | High-level input       | 2        | 3.6     | V        |
    |                                  | voltage on signal pins |          |         |          |
    |                                  | (port B)               |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+
    | V\ :sub:`OL`                     | Low-level output       |          | 0.4     | V        |
    |                                  | voltage on signal pins |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+
    | V\ :sub:`OH`                     | High-level output      | 2.4      |         | V        |
    |                                  | voltage on signal pins |          |         |          |
    +----------------------------------+------------------------+----------+---------+----------+


I/O Port Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~

For information about I/O Static characteristics, refer to :ref:`Table 5.2 <Table5-2>`.

.. _Table5-2:

.. table:: I/O Static Characteristics

   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | **Symbol**    | **Parameter** | **Conditions**    | **Min**  | **Typ**  | **Max**   | **Unit** |
   +===============+===============+===================+==========+==========+===========+==========+
   | V\ :sub:`IL`  | Standard IO   | 2.7 V             | -0.3     |          | 0.8       | V        |
   |               | low-level     | :math:`\leqslant` |          |          |           |          |
   |               | input         | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`IH`  | Standard IO   | 2.7 V             | 2        |          | 5.5       | V        |
   |               | high-level    | :math:`\leqslant` |          |          |           |          |
   |               | input         | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               | (port A)      | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`IH`  | Standard IO   | 2.7 V             | 2        |          | 3.6       | V        |
   |               | high-level    | :math:`\leqslant` |          |          |           |          |
   |               | input         | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               | (port B)      | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`hys` | Standard IO   | 2.7 V             |          | 220      |           | mV       |
   |               | Schmitt       | :math:`\leqslant` |          |          |           |          |
   |               | trigger       | V\ :sub:`CCIN`    |          |          |           |          |
   |               | voltage       | :math:`\leqslant` |          |          |           |          |
   |               | hysteresis    | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`OL`  | Low-level     | 2.7 V             |          |          | 0.4       | V        |
   |               | output        | :math:`\leqslant` |          |          |           |          |
   |               | voltage       | V\ :sub:`CCIN`    |          |          |           |          |
   |               |               | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | V\ :sub:`OH`  | High-level    | 2.7 V             | 2.4      |          |           | V        |
   |               | output        | :math:`\leqslant` |          |          |           |          |
   |               | voltage       | V\ :sub:`CCIN`    |          |          |           |          |
   |               |               | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`OL`  | Low-level     | 2.7 V             |          | 15       |           | mA       |
   |               | output        | :math:`\leqslant` |          |          |           |          |
   |               | current       | V\ :sub:`CCIN`    |          |          |           |          |
   |               |               | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`OH`  | High-level    | 2.7 V             |          | 22       |           | mA       |
   |               | output        | :math:`\leqslant` |          |          |           |          |
   |               | current       | V\ :sub:`CCIN`    |          |          |           |          |
   |               |               | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | I\ :sub:`Ikg` | Input         | 2.7 V             |          | 1        |           | μA       |
   |               | leakage       | :math:`\leqslant` |          |          |           |          |
   |               | current       | V\ :sub:`CCIN`    |          |          |           |          |
   |               |               | :math:`\leqslant` |          |          |           |          |
   |               |               | 5.5 V             |          |          |           |          |
   |               |               |                   |          |          |           |          |
   |               |               | T\ :sub:`A`       |          |          |           |          |
   |               |               | = 25 °C           |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | R\ :sub:`PU`  | Pull-up       |                   | 74 k     | 80 k     | 158 k     | Ω        |
   |               | equivalent    |                   |          |          |           |          |
   |               | resistor      |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | R\ :sub:`PD`  | Pull-down     |                   | 62 k     | 75 k     | 203 k     | Ω        |
   |               | equivalent    |                   |          |          |           |          |
   |               | resistor      |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+
   | C\ :sub:`IO`  | I/O pin       |                   |          | 5        |           | pF       |
   |               | capacitance   |                   |          |          |           |          |
   +---------------+---------------+-------------------+----------+----------+-----------+----------+

.. Note::
   Only port A is a 5-V tolerance IO and the input voltage can be 5.5 V maximumly.

IO AC Characteristics
~~~~~~~~~~~~~~~~~~~~~

For information about I/O AC characteristics, refer to :ref:`Table 5.3 <Table5-3>`.

.. _Table5-3:

.. table:: IO AC Characteristics
   :widths: grid

   +----------------------+------------------+---------------------+---------+---------+---------+----------+
   | **Symbol**           | **Parameter**    | **Conditions**      | **Min** | **Typ** | **Max** | **Unit** |
   +======================+==================+=====================+=========+=========+=========+==========+
   | F\ :sub:`max(io)out` | Maximum          | 2.7 V               |         | 100     |         | MHz      |
   |                      | frequency        | :math:`\leqslant`   |         |         |         |          |
   |                      |                  | V\ :sub:`CCIN`      |         |         |         |          |
   |                      |                  | :math:`\leqslant`   |         |         |         |          |
   |                      |                  | 5.5 V               |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | T\ :sub:`A`         |         |         |         |          |
   |                      |                  | = 25 °C             |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | C\ :sub:`L` = 10 pf |         |         |         |          |
   +----------------------+------------------+---------------------+---------+---------+---------+----------+
   | T\ :sub:`f(IO)out`   | Fall time        | 2.7 V               |         | 2.5     |         | ns       |
   |                      | and              | :math:`\leqslant`   |         |         |         |          |
   |                      | rise time        | V\ :sub:`CCIN`      |         |         |         |          |
   |                      |                  | :math:`\leqslant`   |         |         |         |          |
   |                      |                  | 5.5 V               |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | T\ :sub:`A`         |         |         |         |          |
   |                      |                  | = 25 °C             |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | C\ :sub:`L` = 10 pf |         |         |         |          |
   +                      +                  +---------------------+---------+---------+---------+----------+
   |                      |                  | 2.7 V               |         | 2.5     |         | ns       |
   |                      |                  | :math:`\leqslant`   |         |         |         |          |
   |                      |                  | V\ :sub:`CCIN`      |         |         |         |          |
   |                      |                  | :math:`\leqslant`   |         |         |         |          |
   |                      |                  | 5.5 V               |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | T\ :sub:`A`         |         |         |         |          |
   |                      |                  | = 25 °C             |         |         |         |          |
   |                      |                  |                     |         |         |         |          |
   |                      |                  | C\ :sub:`L` = 10 pf |         |         |         |          |
   +----------------------+------------------+---------------------+---------+---------+---------+----------+

nRESET Pin Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about nRESET pin characteristics, refer to :ref:`Table 5.4 <Table5-4>`.

.. _Table5-4:

.. table:: nRESET Pin Characteristics
   :widths: grid

   +--------------------+-------------------+-------------------+---------+---------+---------+----------+
   | **Symbol**         | **Parameter**     | **Conditions**    | **Min** | **Typ** | **Max** | **Unit** |
   +====================+===================+===================+=========+=========+=========+==========+
   | R\ :sub:`PU`       | Pull-up           | 2.7 V             |         | 80 k    |         | Ω        |
   |                    | equivalent        | :math:`\leqslant` |         |         |         |          |
   |                    | resistor          | V\ :sub:`CCIN`    |         |         |         |          |
   |                    |                   | :math:`\leqslant` |         |         |         |          |
   |                    |                   | 5.5 V             |         |         |         |          |
   |                    |                   |                   |         |         |         |          |
   |                    |                   | T\ :sub:`A`       |         |         |         |          |
   |                    |                   | = 25 °C           |         |         |         |          |
   +--------------------+-------------------+-------------------+---------+---------+---------+----------+
   | T\ :sub:`(nRESET)` | nRESET input      | 2.7 V             |         | 1       |         | ms       |
   |                    | pulse             | :math:`\leqslant` |         |         |         |          |
   |                    |                   | V\ :sub:`CCIN`    |         |         |         |          |
   |                    |                   | :math:`\leqslant` |         |         |         |          |
   |                    |                   | 5.5 V             |         |         |         |          |
   |                    |                   |                   |         |         |         |          |
   |                    |                   | T\ :sub:`A`       |         |         |         |          |
   |                    |                   | = 25 °C           |         |         |         |          |
   |                    |                   |                   |         |         |         |          |
   |                    |                   | C\ :sub:`L`       |         |         |         |          |
   |                    |                   | = 10 pf           |         |         |         |          |
   +--------------------+-------------------+-------------------+---------+---------+---------+----------+

Supply Current Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about supply current characteristics, refer to :ref:`Table 5.5 <Table5-5>`.

.. _Table5-5:

.. table:: Supply Current Characteristics
   :widths: grid

   +--------------+---------------+-----------------+---------------------+-------------+----------+
   | **Symbol**   | **Parameter** | **Conditions**  | f\ :sub:`sysclk`    | **Typical** | **Unit** |
   |              |               |                 | **(MHz)**           |             |          |
   +==============+===============+=================+=====================+=============+==========+
   | I\ :sub:`DD` | Supply        | V\ :sub:`CCIN`  | 100                 | 20          | mA       |
   |              | current       | = 5 V,          |                     |             |          |
   |              | in RUN        | external        |                     |             |          |
   |              | mode          | 24-MHz crystal  |                     |             |          |
   |              |               |                 |                     |             |          |
   |              |               | T\ :sub:`A`     |                     |             |          |
   |              |               | = 25 °C,        |                     |             |          |
   |              |               | PLL ON,         |                     |             |          |
   |              |               |                 |                     |             |          |
   |              |               | AP ON, CP       |                     |             |          |
   |              |               | ON, NPU ON      |                     |             |          |
   |              |               |                 |                     |             |          |
   |              |               | PSRAM           |                     |             |          |
   |              |               | off, NOR        |                     |             |          |
   |              |               | flash           |                     |             |          |
   |              |               | cached          |                     |             |          |
   |              +---------------+-----------------+---------------------+-------------+----------+
   |              | Supply        | T\ :sub:`A`     | 24                  | 1.8         | mA       |
   |              | current       | = 25 °C,        |                     |             |          |
   |              | in            | deep            |                     |             |          |
   |              | VAD&          | sleep           |                     |             |          |
   |              | DEEPSLEEP     | mode            |                     |             |          |
   |              | mode          | entered,        |                     |             |          |
   |              |               | VAD mode        |                     |             |          |
   |              |               | enabled         |                     |             |          |
   |              |               | with 1          |                     |             |          |
   |              |               | audio ADC       |                     |             |          |
   |              |               | on (analog      |                     |             |          |
   |              |               | mic not         |                     |             |          |
   |              |               | included)       |                     |             |          |
   |              +---------------+-----------------+---------------------+-------------+----------+
   |              | Supply        | T\ :sub:`A`     | 24                  | 700         | μA       |
   |              | current       | = 25 °C,        |                     |             |          |
   |              | in            | deep            |                     |             |          |
   |              | DEEPSLEEP     | sleep           |                     |             |          |
   |              | mode          | mode            |                     |             |          |
   |              |               | entered         |                     |             |          |
   +--------------+---------------+-----------------+---------------------+-------------+----------+

Wake-up Time from the Sleep Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about wake-up time from the sleep mode, refer to :ref:`Table 5.6 <Table5-6>`.

.. _Table5-6:

.. table:: Wakeup Time from Sleep Modes
   :widths: grid

   +-------------------+----------------+----------------+-------------+----------+
   | **Symbol**        | **Parameter**  | **Conditions** | **Typical** | **Unit** |
   +===================+================+================+=============+==========+
   | t\ :sub:`WUSLEEP` | Wakeup from    | External pin   | < 2         | ms       |
   |                   | sleep          | wake-up (ROM   |             |          |
   |                   |                | boot not       |             |          |
   |                   |                | included)      |             |          |
   +-------------------+----------------+----------------+-------------+----------+

External Clock Source Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about external clock source characteristics, refer to :ref:`Table 5.7 <Table5-7>`.

.. _Table5-7:

.. table:: External Clock Source Characteristics
   :widths: grid

   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | **Symbol**         | **Parameter**  | **Conditions** | **Min** | **Typ** | **Max** | **Unit** |
   +====================+================+================+=========+=========+=========+==========+
   | f\ :sub:`osc`      | External       |                |         | 24      |         | MHz      |
   |                    | clock source   |                |         |         |         |          |
   |                    | frequency      |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | V\ :sub:`OSCH`     | OSC in input   |                |         | 3.3     |         | V        |
   |                    | pin high       |                |         |         |         |          |
   |                    | level          |                |         |         |         |          |
   |                    | voltage        |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | V\ :sub:`OSCL`     | OSC in input   |                |         | 0       |         | V        |
   |                    | pin low        |                |         |         |         |          |
   |                    | level          |                |         |         |         |          |
   |                    | voltage        |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | C\ :sub:`IN(OSC)`  | OSC in input   |                |         | 5       |         | pF       |
   |                    | capacitance    |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | Ducy\ :sub:`(OSC)` | Duty cycle     |                | 45      |         | 55      | %        |
   |                    |                |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+
   | I\ :sub:`L`        | OSC IN input   |                |         | 430     |         | μA       |
   |                    | leakage        |                |         |         |         |          |
   |                    | current        |                |         |         |         |          |
   +--------------------+----------------+----------------+---------+---------+---------+----------+

Internal Clock Source Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about internal clock source characteristics, refer to :ref:`Table 5.8 <Table5-8>`.

.. _Table5-8:

.. table:: Internal Clock Source Characteristics
   :widths: grid

   +-------------------+---------------+-------------------------+---------+---------+---------+----------+
   | **Symbol**        | **Parameter** | **Conditions**          | **Min** | **Typ** | **Max** | **Unit** |
   +===================+===============+=========================+=========+=========+=========+==========+
   | f\ :sub:`LSI`     | Frequency     | 2.7 V :math:`\leqslant` |         | 32      |         | KHz      |
   |                   |               | V\ :sub:`CCIN`          |         |         |         |          |
   |                   |               | :math:`\leqslant` 5.5 V |         |         |         |          |
   |                   |               |                         |         |         |         |          |
   |                   |               | T\ :sub:`A`             |         |         |         |          |
   |                   |               | = 25 °C                 |         |         |         |          |
   +-------------------+---------------+-------------------------+---------+---------+---------+----------+
   | t\ :sub:`su(LSI)` | LSI           | 2.7 V :math:`\leqslant` |         | 5       |         | s        |
   |                   | oscillator    | V\ :sub:`CCIN`          |         |         |         |          |
   |                   | start-up      | :math:`\leqslant` 5.5 V |         |         |         |          |
   |                   | time          |                         |         |         |         |          |
   |                   |               | T\ :sub:`A`             |         |         |         |          |
   |                   |               | = 25 °C                 |         |         |         |          |
   +-------------------+---------------+-------------------------+---------+---------+---------+----------+
   | I\ :sub:`DD(LSI)` | LSI           | 2.7 V :math:`\leqslant` |         |         | 1       | μA       |
   |                   | oscillator    | V\ :sub:`CCIN`          |         |         |         |          |
   |                   | power         | :math:`\leqslant` 5.5 V |         |         |         |          |
   |                   | consumption   |                         |         |         |         |          |
   |                   |               | T\ :sub:`A`             |         |         |         |          |
   |                   |               | = 25 °C                 |         |         |         |          |
   +-------------------+---------------+-------------------------+---------+---------+---------+----------+

PLL Characteristics
~~~~~~~~~~~~~~~~~~~

For information about PLL characteristics, refer to :ref:`Table 5.9 <Table5-9>`.

.. _Table5-9:

.. table:: PLL Characteristics
   :widths: grid

   ================= ===================== ============== ======= ======= ======= ========
   **Symbol**        **Parameter**         **Conditions** **Min** **Typ** **Max** **Unit**
   ================= ===================== ============== ======= ======= ======= ========
   f\ :sub:`PLL_IN`  PLL input clock                              24              MHz
   f\ :sub:`PLL_OUT` PLL output clock                             300             MHz
   Jitter            Cycle-to cycle jitter                        10              ps
   ================= ===================== ============== ======= ======= ======= ========

EMC
~~~

For information about Electromagnetic Compatibility (EMC), refer to :ref:`Table 5.10 <Table5-10>`.

.. _Table5-10:

.. table:: EMC
   :widths: grid

   +------------+-------------+-----------------+-----------+-----------+----------+
   | **Symbol** | **Ratings** | **Conditions**  | **Class** | **Maximum | **Unit** |
   |            |             |                 |           | Value**   |          |
   +============+=============+=================+===========+===========+==========+
   | VESD (HBM) | Elec        | T\ :sub:`A`     | 2         | 2000      | V        |
   |            | trostatic   | = 25 °C         |           |           |          |
   |            | discharge   |                 |           |           |          |
   |            | voltage     |                 |           |           |          |
   |            | (human      |                 |           |           |          |
   |            | body        |                 |           |           |          |
   |            | model)      |                 |           |           |          |
   +------------+-------------+-----------------+-----------+-----------+----------+
   | VESD (CDM) | Elec        | T\ :sub:`A`     |           | 1000      | V        |
   |            | trostatic   | = 25 °C         |           |           |          |
   |            | discharge   |                 |           |           |          |
   |            | voltage     |                 |           |           |          |
   |            | (charge     |                 |           |           |          |
   |            | device      |                 |           |           |          |
   |            | model)      |                 |           |           |          |
   +------------+-------------+-----------------+-----------+-----------+----------+

Package Information
===================

QFN64 (8*8 mm) Package Information
-----------------------------------

For the package information, see :ref:`Fig. 6.1 <6-1>`, :ref:`Fig. 6.2 <6-2>`, and :ref:`Figure 6-3 <6-3>`.

.. _6-1:

.. figure:: datasheet_figure/6-1_Top_View.png
   :scale: 65%
   :align: center

   Top View

.. _6-2:

.. figure:: datasheet_figure/6-2_Bottom_View.png
   :scale: 65%
   :align: center

   Bottom View


.. _6-3:

.. figure:: datasheet_figure/6-3.png
   :scale: 65%
   :align: center

   Symbol Dimension

Thermal Characteristics
-----------------------

The maximum chip junction temperature (T\ :sub:`J`\max) in degrees
Celsius can be calculated through the following equation:

.. math::    
   T_J max = T_A max + (P_D max * \theta_{JA})   

where:

-  T\ :sub:`A`\max is the maximum ambient temperature in °C.

-  θ\ :sub:`JA` is the package junction-to-ambient thermal resistance in °C/W.

-  P\ :sub:`D`\max is the sum of P\ :sub:`INT`\max and P\ :sub:`I/O`\max
   (P\ :sub:`D`\max = P\ :sub:`INT`\max + P\ :sub:`I/O`\max).

-  P\ :sub:`INT`\max is the product of I\ :sub:`DD` and V\ :sub:`DD` in Watts. 
   This is the maximum chip internal power.

P\ :sub:`I/O`\max represents the maximum power dissipation on output pins and can be 
calculated through the following equation:

.. math::
   P_{I/O} max = \sum (V_{OL} * I_{OL}) + ((V_{DD} – V_{OH}) * I_{OH})

The actual V\ :sub:`OL`/I\ :sub:`OL` and V\ :sub:`OH`/I\ :sub:`OH` of the I/Os at
low and high levels in the application are taken into account.

.. _Table6-1:

.. table:: Package Thermal Characteristics
   :widths: grid

   +---------------+-----------------------------------------+----------------+----------+
   | **Symbol**    | **Parameter**                           | **Value**      | **Unit** |
   +===============+=========================================+================+==========+
   | θ\ :sub:`JA`  | Junction-to-ambient thermal resistance  | 28             | °C/W     |
   |               |                                         |                |          |
   |               | QFN64 – 8*8 mm                          |                |          |
   +---------------+-----------------------------------------+----------------+----------+
   | T\ :sub:`STG` | Storage temperature range               | –65 to +150    | °C       |
   +---------------+-----------------------------------------+----------------+----------+
   | T\ :sub:`J`   | Maximum junction temperature            | 125            | °C       |
   +---------------+-----------------------------------------+----------------+----------+

Reflow Profile
==============

Reflow Diagram
-----------------

For the reflow diagram, see :ref:`Fig. 7.1 <7-1>`.

.. _7-1:

.. figure:: datasheet_figure/7-1_Reflow_Diagram.png
   :scale: 45%
   :align: center

   Reflow Diagram

SMT Reflow Conditions
--------------------------

.. _Table7-1:

.. table:: Reflow Parameter Descriptions
   :widths: grid

   +----------------------------------+----------------------------------+
   | **Parameter**                    | **Requirement**                  |
   +==================================+==================================+
   | N2 purge reflow usage            | Yes                              |
   +----------------------------------+----------------------------------+
   | O2 ppm level                     | < 1500 ppm                       |
   +----------------------------------+----------------------------------+
   | Temperature Min (T\ :sub:`smin`) | 150 °C                           |
   +----------------------------------+----------------------------------+
   | Temperature Max (T\ :sub:`smax`) | 200 °C                           |
   +----------------------------------+----------------------------------+
   | Time                             | 60-120 seconds                   |
   | (t\ :sub:`s`)from(T\ :sub:`smin` |                                  |
   | to T\ :sub:`smax`)               |                                  |
   +----------------------------------+----------------------------------+
   | Ramp-up rate (T\ :sub:`L` to     | 3 °C/second maximumly            |
   | T\ :sub:`P`)                     |                                  |
   +----------------------------------+----------------------------------+
   | Liquidous                        | 217 °C                           |
   | temperature (T\ :sub:`L` )       |                                  |
   +----------------------------------+----------------------------------+
   | Time(t\ :sub:`L`) maintained     | 60-150 seconds                   |
   | above T\ :sub:`L`                |                                  |
   +----------------------------------+----------------------------------+
   | Peak package body                | Tp must not exceed the           |
   | temperature (T\ :sub:`P`)        | Classification                   |
   |                                  | temp (T\ :sub:`C`\ ) in table    |
   |                                  | below                            |
   +----------------------------------+----------------------------------+
   | Time(t\ :sub:`p`)within 5 °C of  | 30 seconds maximumly             |
   | the specified classification     |                                  |
   | temperature (T\ :sub:`C`)        |                                  |
   +----------------------------------+----------------------------------+
   | Ramp-down rate (T\ :sub:`P` to   | 6 °C/second maximumly            |
   | T\ :sub:`L`)                     |                                  |
   +----------------------------------+----------------------------------+
   | Time 25 °C to peak temperature   | 8 minutes maximumly              | 
   +----------------------------------+----------------------------------+

.. _Table7-2:

.. table:: Corresponding Relationshiop among Thickness, Volume, and Temperature
   :widths: grid

   +----------------+----------------+----------------+----------------+
   | **Package      | **Volume mm3   | **Volume mm3   | **Volume mm3   |
   | Thickness**    | < 350**        | 350-2000**     | > 2000**       |
   +================+================+================+================+
   | < 1.6 mm       | 260 °C         | 260 °C         | 260 °C         |
   +----------------+----------------+----------------+----------------+
   | 1.6 mm-2.5 mm  | 260 °C         | 250 °C         | 245 °C         |
   +----------------+----------------+----------------+----------------+
   | > 2.5 mm       | 250 °C         | 245 °C         | 245 °C         |
   +----------------+----------------+----------------+----------------+

Weight
======

The SoC weighs 200 mg.

Application Diagram
===================
For the application diagram, see :ref:`Fig. 9.1 <9-1>`.

.. _9-1:

.. figure:: datasheet_figure/9-1_Application_Diagram.png
   :scale: 50%
   :align: center

   Application Diagram



