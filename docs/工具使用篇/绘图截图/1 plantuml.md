@startuml
autonumber
participant 用户 #White
用户 -> 认证中心: 登录操作
认证中心 --> 缓存: 存放(key=token+ip,value=token)token
用户 <- 认证中心 : 认证成功返回token
用户 -> 认证中心: 下次访问头部携带token认证
认证中心 <- 缓存: key=token+ip获取token
其他服务 <- 认证中心: 存在且校验成功则跳转到用户请求的其他服务
其他服务 -> 用户: 信息
@enduml


@startuml
participant participant as Foo
actor actor as Foo1
boundary boundary as Foo2
control control as Foo3
entity entity as Foo4
database database as Foo5
collections collections as Foo6
queue queue as Foo7
Foo -> Foo1 : To actor
Foo -> Foo2 : To boundary
Foo -> Foo3 : To control
Foo -> Foo4 : To entity
Foo -> Foo5 : To database
Foo -> Foo6 : To collections
Foo -> Foo7 : To queue
@enduml

