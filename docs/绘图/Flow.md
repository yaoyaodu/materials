# 1 流程图 (Flow)

标准流程图

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
```



标准流程图（横向）



```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
```









# 2 流程图（Mermaid-graph）

graph:

Possible FlowChart orientations are:

- TB - top to bottom
- TD - top-down/ same as top to bottom
- BT - bottom to top
- RL - right to left
- LR - left to right

Links between nodes: 

* A link with arrow head: A-->B
* An open link: A --- B
* A---|This is the text|B
* A-->|text|B
* Dotted link: A-.->B
* Dotted link with text: A-. text .-> B



```mermaid
graph LR
A[方形] -->B(圆角)
    B --> C{条件a}
    C -->|a=1| D[结果1]
    C -->|a=2| E[结果2]
    F[横向流程图]
```





```mermaid
graph TD
A[方形] -->B(圆角)
    B --> C{条件a}
    C -->|a=1| D[结果1]
    C -->|a=2| E[结果2]
    F[竖向流程图]
```

```mermaid
graph LR
	good-->bad
	today---tomorrow
	C---|text|D
	E-->|text|F
	A--text---B
	G-- text -->H
	J-.->K
	L-. text .-> M
	O ==> P
	Q == text ==> R
```





```mermaid
graph LR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

```mermaid
graph TD
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```



flowchart:



```mermaid
flowchart TD
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

```mermaid
flowchart LR    
	A --o B    
	B --x C
```

```mermaid
flowchart LR
    A o--o B
    B <--> C
    C x--x D
```

```mermaid
graph TD
    A[Start] --> B{Is it?};
    B -->|Yes| C[OK];
    C --> D[Rethink];
    D --> B;
    B ---->|No| E[End];
```







```mermaid
graph LR
    id
    id1[This is the text in the box]
    id2(This is the text in the box)
    id3([This is the text in the box])
    id4[[This is the text in the box]]
    id5[(Database)]
    id6>This is the text in the box]
    id7((This is the text in the circle))
    id8[/This is the text in the box/]
    id9[\This is the text in the box\]
    A[/Christmas\]
    B[\Go shopping/]
    C{Decision}
    d{{This is the text in the box}}
    id10["This is the (text) in the box"]
```



```mermaid
graph 
    id
    id1[This is the text in the box]
    C{Decision}
```





















# 3 时序图 Sequence Diagram

->>带箭头

->直线

```mermaid
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
    Alice->>John: See you later!
```



```mermaid
sequenceDiagram
    Alice->John: Hello John, how are you?
    loop Every minute
        John-->Alice: Great!
    end
```







```mermaid
sequenceDiagram
	autonumber
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    Note over Alice,John: A typical interaction
    John-x Bob: How about you?
    activate Bob
    Bob--x John: Jolly good!
    deactivate Bob
```

There are six types of arrows currently supported:

| Type | Description                                      |
| ---- | ------------------------------------------------ |
| ->   | Solid line without arrow                         |
| -->  | Dotted line without arrow                        |
| ->>  | Solid line with arrowhead                        |
| -->> | Dotted line with arrowhead                       |
| -x   | Solid line with a cross at the end               |
| --x  | Dotted line with a cross at the end.             |
| -)   | Solid line with an open arrow at the end (async) |
| --)  | Dotted line with a open arrow at the end (async) |



# 3 状态图 State Diagram

```mermaid
stateDiagram
[*] --> s1
s1 --> [*]
```



# 4 类图 Class Diagram

<|--表示继承

+表示public

-表示private

```mermaid
classDiagram
Animal <|-- Duck
Animal <|-- Fish
Animal <|-- Zebra
Animal : +int age
Animal : +String gener
Animal : +isMammal()
Animal : +mate()
class Duck{
	+String beakColor
	+swim()
	+quack()
}
class Fish{
	+int sizeInFeet
	+canEat()
}
class Zebra{
	+bool is_wild
	+run()
}
```





# 4 甘特图



```mermaid
gantt
	title 工作计划
	dateFormat YYYY-MM-DD
	section Section
	A task: al, 2020-01-01, 30d
	Another task: after al, 20d
	section Another 
	Task in sec: 2020-01-12, 12d
	another task: 24d
```



```mermaid
%% 语法示例
        gantt
        dateFormat  YYYY-MM-DD
        title 软件开发甘特图

        section 设计
        需求                      :done,    des1, 2014-01-06,2014-01-08
        原型                      :active,  des2, 2014-01-09, 3d
        UI设计                     :         des3, after des2, 5d
    未来任务                     :         des4, after des3, 5d

        section 开发
        学习准备理解需求                      :crit, done, 2014-01-06,24h
        设计框架                             :crit, done, after des2, 2d
        开发                                 :crit, active, 3d
        未来任务                              :crit, 5d
        耍                                   :2d

        section 测试
        功能测试                              :active, a1, after des3, 3d
        压力测试                               :after a1  , 20h
        测试报告                               : 48h
```

# 5 饼图 Pie



```mermaid
pie
    title Key elements in Product A
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5
```

