# WQ70XX DTOPSS 编程指南

# 1. 概述

WQ70XX是一颗用于无线语音和音频应用的蓝牙SOC芯片，它包括三个子系统：DTOPSS、BTSS和DSPSS。现在**开放一个完全独立的DTOPSS给客户进行自主定制**。

## 1.1 DTOPSS简介

DTOPSS包含一个独立的**RISCV CPU**，同时拥有独立的**IO系统、中断系统和存储系统**。

- IO系统负责对外连接，系统可以通过UART/I2C/SPI/JTAG总线和外部系统连。GPIO作为独立的模块，可以输入输出高低信号。

- 中断系统主要通过中断控制器(INTC)来响应外部和内部信号的响应。当外部系统或者内部系统产生中断信号，INTC会根据每个中断向量的设置，屏蔽或者把中断信号发送给CPU。

- 存储系统主要是Flash和RAM。通过SFC控制器，Flash既可以做数据存储功能，又可以做到代码执行功能。

## 1.2 软件简介

**软件从层次上主要分为上层为用户app，中间是library，底层为驱动。OS和基础库为每层提供相对应的API调用。现在跑在芯片上的OS是FreeRTOS v10.2.1，是基于官方的RISCV移植修改过来的。**

**驱动是针对芯片的外部总线和内部系统进行抽象，对外提供HAL函数。**

现有的驱动系统主要包括ADC、DMA、GPIO、I2C、LED、RTC、SPI、TIMER、Touch Key、UART、WDT等。后面章节针对每个设备展开详细介绍。

# 2. ADC

## 2.1 ADC概述

### 2.1.1 性能指标

### 2.1.2 工作模式

## 2.2 ADC设备API

### 2.1.1      初始化

该接口对ADC驱动进行初始化，必调接口之一。

`void iot_adc_init(void);`

| **参数** | **描述** |
| -------- | -------- |
| void     | 无参数   |
| **返回** | ——       |
| void     | 无返回值 |



### 2.1.2      ADC OPEN

该接口用于打开ADC设备，从信号输入源ch采集数据，接口设计主要用于双输入源同时采集模式，两路同时工作，其中一路port0为VAD专用，另一路port1采集输入源ch的数据，在该模式下，需要配合下文中的iot_adc_single_channel_receive_poll()和iot_adc_close()配合完成整个读数功能，详情见后文示例。

单输入源采集模式可以使用该接口配合下文中的iot_adc_dfe_poll()和iot_adc_close()配合完成整个读数流程，详见后文使用示例。

1. sample rate对两路同时有效 
2. VAD工作时，需要注意软件降采样。 
3. port 0默认用于连续工作模式的数据采集如VAD 
4. port 1默认采集信号输入源ch的数据 
5. 参数ch和gain都是默认配置给port0的，如需要使用port1可用如下函数iot_adc_dynamic_cfg_port(uint8_t port, uint8_t ch, uint8_t gain)

```
void iot_adc_open(
   uint8_t ch,
   IOT_ADC_SAMPLE_RATE sample_rate,
   uint8_t gain,
   IOT_ADC_WORK_MODE mode);
```

| **参数**    | **描述**                                               |
| ----------- | ------------------------------------------------------ |
| ch          | 输入信号源可用前文中枚举IOT_ADC_SIG_SRC强转uint8_t传入 |
| sample_rate | 硬件采样频率                                           |
| gain        | 增益                                                   |
| mode        | 工作模式                                               |
| **返回**    | ——                                                     |
| void        | 有无返回                                               |

### 2.1.3      动态配置port

void iot_adc_dynamic_cfg_port(uint8_t port, uint8_t ch, uint8_t gain)

| **参数** | **描述**                                               |
| -------- | ------------------------------------------------------ |
| port     | 指定要配置的port                                       |
| ch       | 输入信号源可用前文中枚举IOT_ADC_SIG_SRC强转uint8_t传入 |
| gain     | 增益                                                   |
| **返回** | ——                                                     |
| void     | 有无返回                                               |

该接口用于在使用上述接口iot_adc_open(…)打开并启动ADC设备之后，动态的修改指定port的信号源以及gain。典型的使用场景之一就是VAD同时需要采集电池电压和外部一个传感器的输入，那么就可以打开IOT_ADC_WORK_MODE_MULTI_CONTINUOUS模式，使用该接口动态配置port1，在不影响vad连续数据的情况下获取电池电压或者外部传感器数据。

Note： 1. 配置了硬件自动丢弃5笔数据，取1笔有效数据，使用iot_adc_single_channel_receive_poll(…)时无需软件进行丢弃。

### 2.1.4      单输入源采集模式下读取数据

uint32_t iot_adc_dfe_poll(void);

| **参数** | **描述**                   |
| -------- | -------------------------- |
| void     | 无参数                     |
| **返回** | ——                         |
| uint32_t | 无符号硬件code，24bits有效 |

Note： 1. 仅用于读取单输入源采集模式下的转换硬件无符号adc code 2. 需要额外的软件将24bits数据转化成有符号数。

### 2.1.5      双输入源同时采集模式读取数据

uint32_t iot_adc_single_channel_receive_poll(IOT_ADC_PORT port, IOT_ADC_DATA_MODE mode);;

| **参数** | **描述**                   |
| -------- | -------------------------- |
| port     | 读取指定路                 |
| mode     | 平均值或者累加值           |
| **返回** | ——                         |
| uint32_t | 无符号硬件code，24bits有效 |

Note： 1. 仅用于双输入源同时采集模式读取数据 2. 仅用于读取单输入源采集模式下的转换硬件无符号adc code 3. 需要额外的软件将24bits数据转化成有符号数。

### 2.1.6      ADC设备关闭

void iot_adc_close(void);

| **参数** | **描述** |
| -------- | -------- |
| void     | 无参数   |
| **返回** | ——       |
| void     | 无返回   |

该**函数**关闭所有ADC相关CLK,关闭所有ADC相关LDO。

### 2.1.7      读取一次ADC结果

int32_t iot_adc_poll_data(uint8_t ch, uint8_t gain, uint8_t sum_average);

| **参数**     | **描述**                                               |
| ------------ | ------------------------------------------------------ |
| ch           | 输入信号源可用前文中枚举IOT_ADC_SIG_SRC强转uint8_t传入 |
| gain         | 增益                                                   |
| sum_average  | 累加平均滤波宽度                                       |
| **返回**     | ——                                                     |
| int32_tl类型 | 有符号32bits AD转换结果                                |

该接口是ADC驱动中最重要的接口，工作于单输入源采集模式，这个接口工作流程如下： 打开ADC相关的LDO–>打开ADC CLK–>配置ADC–>读取ADC结果并处理–>关闭CLK–>关闭ADC相关LDO。

Note： 1. 模块工作起来耗电约为500uA（LDO耗电30uA，ADC模拟耗电450uA, 其他几十uA），所以ADC不常开，需要读数的时候才开关一次。 2. 该接口操作和配置硬件繁琐，整个流程耗时平均约2ms，避免在中断上下文调用该接口。 3. 该接口独立工作，不需要调用上文中的open接口，也无需使用close接口善后。 4. 采样频率为250kHz 5. 返回结果已经转化为32bits 有符号数。

### 2.1.8      DMA方式读取数据

uint8_t iot_adc_dma_config(void)；

| **参数** | **描述** |
| -------- | -------- |
| void     | 无参数   |
| **返回** | ——       |
| RET_OK   | 成功     |

该接口用于申请一个DMA通道用于传输ADC某个port的AD采样结果。

Note： 1. 驱动内部管理DMA通道，仅支持一个通道，返回值并不是DMA通道号。

void iot_adc_dma_channel_link(IOT_ADC_PORT port);

| **参数** | **描述**                    |
| -------- | --------------------------- |
| port     | 指定使用DMA读取该port的数据 |
| **返回** | ——                          |
| void     | 无返回                      |

port为上文open接口中的prot0或者port1，不论单输入源模式还是双输入源同时采集模式都可使用。

Note： 1. 仅支持一路使用DMA方式读数

//typedef void (*dma_peri_mem_done_callback)(void *buf, uint32_t length);包含于dma驱动
 uint8_t iot_adc_receive_dma(uint32_t *buffer, uint32_t length, dma_peri_mem_done_callback cb);

| **参数**  | **描述**         |
| --------- | ---------------- |
| buffer    | 结果存储位置指针 |
| buffer    | length           |
| cb        | dma完成回调      |
| **返回**  | ——               |
| RET_OK    | 成功             |
| RET_INVAL | 没有config dma   |

port为上文open接口中的prot0或者port1，不论单输入源模式还是双输入源同时采集模式都可使用。

Note： 1. 同时仅支持一路使用DMA方式读数 2. RET_INVAL是因为没有申请过或者申请到DMA通道。

### 2.1.9      ADC_CODE转电压值

float iot_adc_2_mv(uint8_t isdiff, int32_t adc_code);

| **参数** | **描述**       |
| -------- | -------------- |
| isdiff   | 差分模式1，否0 |
| adc_code | 有符号32bits   |
| **返回** | ——             |
| float    | 电压值         |

该接口将32bits有符号的adc code转化为对应的电压值。

### 2.1.10   去初始化

该接口对ADC驱动进行去初始化，睡眠，关机需要调用该接口。

void iot_adc_deinit(void);

| **参数** | **描述** |
| -------- | -------- |
| void     | 无参数   |
| **返回** | ——       |
| void     | 无返回值 |

## 2.3 ADC设备使用示例

以下代码展示了ADC 读取内部电池电压，外部ADC输入，使用DMA读数的方法。

```
#include "types.h"
#include "stdio.h"
#include "iot_adc.h"
#include "iot_dma.h"

#define ADC_EXAPLE_PRINTF(fmt, arg...)
//voltage division ratio
#define ADC_EXAPLE_VBAT_RATIO 0.202f
#define ADC_EXAPLE_DMA_BUFFER_LEN 256

static uint32_t test_adc_buffer[ADC_EXAPLE_DMA_BUFFER_LEN] = {0};
static bool_t adc_done = false;

/* for dma recv done callback */
void dma_peri_mem_done_callback(void *buf, uint32_t length)
{
    (void)buf;
    (void)length;
    adc_done = true;
    ADC_EXAPLE_PRINTF("DMA recv data done\n");
}

int main(void)
{
    uint32_t uadc_code = 0;
    int32_t adc_code = 0;
    uint8_t gain = 0;
    uint8_t sum_average = 1;
    int32_t vol = 0;
    uint32_t i = 0;

    /* adc init */
    iot_adc_init();

    /* battery voltage */
    adc_code = iot_adc_poll_data(IOT_ADC_CHARGER_OUT_VOLTAGE, gain, sum_average) vol =
        (int32_t)iot_adc_2_mv(0, adc_code) / VBAT_RATIO;
    ADC_EXAPLE_PRINTF("vabt vol:%d\n", vol);

    /* extern input diff mode */
    adc_code = iot_adc_poll_data(IOT_ADC_EXT_SIG_CH2, gain, sum_average) vol =
        (int32_t)iot_adc_2_mv(0, adc_code);
    ADC_EXAPLE_PRINTF("derect poll api extern input vol:%d\n", vol);

    /* open single mode dfe poll */
    iot_adc_open(IOT_ADC_EXT_SIG_CH2, IOT_ADC_SAMPLE_RATE_250K, 0, IOT_ADC_WORK_MODE_SINGLE);

    //discard some previous data
    for (i = 0; i < 6; i++) {
        iot_adc_dfe_poll();
    }
    uadc_code = iot_adc_dfe_poll();
    //sign bit
    if (uadc_code & (1 << 23)) {
        adc_code = (int32_t)(uadc_code | (0xffU << 24));
    } else {
        adc_code = (int32_t)(uadc_code & 0x7fffff);
    }
    vol = (int32_t)iot_adc_2_mv(0, adc_code);
    ADC_EXAPLE_PRINTF("open and dfe poll api extern input vol:%d\n", vol);
    iot_adc_close();

    /* open multi mode poll and dma continuous */
    iot_adc_open(IOT_ADC_EXT_DIFF_CH01, IOT_ADC_SAMPLE_RATE_250K, 0,
                 IOT_ADC_WORK_MODE_MULTI_CONTINUOUS);
    iot_adc_dynamic_cfg_port(1, IOT_ADC_EXT_SIG_CH2, 0);
    //dma recv port 0 data
    iot_adc_dma_config();
    iot_adc_dma_channel_link(IOT_ADC_PORT_0);
    iot_adc_receive_dma(test_adc_buffer, ADC_EXAPLE_DMA_BUFFER_LEN, dma_peri_mem_done_callback);

    uadc_code = iot_adc_single_channel_receive_poll(IOT_ADC_PORT_1, IOT_ADC_AVERAGE_DATA);
    //sign bit
    if (uadc_code & (1 << 23)) {
        adc_code = (int32_t)(uadc_code | (0xffU << 24));
    } else {
        adc_code = (int32_t)(uadc_code & 0x7fffff);
    }
    vol = (int32_t)iot_adc_2_mv(0, adc_code);
    ADC_EXAPLE_PRINTF("open and port poll api extern input vol:%d\n", vol);

    while(!adc_done) {
        //waiting dma done
    };

    /* close and deinit */
    iot_adc_close();
    iot_adc_deinit();
    return 0;
}
```



# 3. DMA

