 

 

​        

| Wuqi User Guide                                          |      |
| -------------------------------------------------------- | ---- |
| GUI-Based Task                                           |      |
| Release V1.0                                             |      |
|                                                          |      |
|                                                          |      |
|                                                          |      |
| **Confidential and Proprietary – Wu Qi Micro  Limited.** |      |

 



Copyright

© 2021, XXX Limited. All rights reserved.

No part of this document may be reproduced in any form without the written permission of the copyright owner.

**Disclaimer**

The contents of this document are subject to revision without notice due to continued progress in methodology, design and manufacturing. XXX Limited shall have no liability for any error or damage of any kind resulting from the use of this document.

**Trademark List**

All trademarks mentioned herein are the property of their respective owners. These are shown in the document Trademark Information.

 



Contents

[1.   About This Document 7](#_Toc75875461)

[2.   Initial Configuration. 9](#_Toc75875462)

[2.1    Starting the Tool 9](#_Toc75875463)

[2.2    Connecting a Device. 10](#_Toc75875464)

[3.   Music Parameter Configuration. 11](#_Toc75875465)

[3.1    Configuring the EQ.. 11](#_Toc75875466)

[Glossary. 12](#_Toc75875467)

 



 

Table

[Table 3‑1 BECONFIG Window Parameter Descriptions. 10](#_Toc75875384)

 



 

Figure

[Figure 2‑1 BECONFIG Window.. 9](#_Toc75875445)

[Figure 2‑2 Connect Dialog Box. 10](#_Toc75875446)

 



 



Revision History



| Publication   Date | Version | Edition       |
| ------------------ | ------- | ------------- |
| May 2019           | V1.0    | First Edition |

 

 

 

 



# 1. About This Document

**Purpose**

This document describes the SUN2000-33KTL-US/36KTL-US/40KTL-US (SUN2000 for short) in terms of its installation, electrical connections, commissioning, maintenance, and troubleshooting. Understand the safety information and get familiar with the SUN2000 functions and features before installing and operating the SUN2000.

This document describes how to use XXX/provides information about XXX. The XXX enables users to design the Audio performance of the product efficiently. 

This document applies to the scenario where XXX.

 

**Intended Audience**

This document is intended for XXX engineers.

 

**Prerequisite Skills and Knowledge (Optional)**

The following document must be read and understood before configuration/installation:

- System Security Information

- Personal Health and Safety Information


 <!--调整margin-->

**What Is in This Manual** 

This manual contains the following chapters and appendixes. 



| Chapter 1, XXX  | Defines/Describes… |
| --------------- | ------------------ |
| Chapter 2, XXX  | Describes how to…  |
| Appendix 1, XXX | Provides…          |
| Appendix 2, XXX | Provides…          |

 

**Related Documentation** 

The following documentation is related to this manual:

l XXX (document name)

l XXX

 

**Symbol Conventions**

The symbols that may be found in this document are defined as follows.

| Symbol      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| **Danger**  | Indicates  an imminently hazardous situation  which, if not avoided, will result in death or serious injury. |
| **Warning** | Indicates  a potentially hazardous situation  which, if not avoided, could result in death or serious injury. |
| **Caution** | Indicates  a potentially hazardous situation which, if not avoided, may result in **minor or moderate injury**. |
| **Notice**  | Indicates  a potentially hazardous situation which, if not avoided, could result in **equipment damage**, data loss,  performance deterioration, or unanticipated results.  NOTICE  is used to address practices **not  related to personal injury.** |
| **Note**    | Calls  attention to important information, best practices and tips.  NOTE  is used to address information **not  related to personal injury, equipment damage, and environment deterioration**. |

 

# 2. Initial Configuration

This section describes how to XXX.

## 2.1 Starting the Tool

**Prerequisite (Optional)**

(Describes the preparations before topic operation. Example:)

- The basic parameters are already configured.

- The local terminal is idle and the network is good.

- The local terminal supports the embedded [MCU ](#MCU)function.


 

**Context (Optional)**

Describes the related background information.

 

**Steps**

1    Double-click **BEConfig.exe** to open the Audio configuration tool. The **BECONFIG** window is displayed, see Figure 2‑1. 

 

Figure 2‑1 BECONFIG Window

## 2.2  Connecting a Device

1    In the **Audio Config** window, click **CONNECT**. The **CONNECT** dialog box is displayed, see Figure 2‑3.

 

Figure 2‑2 Connect Dialog Box

# 3. Music Parameter Configuration

This section describes how to configure the music play parameters.

## 3.1 Configuring the EQ

**Steps**

1    Configure the parameters as needed. For a description of the parameters, refer to Table 3‑1.

Table 3‑1 BECONFIG Window Parameter Descriptions



| Parameter                              | Description                                                  | Value Range                                               | Default Value         |
| -------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- | --------------------- |
| Sampling rate                          | Mobile phone related.                                        | l   44100  l   48000                                      | 44100                 |
| Center frequency                       | Center frequency of  each segment that needs to be adjusted.   Sets the center  frequency of a segment. Up to five segments can be set. | 20 Hz–20 kHz                                              | 125 250 500 1000 2000 |
| Low-pass filter  switch                | Signals below the cutoff frequency  are allowed to pass, and signals above the cutoff frequency are not allowed  to pass. | -                                                         | 0                     |
| Low-pass filter transition zone  slope | The larger the value is, the greater  the slope is.          | l   6 dB/Oct  l   12 dB/Oct  l   18 dB/Oct  l   24 dB/Oct | 6 dB/Oct              |
| High-pass filter  switch               | Signals above the cutoff frequency  is allowed to pass, and signals below the cutoff frequency is not allowed to  pass. | -                                                         | -                     |

2    Click **Save Configuration** to write the configuration into the IC. 



|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |

 

 

 

 

# Glossary

| MCU  | Micro Control Unit  An MCU is a single Integrated Circuit (IC) that is typically  used for a specific application and designed to implement certain tasks. |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

 



 

# 4. Rules for Procedural Writing

## 4.1 General Rules

l  **Action-based Heading.** To describe activities or suggest actions, use **task-oriented headings** that contain a **verb**—either **present tense or in gerund (-ing) form**. Present tense works well for headings that identify steps in a process. Examples:

- Adding an account 

- Add an account

- Step rule: general


## 4.2 GUI-Based Task Topic

### 4.2.1 Steps Rules

\1.    Write short sentences. Use **a maximum of 20 words** in each sentence.

\2.    Write **only one instruction in each sentence** unless two or more actions occur at the same time. 

\3.    The **operation result** should follow the operation step. The result cannot act as a separate step and cannot be placed at the beginning of next step.

\4.    Write instructions in the **imperative (command) form**.

\5.    If you start an instruction with a descriptive statement (dependent phrase or clause), divide that statement from the command with a comma.

\6.    Write **notes** only to **give information, not instructions**.

\7.    **Limit a procedure to seven steps**, and preferably fewer. Try to fit all the steps on the same screen.[[u1\]](#_msocom_1) 

\8.    **Abbreviate simple sequences by using right angle brackets**. Include a space before and after each bracket, and don't make the brackets bold.

   Example: Select **Accounts** > **Other accounts** > **Add an account**.

\9.    When there's an **ellipsis** in UI, **don’t include it in instructions or procedures**.

**10.**  If a step is optional, add **(Optional)** at the beginning.

\11.  Most of the time, include actions that finalize a step, such as **OK** or **Apply** buttons.[[u2\]](#_msocom_2) 

\12. For operational steps, it is recommended to use the following patterns:

l  Condition + time + place + operational steps + purpose + brief information + result 

l  (Optional) Purpose + time + place + operational steps + brief information + result

Examples:

l  In the XX area, select xxx. The xxx dialog box is displayed, see Figure x-x.

l  In the **Path** text box, enter the path and name of the file from which you want to import the template. You can also click **Browse** to select the file.

l  (Optional) To display the current settings of this link, click **Query**.

(Note that the position of Purpose is different.)

 



 

 

|                                                              |                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |                                                              |
| **Contact Us**                                               |                                                              |                                                              |
| **Website**:  [www.wuqi-tech.com](http://www.wuqi-tech.com)  | **Technical Support:**  [support@wuqi-tech.com](mailto:support@wuqi-tech.com) | **Business Consultation:**  [sales@wuqi-tech.com](mailto:sales@wuqi-tech.com) |
| **Chongqing**     **Address**:  14/F, 107 Middle Road, Xiantao Big Data Valley, Yubei District, Chongqing,  PRC.  **Tel/Fax:**  023-67682717 | **Shanghai**     **Address**:  8/F, Building 29, No.368, Zhangjiang Road, Pudong New District, Shanghai,  PRC.  **Tel/Fax**:  021-50806308 | **Shenzhen**     **Address**:  Room 1105, Building 2, Fangdacheng, Longzhu 4th Road, Taoyuan Street, Nanshan  District, ShenZhen, PRC.  **Tel/Fax**:  0755-86967944 |
|                                                              |                                                              |                                                              |
| **© 2021, Wu Qi Micro Limited. All rights reserved.**  **No part of this document may be reproduced in any form without**    **the written permission of the  copyright owner.**  **Doc  No.:** |                                                              |                                                              |

 

------



 [[u1\]](#_msoanchor_1)general



 [[u2\]](#_msoanchor_2)general