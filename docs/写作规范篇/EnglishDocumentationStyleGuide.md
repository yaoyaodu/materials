# 英文技术文档写作规范

来源：参考主流技术文档写作规范，针对工作过程中遇到的问题，整理而来

# 1. General Rules

## 1.1 Scannable Content

The volume of content available to customers is overwhelming. Part of a writer's job is to help readers find what they need quickly, or recognize just as quickly when they're not where they need to be. Writing to facilitate scanning will help.

**Organize text into discrete components to support scanning**. The following are some of the methods you can use:

- Headings

- Lists

- Tables


How you write is equally important to scanning.

### 1.1.1 Heading

* Consider using a **heading** to help customers **find instructions quickly**. Use the heading to tell customers what the instructions will help them do. Examples: 
  * Adding an account 
  * Add an account 

* Choose **one phrasing style** for the headings, and write them all the same way **(in parallel structure**).

- Use parallel sentence structure for all headings at the same level. For example, use noun phrases for first-level headings, verb phrases for second-level headings, and infinitive phrases for headings in instructions.


* **Don’t use ampersands (&) or plus signs (+) in headings** unless you're referring to UI that contains them or space is limited.

* Use **vs**., not v. or versus, in headings.

- **Keep headings as short as possible,** and put the most important idea at the beginning. 
- **Be as specific as you can**, and **be even more detailed with lower-level headings**. For example, a second-level heading should be more specific than a first-level heading.
- Don't end headings with a period. A question mark or (rarely) an exclamation point can be used if it's needed for meaning. Examples: 
  - Not seeing what you want? 
  - What can we help you find?

- **Run-in Headings** When you want to highlight the topic of a paragraph or bullet item, without defining it as a major heading level, begin the text with a bold run-in heading. **The preferred style for run-in headings is to end them with a bold period.** However, when meaning is better served by a colon or en dash with spaces, you can use that alternate punctuation. (A **run-in heading** is a heading positioned upon the very same line as the text. Frequently this text is put in either **italic or bold** type.)

### 1.1.2  List

Lists area great way to present complex text in a way that's easy to scan. Lists work best when they have two to seven items. Each item should be fairly short—the reader should be able to see at least two, and preferably three, list items at a glance. It’s OK to have a couple of short paragraphs in a list item, but don’t exceed that length too often. 

Make items in a list parallel. For example, each item should be a noun or a phrase that starts with a verb.

#### 1.1.2.1 Bulleted Lists

l  Keep bulleted lists to **one or two lines** per bullet, **three at most**. 

The purpose of bulleted lists is to **isolate key information for easy reading and retrieval.** Rewrite over-long copy as a set of regular prose paragraphs with subheadings or run-in headings. 

l  The items in a bulleted list should have **parallel construction;** that is, **the form of each item must be the same**. If some items in a bulleted list are complete sentences and some are fragments, rewrite them so that the items are parallel. 

l  **Initial capitalize the first word of each item** in a bulleted list, and **the first word after a** **run-in heading** followed by a period or colon (but not by an en dash). 

l  Rules for **periods** in a bulleted list: 

- Complete sentences: Use periods. 

- Sentence fragments, such as an inventory list format: Do not use periods. 

- List items that complete a sentence begun in the introductory statement: Do not use periods. 


l  Use **bold type for run-in headings** in a bulleted list, followed by a period, an en dash with spaces, or a colon. **The period, colon, and dash are bold.** Use sentence case for the run-in heading. 

Examples: 

- **Run-in heading.** Preferred style. End each true heading with a period. Initial capitalize the first word of follow-on text. Each bulleted item can be one to three lines long; present longer bullet text as paragraphs with run-in headings. 
- **Run-in heading –** Use an en dash when the run-in heading introduces a thought that the rest of the text completes. Lowercase the first word of follow-on text.
- **Single-word:** When they introduce what follows, end single-word headings—such as Example:, Note:, or Caution:—with a colon. Initial capitalize the first word of follow-on text.

#### 1.1.2.2      Numbered lists

Use a numbered list for sequential items (like a procedure) or prioritized items (like a top 10 list).

## 1.2  Wording

l  Do not use different technical names for the same item.

l  Write noun clusters of no more than four words.

l  When a technical name has more than three words, write it in full. Then you can simplify it using either of the following ways:

Ø  Give a shorter name

Ø  Use hyphens between words that are used as a single unit. Examples:

n Make sure that the landing-light cutoff-switch power connection is safe.

n Inspection of the lavatory rapid-decompression device.

n Main-gear-door retraction-winch handle.

l  When applicable, use an article (the, a, an) or a demonstrative adjective (this, these) before a noun.

Ø  In short sentences, it can be clearer to include all the articles before the nouns. But sentences that contain a long series of items are clearer when you do not repeat the articles. Example:

n Install the nuts and the bolts.

n Discard the packings, gaskets, seals and washers.

Ø  **A definite article is incorrect before a noun when an alphanumeric identifier comes after it**. Example:

n Incorrect: Tag the circuit breaker 36L7.

n CORRECT: Tag circuit breaker 36L7.

l  American and British English: In general, technical manuals are written in American English. Example: 

Ø  fiber not fibre

Ø  color not colour

## 1.3            Acronym and Abbreviation

### 1.3.1        Acronyms

An acronym is formed from the first letter of the words in the phrase. Sometimes the acronym is taken from other letters of the keywords, as in the case of Extensible Markup Language (XML).

Acronyms are always written using full capitalization and are expanded when they first appear in the text unless the first appearance is in a heading.

**Exceptions** to this rule:

l  **acronyms containing prepositions** 

*Example: Prepositions in Acronyms*

| Correct                        | Incorrect                      |
| ------------------------------ | ------------------------------ |
| Quality  of Service (QoS)      | Quality  of Service (QOS)      |
| Change  of Authorization (CoA) | Change  of Authorization (COA) |
| IP  over Ethernet (IPoE)       | IP  over Ethernet (IPOE)       |
| Voice  over IP (VoIP)          | Voice  over IP (VOIP)          |

**Note:** An **exception** to this rule applies to acronyms such as In-Service **Software Upgrade (ISSU)** where the preposition is the first word.

Whenever in doubt, check whether your acronym is approved.

 

l  **Products with 'virtual' in the name**

Ø  When writing the **full form** for a virtual product name, use Virtual<product name full form>.

Example: Full Form for a Virtual Product Name

| Correct                         | Incorrect                                                    |
| ------------------------------- | ------------------------------------------------------------ |
| Virtual Evolved  Packet Gateway | Virtualized Evolved  Packet Gateway  virtual Evolved Packet Gateway  Evolved Packet Gateway  Virtualization |

Ø  When writing the **acronym** for a virtual product name, use v<product name acronym>.

Example: Acronym for a Virtual Product Name

| Correct | Incorrect                                             |
| ------- | ----------------------------------------------------- |
| vEPG    | VEPG  virtual EPG  Virtualized EPG  Rules for Writing |

Ø  When writing the full form for a standard term, use Virtual <term name full form>.

| Correct                              | Incorrect                                                    |
| ------------------------------------ | ------------------------------------------------------------ |
| Virtual Network Interface Controller | virtual Network Interface Controller  Virtualized Network Interface  Controller |

Ø  When writing the acronym for a standard term, use V<term name acronym>.

| Correct | Incorrect |
| ------- | --------- |
| VNIC    | vNIC      |

 

**Expanding Acronyms**

Acronyms are introduced by writing out the full phrase followed by the acronym set in parentheses.

| Correct                            | Incorrect                          |
| ---------------------------------- | ---------------------------------- |
| Customer Product Information (CPI) | CPI (Customer Product Information) |

 

**Expanding Acronyms in the Plural**

If an acronym is first used in the plural, expand it in the plural but then use it as singular or plural as necessary.

The plural of an acronym ends in "s"; do not use any punctuation or other letter to indicate a plural acronym.

| Correct                                                      | Incorrect                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| This manual does not deal with the  configuration of Central Processing Units (CPUs). | l   This manual does not deal with the  configuration of Central Processing Units (CPU:s).  l   This manual does not deal with the configuration  of Central Processing Units (CPUes).  l   This manual does not deal with the  configuration of Central Processing Units (CPU's). |

**Acronyms Are Not Verbs**

Do not use any acronym as a verb.

| Correct                     | Incorrect           |
| --------------------------- | ------------------- |
| Send me the file using FTP. | FTP the file to me. |

### 1.3.2        Abbreviations

l  Use a non-breaking space (Ctrl+Atl+Space) in any abbreviation to avoid having one letter move to the beginning of the next line.

l  English abbreviation of months and days of the week are as follows: Month: **Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec** Days of the week: **Mon, Tue, Wed, Thu, Fri, Sat, Sun.**

l  **Avoid the ampersand (&) in text or headings. Spell it out: and.** To save space, you can use the & symbol in presentations, tables, titles, and in the left navigation on Web pages.

l  **Don’t abbreviate** such words as follows:

Ø  Do not abbreviate **Microsoft** as MS when Microsoft is a part of product names.  

Ø  Do not abbreviate **Internet Explorer** as IE.

Ø  Do not abbreviate **Visual Studio** as VS in product names. 

Ø  Do not abbreviate **operating system names**. Correct examples: 

n **Windows Server 2008**

n **Windows Vista**

n **Windows 7**

### 1.3.3        Exceptions

Use an abbreviation or acronym only with a gxref link in the following situations:

l  Do not spell out an abbreviation or acronym that is commonly known to the target audience.

l  Where the meaning is clear and it benefits the user by making the information easier to comprehend.

l  Where it is recognized more easily than its spelled-out form, for example, HTML

l  Where space is limited, for example, in a column in a table or in a detailed diagram

l  In text that deals mainly with dimensions and other numeric specifications

l  In tables, where the abbreviation or acronym can be explained in the table note

l  In titles, where the abbreviation or acronym can be explained in the text nearby

l  Where the abbreviation or acronym and numbers or other letters form a proper noun, for example, EIA RS232.

**Note:** All acronyms, even those not expanded in the text, must be listed in the Glossary.

## 1.4 URL

\1.    In content for a **general audience**, use **address** rather than URL. In content for a **technical audience**, **don't spell out URL on first mention**. If you have a reason to spell out URL, use **uniform resource locator**.

**2.**    Use **a**, not an, as an article preceding URL. **a URL**

\3.    In text references, **you can leave off the http://** unless the URL begins with something other than www. (Include the protocol only if it's something other than HTTP, such as File Transfer Protocol (FTP)). Example:

l  www.microsoft.com/business 

l  ftp://example.com/downloads/myfile.txt

\4.    The trailing slash at the end of a URL is optional. In most cases, leave it off. **Never use a trailing slash in a URL that ends with a file name.** 

\5.    Most of the time, **use lowercase for URLs, email addresses, and newsgroup addresses**. 

\6.    **To refer to an entire website or top-level domain**, such as Microsoft.com, **omit** http://www from the URL and **capitalize** only the first letter of the URL, even if the site name is capitalized differently. Examples: 

l  [www.microsoft.com](http://www.microsoft.com) 

l  Microsoft.com

l  Codeplex.com is home to the open source project site hosted by Microsoft.

\7.    If a sentence ends with a URL, include the period at the end. 

However, when the URL follows a colon, do not include a period at the end. Correct: 

l  For training, visit the Intel® Software College **at** [www.intel.com/software/college](http://www.intel.com/software/college).

l  For more information visit: [www.intel.com/software/products](http://www.intel.com/software/products)

\8.    Use of (not for) to describe the relationship of the word URL to a resource. 

Use the preposition at with the location of a specific address. 

Examples: 

l  Search results include **the URL of the page.** 

l  Learn more about Microsoft products and services **at** [www.microsoft.com](http://www.microsoft.com). 

\9.    If the reader might think the period at the end of a sentence is part of the URL, rewrite the sentence or set the URL off. Examples: 

l  Go to windows.microsoft.com/upgrade to learn how to get your free Windows 10 upgrade.

l  To get your free Windows 10 upgrade, go to our website: windows.microsoft.com/upgrade 

\10.  Write brief but meaningful link text, using the title or a description of a page rather than a generic phrase like click here. In alt text for a graphic that links to another location, state clearly that the graphic is a link. Examples:

l  Go to the Windows 10 upgrade page to learn how to get your free upgrade.

l  (Alt text) Picture of a woman talking on a phone that opens an online chat session with Microsoft support. 

l  (Alt text) Windows 10 logo and link to the Windows 10 upgrade page

## 1.5            Punctuation

Correct punctuation is important because it shows how the different parts of the text are related and prevents ambiguity. 

l  You can use all standard English punctuation marks **except the semicolon (;).**

The semicolon (;) is not approved in STE because it lets you write very long sentences. It is also difficult to use correctly. As an alternative to the semicolon, always write two different sentences.

l  For phrases in cells of a table, use no mark at sentence ends.

For sentences in cells of a table, use periods.

l  In general, you should prefer words to marks (except formulas) in the body.

l  Use an en dash (–): 

Ø  To indicate a range of numbers such as inclusive values, dates, or pages. For example, © 1993–1994, pages 95–110. Do not mix text and en dash, as in “The voltage is from 42–48 V” (Use “from 42 V to 48 V” instead). For ranges, only add the unit after the second value, for example, 2–5 Mbps.

Ø  To indicate a minus sign

Ø  To indicate negative numbers: –79

Ø  To form a compound modifier for a noun, such as Windows NT–based program, dialog box–type options, MS-DOS–compatible products (MS-DOS still uses a hyphen)

Ø  Do not use an en dash to indicate an empty cell in a table. Use a hyphen instead.

Ø  Do not use spaces on either side of an en dash.

l  em dash (—): 

Ø  Used in a complex figure title. For example, Query Active Alarms Dialog Box—Location Tab

## 1.6            Units of Measure Terms

This section covers usage and abbreviations for a variety of terms related to measurement. For other units of measure not covered here, see [*The Chicago Manual of Style*](http://www.chicagomanualofstyle.org/home.html).

l  **Use numerals for measurements of distance, temperature, volume, size, weight, pixels, points**, and so on— even if the number is less than 10. Add a zero before the decimal point for decimal fractions less than one, unless the customer is asked to enter the value. Examples:

Ø  3 ft, 5 in.

Ø  1.76 lb

Ø  80 × 80 pixels 

Ø  0.75 grams 

Ø  enter .75" 3 centimeters

Ø  3 cm

l  Insert a space between the unit of measure and the numeral, or **hyphenate if the measurement modifies a noun.** Examples:

Ø  13.5 inches

Ø  13.5-inch display

Ø  8.0 MP

Ø  8.0-MP camera

l  Use abbreviations only with numbers in specific measurements, such as 20 MP, and don't follow the abbreviation with a period.

**Exception** Follow *in* with a period when used as an abbreviation for *inch.*

l  Use commas in numbers that have four or more digits, regardless of how the numbers appear in the UI: **1,093 MB**.

**Exceptions**

For **pixel measurements and baud**, use commas only when the number has **five or more digits:** *1920 × 1080 pixels, 10,240 × 4320 pixels, 9600 baud, 14,400 baud.*

Don’t use commas after the decimal point in decimal fractions.

l  When the unit of measure is spelled out, **use the singular form when the number is 1. Use the plural form for all other measurements.** Examples

0 points

0.5 points

**1 point**

12 points

l  **Spell out \*by\* in dimensions, except for tile sizes, screen resolutions, and paper sizes.** For those, use the multiplication sign (×). Use a space before and after the multiplication sign. 

Examples

Ø  **10 by 12 ft room**

Ø  **3" by 5" image**

Ø  4 × 4 tile

Ø  8.5" × 11" paper

Ø  1280 × 1024

| Category                                     | Term            | Abbreviation   And Usage                                     |
| -------------------------------------------- | --------------- | ------------------------------------------------------------ |
| Distance and length                          | centimeters     | cm                                                           |
|                                              | feet            | ft                                                           |
|                                              | inches          | in. (or " if space is limited). Always  include a period to avoid confusion with the preposition *in.*  Hyphenate *half-inch* as an adjective. Use instead of *half an inch* or *one-half  inch.*  When space is limited or the  measurement needs to be specific, use *0.5  in.*   Use the abbreviated form sparingly in  content that will be translated or localized. It may be translated  incorrectly as a preposition. |
|                                              | kilometers      | km                                                           |
|                                              | meters          | m                                                            |
|                                              | miles           | mi                                                           |
|                                              | millimeters     | mm                                                           |
| Weight                                       | grams           | g                                                            |
|                                              | kilograms       | kg                                                           |
|                                              | ounces          | oz                                                           |
|                                              | pounds          | lb                                                           |
| Type and fonts                               | points          | pt                                                           |
| UI, display resolution, and digital  imaging | pixels          | Don’t use the abbreviation *px* in the context of screen or camera  resolution.  It’s OK to abbreviate as *px* in content about online design when  space is limited.   Examples  48 × 48 px   The application icon should be 62 × 62  pixels and PNG format. |
|                                              | pixels per inch | It’s OK to use the acronym PPI in  content about creating digital applications, when space is limited, and when  you’re certain that readers will understand it.   Examples  72 pixels per inch At 72 PPI, …. |
|                                              | megapixels      | MP                                                           |
| Print and display resolution                 | dots per inch   | It’s OK to use the acronym dpi to  refer to print and display resolution when you’re certain that readers will  understand it. |
| Speed and frequency                          | baud            | Don't abbreviate. Don't use baud rate—it's  redundant. When designating baud, use commas when the number has five  (not four) or more digits. |
|                                              | gigahertz       | GHz. Spell out on the first mention.  After that, it’s OK to use the abbreviation as a measurement with numerals. |
|                                              | Hertz           | Hz. Spell out on the first mention. After  that, it’s OK to use the abbreviation as a measurement with numerals.  Capitalize the word and the abbreviation. |
|                                              | kilohertz       | KHz. Spell  out on the first mention. After that, it’s OK to use the abbreviation  as a measurement with numerals. |
|                                              | megahertz       | MHz. Spell  out on the first mention. After that, it’s OK to use the abbreviation  as a measurement with numerals. |
| Other                                        | degrees         | ° (for temperature)   deg (for angle)                        |
|                                              | dialog units    | Don’t abbreviate. Example:  Converting from MFC dialog units  (used in resource files to specify height/width) to pixels …. |

## 1.7            Bits and Bytes Terms

In general, spell out *bit* and *byte* terms on the first mention unless:

l  Your audience is familiar with the abbreviation. 

l  You’re working on UI text.

In those cases, or after you’ve spelled out the term on the first mention, it’s OK to use abbreviations for *-bit* or *byte* terms. Use abbreviations only with numbers in specific measurements, such as 128 TB.

l  Insert a space between the abbreviation and the numeral, or hyphenate if the measurement modifies a noun. Examples:

Ø  512 gigabytes (GB) of RAM

Ø  From 1 GB to a maximum of 2 GB

Ø  23 MB/day

Ø  up to 2 terabytes of physical memory with 8 terabytes of address space

Ø  200 MB of available hard-drive space 

Ø  a 650-MB limit

l  In measurements, when the unit of measure isn't abbreviated, use the singular form of the unit of measure when the number is 1. Use the plural form for all other measurements. **Examples**

Ø  0 megabytes

Ø  0.5 megabytes

Ø  **1 megabyte**

Ø  15 megabytes

l  Use *of* to add a modifier to a measurement used as a noun. Example:

The operation requires 200 MB of available hard-drive space.

l  Use commas in numbers that have four or more digits, regardless of how the numbers appear in the UI. Example:

Ø  1,024 MB

| Term                 | Abbreviation | Usage                                                        |
| -------------------- | ------------ | ------------------------------------------------------------ |
| bits per pixel       | bpp          |                                                              |
| bits per second      | bps          | Don't use as a synonym for baud. See  Units of measure term collection for information about baud. |
| byte                 | None         | Don't  abbreviate.                                           |
| exabyte              | EB           | Don’t use E, E byte, or EByte.                               |
| gigabit              | None         | Don’t  abbreviate.                                           |
| gigabits per second  | Gbps         | Don't spell out as *Gb per second*.                          |
| gigabyte             | GB           | Don’t use *G, G byte,* or *GByte*.                           |
| kilobit              | *None*       | Don’t abbreviate.                                            |
| kilobits per second  | Kbps         | Don't spell out as *KB per second*.                          |
| kilobyte             | KB           | Don't use *K, K byte,* or *KByte*.                           |
| kilobytes per second | KBps         | Don't spell out as *KB per second*.                          |
| megabit              | *None*       | Don’t abbreviate.                                            |
| megabits per second  | Mbps         | Don't spell out as *Mb per second*.                          |
| megabyte             | MB           | Don’t use *M, meg, M byte,* or *MByte*.                      |
| megabytes per second | MBps         | Don't spell out as *MB per second*.                          |
| petabyte             | PB           | Don’t use *P, P byte,* or *PByte*.                           |
| terabyte             | TB           | Don’t use *T, T byte,* or *TByte*.                           |
| zettabyte            | ZB           | Don’t use Z, Z byte, or ZByte.                               |

## 1.8            Safety Instructions

**Definitions**

Safety instructions tell the readers that procedures or steps in procedures can be dangerous or cause damage. The words and definitions that follow agree with the specifications for technical publications that are applicable to aerospace and defense:

l  A **warning** tells the reader that there is a risk of **injury or death**.

l  A **caution** tells the reader that there is a risk of **damage to objects**.

It is possible that other industries use different words or categories for safety instructions. If you use different words (for example, “danger”, “attention”, or “notice”) or graphical symbols, always make sure that contents obey the principles of the following rules. For more information, refer to:

l  ANSI Z535.6 American National Standard for Product Safety Information in Product

Manuals, Instructions, and Other Collateral Materials

l  ISO 3864-2 Graphical symbols - Safety colors and safety signs.

**How to write safety instructions**

l  Use an applicable word (for example, “warning” or “caution”) to identify the level of risk. Do an accurate risk analysis to decide if there is a risk of injury or death to persons (warning), or if there is a risk of damage to machines, tools or equipment (caution), or both.

l  Start a safety instruction with a clear and simple command or condition. Your reader must know what to do to prevent accidents and keep a high level of safety. If your reader must know about a specific condition before the start of a procedure or work step, give this condition first.

l  Give an explanation to show the specific risk or possible result. If possible, always tell your reader what can occur if the safety instruction is not obeyed. If the danger is clearly specified, the person who does the task will understand the risk and be more careful.

## 1.9  Glossary 

A glossary, where one is included in a document, is included at the end of a document before the index. The glossary contains words, phrases, and terms from the document text that require clarification; these include technical terms, expanded acronyms, and so on. 

**Glossary Rules and Contents** 

Use the following rules to produce a glossary: 

l  Arrange the glossary as follows: 

\1. Numerical entries in order 

\2. Alphabetical entries in order 

l  All terms in the glossary must appear exactly as they appear in text. 

l  Include an expansion of any acronym added to the glossary. 

l  Include a definition of any term added to the glossary. 

l  Add a link for each glossary item. Example: [GUI](#GUI), [ISO](#ISO)

 

**Glossary Examples** 

| GUI  | Graphical User Interface  An interface between the software  and the user that takes advantage of the graphical capabilities of the  computer. |
| ---- | ------------------------------------------------------------ |
| ISO  | International Organization for  Standardization  A global network of national  standard organizations that identifies and promotes international standards. |

 

# 2. Procedural Writing 

## 2.1 General Rules

- **Action-based Heading.** To describe activities or suggest actions, use **task-oriented headings** that contain a **verb**—either **present tense or in gerund (-ing) form**. Present tense works well for headings that identify steps in a process. Examples:
  - Adding an account 

  - Add an account

- 
  Step rule: general


## 2.2            GUI-Based Task Topic

### 2.2.1        Steps Rules

1. Write short sentences. Use **a maximum of 20 words** in each sentence.

2. Write **only one instruction in each sentence** unless two or more actions occur at the same time. 

3. The **operation result** should follow the operation step. The result cannot act as a separate step and cannot be placed at the beginning of next step.

4. Write instructions in the **imperative (command) form**.

5. If you start an instruction with a descriptive statement (dependent phrase or clause), divide that statement from the command with a comma.

6. Write **notes** only to **give information, not instructions**.

7. **Limit a procedure to seven steps**, and preferably fewer. Try to fit all the steps on the same screen.

8. **Abbreviate simple sequences by using right angle brackets**. Include a space before and after each bracket, and don't make the brackets bold.

   Example: Select **Accounts** > **Other accounts** > **Add an account**.

9. When there's an **ellipsis** in UI, **don’t include it in instructions or procedures**.

**10.**  If a step is optional, add **(Optional)** at the beginning.

11. Most of the time, include actions that finalize a step, such as **OK** or **Apply** buttons.

12. For operational steps, it is recommended to use the following patterns:

- Condition + time + place + operational steps + purpose + brief information + result 

- (Optional) Purpose + time + place + operational steps + brief information + result


Examples:

- In the XX area, select xxx. The xxx dialog box is displayed, see Figure x-x.

- In the **Path** text box, enter the path and name of the file from which you want to import the template. You can also click **Browse** to select the file.

- (Optional) To display the current settings of this link, click **Query**.


(Note that the position of Purpose is different.)

### 2.2.2  Formatting Text in Instructions  

Consistent text formatting helps readers locate and interpret information. Follow these conventions for formatting elements that frequently appear in instructions (also referred to as procedures).

#### 2.2.2.1      In Documentation and Technical Content

Use these conventions in instructions that appear in documentation and technical content.

| ELEMENT                                                    | CONVENTION                                                   | EXAMPLE                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Blades**                                                 | Avoid talking about blades.   Instead, describe what the customer needs to do.    When   you must refer to a blade by name, use bold formatting for the name of the   blade.    Use   sentence-style capitalization unless you need to match the UI. Don't include   the word *blade*   unless it adds needed clarity. | Select   a specific operation to view details about that operation.    In   **Web   app**[[u3\]](#_msocom_3) , provide a name for your site.   Go   to **Audit   logs** to view the events that occurred against   the subscription.   On   the **Resource   group** blade, select **Summary**. |
| **Buttons,**    **check boxes, and other options**         | Avoid talking about UI elements.   Instead, describe what the customer needs to do.    When you must refer to a button,   check box, or other option, use bold formatting for the name. Use   sentence-style capitalization unless you need to match the UI. If an option   label ends with a colon or an ellipsis, don't include that end punctuation   in instructions.    Don't   include the type of UI element, such as *button* or *check box,* unless including it adds needed   clarity. | Select **Save as** (*not* Select **Save as…** or Select the **Save as**   button).    Select **Allow row to break across pages**.    Clear   the **Match   case** check box. |
| **Command-line commands**                                  | Bold.   All lowercase.                                       | **copy**                                                     |
| **Command-line options (also known as switches or flags)** | Bold.   Capitalize the way the option must be typed.         | **/a**   **/Aw**                                             |

| **Commands**                                            | Use bold formatting for command  names.  Use  sentence-style capitalization unless you need to match the UI. If a command  label ends with a colon or an ellipsis, don't include that end punctuation in  instructions.  Don't  include the word *command*  unless it adds needed clarity. | Go to **Tools**, and select **Change language**.  On the **Design** menu, select **Colors**,  and then select a color scheme. |      |
| ------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| **Database  names**                                     | Bold. The capitalization of database  names varies.          | **WingtipToys**  database                                    |      |
| **Device  and port names**                              | All uppercase.                                               | USB                                                          |      |
| **Dialog  boxes**                                       | Avoid  talking about dialog boxes. Instead, describe what the customer needs to do.  When  you must refer to a dialog box by name, use bold formatting for the name of  the dialog box.   Use sentence-style capitalization  unless you need to match the UI. If a dialog box label ends with a colon or  an ellipsis, don't include that end punctuation in instructions. Don't  include the words *dialog  box* unless it adds needed clarity. | Select  **Upload**,  and then select a file to upload.  In **Properties**,  select **Details**,  and then select **Remove  Properties and Personal Information**.   In  the **Protect  document** dialog box, clear the **Shapes**  check box. |      |
| **Error  messages**                                     | Sentence-style  capitalization. Enclose error messages in quotation marks when referring to  them in text. | We can't find a scanner.  Hmm ... looks like that's a broken link.  If you see the error message,  "Check scanner status and try again," use Windows Update to check  for the latest drivers for your device. |      |
| **File  attributes**                                    | All lowercase.                                               | To  remove the hidden attribute from all files in a folder .... |      |
| **File  name extensions**                               | All lowercase.                                               | .mdb   .doc                                                  |      |
| **File  names (user-defined examples)**                 | Title-style capitalization. It's OK  to use internal capital letters in file names for readability. Use bold  formatting for file names in procedures if you're directing the customer to  select, type, or otherwise interact with the name. | My Taxes for 2016   MyTaxesFor2016   Enter **MyTaxesFor2016**. |      |
| **Folder  and directory names (user-defined examples)** | l   Sentence-style capitalization.   l   It's OK to use **internal capital letters** in folder and directory names for  readability.   l   In **procedures**, use **bold  formatting** for names if you're directing the customer to select, type, or  otherwise interact with the name. | Vacation and Sick Pay   MyFiles\Accounting\Payroll\VacPay Select **Documents**. |      |
| **Key names,  combinations, and sequences**             | l  Capitalize.   l  Use **bold formatting** for key names and  keyboard shortcuts in **instructions**.    l  Don't put a  space around the plus sign (+) in keyboard shortcuts.   l  To learn how to  refer to keyboard shortcuts and specific keys, see Keys and keyboard shortcuts term  collection. | Shift, F7   Ctrl+Alt+Del   Alt, F, O   Spacebar   Select the **F1** key.   To open the **Preview**  tab, select **Alt+3**. |      |
| **Macros**                                              | l  Usually all **uppercase**.   l  Use bold  formatting if predefined.  l  MASKROP  l  Might be  monospace if user defined.   l  Treatment  varies. | **LOWORD**                                                   |      |
| **Markup  language elements (tags)**                    | Bold.   Capitalization varies.                               | **<img>**   **<input  type=text>**   **<!DOCTYPE  html>**    |      |
| **Mathematical  constants and variables**               | Italic.                                                      | *a2  + b2 = c2*                                              |      |
| **Menus**                                               | Avoid talking about menus. Instead,  describe what the customer needs to do.   When  you must refer to a menu by name, use bold formatting for the name of the  menu.   Use  sentence-style capitalization unless you need to match the UI. Don’t include  the word *menu*  unless it adds needed clarity. | Go to **Tools**, and select **Change language**.   On the **Design** menu, select **Colors**,  and then select a color scheme. |      |
| **New  terms**                                          | Italicize  the first mention of a new term if you're going to define it immediately in  text. | Microsoft Exchange consists of both *server*  and *client*  components. |      |
| **Palettes**                                            | Avoid talking about palettes.  Instead, describe what the customer needs to do.   When  you must refer to a palette by name, use bold formatting for the name of the  palette.   Use  sentence-style capitalization unless you need to match the UI. Don't include  the word *palette*  unless it adds needed clarity. | In **Colors**, let Windows pull an accent color  from your background, or choose your own color.   In the **Color** palette, select a color for the  object outline. |      |
| **Panes**                                               | Avoid talking about panes. Instead,  describe what the customer needs to do.   When  you must refer to a pane by name, use bold formatting for the name of the  pane.   Use  sentence-style capitalization unless you need to match the UI. Don't include  the word *pane*  unless it adds needed clarity. | Select  the arrow next to the **Styles**  gallery, select **Apply  styles**, and then select a style to modify. If the **Apply Styles**  pane is in your way, just move it. |      |
| **Placeholders  (in syntax and in user input)**         | Italic.                                                      | /v: *version*  Enter *password*.                             |      |
| **Products,  services, apps, and trademarks**           | Usually title-style capitalization.   Check the [Microsoft trademark list ](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/en-us.aspx)for  capitalization of trademarked names. | Microsoft Arc Touch Mouse   Microsoft  Word   Surface Pro   Notepad   Network Connections   Makefile   RC program |      |
| **Slashes**                                             | When instructing customers to enter  a slash, include the spelled-out term (*backslash* or *slash*), followed by the symbol in  parentheses. | Enter two backslashes (\\) ....                              |      |
| **Strings**                                             | When referring to strings in code, a  document, a website, or UI, use sentence-style capitalization unless the text  you’re referring to is capitalized differently. Enclose in quotation marks. | Select "Now is the time."   Find  “font-family:Segoe UI Semibold” in the code. |      |
| **Tabs**                                                | Avoid talking about tabs. Instead,  describe what the customer needs to do.   When  you must refer to a tab by name, use bold formatting for the name of the tab.    Use  sentence-style capitalization unless you need to match the UI. Don't include  the word *tab* unless  it adds needed clarity. | Select  the table, and then select **Design**  > **Header  row**.   On the **Design** tab, select **Header row**.   Go to the **Deploy** tab. In the **Configuration**  list, …. |      |
| **Toggles**                                             | Avoid talking about toggles.  Instead, describe what the customer needs to do.   When  you must refer to a toggle by name, use bold formatting for the name of the  toggle.   Use  sentence-style capitalization unless you need to match the UI. Include the  word *toggle* if  it adds needed clarity. | To  make text and apps easier to see, turn on the toggle under **Turn on high contrast**.   To keep all applied filters, turn on the **Pass all filters**  toggle. |      |
| **URLs**                                                | l   All **lowercase** for complete URLs.   l   If necessary, line-break long URLs  before a slash.   l  Don’t  hyphenate. | www.microsoft.com  msdn.microsoft.com/downloads              |      |
| **User  input**                                         | Usually lowercase, unless case  sensitive. Bold or italic, depending on the element. If the user input string  contains placeholder text, use italic for that text. | Enter **hello world** Enter **-p** *password*                |      |
| Windows                                                 | Avoid talking about windows.  Instead, focus on what the customer needs to do.  When you must refer to a window by name, use regular text.   Use sentence-style capitalization unless  you need to match the UI.  Use window only as a generic term for an area on a PC screen  where apps and content appear. Don’t use  window to refer to a specific dialog box, blade, or similar UI  element. | To embed the new object, switch to the source document.   Easily switch between open windows. Open a new Microsoft Edge  tab in a new window so you can look at tabs side by side. |      |
| XML schema elements                                     | Bold. Capitalization varies.                                 | **ElementType** element   **xml:space** attribute            |      |
|                                                         |                                                              |                                                              |      |

#### 2.2.2.2  In the UI and general content

Instructions can also appear in the UI itself and in content other than documentation, such as blogs and marketing. **In this content, avoid bold and italic formatting.** The goal is to be readable and friendly but also clearly set off the UI label or other text element from the surrounding text.

Choose one of the approaches below and use it consistently.

| OPTION                                                       | EXAMPLE                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Describe the action **without referring to a specific UI label.** | Choose the group or groups that you want to  assign services to. |
| Use wording that clearly sets off  the name of the element.  | Assign services to the Business data  only group.  By selecting the Create my database  button, you agree Microsoft can use entity and field names you create to help  improve our common data model.  Choose how often you want to refresh  data in Schedule refresh. |
| Use quotation    marks. Quotation marks can make text cluttered, **so use them sparingly and only when necessary for clarity.**            Assign    services to the “No business data allowed” group. | Assign services to the “No business data  allowed” group.    |
| Use bold formatting.                                         | Assign services to either the **Business data only** or  **No  business data allowed** group. |

### 2.2.3 Keys and Keyboard Shortcuts (P58)

This term collection covers how to refer to keyboard shortcuts and the names of specific keys. For information about describing customers' interactions with UI, see Procedures and instructions.

#### 2.2.3.1 Keyboard Actions and Access

| Term                                                         | Usage                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **keyboard  shortcut, accelerator key, fast key, hot key, quick key, speed key** | In general, use *keyboard shortcut* to  describe a combination of keystrokes used to perform a task.   **Example**  Alt+Ctrl+S    Don't  use *accelerator  key, fast key, hot key, quick key,* or  *speed  key.* |
| **access  key**                                              | Don't  use in content for a general audience. Use *keyboard shortcut* instead.   In content for developers or content about  customizing the UI, it's OK to distinguish between an *access key*  and a *shortcut  key*.   l  An  access key is a letter or number that users select to access UI controls that have text labels.   For  example, the *F* in  Alt+F.   l  A  shortcut key is a key or key combination that users select to perform a common action.   For  example, Ctrl+V.   If  you use these terms, explain the difference. |
| **Key  Tip**                                                 | In  general, don't use in content for a general audience. Use *keyboard shortcut*  instead.   In content teaching basic skills or  content for a technical audience, it's OK to use *Key Tip* to refer to the letter or number  that appears in the ribbon when the Alt key is pressed. |
| **key  combination**                                         | Don't  use in content for a general audience. Use *keyboard shortcut* instead.  In content for a technical audience,  it's OK to distinguish between a *key  combination* (two or more keys selected simultaneously)  and a *key  sequence* (two or more keys selected sequentially).  If you use these terms, explain the difference. |
| **key  sequence**                                            | Don't  use in content for a general audience. Use *keyboard shortcut* instead.  In content for a technical audience,  it's OK to distinguish between a *key  sequence* (two or more keys selected sequentially)  and a *key  combination* (two or more keys selected simultaneously).  If you use these terms, explain the difference. |
| **keypad**                                                   | Use *numeric keypad* on the first mention. Don't use *keypad* by  itself unless the context has been established and there's no possibility the  customer will confuse the keypad with the keyboard. When in doubt, continue  to use *numeric  keypad*.   In general, don't distinguish  between the keyboard and the numeric keypad. When the customer can select two  keys that look the same, direct the customer to the correct key.   **Example**  Select the Minus sign on the numeric keypad,  not the Hyphen key on the keyboard. |
| **keystroke,  keypress**                                     | Don't use *keypress*. Use *keystroke* instead.               |
| **select,  press, depress, hit, strike, use**                | Use select to describe pressing a key on a  physical or onscreen keyboard. Don't use press, depress, hit, or strike.  Don't use depressed to describe an indented  toolbar button unless you have no other choice.  Use use when select might be confusing, such  as when referring to the arrow keys or function keys and select might make  customers think that they need to select all the arrow keys simultaneously.  Example  Use the arrow keys to move around the text.  Use use when multiple platform or peripheral  choices initiate the same action or actions within a program.   Example  Use the controls on your keyboard or  controller to run through the obstacle course.   Be specific when teaching beginning skills.   Example  To run through the obstacle course, select  the Spacebar on the keyboard or pull the right trigger on the Xbox  controller.   Consider using a table to present  instructions that have more than two alternatives.  Use select and hold only if a delay is built  into the software or hardware interaction. Don't use select and hold when  referring to a mouse button unless you're teaching beginning skills.   See also Describing interactions with UI,  Mouse and mouse interaction term collection |
| **shortcut  key**                                            | Don't use in content for a general  audience. Use *keyboard* *shortcut*  instead.     In content for developers or content about  customizing the UI, it's OK to distinguish between an access key and a  shortcut key. An access key is a letter or number that users select to access  UI controls that havetext labels. For example, the F in Alt+F. A shortcut key  is a key or key combination that users select to perform a common action. For  example, Ctrl+V. If you usetheseterms, explain the difference |

#### 2.2.3.2      Key names

l  In general, use **sentence capitalization** for key names.

**Examples**

the Shift key 

the Page up key

l  Capitalize letter keys in general references.

**Example**

the K key

l  **Lowercase and bold a letter key** when **instructing** customers to **enter the letter** (unless you're instructing them to enter a capital letter).

**Example**

enter **k**

l  On the first mention, you can use the **definite article** ***the\*** and the word ***key\*** with the key name if necessary for clarity. On subsequent mentions, refer to the key by its name only.

**Example** 

Select the **F1** key.

Select F1.

 

If you need guidance for a key name that isn't on this list, **use sentence capitalization and spell it as it appears on the keyboard**.

| Term                                                         | Usage                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Alt**                                                      | **Capitalize**.  Use to refer to the *Alt  key*.             |
| **Application  key**                                         | **Capitalize**.  Use *the  Application key* to refer to the key that opens a shortcut  menu containing commands related to a selection. |
| **arrow  keys, direction keys, directional keys, movement keys** | Arrow keys are labeled only with an arrow.  Refer to similar keys on the numeric keypad as *the arrow keys on the numeric keypad*.  Use **sentence  capitalization** to refer to a specific arrow key: *the Left arrow key,  the Right arrow key, the Up arrow key,* or *the Down arrow key*.   It’s OK to use *arrow key* as a general term for any single  arrow key. Include *the*  and *key* in  references to a specific arrow key except in key combinations or key  sequences.  Don’t use  *direction keys, directional keys,* or *movement keys*.  Use  specific names to refer to other navigational keys, such as *Page up, Page down,  Home,* and *End*. |
| **asterisk  (\*), star**                                     | Use  *asterisk* to  refer to the * symbol.  An  asterisk is used to indicate multiplication in a programming language or as a  wildcard character representing one or more characters.  It’s OK to use *star* to  refer to the key on a phone keypad. |
| **at  sign (@)**                                             | Pronounced *at*. In most cases, don’t  spell out.            |
| **Back**                                                     | Capitalize. Use to refer to the *Back key,*  which performs the same action as the Back button in a browser. |
| **Backspace**                                                | Capitalize. Use to refer to the *Backspace key*.             |
| **backtab**                                                  | Don’t use to refer to the Shift+Tab keyboard  shortcut.      |
| **Break  caps**                                              | Use sentence capitalization. Use to  refer to the *Break  caps key*. |
| **Caps  lock**                                               | Use **sentence capitalization**. Use to refer to the *Caps lock key*. |
| **comma  (,)**                                               | **Spell  out** ***comma\***  **when referring to a key or the punctuation mark.**   **Capitalize**  ***Comma\***  **when instructing a reader to select the key. Include the symbol in parentheses**  when needed for clarity. |
| **Command**                                                  | Capitalize.  Use to refer to the *Command  key* on the Mac keyboard. Use the bitmap to show  this key if possible. It isn't named on the keyboard. |
| **Control**                                                  | **Capitalize**.  Use to refer to the *Control  key* on the Mac keyboard. |
| **Ctrl**                                                     | **Capitalize**.  Use to refer to the *Ctrl  key*. Don’t use for the Mac keyboard. |
| **Del**                                                      | Capitalize. Use to refer to the *Del key*.  On the Mac keyboard only, use to refer to the *forward delete key*. |
| **Delete**                                                   | Capitalize. Use to refer to the *back delete key* on  the Mac keyboard. |
| **End**                                                      | Capitalize. Use to refer to the *End key*.                   |
| **Enter**                                                    | Capitalize.  Use to refer to the *Enter  key*. On the Mac, use only when functionality  requires it. |
| **Esc**                                                      | Always use *Esc,* not *Escape*.                              |
| **F1–F12**                                                   | Capitalize the *F*.  Don't add a space between the *F*  and the number. |
| **Forward**                                                  | Capitalize. Use to refer to the *Forward key,*  which performs the same action as the Forward button in a browser. |
| **Help**                                                     | Use *the Help key* only to refer to the key on the Mac  keyboard. |
| **HELP  key**                                                | Use  *the  HELP key* to avoid confusion with the Help button.  Always include *the*  and *key*. |
| **Home**                                                     | Capitalize. Use to refer to the *Home key*.                  |
| **hyphen  (-)**                                              | **Spell  out** ***hyphen\***  **when referring to a key.** **Capitalize** ***Hyphen\*** **when instructing a reader to select  the key.** Include the symbol in parentheses when  needed for clarity. |
| **Insert**                                                   | Capitalize. Use to refer to the *Insert key*.                |
| **Lock  clear**                                              | Capitalize. Use to refer to the *Lock clear key*.            |
| **minus  sign (–)**                                          | Spell  out *minus  sign* when referring to a key. Use sentence  capitalization **(*****Minus  sign\*****)**  when instructing a reader to select the key. Include the symbol in  parentheses when needed for clarity. |
| **Num  lock option**                                         | Use  sentence capitalization. Use to refer to the *Num lock option key* on the Mac keyboard. |
| **number  sign (#), pound key, hashtag**                     | Use  *# key* to  describe the key.  It's OK to use *pound key (#)**,*  including the symbol in parentheses, to refer to  the keypad on a telephone. It's OK to use *hashtag (#)* to describe the use of the # key to identify  a metadata term in social media. |
| **numeric  keypad, keypad, numerical keypad, numeric keyboard** | Use *numeric keypad* on  first mention. Don't use *keypad* by  itself unless there's no possibility of confusion with the keyboard. Don't use *numerical keypad* or *numeric keyboard*.  In general, don't distinguish  between the keyboard and the numeric keypad. If a customer can select two  keys that look the same, specify the correct key.   **Example**  Select the Minus  sign on the numeric keypad. |
| **on-screen keyboard, keyboard  display, soft keyboard, virtual keyboard, visual keyboard** | Use  to describe the keyboard representation on the screen that the customer  touches to enter characters.   Hyphenate  *on-screen keyboard*. Don't use *virtual keyboard, soft  keyboard, visual keyboard,* or *keyboard display*. |
| **Page  down, Page up**                                      | Use **sentence capitalization**. Use to  refer to the *Page  up key* and the *Page down key*. |
| **Pause**                                                    | Capitalize. Use to refer to the *Pause key*.                 |
| **period  (.)**                                              | Spell  out *period* when referring to a key.   Capitalize  *Period* when instructing a reader to select the  key. Include the symbol in parentheses when needed for clarity. |
| **plus  sign (+)**                                           | Spell  out *plus sign* when  referring to a key.   Use  sentence capitalization (*Plus  sign*)  when instructing a reader to select the key. Include the symbol in  parentheses when needed for clarity. |
| **Print  screen**                                            | Use **sentence capitalization**. Use to refer to the *Print screen key*. |
| **Reset**                                                    | Capitalize. Use to refer to the *Reset key*.                 |
| **Return**                                                   | Capitalize. Use to refer to the *Return key* on  the Mac keyboard. |
| **Scroll  lock**                                             | Use sentence capitalization. Use to  refer to the *Scroll  lock key*. |
| **Select**                                                   | Capitalize. Use to refer to the *Select key*.                |
| **Shift**                                                    | **Capitalize**.  Use to refer to the *Shift  key*.           |
| **Spacebar**                                                 | **Capitalize**.  Use to refer to the *Spacebar*. Always precede with *the*  except in procedures, key combinations, and key sequences. |
| **Tab**                                                      | Capitalize. Use to refer to the *Tab key*.  Always use *the*  and *key*  except in key combinations and key sequences. |
| **Windows  logo key**                                        | Capitalize *Windows*.  Use to refer to the *Windows  logo key*. |

 

#### 2.2.3.3      Special character names

Because special character names could be confused with an action (such as +) or be difficult to see, **always spell out the following special character names:** ***Plus sign, Minus sign, Hyphen, Period,\* and** ***Comma\***.

To avoid confusion, it's OK to add the character in parentheses after spelling out the name. Example: 

Plus sign (+)

Use discretion. This might not be necessary for commonly used characters, such as the period (.).

To show a key combination that includes punctuation requiring use of the Shift key, such as the question mark, **use** ***Shift\* and the name or symbol of the shifted key.** Using the name of the unshifted key, such as *4* rather than *$,* could be confusing or even wrong. For example, the *?* and */* characters aren't shifted keys on every keyboard. **Always spell out** ***Plus sign, Minus sign, Hyphen, Period,\* and** ***Comma\*.** Examples:

- Ctrl+Shift+? 

- Ctrl+Shift+* 

- Ctrl+Shift+Comma


### 2.2.4  Prepositions before GUI Elements 

in the window

in the dialog box

in the right pane

in the **Proxy Server** area

in the lower left part/corner of the window

 

on the right side of the window

on the screen

on the web page

on the tab

on the toolbar

 

from the menu

from the drop-down list

 

under IP address (在IP地址设置项下)

### 2.2.5  Figure Related Rules

1. All Figures must have a number such as Figure X-X, and a title, such as Figure 1-1 XXX Dialog Box.

2. All Figures must have a **reference** to them within the body of the text. Figures are supporting data and will not be reviewed by the user unless they are referenced somewhere within the text body.

3. When referencing Figures the text should read as follows: “see Figure X-X”. The reference must be a hyperlink to the figure, regardless of how close or far the figure is originally located to the reference. In product or technical description information, “Figure x-x shows…” is also acceptable. 

4. For a GUI, the figure title format should be the interface title + the element name. For example, Edit Attribute Dialog Box.

5. Complex figure name: For figures with the same interface title but different content, the figure title can be in the format of the figure title + function/tab name. — should be used to separate the two parts. 

Example

- Figure 1-2 Edit Attribute Dialog Box—Address Setting

- Figure 2-1 Query Active Alarms Dialog Box—Location Tab

- Figure 2-2 Query Active Alarms Dialog Box—Query Result

- Figure 2-3 User Management Dialog Box—User Added


### 2.2.6        Table

#### 2.2.6.1      Table Design

1    A table should be on the same page if possible. If it is not possible, the **header line should be repeated**.

2    No more than three colors should be used in one table. It is better if **no more than two colors are used**.

3    If more than one table is on the same page, the **width** of each table should be the **same**, with **the left and right edges aligned with the body text** and the **maximum width no more than the page width**.

4    A table must not be an image.

#### 2.2.6.2      Table Reference

1    All **formal tables** must have a number such as Table X-X, and a title, such as Table 1-1 Real-time Query Conditions Parameters.

2    All **formal tables** must have a **reference** to them within the body of the text. Tables are supporting data and will not be reviewed by the user unless they are referenced somewhere within the text body.

3    When referencing Tables the text should read as follows: “**For …, refer to Table X-X**”. For example, For a description of the parameters, refer to Table 3‑1.

4    The reference must be a **hyperlink** to the table, regardless of how close or far the table is originally located to the reference.

#### 2.2.6.3  Text Requirement for Table

1    Use a **hyphen** (-) to indicate an empty cell in a table.

2    If the contents in two cells are the same, **repeat the contents**, and do not use “ditto”, “the same as stated above” or any other thing similar.

3    For nouns in the **header line**, use their **single-forms.** The header line uses the same capitalization as titles

#### 2.2.6.4  Parameter Description Table

1    Table name: **XX Parameter Descriptions** if the total title is no more than four words and the meaning is clear. For other cases, table titles use “**Parameter Descriptions for** **xxxx**”.

2    Description row: 

**Option1:** 

*[Meaning, a phrase],* *[required/optional], [parameter type], [range: xxx*–*xxx], [default: xxx], [xxx, a phrase][.]*

*[*Additional information.*]*

*[*How to set*.]*

**Option2:** 

*[Purpose, a sentence with the subject omitted, for example: [Sets xxx].* *[Required/Optional], [parameter type], [range: xxx-xxx], [default: xxx], [xxx, a phrase].*

*[*Additional information.*]*

*[*How to set*.]*

a      The first line describes the **attributes** of the parameter.

b      Following lines describe additional information, for example relations with other parameters, cautions for setting this parameter.

c      The last line describes how to set the parameter. The imperative mood or a sentence with the subject being You must be used.

d      If any cell in a column contains a full stop, every line in every cell in this column must be ended with a full stop, no matter it is a full sentence or just a phrase.

e      You do not have to list all the options of a parameter of enumeration type, unless detailed information about the options is given. The list of options should be listed in the same order as they are listed in the screen and in the same place as the value range.

f      If some information in a Description cell is duplicate with another cell or can be easily known from other information, this information can be omitted. For example, the parameter meaning can be omitted if it is duplicated with or can be easily known from the parameter name.

**Range examples:** 

- l  String type, range: 5–20 digits

- l  Range: 1–255 characters (A–Z, a–z, 0–9)

- l  Range: any valid IP address

- l  String type, range: 9–64 hexadecimal digits

- l  Hexadecimal integer type, range: 0x0000000000–0xFFFFFFFFFF




- l  Range: 0, 1, 128–255

- l  Date type, range: 2008-01-01 through 2599-12-31

- l  Character type, options:
  - F: Female
  - M: Male

- Character type, range: F, M


#### 2.2.6.5 Branch Steps Table

Branch steps are used if different operations need to be done in accordance with different purposes or conditions. The following are two examples of branch steps:

Example 1:

| **To****…**                         | **Do****…**                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| Insert an image from a file         | 1．Click the  place when you want to insert the image.  2．Select **Insert** > **Image** > **From File**.  3．Select the image file, and click **Insert**. |
| Insert an image from the  clipboard | Click the place when you want to  insert the image, and do any of the following:  l   Select  menu **Edit** > **Paste**.  l   Press  Ctrl+V.  l   Right-click  and select **Paste** from the  shortcut menu. |

 

Example 2:

| **If**…                    | **Then**…                                                    |
| -------------------------- | ------------------------------------------------------------ |
| The BSC  ID does not exist | 1. Select the **BSC ID** check  box.  2. Click **OK**.  3. Click **Next**. |
| The BSC ID already exists  | Click **Next**.                                              |

 

Abide by the following rules when using branch steps:

1. For branch steps to be done in accordance with **purposes** only, **use “To…” and “Do…” in the header line.** Use imperative mood in the cells.

2. For branch steps to be done in accordance with conditions only, use “If…” and “Then…” in the header line. Use imperative mood in the “Then…” cells.

3. If there are both conditions and purposes, use “If…” and “Then…” in the header line. For the purposes, use “You want to xxx” in the “If…” cells.

4. Text in each cell must be initial capital. **Punctuation must not be used at the end of any “If…” or “To…” cell.**

## 2.3  Programming Guide Topic (MML-Based Task Topic) 

### 2.3.1  Programming Guide/Register Control Flow部分(Step+Block)

Example: 

Enabling the Clock and the Data Path

This section describes how to XXX.

1    Select a path for an ADC through register XXX. 

aud_glb_reg.AUDIF_GLB_EB->{

  Sdm_adc5_eb   = adc_sel[5]

2    Configure register XXX.

aud_glb_reg.AUDIF_GLB_EB->{

  Sdm_adc4_eb   = adc_sel[4]

### 2.3.2  Q&A/Application Note/Troubleshooting部分

结构1：

- Analysis 

- Solution




结构2：

- Background：(Optional) 故障可能涉及到的背景知识

- Symptom 故障症状：
  - 当描述用户在进行某一个操作中会遇到什么错误时，用when或if引出此场景。
  - **时态用现在时**，表示假定的一个普遍的操作，而不是特定某一个过去的场景。
  - 描述是一个完整的句子，不省略冠词、虚词和主语。

- Probable Cause：用无序列表列出所有原因

- Impact：(Optional) 故障对系统的影响

- Action：用祈使句




# 3. Descriptive Writing

## 3.1  Content Structure

Descriptive writing gives information, not instructions. Descriptive writing can be:

- A description of an item, a product, a system, or a component, its function, how it is made and how it operates

- A text that gives general information

- A note in a procedure


### 3.1.1 Give Information Gradually

In a descriptive text, **give information gradually and make sure that each sentence contains only one topic**. If you give too much information too quickly, your text will be difficult to understand and it will be necessary for the reader to read it again.

### 3.1.2 Use Key Words and Phrases to Organize Your Text Logically

Key words and phrases give structure to a text. 

Key words are words that often occur in a text to connect different ideas. 

Key phrases have the same function. 

Such words and phrases **show how information in a text is related** and give the text a logical structure. 

You can also use **connecting words and phrases** to help the reader understand the **progression of ideas** in the text. 

They function as **traffic signs** and tell the reader **if the information is new, or different, or a conclusion based on preceding facts**. 

Examples of such connecting words and phrases are: “and”, “but”, “thus”, “at the same time”, “as a result”, and many others.

## 3.2 Sentences

Write short sentences. Use **a maximum of 25 words** in each sentence.

Good technical writing uses short sentences for all types of topics (simple and complex). Short sentences make your writing stronger and information easier to understand.

In descriptive writing, the maximum sentence length is 25 words. This is because descriptive text is more complex than procedural text.

## 3.3  Paragraphs

- Use **paragraphs** to show **related information**.
  - In procedures, work steps have numbers and letters to show their sequence. In descriptive writing, **paragraphs** keep related information together and organize the text into a logical sequence. 
  - In STE, a paragraph starts with a **“topic sentence”** which tells the reader what the topic of that paragraph is. Then, the sentences that follow the topic sentence explain it or give additional information to support it.
  - When a new paragraph starts, the reader knows that there will be new or different information in that paragraph. 

- Make sure that each paragraph has **only one topic**.
  - The topic sentence is the first and most important sentence in a paragraph. The topic sentence gives new information and makes a logical connection between it and previous information.
  - To do this, **the topic sentence usually contains a key word and/or a connecting word or phrase.** From the topic sentences, the reader will understand the contents of your text and will find specific information quickly. **If the reader writes down each of the topic sentences from a text, they should make a good outline of its content.** 
  - The other sentences in each paragraph give additional information that supports or develops the topic of the paragraph.

- Make sure that **no paragraph** has more than **six sentences**.









