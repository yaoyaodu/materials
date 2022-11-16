General Description
===================

CSK6 serial is a dual core microcontroller with embedded ARM STAR core &
HIFI4 core. ARM Star is designed for 32-bit microcontroller
applications, offering performance, low power, simple instruction set
and addressing together with reduced code size compared to exiting
solutions. HIFI4 is designed for audio coder and decoder such as mp3,
AAC, flac….. Independent NPU is designed for neural network operation.

Target applications: smart home appliance

The CSK6 serial can run up to 300MHz. Thus it can afford to support a
variety of industrial control and applications which need high CPU
performance. The CSK6 serial has up to 1M bytes internal data SRAM.

Many system level peripheral functions, such as IO port, DVP, Timer,
Watchdog Timer, UART, SPI, I2C, DMA, PLL, USB1.1 (Full speed), RTC, SDIO
are supported.

Block Diagrams
==============

For the block diagrams, see :ref:`Figure 2-1 <2-1>` .

.. _2-1:

.. figure:: datasheet_figure/2-1_Block_Diagram.png
   :scale: 100%
   :alt: Block Diagram
   :align: center

   **Figure 2‑1 Block Diagram**

Pin Mapping and Description
===========================

Pin Mapping
-------------

For the pin mapping diagram, see :ref:`Figure 3-1 <3-1>` .

.. _3-1:

.. figure:: datasheet_figure/3-1_Pin_Mapping_Diagram.png
   :scale: 100%
   :alt: Pin Mapping Diagram
   :align: center

   **Figure 3‑1 Pin Mapping Diagram**

Pin Descriptions
----------------

For pin descriptions, refer to :ref:`Table 3-1 <Table3-1>` .

.. _Table3-1:

.. table:: **Table 3‑1 Pin Descriptions**

   +----------------+--------------------+------------------------------+
   | **Pin Number** | **Pin Name**       | **Description**              |
   +================+====================+==============================+
   | 1              | GPIO_A_14          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 2              | GPIO_A_15          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions, (Boot    |
   |                |                    | ROM UART programming pin)    |
   +----------------+--------------------+------------------------------+
   | 3              | GPIO_A_16          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 4              | GPIO_A_17          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 5              | GPIO_A_18          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions, (Boot    |
   |                |                    | ROM UART programming pin)    |
   +----------------+--------------------+------------------------------+
   | 6              | GPIO_A_19          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 7              | GPIO_A_20          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 8              | GPIO_B_11/USB_DM   | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 9              | GPIO_B_10/USB_DP   | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 10             | VDD_CORE_2         | Should connect with VDD_CORE |
   +----------------+--------------------+------------------------------+
   | 11             | GPIO_B_08/GPADC_2  | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 12             | GPIO_B_07/GPADC_1  | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 13             | GPIO_B_06/GPADC_0  | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 14             | TST                | Test pin, default pull up.   |
   |                |                    | 0: test mode 1: normal mode  |
   +----------------+--------------------+------------------------------+
   | 15             | RESETN             | Reset pin input, default     |
   |                |                    | pull up                      |
   +----------------+--------------------+------------------------------+
   | 16             | GPIO_B_05/KEYSENSE | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 17             | GPIO_B_04          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 18             | GPIO_B_03          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 19             | GPIO_B_02/CBT_2    | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 20             | GPIO_B_01/CBT_1    | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 21             | GPIO_B_00/CBT_0    | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 22             | XTAL_OUT           | 24MHz crystal                |
   +----------------+--------------------+------------------------------+
   | 23             | XTAL_IN            | 24MHz crystal                |
   +----------------+--------------------+------------------------------+
   | 24             | VAD_AON            | Internal LDO output, 1uf cap |
   |                |                    | recommended                  |
   +----------------+--------------------+------------------------------+
   | 25             | VCC                | Power input : 2.7V-5.5V      |
   +----------------+--------------------+------------------------------+
   | 26             | VDD_IO             | Internal LDO output, 4.7uF   |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 27             | AVSS_AUD           | GND                          |
   +----------------+--------------------+------------------------------+
   | 28             | AVDD_AUD           | Internal LDO output, 2.2uF   |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 29             | VREF               | Audio codec reference input  |
   +----------------+--------------------+------------------------------+
   | 30             | VMID               | Internal LDO output, 4.7uF   |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 31             | MICBIAS0           | Mic bias output，Cload=2.2uF |
   +----------------+--------------------+------------------------------+
   | 32             | MICBIAS1           | Mic bias output，Cload=2.2uF |
   +----------------+--------------------+------------------------------+
   | 33             | LIN_R_P            | LINE right channel           |
   |                |                    | differential outputs         |
   |                |                    | positive                     |
   +----------------+--------------------+------------------------------+
   | 34             | LIN_R_N            | LINE right channel           |
   |                |                    | differential outputs         |
   |                |                    | negative                     |
   +----------------+--------------------+------------------------------+
   | 35             | LIN_L_P            | LINE left channel            |
   |                |                    | differential outputs         |
   |                |                    | positive                     |
   +----------------+--------------------+------------------------------+
   | 36             | LIN_L_N            | LINE left channel            |
   |                |                    | differential outputs         |
   |                |                    | negative                     |
   +----------------+--------------------+------------------------------+
   | 37             | MIC0_P             | Mic input positive           |
   +----------------+--------------------+------------------------------+
   | 38             | MIC0_N             | Mic input negative           |
   +----------------+--------------------+------------------------------+
   | 39             | MIC1_P             | Mic input positive           |
   +----------------+--------------------+------------------------------+
   | 40             | MIC1_N             | Mic input negative           |
   +----------------+--------------------+------------------------------+
   | 41             | MIC2_P             | Mic input positive           |
   +----------------+--------------------+------------------------------+
   | 42             | MIC2_N             | Mic input negative           |
   +----------------+--------------------+------------------------------+
   | 43             | MIC3_P             | Mic input positive           |
   +----------------+--------------------+------------------------------+
   | 44             | MIC3_N             | Mic input negative           |
   +----------------+--------------------+------------------------------+
   | 45             | VDD_CORE           | internal LDO output, 4.7uF   |
   |                |                    | cap recommended, should      |
   |                |                    | connect with VDD_CORE_2      |
   +----------------+--------------------+------------------------------+
   | 46             | VDD_IO2            | Internal DC-DC input, 10uF   |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 47             | VBK_PVSS           | DC-DC GND                    |
   +----------------+--------------------+------------------------------+
   | 48             | VBK_SW             | DC-DC switch out, 3.3uH      |
   |                |                    | inductor connected           |
   +----------------+--------------------+------------------------------+
   | 49             | VBK_IN             | DC-DC Input power: 2.7V-5.5V |
   +----------------+--------------------+------------------------------+
   | 50             | GPIO_A_00/SWDCLK   | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 51             | GPIO_A_01/SWDTMS   | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 52             | GPIO_A_02          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 53             | GPIO_A_03          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 54             | FLASH_WP_N         | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 55             | FLASH_MISO         | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 56             | FLASH_CS_N         | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 57             | VDD_IO_1           | Input power connect with     |
   |                |                    | VDD_IO                       |
   +----------------+--------------------+------------------------------+
   | 58             | FLASH_HOLD_N       | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 59             | FLASH_CLK          | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 60             | FLASH_MOSI         | Connect with external QSPI   |
   |                |                    | Flash                        |
   +----------------+--------------------+------------------------------+
   | 61             | GPIO_A_10          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 62             | GPIO_A_11          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 63             | GPIO_A_12          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 64             | GPIO_A_13          | Multi-Purpose Digital I/O,   |
   |                |                    | please refer to the          |
   |                |                    | 60XX_IOMUX.xlsx for the      |
   |                |                    | detailed functions           |
   +----------------+--------------------+------------------------------+
   | 65             | EPAD               | Connect with GND             |
   +----------------+--------------------+------------------------------+

.. Note::
   The pull up resister is configured as 80K.

Function Overview
=================

Core
----

-  ARM STAR&HIFI4 dual core runs up to 300 MHz

-  Independent NPU

-  Hardware multiplier and hardware divider.

-  Embedded Debug Module supports serial debug port(2-wire) and JTAG debug(4-wire)

Memory
------

-  External flash through QSPI interface

-  Totally 1088KB SRAM shared by ARM and HIFI4

-  Dedicated 96KB SRAM for NPU block

Clock Control
-------------

-  Programmable system clock source.

-  External 24 MHz high speed crystal input to provide reference clock for system.

-  Internal 32 KHz low speed oscillator with calibration.

-  PLL allows CPU operation up to 300MHz with the system oscillator.

IO Port
-------

-  Up to 32 general-purpose I/O(GPIO) pins

-  GPIO configuration

-  Quasi-bidirectional (Pull-up Enable)

-  Pull down

-  Push-pull (Output)

-  Input only (high-impedance)

-  I/O pin can be configured as interrupt source with edge/level
   setting.

-  Flexible IO function select.

-  5V tolerance IO for GPIOA

GPT
---

The multi-function timer provides the following 6 usage scenarios
depending on the Channel Mode register bit configurations. PWM maximum
output frequency is 50MHz.

-  Timer mode

   support 8/16/32bit Timer

-  Input capture mode

   Capture count mode is used to capture input pulse count, and capture
   time mode is used to capture pulse width.

-  PWM mode

   PWM can be configured as central-aligned mode(see :ref:`Figure 4-1 <4-1>`) and
   edge-aligned mode(see :ref:`Figure 4-2 <4-2>`):

.. _4-1:

.. figure:: datasheet_figure/4-1_Center-Aligned_Mode.png
   :scale: 40%
   :align: center

   **Figure 4‑1 Center-Aligned Mode**

   .. _4-2:

   .. figure:: datasheet_figure/4-2_Edge-Aligned_Mode.png
      :scale: 40 %

      **Figure 4‑2 Edge-Aligned Mode**

-  LEDC output mode

SAR ADC
-------

-  12-bit resolution, up to 3 channels, up to 1Msps, 24MHz ADC clock

-  Configurable hardware ADC trigger sources

-  User configurable n-times ADC sampling

-  Dedicated ADC Data FIFO for each ADC channel

-  Configurable ADC sampling duration

-  Configurable waiting time for next Round A/D conversion

-  switch on/off control

-  ADC trimming

-  ADC channel selection

-  External/internal VREF selection

-  | Real voltage caculation:
   | Reg\ :sub:`adc_value` = ADC register value
   | Voltage = (Reg\ :sub:`adc_value` - 2048)/2048*3.3

Audio Codec
-----------

-  Audio sample rates support 8KHz to 96KHz in playback (DAC) path

-  Audio sample rates support 8KHz，16KHz，44.1KHz or 48KHz in record (ADC) path

-  | DAC SNR about 95dB，THD -85dB (‘A’-weighted @ 8-48ks/s)
   | ADC SNR about 95dB，THD -85dB (‘A’-weighted @ 8-48ks/s)

-  32bit APB Control Interface to ADC01separately.

-  32bit APB Control Interface to ADC23 and DAC01separately.

-  Programmable gain setting and soft mute control in digital part

-  | Programmable ALC Loop / Noise Gate setting in ADC path
   | Programmable ADC High Pass Filter (wind noise reduction included)
   | Programmable ADC Notch Filter is selectable.

-  Two stereo digital Microphone support for ADC01and ADC23.

-  Output Gain/Volume and mute control

DVP
---

-  Designed as an AHB Master component that can access the memory without DMAC service

-  Image frame complete notice and buffer switching

-  Support separate components 4:2:2 output format in line buffer for JPEG encoding.

IWDG
----

-  Clocked from an internal 32 KHz low speed oscillator or from 32768Hz crystal if avalilable

-  32-bit free running counter

-  Selectable timer-out interval

UART
----

-  Four UART interface(1 for debug)

-  Three UART Support the hardware flow control (CTS/RTS) so that WIFI can be supported through UART interface.

-  UART0-UART2 Supports the hardware handshake for DMA.

-  Up to 3Mb/s baudrate settting

SPI
---

-  Three SPI interfaces

-  Maxim 50Mb/s for master mode

-  Maxim 25Mb/s for slave mode

-  One spi of QSPI function must be used for embedded nor flash or external flash

-  Supports the master mode and the slave mode.

-  Supports memory mapped access (read-only) through AHB bus.

-  Supports the hardware handshake for DMA.

-  Supports the dual I/O and quad I/O modes(QSPI).

I2C
---

-  Two I2C interface is available.

-  Programmable to be a master or a slave device.

-  Programmable clock/data timing.

-  Supports the I2C-bus Standard-mode (100 kb/s), Fast-mode (400 kb/s) and Fast-mode plus (1 Mb/s).

-  Supports the hardware handshake for DMA.

-  Supports the master-transmit, master-receive, slave-transmit and slave-receive modes.

-  Supports the multi-master mode.

-  Supports 7-bit and 10-bit addressing.

-  Supports general call addressing.

-  Supports auto clock stretch.

RTC
---

-  Supports software compensation by setting frequency compensate register

-  The frequency of clock source (before the clock divider) for the counter is 32.768KHz.

-  Separate second, minute, hour and day counters.

-  Periodic interrupts: half-second, second, minute, hour and day interrupts.

-  Programmable alarm interrupt with specified second, minute and hour numbers.

NPU
---

-  Matrix and vector operation accelerator

-  AHB master interface for data read and write

-  APB interface for register configuration

-  Has interrupt signals

-  Support reverse order storage, overflow detection, shift location

FCC RAM Controller
------------------

-  Maxim 200MHz

-  Arbitrate the data access request from CPU, HIFI4, NPU and DMAC

-  Partition the NPU memory into several spaces

-  If the access from different agents are in different spaces, all of them can be done without wait

-  Flexible priority setting: If the accesses from different agents are in the same space, the priority can be set be user through register.

PDM2PCM
-------

-  Support data conversion of PDM data from digital microphone to standard PCM data

-  CIC filter in always on domain, half-band and memory in main power domain

CRYPTO
------

-  Support inside chip AES128 + SHA256 for secure communication

-  AHB master interface for data read and write

-  APB interface for register configuration

EFUSE Controller
----------------

-  Read EFuse content after receiving reset release signal from the reset sequence control

-  Provide the data to Crypto engine for encryption/decryption usage

-  Provide the data to QSPI encrypt wrapper to protect the content of NOR flash

True Random Number Generator
----------------------------

-  True random generator with mixed analog digital implementation to provide true random number

-  Register configuration and generated random number can be accessed through APB bus

I2S Interface
-------------

-  Support extended microphone inputs

-  Support I2S audio inputs and outputs

-  3 independent I2S modules

-  Input or output signal can be TDM extended

-  Register configuration and data operation through APB bus

USB1.1 Full Speed Device
------------------------

-  One set of USB 1.1 FS Device 12 Mbps

-  On-chip USB Transceiver

-  Supports Control, ISO in/out, Bulk in/out, Interrupt in/out transfers

-  Provides 8 programmable endpoints

-  Supports maximum 1K Bytes for isochronous transfer and maximum 64 Bytes for Bulk and interrupt transfer

-  Each endpoint is configurable

SDIO
----

-  Maxim 25MHz output clock

-  Compliant with SD host controller standard specification, version 3.0

-  Supports both DMA and non-DMA data transfers

-  Compliant with SD physical layer specification, version 3.0

-  Supports UHS50/UHS104 SD cards

-  Supports configurable SD bus modes: 4-bit mode and 8-bit mode

-  Compliant with SDIO card specification, version 3.0

-  Compliant with eMMC card specification, version 5.1 mandatory part

-  Supports configurable 1-bit/4-bit SD card bus and 1-bit/4-bit/8-bit EMMC card bus

-  Configurable CPRM function for security

-  Built-in generation and check for 7-bit and 16-bit CRC data

-  Card detection (Insertion/Removal)

Power Management Unit
---------------------

-  Supports Sleep mode to reduce power consumption

-  Supports the wake up through RTC, timer and Key-in from IO

-  Supports the wake up through VAD

-  Supports system wakeup through touch

Touch
-----

-  Supports touch point detection

Audio ADC&DMIC&I2S
------------------

-  Audio ADC shares the internal memory with DMIC and I2S. For the restrictions on combination use, refer to :ref:`Table 4-1 <Table4-1>` .

.. _Table4-1:

.. table:: **Table 4-1 Restrictions on Combination Use**

   +----------------+----------------+----------------+----------------+
   | Occupied       | Available I2S  | Available DMIC | Description    |
   | ADC/DAC        |                |                |                |
   +================+================+================+================+
   | ADC01 only, no | I2S1, I2S2     | DMIC2, DMIC3   |                |
   | DAC            |                |                |                |
   +----------------+----------------+----------------+----------------+
   | ADC23 only, no | I2S0, I2S1 or  | DMIC0, DMIC1   | I2S1 or I2S2   |
   | DAC            | I2S2           |                | (either-or)    |
   +----------------+----------------+----------------+----------------+
   | ADC01+ADC23,   | I2S1 or I2S2   | None           | I2S1 or I2S2   |
   | no DAC         |                |                | (either-or)    |
   +----------------+----------------+----------------+----------------+
   | ADC01 only,    | I2S0, I2S2(IN) | DMIC2, DMIC3   | I2S2(IN)       |
   | with DAC       |                |                |                |
   +----------------+----------------+----------------+----------------+
   | ADC23 only,    | I2S0, I2S1 or  | DMIC0, DMIC1   | I2S1 or        |
   | with DAC       | I2S2(IN)       |                | I2S2(IN)       |
   |                |                |                | (either-or)    |
   +----------------+----------------+----------------+----------------+
   | ADC01+ADC23,   | I2S1 or        | None           | I2S1 or        |
   | with DAC       | I2S2(IN)       |                | I2S2(IN)       |
   |                |                |                | (either-or)    |
   +----------------+----------------+----------------+----------------+

Boot Mode
---------

For descriptions of GPIOB0 and GPIOB1 the boot modes, refer to :ref:`Table 4-2 <Table4-2>` .

.. _Table4-2:

.. table:: **Table 4-2 Boot Mode**
    :widths: 20 20 40

    +--------+---------+-------------------+
    | GPIOB0 | GPIOB1  | Mode Description  |
    +========+=========+===================+
    | 1      | 1       | Nor Flash boot    |
    +--------+---------+-------------------+
    | 1      | 0       | UART              |
    +--------+---------+-------------------+
    | 0      | 1       | Reserved          |
    +--------+---------+-------------------+
    | 0      | 0       | DSP boot only     |
    +--------+---------+-------------------+


.. table:: **Table 4-2 Boot Mode**
    :widths: 40 40 60

    +--------+---------+-------------------+
    | GPIOB0 | GPIOB1  | Mode Description  |
    +========+=========+===================+
    | 1      | 1       | Nor Flash boot    |
    +--------+---------+-------------------+
    | 1      | 0       | UART              |
    +--------+---------+-------------------+
    | 0      | 1       | Reserved          |
    +--------+---------+-------------------+
    | 0      | 0       | DSP boot only     |
    +--------+---------+-------------------+


.. table:: Table 4-2 Boot Mode (grid)
    :widths: grid

    +--------+---------+-------------------+
    | GPIOB0 | GPIOB1  | Mode Description  |
    +========+=========+===================+
    | 1      | 1       | Nor Flash boot    |
    +--------+---------+-------------------+
    | 1      | 0       | UART              |
    +--------+---------+-------------------+
    | 0      | 1       | Reserved          |
    +--------+---------+-------------------+
    | 0      | 0       | DSP boot only     |
    +--------+---------+-------------------+


.. table:: Table 4-2 Boot Mode (grid)
   :widths: grid

   ====== ====== ================
   GPIOB0 GPIOB1 Mode Description
   ====== ====== ================
   1      1      Nor Flash boot
   1      0      UART
   0      1      Reserved
   0      0      DSP boot only
   ====== ====== ================

-  GPIOA15(RXD) & GPIOA18(TXD) are configured as UART function in uart boot mode

.. table:: Table 4-3 Boot Mode1
   :widths: auto

   ====== ====== ================
   GPIOB0 GPIOB1 Mode Description
   ====== ====== ================
   1      1      Nor Flash boot
   1      0      UART
   0      1      Reserved
   0      0      DSP boot only
   ====== ====== ================

Electrical Characteristics
==========================

Parameter Conditions
--------------------

Unless otherwise specified, all voltages are referenced to VSS.

Minimum and Maximum Values
~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless otherwise specified the minimum and maximum values are guaranteed
in the worst conditions of ambient temperature, supply voltage and
frequencies by tests in production on 100% of the devices with an
ambient temperature at 25 °C and max temperature in the range.

Data based on characterization results, design simulation and/or
technology characteristics are indicated in the table footnotes and are
not tested in production. Based on characterization, the minimum and
maximum values refer to sample tests and represent the mean value plus
or minus three times the standard deviation (mean ± 3σ).

Typical Values
~~~~~~~~~~~~~~

Unless otherwise specified, typical data are based on T\ :sub:`A` = 25 °C, V\ :sub:`CCIN`
= 5 V (for the 2.7 V ≤ V\ :sub:`CCIN` ≤ 5 V voltage range). They are given only
as design guidelines and are not tested.

Loading Capacitor
~~~~~~~~~~~~~~~~~

The loading capacitor used for pin parameter measurement is 10pf.

Pin Input Voltage
~~~~~~~~~~~~~~~~~

The input voltage measurement on a pin of the device is through current
source device.

Operating Conditions
--------------------

Absolute Maximum Ratings
~~~~~~~~~~~~~~~~~~~~~~~~

For information about voltage characteristics, refer to :ref:`Table 5‑1 <Table5-1>` .

.. _Table5-1:

.. table:: **Table 5‑1 Voltage Characteristics**
    :widths: grid

    +-------------------------------+------------------------+------+-----+------+
    | Symbol                        | Ratings                | Min  | Max | Unit |
    +===============================+========================+======+=====+======+
    | V\ :sub:`CCIN`-V\ :sub:`SS`   | External supply        | -0.3 | 5.5 | V    |
    |                               | voltage                |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IL`                  | Input Low Voltage on   | -0.3 | 0.8 | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IH`                  | Input High Voltage on  | 2    | 5.5 | V    |
    |                               | signal pin(PortA)      |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IH`                  | Input High Voltage on  | 2    | 3.6 | V    |
    |                               | signal pin(PortB)      |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OL`                  | Output Low Voltage on  |      | 0.4 | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OH`                  | Output High Voltage on | 2.4  |     | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+


I/O Port Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~

For information about I/O Static characteristics, refer to :ref:`Table 5‑2 <Table5-2>` .

.. _Table5-2:

.. table:: **Table 5‑2 I/O Static Characteristics**

   +-------------+-------------+-------------------+------+-----+------+------+
   | Symbol      | Parameter   | Conditions        | Min  | Typ | Max  | Unit |
   +=============+=============+===================+======+=====+======+======+
   | V           | Standard IO | 2.7V ≤            | -0.3 |     | 0.8  | V    |
   | \ :sub:`IL` | Input low   | V\ :sub:`CCIN`    |      |     |      |      |
   |             | level       | ≤ 5.5V            |      |     |      |      |
   |             | voltage     |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | V           | Standard IO | 2.7V ≤            | 2    |     | 5.5  | V    |
   | \ :sub:`IH` | input high  | V\ :sub:`CCIN`    |      |     |      |      |
   |             | level       | ≤ 5.5V            |      |     |      |      |
   |             | vol         |                   |      |     |      |      |
   |             | tage(PortA) | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | V           | Standard IO | 2.7V ≤            | 2    |     | 3.6  | V    |
   | \ :sub:`IH` | input high  | V\ :sub:`CCIN`    |      |     |      |      |
   |             | level       | ≤ 5.5V            |      |     |      |      |
   |             | vol         |                   |      |     |      |      |
   |             | tage(PortB) | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | V           | Standard IO | 2.7V ≤            |      | 220 |      | mV   |
   | \ :sub:`hys`| Schmitt     | V\ :sub:`CCIN`    |      |     |      |      |
   |             | trigger     | ≤ 5.5V            |      |     |      |      |
   |             | voltage     |                   |      |     |      |      |
   |             | hysteresis  | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | V           | Output Low  | 2.7V ≤            |      |     | 0.4  | V    |
   | \ :sub:`OL` | Voltage     | V\ :sub:`CCIN`    |      |     |      |      |
   |             |             | ≤ 5.5V            |      |     |      |      |
   |             |             |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | V           | Output High | 2.7V ≤            | 2.4  |     |      | V    |
   | \ :sub:`OH` | Voltage     | V\ :sub:`CCIN`    |      |     |      |      |
   |             |             | ≤ 5.5V            |      |     |      |      |
   |             |             |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | I           | Low Level   | 2.7V ≤            |      | 15  |      | mA   |
   | \ :sub:`OL` | Output      | V\ :sub:`CCIN`    |      |     |      |      |
   |             | Current     | ≤ 5.5V            |      |     |      |      |
   |             |             |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | I           | High Level  | 2.7V ≤            |      | 22  |      | mA   |
   | \ :sub:`OH` | Output      | V\ :sub:`CCIN`    |      |     |      |      |
   |             | Current     | ≤ 5.5V            |      |     |      |      |
   |             |             |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | I           | Input       | 2.7V ≤            |      | 1   |      | uA   |
   | \ :sub:`Ikg`| leakage     | V\ :sub:`CCIN`    |      |     |      |      |
   |             | current     | ≤ 5.5V            |      |     |      |      |
   |             |             |                   |      |     |      |      |
   |             |             | T\ :sub:`A`\      |      |     |      |      |
   |             |             | =25°C             |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | R           | Pull up     |                   | 74k  | 80k | 158k | Ω    |
   | \ :sub:`PU` | equivalent  |                   |      |     |      |      |
   |             | resistor    |                   |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | R           | Pull down   |                   | 62k  | 75k | 203k | Ω    |
   | \ :sub:`PD` | equivalent  |                   |      |     |      |      |
   |             | resistor    |                   |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+
   | C           | I/O pin     |                   |      | 5   |      | pF   |
   | \ :sub:`IO` | capacitance |                   |      |     |      |      |
   +-------------+-------------+-------------------+------+-----+------+------+

.. Note::
   Only PORT A is 5V tolerance IO, and the input voltage can be 5.5V maximumly.

IO AC Characteristics
~~~~~~~~~~~~~~~~~~~~~

For information about I/O AC characteristics, refer to :ref:`Table 5‑3 <Table5-3>` .

.. _Table5-3:

.. table:: **Table 5‑3 IO AC Characteristics**
   :widths: grid

   +---------------------+--------------+--------------------+-----+-----+-----+------+
   | Symbol              | Parameter    | Conditions         | Min | Typ | Max | Unit |
   +=====================+==============+====================+=====+=====+=====+======+
   | F                   | Maximum      | 2.7V ≤             |     | 100 |     | MHz  |
   | \ :sub:`max(io)out` | frequency    | V\ :sub:`CCIN`     |     |     |     |      |
   |                     |              | ≤ 5.5V             |     |     |     |      |
   |                     |              |                    |     |     |     |      |
   |                     |              | T\ :sub:`A`\       |     |     |     |      |
   |                     |              | =25°C,             |     |     |     |      |
   |                     |              | C\ :sub:`L`\ =10pf |     |     |     |      |
   +---------------------+--------------+--------------------+-----+-----+-----+------+
   | T                   | Output high  | 2.7V ≤             |     | 2.5 |     | ns   |
   | \ :sub:`f(IO)out`   | to low level | V\ :sub:`CCIN`     |     |     |     |      |
   |                     | fall time    | ≤ 5.5V             |     |     |     |      |
   |                     | and output   |                    |     |     |     |      |
   |                     | low to high  | T\ :sub:`A`\       |     |     |     |      |
   |                     | level rise   | =25°C,             |     |     |     |      |
   |                     | time         | C\ :sub:`L`\ =10pf |     |     |     |      |
   +                     +              +--------------------+-----+-----+-----+------+
   |                     |              | 2.7V ≤             |     | 2.5 |     | ns   |
   |                     |              | V\ :sub:`CCIN`     |     |     |     |      |
   |                     |              | ≤ 5.5V             |     |     |     |      |
   |                     |              |                    |     |     |     |      |
   |                     |              | T\ :sub:`A`\       |     |     |     |      |
   |                     |              | =25°C,             |     |     |     |      |
   |                     |              | C\ :sub:`L`\ =10pf |     |     |     |      |
   +---------------------+--------------+--------------------+-----+-----+-----+------+

nRESET Pin Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about nRESET pin characteristics, refer to :ref:`Table 5‑4 <Table5-4>` .

.. _Table5-4:

.. table:: **Table 5‑4 nRESET Pin Characteristics**
   :widths: grid

   +-------------------+-------------------+----------------+-----+-----+-----+------+
   | Symbol            | Parameter         | Conditions     | Min | Typ | Max | Unit |
   +===================+===================+================+=====+=====+=====+======+
   | R\ :sub:`PU`      | Pull up           | 2.7V ≤         |     | 80k |     | Ω    |
   |                   | equivalent        | V\ :sub:`CCIN` |     |     |     |      |
   |                   | resistor          | ≤ 5.5V         |     |     |     |      |
   |                   |                   |                |     |     |     |      |
   |                   |                   | T\ :sub:`A`\   |     |     |     |      |
   |                   |                   | =25°C          |     |     |     |      |
   +-------------------+-------------------+----------------+-----+-----+-----+------+
   | V                 | nRESET input      | 2.7V ≤         |     | 1   |     | ms   |
   | \ :sub:`(nRESET)` | pulse             | V\ :sub:`CCIN` |     |     |     |      |
   |                   |                   | ≤ 5.5V         |     |     |     |      |
   |                   |                   |                |     |     |     |      |
   |                   |                   | T\ :sub:`A`\   |     |     |     |      |
   |                   |                   | =25°C,         |     |     |     |      |
   |                   |                   | C\ :sub:`L`\   |     |     |     |      |
   |                   |                   | =10pf          |     |     |     |      |
   +-------------------+-------------------+----------------+-----+-----+-----+------+

Supply Current Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about supply current characteristics, refer to :ref:`Table 5‑5 <Table5-5>` .

.. _Table5-5:

.. table:: **Table 5‑5 Supply Current Characteristics**
   :widths: grid

   +-----------+-----------+----------------+------------------+---------+------+
   | Symbol    | Parameter | Conditions     | f                | Typical | Unit |
   |           |           |                | \ :sub:`sysclk`\ |         |      |
   |           |           |                | (MHz)            |         |      |
   +===========+===========+================+==================+=========+======+
   | I\        | Supply    | V\ :sub:`CCIN` | 100              | 20      | mA   |
   | :sub:`DD` | current   | = 5V,          |                  |         |      |
   |           | in RUN    | External       |                  |         |      |
   |           | mode      | 24MHz          |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | T              |                  |         |      |
   |           |           | \ :sub:`A`\    |                  |         |      |
   |           |           | =25°C,         |                  |         |      |
   |           |           | PLL ON,        |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | AP ON, CP      |                  |         |      |
   |           |           | ON,NPU ON      |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | PSRAM          |                  |         |      |
   |           |           | off, nor       |                  |         |      |
   |           |           | flash          |                  |         |      |
   |           |           | cached         |                  |         |      |
   |           +-----------+----------------+------------------+---------+------+
   |           | Supply    | T              | 24               | 1.8     | mA   |
   |           | current   | \ :sub:`A`\ =  |                  |         |      |
   |           | in        | 25°C, deep     |                  |         |      |
   |           | VAD&      | sleep          |                  |         |      |
   |           | DEEPSLEEP | mode           |                  |         |      |
   |           | mode      | entered,       |                  |         |      |
   |           |           | VAD mode       |                  |         |      |
   |           |           | enabled        |                  |         |      |
   |           |           | with 1         |                  |         |      |
   |           |           | audio ADC      |                  |         |      |
   |           |           | on(analog      |                  |         |      |
   |           |           | mic not        |                  |         |      |
   |           |           | included)      |                  |         |      |
   |           +-----------+----------------+------------------+---------+------+
   |           | Supply    | T              | 24               | 700     | uA   |
   |           | current   | \ :sub:`A`\ =  |                  |         |      |
   |           | in        | 25°C, deep     |                  |         |      |
   |           | DEEPSLEEP | sleep          |                  |         |      |
   |           | mode      | mode           |                  |         |      |
   |           |           | entered        |                  |         |      |
   +-----------+-----------+----------------+------------------+---------+------+

Wakeup Time from Sleep Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about wakeup time from sleep modes, refer to :ref:`Table 5‑6 <Table5-6>` .

.. _Table5-6:

.. table:: **Table 5‑6 Wakeup Time from Sleep Modes**
   :widths: grid

   +-------------------+----------------+----------------+---------+------+
   | Symbol            | Parameter      | Conditions     | Typical | Unit |
   +===================+================+================+=========+======+
   | t\ :sub:`WUSLEEP` | Wakeup from    | External pin   | <2      | ms   |
   |                   | Sleep          | wakeup (ROM    |         |      |
   |                   |                | boot not       |         |      |
   |                   |                | included)      |         |      |
   +-------------------+----------------+----------------+---------+------+

External Clock Source Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about external clock source characteristics, refer to :ref:`Table 5‑7 <Table5-7>` .

.. _Table5-7:

.. table:: **Table 5‑7 External Clock Source Characteristics**
   :widths: grid

   +------------------+--------------+------------+-----+-----+-----+------+
   | Symbol           | Parameter    | Conditions | Min | Typ | Max | Unit |
   +==================+==============+============+=====+=====+=====+======+
   | f                | External     |            |     | 24  |     | MHz  |
   | \ :sub:`osc`     | clock source |            |     |     |     |      |
   |                  | frequency    |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+
   | V                | OSC IN input |            |     | 3.3 |     | V    |
   | \ :sub:`OSCH`    | pin high     |            |     |     |     |      |
   |                  | level        |            |     |     |     |      |
   |                  | voltage      |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+
   | V                | OSC IN input |            |     | 0   |     | V    |
   | \ :sub:`OSCL`    | pin low      |            |     |     |     |      |
   |                  | level        |            |     |     |     |      |
   |                  | voltage      |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+
   | C                | OSC IN input |            |     | 5   |     | pF   |
   | \ :sub:`IN(OSC)` | capacitance  |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+
   | Ducy             | Duty cycle   |            | 45  |     | 55  | %    |
   | \ :sub:`(OSC)`   |              |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+
   | I\ :sub:`L`      | OSC IN input |            |     | 430 |     | uA   |
   |                  | leakage      |            |     |     |     |      |
   |                  | current      |            |     |     |     |      |
   +------------------+--------------+------------+-----+-----+-----+------+

Internal Clock Source Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about internal clock source characteristics, refer to :ref:`Table 5‑8 <Table5-8>` .

.. _Table5-8:

.. table:: **Table 5‑8 Internal Clock Source Characteristics**
   :widths: grid

   +-------------------+--------------+----------------+-----+-----+-----+------+
   | Symbol            | Parameter    | Conditions     | Min | Typ | Max | Unit |
   +===================+==============+================+=====+=====+=====+======+
   | f\ :sub:`LSI`     | Frequency    | 2.7V ≤         |     | 32  |     | KHz  |
   |                   |              | V\ :sub:`CCIN` |     |     |     |      |
   |                   |              | ≤ 5.5V         |     |     |     |      |
   |                   |              |                |     |     |     |      |
   |                   |              | T\ :sub:`A`\   |     |     |     |      |
   |                   |              | =25°C          |     |     |     |      |
   +-------------------+--------------+----------------+-----+-----+-----+------+
   | t\ :sub:`su(LSI)` | LSI          | 2.7V ≤         |     | 5   |     | s    |
   |                   | oscillator   | V\ :sub:`CCIN` |     |     |     |      |
   |                   | startup time | ≤ 5.5V         |     |     |     |      |
   |                   |              |                |     |     |     |      |
   |                   |              | T\ :sub:`A`\   |     |     |     |      |
   |                   |              | =25°C          |     |     |     |      |
   +-------------------+--------------+----------------+-----+-----+-----+------+
   | I\ :sub:`DD(LSI)` | LSI          | 2.7V ≤         |     |     | 1   | uA   |
   |                   | oscillator   | V\ :sub:`CCIN` |     |     |     |      |
   |                   | power        | ≤ 5.5V         |     |     |     |      |
   |                   | consumption  |                |     |     |     |      |
   |                   |              | T\ :sub:`A`\   |     |     |     |      |
   |                   |              | =25°C          |     |     |     |      |
   +-------------------+--------------+----------------+-----+-----+-----+------+

PLL Characteristics
~~~~~~~~~~~~~~~~~~~

For information about PLL characteristics, refer to :ref:`Table 5‑9 <Table5-9>` .

.. _Table5-9:

.. table:: **Table 5‑9 PLL Characteristics**
   :widths: grid

   ================= ===================== ========== === === === ====
   Symbol            Parameter             Conditions Min Typ Max Unit
   ================= ===================== ========== === === === ====
   f\ :sub:`PLL_IN`  PLL input clock                      24      MHz
   f\ :sub:`PLL_OUT` PLL output clock                     300     MHz
   Jitter            Cycle-to cycle jitter                10      ps
   ================= ===================== ========== === === === ====

EMC
~~~

For information about Electromagnetic Compatibility (EMC), refer to :ref:`Table 5‑10 <Table5-10>` .

.. _Table5-10:

.. table:: **Table 5‑10 EMC??**
   :widths: grid

   +-----------+-----------+-------------+-------+-----------+------+
   | Symbol    | Ratings   | Conditions  | Class | Maximum   | Unit |
   |           |           |             |       | Value     |      |
   +===========+===========+=============+=======+===========+======+
   | VESD(HBM) | Elec      | T\ :sub:`A` | 2     | 2000      | V    |
   |           | trostatic | = 25°C      |       |           |      |
   |           | discharge |             |       |           |      |
   |           | voltage   |             |       |           |      |
   |           | (human    |             |       |           |      |
   |           | body      |             |       |           |      |
   |           | model)    |             |       |           |      |
   +-----------+-----------+-------------+-------+-----------+------+
   | VESD(CDM) | Elec      | T\ :sub:`A` |       | 1000      | V    |
   |           | trostatic | = 25°C      |       |           |      |
   |           | discharge |             |       |           |      |
   |           | voltage   |             |       |           |      |
   |           |           |             |       |           |      |
   |           | (charge   |             |       |           |      |
   |           | device    |             |       |           |      |
   |           | model)    |             |       |           |      |
   +-----------+-----------+-------------+-------+-----------+------+

Package Information
===================

QFN64 (8*8mm) Package information
-----------------------------------

For the package information, see :ref:`Figure 6-1 <6-1>` , :ref:`Figure 6-2 <6-2>` , and :ref:`Figure 6-3 <6-3>` .

.. _6-1:

.. figure:: datasheet_figure/6-1_Top_View.png
   :scale: 50%
   :align: center

   **Figure 6‑1 Top View**

.. _6-2:

.. figure:: datasheet_figure/6-2_Bottom_View.png
   :scale: 50%
   :align: center

   **Figure 6‑2 Bottom View**

Figure 6‑2 Bottom View

.. _6-3:

.. figure:: datasheet_figure/6-3.png
   :scale: 50%
   :align: center

   **Figure 6‑3 Symbol Dimension**

Thermal Characteristics
-----------------------

The maximum chip-junction temperature, T\ :sub:`J` max, in degrees
Celsius, can be calculated using the following equation:

T\ :sub:`J` max = T\ :sub:`A` max + (P\ :sub:`D` max x θ\ :sub:`JA`)

where:

-  T\ :sub:`A` max is the maximum ambient temperature in °C,

-  θ\ :sub:`JA` is the package junction-to-ambient thermal resistance,
   in °C/W,

-  P\ :sub:`D` max is the sum of P\ :sub:`INT` max and P\ :sub:`I/O` max
   (P\ :sub:`D` max = P\ :sub:`INT` max + P\ :sub:`I/O`\ max),

-  P\ :sub:`INT` max is the product of I\ :sub:`DD` and V\ :sub:`DD`,
   expressed in Watts. This is the maximum chip internal power.

P\ :sub:`I/O` max represents the maximum power dissipation on output
pins where:

P\ :sub:`I/O` max = ∑(V\ :sub:`OL` × I\ :sub:`OL`) + ((V\ :sub:`DD` –
V\ :sub:`OH`) × I\ :sub:`OH`),

taking into account the actual V\ :sub:`OL`/I\ :sub:`OL` and V\ :sub:`OH`/I\ :sub:`OH` of the I/Os at
low and high level in the application.

.. _Table6-1:

.. table:: **Table 6‑1 Package Thermal Characteristics**
   :widths: grid

   +--------------+-----------------------------------------+----------------+-------+
   | Symbol       | Parameter                               | Value          | Unit  |
   +==============+=========================================+================+=======+
   | θ\ :sub:`JA` | **Thermal resistance junction-ambient** | 28             | °C/W  |
   |              |                                         |                |       |
   |              | **QFN64 – 8*8 mm**                      |                |       |
   +--------------+-----------------------------------------+----------------+-------+
   | TSTG         |    Storage temperature range            |    –65 to +150 | °C    |
   +--------------+-----------------------------------------+----------------+-------+
   | TJ           |    Maximum junction temperature         |    125         | °C    |
   +--------------+-----------------------------------------+----------------+-------+

Reflow Profile
==============

Reflow Graph
------------

For the reflow graph, see :ref:`Figure 7-1 <7-1>` .

.. _7-1:

.. figure:: datasheet_figure/7-1_Reflow_Graph.png
   :scale: 50%
   :align: center

   **Figure 7‑1 Reflow Graph**

SMT Reflow Condition
--------------------

.. _Table7-1:

.. table:: **Table 7‑1 Title?**
   :widths: grid

   +----------------------------------+----------------------------------+
   | **Parameter**                    | **Requirement**                  |
   +==================================+==================================+
   | N2 purge reflow usage            | Yes                              |
   +----------------------------------+----------------------------------+
   | O2 ppm level                     | <1500 ppm                        |
   +----------------------------------+----------------------------------+
   | Temperature Min (T\ :sub:`smin`) | 150°C                            |
   +----------------------------------+----------------------------------+
   | Temperature Max (T\ :sub:`smax`) | 200°C                            |
   +----------------------------------+----------------------------------+
   | Time                             | 60-120 seconds                   |
   | (t\ :sub:`s`)from(T\ :sub:`smin` |                                  |
   | to T\ :sub:`smax`)               |                                  |
   +----------------------------------+----------------------------------+
   | Ramp-up rate (T\ :sub:`L` to     | 3°C/second max                   |
   | T\ :sub:`P`)                     |                                  |
   +----------------------------------+----------------------------------+
   | Liquidous                        | 217°C                            |
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
   | Time(t\ :sub:`p`)within 5°C of   | 30 seconds max                   |
   | the specified classification     |                                  |
   | temperature (T\ :sub:`C`)        |                                  |
   +----------------------------------+----------------------------------+
   | Ramp-down rate (T\ :sub:`P` to   | 6°C/second max                   |
   | T\ :sub:`L`)                     |                                  |
   +----------------------------------+----------------------------------+
   | Time 25°C to peak temperature    | 8 minutes max                    | 
   +----------------------------------+----------------------------------+

.. _Table7-2:

.. table:: **Table 7‑2 Title?？**
   :widths: grid

   +----------------+----------------+----------------+----------------+
   | **Package      | **Volume mm3   | **Volume mm3   | **Volume mm3   |
   | Thickness**    | <350**         | 350-2000**     | >2000**        |
   +================+================+================+================+
   | <1.6mm         | 260°C          | 260°C          | 260°C          |
   +----------------+----------------+----------------+----------------+
   | 1.6mm-2.5mm    | 260°C          | 250°C          | 245°C          |
   +----------------+----------------+----------------+----------------+
   | >2.5mm         | 250°C          | 245°C          | 245°C          |
   +----------------+----------------+----------------+----------------+

Weight
======

The SoC weighs 200mg.

Application Diagram
===================
For the application diagram, see :ref:`Figure 9-1 <9-1>` .

.. _9-1:

.. figure:: datasheet_figure/9-1_Application_Diagram.png
   :scale: 100%
   :align: center

   **Figure 9‑1 Application Diagram**



