Overview
==============

The CSK6 serial is a dual-core microcontroller embedded with an ARM STAR core and
a HiFi4 core. The ARM Star core is designed for 32-bit microcontroller
applications, offering high performance, low power, simple instruction set
and addressing together with reduced code size compared to exiting
solutions. The HiFi4 core is designed for audio coders and decoders such as MP3,
AAC, and FLAC. The independent NPU is designed for neural network operation.

The CSK6 serial applies for smart home appliances.

The CSK6 serial can operate up to 300 MHz. Thus it can afford to support a
variety of industrial control and applications that requires high CPU
performance. The CSK6 serial has an internal 1-MB data SRAM.

Many system-level peripheral functions, such as IO port, DVP, timer,
watchdog timer, UART, SPI, I2C, DMA, PLL, USB1.1 (full speed), RTC, and SDIO
are supported.

Block Diagrams
==============

For the block diagrams, see :ref:`Fig. 2.1 <2-1>`.

.. _2-1:

.. figure:: datasheet_figure/2-1_Block_Diagram.png
   :scale: 25%
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
   :scale: 100%
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
   | 22             | XTAL_OUT           | 24 MHz crystal               |
   +----------------+--------------------+------------------------------+
   | 23             | XTAL_IN            | 24 MHz crystal               |
   +----------------+--------------------+------------------------------+
   | 24             | VAD_AON            | Internal LDO output. 1 μF    |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 25             | VCC                | Power input: 2.7 V-5.5 V     |
   +----------------+--------------------+------------------------------+
   | 26             | VDD_IO             | Internal LDO output, 4.7 μF  |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 27             | AVSS_AUD           | GND                          |
   +----------------+--------------------+------------------------------+
   | 28             | AVDD_AUD           | Internal LDO output, 2.2 μF  |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 29             | VREF               | Audio codec reference input  |
   +----------------+--------------------+------------------------------+
   | 30             | VMID               | Internal LDO output, 4.7 μF  |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 31             | MICBIAS0           | Mic bias output, Cload=2.2 μF|
   +----------------+--------------------+------------------------------+
   | 32             | MICBIAS1           | Mic bias output, Cload=2.2 μF|
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
   | 45             | VDD_CORE           | internal LDO output, 4.7 μF  |
   |                |                    | cap recommended, should      |
   |                |                    | connect with VDD_CORE_2      |
   +----------------+--------------------+------------------------------+
   | 46             | VDD_IO2            | Internal DC-DC input, 10 μF  |
   |                |                    | cap recommended              |
   +----------------+--------------------+------------------------------+
   | 47             | VBK_PVSS           | DC-DC GND                    |
   +----------------+--------------------+------------------------------+
   | 48             | VBK_SW             | DC-DC switch out, 3.3 μH     |
   |                |                    | inductor connected           |
   +----------------+--------------------+------------------------------+
   | 49             | VBK_IN             | DC-DC input power:           |
   |                |                    | 2.7 V-5.5 V                  |           
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
   The pull up resister is configured as 80 K. 

Functions
===============

Core
----

-  The ARM STAR&HiFi4 dual-core operates up to 300 MHz.

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

The multi-function timer provides the following 6 usage scenarios
depending on the configuration of the channel mode register bit. The maximum
output frequency of the PWM is 50 MHz.

-  | Timer mode
   | Support 8/16/32-bit timers

-  | Input capture mode
   | The capture count mode is used to capture the number of input pulses and the capture time mode 
     is used to capture pulse width.

-  | PWM mode
   | PWM can be configured as central-aligned mode (see :ref:`Fig. 4.1 <4-1>`) and
     edge-aligned mode (see :ref:`Fig. 4.2 <4-2>`).

   .. _4-1:

   .. figure:: datasheet_figure/4-1_Center-Aligned_Mode.png
      :scale: 40%
      :align: center

      Center-Aligned Mode

   .. _4-2:

   .. figure:: datasheet_figure/4-2_Edge-Aligned_Mode.png
      :scale: 40 %

      Edge-Aligned Mode

-  LEDC output mode

SAR ADC
-------

-  12-bit resolution, up to 3 channels, up to 1 Msps, 24-MHz ADC clock

-  Configurable hardware ADC trigger sources

-  User configurable n-times ADC sampling

-  Dedicated ADC data FIFO for each ADC channel

-  Configurable ADC sampling duration

-  Configurable waiting time for the next round of A/D conversion

-  Switch on/off control

-  ADC trimming

-  ADC channel selection

-  External/internal VREF selection

-  | Real voltage caculation:
   | Reg\ :sub:`adc_value` = ADC register value
   | Voltage = (Reg\ :sub:`adc_value` - 2048)/2048*3.3

Audio Codec
-----------

-  Audio sample rates support 8 KHz to 96 KHz in the playback (DAC) path.

-  Audio sample rates support 8 KHz, 16 KHz, 44.1 KHz, or 48 KHz in the record (ADC) path.

-  | DAC SNR about 95 dB, THD -85 dB ('A'-weighted @ 8-48 ks/s).
   | ADC SNR about 95 dB, THD -85 dB ('A'-weighted @ 8-48 ks/s).

-  32-bit APB control interface to ADC01 separately.

-  32-bit APB control interface to ADC23 and DAC01 separately.

-  Programmable gain setting and soft mute control in the digital part.

-  | Programmable ALC loop/noise Gate setting in the ADC path.
   | Programmable ADC high-pass filter (wind noise reduction included).
   | The programmable ADC notch filter is selectable.

-  ADC01 and ADC23 support two stereo digital microphones.

-  Output gain/volume and mute control.

DVP
---

-  Designed as an AHB master component that can access the memory without any DMAC service.

-  Image frame completion notice and buffer switching.

-  Support separate components 4:2:2 output format in the line buffer for JPEG encoding.

IWDG
----

-  Clocked from an internal 32-KHz low-speed oscillator or from a 32768-Hz crystal if available.

-  32-bit free-running counter.

-  Selectable timer-out interval.

UART
----

-  Four UART interfaces (1 for debug).

-  Three UARTs support hardware flow control (CTS/RTS) so that WiFi can be supported through UART interfaces.

-  UART0 to UART2 support the hardware handshake for DMA.

-  Up to 3-Mb/s baudrate settting.

SPI
---

-  Three SPI interfaces.

-  Maximumly 50 Mb/s for the master mode.

-  Maximumly 25 Mb/s for the slave mode.

-  One SPI of QSPI function must be used for the embedded NOR flash or the external flash.

-  Supports the master mode and the slave mode.

-  Supports memory mapped access (read-only) through the AHB bus.

-  Supports the hardware handshake for DMA.

-  Supports the dual I/O and quad I/O modes (QSPI).

I2C
---

-  Two I2C interfaces are available.

-  Programmable to be a master or a slave device.

-  Programmable clock/data timing.

-  Supports the I2C-bus standard-mode (100 kb/s), fast-mode (400 kb/s), and fast-mode plus (1 Mb/s).

-  Supports the hardware handshake for DMA.

-  Supports the master-transmit, master-receive, slave-transmit and slave-receive modes.

-  Supports the multi-master mode.

-  Supports 7-bit and 10-bit addressing.

-  Supports general call addressing.

-  Supports auto clock stretch.

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

-  APB interface for register configuration

-  Has interrupt signals

-  Support reverse order storage, overflow detection, and location shift

FCC RAM Controller
------------------

-  200 MHz maximumly. 

-  Arbitrate the data access request from the CPU, HiFi4, NPU, and DMAC.

-  Partition the NPU memory into several spaces.

-  If the accesses from different agents are in different spaces, all of them can be done without immediately.

-  Flexible priority setting: If the accesses from different agents are in the same space, the priority can be set by users through the register.

PDM2PCM
-------

-  Support data conversion of PDM data from digital microphone to standard PCM data.

-  CIC filter in the always-on domain, half-band and memory in main power domain.

CRYPTO
------

-  Support inside chip AES128 + SHA256 for secure communication.

-  AHB master interface for data read and write.

-  APB interface for register configuration.

eFuse Controller
----------------

-  Read eFuse content after receiving reset release signal from the reset sequence control.

-  Provide data to Crypto engine for encryption/decryption.

-  Provide data to QSPI encryption wrapper to protect the content of the NOR flash.

True Random Number Generator
----------------------------

-  True random generator with mixed analog digital implementation to provide true random numbers.

-  Register configuration and generated random numbers can be accessed through the APB bus.

I2S Interface
-------------

-  Support extended microphone inputs.

-  Support I2S audio inputs and outputs.

-  3 independent I2S modules.

-  Input or output signal can be TDM extended.

-  Register configuration and data operation through the APB bus.

USB1.1 Full Speed Device
------------------------

-  One set of USB 1.1 FS Device 12 Mbps.

-  On-chip USB Transceiver.

-  Supports Control, ISO in/out, Bulk in/out, Interrupt in/out transfers.

-  Provides 8 programmable endpoints.

-  Supports maximum 1K Bytes for isochronous transfer and maximum 64 Bytes for Bulk and interrupt transfer.

-  Each endpoint is configurable.

SDIO
----

-  Maxim 25 MHz output clock

-  Compliant with SD host controller standard specification, version 3.0.

-  Supports both DMA and non-DMA data transfers.

-  Compliant with SD physical layer specification, version 3.0.

-  Supports UHS50/UHS104 SD cards.

-  Supports configurable SD bus modes: 4-bit mode and 8-bit mode.

-  Compliant with SDIO card specification, version 3.0.

-  Compliant with eMMC card specification, version 5.1 mandatory part.

-  Supports configurable 1-bit/4-bit SD card bus and 1-bit/4-bit/8-bit EMMC card bus.

-  Configurable CPRM function for security.

-  Built-in generation and check for 7-bit and 16-bit CRC data.

-  Card detection (Insertion/Removal).

Power Management Unit
---------------------

-  Supports Sleep mode to reduce power consumption.

-  Supports the wake up through RTC, timer and Key-in from IO.

-  Supports the wake up through VAD.

-  Supports system wakeup through touch.

Touch
-----

-  Supports touch point detection.

Audio ADC&DMIC&I2S
------------------

-  Audio ADC shares the internal memory with DMIC and I2S. For the restrictions on combination use, refer to :ref:`Table 4.1 <Table4-1>`.

.. _Table4-1:

.. table:: Restrictions on Combination Use

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

For descriptions of GPIOB0 and GPIOB1 the boot modes, refer to :ref:`Table 4.2 <Table4-2>`.

.. _Table4-2:

.. table:: Boot Mode
    :widths: grid

    +--------+---------+-------------------+
    | GPIOB0 | GPIOB1  | Mode Description  |
    +========+=========+===================+
    | 1      | 1       | NOR flash boot    |
    +--------+---------+-------------------+
    | 1      | 0       | UART              |
    +--------+---------+-------------------+
    | 0      | 1       | Reserved          |
    +--------+---------+-------------------+
    | 0      | 0       | DSP boot only     |
    +--------+---------+-------------------+


-  GPIOA15(RXD) & GPIOA18(TXD) are configured as UART function in the UART boot mode.



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
ambient temperature at 25 °C and the maximum temperature in the range.

Data based on characterization results, design simulation and/or
technology characteristics are indicated in the table footnotes and are
not tested in production. Based on characterization, the minimum and
maximum values refer to sample tests and represent the mean value plus
or minus three times the standard deviation (mean ± 3σ).

Typical Values
~~~~~~~~~~~~~~

Unless otherwise specified, typical data are based on T\ :sub:`A` = 25 °C, V\ :sub:`CCIN`
= 5 V (for the 2.7 V :math:`\leqslant` V\ :sub:`CCIN` :math:`\leqslant` 5 V voltage range). They are given only
as design guidelines and are not tested.

Loading Capacitor
~~~~~~~~~~~~~~~~~

The loading capacitor used for pin parameter measurement is 10 pf.

Pin Input Voltage
~~~~~~~~~~~~~~~~~

The input voltage measurement on a pin of the device is through current
source device.

Operating Conditions
--------------------

Absolute Maximum Ratings
~~~~~~~~~~~~~~~~~~~~~~~~

For information about voltage characteristics, refer to :ref:`Table 5.1 <Table5-1>`.

.. _Table5-1:

.. table:: Voltage Characteristics
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
    |                               | signal pin (PortA)     |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`IH`                  | Input High Voltage on  | 2    | 3.6 | V    |
    |                               | signal pin (PortB)     |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OL`                  | Output Low Voltage on  |      | 0.4 | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+
    | V\ :sub:`OH`                  | Output High Voltage on | 2.4  |     | V    |
    |                               | signal pin             |      |     |      |
    +-------------------------------+------------------------+------+-----+------+


I/O Port Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~

For information about I/O Static characteristics, refer to :ref:`Table 5.2 <Table5-2>`.

.. _Table5-2:

.. table:: I/O Static Characteristics

   +-------------+-------------+-------------------+------+------+-------+------+
   | Symbol      | Parameter   | Conditions        | Min  | Typ  | Max   | Unit |
   +=============+=============+===================+======+======+=======+======+
   | V           | Standard IO | 2.7 V ≤           | -0.3 |      | 0.8   | V    |
   | \ :sub:`IL` | Input low   | V\ :sub:`CCIN`    |      |      |       |      |
   |             | level       | ≤ 5.5 V           |      |      |       |      |
   |             | voltage     |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | V           | Standard IO | 2.7 V ≤           | 2    |      | 5.5   | V    |
   | \ :sub:`IH` | input high  | V\ :sub:`CCIN`    |      |      |       |      |
   |             | level       | ≤ 5.5 V           |      |      |       |      |
   |             | vol         |                   |      |      |       |      |
   |             | tage(PortA) | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | V           | Standard IO | 2.7 V ≤           | 2    |      | 3.6   | V    |
   | \ :sub:`IH` | input high  | V\ :sub:`CCIN`    |      |      |       |      |
   |             | level       | ≤ 5.5 V           |      |      |       |      |
   |             | vol         |                   |      |      |       |      |
   |             | tage(PortB) | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | V           | Standard IO | 2.7 V ≤           |      | 220  |       | mV   |
   | \ :sub:`hys`| Schmitt     | V\ :sub:`CCIN`    |      |      |       |      |
   |             | trigger     | ≤ 5.5 V           |      |      |       |      |
   |             | voltage     |                   |      |      |       |      |
   |             | hysteresis  | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | V           | Output Low  | 2.7 V ≤           |      |      | 0.4   | V    |
   | \ :sub:`OL` | Voltage     | V\ :sub:`CCIN`    |      |      |       |      |
   |             |             | ≤ 5.5 V           |      |      |       |      |
   |             |             |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | V           | Output High | 2.7 V ≤           | 2.4  |      |       | V    |
   | \ :sub:`OH` | Voltage     | V\ :sub:`CCIN`    |      |      |       |      |
   |             |             | ≤ 5.5 V           |      |      |       |      |
   |             |             |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | I           | Low Level   | 2.7 V ≤           |      | 15   |       | mA   |
   | \ :sub:`OL` | Output      | V\ :sub:`CCIN`    |      |      |       |      |
   |             | Current     | ≤ 5.5 V           |      |      |       |      |
   |             |             |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | I           | High Level  | 2.7 V ≤           |      | 22   |       | mA   |
   | \ :sub:`OH` | Output      | V\ :sub:`CCIN`    |      |      |       |      |
   |             | Current     | ≤ 5.5 V           |      |      |       |      |
   |             |             |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | I           | Input       | 2.7 V ≤           |      | 1    |       | uA   |
   | \ :sub:`Ikg`| leakage     | V\ :sub:`CCIN`    |      |      |       |      |
   |             | current     | ≤ 5.5 V           |      |      |       |      |
   |             |             |                   |      |      |       |      |
   |             |             | T\ :sub:`A`\      |      |      |       |      |
   |             |             | =25 °C            |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | R           | Pull up     |                   | 74 k | 80 k | 158 k | Ω    |
   | \ :sub:`PU` | equivalent  |                   |      |      |       |      |
   |             | resistor    |                   |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | R           | Pull down   |                   | 62 k | 75 k | 203 k | Ω    |
   | \ :sub:`PD` | equivalent  |                   |      |      |       |      |
   |             | resistor    |                   |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+
   | C           | I/O pin     |                   |      | 5    |       | pF   |
   | \ :sub:`IO` | capacitance |                   |      |      |       |      |
   +-------------+-------------+-------------------+------+------+-------+------+

.. Note::
   Only PORT A is 5V tolerance IO, and the input voltage can be 5.5V maximumly.

IO AC Characteristics
~~~~~~~~~~~~~~~~~~~~~

For information about I/O AC characteristics, refer to :ref:`Table 5.3 <Table5-3>`.

.. _Table5-3:

.. table:: IO AC Characteristics
   :widths: grid

   +---------------------+--------------+---------------------+-----+-----+-----+------+
   | Symbol              | Parameter    | Conditions          | Min | Typ | Max | Unit |
   +=====================+==============+=====================+=====+=====+=====+======+
   | F                   | Maximum      | 2.7 V ≤             |     | 100 |     | MHz  |
   | \ :sub:`max(io)out` | frequency    | V\ :sub:`CCIN`      |     |     |     |      |
   |                     |              | ≤ 5.5 V             |     |     |     |      |
   |                     |              |                     |     |     |     |      |
   |                     |              | T\ :sub:`A`\        |     |     |     |      |
   |                     |              | =25 °C,             |     |     |     |      |
   |                     |              | C\ :sub:`L`\ =10 pf |     |     |     |      |
   +---------------------+--------------+---------------------+-----+-----+-----+------+
   | T                   | Output high  | 2.7V ≤              |     | 2.5 |     | ns   |
   | \ :sub:`f(IO)out`   | to low level | V\ :sub:`CCIN`      |     |     |     |      |
   |                     | fall time    | ≤ 5.5V              |     |     |     |      |
   |                     | and output   |                     |     |     |     |      |
   |                     | low to high  | T\ :sub:`A`\        |     |     |     |      |
   |                     | level rise   | =25 °C,             |     |     |     |      |
   |                     | time         | C\ :sub:`L`\ =10 pf |     |     |     |      |
   +                     +              +---------------------+-----+-----+-----+------+
   |                     |              | 2.7 V ≤             |     | 2.5 |     | ns   |
   |                     |              | V\ :sub:`CCIN`      |     |     |     |      |
   |                     |              | ≤ 5.5 V             |     |     |     |      |
   |                     |              |                     |     |     |     |      |
   |                     |              | T\ :sub:`A`\        |     |     |     |      |
   |                     |              | =25 °C,             |     |     |     |      |
   |                     |              | C\ :sub:`L`\ =10 pf |     |     |     |      |
   +---------------------+--------------+---------------------+-----+-----+-----+------+

nRESET Pin Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about nRESET pin characteristics, refer to :ref:`Table 5.4 <Table5-4>`.

.. _Table5-4:

.. table:: nRESET Pin Characteristics
   :widths: grid

   +-------------------+-------------------+----------------+-----+------+-----+------+
   | Symbol            | Parameter         | Conditions     | Min | Typ  | Max | Unit |
   +===================+===================+================+=====+======+=====+======+
   | R\ :sub:`PU`      | Pull up           | 2.7 V ≤        |     | 80 k |     | Ω    |
   |                   | equivalent        | V\ :sub:`CCIN` |     |      |     |      |
   |                   | resistor          | ≤ 5.5 V        |     |      |     |      |
   |                   |                   |                |     |      |     |      |
   |                   |                   | T\ :sub:`A`\   |     |      |     |      |
   |                   |                   | =25 °C         |     |      |     |      |
   +-------------------+-------------------+----------------+-----+------+-----+------+
   | V                 | nRESET input      | 2.7 V ≤        |     | 1    |     | ms   |
   | \ :sub:`(nRESET)` | pulse             | V\ :sub:`CCIN` |     |      |     |      |
   |                   |                   | ≤ 5.5 V        |     |      |     |      |
   |                   |                   |                |     |      |     |      |
   |                   |                   | T\ :sub:`A`\   |     |      |     |      |
   |                   |                   | =25 °C,        |     |      |     |      |
   |                   |                   | C\ :sub:`L`\   |     |      |     |      |
   |                   |                   | = 10 pf        |     |      |     |      |
   +-------------------+-------------------+----------------+-----+------+-----+------+

Supply Current Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about supply current characteristics, refer to :ref:`Table 5.5 <Table5-5>`.

.. _Table5-5:

.. table:: Supply Current Characteristics
   :widths: grid

   +-----------+-----------+----------------+------------------+---------+------+
   | Symbol    | Parameter | Conditions     | f                | Typical | Unit |
   |           |           |                | \ :sub:`sysclk`\ |         |      |
   |           |           |                | (MHz)            |         |      |
   +===========+===========+================+==================+=========+======+
   | I\        | Supply    | V\ :sub:`CCIN` | 100              | 20      | mA   |
   | :sub:`DD` | current   | = 5 V,         |                  |         |      |
   |           | in RUN    | external       |                  |         |      |
   |           | mode      | 24 MHz         |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | T              |                  |         |      |
   |           |           | \ :sub:`A`\    |                  |         |      |
   |           |           | =25 °C,        |                  |         |      |
   |           |           | PLL ON,        |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | AP ON, CP      |                  |         |      |
   |           |           | ON, NPU ON     |                  |         |      |
   |           |           |                |                  |         |      |
   |           |           | PSRAM          |                  |         |      |
   |           |           | off, NOR       |                  |         |      |
   |           |           | flash          |                  |         |      |
   |           |           | cached         |                  |         |      |
   |           +-----------+----------------+------------------+---------+------+
   |           | Supply    | T              | 24               | 1.8     | mA   |
   |           | current   | \ :sub:`A`\ =  |                  |         |      |
   |           | in        | 25 °C, deep    |                  |         |      |
   |           | VAD&      | sleep          |                  |         |      |
   |           | DEEPSLEEP | mode           |                  |         |      |
   |           | mode      | entered,       |                  |         |      |
   |           |           | VAD mode       |                  |         |      |
   |           |           | enabled        |                  |         |      |
   |           |           | with 1         |                  |         |      |
   |           |           | audio ADC      |                  |         |      |
   |           |           | on (analog     |                  |         |      |
   |           |           | mic not        |                  |         |      |
   |           |           | included)      |                  |         |      |
   |           +-----------+----------------+------------------+---------+------+
   |           | Supply    | T              | 24               | 700     | uA   |
   |           | current   | \ :sub:`A`\ =  |                  |         |      |
   |           | in        | 25 °C, deep    |                  |         |      |
   |           | DEEPSLEEP | sleep          |                  |         |      |
   |           | mode      | mode           |                  |         |      |
   |           |           | entered        |                  |         |      |
   +-----------+-----------+----------------+------------------+---------+------+

Wakeup Time from Sleep Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about wakeup time from sleep modes, refer to :ref:`Table 5.6 <Table5-6>`.

.. _Table5-6:

.. table:: Wakeup Time from Sleep Modes
   :widths: grid

   +-------------------+----------------+----------------+---------+------+
   | Symbol            | Parameter      | Conditions     | Typical | Unit |
   +===================+================+================+=========+======+
   | t\ :sub:`WUSLEEP` | Wakeup from    | External pin   | < 2     | ms   |
   |                   | Sleep          | wakeup (ROM    |         |      |
   |                   |                | boot not       |         |      |
   |                   |                | included)      |         |      |
   +-------------------+----------------+----------------+---------+------+

External Clock Source Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For information about external clock source characteristics, refer to :ref:`Table 5.7 <Table5-7>`.

.. _Table5-7:

.. table:: External Clock Source Characteristics
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

For information about internal clock source characteristics, refer to :ref:`Table 5.8 <Table5-8>`.

.. _Table5-8:

.. table:: Internal Clock Source Characteristics
   :widths: grid

   +-------------------+--------------+-----------------+-----+-----+-----+------+
   | Symbol            | Parameter    | Conditions      | Min | Typ | Max | Unit |
   +===================+==============+=================+=====+=====+=====+======+
   | f\ :sub:`LSI`     | Frequency    | 2.7 V ≤         |     | 32  |     | KHz  |
   |                   |              | V\ :sub:`CCIN`  |     |     |     |      |
   |                   |              | ≤ 5.5 V         |     |     |     |      |
   |                   |              |                 |     |     |     |      |
   |                   |              | T\ :sub:`A`\    |     |     |     |      |
   |                   |              | =25 °C          |     |     |     |      |
   +-------------------+--------------+-----------------+-----+-----+-----+------+
   | t\ :sub:`su(LSI)` | LSI          | 2.7 V ≤         |     | 5   |     | s    |
   |                   | oscillator   | V\ :sub:`CCIN`  |     |     |     |      |
   |                   | startup time | ≤ 5.5 V         |     |     |     |      |
   |                   |              |                 |     |     |     |      |
   |                   |              | T\ :sub:`A`\    |     |     |     |      |
   |                   |              | =25 °C          |     |     |     |      |
   +-------------------+--------------+-----------------+-----+-----+-----+------+
   | I\ :sub:`DD(LSI)` | LSI          | 2.7 V ≤         |     |     | 1   | uA   |
   |                   | oscillator   | V\ :sub:`CCIN`  |     |     |     |      |
   |                   | power        | ≤ 5.5 V         |     |     |     |      |
   |                   | consumption  |                 |     |     |     |      |
   |                   |              | T\ :sub:`A`\    |     |     |     |      |
   |                   |              | =25 °C          |     |     |     |      |
   +-------------------+--------------+-----------------+-----+-----+-----+------+

PLL Characteristics
~~~~~~~~~~~~~~~~~~~

For information about PLL characteristics, refer to :ref:`Table 5.9 <Table5-9>`.

.. _Table5-9:

.. table:: PLL Characteristics
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

For information about Electromagnetic Compatibility (EMC), refer to :ref:`Table 5.10 <Table5-10>`.

.. _Table5-10:

.. table:: EMC??
   :widths: grid

   +------------+-----------+-------------+-------+-----------+------+
   | Symbol     | Ratings   | Conditions  | Class | Maximum   | Unit |
   |            |           |             |       | Value     |      |
   +=========+==+===========+=============+=======+===========+======+
   | VESD (HBM) | Elec      | T\ :sub:`A` | 2     | 2000      | V    |
   |            | trostatic | = 25 °C     |       |           |      |
   |            | discharge |             |       |           |      |
   |            | voltage   |             |       |           |      |
   |            | (human    |             |       |           |      |
   |            | body      |             |       |           |      |
   |            | model)    |             |       |           |      |
   +------------+-----------+-------------+-------+-----------+------+
   | VESD (CDM) | Elec      | T\ :sub:`A` |       | 1000      | V    |
   |            | trostatic | = 25 °C     |       |           |      |
   |            | discharge |             |       |           |      |
   |            | voltage   |             |       |           |      |
   |            | (charge   |             |       |           |      |
   |            | device    |             |       |           |      |
   |            | model)    |             |       |           |      |
   +------------+-----------+-------------+-------+-----------+------+

Package Information
===================

QFN64 (8*8mm) Package Information
-----------------------------------

For the package information, see :ref:`Fig. 6.1 <6-1>`, :ref:`Fig. 6.2 <6-2>`, and :ref:`Figure 6-3 <6-3>`.

.. _6-1:

.. figure:: datasheet_figure/6-1_Top_View.png
   :scale: 50%
   :align: center

   Top View

.. _6-2:

.. figure:: datasheet_figure/6-2_Bottom_View.png
   :scale: 50%
   :align: center

   Bottom View


.. _6-3:

.. figure:: datasheet_figure/6-3.png
   :scale: 50%
   :align: center

   Symbol Dimension

Thermal Characteristics
-----------------------

The maximum chip junction temperature (T\ :sub:`J`\max) in degrees
Celsius can be calculated through the following equation:

.. code:: 
   
   T_J max = T_A max + (P_D max * \theta_{JA})

..
   T\ :sub:`J` max = T\ :sub:`A` max + (P\ :sub:`D` max x θ\ :sub:`JA`)   

where:

-  T\ :sub:`A`\max is the maximum ambient temperature in °C.

-  θ\ :sub:`JA` is the package junction-to-ambient thermal resistance in °C/W.

-  P\ :sub:`D`\max is the sum of P\ :sub:`INT`\max and P\ :sub:`I/O`\max
   (P\ :sub:`D`\max = P\ :sub:`INT`\max + P\ :sub:`I/O`\max).

-  P\ :sub:`INT`\max is the product of I\ :sub:`DD` and V\ :sub:`DD` in Watts. 
   This is the maximum chip internal power.

P\ :sub:`I/O`\max represents the maximum power dissipation on output pins and can be 
calculated through the following equation:
:math:`P_{I/O} max = \sum (V_{OL} * I_{OL}) + ((V_{DD} – V_{OH}) * I_{OH})`

..
   P\ :sub:`I/O`\max = ∑(V\ :sub:`OL` × I\ :sub:`OL`) + ((V\ :sub:`DD` –
   V\ :sub:`OH`) × I\ :sub:`OH`)



The actual V\ :sub:`OL`/I\ :sub:`OL` and V\ :sub:`OH`/I\ :sub:`OH` of the I/Os at
low and high levels in the application are taken into account.

.. _Table6-1:

.. table:: Package Thermal Characteristics
   :widths: grid

   +---------------+-----------------------------------------+----------------+-------+
   | Symbol        | Parameter                               | Value          | Unit  |
   +===============+=========================================+================+=======+
   | θ\ :sub:`JA`  | Thermal resistance junction-ambient     | 28             | °C/W  |
   |               |                                         |                |       |
   |               | QFN64 – 8*8 mm                          |                |       |
   +---------------+-----------------------------------------+----------------+-------+
   | T\ :sub:`STG` | Storage temperature range               | –65 to +150    | °C    |
   +---------------+-----------------------------------------+----------------+-------+
   | T\ :sub:`J`   | Maximum junction temperature            | 125            | °C    |
   +---------------+-----------------------------------------+----------------+-------+

Reflow Profile
==============

Reflow Diagram
-----------------

For the reflow diagram, see :ref:`Fig. 7.1 <7-1>`.

.. _7-1:

.. figure:: datasheet_figure/7-1_Reflow_Diagram.png
   :scale: 50%
   :align: center

   Reflow Diagram

SMT Reflow Conditions
--------------------------

.. _Table7-1:

.. table:: Title?
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

.. table:: Title?？
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
   :scale: 100%
   :align: center

   Application Diagram



