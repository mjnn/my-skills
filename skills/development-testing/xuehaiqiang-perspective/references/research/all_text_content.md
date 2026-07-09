# Extracted Text Content

Generated: 2026-07-06 15:26:37
Total files: 40 (21 PPTX, 19 PDF)

---

## PPTX: VDU(C车动采)\CEA1.X\汇报文档\C车VDU埋点、One APP埋点数据链路_250218.pptx

199
195
199
176
228
252
264
145
270
317
333
324
357
40
23
20
LLM App 1st Version Commands Distribution
大模型
App
用户指令分布
[类别名称]
46%
[类别名称]
20%
[类别名称]
17%
[类别名称]
5%
[类别名称]
6%
‹#›
Textmasterformat bearbeiten
Zweite Ebene
Dritte Ebene
Vierte Ebene
Fünfte Ebene
‹#›
C
车数据处理流程的图表：
Data Source (Clusters)
：数据源（集群）。
Tech. Concept (Architecture)
：技术概念（架构）。
Data Scope (Signal list)
：数据范围（信号列表）。
Data Verification (Quality)
：数据验证（质量），对数据进行检查和验证，确保数据的质量。
Data Application (Value generation)
：数据应用（价值生成），将经过处理和验证的数据应用到实际场景中，以产生价值。
从数据获取到数据产生价值的整过程
1
C
车
VDU
数据采集传输架构图。车内多个数据采集单元（
NGX
、
LDCU
、
RDCU
、
CDCU_MCU
、
CDCU_SOC
）将数据上传至
T-Box
（车载智能终端），
T-Box
再将数据（秒级数据
&
毫秒级故障数据）上传到数据云端管理平台。
同时，客户确认数据采集声明后，通过
Consent mgmt.
（同意管理）相关操作，数据从
SWW
上传至数据云端管理平台，还存在
U
盘数据采集方式。
车内数据采集，域控制器负载采集数据并进行打包，传输至
TBOX
进行数据上传；
数据处理和打包上传，车端的
TBOX
负责处理域控制器传输数据，秒级数据上传，上传数据到车管平台；
数据云端管理平台即车管平台，部署在云端，负责配置整车上传数据、接收车端上传数据并存储
。
数据的存储处理方案，应当满足和遵循国家法律法规要求，国家标准要求。并考虑到整车
SOP
前后相关已经实施和即将实施的相关要求
；
U
盘数据采集，车辆处于唤醒状态，用户从车上
USB
口插入
U
盘，通过操作
CDCU
（Central Data Control Unit，中央数据控制单元）
进入调试模式，开启
/
停止数据录制。数据通过
CDCU
写入
U
盘中，
U
盘数据通过
PC
端上位机转换成可解析的数据文件
；
CEA One backend
透传给
JVs
的数据应具有可配置传输范围，并开放配置
API
给
JVs backend
。
CEA One backend
透传来自于
JVs
的用户确认
consent
结果给
T-Box
。
3
SVCC
（
移动互联与智能座舱运营
）
-
ChangYifei
，
2024
年全年事故车线索分析
车机信号采集数据应用，监测事故车报警以及线索下发情况，提升售后产出
4
CDC
信号数量来源
ECC
5
车机数据应用场景举例：
在车主用、修、养、换场景进行监控
6
ECC FO
更新
7
C
车车机各功能模块埋点数据，传输至埋点供应商
SDK
采集后的埋点数据传输至
各部分介绍：
外部
CP
：包含
TBD CW12
定点、
TBD
、斑马等外部内容提供商。
C
车车机
Head Unit
：有语音
SDS
、大语言模型
LLM
、场景引擎等功能模块，通过埋点供应商
SDK
（火山
/
阿里）
与后端交互，收集埋点数据。
One Backend
：由
CEA Services
和
Data Platform
构成，接收来自车机的埋点数据。
SVW SP
：包括神策分析前端和神策后台，神策后台接收全量数据以及来自
One App
的埋点数据。
One App
：产生事件
1
、事件
2
到事件
N
等数据，通过神策
SDK
和
CEA SDK
上传埋点数据 。 此架构图呈现了一个集成多种功能与数据交互的汽车智能系统，涵盖了从外部内容接入、车机功能实现到后端数据处理和分析的完整流程。
13
SVCC-
WuYawei
14
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year
| Department
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
Contact slide
As of 00. Month 2019 I Version X.X
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year
| Department
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅
色背景图像
To insert a light
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
分隔页
Divider
副标题
Subline
‹#›
分隔页
Divider
副标题
Subline
‹#›
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
Contact slide
As of 00. Month 2019 I Version X.X
2/18/2025
‹#›
2/18/2025
‹#›
2/18/2025
‹#›
2/18/2025
‹#›
2/18/2025
‹#›
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
分隔页
Divider
副标题
Subline
‹#›
分隔页
Divider
副标题
Subline
‹#›
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
2/18/2025
‹#›
1
C
车数据划分
Cluster
数据源
Cluster1
VDU
Cluster2
RTM
Cluster3
车机埋点
SDS
（
TBD
，预计
CW12
定点）
LLM
（
TBD
）
场景模式（
斑马
）
多媒体（
TBD
）
…
Cluster4
One App
数据
Other
…
Data Source
(Clusters)
Tech.
Concept (Architecture)
Data Scope (Signal list)
Data Verification (Quality)
Data Application
(Value generation)
C-
WD
Digital
Products
&
Cockpit
Page
3
RTM
法规需求介绍
数据上传要求
车辆信息上报的时间周期最大应不超过
30
s
。
数据存储要求
车载终端应将采集到的实时数据保存在内部存储介质中，车载终端内部存储的数据应具有可读性。
车载终端内部存储介质容量应满足至少
7
天的实时数据存储。
数据补发要求
车载终端通信异常时，车载终端应将采集的实时数据存储到本地存储介质中，等待通信恢复正常后进行实时数据的补发，补发数据及方式应符合
GB/T 32960.3
的相关要求。
报警数据上传要求
GB/T
32960-XXXX
新增
可充电储能装置热事件报警，电机超速报警和电机过流报警。
当车辆出现表
24
的
3
级、
4
级报警时，应上报故障发生时间点前
30
s
至报警解除时间周期内
7.2.4
规定的该车型所包括的全部数据项数据且信息采样周期不大于
1
s
，其中故
障发生前数据应以补发的形式进行传输。
动力电池下电监控要求
（
新场景
）
车辆在行驶完成下高压后或充电完成下高压后，应继续进行
7.2.4.2
、
7.2.4.3
中规定的动力电池相关数据监测及上报。下电后
1
h
内应以不小于
1
Hz
的监测频率持续监测，并上报
59
min30
s
至
1h
内
7.2.4.2
、
7.2.4.3
中规定的动力蓄电池相关数据。
定位要求
（新
）
车载终端定位要求应符合车载事故紧急呼叫系统的相关标准的规定。
AECS
使用的车载卫星定位系统应支持
GB/T
XXXX-
202X(
车载定位系统技术要求及试验方法 第
1
部分
:
卫星定位
)
规定的北斗优先或北斗单模模式，并满足
GB/T
XXXX-
202X
第
5
章除
5.5
外的全部要求。
数据安全性要求
（新
）
车载终端应配备具备硬件安全保护机制的汽车芯片。
C-
WD
Digital
Products
&
Cockpit
Page
4
RTM
其他需求
数据质量要求
应满足中国国家和地方平台对
RTM
数据质量的要求，包括但不限于以下数据质量要求
Homologation
测试相关需求
报警模拟触发
直连模式
/
转发模式切换
…
序号
RTM
数据质量指标描述
要求
１
国标数据项解析错误
单车所有检测项检测出的错误报文占比
＜3%；
单车型错误率<
10%
２
触发三级报警无定位数据（
单车在一个月内触发三级报警
后至少上传一条有效位置信息
）
车辆数<0
台
３
触发三级报警无单体数据（
车在一个月内触发三级报警后
至少上传一条有效电池单体信息
）
车辆数<0
台
４
数据延迟（单车平均延迟
5
分钟及以上
）
单车型<10%
５
数据报文补发（单车数据报文补发占比大于
20%）
单车型<
10%
6
数据空值率、异常值率、无效值率、丢包率
单车型＜1%
，单车＜
1%
12
Cluster3 C
车埋点数据链路
Cluster4 One App
埋点数据链路
SVW
13
Cluster3&4_C
车
&One APP
埋点数据链路
C
车车机
Head Unit
One Backend
SVW SP
分析前端
语音
SDS
大语言模型
LLM
场景引擎
火山
/
阿里
SDK
CW16
定点
数据湖
…
埋点数据
外部
CP
TBD
CW12
定点
TBD
斑马
…
埋点数据
Data Platform
CEA Services
全量
数据
One App
事件
1
事件
2
事件
N
SVW
SDK
埋点
数据
埋点数据
CEA SDK
埋点数据
14
Demo
：
HU
埋点数据分析
参考：
ID.S 5.0
智能语音
GPT
用户使用数据分析
平均日活率
6.50%
单车日均指令
1.32
平均月活率
52.94%
TOP 10 user commands
下载量
6555
(13.85%)
N
o.
Command
Category
1
画一幅宫崎骏风格的风景图
AIGC (
画图
)
2
后面的乘客在哪里调节座椅
智能车书
3
耐克和
a
钩有什么区别
百科闲聊
4
写一篇咖啡馆小红书推广文案
AIGC (
文案
)
5
恐龙化石是怎么形成的
百科闲聊
6
今天天气怎么样
百科闲聊
7
红烧肉的图像
AIGC (
画图
)
8
画一幅水墨风山水画
AIGC (
画图
)
9
画出宫崎骏风格的山脉景色
AIGC (
画图
)
10
给我一个大众汽车的销售文案
AIGC (
文案
)
已上线的功能中，用户最常使用的为百科闲聊功能，对
AI
向导及多媒体搜索功能也存在一定需求。
TOP10
的用户指令大多数来自于
App
预置
Hint
（
7/10
），且在这些
hint
中，用户对
AI
画图较感兴趣。
数据统计周期：
2024.09.10 - 2024.12.31
日活率
=
当日打开
App
的去重车辆数
/
截至当日累计下载
App
的车辆数
月活率
=
当月打开
App
的去重车辆数
/
截至当月底累计
App
下载车辆数
平均日活率与平均月活率为
9
月、
10
月、
11
月、
12
月统计周期内的平均值
12
月其他
App
数据参考：
智能语音
GPT
下载率：
13.85%
，月活率：
24.26%
，日活率：
1.22%
QQ
音乐下载率：
27.08%
，月活率
67.25%
，日活率：
30%
哔哩哔哩下载率：
18.23%
，月活率
51.15%
，日活率：
9.2%
来源：
SVCC
DEMO,
数据来自神策
15
Demo
：
One App
埋点数据分析
DEMO,
神策分析表盘
16
Backup
17
C
车数据相关链路（
One Team
提供）
18
C
车埋点相关链路（
One Team
提供）
2
Cluster1 C
车
VDU
数据链路
3
Cluster1_C
车
VDU
数据链路
CDCU/LDCU/RDCU/NGX/…
T-Box
数据云端管理平台
数据胡
Consent mgmt.
VDU
One Backend
（
合规云
）
SVW
数据上传
（可配置上传范围）
数据上传
上传数据
(CAN/LIN/SOMEIP/…)
用户确认数据采集声明
4
Demo
：移动互联车载话务系统运营现状
E Call
进线情况
& CDC/RTG
碰撞线索情况
50.5 %
E Call
事故车案件数量
下发线索数量
394,861
2,440
1,233
装备
E Call
车辆总数
事故车案件数量
下发线索数量
342,651
3,202
347
装备
CDC/RTG
车辆总数
Car Data
Crash* Leads
ECall
Crash Leads
10.8 %
Data
01.-12.2024
Data
01.-12.2024
3
2
# of
ECall
(MQB,MOS3GP & MOS3.X)
* Small collision without
ECall
triggered
2
6
# of Car Data Crash (MOS3GP)
1
3
1
6
3
9
6
4
6
6
2
1
1
16
14
8
11
37
2
来源：
SVCC
，数据截止
2024/12/31
5
C
车
VDU
数据
Demo
（参考
CDC
）
C
车
VDU
暂无，
数据清单、数据样例
计划
CW26
（
6
月下旬）
反馈
，以下以
CDC
信号举例
信号
\
类别
基本信息
驱动系统
车身状态
电气设备
底盘
驾驶辅助
CDC
（
127
，已配置）
16
14
45
8
1
43
基本信息 ：有且仅有车速、加速度、里程、车辆位置、时间、车内外环境信息（温度、降水量、空气质量）
驱动系统：  电池系统、电驱动系统、高压安全与充电系统，发动机系统
车身状态： 四门两盖、车窗、天窗、座椅、内饰件、拖车等状态信号，包括开启关闭、位置、温度设置等状态
电气设备： 电源系统，用电设备，仪表及报警装置，全车电路及配电装置
底盘 ：传动系统，转向系统，制动系统，行驶系统
驾驶辅助： 电气设备中的电子控制信号以及摄像头和传感器信号，包括自动泊车辅助、制动辅助、行车辅助等
分类
S
ignal_Name
信号解释
Description
中文描述
S
ervice_Name
Resource
Property
描述
Index
字段名
基本信息
AB_Belegung_VF
主驾位有人
Driver
2
、驾驶
SafetyBeltState
seatOccupancy
occupancy
主驾位有无人状态（
0-
无此功能
1
occupancy_1
1-
报错
2-
无人
3-
有人）
基本信息
AB_Belegung_VB
副驾位有人
CoDriver
2
、驾驶
SafetyBeltState
seatOccupancy
occupancy
副驾位有无人状态（
0-
无此功能
2
occupancy_2
1-
报错
2-
无人
3-
有人）
驱动系统
Ladezustand_02
HV
电池
SOC
relativeChargingStatehighVoltage
5
、电池
EnergySystem
highVoltageBatteries
relativeChargingStatePhysicalValue
HV
电池
SOC(
电量
)
1
relative_high_voltage_charging_state_physical_value_1
驱动系统
BEM_Ladezustand
值类型
relativeChargingStatelowVoltage
5
、电池
EnergySystem
lowVoltageBatteries
relativeChargingStateValueType
1 - Init
1
relative_low_voltage_charging_state_value_type_1
2 - Error
3 -
LogicalValue
4 -
PhysicalValue
车身状态
ZV_FT_offen
主驾门开启状态
DriverDoor
1
、四门两盖
CarBody
doors
isDoorOpened
主驾门开启状态（
0-
关，
1-
开）
1
carbody_doors_is_door_opened_1
车身状态
FT_FH_Fang
主驾窗关闭状态
DriverDoor
1
、四门两盖
CarBody
doors
isWindowInReceptionRange
主驾窗关闭状态
(false-
未关实
,True-
关实
)
1
carbody_doors_is_window_inreception_range_1
……
……
……
……
……
……
……
……
……
……
……
6
C
车
VDU
数据应用场景举例
序号
类别
应用
简要介绍
1
用
车辆报警实时监控
基于车辆数据，实时监控车辆使用过程中的红灯和黄灯报警情况，并对故障报警车辆进行分析
2
智选充电
基于车端充电站数据，迭代智选充电算法，形成新的智选充电标签
3.0
，辅助用户充电决策，提高用户公桩充电体验
3
车辆充电曲线
+
绝缘报警
基于车辆充电实时数据结合
RTM
数据，实时监测并展示给用户车辆真实充电情况，发现异常情况进行报警，提升用户公共充电安全可靠感知
4
高级别报警车辆场景识别
区分高级别报警车辆场景，识别合适场景进行报警提醒推送，提升用户体验
在店内
×
、在
OTA ×
、在充电
×
、在
KD Flash
×
、在年检
×
、 在行驶、
……
5
修
故障维修线索
基于
e-/b-Call
和车辆碰撞数据，由
e-Call
坐席人员联系用户并通知经销商及时给用户提供道路救援及车辆维修服务
采集车辆故障信号，通过
400
客服中心下发经销商
E
销小程序，经销商直接邀约用户或伴随保养线索下发，提高邀约成功率以及保养增项转化，最终提高经销商保养产值
6
事故线索
采集碰撞时间，碰撞发生地点、碰撞部位、碰撞强度等获得事故车线索，分发经销商以迅速发起事故车线索跟进
7
高压电池预测性维修
后台监控发现用户纯电车高压电池部分模组
/
电芯异常
用户接到预警回店维修
经销商获取后台维修建议，确定模组位置，为用户提前准备模组更换
8
养
保养线索
采集车辆实时里程、剩余保养里程
/
天数，预测下次保养周期，通过手机和车机提醒用户进店保养，并将线索发送至经销商，经销商邀约用户进店保养
9
换
高压电池健康状态评估
车主在上汽大众官方认证二手车渠道卖车
车主上汽大众授权销售服务商，使用评估车辆的专项服务
经销商获取后台二手车信息， 结合高压电池健康状态，为二手车定价
10
事故回溯
ADAS
功能问题分析
通过采集驾驶辅助功能状态数据
(on/off
、执行参数
)
，辅助判断事故与辅助驾驶功能的相关性（功能问题
/
非功能问题），针对舆情和用户抱怨采取相应应对措施，通过同时采集车辆状态数据（时间、车速、里程、电门刹车状态）辅助还原事故场景，辅助事故归因
11
增值报告
月度行车报告
月度行驶公里数、驾驶时长、能耗与驾驶情况
12
车辆健康报告、车辆诊断报告
基于车辆充电行为、维保、里程、质保等数据，展示用户月度用车行为及评价
13
电池健康度报告、充电行为评价报告
通过大数据和算法为
ID
纯电车辆提供官方电池健康度报告，替代线下
ODIS
检查
提供纯电车辆电池检测项、提供充电线上快速预检
业务需求
已实现
7
Cluster2 RTM
C-
WD
Digital
Products
&
Cockpit
Page
1
RTM
用户触点
-
无
用户利益点
确保买到的车符合国家标准。
提前解决故障排除危险。
简述
RTM
是通过
T-
box(OCU,
Conmod)
监控车辆运行数据和上传实时数据的系统。所有新能源汽车的
RTM
功能需要满足国标
GB/T32960
的要求。当车辆为
K
L1
5
上电状态或充电状态时，
RTM
应该为工作状态，车辆数据应以至少每
3
0
秒一条数据的频率传送到国家平台。由企业进行监测，再上报至政府综合管理平台，以加强新能源汽车运行安全管理，提高电动汽车服
务质量和管理水平，预防和减少电动汽车安全事故。
流程
RTM
数据通过
T-
box
从车辆发送到
CEA
one
backend
后台，然后发送到
SVW
后台，最后发送到国家
/
地方平台。当检测到车辆有危险时，后台会向呼叫中心报警。呼叫中心将联
系用户确认车辆情况，必要时会建议用户前往
4S
店处理。
RTM
数据从车端
发至
CEA
后台
One
backend
SVW BE
RTM
数据从
CEA
后台
发送至
SVW
后台
RTM
数据从
SVW
后台
发送至政府平台
报警数据发送至
CEA
后台
报警数据从
CEA
后台
发送至
SVW
后台
6.
通知呼叫中心
呼叫中心与用户沟通确认情况，如有必要，通知用户
到经销商处理故障
8.
用户到经销商处理
报警
无报警
有报警
C-
WD
Digital
Products
&
Cockpit
Page
2
RTM
法规状态
目前
GB/T
32960
处于修订中，根据
TRRC
预测，对新车型
2026.1
实施，在产车型
2027.1
实施。
根据法规预测实施时间和车型
SOP
时间，
C
车需满足
GB/T
32960-XXXX
要求。
RTM
采集数据
整车数据：
车辆状态、充电状态、运行模式、车速、累计里程、总电压、总电流、
SOC、
DCDC
状态、挡位、高压对地绝缘电阻
驱动电机数据：
驱动电机个数、驱动电机状态、驱动电机控制器温度、驱动电机转速、
驱动电机转矩、驱动电机温度
燃料电池数据：
仅用于燃料电池车辆
发动机数据（纯电车型不涉及
）
:
发动机转速
车辆位置数据：
定位状态、坐标系、经度、纬度
报警数据：
温度差异报警、电池高温报警，可充电储能装置热事件报警等…28
项报警
动力蓄电池最小并联单元电压数据：
动力蓄电池包个数、动力蓄电池包电
压、动力蓄电池包电流、最小并联单元总数、本帧最小并联单元电压
动力蓄电池最小并联单元温度数据：
动力蓄电池包温度探针个数、各温度
探针检测到的温度值
数据采集需求
在车辆
KL15
上电或充电状态下开始数据采集。
数据采集采集频次应不低于
1
次
/s
。

---

## PPTX: VDU(C车动采)\CMP21D data_20250617.pptx

2026/6/25
单击此处编辑母版文本样式
二级
三级
四级
五级
‹#›
1
单击此处编辑母版标题样式
单击以编辑母版副标题样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
版本号
Version
：
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
EHA
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
EHA
编辑标题文字
Click to edit Master title style
EHA
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
部门  会议名称  保密级别
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
单击此处编辑母版标题样式
编辑母版文本样式
2026/6/25
‹#›
编辑正文文字
Click to edit Master text styles
‹#›
编辑标题文字
Click to edit Master text styles
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
2026/6/25
‹#›
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
EHA
Xue Haiqiang
: SVW data FO
Qin jingyi: SVW Connectivity PL
Jiang
chengjun
: GC One backend PL
Liu
tengfei
: SVW SP PL
Wang zhiming: One team GB
埋点
SE
Xu
shiqi
: One Team Data PO
Han
weitao
/jiang
xia:OB
埋点云端开发
Zhuang
chunxiao
: SVW SP
埋点
/
数采开发

---

## PPTX: VDU(C车动采)\C车数据采集前提逻辑.pptx

单击此处编辑母版标题样式
单击此处编辑母版副标题样式
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
单击此处编辑母版标题样式
2026/2/13
‹#›
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
2026/2/13
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
2026/2/13
‹#›
1
绑车状态
-
-
绑车
解绑
车辆到达经销商
未到达
到达
到达
-
数据采集状态
可采集
不可采集
可采集
不可采集
3.
用户收到车绑车后，调用接口，
uploadSwitch
传
1
。此时数据可以采集
车辆下产线后，到达经销商前，车辆默认可以进行数据采集
CIM
收到车辆到达经销商的信息，调用接口，
uploadSwitch
传
0
。此时数据不可采集
4.
用户解绑后后，调用接口，
uploadSwitch
传
0
。此时数据不可以采集

---

## PPTX: VDU(C车动采)\VDU.pptx

9/9/2025
Click to edit Master text styles
Second level
Third level
Fourth level
Fifth level
‹#›
编辑标题文字
Click to edit Master title style
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
SC  Connectivity|
Internal/Confidential/Secret
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
Feature Upgrade
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
New
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
单击添加节标题文字
00
单击添加节标题文字
节标题下分二级目录或章节介绍
SC Connectivity / Confidential
‹#›
00
编辑标题文字
Click to edit Master title style
New
SC
Connectivity
/
Confidential
‹#›
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
日    期
Date
：
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
单击添加节标题文字
00
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
SC  Connectivity|
Internal/Confidential/Secret
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
单击添加节标题文字
节标题下分二级目录或章节介绍
SC Connectivity / Confidential
‹#›
00
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
New
编辑标题文字
Click to edit Master title style
Feature Upgrade
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
日    期
Date
：
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
SC
Connectivity
/
Confidential
‹#›
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
SC  Connectivity|
Internal/Confidential/Secret
SC/EPE    Confidential
Click to edit Master title style
SC
Connectivity
/
Confidential
9/9/2025
‹#›
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
部门名称   会议名称
Confidential
‹#›
编辑标题文字
Click to edit Master title style
单击添加目录文本
部门名称   会议名称
Confidential
目录
CONTENTS
单击添加节标题文字
00
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
日    期
Date
：
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
SC  Connectivity|
Internal/Confidential/Secret
255/255/255
219/238/213
129/194/109
75/168/46
Skoda Color
VW Color
192/192/192
110/110/110
0/0/0
169/227/255
0/30/80
0/130/214
182/191/197
223/228/232
0/176/240
文字
/
背景色
填充颜色和图表填充色
SVW Color
168/187/200
255/199/44
132/189/0
203/51/59
0/119/200
80/80/80
0,0,0
166/187/200
51/63/72
0/119/200
255/255/255
166/187/200
超链接
Audi Color
187/10/48
0/0/0
179/179/179
182/177/169
255/255/255
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
SC  Connectivity|
Internal/Confidential/Secret
255/255/255
219/238/213
129/194/109
75/168/46
Skoda Color
VW Color
192/192/192
110/110/110
0/0/0
169/227/255
0/30/80
0/130/214
182/191/197
223/228/232
0/176/240
文字
/
背景色
填充颜色和图表填充色
SVW Color
168/187/200
255/199/44
132/189/0
203/51/59
0/119/200
80/80/80
0,0,0
166/187/200
51/63/72
0/119/200
255/255/255
166/187/200
超链接
Audi Color
187/10/48
0/0/0
179/179/179
182/177/169
255/255/255
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
SC  Connectivity|
Internal/Confidential/Secret
255/255/255
219/238/213
129/194/109
75/168/46
Skoda Color
VW Color
192/192/192
110/110/110
0/0/0
169/227/255
0/30/80
0/130/214
182/191/197
223/228/232
0/176/240
文字
/
背景色
填充颜色和图表填充色
SVW Color
168/187/200
255/199/44
132/189/0
203/51/59
0/119/200
80/80/80
0,0,0
166/187/200
51/63/72
0/119/200
255/255/255
166/187/200
超链接
Audi Color
187/10/48
0/0/0
179/179/179
182/177/169
255/255/255
VDU
Process/
流程
D
e
sc
ri
pt
ion/
简述
The VDU's millisecond-level CAN signal acquisition function collects all CAN signals from the vehicle, packages them, and uploads them to the backend system.
VDU
秒级
CAN
信号采集功能通过采集车端全量
CAN
信号，打包并上传车到后台系统。
OB
1
. Pre-defined rules has been sent to Backend
编辑采集规则并上传到后台系统
2.
Synchronizes the rule to vehicle for execution
同步规则到车辆执行
SVW
3.
Upload the date to backend
上传车辆数据到后台
4.
Deliver the decrypted data to SVW DB
传送处理后的数据到
SVW
数据库
SC  Connectivity|
Internal/Confidential/Secret
Change Scope/
变更范围
车端数据全量采集，不可配置规则
采集范围不是基于整车
DBC
车内信号频率为毫秒级，但采集频率只支持到秒级，对于一些重要些信号会造成采集过程缺失
数据采集没有可视化配置工具
采集类型只有
CAN
痛点
One Backend
配置平台给到
JVs
配置数据采集范围（包括：信号类型，信号数量，采集频率，触发方式等），平台形式为可视化
portal
形式
可以根据业务需求配置不同的采集任务
车端支持毫秒级采集频率
车端增加边缘计算能力
采集类型拓展为
CAN
，
LIN
，
SOA
变更

---

## PPTX: 动采_AF\A\1. A NB PHEV Timeplan_v38.pptx

11/4/2024
‹#›
11/4/2024
Click to edit Master text styles
Second level
Third level
Fourth level
Fifth level
‹#›
1
2
单击此处编辑母版标题样式
单击此处编辑母版副标题样式
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
‹#›
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
confidential
编辑标题文字
Click
to
edit
Master title style
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
‹#›
单击此处编辑母版标题样式
11/4/2024
1
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
单击此处编辑母版文本样式
11/4/2024
‹#›
单击此处编辑母版标题样式
单击图标添加图片
单击此处编辑母版文本样式
11/4/2024
‹#›
单击此处编辑母版标题样式
单击此处编辑母版文本样式
二级
三级
四级
五级
11/4/2024
部门  会议名称  保密级别
‹#›
Ersteller: SVW ET
Date:
01.11.2024
Confidential
A NB PHEV R&D Timeline v38
2024
2025
2026
03
04
05
06
07
08
09
10
11
12
01
02
03
04
05
06
07
08
09
10
11
12
01
02
03
04
05
06
07
08
09
10
1
st
Tooling Parts
KW39
AGT1 Car
EM
06
N3
22
AGT2 subsystem
45 / 11.8
N1
43
Software  AGT2
17 / 4.25
Structure B
Freigabe
HUT ZP5 w.
Seitenteile
(TG2)
AGT2 Baseline
23 / 6.2
Crash Result
23
E/E architecture
AGT2
B
Guss
Plat.
24/6.13
BF Plat. (TG2)
30 / 7.25
ZP5 TBT
12/3.17
SAIC
G8 8.31

MOU
15

ZP7
crash
MRD
16/4.14
NDA
16

1
st
Tooling
49
Crash
20/ 5.12
TLA
Light
26

P
F(
G8
)
42

AGT2
22/ 5.26
EM
16
KF(
G7
)
4/1.24
PLF(
G6
)
14/3.31
N3
29
BF(
G5
)
26/6.26
Axrml
EP
13/3.27
Structure
B
Freigabe
Plat. ZP5 &
Door Ring
(TG2)
Software EP
30/7.21
LF
36
Baseline EP
38/9.17
VFF ZP7
TBT(
G4
)
MRD 51/12.15
E/E architecture
EP
BF LLT (TG2 LLT)
21
PVS ZP7
TBT(
G3
)
MRD 10/3.2
ZP5  TBT
40
9.30
BF All (TG2 All)
29
0S ZP7
TBT(
G2
)
MRD 20/5.11
ZP7 TBT MRD
44
10.27
Structure
B
Freigabe
ZP7 (TG2)
SOP ZP7
TBT (
G1
)
MRD 29/7.13
1
st
EP crash
48
11.24
SOP
32
LLT
RFQ
(SOR)
29

1
st
EP
w. series tooling
51
12.15
Project Milestone
Start 2D
17

EP Car
Nomi.
Tier 0.5
33

1
st
3D
30

Winter test
Internal
34.3

Nomi.
LLT
36 (see detail)

Warm
test
DA/DV
(Go1) 40

Winter test
DE/DF(
SA)
46
Nomi.
All
08
Application
AGT(mu)
01
Design
T
ooling
Part
ZP5
38
Data for
pre start 01
Grob
Strak
36

DDKM Start
(DG0)
44

Final data 07
Tooling
Part
ZP7
42
VF
04
Motor
Soft tooling
40
Application Braking
Winter test
DDKM
(DG1)
08
Application
Sommer test
OTS
04
Application winter test
with EP Car
s.FKM
14
Chassis
N3
29
Application
with EP
DDKM2
LLT 16
Final data
07
Normal
Nomination & Parts
Parameter Fix
25
DDKM2
All
(DG2)
22
ADAS
Strak
Arxml
AGT
32
8.9

Today
Strak
input
43.4

Structure
Simulation
48.5
Pre-Start 3
Software release AGT
44

1
st
Structure finish (
TG1)
05 /
1.27
Data Freeze 10
Structure P
Freigabe
(TG1)
Baseline
49/12.4
Upload 17
technical
output 21

1
st
Simulation
(CAE result) 03
CCC 29
E/E architecture
AGT1
Concept
Abnahme
04
Homologation
2
nd
Simu.
(CAE Result) 29
ZP5 TBT
40/9.30

Concept
Vor
B
Guss
15
ZP7 parts
TBT MRD
44/11.1

BF
Guss
17
HT23
High
11.15
BF
20
1
st
AGT
(mu) 50
52/12.23
ZP7
Software
MRD
18/ 4.28
Soft ST BM
30
AGT2 Car
Premise:
DDKM to DDKM2 the A-surface change should be lower than 5mm and
Fugen
lower than 2mm. Resp. EPD/EPB
VFF car will be used for official homologation tests.
Resp.EPG
KW15/2025 Review the necessity  of soft tooling of
seitenteile
.
AGT2 and PT Baseline need to discuss with ZONE for the maturity of the software
Risk:
SRIH hope
ZP7 TBT postpone 2 weeks considering 3.0
architecture.
A NB PHEV Timeline v38
Change Content
From
To
Change Date
Reason
DA/DV
KW38/24
KW40/24
20240805
VW time reservation from boss
DE/DF
KW50/24
KW46/24
20240805
WOB optimize
Design Internal Decision
KW33/24
KW34.3/24
20240813
Time reservation from ED
ZP5 HUT N3
KW20/25
KW16/25
20240819
Q optimize
ZP5 Platform 1
st
Tryout
KW44/25
KW42/25
20240819
PM optimize
ZP5 Platform N3
KW25/26
KW23/26
20240819
Q optimize
PF Milestone
KW37/24
KW41/24
20240827
VGC&VW meeting plan delay
2nd Round
AGT Crash
KW15/25
KW14/25
20240902
VSC 1 week optimize
Crash Result
KW18/25
KW17/25
20240902
Parallel optimize based on AGT2
B
Guss
Plat.
KW19/25
KW18/25
20240902
Parallel optimize based on Crash
BF Plat. (TG2)
KW27/25
KW24/25
20240902
Parallel 1 week from B
Guss
2 weeks from data making
Quick Tooling
KW35/25
KW32/25
20240902
Parallel optimize based on BF
1
st
Tooling Parts
KW42/25
KW38/25
20240902
Parallel optimize based on BF
1 week use half process parts
Add soft tooling for
seitenteile
,
Serie tooling for EP as best case for backup
KW17/25
KW17/25
20240909
Techinical
review meeting in KW36
Concept
Abnahme
KW52/24
KW51.4/24
20240909
WOB
optimize due to Christmas
Adjust SOP to KW32
KW26/26
KW32/26
20241014
690 wheel, all relevant milestone change according to new SOP
Prepone
strak
input
KW44.5/24
KW43.3/24
20241028
Work acceleration and scope confirmation between EPB and EPK
Adjust ZONE EP time
AGT2/EP
AGT2/EP
20241101
ZONE time change according to new SOP

---

## PPTX: 动采_AF\A\AB车动采timeline.pptx

单击此处编辑母版标题样式
单击以编辑母版副标题样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
2025/2/24
‹#›
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
2025
2026
09
10
11
12
01
02
03
04
1
st
Test
Finish
2
nd
Test
Finish
B/CW49
3
th
Test
CW07
3
th
Test
Finish
Signal Validation
Vehicle Requirement
CW50 – CW12
2
nd
Edition
1
s
t
Edition
B PVS*1
SSTS Release
Release/CW12
Technical Requirement
B SUV EREV
2
nd
Test
CW03
SOP
Start/CW06
0S
PVS
1
st
Test
CW51
Finish/CW12
MQ Test
VFF
CW49.1- CW50.5
Freeze/CW10
Development Plan
Start/CW49
Signal List Collection
2/6/2026
E2E Test
Start
Finish/CW12
Start
C/CW06
2025
2026
11
12
01
02
03
04
05
06
07
E2E Test
SSTS Release
1
st
Test
Finish
Release/CW28
PVS
Signal List Collection
VFF
Development Plan
1
s
t
Edition
Start/CW51
3
th
Test
Finish
2
nd
Edition
A NB PHEV
CW51 – CW28
B/CW51
3
th
Test
CW20
A VFF*1
Freeze/CW19
SOP
Start
2
nd
Test
Finish
0S
C/CW20
1
st
Test
CW01
Technical Requirement
Signal Validation
Finish/CW28
2
nd
Test
CW11
Vehicle Requirement
Start
MQ Test
Start/CW20
CW51.1- CW52.5
Finish/CW28
Start

---

## PPTX: 动采_AF\A\A车动采资源汇报.pptx

‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
A
车动采资源分配现状
信号类型
A
车原方案采集限制数量（个）
CPU
资源
（
DMIPS
）
A
车实际采集数量（个）
预估
CPU
占用
（
DMIPS
）
Datapool
CAN/LIN/
埋点帧
4000
900
1000
500
SOA
1800
1000
120
400
座舱埋点
2000
100
940
100
边缘计算
/
500
/
500
DCC
/
500
/
500
总计
3
k
2
k
动采资源消耗预估：
动采资源消耗组成：
Datapool
（数据处理打包上传）
+
边缘计算（事件采集相关）
+DCC
（车云通讯相关）
目前
A
车对于动采的资源分配计划：
行车场景：数采整体
2k
泊车场景：按当前最新要求，数采整体可能会没有资源，可能需要考虑最低优先级运行或不采
功能影响如下：
影响系统方案：破坏平台方案，需要重新设计
A
车动采系统方案
影响需求：拉齐所有需求方，告知泊车场景下的采集需求无法实施（目前收到
EXE
，
MQ
，
EPFA
，总院和各功能
PO
的需求）
a.
EXE
需求：智驾报告，智驾功能排查，事故定责等
b. MQ
需求：售后问题排查
c. EPFA
需求：车辆模式
&
低压系统监测
d.
总院需求：高压系统监测
e.
各功能
PO
需求：座舱埋点
动采侧意见：
不区分场景，最低
2K DMIPS
的资源分配
1
A
车动采资源评估
数据采集
周期
/
完整采集数量
（
A
车原方案）
事件采集数量
（
A
车原方案）
CPU
资源
（
DMIPS
）
A
车实际数量
预估
CPU
占用
（
DMIPS
）
信号池数量
CAN/LIN/
埋点帧
单脚本
脚本数
150
900
单脚本
脚本数
500
5500
2000
100
（
100ms
）
2
1000
300
（
100ms
）
1
1880
（
1s
）
650
（
1s
）
20
（完整，最低
20ms
）
50
（完整，最低
20ms
）
SOA
1800
（
1s
）
50
1000
120
400
6900
DCTP
2000
/
100
940
100
1041
注：
CAN/LIN
数据采集单脚本限制
2000
个信号，可以配置两个脚本。
SOA
信号，接口共40个（其中
4
个
20ms
，
2
个
50ms
，
34
个
1s
），按照接口数量乘以
3
进行估算，共40*3=120个。
DCTP
信号为座舱埋点，多为用户触发，不存在所有
DCTP
信号同时触发的可能。目前性能预估按照高频（
1
次
/
秒）占比
5%
，中频（
1
次
/10
秒）占比
15%
，低频（
1
次
/
分钟）占比
80%
。
动采资源消耗组成：
Datapool
+
边缘计算
+DCC
，如上资源评估为
Datapool
资源消耗，边缘计算
500
（事件采集相关）
+DCC500
（车云同步的消耗，
zx
评估给出）
100ms
下
CPU
占用（实测
+
经验）
CAN/LIN/
埋点帧
1
DCTP
5
SOA
5
不分场景，最低保证
2K DMIPS
的资源分配的前提下的优化方向：
需求层面：对于已有的采集任务，定期
Review
，关停没有使用价值的采集；对于新增需求，需明确应用范围和优先级
配置层面：不采集埋点帧子信号，只采集埋点帧，自行解析埋点帧获取埋点帧内子信号

---

## PPTX: 动采_AF\F\5s\爬坡计划\开发计划_自己拍的\AB车动采timeline.pptx

单击此处编辑母版标题样式
单击以编辑母版副标题样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
2025/2/24
‹#›
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
2025
2026
09
10
11
12
01
02
03
04
1
st
Test
Finish
2
nd
Test
Finish
B/CW49
3
th
Test
CW07
3
th
Test
Finish
Signal Validation
Vehicle Requirement
CW50 – CW12
2
nd
Edition
1
s
t
Edition
B PVS*1
SSTS Release
Release/CW12
Technical Requirement
B SUV EREV
2
nd
Test
CW03
SOP
Start/CW06
0S
PVS
1
st
Test
CW51
Finish/CW12
MQ Test
VFF
CW49.1- CW50.5
Freeze/CW10
Development Plan
Start/CW49
Signal List Collection
2/6/2026
E2E Test
Start
Finish/CW12
Start
C/CW06
2025
2026
11
12
01
02
03
04
05
06
07
E2E Test
SSTS Release
1
st
Test
Finish
Release/CW28
PVS
Signal List Collection
VFF
Development Plan
1
s
t
Edition
Start/CW51
3
th
Test
Finish
2
nd
Edition
A NB PHEV
CW51 – CW28
B/CW51
3
th
Test
CW20
A VFF*1
Freeze/CW19
SOP
Start
2
nd
Test
Finish
0S
C/CW20
1
st
Test
CW01
Technical Requirement
Signal Validation
Finish/CW28
2
nd
Test
CW11
Vehicle Requirement
Start
MQ Test
Start/CW20
CW51.1- CW52.5
Finish/CW28
Start

---

## PPTX: 动采_AF\F\6s\爬坡计划\开发计划_自己拍的\AB车动采timeline.pptx

单击此处编辑母版标题样式
单击以编辑母版副标题样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
单击此处编辑母版标题样式
2025/2/24
‹#›
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2025/2/24
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2025/2/24
‹#›
2025
2026
09
10
11
12
01
02
03
04
1
st
Test
Finish
2
nd
Test
Finish
B/CW49
3
th
Test
CW07
3
th
Test
Finish
Signal Validation
Vehicle Requirement
CW50 – CW12
2
nd
Edition
1
s
t
Edition
B PVS*1
SSTS Release
Release/CW12
Technical Requirement
B SUV EREV
2
nd
Test
CW03
SOP
Start/CW06
0S
PVS
1
st
Test
CW51
Finish/CW12
MQ Test
VFF
CW49.1- CW50.5
Freeze/CW10
Development Plan
Start/CW49
Signal List Collection
2/6/2026
E2E Test
Start
Finish/CW12
Start
C/CW06
2025
2026
11
12
01
02
03
04
05
06
07
E2E Test
SSTS Release
1
st
Test
Finish
Release/CW28
PVS
Signal List Collection
VFF
Development Plan
1
s
t
Edition
Start/CW51
3
th
Test
Finish
2
nd
Edition
A NB PHEV
CW51 – CW28
B/CW51
3
th
Test
CW20
A VFF*1
Freeze/CW19
SOP
Start
2
nd
Test
Finish
0S
C/CW20
1
st
Test
CW01
Technical Requirement
Signal Validation
Finish/CW28
2
nd
Test
CW11
Vehicle Requirement
Start
MQ Test
Start/CW20
CW51.1- CW52.5
Finish/CW28
Start

---

## PPTX: 动采_AF\F\VDP月会汇报材料.pptx

需求数量对比
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
动采信号更新计划
&
配置流程
动采信号更新原因（更新范围包含数量，采集方式，上传方式）：
运维费用（车辆数量，触发类型，采集周期等因素）
售后问题分析
数据分析需求变更
时间节点
更新计划
SOP
CANLIN
：根据基线
座舱埋点：根据基线
SOA
：根据基线
SOP+3
每两周
Review
：
CI
给出资源费用报告
邀请需求方分享数据应用案例
2.
总结是否更新采集配置
SOP+3
后
按需提交需求
第一年：每三个月
Review
，按实际情况更新采集配置
第二年：每年
4
月，
10
月
Review
，按实际情况更新配置
OTA
按需提交需求
数据导出
部门
测试联调
&
功能优化
ECC
售后问题分析
MQ/ECC
其他
CI
1
F
车动采
&
埋点采集需求现状
信号类型
数量（个）
频率（
ms
）
数量（个）
CAN/LIN/
埋点帧
5433
完整采集
250
100
3017
200
127
500
148
1000
3411
3000
48
SOA
9150
完整采集
201
100
334
200
16
1000
9047
DCTP
（座舱埋点）
1240
事件触发
换算公式：各类频率全部转换为
1s
，比如采集频率
100ms
，即采集数量
*10
高频信号需求由零束提出，具体需求分类如下：
完整采集需求组成：电动座椅，天窗遮阳帘，诊断云端模型
100ms
需求组成：云端模型需求，尾门，座椅，空调，新能源热管理，
RZCU
2
Next Step
配置建议：
所有信号按照
1s
配置
待办项：
后台资源评估，包含总院
SP
和
VC
信号需求排优先级
数据积压解决方案：
降频回滚配置
超过
48h
云端消费不完数据，删除前序积压部分
恢复期间通过业务监控平台导出数据
车端数据上传
EA
数据解析
总院
SP
数据解析，业务监控平台
SP
R
en
C
henglin
大数据平台
VC Li
J
iwei
数据需求收集
EC
数据安全分级
EC
云端资源评估
总院
&CI
信号池制作  总院
业务拉齐需求
EC&
总院
VDP
决策
默认车组任务发布
EC
问题车组任务发布
MQ
3
F
车埋点测试情况
目前埋点数据入库率：
821/1240
，其中
135
个为
SOP+3
需求实现，如下为当前埋点问题票清单：
JIRA
票号
票问题描述
（点击没有埋点上报或上报内容不符合定义）
修复计划
BSUVVW-9074
Dock
栏内部分功能
分析中
BSUVVW-9197
负一屏下部分功能
V5.0.19
BSUVVW-9481
BSUVVW-17600
SDS
语音部分功能埋
V6.1.10
BSUVVW-9483
BSUVVW-17601
智能场景部分功能
V5.0.19
BSUVVW-14385
BSUVVW-17599
蓝牙耳机设置部分功能
V6.1.9
BSUVVW-14458
智驾
-
泊车设置部分功能
分析中
BSUVVW-18076
BSUVVW-18083
地图部分功能
分析中
BSUVVW-17597
香氛部分功能
V5.0.19
BSUVVW-17598
车外声音部分功能
V5.0.19
BSUVVW-17602
停车拍照部分功能
V6.1.9
BSUVVW-17603
退出放电管理页面部分功能
分析中
BSUVVW-17596
座椅设置部分功能
分析中
BSUVVW-17592
灵动
widget
部分功能
分析中

---

## PPTX: 动采_AF\F\动采+埋点状态汇报 - 副本.pptx

‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
埋点状态与计划
2025
2026
10月
11月
12月
1月
2月
3月
43
44
45
46
47
48
49
50
51
52
01
02
03
04
05
06
07
08
09
10
11
12
13
0SBugFix2
0SBugFix1
0S
PVS
BugFix
PVS
埋点（
ODC
开发）
（事件：
245
个；
Key
：
506
个）
数据质量监控
2
nd
Full Test Ongoing
Till today
通过率：
406/506
1
st
Full Test
通过率：
0/506
埋点（零束开发）
（事件：
1016
个；
Key
：
2448
个）
数据质量监控
2
nd
Full Test
1
st
Full Test Ongoing…
Till today
通过率：
333/522
工作内容
点检测试通过率：
355/400
动采通道测试（台架
+
实车）
Go live
0S BugFix1
通道
√
Ready
PVS BugFix1
通道
√
Ready
Full-size SUV 6S
SOP
描述
案例
分析
&
进展
Ticket
修复节点
问题
1
埋点携带经纬度
事件名：无路线进入算路页
上报内容：
{…,
POIlongitude
=121.16483441113324
,
eventname
=
hu_navirouteEnter
,
POIlatitude
=31.301196793957768
}
问题：经纬度为敏感个人信息，目前合规方案设计，通过埋点上报有严重合规问题
BSUVVW-7325
SOP
前
问题
2
上报事件
DataID
错误
DataID
：
03000102010000000000000000300411
事件名：遮阳帘调节；雨刮设置开关；右侧后视镜下倾设置等
问题：多条事件使用同一个
DataID
上报，理论上
DataID
和事件名应该一一对应
BSUVVW-7404
SOP
前
问题
3
上报内容和定义不符
事件名：
DVR
拍视频，属性：
trigger_method
,
eventname
上报内容：
{"hu_dvr_takevideo":"0"}
问题：
Event
作为埋点上报必须字段，错误或者缺失会导致后续无法入神策
进展：
1.
内容问题建票修改
2.
格式问题，和
CIX
沟通可以统一反馈在大数据平台做数据预处理
BSUVVW-7350
应修尽修，部分不影响数据入库问题可接受
SOP+
基线修复
测试覆盖度：
21.3%
测试覆盖度：
100%
3
rd
Full Test
需要零束支持：
对零束开发各应用埋点的数据质量进行测试，并提供测试报告
重新整理各产品手中的埋点定义，形成
SOP
前锁定的最终版本，并外发给
SVW
。
支持
SVW
验收中对于需求的疑惑点解读，比如找不到入口，事件不理解等

---

## PPTX: 动采_AF\F\动采状态.pptx

图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
动态采集通道能力各条目状态：
功能整体状态
A
车
F
车
CAN/LIN
周期采集
VFF 3.0.16 Ready
PVS 4.0.15 Ready
，
0S 5.0.5 Ready
CAN/LIN
完整采集
CAN/LIN
事件采集
SOA
周期采集
SOA
时间采集
座舱埋点周期采集
边缘计算
1
动采项目状态
2025
2026
10月
11月
12月
1月
2月
3月
4月
42
43
44
45
46
47
48
49
50
51
52
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
0SBugFix1
基线
PVS
基线
测试覆盖：
400/1016
通过率：
355/400
PVS
BugFix
基线
第一轮
Full Test
0S
基线
第二轮
Full Test
0SBugFix2
基线
数据质量监控
第二轮
Full Test
通过率：
234/564
埋点（零束开发）
实车测试
手动触发
+
测试车监测
CAN/LIN:1287
SOA:41
SOP
Full-size SUV 6S
手动触发
+
测试车监测
+
跑车监测
PVS BugFix1
功能
Ready
动采信号（
CAN/LIN/SOA
）
工作内容
0S BugFix1
功能
Ready
UAT
测试
第一轮
Full Test
通过率：
0/564
埋点（
ODC
开发）
实车
+
台架测试
实车测试
动采通道测试
Go live
Live
测试
第三轮
Full Test
数据质量监控
目前已知问题：
埋点：
数据上传和定义不匹配，会导致数据无法落库，最终表现为后台查不到数据。
->
需求定义问题已反馈零束更改；实测问题已建票，例
BSUVVW-3280
，
BSUVVW-3281
，
BSUVVW-3283
埋点未开发。
CAN/LIN/SOA:
1.    A
车
ZCU
性能问题导致和
ZCU
相关的
SOA
信号无法采集，部分
CAN
信号无法采集。
->A
车
ZCU
动采改静采软件已发版
Now
2
海外
MNO
运营商
+
流量策略
海外出行
国内运营商（移动
/
电信
/
联通）
平台能力
除
sim
卡相关业务，还可全生命周期管理（
VIN
，
TBOX SN
，
APP
注册，扫码绑车等）可整体部署到车企云平台。
仅
SIM
卡基础业务，
SaaS
账号授权
流量策略
无当地限制，支持同区流量池
+
超额限流
联通支持流量池；移动
/
电信受当地运营商限制
eSIM
方案
IPAe
（卡端集成）
，无需
TBOX
开发、零适配
IPAd
（
TBOX
集成）
，需开发适配、需额外评估
对接周期
海外出行承接
DP
，
对接周期大幅缩短
标准
6
周
axaxz
axaxz
axaxz
3
A
车
ZCU
汇报方案
动采技术方案
①
基于车云服务交互，云端采集任务动态灵活配置下发，实现全量数据采集；
②
动采主控模块在
ZXD-QNX
（
8155-QNX
）部署，支持
CAN/LIN/SOA/ASF/DCTP
采集。
③
ZCU
与动采主控模块进行指令和数据交互，支持
CAN/LIN/SOA
采集
ZCU
采集方案
预计实施：
7
月
4
日释放需求，要求在
VFF
基线实施
实施现状：
11
月
12
日接到延锋反馈，因
ZCU
资源受限，目前无法按计划部署
ZCU
采集方案
预计影响
（涉及部分
CANLIN
和
MCUSOA
采集）
LHZCU
下挂
LHBDCANFD
整网段以及部分
BKBCANFD
网段
CAN
信号无法采集（
影响
VFF
基线低配共计
93
，高配共计
88
个信号；其中需求信号
9
个
）；
LHZCU/RHZCU
下挂
LIN
节点信号无法采集（
影响
VFF
基线共计
137
个信号；其中暂无需求信号
）；
部分
SOA
无法从
ZCU
源头采集（
影响
VFF
基线共计
35
个
service
；其中需求
service5
个
）
实施方案
保留原有与
ZXD
采集脚本的交互逻辑，接收脚本内的标志位确认是否开始采集
固定采集周期为：
100ms
外发周期为：
100ms
ZCU
执行动采示意图（以
CANLIN
为例）
4
功能链路
5
AB
车数据回传链路
ZXD
Vehicle
IAM
动态采集
RHZCU
SVW Cloud
零束云
动采平台
大数据平台
SVW
LHZCU
RZCU
埋点
SDK
APP
ODC
开发
APP
零束开发
座舱埋点数据
CAN/LIN/SOA
神策
座舱埋点数据
数据上传
Https
采集规则下发
MQTT
采集规则

---

## PPTX: 动采_AF\出口\7 CR变更架构评估-F车LHD出口CR-动态数采变更.pptx

架构主要交付物影响评估
架构主要交付物影响
6/23/2026
‹#›
6/23/2026
Click to edit Master text styles
Second level
Third level
Fourth level
Fifth level
‹#›
4
编辑分隔页标题文字Click to edit Master title style
00
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
单击图标添加图片
单击图标添加图片
单击图标添加图片
编辑标题文字Click to edit Master title style
单击图标添加图片
单击图标添加图片
单击图标添加图片
‹#›
单击图标添加图片
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
单击图标添加图片
编辑标题文字Click to edit Master title style
‹#›
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
版本号
Version
：
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑标题文字
Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
单击此处编辑母版标题样式
单击此处编辑母版副标题样式
2026/6/23
‹#›
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
单击图标添加图片
部    门 Division：
标题文本
版本号 Version：
版本号 Version：
‹#›
编辑分隔页标题文字Click to edit Master title style
00
‹#›
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
单击图标添加图片
单击图标添加图片
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
单击图标添加图片
单击图标添加图片
单击图标添加图片
编辑标题文字Click to edit Master title style
单击图标添加图片
单击图标添加图片
单击图标添加图片
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
单击图标添加图片
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
编辑正文文字
单击图标添加图片
编辑标题文字Click to edit Master title style
部门
会议名称
保密级别
▢
SECRET
▢
CONFIDENTIAL
▢
INTERNAL
‹#›
Placeholder subtitle (optional)
First level
First level
First level
First level
First level
‹#›
Placeholder slide title
Creation date: mm.dd.yy  |  Responsible department for filing: C-GSx  |  CSD-Class: xx.x – xx years  |  Data classification: CONFIDENTIAL
编辑标题文字
Click
to
edit
Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
单击图标添加图片
单击图标添加图片
单击图标添加图片
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
SVW EC
保密级别
SECRET
CONFIDENTIAL
INTERNAL
0
变更内容说明
（需求方填写，一般为
PO
或者
FO
）
变更主题
动态数据采集
要求变更
变更编号
3ER(Export)-CR-E-20260417-02
计划断点版本
F
平台
VR1
变更类型
变更
涉及车型
F 6S LHD export
CR
编号
/
PRD
链接
无
PRD
，仅有
CR
申请单。
签字
_3ER(Export)-CR-E-20260417-02-
动态数据采集变更
变更原因：
出口车型需求
变更前：
动态数据采集功能链路车端接收云端动采平台下发的任务
,
采集数据上传到指定云端
变更后：
出口项目涉及的云端动采平台和数据落点都在国外平台
,
所以需要更改相关的
URL,
功能能力不变
1
技术方案
技术方案描述：
（主要描述功能方案，一般由
SO/
架构填写，）
QNX，Android，S32GA都是通过Datapool上报数据，所以要变更URL。
然后开关状态上报URL也要变更
受影响方说明：
ZXD-VAL
模块更改
涉及到的系统或者零件，主要影响
根据需求，如果内容较多，可增加页进行描述
找
薛海强确认方案
2
技术方案
车端相关：
ZXD
零件
ZXD-DRE
及系统需求
EA-
朱芙蓉
需明确承接人员
ZXD
集成的加密模块可能有影响（国密
/
洋密）
Task
：
确认
HMI
和
32G-A
之间通信协议是否沿用国内
确认
ZXD
开发分工是否沿用国内
ZXD
动采软件架构
SP-
庞元
ZXD
软件需求
SP-
刘兰花
ZXD
动采软件开发
SP
团队
URL
确认及开发
云：
SP & VC SRE
ZXD
：
EA
大众
&
海外出行
ZXD
集成的
URL
上传地址有影响
Task
：确认不同国家（越南
/
澳新），车端上传
URL
是否区分
LHZCU/RHZCU
ID-DRE
需明确承接人员
RZCU
SP
提供软件
运动中心负责集成
IAM
通道确认
车载信息子系统
Task
：
确认通道是否沿用国内策略
确认海外运维、流量费用问题
座舱埋点开发
IC
Task
：确认开发方是否为
IC
注意：座舱埋点采集功能条目依赖开发方为
IC
，如果开发不为
IC
，该条目会被拿掉
HMI(
隐私政策
+
动采开关
)
IR-
闻文
(UI/UE
设计和开关实现
)
IR-
顾恺成（隐私政策）
Task
：
确认是否复用国内策略，数据安全信息安全确认
3
架构影响评估
序号
评估项
是否影响
主要影响描述
表态方
计划完成时间
1
功能清单
N
填写影响简单描述，如无影响填写
/
Zhang yinyin
可填写具体时间，或者写跟随架构
XX
阶段发布
2
整车拓扑
N
Wang Xiaoli
3
网络负载
N
涉及
Safety CAN
增加负载
Wang Zhipeng
4
数据库
N
Wang Xiaoli
5
休眠唤醒
N
无特殊休眠唤醒需求
Wang Xiaoli
6
诊断需求
N
Hu Rui
7
整车配置
N
SO
8
原理图
N
Wang Xiaoli
9
低压配电
N
无配电通道需求
Fan Youchen
10
静态功耗
N
Fan Youchen
11
SSTS
动态数据采集
SSTS
SO/
王晓丽
4
架构影响评估
序号
评估项
是否影响
主要影响描述
表态方
计划完成时间
12
整车服务
N
Wang
Qiangqiang
13
以太网
N
不涉及
Liang Jialong
14
网络安全
N
网络安全一般件（
Homo
需要网络安全测试并有测试报告：安全刷新、硬件强化、软件强化、诊断、车内通讯安全、密码技术与安全算法）
Peng Xiaoyan
15
功能安全
N
ASIL A
（
Purple QM
，待确认）
Jiang Zhuheng
16
OTA
N
有
OTA
需求
Zhang Jiatong
17
能耗
N
Fan Youchen
18
集成测试
Y
19
EID/
线束
N
Hu
Yinglu
20
法规认证
N
架构评估结论
动态数采方案未与总院拉齐，待
SO
明确方案后重新评估
本页评估结论由各项
架构相关方
&SO
确认
5
零件受影响方说明
序号
变更零件
变更说明
预估费用
表态方
计划完成时间
1
ZXD
Android，QNX，S32GA都涉及数据的上传，后台变更，需要变更上报的URL；
S32GA接收云端任务平分配到各个主域控进行数据采集，车端也要上报当前采集开关的状态，后台变更，上报的URL要变更
Ma
Gaoyuan
/Shao Bingqing
2
LHZCU
不涉及
Peng Xiaoyan
3
RHZUC
不涉及
Jiang
Zhuheng
评估结论
可行，主要变更在云端（云端方案复用智己海外项目方案）
本页评估结论由
SO
拉齐各方给出

---

## PPTX: 动采_AF\AF.pptx

图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
AB
车数据回传链路
供应商云
坐标偏转
重要地理位置数据不采集
人脸车牌脱敏
合规处理
图商合规专区
SVW
专区
合规云
(
上汽大众
)
转发
数据传输
(SVW&
图商授权
)
图商授权访问
数据挖掘
数据标注
测试验证
算法开发
Vehicle
ZXD
Domain
IAM
(T-BOX)
动态采集
Other ECUs
Other ECUs
SVW Cloud
动采网关
RTM
网关
网关
数据存储
RTM
国家
/
地方平台
智驾数据
(
含敏感数据
)
动采
&RTM
数据（非敏感数据）
RTM
合规处理
IPD
解决方案制定
数据分析
问题
/
事故回放
驾驶行为
测试验收
数据存储
工具链
公有云
(
上汽大众
)
维修售后
电池健康
车辆维保
大数据平台

---

## PPTX: 动采_AF\A车动采资源汇报 - 副本.pptx

‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
动采信号更新计划
&
配置流程
动采信号更新原因（更新范围包含数量，采集方式，上传方式）：
运维费用（车辆数量，触发类型，采集周期等因素）
售后问题分析
数据分析需求变更
时间节点
更新计划
SOP
CANLIN
：根据基线
座舱埋点：根据基线
SOA
：根据基线
SOP+3
每两周
Review
：
CI
给出资源费用报告
邀请需求方分享数据应用案例
2.
根据报告结果更改采集配置
SOP+3
后
按需提交需求
第一年：每三个月
Review
，按实际情况更新采集配置
第二年：每年
4
月，
10
月
Review
，按实际情况更新配置
OTA
按需提交需求
数据导出
部门
测试联调
&
功能优化
ECC
售后问题分析
MQ/ECC
其他
CI
1
F
车动采
&
埋点采集需求现状
信号类型
数量（个）
频率（
ms
）
数量（个）
CAN/LIN/
埋点帧
5433
完整采集
250
100
3017
200
127
500
148
1000
3411
3000
48
SOA
1349
完整采集
24
100
83
200
3
1000
1315
DCTP
（座舱埋点）
1240
事件触发
2
F
车埋点测试情况
目前埋点数据入库率：
821/1240
，其中
135
个为
SOP+3
需求实现，如下为当前埋点问题票清单：
JIRA
票号
票问题描述
（点击没有埋点上报或上报内容不符合定义）
修复计划
BSUVVW-9074
Dock
栏内部分功能
分析中
BSUVVW-9197
负一屏下部分功能
V5.0.19
BSUVVW-9481
BSUVVW-17600
SDS
语音部分功能埋
V6.1.10
BSUVVW-9483
BSUVVW-17601
智能场景部分功能
V5.0.19
BSUVVW-14385
BSUVVW-17599
蓝牙耳机设置部分功能
V6.1.9
BSUVVW-14458
智驾
-
泊车设置部分功能
分析中
BSUVVW-18076
BSUVVW-18083
地图部分功能
分析中
BSUVVW-17597
香氛部分功能
V5.0.19
BSUVVW-17598
车外声音部分功能
V5.0.19
BSUVVW-17602
停车拍照部分功能
V6.1.9
BSUVVW-17603
退出放电管理页面部分功能
分析中
BSUVVW-17596
座椅设置部分功能
分析中
BSUVVW-17592
灵动
widget
部分功能
分析中

---

## PPTX: 动采_AF\B SUV EREV数据采集_20241029_v1.0.pptx

图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
部门
会议名称
保密级别
SECRET
CONFIDENTIAL
INTERNAL
‹#›
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
‹#›
编辑标题文字Click to edit Master title style
部    门 Division：
标题文本
版本号 Version：
版本号 Version：
‹#›
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
版本号
Version
：
部门名称   会议名称
Confidential
‹#›
单击此处编辑母版标题样式
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
部门名称   会议名称
Confidential
‹#›
单击添加目录文本
部门名称   会议名称
Confidential
‹#›
目录
CONTENTS
单击添加节标题文字
节标题下分二级目录或章节介绍
部门名称   会议名称
Confidential
‹#›
00
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
Click to edit Master subtitle style
Thanks.
Copyright © SAIC VOLKSWAGEN. All rights reserved
SAIC VOLKSWAGEN owns and retains all copyrights and other intellectual property rights in this presentation. It may not be reproduced, modified or copied nor used for any commercial purposes (e.g. manufacturing), nor communicated to any third parties without our written consent.
SAIC VOLKSWAGEN undertakes all reasonable efforts to ensure that the information in this presentation is accurate, complete and derives from reliable sources. SAIC VOLKSWAGEN however, does not represent nor warrant (either expressly or implicitly) accuracy, reliability, timeliness or completeness of such information. Therefore, SAIC VOLKSWAGEN is not liable for any errors, consequence of acts or omissions based on the entirety or part of the information available in this presentation.
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
部门
会议名称
保密级别
SECRET
CONFIDENTIAL
INTERNAL
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
部门名称   会议名称
Confidential
‹#›
部    门
Division
：
E
CC
B SUV EREV
数据采集
版本号
Version
：
V1.0
日    期
Date
：
2024.10.29
9
自驾合规云项目发包情况
Backup
10
MQB EVO
数据采集合规云框架（未实现）
Backup
11
MEB
数据采集合规云框架（
VW
AnHui
已上车）
Backup
1
AB
车数据回传链路
供应商云
坐标偏转
重要地理位置数据不采集
人脸车牌脱敏
合规处理
图商合规专区
SVW
专区
合规云
(
上汽大众
)
转发
数据传输
(SVW&
图商授权
)
图商授权访问
数据挖掘
数据标注
测试验证
算法开发
Vehicle
ZXD
Domain
IAM
(T-BOX)
动态采集
Other ECUs
Other ECUs
SVW Cloud
动采网关
RTM
网关
网关
数据存储
RTM
国家
/
地方平台
智驾数据
(
含敏感数据
)
动采
&RTM
数据（非敏感数据）
RTM
合规处理
IPD
解决方案制定
数据分析
问题
/
事故回放
驾驶行为
测试验收
数据存储
工具链
公有云
(
上汽大众
)
维修售后
电池健康
车辆维保
大数据平台
2
各数据采集区别
动采（
CDC
）
动采（
RTG
）
动采（
A/F
车）
VDU
（
C
车）
采集信号类型
CAN
信号
车辆数据（以太网，
ICAN
）
CAN/LIN/SOA/
埋点帧
CAN
信号
采集信号数量
127
263
需求收集中
需求收集中
可采集范围
3000+
接收方
ZXD/ZCU
5000+
采集信号方式
周期
周期
/
事件触发
周期
/
事件触发
周期
采集周期
1s
1s
根据需求配置
1s
上传周期
20s
60s
根据需求配置
10s
数据第一落点
DP
DP
零束云
One Backend
可配置性
上传周期，信号数量，信号类型
采集上传周期，信号数量，信号类型，事件触发方式
采集上传周期，信号数量，信号类型，事件触发方式
回传数据范围
3
各数据埋点区别
A
F
C
埋点
SDK
开发
零束
零束
火山
数据第一落点
零束云
零束云
One Backend
数据落库
神策
神策
神策
埋点数量
2000+
2000+
2000+
采集周期
事件触发
事件触发
事件触发
上传周期
根据需求配置
根据需求配置
根据需求配置
数据类型
用户在车机上的点击行为，
APP
的使用记录
4
各数据采集区别
动采（
CDC
）
动采（
RTG
）
RTM
动采（
B
车）
智驾数据采集
采集信号类型
车辆数据（
CAN
）
车辆数据（以太网，
ICAN
）
车辆数据
(CAN)
车辆数据，用户数据（
CAN/LIN/
SomeIP
）
传感器数据，车辆数据，智驾算法数据，日志
采集信号数量
127
263
120
定义中
采集信号方式
周期
周期
/
事件触发
周期（
DTC
除外）
周期
/
事件触发
事件触发
采集周期
1s
1s
1s
（法规要求不低于
1s
）
定义中
/
上传周期
20s
60s
28s
（法规要求不大于
30s
）
定义中
/
数据量
18960KB
平均
7214KB/
车
/
天
平均
300KB/
车
/
天
定义中
500MB/
包
可配置性
上传周期，信号数量，信号类型
采集上传周期，信号数量，信号类型，事件触发方式
上传周期可配置
采集上传周期，信号数量，信号类型，事件触发方式
事件触发方式
补发机制
无
有
有
有
有
5
数据链路采集内容
智驾数据
RTM
数据
动采数据
数据内容
数据来源
数据内容
数据来源
数据内容
数据来源
非敏感数据
车辆数据
车辆
CAN
总线上的车身、底盘、轮速信号
车辆数据
车辆
CAN
总线上的电池，电驱，故障信号，报警信号
车辆数据
用户数据
车辆
CAN
总线上的车身，底盘，轮速信号（和智驾重复部分）
车辆
CAN
总线上的电池，刹车，灯具，故障，电驱信号
应用使用情况
应用设置项
敏感数据
智驾算法数据
定位、地图、感知、预测、规划、控制等模块的输出信号
/
/
/
/
日志
进程模块产生的日志文件
/
/
/
/
传感器数据
Camera、Lidar
、
IMU、USS
等传感器信号
/
/
/
/
动采和
RTM
在电池相关信号上有部分重复。
RTM
由于法规要求，采集和上传频率固定，而专业科室需要更高频率的信号来满足应用要求，所以在动采上以更高的频率重复采集了电池相关的信号。
动采采集信号的需求收集自各个专业科室，对于智驾部分信号，如果智驾部门统一收集上传到合规云，且其他专业科室没有需求，动采可以不进行重复采集。
以往项目动采数据中智驾信号不到
10%
R  80
G  80
B  80
R  0
G  181
B  226
R  166
G  187
B  200
R  51
G  63
B  72
基础色
R  255
G  91
B  63
R  188
G  35
B  47
R  140
G  226
B  208
R  0
G  115
B  119
辅助色
6
Backup
8
智驾数据链路采集内容
数据内容
数据来源
数据大小
采集频率
传感器数据
Camera、Lidar
、
IMU、USS
等传感器信号
500MB
无固定频率。数采基于事件触发方式采集。
车辆数据
车辆
CAN
总线上的车身、底盘、轮速信号
智驾算法数据
定位、地图、感知、预测、规划、控制等模块的输出信号
日志
进程模块产生的日志文件
Backup
智驾数据闭环基于需求驱动，通过
OEM
自定义筛选器的事件触发逻辑，采取并处理有价值的数据。
主要数据内容包含传感器数据、车辆数据、算法数据及日志等。

---

## PPTX: 动采_AF\动采+埋点状态汇报.pptx

图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
SQL
是：
select id, vin,
sale_status
,
invoice_time
,
case
invoice_time
when '' then 1 else 0 end as '
销售状态
',
bind_user_ids
,
case
bind_user_ids
when '' then 1 else 0 end as '
绑车状态
'
from
ddc_vehicle_bind_sale_status
where
update_time
> '2026-03-26 00:00:00'
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
埋点状态与计划
2025
2026
10月
11月
12月
1月
2月
3月
43
44
45
46
47
48
49
50
51
52
01
02
03
04
05
06
07
08
09
10
11
12
13
0SBugFix2
0SBugFix1
0S
PVS
BugFix
PVS
埋点（
ODC
开发）
（事件：
245
个；
Key
：
506
个）
数据质量监控
2
nd
Full Test Ongoing
Till today
通过率：
406/506
1
st
Full Test
通过率：
0/506
埋点（零束开发）
（事件：
1016
个；
Key
：
2448
个）
数据质量监控
2
nd
Full Test
1
st
Full Test Ongoing…
Till today
通过率：
333/522
工作内容
点检测试通过率：
355/400
动采通道测试（台架
+
实车）
Go live
0S BugFix1
通道
√
Ready
PVS BugFix1
通道
√
Ready
Full-size SUV 6S
SOP
描述
案例
分析
&
进展
Ticket
修复节点
问题
1
埋点携带经纬度
事件名：无路线进入算路页
上报内容：
{…,
POIlongitude
=121.16483441113324
,
eventname
=
hu_navirouteEnter
,
POIlatitude
=31.301196793957768
}
问题：经纬度为敏感个人信息，目前合规方案设计，通过埋点上报有严重合规问题
BSUVVW-7325
SOP
前
问题
2
上报事件
DataID
错误
DataID
：
03000102010000000000000000300411
事件名：遮阳帘调节；雨刮设置开关；右侧后视镜下倾设置等
问题：多条事件使用同一个
DataID
上报，理论上
DataID
和事件名应该一一对应
BSUVVW-7404
SOP
前
问题
3
上报内容和定义不符
事件名：
DVR
拍视频，属性：
trigger_method
,
eventname
上报内容：
{"hu_dvr_takevideo":"0"}
问题：
Event
作为埋点上报必须字段，错误或者缺失会导致后续无法入神策
进展：
1.
内容问题建票修改
2.
格式问题，和
CIX
沟通可以统一反馈在大数据平台做数据预处理
BSUVVW-7350
应修尽修，部分不影响数据入库问题可接受
SOP+
基线修复
测试覆盖度：
21.3%
测试覆盖度：
100%
3
rd
Full Test
需要零束支持：
对零束开发各应用埋点的数据质量进行测试，并提供测试报告
重新整理各产品手中的埋点定义，形成
SOP
前锁定的最终版本，并外发给
SVW
。
支持
SVW
验收中对于需求的疑惑点解读，比如找不到入口，事件不理解等
1
动采
+
埋点状态与计划
2025
2026
10月
11月
12月
1月
2月
3月
43
44
45
46
47
48
49
50
51
52
01
02
03
04
05
06
07
08
09
10
11
12
13
0SBugFix2
0SBugFix1
0S
PVS
BugFix
PVS
动采信号（
CAN/LIN/SOA
）
手动触发
+
测试车监测
+
跑车监测
手动触发
+
测试车监测
√
Ready
（
F
车）
CAN/LIN:1287
，
SOA:41
埋点（
ODC
开发）
（事件：
245
个；
Key
：
506
个）
数据质量监控
2
nd
Full Test Ongoing
Till today
通过率：
406/506
1
st
Full Test
通过率：
0/506
埋点（零束开发）
（事件：
1016
个；
Key
：
2448
个）
数据质量监控
2
nd
Full Test
1
st
Full Test Ongoing…
Till today
通过率：
333/522
工作内容
点检测试通过率：
355/400
动采通道测试（台架
+
实车）
Go live
0S BugFix1
通道
√
Ready
PVS BugFix1
通道
√
Ready
Full-size SUV 6S
SOP
埋点：
零束开发：
ODC
开发：部分应用的开发者未启动埋点开发（如
Avatar
），或应用本身未完成开发导致埋点无法测试
动采（
CAN/LIN/SOA
）
:
A
车
ZCU
性能问题导致和
ZCU
相关的
SOA
信号无法采集，部分
CAN
信号无法采集

已通过更改
ZCU
内部的采集方案以保证
CAN
，
LIN
信号采集不受影响，但是
SOA
无法实现动态采集
描述
原因
ticket
Action
问题
1
车端触发了埋点，神策无法入库
上传的数据和前期零束的定义
不匹配
，导致数据无法落库
BSUVVW-3280
，
BSUVVW-3281
，
BSUVVW-3283
等
提票给零束修改
和CIX约定在大数据平台做数据预处理
问题
2
部分零束开发的应用埋点
SVW
无法测试
埋点的触发手顺零束
未反馈；
各应用的埋点开发进度零束
未反馈
-----
全量测试，有问题直接提票
问题
3
测试进程缓慢
测试资源不足：
ECC
的
5
台车被
IAM
，
RTM
，数字钥匙全时占用，
ECE
的车测试登记表难约；测试人员仅
FO
一人
-----
需要协调专门的开发测试用车，而非
share
点检测试资源，以按时完成整体的开发测试进度
测试覆盖度：
21.3%
测试覆盖度：
100%
3
rd
Full Test
2
A
车
ZCU
汇报方案
动采技术方案
①
基于车云服务交互，云端采集任务动态灵活配置下发，实现数据采集；
②
动采主控模块在
ZXD-QNX
（
8155-QNX
）部署，支持
CAN/LIN/SOA/ASF/DCTP
采集。
③
ZCU
与动采主控模块进行指令和数据交互，支持
CAN/LIN/SOA
采集
ZCU
采集方案
预计实施：
7
月
4
日释放需求，要求在
VFF
基线实施
实施现状：
11
月
12
日接到延锋反馈，因
ZCU
资源受限，目前无法按计划部署
ZCU
采集方案
预计影响
（涉及部分
CANLIN
和
MCUSOA
采集）
LHZCU
下挂
LHBDCANFD
整网段以及部分
BKBCANFD
网段
CAN
信号无法采集（
影响
VFF
基线低配共计
93
，高配共计
88
个信号；其中需求信号
9
个
）；
LHZCU/RHZCU
下挂
LIN
节点信号无法采集（
影响
VFF
基线共计
137
个信号；其中暂无需求信号
）；
SOA
无法采集
实施方案
保留原有与
ZXD
采集脚本的交互逻辑，接收脚本内的标志位确认是否开始全量采集（而非根据脚本在
ZCU
里动态配置采集任务）
SOA
无法采集（有任何配置
ZCU
资源无法支撑）
固定采集周期为：
100ms
外发周期为：
100ms
ZCU
执行动采示意图（以
CANLIN
为例）
3
AB
车数据回传链路
ZXD
Vehicle
IAM
动态采集
RHZCU
SVW Cloud
零束云
动采平台
大数据平台
SVW
LHZCU
RZCU
埋点
SDK
APP
ODC
开发
APP
零束开发
座舱埋点数据
CAN/LIN/SOA
神策
座舱埋点数据
数据上传
Https
采集规则下发
MQTT
采集规则
4
动态采集通道能力各条目状态：
功能整体状态
A
车
F
车
CAN/LIN
周期采集
VFF 3.0.16 Ready
PVS 4.0.15 Ready
，
0S
计划
5.0.5
版本
CAN/LIN
完整采集
CAN/LIN
事件采集
SOA
周期采集
SOA
时间采集
座舱埋点周期采集
边缘计算
5
功能整体状态
0S
基线埋点需求：
零束：
1016
个事件，包含
2448
个
KEY
。目前已覆盖
199
个事件，包含
522
个
KEY
，成功率
333/522
ODC
：
245
个事件，包含
506
个
KEY
。目前已覆盖
183
个事件，包含
406
个
KEY
，成功率
268/406
6
功能链路
7
动采平台合规前提
车端
DDC
动采平台
主数据平台
绑车状态
销售
状态
数据合规需求
销售状态
未售出
售出
-
绑车状态
-
绑车
解绑
数据采集状态
可采集
可采集
不可采集
ZX
云
绑车状态
销售
状态
绑车状态
销售
状态
开关状态
开关状态
SVW
云
经分析
Redis
异常，导致一段时间内的数据缺失（导致车端收到的状态和实际状态不符），所以
总院需要
3.26-4.8
的绑车和销售状态数据进行云端补录

---

## PPTX: 埋点\C\CEA2.x 产品定义及PRD审议会 – KW02.pptx

2026/2/26
单击此处编辑母版文本样式
二级
三级
四级
五级
‹#›
部    门
Division
：
单击此处编辑母版标题样式
单击图标添加图片
版本号
Version
：
版本号
Version
：
Action title in The Group Head Light 18pt, White
Headline in The Group Head Light 28pt, White
24.05.2024
CEA SteerCo | CSD-class: 12.2 - 20 years
‹#›
We
transform automotive mobility
Presentation Title
Placeholder subtitle | place | date [optional]
2/26/2026
R&D PACEMAKER INITIATIVE | Status Report
‹#›
Action title in The Group Head Light 18pt, Vivid Green
Headline in The Group Head Light 28pt, Deep Space Blue
Title in The Group Head Light 44pt, White
Click to edit Date / Department
Click to edit classification
INTERNAL
15th Aug 2024
TOP1  |  Status Aufbau CEA Operational Hub  |  CSD-class 12.2 - 20
‹#›
Mastertextformat bearbeiten
Zweite Ebene
Dritte Ebene
Vierte Ebene
Fünfte Ebene
Headline in The Group Head Light 28pt, White
Action title in The Group Head Light 18pt, White
部    门
Division
：
单击此处编辑母版标题样式
单击图标添加图片
版本号
Version
：
版本号
Version
：
‹#›
单击此处编辑母版标题样式
单击此处编辑母版标题样式
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
单击添加目录文本
‹#›
目录
CONTENTS
部门名称   会议名称
Confidential
‹#›
单击此处编辑母版标题样式
单击添加节标题文字
节标题下分二级目录或章节介绍
‹#›
00
Click to edit Master subtitle style
Thanks.
Copyright © SAIC VOLKSWAGEN. All rights reserved
SAIC VOLKSWAGEN owns and retains all copyrights and other intellectual property rights in this presentation. It may not be reproduced, modified or copied nor used for any commercial purposes (e.g. manufacturing), nor communicated to any third parties without our written consent.
SAIC VOLKSWAGEN undertakes all reasonable efforts to ensure that the information in this presentation is accurate, complete and derives from reliable sources. SAIC VOLKSWAGEN however, does not represent nor warrant (either expressly or implicitly) accuracy, reliability, timeliness or completeness of such information. Therefore, SAIC VOLKSWAGEN is not liable for any errors, consequence of acts or omissions based on the entirety or part of the information available in this presentation.
单击此处编辑母版标题样式
‹#›
编辑标题文字
Click
to
edit
Master title style
‹#›
部门名称   会议名称
Confidential
‹#›
单击此处编辑母版标题样式
2/26/2026
‹#›
‹#›
编辑标题文字Click to edit Master title style
单击此处编辑母版标题样式
单击此处编辑母版副标题样式
19.07.2023
Department K-OE  |  Presentation title  |  CSD-class
‹#›
单击此处编辑母版标题样式
单击此处编辑母版副标题样式
19.07.2023
Department K-OE  |  Presentation title  |  CSD-class
‹#›
部门名称   会议名称
Confidential
‹#›
单击此处编辑母版标题样式
部    门
Division
：
单击此处编辑母版标题样式
单击图标添加图片
版本号
Version
：
版本号
Version
：
部    门
Division
：
单击此处编辑母版标题样式
单击图标添加图片
版本号
Version
：
版本号
Version
：
‹#›
单击此处编辑母版标题样式
单击此处编辑母版标题样式
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
单击添加目录文本
‹#›
目录
CONTENTS
单击添加节标题文字
节标题下分二级目录或章节介绍
‹#›
00
单击添加目录文本
‹#›
目录
CONTENTS
单击添加节标题文字
节标题下分二级目录或章节介绍
‹#›
00
Click to edit Master subtitle style
Thanks.
Copyright © SAIC VOLKSWAGEN. All rights reserved
SAIC VOLKSWAGEN owns and retains all copyrights and other intellectual property rights in this presentation. It may not be reproduced, modified or copied nor used for any commercial purposes (e.g. manufacturing), nor communicated to any third parties without our written consent.
SAIC VOLKSWAGEN undertakes all reasonable efforts to ensure that the information in this presentation is accurate, complete and derives from reliable sources. SAIC VOLKSWAGEN however, does not represent nor warrant (either expressly or implicitly) accuracy, reliability, timeliness or completeness of such information. Therefore, SAIC VOLKSWAGEN is not liable for any errors, consequence of acts or omissions based on the entirety or part of the information available in this presentation.
单击添加目录文本
部门名称   会议名称
Confidential
‹#›
目录
CONTENTS
Click to edit Master subtitle style
Thanks.
Copyright © SAIC VOLKSWAGEN. All rights reserved
SAIC VOLKSWAGEN owns and retains all copyrights and other intellectual property rights in this presentation. It may not be reproduced, modified or copied nor used for any commercial purposes (e.g. manufacturing), nor communicated to any third parties without our written consent.
SAIC VOLKSWAGEN undertakes all reasonable efforts to ensure that the information in this presentation is accurate, complete and derives from reliable sources. SAIC VOLKSWAGEN however, does not represent nor warrant (either expressly or implicitly) accuracy, reliability, timeliness or completeness of such information. Therefore, SAIC VOLKSWAGEN is not liable for any errors, consequence of acts or omissions based on the entirety or part of the information available in this presentation.
单击此处编辑母版标题样式
‹#›
编辑标题文字
Click
to
edit
Master title style
‹#›
部门名称   会议名称
Confidential
‹#›
单击此处编辑母版标题样式
2/26/2026
‹#›
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅
色背景图像
To insert a light
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
单击添加节标题文字
节标题下分二级目录或章节介绍
部门名称   会议名称
Confidential
‹#›
00
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
单击此处编辑母版标题样式
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
部门名称   会议名称
Confidential
‹#›
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
编辑母版文本样式
单击此处编辑母版标题样式
‹#›
单击此处编辑母版标题样式
单击此处编辑母版副标题样式
2026/2/26
‹#›
‹#›
标题占位符
Placeholder slide title
2/26/2026
‹#›
编辑标题文字
Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
Click to edit Master subtitle style
Thanks.
Copyright © SAIC VOLKSWAGEN. All rights reserved
SAIC VOLKSWAGEN owns and retains all copyrights and other intellectual property rights in this presentation. It may not be reproduced, modified or copied nor used for any commercial purposes (e.g. manufacturing), nor communicated to any third parties without our written consent.
SAIC VOLKSWAGEN undertakes all reasonable efforts to ensure that the information in this presentation is accurate, complete and derives from reliable sources. SAIC VOLKSWAGEN however, does not represent nor warrant (either expressly or implicitly) accuracy, reliability, timeliness or completeness of such information. Therefore, SAIC VOLKSWAGEN is not liable for any errors, consequence of acts or omissions based on the entirety or part of the information available in this presentation.
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
部门名称   会议名称
Confidential
‹#›
-
Draft -
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
‹#›
CEA 2.x Requirement
Status Report
TOP 1
Presenter:	PVP, Shao Chunhui
SVW-PSK/27.08.2025
confidential
‹#›
CEA 2.x Requirement
Status Report
TOP 1
Presenter:	PVD, Shao Chunhui
SVW-PSK/27.08.2025
confidential
Edit Master text styles
Second level
Third level
Fourth level
Fifth level
Level six
Level seven
Level eight
Level nine
8,40
15,80
4,40
6,60
15,80
Click to add title
24.05.2024
CEA SteerCo | CSD-class: 12.2 - 20 years
‹#›
INTERNAL
Click to edit slide title (maximum two lines)
Click to edit text
Second level
Third level
Fourth level
15th Aug 2024
TOP1  |  Status Aufbau CEA Operational Hub  |  CSD-class 12.2 - 20
‹#›
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
Click to edit slide title (maximum two lines)
Click to edit text
Second level
Third level
Fourth level
19.07.2023
Department K-OE  |  Presentation title  |  CSD-class
‹#›
8,40
15,80
4,40
6,60
15,80
INTERNAL
Click to edit slide title (maximum two lines)
Click to edit text
Second level
Third level
Fourth level
19.07.2023
Department K-OE  |  Presentation title  |  CSD-class
‹#›
8,40
15,80
4,40
6,60
15,80
INTERNAL
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
1
CEA2.x
运营
组
PRD
汇报
–
数据平台及能力
RPD
2.
3
CEA2.x
新增
–
边缘计算
CMP
车端信号
ECUs
数据采集
边缘计算
计算模块
存储
模块
配置监听
数据上传
云端配置
数据平台
数据输入
数据分析
数据上传
云端
TBox
技术优势
应用价值
边缘计算
+
云端协同：
车端
毫秒级
数据的收集与处理
基于场景模型的计算与存储
云端实时更新和迭代模型
降低数据运维成本
实时响应数据相关分析需求

---

## PPTX: 埋点\C\CMP21D data_20250617.pptx

2026/6/25
单击此处编辑母版文本样式
二级
三级
四级
五级
‹#›
1
单击此处编辑母版标题样式
单击以编辑母版副标题样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
图 片 占 位 符
部    门
Division
：
单击此处编辑母版标题样式
版本号
Version
：
版本号
Version
：
编辑分隔页标题文字
Click to edit Master title style
00
‹#›
EHA
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
EHA
编辑标题文字
Click to edit Master title style
EHA
编辑正文文字
Click to edit Master text styles
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
添加文本、图片、图形、图表、表格等内容
Click to edit text, pictures, graphics, charts, tables, etc.
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
添加图片、图形、图表、表格等内容
Click to edit pictures, graphics, charts, tables, etc.
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
编辑标题文字
Click to edit Master title style
图 片 占 位 符
图 片 占 位 符
图 片 占 位 符
部门  会议名称  保密级别
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
编辑正文文字
Click to edit Master text styles
图 片 占 位 符
编辑标题文字
Click to edit Master title style
部门  会议名称  保密级别
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
单击此处编辑母版标题样式
编辑母版文本样式
2026/6/25
‹#›
编辑正文文字
Click to edit Master text styles
‹#›
编辑标题文字
Click to edit Master text styles
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
单击此处编辑母版标题样式
2026/6/25
‹#›
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
编辑母版文本样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
2026/6/25
‹#›
单击此处编辑母版标题样式
编辑母版文本样式
第二级
第三级
第四级
第五级
2026/6/25
‹#›
编辑标题文字
Click to edit Master title style
编辑正文文字
Click to edit Master text styles
第二级
Second level
第三级
Third level
第四级
Fourth level
第五级
Fifth level
‹#›
EHA
Xue Haiqiang
: SVW data FO
Qin jingyi: SVW Connectivity PL
Jiang
chengjun
: GC One backend PL
Liu
tengfei
: SVW SP PL
Wang zhiming: One team GB
埋点
SE
Xu
shiqi
: One Team Data PO
Han
weitao
/jiang
xia:OB
埋点云端开发
Zhuang
chunxiao
: SVW SP
埋点
/
数采开发

---

## PPTX: 埋点\C\Vehicle data sharing usage status  request_20260330 - 副本.pptx

Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year
| Department
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
Contact slide
As of 00. Month 2019 I Version X.X
点击图标
插入
浅
色背景图像
To insert a light
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year
| Department
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅
色背景图像
To insert a light
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
分隔页
Divider
副标题
Subline
‹#›
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
分隔页
Divider
副标题
Subline
‹#›
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
Contact slide
As of 00. Month 2019 I Version X.X
单击此处编辑母版标题样式
Confidential
‹#›
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year
| Department
点击图标
插入
深
色背景图像
To insert a dark
background image: Please click on the image
placeholder and then select an image by clicking on the
“Insert“ tab and choosing the “Pictures“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
深色
背景
视频
To insert a dark background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅色
背景
视频
To insert a light background video: Please click on the media
placeholder and then select a video by clicking on the “Insert“ tab and
choosing your preferred file via the “Video“ command.
Data classification: Internal
主标题
Presentation title
副标题
Subtitle
Location | Month Day, Year | Department
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
深色
背景
图像
To insert a dark background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
点击图标
插入
浅色
背景
图像
To insert a light background image: Please click on the image placeholder and then
select an image by clicking on the “Insert“ tab and choosing the “Pictures“ command.
分隔页
Divider
副标题
Subline
‹#›
Edit Master text styles
分隔页
Divider
副标题
Subline
‹#›
分隔页
Divider
副标题
Subline
‹#›
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
章节标题
Chapter title
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
X.X
小节
Sub-chapter
‹#›
议程
Agenda
副标题占位符
Placeholder subtitle (optional)
第一层级
第一层级
第一层级
First level
First level
First level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
‹#›
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
正文小标题占位符
第二层级
第三层级
第三层级
第三层级
‹#›
Placeholder Subtitle
Second level
Third level
Third level
Third level
标题占位符
Placeholder slide title
副标题占位符
Placeholder subtitle (optional)
‹#›
标题占位符
Placeholder slide title
分隔页
Divider
副标题
Subline
‹#›
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
描述
信息汉仪旗黑
60S
60pt
Describing Copy in
VW Head Office 60
pt
‹#›
VW Head Office Bold 60
pt
点击图标
插入深色背景图像
Insert a dark image by clicking on symbol on the left
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
‹#›
点击图标
插入
浅色
背景图像
Insert a light image by clicking on symbol on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入深色背景图像
Insert a dark image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
VW Head Office Bold 44
pt
Edit Master text styles
点击图标
插入
浅
色背景图像
Insert a light image by                                                            clicking
onsymbol
on the left
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office 44
pt
Headcopy
in VW Head Office 44
pt
Edit Master text styles
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
汉仪旗黑
60S
44pt
Describing Copy in VW Head Office
44
pt
VW Head Office Bold 44
pt
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
正文小标题
Placeholder Subtitle
第二层级
Second level
第三层级
Third level
第三层级
Third level
第三层级
Third level
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
点击图标
插入
图片
Insert an image by clicking on symbol below
‹#›
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
第一层级
First level
分隔页
Divider
副标题
Subline
‹#›
副标题占位符
Placeholder subtitle (optional)
标题占位符
Placeholder slide title
图表标题
Graph headline
单位
Value unit
点击图标
插入
图表
Insert a graph by clicking on symbol below
*
脚注
Space for Footnotes
‹#›
Contact slide
As of 00. Month 2019 I Version X.X
标题文本
编辑分隔页标题文字Click
to edit Master title style
00
‹#›
编辑正文文字
编辑分隔页标题文字Click
to edit Master title style
编辑正文文字
‹#›
单击图标添加图片
部    门 Division：
标题文本
版本号 Version：
版本号 Version：
部门
会议名称
保密级别
SECRET
CONFIDENTIAL
INTERNAL
‹#›
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
演示
文稿标题占位符
Placeholder slide title
副标题
占位符
Placeholder Subtitle
第二
层级
Second level
第三
层级
Third level
第三
层级
Third level
第三
层级
Third level
‹#›
标题文本
正文级别
1
正文级别
2
正文级别
3
正文级别
4
正文级别
5
‹#›
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
部门
会议名称
保密级别
SECRET
CONFIDENTIAL
INTERNAL
JV
0
CMP21 Data Sharing SVW Proposal
1.X Proposal
2.X Proposal
One Backend
One Backend
PO
Quality
Market
Data PO/FO
1. Requirement
2
. Analysis
3. Data Transform Config
JV
Data PO/FO
Todo:
Transform Config Portal
More Data Scope
JV
Data PO/FO
3. Data Collection Config
Todo:
Data Config Portal
Full DBC
Data Requirement
1.X Portal
The full data uploaded from the vehicle should be configured
Data should be configured in an open and flexible portal.
2.X Portal
Full DBC signals should be configured.
The configuration range includes: signal type, acquisition frequency, upload frequency
JV
own data decision instead of One Team
CMP21 One Backend CAN Data Security
JV is the
compliance entity
for automotive data security and privacy protection. Full compliance requires:
Vehicle data collection & One Backend data usage must be based on JV’s approval;
JV
requires a detailed list of whole vehicle data collection;
JV
should have right to decide data transmission scope.
D
ata collection in the privacy agreement
One Backend
SVW SP
MOS APP
Vehicle
Binding Status
Collectible Status
Binding Status
Signing the privacy agreement in the vehicle binding process
ADAS Achievements Sys
2
Contact
OneBackend
C|GC-4   ADAS
FO
ECCBackend
ECC-3   ADAS Report Backend FO
Tech Solution
Kafka
for public network
Data List
T+1 ADAS
per trip
（
39
data items / report
）
VIN
Model Code
Trip Start Time
Trip End Time
Driving Mileage
Driving Duration
ID Mileage
ID Duration
ID Proportion
NOA Mileage
NOA Proportion
NOA Duration
NOA Dur-proportion
LCC Mileage
LCC Proportion
LCC Duration
LCC Dur-proportion
ACC Mileage
ACC Proportion
ACC Duration
ACC Dur-proportion
Parking Freq
APA Freq
SVP
Freq
ASP Freq
PRA Freq
APA avg Duration
APA+RPA
Duration
APA+RPA
avg Duration
SVP+ASP
Mileage
Track
NOA
Track
LCC
Track
ACC Track
avg Speed
avg Consumption
Total
Consumption
Emission
Reduction
Trip
uuid
ADAS Achievements Sys
3
Data Usage
ADAS
Achievements
Vehicle Milestone
：
Driving Mileage
,
Driving Duration
, Valet Parking Mileage, Valet Parking Count
,
Auto Parking Count, Remote Parking Count
User
Badge
：
Driving Mileage
User Badge
(Examples of past badges)
Issue
Insufficient
data.
The lack of
userID
in OB makes it impossible to calculate badges. ECC Backend needs to obtain data from other sources, leading to issues such as inaccuracy.
Vehicle Milestone
(Examples of NIO App)

---

## PPTX: 数据采集汇总文档 - 副本.pptx

图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
图商提供
SDK
，
MMT
集成
SDK
，满足合规要求
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字 Click to edit Master text styles
编辑标题文字Click
to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click to edit Master title style
‹#›
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加文本、图片、图形、图表、表格等内容
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
添加图片、图形、图表、表格等内容
编辑正文文字
Click to edit Master text styles
编辑正文文字 Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字Click to edit Master text styles
编辑标题文字Click to edit Master title style
‹#›
编辑正文文字
编辑标题文字Click
to edit Master title style
保密级别
C3-Secret         C2-Confidential        C1-Internal        C0-Public
0
各数据埋点区别
A
F
C
埋点
SDK
开发
零束
零束
火山
数据第一落点
零束云
零束云
One Backend
数据落库
神策
神策
神策
埋点数量
2000+
2000+
2000+
采集周期
事件触发
事件触发
事件触发
上传周期
根据需求配置
根据需求配置
根据需求配置
数据类型
用户在车机上的点击行为，
APP
的使用记录
CEA2.X Data Collection Proposal
One Backend
SP
CDCU
RDCU/LDCU/…
NGX
ADAS Master
SP
CMP21D Status
：
One Backend
CEA2.X Proposal
：
车辆数据，边缘计算结果，智驾数据
One Backend
智驾数据
CCU
RDCU/LDCU/…
NGX
ADAS Master
T-Box
边缘计算
Vehicle
Vehicle
T-Box
One Backend
配置平台给到
JVs
配置数据采集范围（包括：信号类型，信号数量，采集频率，触发方式等）
数据第一落点在
SVW
SP
车端支持毫秒级采集频率
数据采集能力可升级
数据结构标准化
，
向前兼容
车端增加边缘计算能力
数据采集配置和边缘计算配置下发
车端数据全量采集，不可配置规则，
且不提供全量数据清单
车内信号频率为毫秒级，但采集频率只支持到秒级
数据采集链路冗余
SVW Cloud
非智驾数据
数采合规云
合规云
智驾
合规云
SVW Cloud
痛点
建议
VDU
Data Collection Master
*Entry Line
没有
NGX
，可以通过动采，采集智驾相关信号
C
车后台对接
C
车后台对接
C
车后台对接
C
车后台对接
1
各数据采集区别
动采（
CDC
）
动采（
RTG
）
动采（
A/F
车）
VDU
（
C
车）
采集信号类型
CAN
信号
车辆数据（以太网，
ICAN
）
CAN/LIN/SOA/
埋点帧
CAN
信号
采集信号数量
127
263
需求收集中
需求收集中
可采集范围
3000+
收发方
ZXD/ZCU
5000+
采集信号方式
周期
周期
/
事件触发
周期
/
事件触发
周期
采集周期
1s
1s
根据需求配置
1s
上传周期
20s
60s
根据需求配置
10s
数据第一落点
DP
DP
零束云
(
部署在
SVW)
One Backend
可配置性
上传周期，信号数量，信号类型
采集上传周期，信号数量，信号类型，事件触发方式
采集上传周期，信号数量，信号类型，事件触发方式
回传数据范围
2
AB
车数据回传链路
工具链
地图数据
问题数据
合规云
(MMT)
智驾合规云
(SVW)
智驾数据
工具链
大数据平台
智驾数据
非智驾数据
地图数据
问题数据
远程访问
SVW
数据湖
上汽大众云
Vehicle
IAM
(T-BOX)
ZXD
动态采集
RTM
合规处理
IPD
零束云
车端采集
&
上传逻辑：
车端请求数据采集清单
ZXD
将数据打包并全量
上传
至大数据平台
云端处理逻辑：
具有数据采集配置能力，可以在云端配置采集清单，下发到车端
非智驾数据
3
AB
车数据回传链路
供应商云
坐标偏转
重要地理位置数据不采集
人脸车牌脱敏
合规处理
图商合规专区
SVW
专区
合规云
(
上汽大众
)
转发
数据传输
(SVW&
图商授权
)
图商授权访问
数据挖掘
数据标注
测试验证
算法开发
Vehicle
ZXD
Domain
IAM
(T-BOX)
动态采集
Other ECUs
Other ECUs
SVW Cloud
动采网关
RTM
网关
网关
数据存储
RTM
国家
/
地方平台
智驾数据
(
含敏感数据
)
动采
&RTM
数据（非敏感数据）
RTM
合规处理
IPD
解决方案制定
数据分析
问题
/
事故回放
驾驶行为
测试验收
数据存储
工具链
公有云
(
上汽大众
)
维修售后
电池健康
车辆维保
大数据平台
4
AB
车数据回传链路
5
AB
车数据回传链路
6
C
车数据回传链路
工具链
地图数据
问题数据
合规云
(
Carizon
)
智驾合规云
(One Team)
智驾数据
工具链
数采合规云
(
One Team
)
Data Platform
Non-Geo Data
Vehicle
T-BOX
NGX
智驾数据
非智驾数据
CDCU/RDCU/LDCU/…
VDU
智驾数据上传
工具链
地图数据
问题数据
地图数据
问题数据
智驾数据
智驾数据
工具链
地图数据
问题数据
SVW Proposal
远程访问
SVW
智驾合规云
(SVW)
数据湖
合规云
(
Carizon
)
车端采集
&
上传逻辑：
各个域控制器以
1s
频率发送数据给
T-Box
T-Box
将数据打包并以
10s
的频率全量发送至
One Backend
（
geo-data
和
non-geo data
混合在一起
）
云端处理逻辑：
合规云对数据进行脱敏，区分
geo-data
和
non-geo data
One Backend
具有数据传输范围可配置能力，并开放
API
给到
JVs
进行配置
上汽大众云
C
车数据配置链路
CEA
原方案：
各个域控制器以
1s
频率发送数据给
T-Box
T-Box
将数据打包并以
10s
的频率全量发送至
One Backend
One Backend
具有数据传输范围可配置能力，并开放
API
给到
JVs
进行配置，配置范围仅限信号数量
CEA
原方案
SVW
新建议
SVW Proposal
：
One Backend
提供数据采集配置平台给到
JVs
配置数据采集范围（配置范围不仅限于：信号类型，信号数量，上传频率，触发方式等）
T-Box
向云端请求配置清单（时机：每一小时
/KL15 ON/
移动数据开关切换等
）
配置下发至车端，
T-Box
将数据按配置规则打包并实时并全量地上传
*
对于涉及应用可以收集需求在云端配置，后续应用场景变更或者拓展都可以通过配置平台更改采集需求，将影响范围减少到最小，也预留了灵活的更新能力。
Vehicle
T-BOX
CDCU/RDCU/LDCU/…
VDU
数采合规云
(
common
)
Data Platform
数据湖
上汽大众云
Vehicle
T-BOX
CDCU/RDCU/LDCU/…
VDU
数采合规云
(
common
)
Data Platform
数据湖
上汽大众云
采集规则配置平台
采集规则下发
更改范围
采集规则请求
VDU
Vehicle
T-BOX
CDCU/RDCU/LDCU/…
VDU
Data Platform
SVW Cloud
Vehicle Management
Diagnostic
配置下发
Data Service
Remote Service
Data Lake
MOS APP
One SDK
目前有很多服务依赖
VDU
的数据：车管平台，
One SDK
，数字车服务，售后诊断服务等
数据第一落点在
Data Platform
，
DP
接收实时信号后：
实时计算：
DP
先解析信号，然后根据车管的配置过滤信号，最后再将数据转回
存储
+
离线计算
信号的处理和存储工作都在
DP
侧
车管平台有信号转发功能，可以配置转发信号的
Scope

---

## PDF: VDU(C车动采)\CEA1.X\PRD\PDD_MOS021_整车级数据采集与上报_V1.0_外发版.pdf

PRD_MOS021_ 整 车 级数 据 采 集 与上 报 
 
版 本 和状 态 Version and Status 
当前版本：V1.0 
评审状态：已评审 
开发状态：已开始 
修 订 历史 
版本 日期 修 订人 修 订记 录 
号 
V0.6 2025.04.25 ... 
创建文档 
V0.7 2025.05.23 ... 
增加 4.2 灵活数采需求描述 
V0.8 2025.6.13 Xu, Shiqi 增加 4.7 权限域隐私控制 
V0.9 2025.6.17 Xu, Shiqi 
增加 5 系统依赖需求 
Dong, 
增加功能列表 
Menglin 
更新全文标号 
V1.0 2025.6.18 Dong, 
更新 4.7.3 用户隐私协议相关 PO+文
Menglin 
档链接补充描述 
 
功 能 列表 
Fuli CEA 功能描
L0 L1 L2 L3 FO Priority IPD 
ID 
述
后台大数据 后台大数据
车辆数据 大数据分
分析数据采 分析数据采
联网
采集和上 析数据采
集和上传 集和上传
服务 
传 集和上传
Liu, 
Collection Collection 
New P0 IPD5.0 
Collection Collection 
Ya 
and upload of and upload of 
IOV 
and upload and upload 
background background 
service of vehicle of vehicle 
big data big data 
data data 
analysis analysis 
1 引言 
1.1 文 档目 的（Functional Objective ） 
本文范用于定义 CMP21D  MEB31 平台下整车数据采集与上传的统一功能标准，通过明确
定义各功能的激活条件、运行机制、异常处理与配置接口，作为功能开发实现及整车测试
的依据与输入。 
 
1.2 使 用范 围 
本功能定义适用于 CMP21D 平台下所有车型的整车级数据采集、上传、异常报警与云端
配置的相关功能。 
 
1.3 相 关法 律法规 
功能设计需满足并严格遵循国家关于车联网、隐私保护、车辆数据管理等相关法律法规，
以及 SOP 前后实施的国家与行业标准。 
 
1.4 名 词解 释与缩 写 
缩写 含义 
TBox Telematics Box 远程通信盒子 
VDU Vehicle Data Upload 整 车数据上传 
CDCU 中央域控制器
NGX 新一代网关模块 
SOP Start of Production 
CAN/LIN 控制器局域网络 / 本地互联网络 
MQTT 一种轻量级消息传输协议 
 
2 业 务 背 景与 目 标 
2.1 背 景说 明 
随着智能汽车向软件定义汽车演进，整车数据的采集、上传、处理与合规管理成为基础能
力之一。该功能模块旨在打通端-边-云全链路 ，实现高频率、高可靠性、高可控性的数据
上报能力。 
 
2.2 产 品定 位与价 值 
• 构建高可用的整车级数据采集与上报体系 
• 支持秒级数据处理与上传，支撑云端多维度运营策略，后续车型可根据需要升级架
构与硬件并提高数据上传能力至毫秒级 
• 提升整车调试、运维与售后诊断效率 
 
2.3 差 异化 亮点 
1. 全量数据采集：支持 CAN/LIN/SomeIP 以太网等全协议打包，覆盖各类整车信号； 
2. 端侧主动上传机制：支持毫秒级故障识别与前后追踪式数据保存； 
3. 边云联动配置机制：通过 CEA 平台远程下发配置、实时调整上传逻辑； 
4. 支持 U 盘录制：便于工程调试、离线分析、售后故障辅助定位。 
 
3 功能概述 
3.1 系 统架 构图
（ CDCU_SOC :  指车机端大屏 ; MCU ≈ CDCU ） 
 
3.2 功 能模 块拆解 
模 块名 称 简 要描 述 
车端数据采集 域控制器采集并打包以太网数据上传至 TBox 
TBox 数据处理上传 处理周期数据/ 故障上传/ 缓存与补发机制 
云端管理平台 配置数据上传策略、接收与存储车端数据 
主动触发采集 基于高优先级告警事件的毫秒级前后追踪上传 
U 盘录制功能 开启录制模式后写入数据至 U 盘用于 PC 端解析 
用户隐私控制 用户同意后开启数据采集，支持分模块授权 
 
4 功 能 需 求详 情 
4.1 车 内数 据采集 
基本流程：
• 域控制器作为 TCP 客户端连接 TBox ； 
• 数据缓存在域控内，优先保留最早产生的数据； 
• 定时（1 秒）或缓存满时触发打包上传； 
• 睡眠状态断开连接，状态置为 0。 
特殊场景： 
• 下电：收集锁车前后的完整数据；( 具体可收集下电前所有数据 ，下电后无法上传
数据) 
• 售前：预留预装车数据； 
• 售后：平台可调阅车端记录信息。 
 
4.2 数 据打 包与上 传 
关键逻辑： 
• TBox 缓存数据，1 秒内最新数据打包； 
• 支持 MQT T 通信协议 + HTTP 补发机制； 
• 本地缓存最多 7 天，断网自动补发。 
 
4.3 云 端数 据管理 平台 
功能范围： 
• 云端接收车端数据，存储、转发； 
• 支持通过 One Backend 为特定车辆 /VIN 分发 采集配置； 
• 每 10 秒上传一次（ 后台 可设 置上传 频率 ：5s/10s 可选 ）； 
 
4.4 U 盘 数 据采 集 
触发方式：插入 U 盘 → CDCU 进入调试模式 → UI 开启录制 → 通过 TBox 采集并写入 U
盘 
支持信号：DCAN/BCAN/ECAN/ICAN/ 以太网 SOMEIP 等全量毫秒级 数据 
数据结构：复用 CAN/CANFD/SOMEIP/LIN 等协议标准格式
4.5 主 动触 发上传 机制 
触发条件： 
• 高等级故障、底盘/ 自动驾驶/ 电池告警等； 
• 最小保存：前 10 秒、后 5 秒； 
 
4.6 车 辆日 志提取 ： 
支持通过大屏日志的接口调取车辆日志信息，具体日志内容由各业务或功能进行定义。 
 
4.7 权 限与 隐私控 制 
• 云端支持 VIN 维度 权 限下发； 
• 售前数据采集不依赖用户授权。 
 
4.7.1 功 能概 述 
本模块负责车 辆售 出 后，确保整车数据（包括 CAN 数据、GPS 数据和 RTM 数据）的上
报符合隐私保护法规要求，同时满足车辆监控和服务的业务需求。 
4.7.2 数 据分 类 
数 据包 数 据类 型 采 集内 容 控 制机 制 
车辆总线数据 手机隐私协议控制（和绑车强关联）
CAN 数据 
等 CAN 数据上报 
VDU 数
据包 
手机端隐私协议+车机端隐私协议（绑
GPS 数据 经纬度 
车状态+GPS 权限）控制上报 
RTM 数 RTM 数据(含 电池状态、告
强制采集及上报，不受用户控制 
据包 GPS 数据) 警数据等 
4.7.3 详 细需 求（ 注 ：用 户隐 私协议 弹窗 逻辑及 交互 以用户 隐私 协议 PRD 为 主 ，本章 节不
做 阐述 。待用 户隐 私协议 PO Junxiang Zhang 更 新后 在此处 补充 文档链 接 ）
4.7.3.1. 绑 车与 手机端隐 私协 议联动 
1.1 用户操作绑车，需弹出手机端隐私协议（不可跳过）： 
• 用 户同 意协议 ：可继续完成绑车流程，当完成绑车流程，则上报 CAN 数据； 
• 用 户拒 绝协议 ：无法继续绑车流程，关闭弹窗并退回到绑车初始页，显示 Toast ："
需同意协议才能完成车辆绑定"(仅供参考)，禁 止上传 CAN 数据； 
1.2 解绑处理机制 
• 用 户解 绑车辆 ： 立即停止所有 CAN 数据上传。 
1.3 重新绑定要求： 
• 需重新同意《手机端隐私协议》，绑车成功后，启动 CAN 数据上传； 
4.7.3.2. GPS 数 据授权管 理 
GPS 数据授权开关请参照用户隐私协议文档，但 T-BOX 需动态调整 上报策略 
GPS 开关 车 辆绑 定
数 据上 报行为 
状态 状态 
上报 CAN+GPS 数
开启 已绑定 
据 
禁止 CAN+GPS 数
开启 未绑定 
据上报 
关闭 已绑定 仅上报 CAN 数据 
禁止 CAN+GPS 数
关闭 未绑定 
据上报 
 
时序图：
4.7.4 日 志记 录 
• 记录所有开关操作（时间、设备、操作人、操作类型），至少保留 6 个月； 
操 作时 间 操 作设 备 操 作人 操 作类 型 
XXX 
精确到毫秒 设备 ID 同意车端隐私协议 
XXX 
精确到毫秒 设备 ID 拒绝手机端隐私协议 
XXX 
精确到毫秒 设备 ID 授权位置 
XXX 
精确到毫秒 设备 ID 授权位置关闭
• 日志记录存储位置：本地+云端 
 
 
5 系 统 依 赖说 明 
参考
依 赖项 内 容描 述 
章节 
用户隐私协议 数据采集管理，交互逻辑，状态同步等 4.7 
按照用户隐私协议统一位置要求，在用户界面设置“位置权限”开
HMI 4.7 
关，用于用户自行控制是否允许收集位置权限 
HMI 及用户
用户隐私协议文言 4.7 
隐私协议 
 
6  安 全 合 规要 求 
• 数据上传不得影响驾驶安全； 
• 故障上传需提供事故分析数据依据； 
• 国家监管可调阅授权数据； 
 
7  业务流程 
车端上传流程： 
1. 车辆上电 → 域控制器启动采集 → 建立 TCP 连接； 
2. 数据上传到 TBox 缓存 → 周期上传或异常上传； 
3. TBox 通过 MQTT 上传至云平台 → 云平台解析存储。 
主动故障上传流程： 
1. 系统检测到高优告警 → 触发缓存前后数据； 
2. 打包上传至平台 → 后台补发机制启用。
8 权 限 与 角色 设 计 
角色 权 限说 明 
车主 拥有数据采集授权开关控制权 
JV 后台 可下发特定车辆数据采集策略 
平台管理员 配置采集参数、故障场景上传规则

---

## PDF: VDU(C车动采)\CEA1.X\拓扑图\CEA1.0_Topo_V2.6_CS_20250527.pdf

CEA1.0  NETWORK  TOPOLOGY
Update History Management/ 更改历史管理
  V    1     .    1     _ CN
Reversion Date Author Reviewed by Update Comments
版本 日期 作者 审核 更新说明
Zhao Lin
V2.6_CS 2025-05-27 V2.6 Version for SVW.
Liu Ya
Network Channel Information
Acronyms Full Name Chinese Name Channel Attribute Note
缩写 全称 中文名 网段属性 备注
BCAN Body CAN 车身CAN CAN (500Kbps)
BLCAN Bluetooth Low Energy CAN 蓝牙CAN CANFD (500Kbps/2Mbps)
CCAN Chassis CAN 底盘CAN CANFD (500Kbps/2Mbps)
DCAN Diagnosis CAN 诊断CAN CAN (500Kbps)
ECAN ELectrical Propulsion CAN 三电CAN CANFD (500Kbps/2Mbps)
ICAN In-Vehicle Infotainment CAN 车载信息CAN CANFD (500Kbps/2Mbps)
LPCAN Lamp (External) CAN 外灯CAN CANFD (500Kbps/2Mbps)
SCAN1 Smart CAN 1 智能CAN CANFD (500Kbps/2Mbps)
TPCAN TBOX Private CAN TBOX 私有CAN CANFD (500Kbps/2Mbps)
CLIN CDCU LIN 中央域控制器LIN LIN (19.2Kbps)
LLIN LDCU LIN 左域控制器LIN LIN (19.2Kbps)
RLIN RDCU LIN 右域控制器LIN LIN (19.2Kbps)
DEth Diagnosis Ethernet 诊断以太网 Ethernet (100Base-Tx)
LEth LDCU-CDCU Ethernet LDCU-CDCU 以太网 Ethernet (100Base-T1)
REth RDCU-CDCU Ethernet RDCU-CDCU 以太网 Ethernet (100Base-T1)
FLC-CDCU ：100Base-T1
XEth NGX/FLC-CDCU Ethernet NGX/FLC-CDCU 以太网 Ethernet (100/1000Base-T1)
NGX-CDCU ：1000Base-T1
TEth TBOX-CDCU Ethernet TBOX-CDCU 以太网 Ethernet (1000Base-T1)
CAN Node List
Acronyms Full Name Chinese Name Battery Supply Network Management Note
缩写 全称 中文名 配电方式 网络管理 备注
Domain Control Unit
ICAN: Autosar NM
BCAN: Autosar NM
CDCU Centre Domain Control Unit 中央域控制器 KL30
TPCAN: Autosar NM
wakeup line: LDCU BU
ICAN: Autosar NM
ECAN: Autosar NM
LDCU Left Domain Control Unit 左域控制器 KL30
BLCAN: Autosar NM
wakeup line: RDCU BU
ICAN: Autosar NM
RDCU Right Domain Control Unit 右域控制器 KL30
wakeup line: LDCU BU
TPCAN: Autosar NM 
TBOX-5G Telematics Box - 5G 5G Tbox 模块 KL30 BLCAN: Autosar NM
wakeup line: LDCU BU
Chassis System ECU
MSBD Motor Seat Belt Driver 主驾安全带电机 KL30 简单NM
MSBP Motor Seat Belt Passenger 副驾安全带电机 KL30 简单NM
SRS Supplemental Restraint System 安全气囊控制器 KL15: RDCU (Switch power supply) 间接NM: RDCU 控制
IBRS One-Box (Integrated Power Brake) 智能集成制动系统 KL30 间接NM; wakeup line: RDCU
EPS Electronic Power Steering 电动助力转向 KL30 间接NM; wakeup line: RDCU
DCC Dynamic Chassis Control 底盘减震器 KL30 间接NM; wakeup line: LDCU
E-Drive System ECU
BMCe Battery Management 电池管理 KL30 ECAN: Autosar NM; wakeup line: LDCU
On Board Charger, 车载充电机
OCDC KL30 ECAN: Autosar NM; wakeup line: LDCU
Direct Current / Direct Current  Converter 直流/ 直流转换器
F_Inverter Front E-Drive 前电机控制单元 KL30 间接NM; wakeup line: LDCU
R_Inverter Rear E-Drive 后电机控制单元 KL30 间接NM; wakeup line: LDCU
ADAS System ECU
NGX Advanced driver assistance systems 自动驾驶控制器 KL30 间接NM; wakeup line ：RDCU
MRR Front Radar 前毫米波雷达模块 KL30 间接NM; wakeup line ：RDCU
FLC
Front Long range camera controller 前视一体机 KL30 间接NM; wakeup line ：RDCU
Body System ECU
CWCD_NFC Charging Wireless Control Driver Plus NFC 无线充电模块_ 主驾带NFC KL30 简单NM & 间接NM; wakeup line: RDCU
NFC Near Field Communication Module NFC 模块 KL30 BLCAN: autosar NM
BLE （UWB ） Blue-Tooth Low Energy 低功耗蓝牙主模块 KL30 BLCAN: autosar NM
BLCU Backup Unlock Control Unit 备份门锁控制单元 KL30 简单NM
BLE_FL / FR / RR / RL (UWB) BLE_FrontL / FrontR / RearR / RearL 低功耗蓝牙天线_ 左前/ 右前/ 右后/ 左后 KL15: BLE (Switch power supply) 间接NM: BLE 控制
AMP Amplifier 音响功放 KL30 间接NM; wakeup line ：RDCU
SMLS Steering Wheel Switch 组合开关 KL30 间接NM; wakeup line ：LDCU
SMLS (AGT) Steering Wheel Switch 组合开关 KL30 BCAN: Autosar NM
HUD HeadupDisplay 抬头显示器 KL30 间接NM; wakeup line ：RDCU
FID Fahrerinformations Diaplay 仪表 KL30 间接NM; wakeup line ：CDCU
FSL Front Signal Light 前灯语模块 KL30 间接NM; wakeup line ：RDCU
RSL Rear Signal Light 后灯语模块 KL30 间接NM; wakeup line ：RDCU
LHCM Headlamp Led Left 左大灯控制模块 KL30 间接NM; wakeup line ：RDCU
RHCM Headlamp Led Right 右大灯控制模块 KL30 间接NM; wakeup line ：RDCU
DSL Dashboard Smart Light 仪表台智能交互内饰灯带 KL30 间接NM; wakeup line ：RDCU
LIN Node List
Acronyms Full Name Chinese Name Battery Supply Network Management Note
缩写 全称 中文名 配电方式 网络管理 备注
ADAS System
USS FSL/R Ultrasonic Sensor System Front Side Left/Right 左右侧面前超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
USS RSL/R Ultrasonic Sensor System Rear Side Left/Right 左右侧面后超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
USS FOL/R Ultrasonic Sensor System Front Outboard Left/Right 左右外侧前超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
USS ROL/R Ultrasonic Sensor System Rear Outboard Left/Right 左右外侧后超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
USS FCL/R Ultrasonic Sensor System Front Center Left/Right 中央左右前超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
USS RCL/R Ultrasonic Sensor System Rear Center Left/Right 中央左右后超声波雷达 KL15: RDCU (Switch power supply) DSI: 间接NM (Slave)
Body System
WWM Windshield Wiper Motor 电子雨刮 KL30 RLIN3: LIN NM
SPR re. Passenger Seat Massage Module 副驾按摩模块 KL30 RLIN4: LIN NM
SPR li. Driver Seat Massage Module 主驾按摩模块 KL30 LLIN1: LIN NM
LLR_LL Seat Ventilation Left Backrest 主驾座椅靠背通风 KL30 LLIN1: LIN NM
LLR_LS Seat Ventilation Left Cushion 主驾座椅坐垫通风 KL30 LLIN1: LIN NM
LLR_RL Seat Ventilation Right Backrest 副驾座椅靠背通风 KL30 RLIN4: LIN NM
LLR_RS Seat Ventilation Right Cushion 副驾座椅坐垫通风 KL30 RLIN4: LIN NM
LinDA Head Console 前顶灯控制模块 KL30 LLIN5: LIN NM
LISI/LTM Light Switch 大灯开关 KL30 RLIN3: LIN NM 
RF Radio Frequency 射频模块 KL30 LLIN4: LIN NM
FKS Foot Kick Sensor 脚踢传感器 KL30 LLIN5: LIN NM
ATL_1-19 Atmosphere LIghting 1-19 氛围灯模块 KL15: RDCU&LDCU (Switch power supply) CLIN2/3: 间接NM (Slave)
KLR Capacitive Steering Wheel 电容方向盘HOD ( 离手检测) KL30 CLIN5: LIN NM
MFL Multi-Funtion Steering Wheel 方向盘开关 KL30 CLIN5: LIN NM
TBF_FS Driver Side Door Control Panel 主驾车窗/ 后视镜控制模块 KL30 CLIN1: LIN NM
GBM Glove Box Motor 手套箱电机模块 KL30 RLIN3: LIN NM
E-Drive System
EBS Electronic Battery Sensor 蓄电池传感器 KL30 LLIN2: LIN NM
AGS Active Grille Shutter 主动进气格栅 KL30 LLIN2: LIN NM
Thermal management System
RLFS Rain Light Humidity Sun Sensor 雨量光照传感器 KL30 RLIN3: LIN NM
FRS Fragrance System 智能香氛系统 KL15: RDCU (Switch power supply) CLIN4: 间接NM; wakeup: relay enable from RDCU
EKK Air Conditioning Compressor 空调压缩机 RLIN1: 间接NM; wakeup: relay enable from RDCU
KL15 (Switch power supply)
BLDC Brushless DC motor 无刷鼓风机 KL30 RLIN1: LIN NM
HV_H6 High Voltage Water Heater 高压水加热器PTC KL15 (Switch power supply) RLIN5: 间接NM; wakeup: relay enable from RDCU
PT1/2 Pressure and Temperature Sensor R134a 热泵压力温度传感器*2 KL15 (Switch power supply) RLIN1: 间接NM; wakeup: relay enable from RDCU
PS Pressure Sensor 压力传感器 KL15 (Switch power supply) RLIN1: 间接NM; wakeup: relay enable from RDCU
AC_EXV Expansion Valve1 R134a 热泵膨胀阀 KL15 (Switch power supply) RLIN4: 间接NM; wakeup: relay enable from RDCU
Bat_EXV Expansion Valve2 电池冷却膨胀阀 KL15 (Switch power supply) RLIN4: 间接NM; wakeup: relay enable from RDCU
PV1/2 Proportional Valve 1/2 四通阀1 、2 KL15 (Switch power supply) RLIN4: 间接NM; wakeup: relay enable from RDCU
ASV 1-3 Shutt Off Valve 1-3 热泵ASV1-3 KL15 (Switch power supply) RLIN5: 间接NM; wakeup: relay enable from RDCU
Blower Blower 有刷鼓风机调速模块 KL30 RLIN5: LIN NM
UIF Cabin Temperature Sensor 车内温度传感器 KL30 RLIN5: LIN NM
PMS PM2.5 Sensor PM2.5 KL15 (Switch power supply) RLIN5: 间接NM; wakeup: relay enable from RDCU
AQS Air Quality Sensor AQS 空气质量传感器 KL15 (Switch power supply) RLIN5: 间接NM; wakeup: relay enable from RDCU
CMP21_VW316/9_CS _B A SUV EntryLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
GBM WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
BLCU
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH2
CH1
ASIC1
BCAN
CLIN1
REth
CLIN2
Slave
ATL_10 ... ATL_1
CDCU_SOC
CLIN3
(MTK8676)
XEth XEth FLC
ATL_19 ... ATL_11
Slave Master
CLIN4
DEth
CDCU_MCU
Auto
DCAN
CLIN5
CCAN ICAN
MFL
LPCAN
CDCU    
LHCM RHCM
ICAN
Topview Camera front
Topview Camera rear
FID
Topview Camera left side
Topview Camera right side
LEth
Slave
ABT
BLCAN ECAN CCAN
CWCD_NFC BMCe IBRS
NFC EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
CAN (500K) 120Ω (Terminal resistor)
LLIN2
CANFD (2M)
Camera
AGS EBS
LIN (19.2K)
LLIN3
MAXIM
LDCU
Ethernet (100Base-T1)
Ethernet (100Base-Tx)
Defaut VLAN
LLIN4
Ethernet (1000Base-T1)
VLAN1
RF
LVDS
LLIN5
MM Component (COP MM Design)
ICAN
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
PCIe/SGMII
Switch
OBD
CMP21_VW316/9_CS_B A SUV VolumeLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
GBM WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
MSBD
BLCU
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1
CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
DMS camera
SCAN1 MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
ATL_10 ... ATL_1
CDCU_SOC
CLIN3 Front wide camera
(MTK8676)
XEth XEth
ATL_19 ... ATL_11 Rear facing camera
Slave Master
CLIN4
DEth
CDCU_MCU
Topview Camera front
Auto
DCAN
CLIN5 Topview Camera rear
KLR MFL Topview Camera left side
NGX
LPCAN
Topview Camera right side
CDCU    
FSL RSL LHCM RHCM
ICAN
FID
Front tele Camera
HUD Side Camera Front Left
LEth
Side Camera Front Right
Slave
ABT
Side Camera Rear Left
Side Camera Rear Right
BLCAN ECAN CCAN
CCAN ICAN
CWCD_NFC BMCe IBRS
NFC EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
CAN (500K) 120Ω (Terminal resistor)
LLIN2
CANFD (2M)
Camera
AGS EBS
LIN (19.2K)
LLIN3
MAXIM
LDCU
Ethernet (100Base-T1)
Ethernet (100Base-Tx)
Defaut VLAN
LLIN4
Ethernet (1000Base-T1)
VLAN1
RF
LVDS
LLIN5
MM Component (COP MM Design)
ICAN
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
PCIe/SGMII
Switch
OBD

---

## PDF: VDU(C车动采)\CEA1.X\拓扑图\CEA_Topo_V2.5_20241213.pdf

CEA  NETWORK  TOPOLOGY
Update History Management/ 更改历史管理
Reversion Date Author Reviewed by Update Comments
版本 日期 作者 审核 更新说明
 1 、Change the FrontRadar name to MRR; 
 2 、Change the switch of NGX to PHY;
V1.0 2024-04-30 ZhiqiangWang
 3 、Change the NGX attached camera name ;
 4 、CMP21D-EntryLine ：change the CDCU attached camera name  from rear camera to Rear TV Camera.
1 、CMP21D-VolumeLine-AGT ：MFL and KLR move to CLIN4 from CLIN5 ；
2 、CMP21D-VolumeLine/CMP 21D-EntryLine/MEB31PA : use MTK8676 with 5G TBOX as CDCU SOC, cancel TBOX ECU ；delete TPCAN;
3 、add Charger  to connect OCDC through CAN2.0B(250kbit/s);
4 、MEB31PA ：ECAN delete EOP ；change Inverter name to R-Inverter, addF-Inverter 。
5 、MEB31PA ：LISI/LTM is packaged;
6 、MEB31PA ：change FRS to optional;
7 、MEB31PA ：delete LSU in LLIN1; Add LLR_LS in LLIN1; Add LLR_RS  in RLIN4;
8 、MEB31PA ：elete  CornerRadar_FL/CornerRadar_FR/CornerRadar_RL/CornerRadar_RR;
9 、MEB31PA ：ePGD is packaged;
V1.1 2024-05-30 ZhiqiangWang 10 、MEB31PA: DCC is optional packaged ，change color to green;
11 、MEB21D-VolumeLine/VolumeLine-AGT/CMP 21D-EntryLine: change Inverter name to F-Inverter;
12 、CMP21D-VolumeLine/CMP 21D-EntryLine/MEB31PA ：add FID conne/ct to ICAN;
13 、MEB31PA: change AWV1/2 name to  BCMV1/2; delete Mot_PUMP and  Bat_PUMP; RLIN2: Delete AGS, add ROLLO;
14 、add MEB 31 Project; add DS and HV_AirPTC.
15 、delete IBCAN of CDCU;
16 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine/MEB31PA:
change  AC_EXV2 name to Bat_EXV ; change AC_EXV1 name to AC_EXV; change RLS to RLFS;
17 、CMP21D-VolumeLine/CMP 21D-EntryLine/MEB31PA: CWCD_NFC clolor from Green to Yellow, delete RDCU wakeup line;
18 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine/MEB31PA: change ASV1/2/3 from RLIN4 to RLIN5;
1 、MEB31: use MTK8676 with 5G TBOX as CDCU SOC, cancel TBOX ECU ；delete TPCAN;
V2.0 2024-05-31 ZhiqiangWang
2 、MEB31: add AMP to connect CDCU through A2B ;
1 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine/MEB31PA/MEB31: change AC_EXV and Bat_EXV from RLIN1 to RLIN4 ;
V2.1 2024-06-03 ZhiqiangWang 2 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine/MEB31PA: change HV_H  from RLIN1 to RLIN5 ;
3 、MEB31PA: change ION  from RLIN1 to RLIN5 ;
1 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/MEB31PA/MEB31: NGX delete SCAN2/SCAN3/SCAN4/SCAN5;
2 、MEB31PA: BCAN add CAN node  AMP , folllow MEB31;
3 、add MEB31 AGT ；
V2.2 2024-06-21 ZhiqiangWang 4 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine: change RLIN5 Blower Battery Supply from KL15 to KL30 ；
5 、MEB31PA/MEB31 ：change F-Inverter/R-Inverter  color from red to yellow;
6 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/MEB31PA/MEB31: change NGX Diagnostic Interface  from XEth ：DoIP to  ICAN: DoCANFD;
7 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/MEB31PA/MEB31: EBS Diagnostic Interface change to Not Support ；change name of Charger to EVSE;
1 、MEB31-AGT:  CLIN4 delete FRS; move MFL and  KLR  from CLIN5 to CLIN4;
2 、MEB31PA/MEB31/MEB31-AGT:change RLIN1 BLDC Battery Supply from KL15 to KL30 ；
3 、LIN-ECU List ：update the Thermal management System ECU Full name; MEB31/MEB31-AGT: change HV_AirPTC to HV_H3; change DS to PS;
CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/CMP 21D-EntryLine/MEB31PA:change BCMV1 to PV1, change BCMV2 to PV2. change HV_H to HV_H6;
4 、MEB31PA/MEB31 ：change FKS color from green to yellow ；
5 、CMP21D-VolumeLine/CMP 21D-EntryLine/MEB31PA/MEB31: change SRS color from green to red ；
6 、CMP21D-VolumeLine/CMP 21D-EntryLine ：LLIN5 delete LinDA;
V2.3 2024-07-26 ZhiqiangWang
7 、CMP21D-VolumeLine/CMP 21D-EntryLine/MEB31PA/MEB31: change CWCD_NFC color from yellow to green ；
8 、CMP 21D-EntryLine （need final decision ）：change USS  interface from CLIN1 to DSI3 ,change color to red; delete Rear TV Camera connect to CDCU,
add  Topview Camera front/Topview Camera rear/ Topview Camera left side/Topview Camera right side  to connect CDCU;add FLC connect to ICAN/CCAN/ETH;
9 、MEB31PA/MEB31 :change   IDLight name to DSL; 
10 、CMP21D-VolumeLine/CMP21D-VolumeLine-AGT/MEB31PA/MEB31/MEB31-AGT: 12*USS connect to NGX  changed; 
11 、MEB31PA/MEB31/MEB31-AGT: change DCC color from green to red;
12 、change Project CMP21D  to CMP21;
Reversion Date Author Reviewed by Update Comments
版本 日期 作者 审核 更新说明
V2.4 2024-08-14 Liu Ya Add new project VW311/OCM_B A NB in MEB31
1 、Delete project MEB31_VW311, MEB31PA and MEB31PA-AGT;
2 、Change the page name of “CAN 网段信息” to “ 网络通道信息”:
change the table name from "CAN network information" to "Network Channel Information"; change information of  LPCAN; 
add information of CLIN/LLIN/RLIN and DEth/LEth/REth/XEth;delete the information of IBCAN and PCAN;
change Diagnostic Interface of BLE(UWB) to BLACAN from TPCAN; delete TPCAN Diagnostic Interface of CWCD_NFC; 
3 、Delete EVSE from this topology for all projects;
4 、Adjust some details of CAN-ECU List and LIN-ECU List;
5 、CMP21-VolumeLine: delete MSBP of BCAN;
delete MAXIM Interface: Interior cabin camera (Reserved);
6 、MEB31-VW313: delete CMCP of BCAN
Zhao Lin 7 、MEB31-VW313/MEB31-VW316, CMP21-VolumeLine/CMP21-EntryLine: change terminal resistor of LPCAN from CDCU to RHCM;
V2.5 2024-12-13
Liu Ya 8 、MEB31-VW313/MEB31-VW316: change CLIN4 FRS Battery Supply from KL30 to KL15, change the Network Management from LIN NM to 间接NM (wakeup: relay
enable from RDCU);
9 、MEB31-VW313/MEB31-VW316, CMP21-VolumeLine/CMP21-EntryLine: change FID Diagnostic Interface to LVDS interface from ICAN: DoCANFD;
10 、CMP21-EntryLine/VloumeLine and AGT CMP21 VolumeLine: change the color of line that CDCU_SOC and CDCU_MCU linked to Switch.
11 、CMP21-EntryLine/VloumeLine: change the color of EKK/HV_6/PT1/PT2/Bat_EXV/AC_EXV/ASV1/ASV2/ASV3/PV1/PV2/MFL from blue to red; 
change the color of EBS/CWCD_NFC/NFC/BLE/BLE_FL(UWB)/BLE_FR(UWB)/BLE_RL(UWB)/BLE_RR(UWB) from green to red;
add RF to LLIN4;
delete FRS of CLIN4, delete CMCe;
12 、CMP21-VloumeLine: change the color of KLR from blue to red; 
13 、MEB31 and CMP21: change the Acronyms/Full Name/Chinese Name of AR-HUD to HUD/HeadupDisplay/ 抬头显示器.
14 、Add new project AGT(IS34)  Based CMP21-VloumeLine, CMP21-EntryLine and VFF MEB31.
AGT CMP21-VolumeLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
LISI/LTM WWM RLFS
RLIN4
PV2 PV1 AC_EXV Bat_EXV
REth
CCAN
RLIN5
Master BCAN
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
SMLS
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1
CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
TBF_FS SCAN1 MRR
PPS
REth
CLIN2
Slave
CLIN3 CDCU_SOC Front wide camera
XEth XEth
Rear facing camera
Slave Master
CLIN4
DEth
CDCU_MCU
KLR MFL Topview Camera front
Auto
DCAN
CLIN5 Topview Camera rear
Topview Camera left side
NGX
Topview Camera right side
CDCU    
ICAN DMS camera
FID
TEth
Slave
LEth
Slave
ABT
TPCAN ECAN CCAN
CCAN ICAN
TEth
Master
BMCe IBRS
TBOX-5G
EPS
cv
BLCAN
BLE_FL(UWB)
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLIN2
AGS EBS
CAN (500K) 120Ω (Terminal resistor)
LLIN3
LDCU
CANFD (2M)
Camera
LIN (19.2K)
LLIN4
MAXIM
Ethernet (100Base-T1)
Ethernet (100Base-Tx)
Defaut VLAN
LLIN5
ICAN
Ethernet (1000Base-T1)
VLAN1
LinDA
LVDS
MM Component (COP MM Design)
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
Switch
OBD
AGT(IS34) CMP21-EntryLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
USS ROL USS FOR
USS RCL USS FCR
USS RCR USS FCL
USS ROR USS FOL
CH2
CH1
BCAN
CLIN1 ASIC
TBF_FS
REth
CLIN2
Slave
CDCU_SOC
CLIN3
(MTK8676)
XEth XEth FLC
Slave Master
CLIN4
DEth
CDCU_MCU
Auto
DCAN
CLIN5
CCAN ICAN
MFL
LPCAN
CDCU    
ICAN
Topview Camera front
Topview Camera rear
FID
Topview Camera left side
Topview Camera right side
LEth
Slave
ABT
BLCAN ECAN CCAN
BMCe IBRS
EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
LLIN2
AGS EBS
CAN (500K) 120Ω (Terminal resistor)
LLIN3
LDCU
CANFD (2M)
Camera
LIN (19.2K)
LLIN4
MAXIM
Ethernet (100Base-T1)
RF
Ethernet (100Base-Tx)
Defaut VLAN
LLIN5
ICAN
Ethernet (1000Base-T1)
VLAN1
LinDA
LVDS
MM Component (COP MM Design)
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
Switch
OBD
AGT(IS34) CMP21-VolumeLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
MSBD
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1
CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
TBF_FS SCAN1 MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
CDCU_SOC
CLIN3 Front wide camera
(MTK8676)
XEth XEth
Rear facing camera
Slave Master
CLIN4
DEth
CDCU_MCU
Topview Camera front
Auto
DCAN
CLIN5 Topview Camera rear
MFL Topview Camera left side
NGX
LPCAN
Topview Camera right side
CDCU    
ICAN DMS camera
FID
HUD
LEth
Slave
ABT
BLCAN ECAN CCAN
CCAN ICAN
BMCe IBRS
EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
LLIN2
AGS EBS
CAN (500K) 120Ω (Terminal resistor)
LLIN3
LDCU
CANFD (2M)
Camera
LIN (19.2K)
LLIN4
MAXIM
Ethernet (100Base-T1)
RF
Ethernet (100Base-Tx)
Defaut VLAN
LLIN5
ICAN
Ethernet (1000Base-T1)
VLAN1
LinDA
LVDS
MM Component (COP MM Design)
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
Switch
OBD
CMP21-EntryLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
USS ROL USS FOR
USS RCL USS FCR
USS RCR USS FCL
USS ROR USS FOL
CH2
CH1
BCAN
CLIN1 ASIC
REth
CLIN2
Slave
ATL_10 ... ATL_1
CDCU_SOC
CLIN3
(MTK8676)
XEth XEth FLC
ATL_19 ... ATL_11
Slave Master
CLIN4
DEth
CDCU_MCU
Auto
DCAN
CLIN5
CCAN ICAN
MFL
LPCAN
CDCU    
LHCM RHCM
ICAN
Topview Camera front
Topview Camera rear
FID
Topview Camera left side
Topview Camera right side
LEth
Slave
ABT
BLCAN ECAN CCAN
CWCD_NFC BMCe IBRS
NFC EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
LLIN2
AGS EBS
CAN (500K) 120Ω (Terminal resistor)
LLIN3
LDCU
CANFD (2M)
Camera
LIN (19.2K)
LLIN4
MAXIM
Ethernet (100Base-T1)
RF
Ethernet (100Base-Tx)
Defaut VLAN
LLIN5
ICAN
Ethernet (1000Base-T1)
VLAN1
LVDS
MM Component (COP MM Design)
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
Switch
OBD
CMP21-VolumeLine
ICAN
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_EXV
REth
CCAN
RLIN5
BCAN
Master
HV_H6 Blower UIF
SRS
ASV3 ASV2 ASV1
Private CAN
MSBD
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1
CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
SCAN1 MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
ATL_10 ... ATL_1
CDCU_SOC
CLIN3 Front wide camera
(MTK8676)
XEth XEth
ATL_19 ... ATL_11 Rear facing camera
Slave Master
CLIN4
DEth
CDCU_MCU
Topview Camera front
Auto
DCAN
CLIN5 Topview Camera rear
KLR MFL Topview Camera left side
NGX
LPCAN
Topview Camera right side
CDCU    
FSL RSL LHCM RHCM
ICAN DMS camera
FID
HUD
LEth
Slave
ABT
BLCAN ECAN CCAN
CCAN ICAN
CWCD_NFC BMCe IBRS
NFC EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
 6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN
ECAN CCAN
LEth
LLIN1
Master
LLR_LL LLR_LS
LLIN2
AGS EBS
CAN (500K) 120Ω (Terminal resistor)
LLIN3
LDCU
CANFD (2M)
Camera
LIN (19.2K)
LLIN4
MAXIM
Ethernet (100Base-T1)
RF
Ethernet (100Base-Tx)
Defaut VLAN
LLIN5
ICAN
Ethernet (1000Base-T1)
VLAN1
LVDS
MM Component (COP MM Design)
IO harewire
DSI3 VW Component (New VW HW/SW)
A2B
VW Component (New VW SW)
optional VW Component (No VW Change)
Switch
OBD

---

## PDF: VDU(C车动采)\CEA1.X\拓扑图\CEA_Topo_V4.0_CS_20250807.pdf

CEA1.0 Network Topology
Version Management
InIn  cacasese  ofof  any many miissttakakeess  in topoin topollogyogy,,  pplsls. . ccontacontactt  LiuLiu, , Ya Ya (Le(Leo) o) (C|(C|GAGA--2) & 2) & PiPi, , HaiHaiyu (yu (VVCTCTCC--AA)AA)
For latFor latestest ver versionsion,,  ppllease cliease clickck  the the hyperhyperlinlink:k: ProjecProjecProjecttt Hou Hou House se se ---Topology Topology Topology ---   CEA CEA CEA 111              .x.x.x
Version nuVersion nummbbereriinng expg expllanatanatioionn:: Note
The version iteration upgrade rule applies to versions after V2.6.
V  1  .  1  _  CN
Joint venture code
Main version Sub version
Empty    Superset topology for all HUTs incl. VWA/FAW/SVW
Update main version when new vehicle 1. Update sub version when changes on the existing projects.
CN    topology collection for FAW HUTs 
model project is introduced. 2. When main version is updated, sub version is rolling from 0 again.
CS    topology collection for SVW HUTs
Version Release Date Author Update Comments
Please refer to the previous version for details
…. …. …..
V2.4 2024/8/14 Liu Ya Add new project VW311/OCM_B A NB in MEB31
1、Delete project MEB31_VW311, MEB31PA and MEB31PA-AGT;
2、Change the page name of “CAN 网段信息” to “ 网络通道信息”:change the table name from "CAN network information" to "Network Channel Information"; change information of LPCAN;add information of 
CLIN/LLIN/RLIN and DEth/LEth/REth/XEth;delete the information of IBCAN and PCAN;change Diagnostic Interface of BLE(UWB) to BLACAN from TPCAN; delete TPCAN Diagnostic Interface of CWCD_NFC;
3、Delete EVSE from this topology for all projects;
4、Adjust some details of CAN-ECU List and LIN-ECU List;
5、CMP21-VolumeLine: delete MSBP of BCAN;
delete MAXIM Interface: Interior cabin camera (Reserved);
6、MEB31-VW313: delete CMCP of BCAN
7、MEB31-VW313/MEB31-VW316, CMP21-VolumeLine/CMP21-EntryLine
Zhao Lin
V2.5 2024/12/13 : change terminal resistor of LPCAN from CDCU to RHCM;
Liu Ya
8、MEB31-VW313/MEB31-VW316: change CLIN4 FRS Battery Supply from KL30 to KL15,change the Network Management from LIN NM to 间接NM (wakeup: relayenable from RDCU);
9、MEB31-VW313/MEB31-VW316, CMP21-VolumeLine/CMP21-EntryLine: change FID Diagnostic Interface to LVDS interface from ICAN: DoCANFD;
10、CMP21-EntryLine/VloumeLine and AGT CMP21 VolumeLine: change the color of line that CDCU_SOC and CDCU_MCU linked to Switch.
11、CMP21-EntryLine/VloumeLine: change the color of EKK/HV6/PT1/PT2/Bat_EXV/AC_EXV/ASV1/ASV2/ASV3/PV1/PV2/MFL from blue to red;change the color of 
EBS/CWCD_NFC/NFC/BLE/BLE_FL(UWB)/BLE_FR(UWB)/BLE_RL(UWB)/BLE_RR(UWB) from green to red;
add RF to LLIN4;delete FRS of CLIN4, delete CMCe;
12、CMP21-VloumeLine: change the color of KLR from blue to red;
13、MEB31 and CMP21: change the Acronyms/Full Name/Chinese Name of AR-HUD to HUD/HeadupDisplay/ 抬头显示器.
14、Add new project AGT(IS34) Based CMP21-VloumeLine, CMP21-EntryLine and VFF MEB31.
1. Add legend of PCIe/SGMII.
2. Change ASV1-3 NM from "RLIN4: 间接NM" to "RLIN5: 间接NM".
3. Change Network Management of CWCD_NFC to " 简单NM & 间接NM; wakeup line: RDCU" from "简单NM“.
Zhao Lin 4.CMP21-EntryLine/VloumeLine: Add BLCU.
V2.6 2025/4/8
Liu Ya 5. Change USS quantity in CMP21-EntryLine;Replace
NGX with NGX Pro solution in CMP21-VolumeLine; DMS camera is transferred from NGX to CDCU in CMP21-VolumeLine , MEB-VW313 ,MEB-VW316
6. Delete ethernet interface between MRR and NGX
7. Add LIN node GBM to RLIN3
1. Add MEB31_VW316/6_CN_B1 ID4 PA project page.
2. Change name of page“CMP21_VW316/A SUV BEV-EntryLine” to "CMP21_VW316/9_CS _BA SUVe EntryLine""CMP21_VW316/A SUV BEV-VolumeLine" to "CMP21_VW316/9_CS _BA SUVe 
VolumeLine""MEB31_VW313/A COSe" to "MEB31_
Zhao Lin VW313/2_CM A COSe""MEB31_VW316/BL MY26" to "MEB31_VW316/8_CM A SUVe BL MY26"
V3.0 2025.05.30 Pi Haiyu 3.Update List Name of ECU List-CAN/LIN
Liu Ya 4.Update description of Network management Line Chinese to English in CAN/LIN ECU List
5.Add ETC description in CAN/LIN ECU List
6.Add ETC Node in CMP21-VW316-VolumeLine and CMP21-VW316-EntryLine
7.Delete GBM LIN Node in CMP21-VW316-VolumeLine and CMP21-VW316-EntryLine
1.Add CF LIN Node in ID4 PA ；
2.Change LVDS interface to GMSL ；
3.Add OMS to CDCU in CMP21-VolumeLine
4.Change TMS LIN nodes in ID4 PA which are same to CMP21 platform
5.Add FKS LIN node in CMP21_VW316/9_CS _B A SUVe VolumeLine
Pi Haiyu
V4.0 2025.08.05 6.Delete WWM LIN node in CMP21_VW316/9_CS _B A SUVe VolumeLine and EntryLine, ID4 PA
Liu Ya
7.Add Lidar for NGX PRO in ID4 PA VolumeLine
8.Add EntryLine with FLC configuration for ID4 PA
9.Add new hut CMP21_VW311/1_CN _B A NB VolumeLine&EntryLine
10.Add new hut CMP21 Export LHD A SUV VolumeLine&EntryLine
11. Add HCM in AGT(IS34) CMP21
CONFIDENTIAL CLASS: INTERNAL Page 2
Network Channel Information
Abbreviation Full Name Chinese Name Channel Attribute Note
BCAN Body CAN 车身CAN CAN(500Kbps)
BLCAN Bluetooth Low Energy CAN 蓝牙CAN CANFD(2Mbps)
CCAN Chassis CAN 底盘CAN CANFD (2Mbps)
DCAN Diagnosis CAN 诊断CAN CAN (500Kbps)
ECAN Electrical Propulsion CAN 三电CAN CANFD (2Mbps)
ICAN In-Vehicle Infotainment CAN 车载信息CAN CANFD (2Mbps)
LPCAN Lamp (External) CAN 外灯CAN CANFD (2Mbps)
SCAN1 Smart CAN 1 智能CAN CANFD (2Mbps)
TPCAN TBOX Private CAN TBOX 私有CAN CANFD (2Mbps)
CLIN CDCU LIN 中央域控制器LIN LIN (19.2Kbps)
LLIN LDCU LIN 左区域控制器LIN LIN (19.2Kbps)
RLIN RDCU LIN 右区域控制器LIN LIN (19.2Kbps)
DEth Diagnosis Ethernet 诊断以太网 Ethernet (100Base-Tx)
LEth LDCU-CDCU Ethernet LDCU-CDCU 以太网 Ethernet (100Base-T1)
REth RDCU-CDCU Ethernet RDCU-CDCU 以太网 Ethernet (100Base-T1)
FLC-CDCU ：100Base-T1
XEth NGX/FLC-CDCU Ethernet NGX/FLC-CDCU 以太网 Ethernet (100/1000Base-T1)
NGX-CDCU ：1000Base-T1
TEth TBOX-CDCU Ethernet TBOX-CDCU 以太网 Ethernet (1000Base-T1)
CONFIDENTIAL CLASS: INTERNAL Page 3
CAN Node List
Abbreviation Full Name Chineses Name Power Supply Network Management Note
Core Control Unit
ICAN: Autosar NM
BCAN: Autosar NM
CDCU Centre Domain Control Unit 中央域控制器 KL30 wakeup line: LDCU
TPCAN: Autosar NM
间接NM (hardwire wakeup)  
ICAN: Autosar NM
ECAN: Autosar NM
LDCU Left Domain Control Unit 左区域控制器 KL30 wakeup line: RDCU
BLCAN: Autosar NM
间接NM (hardwire wakeup)  
ICAN: Autosar NM
RDCU Right Domain Control Unit 右区域控制器 KL30 wakeup line: LDCU
间接NM (hardwire wakeup)  
TPCAN: Autosar NM
TBOX-5G Telematics Box - 5G 5G Tbox 模块 KL30 BLCAN: Autosar NM wakeup line: LDCU
间接NM (hardwire wakeup)  
ADAS System ECU
NGX Advanced driver assistance systems 自动驾驶控制器 KL30 间接NM (hardwire wakeup)  wakeup line: RDCU
MRR Front Radar 前毫米波雷达模块 KL30 间接NM (hardwire wakeup)  wakeup line: RDCU
FLC Front Long range camera controller 前视一体机 KL30 间接NM (hardwire wakeup)  wakeup line: RDCU
Body System ECU
CWCD_NFC Charging Wireless Control Driver Plus NFC 无线充电模块_主驾带NFC KL30 Simple NM & 间接NM(Hardwire wakeup) wakeup line: RDCU
NFC Near Field Communication Module NFC 模块 KL30 BLCAN: autosar NM
BLE （UWB） Blue-Tooth Low Energy 低功耗蓝牙主模块 KL30 BLCAN: autosar NM
BLCU Backup Unlock Control Unit 备份门锁控制单元 KL30 Simple NM
BLE_FL (UWB) BLE_Front Left 低功耗蓝牙天线_左前 Switch power supply: BLE(UWB) power start up / shut down powered by BLE(UWB)
BLE_FR (UWB) BLE_Front Right 低功耗蓝牙天线_右前 Switch power supply: BLE(UWB) power start up / shut down powered by BLE(UWB)
BLE_ RR  (UWB) BLE_Rear Right 低功耗蓝牙天线_右后 Switch power supply: BLE(UWB) power start up / shut down powered by BLE(UWB)
BLE_RL (UWB) BLE_RearLeft 低功耗蓝牙天线_左后 Switch power supply: BLE(UWB) power start up / shut down powered by BLE(UWB)
AMP Amplifier 音响功放 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
SMLS Steering Wheel Switch 组合开关 KL30 间接NM(Hardwire wakeup) wakeup line: LDCU
SMLS(AGT) Steering Wheel Switch 组合开关 KL30 BCAN: Autosar NM
HUD HeadupDisplay 抬头显示器 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
FID Fahrerinformations Display 仪表 KL30 间接NM(Hardwire wakeup) wakeup line: CDCU
FSL Front Signal Light 前灯语模块 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
RSL Rear Signal Light 后灯语模块 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
LHCM Headlamp Led Left 左大灯控制模块 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
RHCM Headlamp Led Right 右大灯控制模块 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
DSL Dashboard Smart Light 仪表台智能交互内饰灯带 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
ETC Electronic Toll Collection 电子不停车收费（电子收费） Switch power supply: LDCU power start up / shut down powered by LDCU
Chassis System ECU
MSBD Motor Seat Belt Driver 主驾安全带电机 KL30 Simple NM
MSBP Motor Seat Belt Passenger 副驾安全带电机 KL30 Simple NM
SRS Supplemental Restraint System 安全气囊控制器 Switch power supply: RDCU power start up / shut down powered by RDCU
IBRS One-Box (Integrated Power Brake) 智能集成制动系统 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
EPS Electronic Power Steering 电动助力转向 KL30 间接NM(Hardwire wakeup) wakeup line: RDCU
DCC Dynamic Chassis Control 底盘减震器 KL30 间接NM(Hardwire wakeup) wakeup line: LDCU
E-Drive System ECU
BMCe Battery Management 电池管理 KL30 ECAN: Autosar NM wakeup line: LDCU
OCDC On Board Charger,DC/DC Converter 车载充电机直流/ 直流转换器 KL30 ECAN: Autosar NM wakeup line: LDCU
F_Inverter Front E-Drive 前电机控制单元 KL30 间接NM(Hardwire wakeup) wakeup line: LDCU
R_Inverter Rear E-Drive 后电机控制单元 KL30 间接NM(Hardwire wakeup) wakeup line: LDCU
CONFIDENTIAL CLASS: INTERNAL Page 4
LIN Node List
Abbreviation Full Name Chineses Name Power Supply Network Management Note
ADAS System
USS_FCL Ultrasonic Sensor System Front Side Left/Right 左右侧面前超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_FCR Ultrasonic Sensor System Rear Side Left/Right 左右侧面后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_FOL Ultrasonic Sensor System Front Outboard Left/Right 左右外侧前超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_FOR Ultrasonic Sensor System Rear Outboard Left/Right 左右外侧后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_FSL Ultrasonic Sensor System Front Center Left/Right 中央左右前超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_FSR Ultrasonic Sensor System Rear Center Left/Right 中央左右后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_RCL Ultrasonic Sensor System Rear Center Left 中央左后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_RCR Ultrasonic Sensor System Rear Center Right 中央右后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_ROL Ultrasonic Sensor System Rear Outboard Left 左外侧后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_ROR Ultrasonic Sensor System Rear Outboard Right 右外侧后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_RSL Ultrasonic Sensor System Rear Side Left 左侧面后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
USS_RSR Ultrasonic Sensor System Rear Side Right 右侧面后超声波雷达 Switch power supply: RDCU DSI: 间接NM (hardwire wakeup)  (Slave)
Body System
WWM Windshield Wiper Motor 电子雨刮 KL30 RLIN3: LIN NM
SPR re. Passenger Seat Massage Module 副驾按摩模块 KL30 RLIN4: LIN NM
SPR li. Driver Seat Massage Module 主驾按摩模块 KL30 LLIN1: LIN NM
LLR_LL Seat Ventilation Left Backrest 主驾座椅靠背通风 KL30 LLIN1: LIN NM
LLR_LS Seat Ventilation Left Cushion 主驾座椅坐垫通风 KL30 LLIN1: LIN NM
LLR_RL Seat Ventilation Right Backrest 副驾座椅靠背通风 KL30 RLIN4: LIN NM
LLR_RS Seat Ventilation Right Cushion 副驾座椅坐垫通风 KL30 RLIN4: LIN NM
LinDA Head Console 前顶灯控制模块 KL30 LLIN5: LIN NM
LISI/LTM Light Switch 大灯开关 KL30 RLIN3: LIN NM
RF Radio Frequency 射频模块 KL30 LLIN4: LIN NM
FKS Foot Kick Sensor 脚踢传感器 KL30 LLIN5: LIN NM
ATL_1-19 Atmosphere Lighting 1-19 氛围灯模块 Switch power supply: RDCU&LDCU power start up / shut down controlled by LDCU and RDCU
KLR Capacitive Steering Wheel 电容方向盘HOD (离手检测) KL30 CLIN5: LIN NM
MFL Multi-Funtion Steering Wheel 方向盘开关 KL30 CLIN5: LIN NM
TBF_FS Driver Side Door Control Panel 主驾车窗/后视镜控制模块 KL30 CLIN1: LIN NM
CF Console Refrigerator 车载冰箱 KL30 LLIN1: LIN NM
E-Drive System
EBS Electronic Battery Sensor KL30 LLIN2: LIN NM
蓄电池传感器
AGS Active Grille Shutter 主动进气格栅 KL30 LLIN2: LIN NM
ROLLO Rollo Curtain KL30 LLIN2: LIN NM
进气卷帘
Thermal management System
RLFS Rain Light Humidity Sun Sensor 雨量光照传感器 KL30 RLIN3: LIN NM
FRS Fragrance System 智能香氛系统 Switch power supply: RDCU power start up / shut down controlled by RDCU
EKK Air Conditioning Compressor 空调压缩机 Switch power supply: Relay power start up / shut down relay enable from RDCU
BLDC Brushless DC motor 无刷鼓风机 KL30 RLIN1: LIN NM
HV_H2 High Voltage Battery Heater 高压水加热器PTC Switch power supply: Relay power start up / shut down relay enable from RDCU
HV_H3 High Voltage Air Heater 风暖PTC Switch power supply: Relay power start up / shut down relay enable from RDCU
HV_H6 High Voltage Water Heater 高压水加热器PTC Switch power supply: Relay power start up / shut down relay enable from RDCU
PT1 Pressure and Temperature Sensor R134a 热泵压力温度传感器1 Switch power supply: Relay power start up / shut down relay enable from RDCU
PT2 Pressure and Temperature Sensor R134a 热泵压力温度传感器2 Switch power supply: Relay power start up / shut down relay enable from RDCU
PS Pressure Sensor 压力传感器 Switch power supply: Relay power start up / shut down relay enable from RDCU
AC_EXV Expansion Valve1 R134a 热泵膨胀阀 Switch power supply: Relay power start up / shut down relay enable from RDCU
Bat_EXV Expansion Valve2 电池冷却膨胀阀 Switch power supply: Relay power start up / shut down relay enable from RDCU
PV1 Proportional Valve 1 四通阀1 Switch power supply: Relay power start up / shut down relay enable from RDCU
PV2 Proportional Valve 2 四通阀2 Switch power supply: Relay power start up / shut down relay enable from RDCU
ASV 1 Shutt Off Valve 1 热泵ASV1 Switch power supply: Relay power start up / shut down relay enable from RDCU
ASV 2 Shutt Off Valve 2 热泵ASV2 Switch power supply: Relay power start up / shut down relay enable from RDCU
ASV 3 Shutt Off Valve 3 热泵ASV3 Switch power supply: Relay power start up / shut down relay enable from RDCU
Blower Blower 有刷鼓风机调速模块 KL30 RLIN5: LIN NM
UIF Cabin Temperature Sensor 车内温度传感器 KL30 RLIN5: LIN NM
PMS PM2.5 Sensor PM2.5 Switch power supply: Relay power start up / shut down relay enable from RDCU
AQS Air Quality Sensor AQS空气质量传感器 Switch power supply: Relay power start up / shut down relay enable from RDCU
CONFIDENTIAL CLASS: INTERNAL Page 5
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal
CMP21_VW316/9_CS _B A SUVe EntryLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
Master BCAN
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
ETC
USS RSR USS RSL USS FSR USS FSL
BLCU
CH2 CH1
BCAN
ASIC1
CLIN1
REth
CLIN2
Slave
ATL_10 ... ATL-1
100base-T1
CDCU_SOC
CLIN3
FLC
XEth
XEth
Slave
Master
ATL_19 ... ATL-11
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN
CLIN5
CCAN ICAN
MFL
CDCU
LPCAN
LHCM RHCM
Topview Camera front
ICAN
Topview Camera Rear
FID
Topview Camera Left side
Topview Camera Right side
LEth
Slave
ABT
BLCAN ECAN CCAN
CWCD_NFC BMCe IBRS
NFC EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
CONFIDENTIAL CLASS: INTERNAL Page 6
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal
CMP21_VW316/9_CS_B A SUV VolumeLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
BCAN
Master
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
MSBD
USS RCR USS RCL USS FCR USS FCL
ETC
USS ROR USS ROL USS FOR USS FOL
BLCU
USS RSR USS RSL USS FSR USS FSL
CH1 CH2 CH2 CH1
BCAN
OMS camera
CLIN1 ASIC2 ASIC1
DMS camera
SCAN1
MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
ATL_10 ... ATL-1
1000base-T1
CDCU_SOC
CLIN3
XEth
XEth Front Wide Camera
Slave
Master
ATL_19 ... ATL-11
Rear facing camera
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN Topview Camera front
CLIN5
Topview Camera Rear
KLR MFL
CDCU NGX_PRO
Topview Camera Left side
LPCAN
Topview Camera Right side
LHCM RHCM
ICAN
FID
Front Tele Camera
HUD
LEth
Side Camera Front Left
Slave
ABT
Side Camera Front Right
Side Camera Rear Left
BLCAN Side Camera Rear Right
ECAN CCAN CCAN ICAN
CWCD_NFC BMCe IBRS
EPS
NFC
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
FKS
CONFIDENTIAL CLASS: INTERNAL Page 7
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal
CMP21_Export LHD A SUV EntryLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
Master BCAN
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
BLCU
CH2 CH1
BCAN
ASIC1
CLIN1
REth
CLIN2
Slave
ATL_10 ... ATL-1
100base-T1
CDCU_SOC
CLIN3
FLC
XEth
XEth
Slave
Master
ATL_19 ... ATL-11
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN
CLIN5
CCAN ICAN
MFL
CDCU
LPCAN
LHCM RHCM
Topview Camera front
ICAN
Topview Camera Rear
FID
Topview Camera Left side
Topview Camera Right side
LEth
Slave
ABT
BLCAN ECAN CCAN
CWCD_NFC BMCe IBRS
NFC EPS
EVCC
BLE_FL(UWB) SMLS
Private CAN
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
CONFIDENTIAL CLASS: INTERNAL Page 8
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal
CMP21_Export LHD A SUV VolumeLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
BCAN
Master
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
MSBD
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
BLCU
USS RSR USS RSL USS FSR USS FSL
CH1 CH2 CH2 CH1
BCAN
OMS camera
CLIN1 ASIC2 ASIC1
DMS camera
SCAN1
MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
ATL_10 ... ATL-1
1000base-T1
CDCU_SOC
CLIN3
XEth
XEth Front Wide Camera
Slave
Master
ATL_19 ... ATL-11
Rear facing camera
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN Topview Camera front
CLIN5
Topview Camera Rear
KLR MFL
CDCU NGX_PRO
Topview Camera Left side
LPCAN
Topview Camera Right side
LHCM RHCM
ICAN
FID
Front Tele Camera
HUD
LEth
Side Camera Front Left
Slave
ABT
Side Camera Front Right
Side Camera Rear Left
BLCAN Side Camera Rear Right
ECAN CCAN CCAN ICAN
CWCD_NFC BMCe IBRS
EPS
NFC
EVCC
BLE_FL(UWB) SMLS
Private CAN
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
FKS
CONFIDENTIAL CLASS: INTERNAL Page 9
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal EECU COP CU COP MM DMM Desesiiggnn
AGT CMP21-VolumeLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd EECU COP CU COP NNEEWW VW VW HW HW//SWSW
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
EECU COP CU COP NNEEWW VW VW HW HW
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
EECU COP CU COP MEMEBB
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
LISI/LTM WWM RLFS
RLIN4
PV2 PV1 AC_EXV Bat_Exv
CCAN
RLIN5 REth
Master BCAN
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
SMLS
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1 CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
TBF_FS
SCAN1
MRR
REth
CLIN2
Slave
1000base-T1
CDCU_SOC
CLIN3
XEth
XEth Front Wide Camera
Slave
Master
Rear facing camera
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
KLR MFL
DCAN Topview Camera front
CLIN5
Topview Camera Rear
                     CDCU NGX
Topview Camera Left side
Topview Camera Right side
ICAN
DMS camera
1000base-T1
FID
TEth
Slave
LEth
Slave
ABT
TPCAN ECAN CCAN CCAN ICAN
TEth
Master
BMCe IBRS
TBOX-5G
EPS
BLCAN
BLE_FL(UWB)
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
LLIN5
ICAN
LinDA
CONFIDENTIAL CLASS: INTERNAL Page 10
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal EECU COP CU COP MM DMM Desesiiggnn
AGT(IS34) CMP21-EntryLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd EECU COP CU COP NNEEWW VW VW HW HW//SWSW
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
EECU COP CU COP NNEEWW VW VW HW HW
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
EECU COP CU COP MEMEBB
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
Master BCAN
HV_H6 Blower UIF
SRS
Private CAN
UUSSSS R ROOLL UUSSSS F FOORR
ASV3 ASV2 ASV1
UUSSSS R RCCLL UUSSSS F FCCRR
UUSSSS R RCCRR UUSSSS F FCCLL
UUSSSS R ROORR UUSSSS F FOOLL
CCHH11
CCHH22
BCAN
ASASIICC
CLIN1
TBF_FS
REth
CLIN2
Slave
1000base-T1
CDCU_SOC
CLIN3
FLC
XEth
XEth
Slave
Master
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN
CLIN5
CCAN ICAN
MFL
                     CDCU
LPCAN
LHCM RHCM
Topview Camera front
ICAN
Topview Camera Rear
FID
Topview Camera Left side
Topview Camera Right side
LEth
Slave
ABT
BLCAN ECAN CCAN
BMCe IBRS
EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
LinDA
CONFIDENTIAL CLASS: INTERNAL Page 11
Switch
100base-T1 100base-T1
OBD
LegenLegenLegenddd
EEEttthhhererernnnetetet CACACANNNFDFDFD(((2M2M2Mbbbpppsss))) AAA2B2B2B
OpOpOptttiiiooonnnalalal EECU COP CU COP MM DMM Desesiiggnn
AGT(IS34) CMP21-VolumeLine
SGSGSGMIMIMIIII///PCIPCIPCIeee CACACANNN(((500K500K500Kbbbpppsss))) HarHarHardddwwwiiirrreee
StandStandStandarararddd EECU COP CU COP NNEEWW VW VW HW HW//SWSW
LILILINNN(((19.19.19.2K2K2Kbbbpppsss))) 120120120ΩΩΩ   (((tttererermmmiiinnnalalal r r resesesiiissstttooorrr)))
EECU COP CU COP NNEEWW VW VW HW HW
GGGMSLMSLMSL VVLALANN  ((ddefauefaulltt))
EECU COP CU COP MEMEBB
DDDSISISI333 CamCamCamerereraaa
VVLALANN11
RLIN1
PT2 PT1 EKK
RLIN2
RLIN3
RDCU
WWM RLFS
RLIN4
PV2 PV1 AC_EXV LLR_RL LLR_RS Bat_Exv
CCAN
RLIN5 REth
Master BCAN
HV_H6 Blower UIF
SRS
Private CAN
ASV3 ASV2 ASV1
MSBD
USS RCR USS RCL USS FCR USS FCL
USS ROR USS ROL USS FOR USS FOL
USS RSR USS RSL USS FSR USS FSL
CH1 CH2 CH2 CH1
BCAN
CLIN1 ASIC2 ASIC1
TBF_FS
SCAN1
MRR
PPS(NGX to CDCU)
REth
CLIN2
Slave
1000base-T1
CDCU_SOC
CLIN3
XEth
XEth Front Wide Camera
Slave
Master
Rear facing camera
100base-Tx
CLIN4
DEth
Auto
CDCU_MCU
DCAN Topview Camera front
CLIN5
Topview Camera Rear
MFL
                     CDCU NGX
Topview Camera Left side
LPCAN
Topview Camera Right side
LHCM RHCM
ICAN
DMS camera
FID
HUD
LEth
Slave
ABT
BLCAN ECAN CCAN CCAN ICAN
BMCe IBRS
EPS
BLE_FL(UWB) SMLS
BLE_FR(UWB) EOP
Private Lin
BLE_RL(UWB)
6 in 1
BLE_RR(UWB) F-Inverter
BLE(UWB) OCDC
BLCAN ECAN CCAN
LEth
Master
LLIN1
LLR_LL LLR_LS
LLIN2
AGS EBS
LLIN3
LDCU
LLIN4
RF
LLIN5
ICAN
LinDA
CONFIDENTIAL CLASS: INTERNAL Page 12
Switch
100base-T1 100base-T1
OBD

---

## PDF: VDU(C车动采)\CEA2.X\PRD\PDD_数据平台及能力_边缘计算_CEA2.0_IPDT3.0_外发版.pdf

PDD_数 据 平 台 及 能 力_边缘计算
_CEA2.0_IPDT3.0 
1. 文档概述 Document Overview 
1.1 基本 信息 Basic Information 
本文档旨在定义车端边缘计算模块的功能产品需求，包括边缘计算功能逻辑定义，以及数
据计算和交互流程，作为后续详细方案设计、开发、测试的指导文档和规范。 
本文档定义的边缘计算模块功能适用于CEA 2.0 。 
1.2 术语 缩写 Abbreviations 
为了确保读者对专业术语有一致的理解，以下专业术语表中定义了相应的术语缩写和说
明。 
术语缩写 定义及说明 
Abbreviation Definition and Description 
Electronic Control Unit, 车载电子控制单元 
ECU 
Database CAN, CAN 总 线数据库 
DBC 
Telematics-BOX, 车载 远程信息处理器 
T-BOX 
1.3 版本 信息 Version Record 
修
版本
日期 Department 订 修订记录 
号 
人 
王
俊 创建初版 
V0.1 2025.12.12 CBB 
皓
王 增加“数据及计算结
俊 果上传”及 “边缘计
V0.2 2025.12.26 CBB 
皓 算效能评估 ”部分。 
王
俊 V1.0版冻结 
V1.0 2026.03.05 CBB 
皓 
2. 需求描述 Product Description 
2.1 产品 概述 Product Overview 
随着汽车电子电器架构的迅速迭代发展，车端计算单元算力得到了前所未有的提升，为了
应对日益增长的数据处理需求，建立更为高效和敏捷的车云协同架构，满足更多的实时处
理和安全隐私需求，车端的边缘计算模块需要具备相应的计算处理能力。 
车端边缘计算模块是智能汽车电子架构中的快速计算处理的模块之一，通过分布式计算架
构实现数据就近处理，有效解决传统云端计算在实时性低、带宽成本高和数据隐私方面的
瓶颈问题。 
本产品旨在提供在部署边缘计算的平台能力，具体的边缘计算业务场景规则或模型由JV
或需求方自行配置实现，边缘计算模块的核心平台能力包括： 
• 车端实时数据的灵活收集与处理（可配置参与计算的信号范围及采样频率等） 
• 车端基于给定配置设定计算逻辑，储存对应结果（可配置计算规则，计算结果存储
及上传等） 
• 与云端联动的场景模型及配置的更新与迭代（云端提供面向需求方的配置平台，下
发配置文件，车端读取配置并实现更新） 
2.2 应用 场景 Applicable Scenarios 
边缘计
场
痛点 描述 示例 算价值&
景 
优势
•  端侧基
通过统计零
于小算
部件的使用
力计算
频次、时
部件耐
长、强度等
久性能 
统计制动器制动应
信息，分析
力曲线和制动时
零部件的使
零 •  仅上传
长，基于积分和加
用情况，评
部 结果数
法计算，构建出车
估零部件耐
件 据，显
大量原始 辆制动盘的实际耐
久磨损性能
耐 著降低
数据上传 久性能评估，将实
你，指导零
久 数据上
占用大量 际情况下的耐久表
部件耐久性
性 传流量
流量。 现与设计预期进行
能设计。 
能 及云端
比对，基于零部件
评 负载 
场景价值： 耐久的实际效果指
估 
对比实际数 导后续车型的耐久
•  基于高
据和测试数 指标设计与开发。 
频数据
据，进一步
提升寿
指导车辆耐
命评估
久研发。 
和预测
 
精度。
•  车端实
时分析
高频数
据，无
需全量
上传 
收集车辆在
事件发生前
•  毫秒级
当车辆遇
后指定时间
事件触
到故障/ 紧
车
段的快照数
发机
急事件需 收到事件数据收集
辆
据，支持紧
制，保
要数据回 指令后，将事件发
紧
急事件或故
障关键
溯或紧急 生前后1分钟的高
急
障的数据回
数据完
处理时， 频数据进行记录后
状
溯，供后续
整性 
云端没有 分析计算，供后续
态
分析。 
高频数据 紧急事件或故障的
数
•  基于事
支持，同 数据回溯及根因分
据 场景价值：
件动态
事数据到
析使用。 
快 捕捉特殊边
调整采
云端处理
 
照 界情况，供
集时长
有延迟。 
后续进一步
与频
 
分析优化。 
率，仅
 
上传事
件关联
数据，
节省至
少90%数
据流量
通过采集车
辆高频数
据，通过部
署在车端的 •  支持云
车
在车端部署驱动电
机器学习或 端模型
端 相对复杂
机转速异常预警的
深度学习算 迭代升
实 的模型部
机器学习模型（JV
法，为车辆 级 
时 署在云
提供），当发现异
提供及时的
预 端，车端
•  本地模
常时及时联动诊断
报警和预
警 以简单规
型及时
服务或上报云端进
警。 
模 则计算。 
触发紧
行处理。 
型 
场景价值： 急预警 
在车端迅速
完成数据闭
环 
•  基于高
频数据
基于车辆高
捕捉客
频驾驶数据 统计驾驶员瞬时加
车 户驾驶
云端低频
和统计驾驶 减速度的次数和大
辆 行为，
数据无法
员驾驶表 小，基于分布统计
驾 构造用
捕捉驾驶
现，分析用 及统计计算，分析
驶 户群体
过程中的
户使用习 驾驶员的驾驶风
行 使用习
快速变化
惯，构建车 格，形成不同风格
为
惯 
场景（如
辆驾驶行为 的驾驶图谱，作为
建
频繁制
•  驾驶特
模型，指导 后续车辆迭代设计
模 
动） 
征本地
车辆迭代设 开发的参考数据 
 
提取，
计开发 
保护用
户隐私 
2.3 法律 法规 要求 Regulation Requirements 
边缘计算设备应符合GB 4943.1 《信息技术设备 安全 第1部分：通用要求》 
边缘计算数据安全管理需符合《汽车数据安全管理若干规定（试行）》要求 
2.4 竞品 对标 分析 Benchmark Analysis
边缘计算的使用：目前已逐步运用到减少数据上传流量，车辆开发及维护（电池健康度及
安全风险），模型训练及迭代（ADAS 辅助驾驶）及AI相关应用（智 能诊断）等业务中。 
品牌 特性 应用场景示例 优势 
开发
速
度、
软件
质量
提升,
有效
降低
基于 使用
KubeEdge
成本 
的边缘侧
蔚来 
容器化的 边缘
边缘计算 节点
过滤
 
 
无效
数
云边协同的新能源汽车电池健康安全数据
据，
分析 
云端
训练
效率
提升
40%
获取车辆
的行驶信
息；根据
行驶信息
进行边缘
计算；响 及时
识别到车辆安全风险及时发送救援请求信
应于边缘 响应
息。 
比亚迪 
计算结果 应急
CN 119767284 A 
表征车辆 信息 
存在安全
风险，通
过通信单
元发送救
援信息。 
通过车端
规则引擎
初筛高价
值数据
（如
全面
Corner 
吸收
Case），
驾驶
云端结合
数
合成数据
小鹏 据，
生成技术
不遗
（如
漏关
GAN、扩
键细
 
散模型）
节。 
填补数据
辅助驾驶模型训练。 
空白，提
升模型泛
化能力。
实现
数据
传输
成本
由车端的 下降
边缘计算 75%，
引擎、边 云端
缘数据引 存储
擎、边缘 成本
数据库, 下降
智协慧同 
以及云端 90%，
的算法开 云端
（Tier1） 
发工 计算
具）、云 成本
 
端计算引 下降
擎和云端 33%，
车端数据解析& 复杂逻辑计算 
管理平台 总成
构成 本优
化可
以下
降
85%。 
2.5 需求 列表 Feature List 
L1 L2 L3 L4 Description
根据不同应用
场景的需求定
义边缘计算数
据采集能力 
• 能够从
信号矩
阵中选
取需要
场景数据采
边缘数据底
数据平台
边缘计算车 的信号
集 
座 Edge 
及能力 
进行读
端能力 
Data  Platform 
Data 
取 
Edge Scenarios 
- 数据边缘计
Platform 
Computation Data 
• 根据给
and 
算 Data Edge 
Capability Collection 
定的数
Capability 
Computation 
 
据采集
策略提
取并记
录数
据，作
为计算
模块的
输入
根据不同应用
场景的需求定
义边缘计算模
块的数据处理
逻辑 
• 处理异
常的数
据，完
成数据
清洗，
转换，
标准化
等预处
理操
作，支
持后续
边缘计
场景数据计
算和实
算 
时分析
   
等场
Scenarios 
Data 
景。 
Calculation 
• 基于给
定的数
据处理
及计算
逻辑
（如时
间段、
硬件、
问题类
型
等），
选择目
标数
据，进
行计
算。 
• 计算能
力涵盖
计数
器，计
时器，
加法
器，数
值比
较，筛
选，数
据统计
及简单
算法
等。
根据不同应用
场景的需求定
义边缘计算模
块的数据存储
逻辑 
• 支持基
于数据
实时
性，计
算需求
及计算
结果更
新周期
的分级
数据存储 存储 
   
• 支持数
Data Storage 
据的读
取，存
储，修
改及删
除 
• 存储计
算后的
结果的
备份数
据 
• 清除后
续不再
参与计
算的历
史数据 
数据及计算
能够将采集到
结果上传 
的数据或边缘
   
计算的结果数
Data and 
据按指定策略
Computing 
Result 
进行上传 
Upload
根据云端下发
的配置文件进
行边缘计算配
置的更新 
• 数据采
集、存
储、上
传的配
场景配置更
置 
新 
• 能够基
   
于平台
Scenarios 
下发的
Configuration 
Updating 
参数/
脚本设
置指令
调整数
据处理
和计算
逻辑策
略 
记录边缘计算
边缘计算效
模块使用效能
能评估 
及故障日志，
   
以支持边缘计
Edge 
Computing 算模块的持续
Performance 
优化及故障问
Evaluation 
题的解决。
根据不同应用
场景的需求定
义边缘计算所
需要的平台数
据配置能力 
• 平台可
以下发
的数据
采集及
存储的
调整的
参数配
置 
• 平台可
场景配置及
以配置
计算模型迭
边缘数据底
数据平台
边缘计算云 数据传
代 
座 Edge Data 
及能力 
端能力 输触发
Platform - 数
Data 
的条
Cloud for 
Configuration 
Platform 据边缘计算 
Edge 
Setting and 件，定
and 
Data Edge 
Computation 
Calculation 
期/ 不
Capability 
Computation 
Model 
定期，
Update 
依据指
令触发
等 
• 云端平
台配置
并下发
数据计
算逻
辑，阈
值，脚
本等边
缘计算
核心逻
辑
边缘计算结
根据不同应用
果可视化 
场景的需求展
   
示边缘计算上
Result 
传的结果数据 
Visualization 
2.6 产品 框架 
功能逻辑框图及数据流（以雨刮器耐久为例） 
 
3. 功能描述 Function Description 
3.1 边缘 计算 车端 功 能 Edge Computing - Edge Side 
Functions 
3.1.1 场景数据采集 Scenarios Data Collection 
功能描述 
根据不同应用场景的需求定义边缘计算数据采集能力，具体包括 
• 数据采集规则可配置（基于云端下发的配置文件） 
• 能够从信号矩阵范围中选取需要的信号进行读取 
• 基于数据来源及属性需求实施不同的数据采集策略（采样频率） 
• 根据给定的数据采集策略提取并记录数据，作为后续计算模块的输入 
前置条件
• 车端接收到数据采集配置文件 
• 边缘计算数据采集模块能接收到整车级数据（包括CAN/LIN/SOMEIP 等）。 
• 可配置的采集信号在整车级数据采集范围内（与T-BOX接收到的整车 级数据范围
保持一致），不包含敏感数据。具体数据范围详见整车级数据采集PRD。 
• 用户同意隐私协议对车辆数据进行采集和上传 
https://devstack.vgc.com.cn/confluence/spaces/CEAA/pages/499414291/PRD_MOS021_%E6%
95%B4%E8%BD%A6%E7%BA%A7%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86
%E4%B8%8E%E4%B8%8A%E6%8A%A5 
激活条件 
车辆上电 && 车辆信号传输正常 
基本事件 
• 检查目标数据采集的配置文件及车辆数据采集用户隐私知情同意（与VDU整车数
据上传一致）的完整性，包括  
o 数据采集配置文件中的：信号名称，帧ID，采 样频率，解析规则（DBC ）
等策略。 
o 用户知情同意状态为同意进行数据采集。 
• 根据配置文件设定的策略采集并解析数据，将解析后的实时数据导入各场景的计算
模块。  
o 数据采集范围限定于T-BOX能接收到的整车级数据。 
o 采样频率支持毫秒级到秒级的数据采样，最高采集频率与T-BOX能接 收到
的频率一致。 
异常事件 
若出现以下异常情况，生成对应故障报文上传云端平台： 
• 配置文件或用户知情同意状态读取失败 
• 配置文件中发现数据缺失或错误配置 
• 目标数据采集或解析失败 
部分数据采集场景出现异常时，不影响其他数据的正常采集与计算。 
3.1.2 场景数据计算 Scenarios Data Calculation 
功能描述
基于不同场景的计算是边缘计算模块的核心，根据不同应用场景的需求定义边缘计算模块
的数据处理逻辑，具体功能包括： 
• 计算规则可配置（基于云端下发的配置文件） 
• 数据预处理，针对异常的数据进行清洗，转换，标准化等操作，支持后续边缘计算
和分析。 
• 基于给定的数据处理及计算逻辑，选择目标数据作为输入，进行计算。 
• 计算能力涵盖计数器，计时器，加法器，数值比较，筛选，数据统计及简单算法
等。 
前置条件 
• 车端接收到数据计算配置文件 
触发条件 
车辆上电 && 车辆信号传输正常 
基本事件 
• 读取配置文件中的数据预处理规则，对输入数据进行预处理  
o 识别到数据为空值、缺失、超出有效范围或异常时，不使用该值参与计算或
使用上一个有效值进行计算 
o 插入元数据信息（时间戳、类型等），确保数据对齐 
o 对原始输入数据进行聚合计算，生成后续计算需要的中间结果 
• 读取配置文件中各场景的计算规则，运行对应的计算算子组合，生成需要的结果 
• 计算算子需包括  
o 基础逻辑：布尔运算及其他复合逻辑运算 
o 数值计算：包括算数运算（加减乘除积分微分等） 
o 统计运算：最大值，最小值，计数、均值、方差等 
o 流式计算：基于数据流设定相应的时间或事件窗口进行的聚合计算 
o 规则比较：基于设定规则的数据筛选，数值比较等 
o 简单算法：基于指定的计算逻辑或脚本计算（例如雨流计数算法，基于基于
时间序列的平滑，滤波，统计等） 
• 计算结果按照对应的场景进行聚合，并按指定的输出格式存储到车载。 
异常事件 
当数据计算过程出现异常时，生成对应故障报文上传云端平台 
3.1.3 数据存储 Data Storage
功能描述 
根据不同应用场景的需求定义边缘计算模块的数据存储逻辑，具体包括能够 
• 数据存储规则可配置（基于云端下发的配置文件） 
• 支持基于数据实时性，计算需求及计算结果更新周期的分级存储； 
• 支持数据的读取，存储，修改及删除； 
• 备份存储计算后的结果数据； 
• 定时清除后续不再参与计算的历史数据。 
前置条件 
• 边缘计算模块具备数据存储能力，或可以使用车载数据存储能力。 
• 车端接收到数据存储配置文件 
激活条件 
车辆上电 && 车辆信号传输正常 
基本事件 
• 数据存储的可配置内容：数据存储方式，存储格式，数据清理周期，数据备份等 
• 数据分级存储：读取数据存储的配置文件，根据预定义的数据标签实施分级存储管
理。数据分类包括：  
o  
数 存 清 数
据 储 理 据
定义 
类 方 周 备
型 式 期 份 
缓 数
实
通过CAN/LIN/SOMEIP 存/ 据
时
等总线实时采集并解析 不 使 否 
数
的整车级数据。 存 用
据 
储 后
缓
存/
中
计算过程中临时产生， 持
间 每
需参与后续计算环节的 久 是 
数 日 
中间过程或结果数据。 化
据 
存
储 
结
用户设定的最终计算结
持 果
果指标，用于云端上传
结
久 上
果 或调取的数据。 
化 传 是 
数
存 成
包括行程数据、周期数
据 
储 功
据、连续累积数据等。 
后 
• 数据存储能力：  
o 数据操作：支持在计算过程中对中间数据或结果数据进行读取、存储、修改
及删除。 
o 数据备份：依据配置文件对存储的数据进行周期性备份。 
o 数据清理：数据完成计算任务或结果上传后，按照给定的清理周期进行数据
清理。 
o 下电数据存储：车辆下电前自动将当前行程计算的完整结果按预定格式进行
持久化存储。 
异常事件 
若出现以下异常情况，按对应策略执行： 
• 车辆异常下电：自动缓存当前中间数据和结果数据并按指定格式完成紧急存储，待
系统恢复后自动重新加载数据继续计算。 
• 数据存储异常：启用备份数据，保证计算数据连续性和业务不间断。 
• 数据存储容量低：存储使用量接近设定存储容量时，优先清理早期存储数据，上传
相应结果数据，确保系统存储容量始终处于安全范围。 
3.1.4 数据及计算结果上传 Data and Computing Result Upload 
功能描述 
将采集到的数据及边缘计算的结果数据按指定策略进行上传
前置条件 
• 车端接收到数据存储配置文件 
• 用户同意隐私协议对车辆数据进行采集和上传 
激活条件 
• 满足配置的数据上传触发规则（固定周期或给定条件） 
• 接收到云端下发的数据上传指令 
基本事件 
• 确认用户同意隐私协议对车辆数据进行采集和上传 
• 读取数据上传的触发规则  
o 支持数据上传周期在7-30天间进行配置 
o 接收到云端下发的数据上传指令时，上传全部数据 
• 从数据存储中提取结果数据，按配置好的上传通道及指定格式进行上传。 
• 确认数据或计算结果传输成功后，根据数据存储配置对数据进行清理。 
异常事件 
当数据上传出现异常时，尝试重复上传或再次上电后补发。 
3.1.5 场景配置更新 Scenarios Configuration Upgrade 
功能描述 
根据云端下发的配置文件对车端边缘计算配置进行更新，具体包括 
• 数据采集、存储、上传的配置 
• 数据处理和计算逻辑策略（平台下发的参数/ 脚本） 
前置条件 
车辆上电 
激活条件 
接收到云端下发的场景配置文件或指令 
基本事件
• 接收到云端下发的场景配置文件后，进行完整性及可用性校验 
• 在不影响车辆正常行驶及充电的条件下，寻找合适的时间点进行更新（推荐车辆处
于静置状态），更新配置信息包括：  
o 数据采集、存储、上传的配置 
o 数据计算规则，依赖，模型算法 
• 完成计算模型和配置调整更新后，重启边缘计算模块，检查边缘计算模块可用性，
并向云端平台上传更新状态 
异常事件 
若出现配置更新不成功，生成对应故障报文上传云端平台，并使用上一般正确运行的版
本。 
3.1.6 边缘计算模块效能评估 Edge Computing Performance Evaluation 
功能描述 
监控边缘计算模块各场景运行状态及问题日志上传 
激活条件 
边缘计算模块运行 
基本事件流 
• 场景运行状态监控：监控各场景运行状态，记录场景异常状态时的故障日志 
• 按云端需求向云端传输异常状态时的故障日志 
3.2 边缘 计算 云端 功 能 Edge Computing - Cloud Side 
Functions 
3.2.1 边缘计算场景配置 Edge Computing Scenarios Configuration 
功能描述 
根据应用场景的不同需求定义边缘计算所需要的平台数据配置能力 
• 云端平台基于场景提供配置设定界面，并下发数据采集、存储及上传的配置 
• 云端配置并下发数据计算逻辑，脚本等边缘计算核心逻辑  
前置条件
需求方提出需求，由平台运营人员进行操作 
激活条件 
平台运营人员接收到对边缘计算场景的配置新增，更新或修改的需求 
基本事件 
• 用户进入 “边缘计算场景配置页面 ”，设置对应边缘计算业务场景的配置参数，具体
包括  
o 业务场景信息：场景名称 
o 数据采集配置：采集信号，采样频率，解析规则等 
o 数据计算配置：预处理方式，数据依赖，触发条件，输出结果格式，计算规
则（通过可视化平台完成逻辑组合或给定脚本实现）等 
o 数据存储配置：存储位置，格式，清理周期，数据备份等 
o 数据上传配置：上传周期、结构，接口等 
• 用户进入 “边缘计算发布配置页面 ”，设置规则生效的车辆范围  
o 可基于不同品牌/ 车型/ 车型码/ 生产下线时间/ 自定义的车辆清单进行配置 
• 在配置过程中检查到用户设置的参数不合理，生成红色文字提示，配置完成后，再
次检查设置参数及规则的合理性。 
• 生成对应的配置文件，经过灰度测试和审批后批量下发给目标车辆。 
CEA2.0 定义支持配置的边缘计算场景见（约400 个）： 边缘计算场景示例_20260303.xlsx 
配置示例如下： 
数
场 场 场景 据
数据
景 景 描述 数 据计 算配 上
触 发条 件配置 数 据采 集配置 存储
类 名 （示 置 传
配置 
别 称 例） 配
置 
Json; 
统计
每
ABS
统计ABS 信 30
功
持久
ABS
ABS 工作状态 
信号
日 
能
号切换为激
激 化覆
车辆上电 
切换
使
活的次数 
活 盖存
IPB_ABSActSt_E2E 
打
到激
用
频 储； 
CUCU_KL15status = 1 
包
活的
计 算子：
采集频率：1s 
次 
上
数 累积
CounterScalar 
不清
传 
次数 
理
Json; 
每
累计
累积制动液 30
状 低
持久
制动
制动液位低警告 
日 
水平低于下
态 制
化覆
液低
车辆上电 
时 动 限状态的时
盖存
于下 CDCU_BFLWarning 
打
长 液 长 
储； 
CUCU_KL15status = 1 
限的
包
统 状
采集频率：1s 
持续
上
计 态 算子：Sum 
不清
时间 
传 
理 
通过
雨流
通过雨流算
Json; 
计算
法统计车辆
车身
左 加速时加速
持久
每
加速
前 度上下限值
车辆上电 
化每
边 度的 7
车
及对应的次
左前车辆加速度 
个行
日 
界 穿刺
辆
CUCU_KL15status = 1 
数 
程存
迟 次数
加 AS_Accelerometer_FLVD 
打
储； 
滞 统计
左前车辆加速度大于0 
速
算子：
包
曲 得到
采集频率：50ms 
度
Rainflow 
数据
上
线 车辆
AS_Accelerometer_FLVD >0 
边
上传
传 
实际
中间数据：
界 
后清
驾驶
车辆加速度
理 
加速
上下限值 
度边
界 
 
3.2.2 边缘计算结果可视化 Edge Computing Visualization 
功能描述 
接收到上传的周期性边缘计算结果后，可以在云端平台上按应用场景进行可视化展示 
激活条件 
用户需要在云端页面上查看可视化图表时 
基本事件 
• 用户进入 “边缘计算结果可视化页面 ”，设定需要调取的场景结果数据及时间段
o 返回指定时间段内的结构化数据，供用户查看 
o 通过BI工具设定数据展 示维度，生成对应可视化图表 
o 支持对应结果数据和可视化图表导出 
• 云端存储的数据施行1年热备，超过1年的数据冷备的策略 
4. 系 统 资 源需 求 
基于CEA2.0 已明确的约400个场景的资源估算（以实际开发为准）： 
• RAM: 8 ~ 16MB 
• 单次落盘存储： 0.8 ~ 1.5 MB 
• 快照场景：1.1 ~ 1.9 MB 
5. 数 据 安 全合 规 要 求 
• 数据安全合规需严格遵循《中华人民共和国数据安全法》《中华人民共和国个人信
息保护法》《汽车数据安全管理若干规定（试行）》《汽车数据出境安全指引
（2026 版）》 
• 边缘计算模块数据采集隐私保护与整车级数据上传保持一致，参考：
PRD_MOS021_ 整车级数据采集与上报 - CEA - DevStack Confluence 
6. 验收标准 
7. 排期计划 
IPDT 节 车 端能 云 端能
奏 力 力 
车端基 云端基
IPDT3.0 础能力 础能力
开发 开发 
配置功 配置平
IPDT4.0 
能开发 台开发 
可视化
计算逻
IPDT5.0 平台开
辑验证 
发
联调进 联调进
IPDT6.0 
度 度
=100% =100%

---

## PDF: 动采_AF\A\ZCU性能问题\ZCU动采方案评估材料.pdf

ZCU动采方案评估材料
YFT
2025
LL  CCoonnffiiddeennttiiaall@@22002200
1
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
ID SWPEL00xx Customer: xx Project: xx Product Zone: xx Title: xxxx Program Phase: xx Submitter: xx
A车VFF阶段ZCU域控制器系统概况
内存资源占用情况： CPU Load占用情况(基于AL V4.2.6版本进行分析)：
AL ZCU                                  实车台架场景：AL刷写前Core0 79% Core 1 84%，刷写时Core0 84%，Core1 89%
Flash: 73.1%          0S预计上升到 78%~83%
RAM: 80.9%          0S预计上升到 85%~90%
AR ZCU：
Flash: 70.9%               0S预计上升到 75%~80%
RAM: 67.8%               0S预计上升到 72%~77% 横展11/09 大众台架AL刷写失败问题：11/9号更新V4.2.2版本软件后，大众台架AL
                      侧刷写功能异常，实测刷写失败率高达90%；经过分析发现是刷写时系统负载过高导致
                      系统异常复位（Core0 92%，Core1 98%），经过一系列降低负载操作后刷写功能恢复正常；
*异常场景下Core1峰值负载达到100%，由于获取不到CPU资源，看门狗触发复位
Plan                Execute      Confirm             Reflect
R/Y/G or

进度Progress
L Confidential@2020
2
 
 
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
ID SWPEL00xx Customer: xx Project: xx Product Zone: xx Title: xxxx Program Phase: xx Submitter: xx
数据动采功能资源占用情况概览（数据来源：B车BL PVS版本集成软件）
B车动采模块内存占用情况：
B车左域动采模块CPULoad占用（单件空载环境，仅实现CAN/LIN数据动采）：      B车左域模拟固定动采40条以太网周期报文场景下测试CPULoad占用：      
动采开启前：                动采开启前：                
Core0 38.35%，Core1 45.11%； Core0 38.35%，Core1 45.11%；
动采开启后：                动采开启后：                
Core0 46.40%，Core1 47.12%； Core0 46.40%，Core1 55.38%；
总结：理想环境下CAN/LIN数据动采增加10.05%左右的CPU负载； 总结：模拟发送ETH报文估算以太网动采预计增加10%~20%左右的系统负载，即
10%~15% (ETH报文处理负载)+2%~5% (SOMEIP服务查找算法)
Plan                Execute      Confirm             Reflect
R/Y/G or

进度Progress
L Confidential@2020
3
 
 
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
ID SWPEL00xx Customer: xx Project: xx Product Zone: xx Title: xxxx Program Phase: xx Submitter: xx
A车数据动采方案评估材料
总结：
                 1. A车内存占用过高，需优化存储空间：
a. 目前A车左域Flash使用量为73.1%，RAM用量为：80.9%；后续版本迭代预计会再增加10%左右的内存占用即：Flash：80%，RAM：90%；
b. 若加上数据动采功能则AL Flash达到 83.2%，RAM占用92%；
c. 考虑到后续系统升级维护要求，需要考虑内存预留给新增功能；
             
                 2. A车CPU Load过高，需优化系统负载：
a. 目前AL控制器实车平均负载已经高达Core 0 79%，Core 1 84%；
b. 若加上动采功能则会导致高负载场景下负载达到：Core 0 91% (OTA增加5%，CAN/LIN动采增加10%) ， Core 1 119% (OTA增加5%，车窗防夹增加10%，ETH动采增加20%) ；
c. 后续功能新增需预留5%~10%系统负载；
结论：
                目前A车系统负载过高，已经达到临界值。考虑PVS+0S阶段版本迭代仍有5%~10%的负载增加，目前的A车软件无法支撑数据动采功能实施；
Plan                Execute      Confirm             Reflect
R/Y/G or

进度Progress
L Confidential@2020
4
 
 
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential
Yanfeng Confidential Yanfeng Confidential Yanfeng Confidential

---

## PDF: 动采_AF\A\拓扑图\A车AGT2阶段网络拓扑Draft V0.6_20250122-水印.pdf



---

## PDF: 动采_AF\A\拓扑图\大众A车PT阶段网络拓扑_draft_V0.4_20250227_水印.pdf



---

## PDF: 动采_AF\F\6s\TOP1 B SUV EREV 6S Time Line 20241220.pdf

B SUV EREV Timeline 2024.12.19(KW51.4)
Confidenti al
2024 2025 2026
03 04 05 06 07 08 09 10 11 12 01 02 03 04 05 06 07 08 09 10 11 12 01 02 03 04 05 06 07
Project Milestone
里程节点
MOU NDA TLA lite PF(G8) KF(G7) PLF(G6) BF LF VFF PVS 0S SOP
15  16  26  42/10.15 49/12.2 07/2.10 (G5) 30 (G4) (G3) (G2) (G1)
18/4.30 40-1/9.29 49-1/12.01 06-1/2.2 13-5/3.27
Design
造型
st st
Start 2D  1 3D  1 3D  DA/DV(Go1) DE/DF(SA ）
Problem & Task
17 Ext. 29 Int. 30 40.1  47.1
1 Due to production location in CPH, ZP5 must be 
DDKM2 All
Strak
changed, B-Guss delay risk
（DG2）13
光顺
-> find solution to keep B-Guss CW05   Resp. EKK/PFS
Design direction 1. Strak DDKM VF VF DDKM DDKM s.FKM DDKM2
-> release P-F data KW51/5                      Resp. EKK 
alignment 36  （DG0） ZP5 ZP7 ZP5 (DG1) 06 LLT
33 -> 34.3  40 47.5 48 50 52 08
Structure P Freigabe
st st
(TG1)
Structure 1 Simulation 1 Structure
for Simulation for body finish(TG1)
41 46  48 
Concept
nd
方案 technical Concept 2 Simu.
output 21  release 50  1 (CAE Result) 17
Structure B Freigabe (TG2)
upper body 上车 体钣 金
st
Vergabe to PM B Guss B-Frei Prio.1(TG2) 1 tryout M1
45.1 ->47.3  05 10/3.7 28 10
Structure B Freigabe (TG2)
under body 下车 体钣 金 st
B Guss B-Frei Prio.1(TG2) 1 tryout M1
05 10/3.7 28/7.11 10
Structure B Freigabe (TG2)
st
ext. & int. 内外 饰 B-Frei Prio.1(TG2) 1 tryout OTS K-Freigabe(ESO)
14/4.4 37
Nomination & Parts
Start Nomi for Nomi DDL  36 -> 51 Tooling Part ToolingPart OTS K-Freigabe(ESO)
development supplier ZP5 body ext. & int.
from cw 29  28/7.11 34/8.22
E/E architecture
sub system audit
AGT1
for change ECM
Purchase Body of Base car
(simu car of IM F model)
Start PR Handover Body
29 -> 30  44 / 11.01 
AGT1(mule) Car
st
RFQ(SOR) ZP7 TBT(GA MRD) 1 Car(FIV mule)
29 ->32  46/11.15 -> 47  52/12.27
E/E architecture
AGT2
PRD&EFL Prio.1 Axrml AGT2 Software AGT2 Baseline release AGT2
35 / 8.30  47 / 11.22  09 / 2.28 14/4.3
AGT2(Simu) Car
st
start RFQ(SOR) ZP5 TBT(BO MRD) ZP7 TBT(GA MRD) 1 Car(FIV simu)
47 -> 49  06 / 2.7 10 / 3.3 16 / 4.18
E/E architecture 
PRD&EFL Prio.1 Axrml PT Software PT Baseline release PT
EP
44 / 11.1  09 / 2.27 24 / 6.13 31 / 8.1
EP crash Car
ZP5 TBT(BO MRD) ZP7 TBT(GA MRD) 12 crash car(FIV EP) ZDC release DDL for Homo 
28 / 7.11 34 / 8.22 37-38 45 / 11.6
EP Car
st
ZP5 TBT(BO MRD) ZP7 TBT(GA MRD) 1 ep cars for Homo(FIV EP)
28 / 7.11 34 /8.22 39 / 9.26  
Mod Motor EA211 1.5T
st
RFQ 1 HW with SW B-Sample for AGT2 C-Sample Data for data freeze DET
31 46->48  04 21 pre test 42 45 04
Mod Transmission HT30
st
new housing
RFQ(TG0) 1st  HW(DL2) PT part(DL3) B-Frei(TG2) 1 T0(VB)
34  46  10 / 3.4 18 / 4.30 30 / 7.25
Thermal management
software new develop
Start BM Nomi supplier for SW SW for AGT2 SW for EP/VFF Final data
32 37 -> 44.1  08 32 04
Powertrain & chassis
application
Application AGT1 Winter test Environment test Data for Final data
01 pre test 42 04
ADAS
RFQ(SOR) Nomi BSW 台架 ASW 台架 BSW 功能闭环
BSW development
31.1  38.2->44 (8650&BMC) (8650&BMC) 31
03 08
Function development
AGT2(Simu) PT(EP) VFF test car Function ready
17 39 42 10
Function release
Start PVS Validation Customer release
51 10
E/E architecture
Vorserien
Baseline Baseline Baseline Baseline release
release PT/VFF release PVS release 0S SOP+1 bugfix
31 /8.1 42 / 10.17 52 / 12.24 18 / 4.30
Homologation
using EP car for Pre Test and 
Pre-Start Compulsory System acceptance CCC
using VFF car for Homologation
41-1 / 10.6 test 52-4 / 12.25 12
46-4 / 11.13
2024.12.19(KW51.4)
Ersteller: SVW EPM
Date:  19.12.2024

---

## PDF: 动采_AF\F\拓扑图\AGT2&PT B车 Network Topology  20241018 V0.6.pdf



---

## PDF: 动采_AF\F\拓扑图\PT B车 Network Topology  20250124 V1.0-外发.pdf

上汽零束保密文件，仅用于大众和上汽零束项目使用
上汽零束保密文件，仅用于大众和上汽零束项目使用
上汽零束保密文件，仅用于大众和上汽零束项目使用
上汽零束保密文件，仅用于大众和上汽零束项目使用
上汽零束保密文件，仅用于大众和上汽零束项目使用
上汽零束保密文件，仅用于大众和上汽零束项目使用

---

## PDF: 动采_AF\F\拓扑图\PT 大众B车 Network Topology  20250221 V2.0 - 外发.pdf

SVW PT B 车 Network Topology  
Version 2.0
Li Maoya
上汽零束保密文件，仅用于大众和上汽零束项目使用
TPMS
诊断口 智能网联控制器
DLC IAM
SVW PT  B-SUV 
120
Diagnostic CAN Diag_ETH Connected CANFD IAM_ETH
 ETH&CAN Network Topology
60 120
ADAS_ETH
ICC
120
RZCU CANFD
Standard
ICM
120 120
BackUp CANFD
AMP
ZXD
IPD
Optional
120
120
120
 
智驾控制单元
 
 
Project
 
 
 
 
HeadLighting
 
RHZCU_ETH
 LHZCU_ETH
Backbone CANFD
CANFD
 
 
 
ADAS Local CANFD
 
FLIDAR_ETH
 
RZCU_ETH
 
Intergrate
 
 
 
 
 
120
Status:                    Add 
A
                               Modified         
M
FLIDAR FDR
                               Carry Over
C
前雷达
前向激光雷达
Connector Config: 
120 120
120
TR=120Ω Shielded
BCM ITMS
BCM SCU
IMU BCM
120
Chassis CANFD
60
TR=60Ω Wireless
RRSM
FRDCM
FLDCM
RF SMLS
120
Safety CANFD
RZCU
LHZCU RHZCU
TR=∞/Irrelevant
RLSM
RRDCM
RLDCM EASC
PLCM
FRSM IEC
IEC
FLSM
Connection Config: 
120
120
120 120 120 120
Ethernet_10G_base_T1
Ethernet_1000M_base_T1
RH Body CAN
Ethernet_100M_base_T1
Z
PowerTrain CANFD Extended Range CANFD PowerTrain Extended CAN LH Body CANFD
Suspension CANFD
Ethernet_10M_base_T1
数字钥匙主模块
CANFD
Local CANFD
RHA
CAN
120
BPEPS
Diagnostic_CAN
兼容UWB
Local CAN
右前大灯模块
120
120
EAC
120
120
IBS
SCM PEU
SDM
LIN
电动空调压缩机
集成式制动系统 自适应悬架
NFCSM
电力电子单元
Flexray
安全气囊控制诊断模块
集成MPWC
LVDS
120
NFC 启动模块 LHA
EPS
120
ECM
左前大灯模块
电动助力转向
NFCAM
集成CMM
智舱SOC 接口
Inftn
发动机控制模块
NFC 进入模块
RWSL
后轮转向 RRBLEA
LVBM
右后蓝牙天线
低压电源管理
RLBLEA
左后蓝牙天线
CCU
高低压集成充电模块
FRBLEA
右前蓝牙天线
120 120
TC
FLBLEA
后电机
左前蓝牙天线
ESS
120
120
OffBdChrgr CAN
ChrgrSkt
能量储能系统
充电口
上汽零束保密文件，仅用于大众和上汽零束项目使用
SVW PT B 车 
LIN Network Topology
DTSM_FR FRSASW( 座椅调节开关)
Standard
DTSM_RR
RHZCU RZCU
DOTSM_FR
DOTSM_RR
Optional
RHZCU_LIN5
RHZCU_LIN6
RHZCU_LIN4
RHZCU_LIN8
RHZCU_LIN3 RHZCU_LIN7
RZCU_LIN3 RZCU_LIN4
RZCU_LIN2
RHZCU_LIN2
RZCU_LIN1
 
 
Project
 
 
ChrgngStaLamp
TailLampAsmblA_LH
CF UpIPAmbtLampA_LH DoorAmbtLamp_FR RoofAmbtLampA_LH ESSClntPump FRSLMM
 
ClntVlv
AIntnlTemSnsr
 
 
 
 
 
顶棚氛围灯A- 左 三通阀
充电状态灯 
门饰板氛围灯-右前 能量存储系统冷却水泵
尾灯总成A_ 左
 车载冰箱
上仪表板氛围灯A- 左
右前座椅腰托按摩模块
 
舱内温度传感器
 
 
Intergrate
 
 
 
RoofAmbtLampB_LH
DoorAmbtLamp_FRM
 UpIPAmbtLampB_LH
IFM
 
TailLampAsmblA_RH  
APTC TailLampAsmblA_RH  
MulChnlVlv
WtrPTCPump
RLSLMM RRSLMM
Status:                    Add 顶棚氛围灯B- 左
A
门饰板氛围灯M- 右前
上仪表板氛围灯B- 左
香氛散发模块
                               Modified         
M
尾灯总成A_ 右
冷却系统多通阀 空气加热器
HVPTC 水泵
左后座椅腰托按摩模块 右后座椅腰托按摩模块
                               Carry Over
C
RoofAmbtLampC_LH
DoorAmbtLamp_RR
UpIPAmbtLampA_RH
仅 6 座 车 型
CoolngFan
TailLampBsmblB_RH
PEBClntPump1
TailLampAsmblB_LH
Connector Config: 顶棚氛围灯C-左
门饰板氛围灯-右后
上仪表板氛围灯A-右
120
TR=120Ω Shielded
N o t e : 上 仪 表 氛 围 灯 拆 分 ， 硬 件 P T 实 施 ， 功 能 P V S 实 施
电驱动电子水泵 冷却风扇
尾灯总成B_ 左
60
TR=60Ω Wireless RoofAmbtLampD_LH
DwnIPAmbtLampA_LH
DoorAmbtLamp_RRM
TR=∞/Irrelevant
顶棚氛围灯D-左
AGS1
Blwr_F
TailLampAsmblB_RH
下仪表板氛围灯A-左
门饰板氛围灯M- 右后
Connection Config: 
RoofAmbtLampA_RH 主动进气格栅_1 前鼓风机
Ethernet_10G_base_T1
尾灯总成B_ 右
Ethernet_1000M_base_T1
DwnIPAmbtLampA_RH
MapPcktAmbtLamp_FR
Ethernet_100M_base_T1
顶棚氛围灯A- 右
Ethernet_10M_base_T1
下仪表板氛围灯A-右 地图袋氛围灯-右前
CANFD
RoofAmbtLampB_RH
Local CANFD
CAN
MapPcktAmbtLamp_RR
DwnIPAmbtLampB_RH
Diagnostic_CAN
顶棚氛围灯B- 右
Local CAN
下仪表板氛围灯B- 右
地图袋氛围灯-右后
LIN RoofAmbtLampC_RH
Flexray
顶棚氛围灯C- 右
LVDS
RoofAmbtLampD_RH
智舱SOC 接口
Inftn
顶棚氛围灯D- 右
N o t e ： P V S 将 取 消 顶 棚 氛 围 灯 左 右 D 节 点
LHZCU ZXD ECM PEU
LHZCU_LIN2 ZXD_LIN1 ECM_LIN1 PEU_LIN1
LHZCU_LIN3 ZXD_LIN2 ZXD_LIN4
LHZCU_LIN8
LHZCU_LIN4
EnEleclMainWtrPump EOPC
LAirVentVertMot
FLSLMM
CupholderAmbtLamp_LH
TPMS
OHC
DoorAmbtLamp_FL
左侧出风口垂直扫风电机
电子油泵控制器
杯托氛围灯-左 发动机电子主水泵
门饰板氛围灯-左前
顶控模块
胎压传感器 左前座椅腰托按摩模块 
LAirVentHoztMot
MFL
DrvrDsp
RLSS
左侧出风口水平扫风电机     
CupholderAmbtLamp_RH
DoorAmbtLamp_FLM
KickSnsr
方控开关
仪表屏
阳光雨量传感器
门饰板氛围灯M- 左前 杯托氛围灯-右
脚踢传感器 MidLAirVentVertMot
N o t e ： 屏 幕 功 能 安 全 接 口 预 留
中央左出风口垂直扫风电机  
FWM
DoorAmbtLamp_RL CnsoAmbtLamp_LH
HODM
RoofDsp
MidLAirVentHoztMot
前雨刮电机模块
门饰板氛围灯-左后 中央通道氛围灯- 左
后排吸顶屏电机
离手检测模块
中央左出风口水平扫风电机  
MidRAirVentVertMot
DoorAmbtLamp_RLM
CnsoAmbtLamp_RH
中央右出风口垂直扫风电机 
门饰板氛围灯M- 左后
中央通道氛围灯-右
MidRAirVMidRAirVentHoztMotentHoztMot
MapPcktAmbtLamp_FL
CnsoAmbtLamp_LM
中央右出风口水平扫风电机 
中央通道氛围灯-左中
地图袋氛围灯-左前
RAirVentVertMot
右侧出风口垂直扫风电机
MapPcktAmbtLamp_RL
CnsoAmbtLamp_RM
RAirVentHoztMot
地图袋氛围灯-左后
中央通道氛围灯-右中
右侧出风口水平扫风电机
N o t e ： 中 央 通 道 氛 围 灯 新 增 L M 、 R M 节 点 ，
硬 件 P T 实 施 ， 功 能 P V S 实 施
电动出风口
上汽零束保密文件，仅用于大众和上汽零束项目使用
右前侧周视摄像头 左后侧周视摄像头 右后侧周视摄像头 
前周视摄像头3 后周视摄像头
左前侧周视摄像头 
前周视摄像头1
抬头显示 后排吸顶屏
后排智能表面_左 后排智能表面_右
SVW PT  B 车 
AVCamr_F3 AVCamr_R AVCamr_FLS AVCamr_FRS AVCamr_RLS AVCamr_RRS
AVCamr_F1
HUD
RoofDsp
LHRSS
RHRSS
ETH&LVDS Network Topology
Standard
RoofDsp_LVDS
HUD_LVDS
RHRSS_LVDS
LHRSS_LVDS
AVCamr_F1_LVDS AVCamr_F3_LVDS AVCamr_R_LVDS AVCamr_FLS_LVDS AVCamr_FRS_LVDS AVCamr_RLS_LVDS AVCamr_RRS_LVDS
Optional
 
 
Project
 
 
 
 
 
 
 
 
 
DVR_LVDS
IAM_ETH
IAM
 
 
 
Intergrate
 
 
 
 
AVM_LVDS
 
ZXD IPD
Status:                    Add 
A
                               Modified         ADAS_ETH
M
Diag_ETH
DLC
                               Carry Over
C
Connector Config: 
120
TR=120Ω Shielded
60
TR=60Ω Wireless
FLIDAR_ETH
TR=∞/Irrelevant
HDAVMCamr_F_LVDS HDAVMCamr_RH_LVDS
HDAVMCamr_R_LVDS HDAVMCamr_LH_LVDS
Connection Config: 
CnsoDsp_LVDS CoDrvrDsp_LVDS
LHZCU_ETH
DrvrDsp_LVDS
RHZCU_ETH RZCU_ETH
DMS_LVDS OMS_F_LVDS
OMS_R_LVDS
Ethernet_10G_base_T1
Ethernet_1000M_base_T1
Ethernet_100M_base_T1
Ethernet_10M_base_T1
CANFD
Local CANFD
CAN
Diagnostic_CAN
Local CAN
CoDrvrDsp LHZCU RHZCU RZCU
CnsoDsp DrvrDsp DMS OMS_F HDAVMCamr_LH
OMS_R HDAVMCamr_F HDAVMCamr_R HDAVMCamr_RH
FLIDAR
LIN
车内摄像头
车内前摄像头 车内后摄像头
高清环视摄像头_ 前
高清环视摄像头_后 高清环视摄像头_ 左 高清环视摄像头_右
中控大屏 仪表屏 副驾娱乐屏 前向激光雷达
Flexray
LVDS
智舱SOC 接口
Inftn
上汽零束保密文件，仅用于大众和上汽零束项目使用
A b b r e v i a t i on
C om po ne n t Lon gN a m e C hi n e s e N am e C om po ne n t Lo ng N am e C hi n es e N a me
L I N _ P EU
C A N
ZXD Zenith X Drive 舱算融合计算平台 EOPC Electric Oil Pump Controller 电子油泵控制器
LIN _LH ZC U
IPD Intelligent Pilot Device 智驾域控制器
IAM Intelligent Antenna Module 智联域控制器 OHC Over Head Control 顶控模块
DLC Data Link Connector (Diagnostic Connector) 诊断接口 RLSS Rain Light Solar Sensor 雨量灯光阳光传感器  
FDR Front Detection Radar 前向探测雷达 FWM Front Wiper Motor 前雨刮电机模块
FLIDAR Front Lidar 前激光雷达 DoorAmbtLamp_FL Door Ambient Lamp_FL 门饰板氛围灯-左前
LHA Left Headlamp Assembly 左前大灯总成 DoorAmbtLamp_FLM Door Ambient Lamp_FLM 门饰板氛围灯M-左前
RHA Right Headlamp Assembly 右前大灯总成 DoorAmbtLamp_RL Door Ambient Lamp_RL 门饰板氛围灯-左后
RZCU Rear Zonal Control Unit 后区域控制器 DoorAmbtLamp_RLM Door Ambient Lamp_RLM 门饰板氛围灯M-左后
SDM Sensing Diagnostic Module 安全气囊控制诊断模块 MapPcktAmbtLamp_FL Map Pokit Ambient Lamp_FL 地图袋氛围灯-左前
IBS Integrated Brake System 集成式制动系统 MapPcktAmbtLamp_RL Map Pokit Ambient Lamp_RL 地图袋氛围灯-左后
EPS Electric Power Steering 电动助力转向 CupholderAmbtLamp_LH Cupholder Ambient Lamp_LH 杯托氛围灯-左
RWSL Rear Wheel Steering Loacal 后轮转向 CupholderAmbtLamp_RH Cupholder Ambient Lamp_RH 杯托氛围灯-右
SCM Suspension Control Module 自适应悬架或主动悬架 CnsoAmbtLamp_LH Consol Ambient Lamp_LH 中央通道氛围灯-左
PEU Power Electric Unit 电力电子单元 CnsoAmbtLamp_RH Consol Ambient Lamp_RH 中央通道氛围灯-右
ECM Engine Control Module 发动机控制模块 CnsoAmbtLamp_LM Consol Ambient Lamp_LM 中央通道氛围灯-左中
LVBM Low Voltage Battery Module 低压电池模块 CnsoAmbtLamp_RM Consol Ambient Lamp_RM 中央通道氛围灯-右中
CCU Combined Charging Unit 高低压集成充电模块 TPMS Tire Pressure Monitoring System 胎压监测系统
ESS Energy Storage System 能量存储系统 FLSLMM Front Left Seat Lumbar And Massage Module 左前座椅腰托按摩模块 
ChrgrSkt Charger Socket 充电口 KickSnsr Kick Sensor 脚踢传感器
LHZCU Left Hand Zonal Control Unit 左区域控制器 LIN _RZC U
BPEPS Bluetooth Passive Entry Passive Start 蓝牙无钥匙进入和启动 ChrgngStaLamp Charing State Lamp 充电状态灯 
NFCAM Near Field Control Access Module NFC 进入模块 APTC Air PTC 空气加热器
NFCSM Near Field Control Strat Module NFC 启动模块 TailLampAsmblA_LH Tail Lamp Assembly A_LH 尾灯总成A_左
RRBLEA Rear Right Bluetooth Antenna 右后蓝牙天线 TailLampAsmblA_RH Tail Lamp Assembly A_RH 尾灯总成A_右
RLBLEA Rear Left Bluetooth Antenna 左后蓝牙天线 TailLampAsmblB_LH Tail Lamp Assembly B_LH 尾灯总成B_左
FRBLEA Front Right Bluetooth Antenna 右前蓝牙天线 TailLampAsmblB_RH Tail Lamp Assembly B_RH 尾灯总成B_右
FLBLEA Front Left Bluetooth Antenna 左前蓝牙天线 RLSLMM Rear Left Seat Lumbar And Massage Module 左后座椅腰托按摩模块
RHZCU Right Hand Zonal Control Unit 右区域控制器 RRSLMM Rear Right Seat Lumbar And Massage Module 右后座椅腰托按摩模块
EAC Electric Air Conditioning Compressor 电动空调压缩机（混动） 
LI N _Z X D
L I N _ R H Z C U MFL Multifunction lenkrad 方向盘开关
AIntnlTemSnsr Ambient Internal Temperature Sensor 舱内温度传感器 HODM Hands Off Detection Module 离手检测模块 
CF Cooling  Fridge 车载冰箱 DrvrDsp Drvr Ambient DrvrDsp_DrvrDsp 屏幕功能安全
IFM Intelligent fragrance module 香氛散发模块 RoofDsp Roof Ambient RoofDsp_RoofDsp 后排吸顶屏电机
UpIPAmbtLampA_LH Up IP Ambient Lamp A_LH 上仪表板氛围灯A-左 LAirVentVertMot Left Air Vent Vertical Motor 左侧出风口垂直扫风电机
UpIPAmbtLampB_LH Up IP Ambient Lamp B_LH 上仪表板氛围灯B-左 LAirVentHoztMot Left Air Vent Horizontal Motor 左侧出风口水平扫风电机       
UpIPAmbtLampA_RH Up IP Ambient Lamp A_RH 上仪表板氛围灯A-右 MidLAirVentVertMot Middle Left Air Vent Vertical Motor 中央左出风口垂直扫风电机   
DwnIPAmbtLampA_LH Down IP Ambient Lamp A_LH MidLAirVentHoztMot Middle Left Air Vent Horizontal Motor 中央左出风口水平扫风电机       
下仪表板氛围灯A-左
DwnIPAmbtLampA_RH Down IP Ambient Lamp A_RH MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
下仪表板氛围灯A-右
DwnIPAmbtLampB_RH Down IP Ambient Lamp B_RH MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
下仪表板氛围灯B-右
DoorAmbtLamp_FR Door Ambient Lamp_FR 门饰板氛围灯-右前 MidRAirVentHoztMot Middle Right Air Vent Horizontal Motor 中央右出风口水平扫风电机       
DoorAmbtLamp_FRM Door Ambient Lamp_FRM 门饰板氛围灯M-右前 RAirVentVertMot Right Air Vent Vertical Motor 右侧出风口垂直扫风电机
DoorAmbtLamp_RR Door Ambient Lamp_RR 门饰板氛围灯-右后 RAirVentHoztMot Right Air Vent Horizontal Motor 右侧出风口水平扫风电机       
L V D S
DoorAmbtLamp_RRM Door Ambient Lamp_RRM 门饰板氛围灯M-右后
MapPcktAmbtLamp_FR Map Pocket Ambient Lamp_FR LHRSS Left Hand Rear Smart Surface 后排智能表面_左
地图袋氛围灯-右前
MapPcktAmbtLamp_RR Map Pocket  Ambient Lamp_RR RHRSS Right Hand Rea Smart Surface 后排智能表面_右
地图袋氛围灯-右后
RoofAmbtLampA_LH Roof Ambient LampA_LH HUD Head Up Display 抬头显示
顶棚氛围灯A-左
RoofDsp Roof Display
RoofAmbtLampB_LH Roof Ambient LampB_LH 顶棚氛围灯B-左 后排吸顶屏
RoofAmbtLampC_LH Roof Ambient LampC_LH CnsoDsp Console Display 中控大屏
顶棚氛围灯C-左
RoofAmbtLampD_LH Roof Ambient LampD_LH 顶棚氛围灯D-左 DrvrDsp Driver Display 仪表屏
RoofAmbtLampA_RH Roof Ambient LampA_RH 顶棚氛围灯A-右 CoDrvrDsp CoDriver Display 副驾娱乐屏 
RoofAmbtLampB_RH Roof Ambient LampB_RH 顶棚氛围灯B-右 DMS Driver Monitor System 车内摄像头
RoofAmbtLampC_RH Roof Ambient LampC_RH OMS_F Occupancy Monitoring System_Front 车内前摄像头
顶棚氛围灯C-右
RoofAmbtLampD_RH Roof Ambient LampD_RH OMS_R Occupancy Monitoring System_Rear 车内后摄像头
顶棚氛围灯D-右
ESSClntPump ESSClnt Ambient ESSClntPump_ESSClntPum能p 量存储系统冷却水泵 AVCamr_F1 Around View Camera_Front1 前周视摄像头1
MulChnlVlv Mul Ambient ChnlVlv_MulChnlVlv AVCamr_F3 Around View Camera_Front3 前周视摄像头3
冷却系统多通阀
PEBClntPump1 PEBClnt Ambient PEBClntPump_PEBClntPum电p1驱动电子水泵 AVCamr_FLS Around View Camera_Front Left Side 左前侧周视摄像头 
AGS1 Active Grille Shutter 1 主动进气格栅_1 AVCamr_FRS Around View Camera_Front Right Side 右前侧周视摄像头 
ClntVlv Clnt Ambient ClntVlv_ClntVlv 三通阀 AVCamr_R Around View Camera_Rear 后周视摄像头 
AVCamr_RLS Around View Camera_Rear Left Side 
WtrPTCPump Wtr Ambient WtrPTCPump_WtrPTCPump HVPTC水泵 左后侧周视摄像头 
CoolngFan Coolng Ambient CoolngFan_CoolngFan 冷却风扇 AVCamr_RRS Around View Camera_Rear Right Side 右后侧周视摄像头 
Blwr_F Blower_F 前鼓风机 HDAVMCamr_F High Definition AVM Camera_F 高清环视摄像头_前 
FRSLMM Front Right Seat Lumbar And Massage Mod右ul前e 座椅腰托按摩模块 HDAVMCamr_LH High Definition AVM Camera_LH 高清环视摄像头_左 
LIN _EC M
HDAVMCamr_R High Definition AVM Camera_R 高清环视摄像头_后 
EnEleclMainWtrPump Engine Electrical Main Water Pump 发动机电子主水泵 HDAVMCamr_RH High Definition AVM Camera_RH 高清环视摄像头_右 
上汽零束保密文件，仅用于大众和上汽零束项目使用
Version History
序号 版本 修订日期 修改人 详细变更 
1 V0.1 2024-08-22 王众 First version
1、删除IPS 模块 
2、后排吸顶屏电机挂ZXD_LIN1
2 V0.2 2024-09-05 王众
3、取消HD 大灯模块 
4 、智驾方案待定
1、ITMS 不集成，LHZCU_LIN 6 节点 
3 V0.3 2024-09-13 王众
2、智驾方案更新
1、增加OMC 摄像头-备注DMC-OMC AGT2 阶段不实施
2、氛围灯AGT2 阶段不实施 
4 V0.4 2024-09-18 王众
3、删除充电小门LIN 节点 
4、删除泊车雷达CAN 节点，FDR 接BackupCANFD
1、标记UWB 钥匙及NFC ，HUD 阶段不实施 
2、新增OMS_R 摄像头 
3、调整HODM 及SecRawClngMntdScrn LIN 模块LIN 网段位置
5 V0.5 2024-10-14 王众
4、更改ADCU 名称为IPD 
5、TPMS AGT2 阶段实施 
6、左右座椅腰托AGT2 阶段不实施 
1、调整RHZCU_LIN6,LIN7 网段节点
6 V0.6 2024-10-18 王众
2、更改后排吸顶屏命名
1、增加后排smart surface 屏幕 LVDS 节点 
7 V0.7 2024-11-28 王众 2、增加氛围灯LIN 节点, 增加后尾灯LIN 节点,增加脚踢传感器LIN 节点，增加顶控OHC LIN 节点 
4、将高压加热器LIN 节点合并至RZCU_LIN1
1、香氛IFM 节点从连接RHZCU_LIN3 更改为ZXD_LIN3; 
2、增加电动出风口LIN 节点于ZXD_LIN4; 
3、增加舱内温度传感器AIntnlTemSnsrLIN 节点于RHZCU_LIN2; 
8 V0.8 2024-12-19 李茂亚
4、HODM 更改为直接ZXD_LIN1; 
5、删除LH Body CANFD 上UWBA 天线节点，增加LH Body CANFD 上RRBLEA 、RLBLEA 、FRBLEA 、
FLBLEA 蓝牙天线节点；
1 、笔误修订：MapPcktAmbtLamp_RL 节点重复，修订为MapPcktAmbtLamp_FR 及MapPcktAmbtLamp_RR ； 
2、笔误修订：尾灯模块节点名称更改，TailLampBsmblB_LH 更改为TailLampAsmblB_LH ，TailLampBsmblB_RH 更改
为TailLampAsmblB_RH ； 
3、按信号需求统一拓扑节点名称： 
DoorAmbLamp_FR 更改为DoorAmbtLamp_FR ；DoorAmbLamp_FRM 更改为DoorAmbtLamp_FRM ； 
9 升版至V1.0-PT 2025-01-24 李茂亚 DoorAmbLamp_RR 更改为DoorAmbtLamp_RR ；DoorAmbLamp_RRM 更改为DoorAmbtLamp_RRM ； 
DoorAmbLamp_FL 更改为DoorAmbtLamp_FL ；DoorAmbLamp_FLM 更改为DoorAmbtLamp_FLM ； 
DoorAmbLamp_RL 更改为DoorAmbtLamp_RL ；DoorAmbLamp_RLM 更改为DoorAmbtLamp_RLM ； 
电子油泵CCEOP 统一更改为EOPC ； 
车载冰箱CnsoFdge 统一名称更改为CF ； 
4、香氛改为连ZXD_LIN4;
1、香氛IFM 节点从ZXD_LIN4 更改为接RHZCU_LIN3;
2、氛围灯配置变更，需取消顶棚氛围灯节点：RoofAmbtLampD_LH 及RoofAmbtLampD_RH ，功能PVS 实
施，新增Note ：PVS 将取消顶棚氛围灯左右D 节点；
氛围灯配置变更：UpIPAmbtLamp_RH 节点变更为：UpIPAmbtLampA_LH ，UpIPAmbtLampB_LH ，
UpIPAmbtLampA_RH ，增加Note ：上仪表氛围灯拆分，硬件PT 实施，功能PVS 实施；
10 V2.0-PT 2025-02-21 李茂亚
氛围灯配置变更：新增console 氛围灯节点：CnsoAmbtLamp_LM 及CnsoAmbtLamp_RM ，新增Note：中央
通道氛围灯新增LM、RM节点，硬件PT实施，功能PVS实施；
3、增加氛围灯各节点中文命名，FLIDAR 中文命名前向激光雷达；
4、更改副驾屏CoDrvrDsp 、后排吸顶屏RoofDsp 为选配节点；
5、拓扑各节点中文名称拉齐更新，Abbreviation 信息拉齐更新；
上汽零束保密文件，仅用于大众和上汽零束项目使用

---

## PDF: 动采_AF\F\拓扑图\大众B车 6S PVS+5S PT Network Topology  20250529 V3.1-发布.pdf

SVW PVS B 车 Network Topology-6S 、5S 
Version 3.1
Li Maoya
上汽零束保密文件
仅用于大众和上汽零束项目使用
SVW B-SUV 6S+5S 
诊断口 智能网联控制器
 ETH&CAN Network Topology
DLC IAM
120
Diagnostic CAN Diag_ETH Connected CANFD IAM_ETH
60 120
ADAS_ETH
ICC
120
RZCU CANFD
Standard
ICM
120 120
BackUp CANFD
AMP
ZXD
IPD
Optional
120
120
120
 
智驾控制单元
 
 
Project
 
 
 
 
HeadLighting
 
RHZCU_ETH
 LHZCU_ETH
Backbone CANFD
CANFD
 
 
 
ADAS Local CANFD
 
FLIDAR_ETH
 
RZCU_ETH
 
Intergrate
 
 
 
 
 
120
Status:                    AddA 
                               Modified         
M
FLIDAR FDR
                               Carry OverC
前雷达
前向激光雷达
Connector Config: 
120
120
仅 6 S 车 型
120
TR=120Ω Shielded
BCM ITMS
BCM SCU
IMU BCM
120
Chassis CANFD
60
Z
TR=60Ω Wireless
RRSM
FRDCM
FLDCM
RF SMLS
120
Safety CANFD
RZCU
LHZCU RHZCU
TR=∞/Irrelevant
RLSM
RRDCM
RLDCM EASC
PLCM
FRSM IEC
IEC
FLSM
Connection Config: 
120
120
120 120 120 120
Ethernet_10G_base_T1
Ethernet_1000M_base_T1
RH Body CAN
Ethernet_100M_base_T1
PowerTrain CANFD Extended Range CANFD PowerTrain Extended CAN LH Body CANFD
Suspension CANFD
Ethernet_10M_base_T1
CANFD
Local CANFD
RHA
CAN
120
BPEPS
Diagnostic_CAN
兼容UWB
Local CAN
右前大灯模块
120
120
数字钥匙主模块
EAC
120
120
IBS
SCM PEU
SDM
LIN
电动空调压缩机
集成式制动系统 自适应悬架
NFCSM
电力电子单元
Flexray
安全气囊控制诊断模块
集成MPWC
LVDS
120
NFC 启动模块 LHA
EPS
120
ECM
左前大灯模块
电动助力转向
NFCAM
集成CMM
智舱SOC 接口
Inftn
发动机控制模块
NFC 进入模块
RWSL
后轮转向 RRBLEA
LVBM
仅 6 S 车 型
右后蓝牙天线
低压电源管理
RLBLEA
左后蓝牙天线
CCU
高低压集成充电模块
FRBLEA
右前蓝牙天线
120 120
TC
FLBLEA
后电机
左前蓝牙天线
ETCM
ESS
120
120
OffBdChrgr CAN
ChrgrSkt
电子收费系统
能量储能系统
充电口
上汽零束保密文件
仅用于大众和上汽零束项目使用
SVW B-SUV 6S+5S 
LIN Network Topology
DTSM_FR FRSASW( 座椅调节开关)
Standard
DTSM_RR
RHZCU RZCU
DOTSM_FR
DOTSM_RR
Optional
RHZCU_LIN5
RHZCU_LIN6
RHZCU_LIN4
RHZCU_LIN8
RHZCU_LIN3 RHZCU_LIN7
RZCURZCU_LIN3_LIN3 RZCURZCU_LIN4_LIN4
RZCU_LIN2
RHZCU_LIN2
RZCU_LIN1
 
 
Project
 
 
RRSLMM
ChrgngStaLamp RLSLMM
TailLampAsmblA_LH
CF UpIPAmbtLampA_LH DoorAmbtLamp_FR RoofAmbtLampA_LH ESSClntPump FRSLMM
 
ClntVlv
AIntnlTemSnsr
 
 
 
 
 
顶棚氛围灯A- 左
三通阀
充电状态灯 
门饰板氛围灯- 右前 能量存储系统冷却水泵 右后座椅腰托按摩模块
 车载冰箱 尾灯总成A_左 左后座椅腰托按摩模块
上仪表板氛围灯A- 左
右前座椅腰托按摩模块
 
舱内温度传感器
 
 
Intergrate
 
 
仅 6 S + 5 S 高 配 车 型
仅 6 S + 5 S 高 配 车 型
 
RoofAmbtLampB_LH MulChnlVlv
WtrPTCPump
DoorAmbtLamp_FRM
 UpIPAmbtLampB_LH
IFM
 
TailLampAsmblA_RH  
APTC TailLampAsmblA_RH  
DTSP_RR
冷却系统多通阀
HVPTC 水泵
Status:                    Add 顶棚氛围灯B- 左
A
门饰板氛围灯M- 右前
上仪表板氛围灯B- 左
香氛散发模块
                               Modified         
M
尾灯总成A_右
空气加热器
右后门触控开关面板
                               Carry Over
C
DoorAmbtLamp_RR
RoofAmbtLampC_LH
仅 5 S 低 配 车 型
UpIPAmbtLampA_RH
CoolngFan
PEBClntPump1
仅 6 S 车 型
TailLampBsmblB_RH
TailLampAsmblB_LH
Connector Config: 
门饰板氛围灯- 右后
上仪表板氛围灯A- 右 顶棚氛围灯C-左 冷却风扇
电驱动电子水泵
120
TR=120Ω Shielded
尾灯总成B_ 左
60
TR=60Ω Wireless
DwnIPAmbtLampA_LH
DoorAmbtLamp_RRM
RoofAmbtLampA_RH
AGS1
Blwr_F
TR=∞/Irrelevant
下仪表板氛围灯A- 左
门饰板氛围灯M- 右后
顶棚氛围灯A- 右
TailLampAsmblB_RH
主动进气格栅_1 前鼓风机
Connection Config: 
Ethernet_10G_base_T1
尾灯总成B_ 右
DwnIPAmbtLampA_RH
RoofAmbtLampB_RH
Ethernet_1000M_base_T1
Ethernet_100M_base_T1
Ethernet_10M_base_T1 顶棚氛围灯B- 右
下仪表板氛围灯A- 右
CANFD
Local CANFD
RoofAmbtLampC_RH
DwnIPAmbtLampB_RH
CAN
Diagnostic_CAN
顶棚氛围灯C-右
Local CAN
下仪表板氛围灯B- 右
仅 6 S 车 型
LIN
Flexray
LVDS
智舱SOC 接口
Inftn
Z
ZXD ECM
LHZCU PEU
ZXD_LIN1 ECM_LIN1
ZXD_LIN4
ZXD_LIN2
LHZCU_LIN2 PEU_LIN1
LHZCU_LIN3
LHZCU_LIN8
LHZCU_LIN4
EnEleclMainWtrPump
EOPC
LAirVentVertMot
FLSLMM
CupholderAmbtLamp_LH
TPMS
OHC
DoorAmbtLamp_FL
左侧出风口垂直扫风电机
电子油泵控制器
发动机电子主水泵
杯托氛围灯- 左
门饰板氛围灯-左前
顶控模块
胎压传感器 左前座椅腰托按摩模块 
LAirVentHoztMot
SWS
DrvrDsp
RLSS
左侧出风口水平扫风电机     
CupholderAmbtLamp_RH
DoorAmbtLamp_FLM
KickSnsr
方向盘开关
仪表屏
阳光雨量传感器
门饰板氛围灯M- 左前 杯托氛围灯- 右
MidLAirVentVertMot
脚踢传感器
N o t e ： 屏 幕 功 能 安 全 接 口 预 留
中央左出风口垂直扫风电机  
FWM
DoorAmbtLamp_RL CnsoAmbtLamp_LH
HODM
RoofDsp
MidLAirVentHoztMot
DTSP_RL
前雨刮电机模块
后排吸顶屏电机
门饰板氛围灯-左后 中央通道氛围灯-左
离手检测模块
中央左出风口水平扫风电机  
左后门触控开关面板
仅 6 S 车 型
仅 5 S 低 配 车 型
MidRAirVentVertMot
DoorAmbtLamp_RLM
CnsoAmbtLamp_RH
中央右出风口垂直扫风电机 
门饰板氛围灯M- 左后
中央通道氛围灯- 右
MMiidRAdRAiirVrVentHoztMotentHoztMot
CnsoAmbtLamp_LM
中央右出风口水平扫风电机 
中央通道氛围灯- 左中
RAirVentVertMot
右侧出风口垂直扫风电机
CnsoAmbtLamp_RM
RAirVentHoztMot
中央通道氛围灯- 右中
右侧出风口水平扫风电机
电动出风口
上汽零束保密文件
仅用于大众和上汽零束项目使用
右前侧周视摄像头 左后侧周视摄像头 右后侧周视摄像头 
前周视摄像头3 后周视摄像头
左前侧周视摄像头 
前周视摄像头1
抬头显示 后排吸顶屏
后排智能表面_左 后排智能表面_右
SVW B-SUV 6S+5S 
AVCamr_F3 AVCamr_R AVCamr_FLS AVCamr_FRS AVCamr_RLS AVCamr_RRS
AVCamr_F1
HUD
RoofDsp
LHRSS
RHRSS
ETH&LVDS Network Topology
仅 6 S 车 型
Standard
RoofDsp_LVDS
HUD_LVDS
RHRSS_LVDS
LHRSS_LVDS
AVCamr_F1_LVDS AVCamr_F3_LVDS AVCamr_R_LVDS AVCamr_FLS_LVDS AVCamr_FRS_LVDS AVCamr_RLS_LVDS AVCamr_RRS_LVDS
Optional
 
 
Project
 
 
 
 
 
 
 
 
 
DVR_LVDS
IAM_ETH
IAM
 
 
 
Intergrate
 
 
 
 
AVM_LVDS
 
ZXD IPD
Status:                    Add 
A
                               Modified         ADAS_ETH
M
Diag_ETH
DLC
                               Carry Over
C
Connector Config: 
120
TR=120Ω Shielded
60
TR=60Ω Wireless
FLIDAR_ETH
TR=∞/Irrelevant
HDAVMCamr_F_LVDS HDAVMCamr_RH_LVDS
HDAVMCamr_R_LVDS HDAVMCamr_LH_LVDS
Connection Config: 
CnsoDsp_LVDS CoDrvrDsp_LVDS
LHZCU_ETH
DrvrDsp_LVDS
RHZCU_ETH RZCU_ETH
DMS_LVDS OMS_F_LVDS
OMS_R_LVDS
Ethernet_10G_base_T1
Ethernet_1000M_base_T1
Ethernet_100M_base_T1
Ethernet_10M_base_T1
CANFD
Local CANFD
CAN
Diagnostic_CAN
Local CAN
CoDrvrDsp LHZCU RHZCU RZCU
CnsoDsp DrvrDsp DMS OMS_F HDAVMCamr_LH
OMS_R HDAVMCamr_F HDAVMCamr_R HDAVMCamr_RH
FLIDAR
LIN
车内摄像头
车内前摄像头 车内后摄像头
高清环视摄像头_ 前
高清环视摄像头_后 高清环视摄像头_ 左 高清环视摄像头_右
中控大屏 仪表屏 副驾娱乐屏 前向激光雷达
Flexray
仅 6 S 车 型
LVDS
仅 6 S 车 型
智舱SOC 接口
Inftn
上汽零束保密文件
仅用于大众和上汽零束项目使用
A b b r e v i a t i on
C om po ne n t Lon gN a m e C hi n e s e N am e C om po ne n t Lo ng N am e C hi n es e N a me
L I N _ P EU
C A N
ZXD Zenith X Drive 舱算融合计算平台 EOPC Electric Oil Pump Controller 电子油泵控制器
IPD Intelligent Pilot Device 智驾域控制器 LIN _LH ZC U
IAM Intelligent Antenna Module 智联域控制器 OHC Over Head Control 顶控模块
DLC Data Link Connector (Diagnostic Connector) 
诊断接口 RLSS Rain Light Solar Sensor 雨量灯光阳光传感器  
FDR Front Detection Radar 前向探测雷达 FWM Front Wiper Motor 前雨刮电机模块
FLIDAR Front Lidar 前激光雷达 DoorAmbtLamp_FL Door Ambient Lamp_FL 门饰板氛围灯-左前
LHA Left Headlamp Assembly 左前大灯总成 DoorAmbtLamp_FLM Door Ambient Lamp_FLM 门饰板氛围灯M-左前
RHA Right Headlamp Assembly 右前大灯总成 DoorAmbtLamp_RL Door Ambient Lamp_RL 门饰板氛围灯-左后
RZCU Rear Zonal Control Unit 后区域控制器 DoorAmbtLamp_RLM Door Ambient Lamp_RLM 门饰板氛围灯M-左后
SDM Sensing Diagnostic Module 安全气囊控制诊断模块 CupholderAmbtLamp_LH Cupholder Ambient Lamp_LH 杯托氛围灯-左
IBS Integrated Brake System 集成式制动系统 CupholderAmbtLamp_RH Cupholder Ambient Lamp_RH 杯托氛围灯-右
EPS Electric Power Steering 电动助力转向 CnsoAmbtLamp_LH Consol Ambient Lamp_LH 中央通道氛围灯-左
RWSL Rear Wheel Steering Loacal 后轮转向 CnsoAmbtLamp_RH Consol Ambient Lamp_RH 中央通道氛围灯-右
SCM Suspension Control Module 自适应悬架或主动悬架 CnsoAmbtLamp_LM Consol Ambient Lamp_LM 中央通道氛围灯-左中
PEU Power Electric Unit 电力电子单元 CnsoAmbtLamp_RM Consol Ambient Lamp_RM 中央通道氛围灯-右中
ECM Engine Control Module 发动机控制模块 TPMS Tire Pressure Monitoring System 胎压监测系统
LVBM Low Voltage Battery Module 低压电池模块 FLSLMM Front Left Seat Lumbar And Massage Module 左前座椅腰托按摩模块 
CCU Combined Charging Unit 高低压集成充电模块 KickSnsr Kick Sensor 脚踢传感器
ESS Energy Storage System 能量存储系统 DTSP_RL Door Touch Switch Panel_RL 左后门触控开关面板
ChrgrSkt Charger Socket 充电口 LIN _RZC U
LHZCU Left Hand Zonal Control Unit 左区域控制器 ChrgngStaLamp Charing State Lamp 充电状态灯 
BPEPS Bluetooth Passive Entry Passive Start 蓝牙无钥匙进入和启动 APTC Air PTC 空气加热器
NFCAM Near Field Control Access Module NFC 进入模块 TailLampAsmblA_LH Tail Lamp Assembly A_LH 尾灯总成A_左
NFCSM Near Field Control Strat Module NFC 启动模块 TailLampAsmblA_RH Tail Lamp Assembly A_RH 尾灯总成A_右
RRBLEA Rear Right Bluetooth Antenna 右后蓝牙天线 TailLampAsmblB_LH Tail Lamp Assembly B_LH 尾灯总成B_左
RLBLEA Rear Left Bluetooth Antenna 左后蓝牙天线 TailLampAsmblB_RH Tail Lamp Assembly B_RH 尾灯总成B_右
FRBLEA Front Right Bluetooth Antenna 右前蓝牙天线 RLSLMM Rear Left Seat Lumbar And Massage Module 左后座椅腰托按摩模块
FLBLEA Front Left Bluetooth Antenna 左前蓝牙天线 RRSLMM Rear Right Seat Lumbar And Massage Module 右后座椅腰托按摩模块
RHZCU Right Hand Zonal Control Unit 右区域控制器 LI N _Z X D
EAC Electric Air Conditioning Compressor 电动空调压缩机（混动） SWS Steering Wheel Switch 方向盘开关
ETCM Electronic Toll Collection 电子收费系统 HODM Hands Off Detection Module 离手检测模块 
L I N _ R H Z C U DrvrDsp Drvr Ambient DrvrDsp_DrvrDsp 屏幕功能安全
AIntnlTemSnsr Ambient Internal Temperature Sensor 舱内温度传感器 RoofDsp Roof Ambient RoofDsp_RoofDsp 后排吸顶屏电机
CF Consle Fridge 车载冰箱 LAirVentVertMot Left Air Vent Vertical Motor 左侧出风口垂直扫风电机
IFM Intelligent fragrance module 香氛散发模块 LAirVentHoztMot Left Air Vent Horizontal Motor 左侧出风口水平扫风电机       
UpIPAmbtLampA_LH Up IP Ambient Lamp A_LH 上仪表板氛围灯A-左 MidLAirVentVertMot Middle Left Air Vent Vertical Motor 中央左出风口垂直扫风电机   
UpIPAmbtLampB_LH Up IP Ambient Lamp B_LH MidLAirVentHoztMot Middle Left Air Vent Horizontal Motor 中央左出风口水平扫风电机       
上仪表板氛围灯B-左
UpIPAmbtLampA_RH Up IP Ambient Lamp A_RH 上仪表板氛围灯A-右 MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
DwnIPAmbtLampA_LH Down IP Ambient Lamp A_LH 下仪表板氛围灯A-左 MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
DwnIPAmbtLampA_RH Down IP Ambient Lamp A_RH 下仪表板氛围灯A-右 MidRAirVentHoztMot Middle Right Air Vent Horizontal Motor 中央右出风口水平扫风电机       
DwnIPAmbtLampB_RH Down IP Ambient Lamp B_RH RAirVentVertMot Right Air Vent Vertical Motor 右侧出风口垂直扫风电机
下仪表板氛围灯B-右
DoorAmbtLamp_FR Door Ambient Lamp_FR RAirVentHoztMot Right Air Vent Horizontal Motor 右侧出风口水平扫风电机       
门饰板氛围灯-右前
DoorAmbtLamp_FRM Door Ambient Lamp_FRM L V D S
门饰板氛围灯M-右前
DoorAmbtLamp_RR Door Ambient Lamp_RR 门饰板氛围灯-右后 LHRSS Left Hand Rear Smart Surface 后排智能表面_左
DoorAmbtLamp_RRM Door Ambient Lamp_RRM 门饰板氛围灯M-右后 RHRSS Right Hand Rea Smart Surface 后排智能表面_右
HUD
RoofAmbtLampA_LH Roof Ambient LampA_LH 顶棚氛围灯A-左 Head Up Display 抬头显示
RoofAmbtLampB_LH Roof Ambient LampB_LH RoofDsp Roof Display 后排吸顶屏
顶棚氛围灯B-左
RoofAmbtLampC_LH Roof Ambient LampC_LH CnsoDsp Console Display 中控大屏
顶棚氛围灯C-左
RoofAmbtLampA_RH Roof Ambient LampA_RH DrvrDsp Driver Display 仪表屏
顶棚氛围灯A-右
RoofAmbtLampB_RH Roof Ambient LampB_RH 顶棚氛围灯B-右 CoDrvrDsp CoDriver Display 副驾娱乐屏 
RoofAmbtLampC_RH Roof Ambient LampC_RH 顶棚氛围灯C-右 DMS Driver Monitor System 车内摄像头
ESSClntPump ESSClnt Ambient ESSClntPump_ESSClntPum能p 量存储系统冷却水泵 OMS_F Occupancy Monitoring System_Front 车内前摄像头
MulChnlVlv Mul Ambient ChnlVlv_MulChnlVlv 冷却系统多通阀 OMS_R Occupancy Monitoring System_Rear 车内后摄像头
PEBClntPump1 PEBClnt Ambient PEBClntPump_PEBClntPum电p1驱动电子水泵 AVCamr_F1 Around View Camera_Front1 前周视摄像头1
AVCamr_F3 Around View Camera_Front3 
AGS1 Active Grille Shutter 1 主动进气格栅_1 前周视摄像头3
ClntVlv Clnt Ambient ClntVlv_ClntVlv 三通阀 AVCamr_FLS Around View Camera_Front Left Side 左前侧周视摄像头 
WtrPTCPump Wtr Ambient WtrPTCPump_WtrPTCPump HVPTC水泵 AVCamr_FRS Around View Camera_Front Right Side 右前侧周视摄像头 
CoolngFan Coolng Ambient CoolngFan_CoolngFan 冷却风扇 AVCamr_R Around View Camera_Rear 后周视摄像头 
AVCamr_RLS Around View Camera_Rear Left Side 
Blwr_F Blower_F 前鼓风机 左后侧周视摄像头 
FRSLMM Front Right Seat Lumbar And Massage Mod右ul前e 座椅腰托按摩模块 AVCamr_RRS Around View Camera_Rear Right Side 右后侧周视摄像头 
DTSP_RR Door Touch Switch Panel_RR 右后门触控开关面板 HDAVMCamr_F High Definition AVM Camera_F 高清环视摄像头_前 
LIN _EC M HDAVMCamr_LH High Definition AVM Camera_LH 高清环视摄像头_左 
HDAVMCamr_R High Definition AVM Camera_R 
EnEleclMainWtrPump Engine Electrical Main Water Pump 发动机电子主水泵 高清环视摄像头_后 
HDAVMCamr_RH High Definition AVM Camera_RH 高清环视摄像头_右 
上汽零束保密文件
仅用于大众和上汽零束项目使用
Version History
序号 版本 修订日期 修改人 详细变更 
1 V0.1 2024-08-22 王众 First version
1、删除IPS 模块 
2、后排吸顶屏电机挂ZXD_LIN1
2 V0.2 2024-09-05 王众
3、取消HD 大灯模块 
4、智驾方案待定
1、ITMS 不集成，LHZCU_LIN 6 节点 
3 V0.3 2024-09-13 王众
2、智驾方案更新
1、增加OMC 摄像头- 备注DMC-OMC AGT2 阶段不实施
2、氛围灯AGT2 阶段不实施 
4 V0.4 2024-09-18 王众
3、删除充电小门LIN 节点 
4、删除泊车雷达CAN 节点，FDR 接BackupCANFD
1、标记UWB 钥匙及NFC ，HUD 阶段不实施 
2、新增OMS_R 摄像头 
3、调整HODM 及SecRawClngMntdScrn LIN 模块LIN 网段位置
5 V0.5 2024-10-14 王众
4、更改ADCU 名称为IPD 
5、TPMS AGT2 阶段实施 
6、左右座椅腰托AGT2 阶段不实施 
1、调整RHZCU_LIN6,LIN7 网段节点
6 V0.6 2024-10-18 王众
2、更改后排吸顶屏命名
1、增加后排smart surface 屏幕 LVDS 节点 
7 V0.7 2024-11-28 王众 2、增加氛围灯LIN 节点,增加后尾灯LIN 节点,增加脚踢传感器LIN 节点，增加顶控OHC LIN 节点 
4、将高压加热器LIN 节点合并至RZCU_LIN1
1、香氛IFM 节点从连接RHZCU_LIN3 更改为ZXD_LIN3; 
2、增加电动出风口LIN 节点于ZXD_LIN4; 
3、增加舱内温度传感器AIntnlTemSnsrLIN 节点于RHZCU_LIN2; 
8 V0.8 2024-12-19 李茂亚
4、HODM 更改为直接ZXD_LIN1; 
5、删除LH Body CANFD 上UWBA 天线节点，增加LH Body CANFD 上RRBLEA 、RLBLEA 、FRBLEA 、
FLBLEA 蓝牙天线节点；
1、笔误修订：MapPcktAmbtLamp_RL 节点重复，修订为MapPcktAmbtLamp_FR 及MapPcktAmbtLamp_RR ； 
2、笔误修订：尾灯模块节点名称更改，TailLampBsmblB_LH 更改为TailLampAsmblB_LH ，TailLampBsmblB_RH 更改
为TailLampAsmblB_RH ； 
3、按信号需求统一拓扑节点名称： 
DoorAmbLamp_FR 更改为DoorAmbtLamp_FR ；DoorAmbLamp_FRM 更改为DoorAmbtLamp_FRM ； 
DoorAmbLamp_RR 更改为DoorAmbtLamp_RR ；DoorAmbLamp_RRM 更改为DoorAmbtLamp_RRM ； 
9 升版至V1.0-PT 2025-01-24 李茂亚
DoorAmbLamp_FL 更改为DoorAmbtLamp_FL ；DoorAmbLamp_FLM 更改为DoorAmbtLamp_FLM ； 
DoorAmbLamp_RL 更改为DoorAmbtLamp_RL ；DoorAmbLamp_RLM 更改为DoorAmbtLamp_RLM ； 
电子油泵CCEOP 统一更改为EOPC ； 
车载冰箱CnsoFdge 统一名称更改为CF ； 
4、香氛改为连ZXD_LIN4;
1、香氛IFM 节点从ZXD_LIN4 更改为接RHZCU_LIN3;
2、氛围灯配置变更，需取消顶棚氛围灯节点：RoofAmbtLampD_LH 及RoofAmbtLampD_RH ，功能PVS 实
施，新增Note ：PVS 将取消顶棚氛围灯左右D 节点；
氛围灯配置变更：UpIPAmbtLamp_RH 节点变更为：UpIPAmbtLampA_LH ，UpIPAmbtLampB_LH ，
UpIPAmbtLampA_RH ，增加Note ：上仪表氛围灯拆分，硬件PT 实施，功能PVS 实施；
10 V2.0-PT 2025-02-21 李茂亚
氛围灯配置变更：新增console 氛围灯节点：CnsoAmbtLamp_LM 及CnsoAmbtLamp_RM ，新增 Note：中央
通道氛围灯新增LM、RM节点，硬件PT实施，功能PVS实施；
3、增加氛围灯各节点中文命名，FLIDAR 中文命名前向激光雷达；
4、更改副驾屏CoDrvrDsp 、后排吸顶屏RoofDsp 为选配节点；
5、拓扑各节点中文名称拉齐更新，Abbreviation 信息拉齐更新；
1、增加ETC 节点，接LH Body CANFD ； 
2、拉齐氛围灯配置信息，删除氛围灯RoofAmbtLampD_LH 及RoofAmbtLampD_RH 节点及氛围灯实施基线
11 V2.1-PVS 2025-02-28 李茂亚
Note 信息； 
3、方向盘开关名称由MFL 统一为SWS ； 
1、ETC 节点命名更新为ETCM ；
2、地图袋氛围灯改为白灯直驱方案，拓扑取消地图袋氛围灯节点：MapPcktAmbtLamp_FL 、
MapPcktAmbtLamp_RL 、MapPcktAmbtLamp_RR 、MapPcktAmbtLamp_FR.
3、5S 、6S 拓扑共版，增加6S、5S配置差异节点备注；
4、更新控制器清单；
5、新增DTSP_RL 左后门触控开关面板，接LHZCU_LIN8;
6、新增DTSP_RR 右后门触控开关面板，接RHZCU_LIN8;
V3.0 5S 对比6S 配置差异如下：
12 6S-PVS 20250409 李茂亚 a 、无前向激光雷达FLIDAR ；
5S-PT b、无RWSL 后轮转向；
 c 、无APTC ；
 d、无后排吸顶屏电机RoofDsp ；
 e 、新增DTSP_RL 左后门触控开关面板;
 f 、新增DTSP_RR 右后门触控开关面板;
 g、无OMS_R 车内后摄像头，OMS_F 为选配；
 h、无顶棚氛围灯；
 i 、无后排座椅腰托按摩模块RLSLMM 、RRSLMM ；
1、RRSLMM 及RLSLMM 模块配置备注更新，5S车型低配取消后排座椅腰托按摩模块，高配保留；
V3.1 
13 6S-PVS 20250416 李茂亚
5S-PT
上汽零束保密文件
仅用于大众和上汽零束项目使用

---

## PDF: 动采_AF\F\拓扑图\大众B车 6S PVS+5S PT Network Topology  20250710 V3.2-外发.pdf

SVW PVS B 车 Network Topology-6S 、5S 
Version 3.2
Li Maoya
上汽零束保密文件
仅用于大众和上汽零束项目使用
SVW B-SUV 6S+5S 
诊断口 智能网联控制器
 ETH&CAN Network Topology
DLC IAM
120
Diagnostic CAN Diag_ETH Connected CANFD IAM_ETH
60 120
ADAS_ETH
ICC
120
RZCU CANFD
Standard
ICM
120 120
BackUp CANFD
AMP
ZXD
IPD
Optional
120
120
120
 
智驾控制单元
 
 
Project
 
 
 
 
HeadLighting
 
RHZCU_ETH
 LHZCU_ETH
Backbone CANFD
CANFD
 
 
 
ADAS Local CANFD
 
FLIDAR_ETH
 
RZCU_ETH
 
Intergrate
 
 
 
 
 
120
Status:                    AddA 
                               Modified         
M
FLIDAR FDR
                               Carry OverC
前雷达
前向激光雷达
Connector Config: 
120 120
120
TR=120Ω Shielded
BCM ITMS
BCM SCU
IMU BCM
120
Chassis CANFD
60
TR=60Ω Wireless
RRSM
FRDCM
FLDCM
RF SMLS
120
Safety CANFD
RZCU
LHZCU RHZCU
TR=∞/Irrelevant
RLSM
RRDCM
RLDCM EASC
PLCM
FRSM IEC
IEC
FLSM
Connection Config: 
120
120
120 120 120 120
Ethernet_10G_base_T1
Ethernet_1000M_base_T1
Z
RH Body CAN
Ethernet_100M_base_T1
PowerTrain CANFD Extended Range CANFD PowerTrain Extended CAN LH Body CANFD
Suspension CANFD
Ethernet_10M_base_T1
CANFD
Local CANFD
RHA
CAN
120
BPEPS
Diagnostic_CAN
兼容UWB
Local CAN
右前大灯模块
120
120
数字钥匙主模块
EAC
120
120
IBS
SCM PEU
SDM
LIN
电动空调压缩机
集成式制动系统 自适应悬架
NFCSM
电力电子单元
Flexray
安全气囊控制诊断模块
集成MPWC
LVDS
120
NFC 启动模块 LHA
EPS
120
ECM
左前大灯模块
电动助力转向
NFCAM
集成CMM
智舱SOC 接口
Inftn
发动机控制模块
NFC 进入模块
RWSL
后轮转向 RRBLEA
LVBM
仅 6 S 车 型
右后蓝牙天线
低压电源管理
RLBLEA
左后蓝牙天线
CCU
高低压集成充电模块
FRBLEA
右前蓝牙天线
120 120
TC
FLBLEA
后电机
左前蓝牙天线
Note ：PT 阶段硬件
ETCM
ESS
预埋，功能PVS 实施 ；
120
120
OffBdChrgr CAN
ChrgrSkt
电子收费系统
能量储能系统
充电口
Note ：仅6S 高配车型，
FDM
PT 阶段硬件预埋， 
功能0S实施；
防炫目流媒体内后视镜
TPMS
胎压监测系统
上汽零束保密文件
仅用于大众和上汽零束项目使用
SVW B-SUV 6S+5S 
LIN Network Topology
DTSM_FR FRSASW( 座椅调节开关)
Standard
DTSM_RR
RHZCU
RZCU
DOTSM_FR
DOTSM_RR
Optional
RHZCU_LIN5
RHZCU_LIN6
RHZCU_LIN4
RHZCU_LIN8
RHZCU_LIN3 RHZCU_LIN7
RZCRZCUU_LIN3_LIN3 RZCRZCUU_LIN4_LIN4
RHZCU_LIN2
RZCU_LIN2
RZCU_LIN1
 
 
Project
Local_LIN
 
 
CF UpIPAmbtLampA_LH DoorAmbtLamp_FR RoofAmbtLampA_LH ESSClntPump FRSLMM
 ChrgngStaLamp RRSLMM
RLSLMM
TailLampAsmblA_LH
ClntVlv FRSCMM
AIntnlTemSnsr
 
 
 
 
 
右前座椅坐垫按摩模块
顶棚氛围灯A- 左 三通阀
门饰板氛围灯- 右前 能量存储系统冷却水泵
 车载冰箱 充电状态灯 
上仪表板氛围灯A- 左 右后座椅腰托按摩模块
尾灯总成A_左 左后座椅腰托按摩模块
右前座椅腰托按摩模块
 
舱内温度传感器
 
 仅 6 S 高 配 ， 座 椅 域 内 控 制 器
Intergrate
 
 
仅 6 S + 5 S 高 配 车 型
 
仅 6 S + 5 S 高 配 车 型
RoofAmbtLampB_LH MulChnlVlv
WtrPTCPump
DoorAmbtLamp_FRM
 UpIPAmbtLampB_LH
IFM
 
TailLampAsmblA_RH  
APTC TailLampAsmblA_RH  
DTSP_RR
冷却系统多通阀
HVPTC 水泵
Status:                    Add 顶棚氛围灯B- 左
A
门饰板氛围灯M- 右前
上仪表板氛围灯B- 左
香氛散发模块
                               Modified         
M
尾灯总成A_右
空气加热器
右后门触控开关面板
                               Carry OverC
DoorAmbtLamp_RR
RoofAmbtLampC_LH
仅 5 S 低 配 车 型
UpIPAmbtLampA_RH
CoolngFan
PEBClntPump1
仅 6 S 车 型
TailLampBsmblB_RH
Connector Config: 
TailLampAsmblB_LH
门饰板氛围灯- 右后
上仪表板氛围灯A-右 顶棚氛围灯C-左 冷却风扇
电驱动电子水泵
120
TR=120Ω Shielded
尾灯总成B_ 左
60
TR=60Ω Wireless
DwnIPAmbtLampA_LH
DoorAmbtLamp_RRM
RoofAmbtLampA_RH
AGS1
Blwr_F
TR=∞/Irrelevant
下仪表板氛围灯A-左
门饰板氛围灯M- 右后
顶棚氛围灯A-右
主动进气格栅_1 前鼓风机 TailLampAsmblB_RH
Connection Config: 
Ethernet_10G_base_T1
DwnIPAmbtLampA_RH 尾灯总成B_ 右
RoofAmbtLampB_RH
Ethernet_1000M_base_T1
Ethernet_100M_base_T1
Ethernet_10M_base_T1 顶棚氛围灯B- 右
下仪表板氛围灯A-右
CANFD
Local CANFD
RoofAmbtLampC_RH
DwnIPAmbtLampB_RH
CAN
Diagnostic_CAN
顶棚氛围灯C-右
Local CAN
下仪表板氛围灯B- 右
仅 6 S 车 型
LIN
Flexray
LVDS
智舱SOC 接口
Inftn
Z
ZXD ECM
LHZCU PEU
ZXD_LIN1 ECM_LIN1
ZXD_LIN4
ZXD_LIN2
LHZCU_LIN2 PEU_LIN1
LHZCU_LIN8
LHZCU_LIN4
EnEleclMainWtrPump
EOPC
LAirVentVertMot
FLSLMM
CupholderAmbtLamp_LH
OHC
DoorAmbtLamp_FL
左侧出风口垂直扫风电机
电子油泵控制器
发动机电子主水泵
杯托氛围灯-左
门饰板氛围灯- 左前
顶控模块
左前座椅腰托按摩模块 
LAirVentHoztMot
SWS
DrvrDsp
RLSS
左侧出风口水平扫风电机     
CupholderAmbtLamp_RH
DoorAmbtLamp_FLM
KickSnsr
方向盘开关
仪表屏
阳光雨量传感器
门饰板氛围灯M- 左前 杯托氛围灯-右
MidLAirVentVertMot
脚踢传感器
N o t e ： 屏 幕 功 能 安 全 接 口 预 留
中央左出风口垂直扫风电机  
FWM
DoorAmbtLamp_RL CnsoAmbtLamp_LH
HODM
RoofDsp
MidLAirVentHoztMot
DTSP_RL
前雨刮电机模块
后排吸顶屏电机
门饰板氛围灯-左后 中央通道氛围灯-左
离手检测模块
中央左出风口水平扫风电机  
左后门触控开关面板
仅 6 S 车 型
仅 5 S 低 配 车 型
MidRAirVentVertMot
DoorAmbtLamp_RLM
CnsoAmbtLamp_RH
中央右出风口垂直扫风电机 
门饰板氛围灯M- 左后
中央通道氛围灯-右
MMiidRAdRAiirVrVentHoztMotentHoztMot
CnsoAmbtLamp_LM
中央右出风口水平扫风电机 
中央通道氛围灯- 左中
RAirVentVertMot
右侧出风口垂直扫风电机
CnsoAmbtLamp_RM
RAirVentHoztMot
中央通道氛围灯- 右中
右侧出风口水平扫风电机
电动出风口
上汽零束保密文件
仅用于大众和上汽零束项目使用
右前侧周视摄像头 左后侧周视摄像头 右后侧周视摄像头 
前周视摄像头3 后周视摄像头
左前侧周视摄像头 
前周视摄像头1
抬头显示 后排吸顶屏
后排智能表面_左 后排智能表面_右
SVW B-SUV 6S+5S 
AVCamr_FRS AVCamr_RLS AVCamr_RRS
AVCamr_F3 AVCamr_R AVCamr_FLS
AVCamr_F1
HUD
RoofDsp
LHRSS
RHRSS
ETH&LVDS Network Topology
仅 6 S 车 型
Standard
HUD_LVDS RoofDsp_LVDS
LHRSS_LVDS RHRSS_LVDS
AVCamr_F1_LVDS AVCamr_F3_LVDS AVCamr_R_LVDS AVCamr_FLS_LVDS AVCamr_FRS_LVDS AVCamr_RLS_LVDS AVCamr_RRS_LVDS
Optional
 
 
Project
 
 
 
 
 
 
 
 
 
IAM_ETH DVR_LVDS
IAM
 
 
 
Intergrate
 
 
 
 
AVM_LVDS
 
FDM
ZXD IPD
Status:                    AddA 
ADAS_ETH
                               Modified         
M
Diag_ETH
DLC
                               Carry OverC
Connector Config: 
120
TR=120Ω Shielded
60
TR=60Ω Wireless
FLIDAR_ETH
TR=∞/Irrelevant
FDMCamr_LVDS
HDAVMCamr_F_LVDS HDAVMCamr_RH_LVDS
HDAVMCamr_R_LVDS
HDAVMCamr_LH_LVDS
Connection Config: 
CnsoDsp_LVDS CoDrvrDsp_LVDS
DrvrDsp_LVDS LHZCU_ETH
RHZCU_ETH RZCU_ETH
DMS_LVDS OMS_F_LVDS
OMS_R_LVDS
Ethernet_10G_base_T1
Note ：仅6S 高配车型，
Ethernet_1000M_base_T1
PT 阶段硬件预埋， 
Ethernet_100M_base_T1
功能0S 实施；
Ethernet_10M_base_T1
CANFD
Local CANFD
CAN
Diagnostic_CAN
Local CAN
FDMCamr
CoDrvrDsp LHZCU RHZCU RZCU
CnsoDsp DrvrDsp DMS OMS_F HDAVMCamr_LH
OMS_R
HDAVMCamr_F HDAVMCamr_R HDAVMCamr_RH
FLIDAR
LIN
防炫目流媒体内后视镜摄像头
车内摄像头
车内前摄像头 车内后摄像头
高清环视摄像头_前
高清环视摄像头_后 高清环视摄像头_左 高清环视摄像头_右
中控大屏 仪表屏 副驾娱乐屏 前向激光雷达
Flexray
LVDS 仅 6 S 车 型
智舱SOC 接口
Inftn
上汽零束保密文件
仅用于大众和上汽零束项目使用
A b b r e v i a t i on
C om po ne n t Lon gN a m e C hi n e s e N am e C om po ne n t Lo ng N am e C hi n es e N a me
L I N _ P EU
C A N
ZXD Zenith X Drive 舱算融合计算平台 EOPC Electric Oil Pump Controller 电子油泵控制器
IPD Intelligent Pilot Device 智驾域控制器 LIN _LH ZC U
IAM Intelligent Antenna Module 智联域控制器 OHC Over Head Control 顶控模块
DLC Data Link Connector (Diagnostic Connector) 诊断接口 RLSS Rain Light Solar Sensor 雨量灯光阳光传感器  
FDR Front Detection Radar 前向探测雷达 FWM Front Wiper Motor 前雨刮电机模块
FLIDAR Front Lidar 前激光雷达 DoorAmbtLamp_FL Door Ambient Lamp_FL 门饰板氛围灯-左前
LHA Left Headlamp Assembly 左前大灯总成 DoorAmbtLamp_FLM Door Ambient Lamp_FLM 门饰板氛围灯M-左前
RHA Right Headlamp Assembly 右前大灯总成 DoorAmbtLamp_RL Door Ambient Lamp_RL 门饰板氛围灯-左后
RZCU Rear Zonal Control Unit 后区域控制器 DoorAmbtLamp_RLM Door Ambient Lamp_RLM 门饰板氛围灯M-左后
SDM Sensing Diagnostic Module 安全气囊控制诊断模块 CupholderAmbtLamp_LH Cupholder Ambient Lamp_LH 杯托氛围灯-左
IBS Integrated Brake System 集成式制动系统 CupholderAmbtLamp_RH Cupholder Ambient Lamp_RH 杯托氛围灯-右
EPS Electric Power Steering 电动助力转向 CnsoAmbtLamp_LH Consol Ambient Lamp_LH 中央通道氛围灯-左
RWSL Rear Wheel Steering Loacal 后轮转向 CnsoAmbtLamp_RH Consol Ambient Lamp_RH 中央通道氛围灯-右
SCM Suspension Control Module 自适应悬架或主动悬架 CnsoAmbtLamp_LM Consol Ambient Lamp_LM 中央通道氛围灯-左中
PEU Power Electric Unit 电力电子单元 CnsoAmbtLamp_RM Consol Ambient Lamp_RM 中央通道氛围灯-右中
ECM Engine Control Module 发动机控制模块 FLSLMM Front Left Seat Lumbar And Massage Module 左前座椅腰托按摩模块 
LVBM Low Voltage Battery Module 低压电池模块 KickSnsr Kick Sensor 脚踢传感器
CCU Combined Charging Unit 高低压集成充电模块 DTSP_RL Door Touch Switch Panel_RL 左后门触控开关面板
ESS Energy Storage System 能量存储系统 LIN _RZC U
ChrgrSkt Charger Socket 充电口 ChrgngStaLamp Charing State Lamp 充电状态灯 
LHZCU Left Hand Zonal Control Unit 左区域控制器 APTC Air PTC 空气加热器
BPEPS Bluetooth Passive Entry Passive Start 蓝牙无钥匙进入和启动 TailLampAsmblA_LH Tail Lamp Assembly A_LH 尾灯总成A_左
NFCAM Near Field Control Access Module NFC 进入模块 TailLampAsmblA_RH Tail Lamp Assembly A_RH 尾灯总成A_右
NFCSM Near Field Control Strat Module NFC 启动模块 TailLampAsmblB_LH Tail Lamp Assembly B_LH 尾灯总成B_左
RRBLEA Rear Right Bluetooth Antenna 右后蓝牙天线 TailLampAsmblB_RH Tail Lamp Assembly B_RH 尾灯总成B_右
RLBLEA Rear Left Bluetooth Antenna 左后蓝牙天线 RLSLMM Rear Left Seat Lumbar And Massage Module 左后座椅腰托按摩模块
FRBLEA Front Right Bluetooth Antenna 右前蓝牙天线 RRSLMM Rear Right Seat Lumbar And Massage Module 右后座椅腰托按摩模块
FLBLEA Front Left Bluetooth Antenna 左前蓝牙天线
LI N _Z X D
RHZCU Right Hand Zonal Control Unit 右区域控制器 SWS Steering Wheel Switch 方向盘开关
EAC Electric Air Conditioning Compressor 电动空调压缩机（混动） HODM Hands Off Detection Module 离手检测模块 
ETCM Electronic Toll Collection 电子收费系统 DrvrDsp Drvr Ambient DrvrDsp_DrvrDsp 屏幕功能安全
FDM Full Display Mirror 防炫目流媒体内后视镜 RoofDsp Roof Ambient RoofDsp_RoofDsp 后排吸顶屏电机
TPMS Tire Pressure Monitoring System 胎压监测系统 LAirVentVertMot Left Air Vent Vertical Motor 左侧出风口垂直扫风电机
L I N _ R H Z C U LAirVentHoztMot Left Air Vent Horizontal Motor 左侧出风口水平扫风电机       
AIntnlTemSnsr Ambient Internal Temperature Sensor 舱内温度传感器 MidLAirVentVertMot Middle Left Air Vent Vertical Motor 中央左出风口垂直扫风电机   
CF Consle Fridge 车载冰箱 MidLAirVentHoztMot Middle Left Air Vent Horizontal Motor 中央左出风口水平扫风电机       
IFM Intelligent fragrance module 香氛散发模块 MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
UpIPAmbtLampA_LH Up IP Ambient Lamp A_LH 上仪表板氛围灯A-左 MidRAirVentVertMot Middle Right Air Vent Vertical Motor 中央右出风口垂直扫风电机
UpIPAmbtLampB_LH Up IP Ambient Lamp B_LH MidRAirVentHoztMot Middle Right Air Vent Horizontal Motor 中央右出风口水平扫风电机       
上仪表板氛围灯B-左
UpIPAmbtLampA_RH Up IP Ambient Lamp A_RH RAirVentVertMot Right Air Vent Vertical Motor 右侧出风口垂直扫风电机
上仪表板氛围灯A-右
DwnIPAmbtLampA_LH Down IP Ambient Lamp A_LH RAirVentHoztMot Right Air Vent Horizontal Motor 右侧出风口水平扫风电机       
下仪表板氛围灯A-左
DwnIPAmbtLampA_RH Down IP Ambient Lamp A_RH 下仪表板氛围灯A-右 L V D S
DwnIPAmbtLampB_RH Down IP Ambient Lamp B_RH 下仪表板氛围灯B-右 LHRSS Left Hand Rear Smart Surface 后排智能表面_左
Right Hand Rea Smart Surface
DoorAmbtLamp_FR Door Ambient Lamp_FR 门饰板氛围灯-右前 RHRSS 后排智能表面_右
DoorAmbtLamp_FRM Door Ambient Lamp_FRM HUD Head Up Display 抬头显示
门饰板氛围灯M-右前
DoorAmbtLamp_RR Door Ambient Lamp_RR RoofDsp Roof Display 后排吸顶屏
门饰板氛围灯-右后
DoorAmbtLamp_RRM Door Ambient Lamp_RRM CnsoDsp Console Display 中控大屏
门饰板氛围灯M-右后
RoofAmbtLampA_LH Roof Ambient LampA_LH 顶棚氛围灯A-左 DrvrDsp Driver Display 仪表屏
RoofAmbtLampB_LH Roof Ambient LampB_LH 顶棚氛围灯B-左 CoDrvrDsp CoDriver Display 副驾娱乐屏 
RoofAmbtLampC_LH Roof Ambient LampC_LH 顶棚氛围灯C-左 DMS Driver Monitor System 车内摄像头
RoofAmbtLampA_RH Roof Ambient LampA_RH OMS_F Occupancy Monitoring System_Front 车内前摄像头
顶棚氛围灯A-右
RoofAmbtLampB_RH Roof Ambient LampB_RH OMS_R Occupancy Monitoring System_Rear 车内后摄像头
顶棚氛围灯B-右
RoofAmbtLampC_RH Roof Ambient LampC_RH AVCamr_F1 Around View Camera_Front1 前周视摄像头1
顶棚氛围灯C-右
ESSClntPump ESSClnt Ambient ESSClntPump_ESSClntPum能p 量存储系统冷却水泵 AVCamr_F3 Around View Camera_Front3 前周视摄像头3
MulChnlVlv Mul Ambient ChnlVlv_MulChnlVlv AVCamr_FLS Around View Camera_Front Left Side 左前侧周视摄像头 
冷却系统多通阀
PEBClntPump1 PEBClnt Ambient PEBClntPump_PEBClntPum电p1驱动电子水泵 AVCamr_FRS Around View Camera_Front Right Side 右前侧周视摄像头 
AGS1 Active Grille Shutter 1 主动进气格栅_1 AVCamr_R Around View Camera_Rear 后周视摄像头 
ClntVlv Clnt Ambient ClntVlv_ClntVlv 三通阀 AVCamr_RLS Around View Camera_Rear Left Side 左后侧周视摄像头 
WtrPTCPump Wtr Ambient WtrPTCPump_WtrPTCPump HVPTC水泵 AVCamr_RRS Around View Camera_Rear Right Side 右后侧周视摄像头 
CoolngFan Coolng Ambient CoolngFan_CoolngFan 冷却风扇 HDAVMCamr_F High Definition AVM Camera_F 高清环视摄像头_前 
Blwr_F Blower_F 前鼓风机 HDAVMCamr_LH High Definition AVM Camera_LH 高清环视摄像头_左 
FRSLMM Front Right Seat Lumbar And Massage Mod右ul前e 座椅腰托按摩模块 HDAVMCamr_R High Definition AVM Camera_R 高清环视摄像头_后 
FRSCMM Front Right Seat Cushion Massage Module 右前座椅坐垫按摩模块 HDAVMCamr_RH High Definition AVM Camera_RH 高清环视摄像头_右 
DTSP_RR Door Touch Switch Panel_RR 右后门触控开关面板 FDMCamr Full Display Mirror Camera 防炫目流媒体后视镜摄像头
LIN _EC M
EnEleclMainWtrPump Engine Electrical Main Water Pump 发动机电子主水泵
上汽零束保密文件
仅用于大众和上汽零束项目使用
Version History
序号 版本 修订日期 修改人 详细变更 
1 V0.1 2024-08-22 王众 First version
1、删除IPS 模块 
2、后排吸顶屏电机挂ZXD_LIN1
2 V0.2 2024-09-05 王众
3、取消HD 大灯模块 
4、智驾方案待定
1、ITMS 不集成，LHZCU_LIN 6 节点 
3 V0.3 2024-09-13 王众
2、智驾方案更新
1、增加OMC 摄像头- 备注DMC-OMC AGT2 阶段不实施
2、氛围灯AGT2 阶段不实施 
4 V0.4 2024-09-18 王众
3 、删除充电小门LIN 节点 
4、删除泊车雷达CAN 节点，FDR 接BackupCANFD
1、标记UWB 钥匙及NFC ，HUD 阶段不实施 
2、新增OMS_R 摄像头 
3、调整HODM 及SecRawClngMntdScrn LIN 模块LIN 网段位置
5 V0.5 2024-10-14 王众
4、更改ADCU 名称为IPD 
5、TPMS AGT2 阶段实施 
6、左右座椅腰托AGT2 阶段不实施 
1、调整RHZCU_LIN6,LIN7 网段节点
6 V0.6 2024-10-18 王众
2、更改后排吸顶屏命名
1、增加后排smart surface 屏幕 LVDS 节点 
7 V0.7 2024-11-28 王众 2、增加氛围灯LIN 节点,增加后尾灯LIN 节点,增加脚踢传感器LIN 节点，增加顶控OHC LIN 节点 
4、将高压加热器LIN 节点合并至RZCU_LIN1
1、香氛IFM 节点从连接RHZCU_LIN3 更改为ZXD_LIN3; 
2、增加电动出风口LIN 节点于ZXD_LIN4; 
3、增加舱内温度传感器AIntnlTemSnsrLIN 节点于RHZCU_LIN2; 
8 V0.8 2024-12-19 李茂亚
4、HODM 更改为直接ZXD_LIN1; 
5、删除LH Body CANFD 上UWBA 天线节点，增加LH Body CANFD 上RRBLEA 、RLBLEA 、FRBLEA 、
FLBLEA 蓝牙天线节点；
1、笔误修订：MapPcktAmbtLamp_RL 节点重复，修订为MapPcktAmbtLamp_FR 及MapPcktAmbtLamp_RR ； 
2、笔误修订：尾灯模块节点名称更改，TailLampBsmblB_LH 更改为TailLampAsmblB_LH ，TailLampBsmblB_RH 更改
为TailLampAsmblB_RH ； 
3、按信号需求统一拓扑节点名称： 
DoorAmbLamp_FR 更改为DoorAmbtLamp_FR ；DoorAmbLamp_FRM 更改为DoorAmbtLamp_FRM ； 
DoorAmbLamp_RR 更改为DoorAmbtLamp_RR ；DoorAmbLamp_RRM 更改为DoorAmbtLamp_RRM ； 
9 升版至V1.0-PT 2025-01-24 李茂亚
DoorAmbLamp_FL 更改为DoorAmbtLamp_FL ；DoorAmbLamp_FLM 更改为DoorAmbtLamp_FLM ； 
DoorAmbLamp_RL 更改为DoorAmbtLamp_RL ；DoorAmbLamp_RLM 更改为DoorAmbtLamp_RLM ； 
电子油泵CCEOP 统一更改为EOPC ； 
车载冰箱CnsoFdge 统一名称更改为CF ； 
4、香氛改为连ZXD_LIN4;
1、香氛IFM 节点从ZXD_LIN4 更改为接RHZCU_LIN3;
2、氛围灯配置变更，需取消顶棚氛围灯节点：RoofAmbtLampD_LH 及RoofAmbtLampD_RH ，功能PVS 实
施，新增Note ：PVS 将取消顶棚氛围灯左右D 节点；
氛围灯配置变更：UpIPAmbtLamp_RH 节点变更为：UpIPAmbtLampA_LH ，UpIPAmbtLampB_LH ，
UpIPAmbtLampA_RH ，增加Note ：上仪表氛围灯拆分，硬件PT 实施，功能PVS 实施；
10 V2.0-PT 2025-02-21 李茂亚
氛围灯配置变更：新增console 氛围灯节点：CnsoAmbtLamp_LM 及CnsoAmbtLamp_RM ，新增 Note：中央
通道氛围灯新增LM、RM节点，硬件PT实施，功能PVS实施；
3、增加氛围灯各节点中文命名，FLIDAR 中文命名前向激光雷达；
4、更改副驾屏CoDrvrDsp 、后排吸顶屏RoofDsp 为选配节点；
5、拓扑各节点中文名称拉齐更新，Abbreviation 信息拉齐更新；
1、增加ETC 节点，接LH Body CANFD ； 
2、拉齐氛围灯配置信息，删除氛围灯RoofAmbtLampD_LH 及RoofAmbtLampD_RH 节点及氛围灯实施基线
11 V2.1-PVS 2025-02-28 李茂亚
Note 信息； 
3、方向盘开关名称由MFL 统一为SWS ； 
1、ETC 节点命名更新为ETCM ；
2、地图袋氛围灯改为白灯直驱方案，拓扑取消地图袋氛围灯节点：MapPcktAmbtLamp_FL 、
MapPcktAmbtLamp_RL 、MapPcktAmbtLamp_RR 、MapPcktAmbtLamp_FR.
3、5S 、6S 拓扑共版，增加6S、5S配置差异节点备注；
4、更新控制器清单；
5、新增DTSP_RL 左后门触控开关面板，接LHZCU_LIN8;
6、新增DTSP_RR 右后门触控开关面板，接RHZCU_LIN8;
V3.0 5S 对比6S 配置差异如下：
 a 、无前向激光雷达FLIDAR ；
12 6S-PVS 20250409 李茂亚
 b、无RWSL 后轮转向；
5S-PT
 c 、无APTC ；
 d、无后排吸顶屏电机RoofDsp ；
 e 、新增DTSP_RL 左后门触控开关面板;
 f 、新增DTSP_RR 右后门触控开关面板;
 g、无OMS_R 车内后摄像头，OMS_F 为选配；
 h、无顶棚氛围灯；
 i 、无后排座椅腰托按摩模块RLSLMM 、RRSLMM ；
V3.1 
1、RRSLMM 及RLSLMM 模块配置备注更新，5S车型低配取消后排座椅腰托按摩模块，高配保留；
13 20250416 李茂亚
6S-PVS 
1、5S 新增前向激光雷达，FLIDAR 取消备注“ 仅6S 车型” ； 
2、6S 高配新增右前座椅内部控制器：右前座椅坐垫按摩模块FRSCMM ，连接FRSMM Local_LIN ； 
3、TPMS LIN 改CAN ，删除TPMS LIN 节点，新增TPMS CAN 节点，连接LHBDCANFD ； 
V3.2 
4、新增FDM 防炫目流媒体内后视镜CAN 节点，连接LHBDCANFD ，PT 阶段硬件预埋； 
14 6S-PVS 20250710 李茂亚
5、新增FDMCamr 防炫目流媒体内后视镜摄像头，LVDS 连接FDM ，PT 阶段硬件预埋； 
5S-PT
6、ETCM PT 阶段硬件预埋，增加备注信息； 
7、更新Abbreviation ；  
上汽零束保密文件
仅用于大众和上汽零束项目使用

---

## PDF: 动采_AF\出口\6 CR变更架构评估-F车LHD出口CR-取消静态数采.pdf

变更内容说明 （需求方填写，一般为PO 或者FO ）
变更主题 取消静态数采功能 变更编号 3ER (Export)-CR-E-20260417-01
计划断点版本 F 平台VR1 变更类型 变更
涉及车型 F 6S LHD export CR 编号 /
PRD链接 无PRD ，仅有CR申请单。签字_3ER(Export)-CR-E-20260417-01-静态数据采集变更
变更原因：
出口车型需求
变更前：
• 根据法规要求定义数据采集内容,并且上传到云端和国家平台
变更后：
• 功能服务于国内法规要求,国外没有相关法规要求,功能删除
0
技术方案
技术方案描述：
（主要描述功能方案，一般由SO/架构填写，）
IAM删除静采模块，不需要收集信号帧打包上传，本身车上Arxml不变
受影响方说明：
IAM
涉及 到的 系统 或者零件，主要 影响
根据需求，如果内容较多，可增加页进行描述
1
架构影响评估
序号 评估项 是否影响 主要影响描述 表态方 计划完成时间
可填写具体时间，或者写
数据埋点上传 Function Group 下子功能按需删除 –FO/SO提出申请
1 功能清单 Y Zhang yinyin
跟随架构XX阶段发布
2 整车拓扑 N Wang Xiaoli
3 网络负载 N 涉及Safety CAN 增加负载 Wang Zhipeng
4 数据库 N Wang Xiaoli
休眠唤醒 N 无特殊休眠唤醒需求 Wang Xiaoli
5
6 诊断需求 IAM识别配置字，需更新Part4 、95文件 Hu Rui
7 配置字需求 IAM识别配置字 SO
8 原理图 N Wang Xiaoli
9 低压配电 N 无配电通道需求 Fan Youchen
静态功耗 N Fan Youchen
10
11 SSTS N SO直接传递给IAM 王晓丽
2
架构影响评估
本页评估结论由各项架构相关方&SO 确认
序号 评估项 是否影响 主要影响描述 表态方 计划完成时间
12 整车服务 N
13 以太网 N Liangjialong
14 网络安全 N Peng Xiaoyan
Jiang 
15 功能安全 N
Zhuheng
16 OTA N Zhang Jiatong
17 能耗 N
18 集成测试 Y
19 EID/ 线束 N
20 法规认证 N
架构评估结论 架构可行，在VR1断点
3
零件受影响方说明
本页评估结论由SO 拉齐各方给出
序
变更零件 变更说明 预估费用 表态方 计划完成时间
号
Kong 
IAM删除静采
IAM
Xiaonan/
评估结论 已和IAM Kong Xiaonan 拉齐，通过checklist 传递需求变更（基于IAM开发分工在 总院）
4

---

## PDF: 动采_AF\动采平台\动采云平台操作手册.pdf

零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 
 
 
 
 
 
动态数据采集系统 
 
产品使用手册 
 
 
 
 
 
 
 
 
 
 
  
1
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
修订记录 
 
版本 修改内容 修改时间 修订人 审核人 
V1.0.0 创建 2024-08-09 郑律斯 孙云华 
 
  
2
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
目录 
1 介绍 ...................................................................... 4 
1.1 概述 ..................................................... 4 
1.2 目标和范围 ............................................... 4 
1.3 预期读者 ................................................. 4 
1.4 名词解释 ................................................. 4 
2 功能概述 .................................................................. 5 
2.1 业务流程 ................................................. 5 
2.2 功能列表 ................................................. 5 
3 模块功能用户使用说明 ....................................................... 7 
3.1 基础数据管理 ............................................. 7 
3.1.1品牌车型管理 .......................................... 7 
3.1.2车型车辆管理 .......................................... 8 
3.1.3车型分组管理 .......................................... 9 
3.2 标签数据管理............................................... 15 
3.2.1标签类型管理 ......................................... 15 
3.3 信号池管理................................................. 20 
3.3.1 CANLIN 信号池管理 .................................... 20 
3.3.2 DataID 信号配置管理 .................................. 29 
3.3.3 DC/TP 信号池管理 ..................................... 37 
3.3.4 DataID 信号池管理 .................................... 41 
3.3.5信号池发布审核 ....................................... 41 
3.3.6信号绑定配置 ......................................... 44 
3.4 采集任务管理............................................... 45 
3.4.1 边缘计算配置......................................... 45 
3.4.2 CANLIN 采集任务配置 .................................. 51 
3.4.3 ASF 采集任务配置 ..................................... 60 
3.4.4 DC/TP 采集任务配置 ................................... 64 
3.4.5 CAN/LIN 过滤任务配置 ................................. 68 
3.4.6 事件融合采集任务配置................................. 71 
3.4.7 采集任务调度管理..................................... 73 
3.4.8数据采集审核 ......................................... 76 
3.5 业务监控统计............................................... 77 
3.7.1数据采集任务统计 ..................................... 77 
3.7.2车辆采集状态统计 ..................................... 78 
3.7.3流量监控与统计 ....................................... 79 
3.8 系统管理 ................................................... 80 
3.8.1采集审核配置 ......................................... 80 
3.8.2信号审核配置 ......................................... 81 
3.8.3操作日志 ............................................. 81 
3
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
1 介绍 
1.1 概述 
为深入挖掘车辆数据的巨大价值，实现云管端一体化统一治理，打破数据采集边界，实现
动态、灵活、按需的数据采集；增强数据保护机制，避免数据意外丢失；动态配置采集及触发
条件，实现整车级信号的周期、触发、完整采集功能；标准化通用数据采集规则，总体管控数
据项配置及管理，建设零束全域动态数据采集管理服务平台，支持其他业务系统相关数据采集
需求，为未来的大数据分析、运营管理、数据增值等业务实现有力支撑，保证车型项目的完整
交付。 
1.2 目标和范围 
本文档描述动态数据采集系统使用说明，帮助运营管理人员认识本平台的相关能力。对基础
数据管理、标签数据管理、信号池管理、采集任务管理、业务监控统计、系统管理进行能力介
绍。 
1.3 预期读者 
本说明书的预期读者包括： 
⚫ 系统管理员角色； 
⚫ 信号管理员角色； 
⚫ 信号审核员角色； 
⚫ 采集申请人角色； 
⚫ 采集审核员角色； 
1.4 名词解释 
NA 
4
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
2 功能概述 
2.1 业务流程 
 
2.2 功能列表 
一级 
二级功能 功能描述 
功能 
基于主数据中的信息，管理动态数据采集系统中所支持等品
品牌车型管理 
牌、车型信息。 
基于主数据中的品牌、车型等信息，管理动态数据采集系统中
基础数 车型车辆管理 
所支持等品牌、车型以及与车辆数据及其关联关系。 
据管理 
基于车型对车辆进行分组管理，包括分组的增、删、改、查；
车型分组管理 以及对分组内车辆的管理，分组内车辆管理支持车辆导入、添
加、删除等操作。 
标签类型管理 支持 4 级标签类型的定义和配置管理； 
标签管
理 
标签管理 对信号打标签管理，支持批量导入导出操作。 
CAN/LIN 信号池 信号池管理，包括信号池及版本的增、删、改、查、以及信号
管理 池版本的审核发布流程。 
信号池 DataID 信号配
包含 dctp 智舱埋点信号，支持 dataid 全量信号的查询；  
管理 置管理 
管理 DCTP 信号池，包括信号池及版本的增、删、改、查、以
DC/TP 信号池管
及信号池版本的审核发布流程。 
理 
5
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
DataID 信号池 Someip 信号池管理，包括信号池及版本的增、删、改、查、
管理 以及信号池版本的审核发布流程。 
新增 CANLIN 信号池、DC.DC/TP 信号池、Dataid 信号池时需要
有审核流程支持，审核环节可配置支持不超过 5 个环节，其中
信号池发布审核 
任何一个审核环节退回则需重新修改发布，只有所有环节都通
过才能提供给其他模块使用。 
根据车型项目基线绑定各类型的信号池版本 
信号绑定配置 
支持边缘计算算法的配置，设定算法计算参数、计算规则等。 
边缘计算配置 
支持两种方式进行基于信号方式定义采集申请，在设定采集信
CAN/LIN 采集任
号范围、生效时间范围、采集车辆后进入审核流程，包括 D-
务配置 
PDU 信号&CAN&LIN 采集与解析 
ASF 采集任务配
采集数据范围包括 SOME/IP 周期完整数据 
置 
设定 Can 和 Lin 指令过滤范围、生效时间、采集车辆后进入审
CANLIN 过滤任
核流程。 
务配置 
采集任
DC/TP 采集任务
务管理 
支持 ICM 的智舱埋点信号的周期和完整采集 
配置 
基于边缘计算的触发事件实现 canlin、ASF-someip 信号的融
事件融合采集任
合采集 
务配置 
针对采集任务进行调度管理，如任务暂停、任务恢复、任务终
采集任务调度管
止等。 
理 
对采集申请进行审核，审核环节可配置支持不超过 5 个环节，
其中任何一个审核环节退回则需重新修改发布，只有所有环节
数据采集审核 
都通过才能提供给其他模块使用。 
以数据采集任务为轴心进行统计，提供当前数据任务的各类状
数据采集任务统
态以及相关数据统计。 
计 
业务监
以车辆采集状态为轴心进行统计，提供车辆执行配置脚本清空
车辆采集状态统
控与统
的相关数据统计。 
计 
计 
以车辆维度统计上传文件合计大小的流量排序，支持按照月、
流量监控与统计 
周、日维度统计，并能查看流量详情。 
对采集审核的环节数量以及各环节通知进行配置管理。 
采集审核配置 
系统管
对信号池审核的环节数量以及各环节通知进行配置管理。 
信号审核配置 
理 
记录 WEB 端使用用户的关键操作。 
操作日志 
 
6
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3 模块功能用户使用说明 
3.1 基础数据管理 
3.1.1 品牌车型管理 
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
此页面默认展示品牌信息，点击车型和切换到车型信息。 
2.数据来源：品牌、车型数据来源于主数据，本模块通过对品牌和车型数据进行编码配置将品
牌数据引入到 DDC 中。 
 
 品牌车型管理-品牌列表页面 
3.设置编码按钮：即给品牌设置编码。 
 
 
品牌车型管理-设置品牌编码弹框 
操作步骤如下： 
第一步：品牌名称自动带入显示不可编辑； 
第二步：输入品牌编码，规则：数值，uint8, 输入十进制，系统自动转化为 16 进制表达
且应保持唯一。范围 1-255。 
当输入品牌编码不唯一时，提示用户“已有相同品牌编码，请修改后重试”。 
第三步：点击确定按钮。 
如果需要取消设置品牌编码，则点击取消按钮。 
7
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 
品牌车型管理-品牌列表页面 
4.查询按钮：可根据品牌名称、车型项目、车型年份，输入格式不限，最长 30 个字符，进行模
糊匹配查询。 
5.重置按钮：点击后，重置查询条件。 
6.设置编码按钮：即给车型设置编码。点击后弹出“图表 品牌车型管理-设置车型编码弹
框。” 
 
品牌车型管理-设置车型编码弹框 
操作步骤如下： 
第一步：品牌名称、车型项目、车型年份自动带入显示，不用编辑； 
第二步：输入品牌编码，规则：数值，uint8, 输入十进制，系统自动转化为 16 进制表达
且在同一品牌下，版本号编码应保持唯一。范围 1-255。 
第三步：点击确定按钮。 
如果需要取消设置车型编码，则点击取消按钮。 
7.列表排序： 
默认根据“最新修改时间”倒序排；  
3.1.2 车型车辆管理 
0.数据来源：车辆数据来源于主数据。 
8
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
 
车型车辆管理 
2.查询按钮：可根据品牌名称、车型项目、基线、销售状态、车辆类型、车辆状态、VIN 等进
行，进行模糊匹配查询。 
3.重置按钮：点击后，重置查询条件。 
3.1.3 车型分组管理 
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
注：车辆分组名称一般命名有实际业务含义，以方便查询和部署采集任务目标车辆锁定。 
 
车型分组管理 
2.查询按钮：可根据品牌名称、车型项目、车型年份，输入格式不限，最长 30 个字符，进行模
糊匹配查询。 
3.重置按钮：点击后，重置查询条件。 
4.分组管理按钮：点击后跳转到【3.1.3.1 分组管理】页面 
5.列表排序：默认根据 品牌、车型项目、车型年份、车型配置、销售状态、车辆类型、VIN 正
向排序。  
9
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
6. 车辆分组批量导入按钮:点击后跳转到“批量导入”页面。 
 
车型分组信息-分组管理-批量导入页面 
操作步骤： 
第一步：点击“导入”按钮，进入到“批量导入”页面； 
第二步：点击“下载模板”按钮，保存到桌面； 
 
第三步：在桌面找到保存的模板并打开如下图， 
 
在模板中按照事例填写，并保存； 
第四步：点击“上传文件”，弹出选择文件框，选择模板后，点击打开按钮； 
 
上传成功后，上传文件按钮位置，变为上传文件的名称，如下图。如果需要修改上传的
文件，则删除后，重复第四步操作。 
 
第五步：点击“下一步”按钮，当没有上传文件时则提示“请上传文件”，如上传文件
则系统将执行数据导入操作，并切换到“执行导入”页面； 
10
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 
车型分组信息-分组管理-批量导入-执行导入页面 
在“执行导入”页面中，系统将自动筛选可导入记录数量以及不可导入记录数据，并列出
不可导入记录表及错误提示。 
第六步：A 如果需要修改导入模板数据，则可点击“返回重新上传”按钮，回到“执行导
入”页面，修改导入模板数据后，重复操作第四步。 
       B 点击“下一步”按钮，切换到“导入完成”页面。并提示批量导入完成数据的
条数。 
11
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
车型分组信息-分组管理-车辆管理-批量导入-执行导入-导入完成页面 
第七步：点击完成按钮，回到【3.1.3 车型分组管理】页面。全部导入操作成功。 
7.车辆分组批量导出：点击后将此页面中全部车组的车辆数据导入到 excel 中，导出样例： 
 
 
3.1.3.1 分组管理页面 
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
注：系统自动为品牌、车型项目、车型配置下维护一个默认分组，该配置下所有车辆默认均在
此分组中。 车辆属于且只属于一个分组。 用户可将车辆从默认分组移动到其它分组中；也可
从其它分组中移除车辆，但此时车辆会回到默认分组中。 
2.查询按钮：可根据分组名称，输入格式不限，最长 30 个字符，模糊匹配相关车辆组条目。 
3.重置按钮：点击后，重置查询条件。 
12
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
车型分组信息-分组管理页面 
4.新建分组按钮：点击后弹出新建分组弹框， 
 
车型分组信息-分组管理-新建分组弹框 
操作步骤如下： 
第一步：车型项目自动获取； 
第二步：输入分组名称，规则非空，车型配置下唯一，由字母、中文、数字、下划线组
成，最长30 个字符； 
第三步：输入备注，规则格式不限，最长 300 个字符。 
第四步：点击确定按钮。 
如需要取消新建分组，则点击取消按钮。 
5.修改按钮：点击后弹出编辑分组弹框，编辑步骤及规则与新建分组一致。 
6.删除按钮： 存在以下 3 种清空： 
A.已关联未完成任务申请时，删除时提示用户：“已有数据采集任务使用此分组，无法删
除。 
B.已关联车辆不允许删除，删除时提示用户：“分组下关联有车辆，请移除分组内车辆后
重试”。 
13
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
C.当既没有关联未完成的任务申请以及车辆时，删除时提示用户：“确定要删除该分组
吗”。点击确定则删除分组成功，点击取消，则表示取消删除操作。 
7.车辆管理按钮：点击后跳转到【3.1.3.1.1 车辆管理】页面。 
注：默认分组没有车辆管理按钮。 
3.1.3.1.1车辆管理页面 
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
注：用户在创建车型分组信息后，通过此页面来添加勾选此分组下的车辆。 
默认展示此分组下的车辆信息。 
车辆添加有 2 种方式：1.通过点击导入按钮，进行批量导入 2.通过点击添加车辆按钮，进
行添加。 
2.查询按钮：可根据车辆类型、销售状态、车辆状态、车辆 VIN、基线，进行模糊匹配相关车
辆条目。 
3.重置按钮：点击后，重置查询条件。 
 
 
车型分组信息-分组管理-车辆管理页面 
4.车辆添加按钮：  
点击后跳转到【添加车辆】页面，在此页面中选择车辆，添加到对应的分组信息中。如下： 
【添加车辆】页面 
1.使用对象：系统管理员、信号管理员、采集申请人（只读）。 
注：只展示具有数据权限的同品牌、车型项目、车型年份、车型配置中其它分组下的车辆数
据。 
2.查询按钮：可根据车辆类型、销售状态、车辆状态、分组、车辆 VIN，进行模糊匹配相关车
辆条目。 
3.重置按钮：点击后，重置查询条件。 
4.列表排序：根据车辆类型、销售状态、车辆状态、VIN 字段正向排序。 
 
14
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
车型分组信息-分组管理-车辆管理-添加车辆页面  
5.添加车辆有 3 种方式： 
方式一：  
批量添加：可在当前页面全选：即批量选择列第一个选项、选中按钮； 
选中后，点击批量添加按钮，则当前页面所有车辆将车从原分组中移除，移除后车辆进入
新分组。 
方式二： 
添加按钮：定义：将单个车辆从原分组中移除，移除后车辆进入新分组。 
6.删除按钮：只针对此分组下某一辆车，点击后提示“确定要从分组中移除该车辆吗?”用户确
认后，当前列表中对应车辆记录删除，车辆已成功从当前分组中移除。移除后的车辆进入该车
型下的默认分组中。 
7.批量删除按钮：选择批量车辆后，点击按钮，提示用户“确认要删除全部列表中的数据
吗？”用户确认后，当前列表中车辆记录删除，并提示“车辆已成功从当前分组中移除。移除
后的车辆进入该车型下的默认分组中。 
3.2 标签数据管理 
3.2.1 标签类型管理 
1.定义：用户在此页面根据业务场景定义标签类型，标签类型分为三层级别，一级标签类型例
如售后运营、故障诊断、大数据应用服务等，二级标签类型例如售后运营下的驾驶行为、电池
分析车身状况等，三级标签类型例如驾驶行为下的超速、急加速、急减速等。 
2.使用对象：系统管理员、信号管理员。 
3.查询按钮：可根据标签类型名称、显示级别（全部、一级、二级、三级），进行模糊匹配相
关条目。 
4.重置按钮：点击后，重置查询条件。 
5.列表排序：按照深度优先方式展示；同等级的，按照“排序”字段顺序排序；同等级“排
序”相同的，按照最新更新时间逆序排序。 
注：类型编号：系统自动生成。标签数量：只在第三级标签类型下显示对应的标签数量。 
15
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
标签类型管理 
6.新建标签类型：点击后弹出新建标签类型弹框。 
 
标签类型管理-新建标签类型弹框 
1）父节点级别与父节点名称关联规则： 
①父节点级别：默认根节点父节点名称。根节点为建立一级标签类型；一级节点为建立二
级标签类型；二级节点为建立三级标签类型。 
②当父节点级别为根节点时，父节点名称不可选。 
③当父节点级别为一级节点时，父节点名称为一级名称，当父节点名称无内容时，用户不
可选，其它输入框也不可输入；需要用户先建立一级分类。 
④当父节点级别为二级节点时，父节点名称为一级名称/二级名称，当父节点名称列表无内
容时，用户不可选，其它输入框也不可输入；需要用户先建立一级分类及对应二级分类。 
操作步骤： 
2）类型名称：必填，在父级节点下唯一，字母、中文、数字、下划线，最长 30 个字符。当
类型名称填写重复时，出现提示”类型名称重复，请重新输入” 
3）排序：正整数。 
4）备注：输入格式不限，最多可输入 300 个字符，选填。 
5）当必填项填写完毕后，点击确定按钮，标签类型添加成功。点击取消按钮，则取消建立
标签类。 
6）当添加成功后在【3.2.1标签类型管理】页面产生一条分类信息。 
7.编辑按钮：点击后弹出“编辑标签类型”弹出，类型编码系统自动生成，类型名称、排序及
备注数据自动带入，修改规则同新建。 
16
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
标签类型管理-编辑标签类型弹框 
8.删除按钮：点击后弹出删除标签类型弹框，如下 
 
标签类型管理-删除标签类型弹框 
1）已有子节点的 不允许删除，点击确定按钮时提示用户：“ 该标签类型有子类型，请
清空子类型后删除” 
    2）已关联有标签的节点 不允许删除，点击确定按钮时提示用户：“ 该标签类型已关联有
标签，请解除关联后删除” 
3.2.2 标签管理 
1.定义：此页面自动获取在【3.2.1 标签类型管理】中获取三级标签类型，并通过点击第三级
标签类型，建立标签，并可通过系统自动获取该标签下的关联的关联CANLIN 数量、Dataid 数
量。 
2.使用对象：系统管理员、信号管理员。 
3.查询按钮：可根据标签类型名称、标签类型（全部、普通标签、信号标签），进行模糊匹配
相关条目。 
4.重置按钮：点击后，重置查询条件。 
5.列表排序：默认按照最新修改时间逆序排列；支持用户修改排序规则为按照对应关联数据进
行顺序、逆序排列 。 
17
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
标签管理 
6.搜索标签类型：输入标签类型名称，点击查询按钮，搜索出相应内容。 
 
标签管理-标签类型搜索 
 
7.新建标签按钮：点击此按钮，弹出新建标签页面。 
注：一级、二级、三级标签类型自动显示. 
 
标签管理-新建标签 
第一步：输入标签名称（规则：必填，全局唯一，字母、中文、数字下划线，最长 30 个字
符）。  
18
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
第二步：选择标签类型：普通标签/信号标签，默认选择普通标签（信号标签只能关联一个
信号，用于时间触发条件等场景；普通标签可任意关联）。 
第三步：点击确定按钮，当标签名称重复时，则出现提示“标签名称重复，请重新输
入”。 
当填写内容符合规则时，则点击确定，创建标签成功，并在【3.2.2 标签管理】页面中
产生一条记录。 
点击“取消”按钮，则取消建立标签。 
8.删除按钮：  
 
标签管理-删除标签 
1）已关联 CANLIN 信号、SOA 服务、事件的“标签” 不允许删除，点击删除按钮时提示用
户：“ 该标签已关联有信号或者事件，请解除关联后删除”。 
   2）对信号标签类型，还需检查是否关联事件框架定义中是否已关联，如果关联不不允许删
除，删除时提示用户：“ 事件定义中已使用该信号标签，请解除关联后删除” 
3）当需要删除的标签不满足以上 1,2 条件是，可以删除成功。 
9.标签详情按钮：点击进入到【3.2.2.1 标签详情】页面。 
10.编辑按钮：编辑步骤同新建一致，但标签类型不可修改。 
3.2.2.1 标签详情 
1.定义：通过【3.2.1 标签类型管理】中点击标签详情进入到此页面，并通过系统自动获取该
标签名称、标签类型、标签类型、以及关联的关联 CANLIN 数量、Dataid 数量，并展示出
CAN/LIN 信号池、Dataid 的数据列表。 
2.使用对象：系统管理员、信号管理员. 
3. 默认显示 CAN/LIN 信号池信息、可切换至 Dataid 信号池列表信息。 
 
标签管理-标签详情 
1)CAN/LIN 信号池： 
19
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
A． 排序：按照标签关联数量逆序、 信号池名称、信号池主版本号、次版本号排
序。 
B． 查询：根据信号池名称、主版本号、此版本号、是否关联（该标签在该信号池版
本中关联信号数量=0 是，为未关联；当大于 0 时，为关联），进行模糊匹配查
询。 
注:输入格式不限，最长 30 个字符，模糊匹配搜索。 
   默认显示全部版本的 CAN/LIN 信号池数据。 
2）Dataid 信号池： 
A． 排序：按照标签关联数量逆序排序。 
B． 查询：根据 DataID 名称、模块、ECU、应用类别、供应商、平台、产品线、
DataId、是否绑定，进行模糊匹配查询。 
注:输入格式不限，最长 30 个字符，模糊匹配搜索。 
   默认显示全部版本的 Dataid 信号池数据。 
3.3 信号池管理 
说明： 
1）信号池状态：申请、审核中、审核退回、审核通过。 
2）信号池流程流程：新建的信号池/服务池会申请状态，提交审核后，进入到审核中状态。 
A 当信号审核管理员，点击审核通过后进入到会进入到审核通过阶段。 
B 当信号审核管理员审核不通过后，进入到审核退回状态。 
3）审核退回状态的信号池，需要点击重新编辑按钮，重新回到申请阶段，修改后重新走审核流
程。 
4）数据的密级分为普通、机密和敏感三种类型。 
5）同一信号可以关联多个普通标签和多个信号标签。 
3.3.1 CANLIN 信号池管理 
1.定义： 创建 CANLIN 信号池，为车型信号的绑定和采集任务配置提供信号信息。 
2.使用对象：系统管理员、信号管理员。 
3.查询按钮：可根据信号池名称、主版本号、次版本号、最新修改人，进行模糊匹配相关条
目。 
4.重置按钮：点击后，重置查询条件。 
5.列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
6.页面展示: 默认显示申请的数据，可任意切换至 审核中、审核退回、审核通过。 
7.【申请】页面 
20
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
CANLIN 信号池管理-申请列表 
1）新建信号池按钮：点击后弹出新建信号池弹框。 
 
CANLIN 信号池管理-新建信号池 
第一步：输入信号池名称。输入规则：非空，唯一，字母、中文、数字、下划线，最长 30
个字符。 
第二步：输入主版本号。输入规则：非空，非负整数。 
第三步：输入次版本号。输入规则：非空，非负整数，但主版本号为 0 时，次版本号不能
为 0。 
第四步：输入备注（选填）。输入规则：格式不限，最多 300 个字符。 
第五步：点击新建按钮，在符合输入规则的前提下，新的信号池建立成功。 
注：主版本号、次版本号共同构成唯一 （主版本号.次版本号 唯一） 
取消按钮：点击后则取消建立新的信号池。 
    建立成功的信号池，需要审核，点击提交后才会进入到审核中状态。 
2）修改按钮：点击后弹出编辑信号池弹框。 
注：在此弹框，将原有的信号池信息带入，可在原有的基础上进行修改。 
修改步骤可参照新建步骤。 
 
21
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
        CANLIN 信号池管理-编辑信号池 
3）删除按钮：点击此按钮后，弹出是否确认删除该信号池版本的弹框。 
 
CANLIN 信号池管理-删除信号池 
A 当有基于此信号池版本，新建的新的信号池版本时，点击确定按钮，则弹出提示“该
信号池有其它版本，请删除其它版本后重试”。 
B 当没有基于此信号池版本，新建的新的信号池版本时，则点击确定按钮，可删除成
功。 
4）信号管理按钮：点击进入到【3.3.1.1 信号集管理】页面 
5）提交审核按钮：点击后，此信号池信息将移入到审核中列表。此操作是将新建立的信号
池提交到审核流程。 
8.【审核中】页面。 
 
CANLIN 信号池管理-审核中列表 
1） 表现形式：a/b，a 表示当前审核节点，b 代表全部审核节点数量。 
2）详情按钮：点击进入到【信号池发布审核】管理页面。 
9.【审核退回】当审核不通过时，将审核中页面的数据移入到审核退回列表。 
 
图表 15-6 CANLIN 信号池管理-审核退回列表 
22
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
1） 表现形式：a/b，a 表示当前审核节点，且表示在当前节点被审核退回，b
代表全部审核节点数量。 
2）详情按钮：点击进入到【信号池发布审核】管理页面。 
3）重新编辑按钮：点击后，当前列表中过滤掉对应记录，申请列表中增加该条记录；页
面跳到【申请】列表。 
10.【审核通过】页面。 
1） 表现形式：已通过/b，已通过表示全部审核节点审核通过，b 代表全部审
核节点数量。 
2）详情按钮：点击进入到【信号池发布审核】管理页面。 
3）管理按钮：点击进入到【信号集详情】页面。 
 
CANLIN 信号池管理-审核通过列表 
4）新建版本按钮：点击后弹出新建版本弹框。 
 
CANLIN 信号池管理-审核通过列表-新建版本 
注：信号池名称：系统默认当前信号池名称，不可编辑。 
23
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
第一步：修改主版本号。修改规则：非空，非负整数。 
第二步：修改次版本号。修改规则：非空，非负整数，但主版本号为 0 时，次版本号不能
为 0。 
第三步：默认显示“指定信号池版本”，显示信号池版本（信号池版本为【审核通过】列
表中对当条信号池版本记录点击“新建版本”按钮的信号池版本名称+主版本号+次版本号），
如下图 
 
第四步：点击新建按钮，在符合输入规则的前提下，新的信号池建立成功。记录进入到
【申请】列表中。 
注： 
A.信号池名称、主版本号、次版本号自动获取，信号池名称不可修改。 
B.主版本号、次版本号共同构成唯一 （主版本号.次版本号 唯一） 
C.取消按钮：点击后则取消建立新建版本的信号池。 
3.3.1.1信号集管理 
1.定义：此信号集管理是通过每个 CANLIN 信号池管理的 CANLIN 信号的集合。每个信号池版本
中信号唯一。 
2.使用对象：系统管理员、信号管理员。 
3.查询按钮：信号类型、信号简称、Channel、Can/LIN ID、标签，进行模糊匹配相关条目。 
4.重置按钮：点击后，重置查询条件。 
5.列表排序：默认根据信号简称顺序排列。 
 
CANLIN 信号池管理-信号集管理 
 
6.新建按钮：点击后弹出新建信号弹框。 
24
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
CANLIN 信号池管理-信号集管理-新建信号弹框 
第一步：点击新建按钮，弹出新建信号弹框。 
第二步：选择新建信号类型：CAN 信号/CAN 埋点/Lin 中的一种，点击后进入到【新建信
号】页面。 
 
 
CANLIN 信号池管理-信号集管理-新建信号-基础信息、详细信息页面 
第三步：填写信号基础信息。 
（1） 输入信号简称，当没有输入时，则提示“请输入信号简称”。 
（2） 输入信号名称，当没有输入时，则提示“请输入信号名称”。 
（3） 输入 CANID，输入规则：数值,bit16，当没有输入时，则提示“CANID 不能为
空”。 
（4） 输入 MSB，输入规则：数值，9bit，输入后自动生成 LSB。当没有输入时，则提示
“必须输入数字”。 
（5） 输入 TX，当没有输入时，则提示“请输入 TX”。 
25
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
（6） 输入 EvtID，当没有输入时，则提示“不允许为空”。 
（7） Data Length（Byte），当没有输入时，则提示“必须输入数字”。 
（8） Event Short Name，当没有输入时，则提示“请输入Event Short Name”。 
（9） Signal Conversion，当没有输入时，则提示“请输入Signal 
Conversion”。当输入Signal Conversion 后，自动生成 Offset/Factor 。 
       转换公式字段： 
            CAN 信号: Internal-To-Phys 
            CAN 埋点: Signal Convertion 
            Lin: Convertion 
       用户输入公式后，系统自动填充 Offset/Factor 字段； 
      当用户清空公式字段，Offset/Factor 字段提示： 输入{对应公式字段名称} 
       当输入公式转换出错，公式字段标记红框，并在下方提示“无法解析出偏移量和系
数” 
（10） 当必填项填写完毕后，点击提交按钮则提示“添加成功”，并回到【3.3.1.1 信号
集管理页面】。 
注：1）CANID、MSB、LSB、EvtID、Data Length（Byte）、Signal Length（Bit）输入
后，再输入框后，系统自动转换为十六进制。 
2）新建信号，依据信号管理页面中的信号类型，不同类型字段不同。默认为 can-无
EventID(CAN 信号)类型。 
3）红色 为必填项。 
 
4）在新建信号-基础信息、详细信息页面；标签页面；密级页面，点击重置按钮，都是
将当前页面填写的数据进行清除，清除后，需要重新填写。 
5）当在新建信号页面没有点击提交按钮，但是切换到标签/密级Tab 页时，在标签/密级
Tab 页点击“提交”按钮则提示“信号 ID 不能为空”。 
7.编辑按钮： 
1）编辑-信号，操作步骤同新建一致。 
2）编辑-标签：点击进入编辑信号页面，点击标签 Tab 进入到标签页面。 
 
CANLIN 信号池管理-信号集管理-编辑信号-标签页面 
第一步：点击添加标签按钮，弹出选择标签框，根据选择标签框，选择对应的标签。选
择完毕后，显示对应的标签的一级、二级、三级及标签名称。 
标签可多选。 
去除按钮：点击后可去除当前选择的标签。 
注：信号可同时关联信号标签及普通标签。 
26
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
（1） 提交按钮：判断信号 ID 是否为空，如果为空则提示“信号 id 不能为空”，如果
不为空，点击后则提示“保存成功”，并回到【3.3.1.1 信号集管理页面】。 
3）编辑-密级：点击进入编辑信号页面，点击密级 Tab 进入到密级页面。 
第一步：在密级页面可针对当前信号选择某一个密级（普通、机密、敏感） 
 
CANLIN 信号池管理-信号集管理-新建信号-密级页面 
第二步：点击提交按钮，则提示“存成功”。回到【3.3.1.1 信号集管理】页面，并生成
一条信号数据。 
8.删除按钮：点击后弹出提示“确定要删除该信号吗?” ，确认则删除此信号。 
9.一键删除按钮：当结果列表中有数据时可用，点击此按钮，提示用户“确认要删除全部列表
中的数据吗？”用户确认后进行处理。 
10.导入按钮：点击后跳转到【批量导入】页面。 
 
CANLIN 信号池管理-信号集管理-新建信号-批量导入 
操作步骤： 
第一步：点击“导入”按钮，进入到“批量导入”页面； 
第二步：选择文件类型（CAN 信号 、埋点/D-PDU、 LIN，默认 CAN 信号） 
第二步：点击“下载模板”按钮，保存到桌面； 
 
第三步：在桌面找到保存的模板，如下， 
27
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
在模板中按照格式要求填写，保存； 
第四步：点击“上传文件”，弹出选择文件框，选择模板后，点击打开按钮； 
 
上传成功后，上传文件按钮位置，变为上传文件的名称，如下图。如果需要修改上传的文
件，则删除后，重复第四步操作。 
 
第五步：点击“下一步”按钮后，系统将执行数据导入操作，并切换到“执行导入”页面；
（当没有上传文件时，下一步按钮置灰不可选）； 
在“执行导入”页面中，系统将自动筛选可导入记录数量以及不可导入记录数据，并列出
不可导入记录表及错误提示。 
第六步：A 如果需要修改导入模板数据，则可点击“返回重新上传”按钮，回到“执行导
入”页面，修改导入模板数据后，重复操作第四步。 
        B 点击“下一步”按钮，切换到“导入完成”页面。并提示批量导入完成数据的
条数。 
第七步：点击完成按钮，回到【3.3.1.1 信号集管理】页面。全部导入操作成功。 
11.导出按钮：可根据查询条件导出需要的信号数据，点击此按钮后，导出一个 excel 文件，
导出样例。 
28
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
12. 标签导入按钮：导入步骤同 10.批量导入。 
 
标签导入样例： 
 
13.批量删除按钮：当结果列表中有数据时可用，A 选择需要删除的数据，点击此按钮，提示用
户“您确认要批量删除信号吗？”用户确认后进行处理。B 当没有选择想要删除的数据时，点
击此按钮，则提示“请选择信号数据”。  
3.3.2 DataID 信号配置管理 
0.使用对象：系统管理员、信号管理员。 
1.定义：此页面是对 DataID 信号的建立的基础信息配置，包含应用类型配置、供应商识别码配
置、平台识别码配置、SinkAPP 配置、区分码范围配置，并通过 DataID 配置页面建立新的
DataID。 
2.默认显示 Data ID 配置，可自由切换到应用类型配置、供应商识别码配置、平台识别码配
置、SinkAPP 配置、区分码范围配置。 
3. DataID 配置页面： 
定义：建立 DataID 通过 DataID 配置页面申请，才可新建。此页面展示所有建立的 DataID
信息。 
   1）查询按钮：根据 DataID 名称、模块、ECU、应用类型、供应商、平台、产品线、区分
码、标签关键字、最新修改人，进行模糊匹配查询。 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
    4）DataID 申请按钮：点击后进入到【3.3.4.1DataID 管理】页面。 
5）详情按钮：点击后进入到【3.3.4.1.3DataID 详情】页面。 
29
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
6）复制按钮：复制 DataID信息到剪切板。 
 
DataID 信号配置管理-DataID 配置 
4.应用类型配置页面： 
1）查询按钮：根据应用类型进行模糊匹配查询。 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。支持
应用类型识别码排序，支持顺序、逆序排序。 
 
DataID 信号配置管理-应用类型配置 
4）新建按钮：点击此按钮后，弹出“新建应用类型识别码”弹框。 
 
DataID 信号配置管理-应用类型配置-新建 
30
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 第一步：输入应用类型识别码，并可根据系统自带的按钮进行增加或减少。规则：不能
为空，保持唯一性，数值 Uint13。当输入不符合规则时，则输入框下面出现提示。 
  第二步：输入应用类型，规则:不能为空，保持唯一性，由字母、中文、数字、下划线
组成，最长 30 个字符。当输入不符合规则时，则输入框下面出现提示。 
第三步：输入备注。可以选填。规则：最长 300 个字符。 
第四步：点击确定按钮，提示“新建成功”。 
但：在此弹框中点击取消按钮，则代表取消新建应用类型识别码。 
5）编辑按钮：编辑规则与新建一致。 
    6）删除按钮：a 当此应用类型识别码被新建立区分码时使用，则提示“此应用类型识别码
不允许删除”。 
               b.当没有被使用过，则可删除。点击此按钮，则提示是否确认删除，如果点击
确定则提示删除成功，如果取消，则取消删除操作 
5.供应商识别码配置： 
1）查询按钮：根据供应商名称进行模糊匹配查询。 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。支持
供应商识别码排序，支持顺序、逆序排序 
 
 
DataID 信号配置管理-供应商识别码配置  
4）新建按钮：点击此按钮后，弹出“新建供应商识别码”弹框。 
 
信号配置管理-供应商识别码配置-新建供应商识别码 
第一步：输入供应商识别码，并可根据系统自带的按钮进行增加或减少。规则：不能为
空，保持唯一性，数值 Uint8。当输入不符合规则时，则输入框下面出现提示。 
31
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
第二步：输入供应商名称，规则:不能为空，保持唯一性，由字母、中文、数字、下划线
组成，最长 30 个字符。当输入不符合规则时，则输入框下面出现提示。 
第三步：输入备注。可以选填。规则：最长 300 个字符。 
第四步：点击确定按钮，提示“新建成功”。 
但：在此弹框中点击取消按钮，则代表取消新建供应商识别码。 
    5）编辑按钮：编辑规则与新建一致。 
    6）删除按钮：a 当此供应商识别码被新建立区分码时使用，则提示“此供应商识别码不允
许删除”。 
               b.当没有被使用过，则可删除。点击此按钮，则提示是否确认删除，如果点击
确定则提示删除成功，如果取消，则取消删除操作。 
6.平台识别码配置页面： 
1）查询按钮：根据平台名称进行模糊匹配查询。 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。支持
平台识别码排序，支持顺序、逆序排序。 
 
DataID 信号配置管理-平台识别码配置  
4）新建按钮：点击此按钮后，弹出“新建平台识别码”弹框。 
 
DataID 信号配置管理-平台识别码配置-新建平台识别码 
第一步：输入平台识别码，并可根据系统自带的按钮进行增加或减少。规则：不能为
空，保持唯一性，数值 Uint8。当输入不符合规则时，则输入框下面出现提示。 
第二步：输入平台名称，规则:不能为空，保持唯一性，由字母、中文、数字、下划线组
成，最长 30 个字符。当输入不符合规则时，则输入框下面出现提示。 
第三步：输入备注。可以选填。规则：最长 300 个字符。 
32
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
第四步：点击确定按钮，提示“新建成功”。 
但：在此弹框中点击取消按钮，则代表取消新建平台识别码。 
    5）编辑按钮：编辑规则与新建一致。 
    6）删除按钮：a 当此平台识别码被新建立区分码时使用，则提示“此平台识别码不允许删
除”。 
               b.当没有被使用过，则可删除。点击此按钮，则提示是否确认删除，如果点击
确定则提示删除成功，如果取消，则取消删除操作。 
7.SinkAPP ID 配置页面： 
1）查询按钮：根据应用名称进行模糊匹配查询。 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。   
4）复制按钮：复制 APPID 信息到剪切板 
 
DataID 信号配置管理-SinkAPP ID 配置  
5）新建按钮：点击此按钮后，弹出“新建 APP”弹框。 
 
DataID 信号配置管理- SinkAPP ID 配置-新建 SinkAPP ID 
第一步：输入应用名称。规则：不能为空，保持唯一性，由字母、中文、数字、下划
线组成，最长 30 个字符。当输入不符合规则时，则输入框下面出现提示。   
第二步：输入备注。可以选填。规则：最长 300 个字符。 
第三步：点击确定按钮，提示“新建成功”。 
但：在此弹框中点击取消按钮，则代表取消新建 APP。 
     6）编辑按钮：编辑规则与新建一致。 
      7）删除按钮：a 当此 APP 被使用，则提示“此 APP 不允许删除”。 
                   b.当没有被使用过，则可删除。点击此按钮，则提示是否确认删除，如果
点击确定则提示删除成功，如果取消，则取消删除操作。 
8）复制按钮：复制 APPID 信息到剪切板。 
33
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
注：APPID- 新建时，系统自动建立 APPID, 唯一， Uint32，顺序分配。 
8.区分码范围配置： 
1）查询按钮：根据模块、ECU、应用类型、供应商、平台进行模糊匹配查询。 
 （1. 模块：默认全部。  DC.DC/TP  DC.Shadow  。 
2.ECU：默认全部。ICC 、 IAM  、 ICM 、 IPD 、IMATE。 
4.应用类型：默认全部。模糊匹配搜索。 
5.供应商：默认全部。模糊匹配搜索。 
6.平台：默认全部。模糊匹配搜索。） 
2）重置按钮：点击后，重置查询条件。 
3）列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
 
DataID 信号配置管理-区分码范围配置 
4）新建按钮： 
第一步：选择 ECU。 
第二步：选择模块。 
第三步: 选择应用配备。 
第四步：选择供应商。 
第五步：选择平台。 
第六步：输入产品线名称。规则：非空，唯一，字母、中文、数字、下划线，最长 30 个字
符。 
如点击取消按钮，则代表取消建立区分码范围。  
注：区分码个数：通过区分码范围最小值与最大值通过 16 进制转换10 进制得出的结果。 
5）编辑/删除按钮： 
A.此区分码范围内，如果已经被使用，则不可删除/编辑。 
B.如果没有被使用，则可以编辑/删除。但编辑时，规则同新建。 
C.删除：当没有被使用时，点击后弹出“是否确认删除”弹框。如果点击确认，则提示删
除成功。点击取消则取消删除操作。 
34
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
DataID 信号配置管理-区分码范围配置-新建区分码范围配置 
3.3.2.1 DataID管理页面 
 
DataID 信号管理 
0.使用对象：系统管理员、信号管理员。 
1.定义：此页面是在 DataID 信号配置管理的基础上，建立 DataID。 
2 查询按钮：根据 DataID 名称、模块、ECU、应用类型、供应商、平台、产品线、区分码、标
签关键字、最新修改人，进行模糊匹配查询。 
3 重置按钮：点击后，重置查询条件。 
4 列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
5 新建按钮：点击后进入到【3.3.2.1.1 新建 DataID】页面。 
6 详情按钮：点击后进入到【3.3.2.1.3DataID 详情】页面。 
7 复制按钮：复制 DataID 信息到剪切板。 
8 一键删除/删除按钮： 
未关联DataID信号池/申请中 信号池，可删除，如关联 DataID信号池（审核中、已
驳回、审核通过）不可删除，点击时可出现toast提示“此 DataID已关联DataID信号池
不可删除”。 
一键删除提示：确定要删除全部 DataID吗？（已关联审核中、审核退回、审核通过信
号池的DataID不可删除）。 
35
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
9.编辑按钮： 
已关联审核中/审核退回/审核通过的 DataID 信号池的 DataID 都不能编辑。 
未关联 DataID 信号池或只关联申请状态下的信号池，DataD 可以编辑。点击此按钮进入
到【3.3.4.1.2 编辑 DataID】页面。 
3.3.2.1.1 新建DataID 页面 
 
新建 DataID 
新建DataID 分为三大步：一、基础信息与扩展信息，二、标签，三、密级。 
一、基础信息与扩展信息： 
第一步：输入 DataID 名称。规则： 必填，唯一，字母、中文、数字下划线，最长 30 个
字符。 
第二步：选择 ECU。 
第三步：选择模块。默认显示 DC.DC/TP 或重新选择为 DC.Shadow。 
当模块为 DC.DC/TP 时，第四步，第五步，两项用户不可选，且分别默认为不需要云端影
子引擎解析，数据流。 
当模块为 DC.Shadow 时，第四步，第五步两项用户可选。 
第四步：选择影子引擎解析  规则：必填， 0 不需要云端影子引擎解析、 1 需要云端
影子引擎解析，默认显示 0. 
   第五步：选择车端数据源接入方式： 必填，0 数据流、 1 数据文件。 
   第六步：选择应用类型。 
第七步：供应商。 
第八步：选择平台。 
第九步：根据第二，三，六，七，八步，选择对应的产品线，并自动生成区分码；还可以
手动修改。规则：22 位字符，唯一。当输入的区分码被占用时，则弹出提示“区分码已
被占用，请刷新或修改” 
第十步：输入 Offset：默认显示 0，可手动修改。 
规则：数值，可小数，可负数、可整数。且只有当在第三步选择模块为 DC/TP，
第六步应用类型选择事件判断触发信号时，可以修改，否则置灰。 
第十一步：输入 Factor，默认显示 1，可手动修改。 
36
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
规则：数值，可小数，可负数、可整数。且只有当在第三步选择模块为
DC/TP，第六步应用类型选择事件判断触发信号时，可以修改，否则置灰。 
第十二步：备注：格式不限，最长 300 个字符，选填。 
扩展信息：当在第三步选择模块为 DC.DC/TP 时，需要填写第十三步，第十四步。当在第
三步选择模块为 DC.Shadow 时，需要填写第十五、十六、十七步。 
第十三步：输入对应数据长度。规则 ：正整数 ， uint32 
第十四步：输入解析规则。规则：必填、3000 字符。 
第十五步：输入数据/事件简称 
第十六步：选择 是否支持周期采集 
第十七步：输入：数据格式。 
第十八步：当以上操作步骤完成时，可切换到标签 Tab 页。来维护 DataID 标签。 
二、三：标签与密级的设置同【3.3.1.1】CANLIN 信号 
 
3.3.2.1.2 DataID详情 
在此展示DataID 详细信息。没有其他操作步骤。 
 
DataID 详情 
3.3.3 DC/TP 信号池管理 
1.定义： 创建 DC/TP 信号池，为车型信号的绑定和采集任务配置提供信号信息。 
2.使用对象：系统管理员、信号管理员。 
3.查询按钮：可根据信号池名称、主版本号、次版本号、最新修改人。 
4.重置按钮：点击后，重置查询条件。 
5.列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
6.页面展示: 默认显示申请的数据，可任意切换至 审核中、审核退回、审核通过。 
7.【申请】页面 
37
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
DC/TP 信号池管理  
1）新建信号池按钮：点击后弹出新建信号池弹框。 
 
DC/TP 信号池管理-新建信号池 
第一步：输入信号池名称。输入规则：非空，唯一，字母、中文、数字、下划线，最长
30 个字符。 
第二步：选择模块。 
第三步：输入主版本号。输入规则：非空，非负整数。 
第四步：输入此版本号。输入规则：非空，非负整数，但主版本号为 0 时，次版本号不能
为 0。 
第五步：输入备注（选填）。输入规则：格式不限，最多 300 个字符。 
第六步：点击新建按钮，在符合输入规则的前提下，新的信号池建立成功。 
注：主版本号、次版本号共同构成唯一 （主版本号.次版本号 唯一） 
取消按钮：点击后则取消建立新的信号池。 
    建立成功的信号池，需要审核，点击提交后才会进入到审核中状态。 
2）修改按钮：点击后弹出编辑信号池弹框。 
注：在此弹框，将原有的信号池信息带入，可在原有的基础上进行修改。 
修改步骤可参照新建步骤。 
3）删除按钮：点击此按钮后，弹出是否确认删除该信号池版本的弹框。 
38
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
DC/TP 信号池管理-删除信号池 
A 当有基于此信号池版本，新建的新的信号池版本时，点击确定按钮，则弹出提示“该
信号池有其它版本，请删除其它版本后重试”。 
B 当没有基于此信号池版本，新建的新的信号池版本时，则点击确定按钮，可删除成
功。 
4）信号管理按钮：点击进入到【3.3.3.1 DC/TP 集合管理】页面。 
5）提交审核按钮：点击后，此信号池信息将移入到审核中列表。此操作是将新建立的信号
池提交到审核流程。 
8.【审核中、审核退回、审核通过】页面：规则和操作步骤与【3.3.1 CANLIN 信号池管
理】相同 
3.3.3.1 DC/TP 集合管理页面 
 
DC/TP 信号集合管理 
0.使用对象：系统管理员、信号管理员。 
1.定义：此页面是在 DataID 信号池中信号的集合，可通过此页面选择新的 DataID 或者删除原
有DataID。 
2．查询按钮：根据 DataID名称、模块、ECU、应用类型、供应商、平台、产品线、区分码、标
签关键字、最新修改人，进行模糊匹配查询。 
3．重置按钮：点击后，重置查询条件。 
4．列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
5．复制按钮：复制 DataID信息到剪切板。 
6．一键删除按钮：当表中有数据时，此按钮可点击，点击此按钮，提示“确定要全部删除 
DataID 吗?”用户确认则此信号池下所有 DataID 删除。 
7 ：只能选择当前页面的 DataID，当选择后，则提示“确定要删除选中的 DataID 
39
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
吗?”用户确认则此选中的 DataID 删除。 
      未勾选需要删除的 DataID 时，则不可点击此按钮。 
8.删除按钮：表示删除此条 DataID，点击此按钮后则提示“确定要删除该 DataID 吗?”用户
确认则此选中的 DataID 删除。 
9 ：点击选择 DataID ，点击进入到【3.3.3.1.1 选择 DataID】页面，选择的数据
要根据信号池对应的模块（DC.DCTP / DC.Shadow）进行区分，不可放到一起。并且在当前
DataID 信号池下，Dataid 保持唯一。 
3.3.3.1.1 选择DataID 页面 
 
DC/TP 信号集合管理-选择 DataID 
0.使用对象：系统管理员、信号管理员。 
1.定义：此页面可以为对应的信号池选择新的 DataID。 
2.查询按钮：根据 DataID名称、模块、ECU、应用类型、供应商、平台、产品线、区分码、标
签关键字、最新修改人，进行模糊匹配查询。 
3．重置按钮：点击后，重置查询条件。 
4．列表排序：默认根据 DataID“最新修改时间”倒序排，最新修改的记录，排在最上方。 
5．复制按钮：复制 DataID信息到剪切板。 
6.一键选择按钮：当表中有数据时，此按钮可点击，点击此按钮，提示“确定要选择全部的 
DataID 吗?”用户确认，则全部的 DataID 数据将移入到 DataID 集合管理中。并提示用户操作
成功。 
7.批量选择按钮：只能批量勾选 当前页面的DataID，当选择后，则提示“确定要选择 
DataID 吗?”用户确认则此选中的 DataID 数据将移入到 DataID 集合管理中。并提示用户操作
成功。未勾选 DataID/没有数据时 则不能点击此按钮。 
8“已选中 0 个。”0 代表：在此页面勾选了多少个 DataID。 
注：此页面数据：基于不在当前 DataID 信号池下，某个模块下，筛选的 DataID 数据。 
40
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3.3.4 DataID 信号池管理 
0.使用对象：系统管理员、信号审核员。 
1.定义：查看 SOMEIP 信号池，为车型信号的绑定和采集任务配置提供信号信息。 
2.查询按钮：可根据车型项目、基线进行模糊查询； 
3.列表排序：根据更新时间倒序排序。 
4.数据源：元数据中心的信号池管理（ASF-SOMEIP） 
 
5.详情按钮：点击按钮后，进入【3.3.4.1 SOMEIP 信号池详情】页面 
3.3.4.1 SOMEIP 信号池详情 
 
3.3.5 信号池发布审核 
0.使用对象：信号审核员。 
1.定义：此页面是针对提交审核的 CANLIN 信号池、SOA服务池、DC.DC/TP 信号池、DC.Shadow
信号池进行审核通过/不通过的操作。当审核通过后，则进入到已审核 Tab 中。 
41
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
1.1 审核环节： 表现形式：a/b，a 表示当前审核节点，且表示在当前节点被审
核退回，b 代表全部审核节点数量，此审核节点数量在【信号审核配置】中设置。 
2.查询按钮：可根据申请类型、名称、申请人进行模糊查询。 
3.列表排序：根据申请时间倒序排序。最新修改的记录，排在最上方。 
4.待审核页面. 
 
信号池发布审核-待审核 
4.1 审核通过/审核驳回按钮：点击此按钮，弹出审核意见弹框。 
 
信号池发布审核—审核意见弹框 
    第一步：选择审核意见：审核通过/驳回 
第二步：当用户点击审核驳回按钮时，需要填写 “意见描述”，规则：字母、中文、数字
下划线，最长 300 个字符。（必填）当用户没有输入审核意见时，点击“确认”按钮，提示
“请输入审核意见，最长 300 个字符”。当用户点击审核通过按钮时，意见描述选填。 
第三步：点击确认按钮，则提示“保存成功”。 
如果存在多个审核节点，那么每个审核人员点击审核流程都是一致的。 
当点击审核驳回后，则下一个审核人员无需操作审核，直接将审核驳回的数据打回到对应
的信号池/服务池中，状态“审核退回”列表中。 
42
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
审核通过的数据，则在【3.3.5 信号池发布审核】移入到“已审核”Tab 页，在对应的信号
池的状态变为审核通过。 
4.2 详情按钮：点击进入到【3.3.5.1 信号池发布审核-详情】 
5.已审核页面。 
 
信号池发布审核—已审核 
5.1 详情按钮：点击进入到【3.3.5.1 信号池发布审核-详情】 
3.3.5.1 信号池发布审核-详情页面 
1.定义：此页面通过【3.3.5 信号池发布审核】页面点击操作下的“详情”按钮进入。 
 
信号池发布审核详情 
2.此页面展示信号池的基础信息以及审核详情以及历史审核详情。 
3. 按钮 
3.1 通过【3.3.7 信号池发布审核】页面点击操作下的“详情”按钮进入此页面时，点击
此按钮，进入对应信号池类型下的【信号集合详情】不包含 “标签”“密级”按钮。 
43
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3.2 通过【3.3.1CANLIN 信号池管理】【3.3.3 DC/TP服务池管理】页面点击操作下的
“详情”按钮进入页面，点击此按钮，点击进入对应信号池类型下的【信号集合详情】包
含 “标签”“密级”按钮。 
3.3.6 信号绑定配置 
0.使用对象：系统管理员、信号管理员。 
1.定义：提供品牌车型各基线下与 CAN/LIN 信号池、DC/TP 智舱信号池、SOMEIP 信号池版本的
绑定关系。 
 
信号绑定配置 
2.查询按钮：根据品牌名称、车型项目、基线、信号池名称查询。 
3.此处展示所有车的品牌-车型项目-基线信息以及对应绑定的 CAN/LIN 信号池、SOMEIP 信号
池、DC/TP 智舱信号池。 
4.绑定配置按钮：点击进入到【3.3.6.1 信号池基线绑定】页面。 
3.3.6.1 信号池基线绑定页面 
 
车型信号池版本配置-绑定信号池页面 
操作步骤： 
第一步:根据在【3.3.6 信号绑定配置】页面选择的某条信息，获取车的品牌、车型项
目、基线信息。 
第二步:选择 CAN/LIN 信号池，选择主版本号，选择当前主版本号对应的次版本号，点
击“绑定”按钮，绑定成功。 
44
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
第三步:选择 DC/TP 智舱信号池，选择主版本号，选择当前主版本号对应的次版本号，
点击“绑定”按钮，绑定成功。 
注:SOMEIP 信号池的绑定关系在元数据中心维护 
解绑：针对已经绑定的信号池，支持点击“解绑”按钮。 
3.4 采集任务管理 
3.4.1 边缘计算配置 
 
1.查询按钮：根据空间名称进行模糊查询 
2.新建按钮： 
 
第一步：填写“空间名称、描述”信息 
第二步：点击“确定”按钮，回到【边缘计算配置】页面 
3.查看按钮：点击后进入【3.4.1.1 算法管理】页面 
45
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3.4.1.1 算法管理页面 
 
1.ID 按钮：点击 ID，可跳转至算法编辑器中。 
编辑器概述：每个算法必须要包含开始、结束、事件或变量组件； 
 
1-1 开始组件：选择事件算法触发所需的信号；仅支持 DDS 信号、Can 信号、Lin 信号以
及自定义变量 
注意：信号类型和车型基线以及所在域控有关联。 
46
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 1-2 通用组件-运算组件 
运算组件：支持整个算法中的运算过程； 
注意：赋值变量，需要在开始节点自定义变量进行定义。 
 
 
 1-3 通用组件-判断组件 
47
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
判断组件：支持整个算法中的判断运算过程。 
 
 
1-4 输出组件-事件组件 
事件组件：进行输出事件 ID 给到采集数据进行使用。 
注意：每个事件 ID都选择上报云端，这样方便查阅算法运行状态。 
48
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 
1-5 输出组件-变量组件 
变量组件：作为一个变量输出给到相关方使用。 
 
49
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
1-6 保存-预执行-发布 
保存：可以将编辑中的事件算法保存；预执行：检查算法是否正确；发布：将算法发布至
数采平台进行使用。 
 
2.创建算法按钮： 
第一步：填写“车型、基线、目标 ECU、执行周期、备注”信息； 
第二步：点击“确定”按钮，算法创建完成； 
50
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
3.详情：点击“详情”按钮后，跳出算法的详情弹窗 
 
4.发布：点击“发布”按钮，算法发布成功，可在事件融合采集任务配置中，选择该算法事件
进行触发式数据采集。 
5.删除：点击后，该条算法将被删除； 
6.复制：点击后，跳出二次确认弹窗，点击确定后，弹窗消失，算法列表新增一条相同的算
法； 
3.4.2 CANLIN 采集任务配置 
0.使用对象：系统管理员、采集申请人。 
1.定义：支持两种方式进行基于信号方式定义采集申请，在设定采集信号范围、生效时间范
围、采集车辆后进入审核流程，采集方式如下： 
Can/Lin 周期采集：基于周期采集设定采集信号，支持通过数据标签快速获取和筛选信号。 
51
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
Can/Lin 完整采集：基于完整采集设定采集信号，支持通过数据标签快速获取和筛选信号。 
*采集配置支持增量累加方式叠加之前同类型采集任务 
2.查询按钮：可根据申请编号、申请标题、最新修改人进行模糊查询。 
3.重置按钮：点击“重置”按钮可以清空搜索条件。 
4.申请页面： 
 
CAN/LIN 采集任务配置 
1） 删除按钮：点击“删除”，弹出“您确定要删除申请任务吗？”的提示。点击“取
消”，用户可以取消删除申请，点击“确定”，可以成功删除申请，并提示删除成 
2） 编辑按钮：将原有信息带入，操作步骤同 3）新建任务配置一样。 
3）新建任务配置按钮：点击“新建任务配置”按钮，进入新建采集任务配置页面。见下
图： 
 
新建采集任务配置 
第一步：点击车型展示框后的“选择”按钮，弹出选择车型弹框， 如下图，在此弹框中可根据
品牌名称、车型项目、车型年份进行查询需要选择的车型。点击某一车型列表操作下的“添
加”按钮，则添加车型成功。 
52
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务配置-车型选择 
第二步：根据选择的车型选择对应的车辆范围，点击“添加车型分组”按钮，弹出选择分组弹框 
 
新建采集任务配置-分组选择 
可根据分组名称进行“查询”，“重置”，“添加”操作。 
单个添加：点击“添加”后，可以成功添加到车辆分组，如果已经添加的会提示已添加。 
批量添加：勾选一条或多条车辆分组数据，“批量添加”按钮即可使用 
第三步：查询车辆概况：点击”查看车辆概况“，弹出”车辆概况“，如下图，可以查看车辆
的信号池版本，服务池版本，车辆数量，车辆 VIN 详情。 
53
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
 
新建采集任务配置-查看车辆概况 
在查看车辆概况弹框中点击车辆 VIN 详情下的“详情”按钮，弹出“车辆 VIN 清单”，页面展
示序号，VIN 和 ECU。 
 
新建采集任务配置-查看车辆概况-车辆 VIN 清单 
第四步：配置起始时间，有 2 种配置方式。 
注：起始时间：非空，必须晚于当前时间；默认当前日期+1 天，23:00。 
结束时间：非空，必须晚于起始时间；默认当前日期+1 月，23:00，起始时间为立即执行
时，结束时间必须晚于当前时间。 
1）选指定时间：即可以自主选择时间范围。（起始时间与结束时间必须选择。） 
 
2）选择审核通过后立即执行（即采集任务开始时间就是审核通过时间，起始时间不用选择，
只需选择结束时间） 
 
第五步：输入申请标题：非空，字母、中文、数字、下划线，最长 30个字符。 
当没有输入申请标题时，输入框下弹出红色文字提示“仅支持字母、中文、数字、下划
线” 
第六步：点击下一步按钮，进入到 2确定采集配置页面-2.1确定信号范围页。 
54
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围 
第七步：选择信号范围。 
在此弹框中有 2 种添加信号的方式“通过标签选择”“通过信号选择”。 
A.当前标签选择信号为例： 
可以根据标签名称进行查询，可以点击 按钮，选择对应的标签， 
并通过标签找到对应的标签下关联的信号池版本中的信号数据， 
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围-标签选择添加信号 
即点击“详情”按钮，展示的是关联信号数量， 
1）添加关联新按钮：点击将添加该标签关联下的当前 CAN/LIN 信号池版本下的信号。击后则弹
出提示“ ”点击确定按钮则关闭“选择标签弹框”，选择的信
号将添加到确定信号范围页面中。 
2）如有添加重复信号，平台自动排重，提示“xxxx 信号已在列表中”  
B.当前以信号选择为例： 
55
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
点击信号选择按钮后，将切换到信号选择列表弹框页面，将该 CAN/LIN 信号池版本下的所有信
号展示出来， 
 
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围-信号选择 
1） 添加按钮：单个添加信号。 
2） 批量添加：点击当前页面序号左上角的选择框，可以选择当前页的所有信号，可以根据需
要勾选当前页某几个信号，然后点击批量添加按钮，则将此某几个信号添加到确定信号范
围页面中。 
3） 当信号选择完毕后，回到 2.1 确定信号范围页面，所有信号采集方式默认周期采集。 
 
图表  32-11 新建采集任务配置-2 确定采集配置-2.1确定信号范围（已选信号） 
在此页面可设置： 
不采集按钮：（即删除此信号）可批量操作，也可单个信号操作。 
设置周期采集按钮：1.在当前页面全选，进行批量操作。2.在设置采集方式下方，对每条信号
进行单个设置采集方式。 
设置完整采集按钮：1.在当前页面全选，进行批量操作。2.在设置采集方式下方，对每条信号
进行单个设置采集方式。 
第八步：当信号范围确定后，则在 2.1 确定信号范围页点击下一步按钮，进入到 2.2 确定采集
参数页面。 
56
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务配置-2 确定采集配置-2.2确定采集参数 
2.2 确定采集参数页面中：左侧分别信号密集展示 CAN/LIN 周期，CAN/LIN 完整设置页面。 
1）CAN/LIN 周期采集： 
在此页面需要设置： 
A. 采集任务配置目标 ECU,上传周期，优先级及采集任务开关。 
 
目标 EUC 默认 ICC. 
上传周期：大于 0 秒，默认 10 秒。必须输入正整数。 
优先级：高/中/低。 
：默认开，点击后按钮变为关闭状态，CAN/LIN 周期此种采集类型变为关闭采集状
态。 
注：同一采集类型存在多种密级，需要设置不同优先级。 
    当选择的信号范围密级只有一种（例如普通时）其它密级则不可设置且不可点
击。 
    当设置未完成时，点击下一步按钮，则弹出提示“设置未完成”。 
B. 采集信号配置：设置采样周期。 
 
57
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
设置“采样周期”按钮:点击“设置采样周期”按钮，弹出“设置采样周期”框，可以进行设置
选择。点击“确定”按钮，设置完成；点击“取消”按钮，可以取消。 
如下图：设置采样周期 
 
设置采样周期 
2）CAN/LIN 完整采集： 
在此页面需要设置： 
A.采集任务配置目标 ECU,上传周期，优先级及采集任务开关。 
 
目标 EUC 默认 ICC. 
上传周期：大于 0 秒，默认 10 秒。必须输入正整数。 
优先级：高/中/低。 
：默认开，点击后按钮变为关闭状态，CAN/LIN 完整此种采集类型变为关闭采集状
态。 
注：同一采集类型存在多种密级，需要设置不同优先级。 
    当选择的信号范围密级只有一种（例如普通时）其它密级则不可设置且不可点
击。 
    当设置未完成时，点击下一步按钮，则弹出提示“设置未完成”。 
第九步：在 2.2确定采集参数页面中点击下一步按钮，进入到“3 提交申请”页面。 
 
58
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
新建采集任务配置-3 提交申请 
 
提交审核按钮；点击提交审核按钮，返回到 CAN/LIN 采集任务配置-申请页面，并提示“提交
成功”。但此提交审核数据将在“审核中”页面中生成。 
保持按钮：点击此按钮，保存填写信息，返回到 CAN/LIN 采集任务配置-申请页面，并产生一条
数据，操作下显示编辑、删除按钮。 
5.审核中页面 
 
CAN/LIN 采集任务配置-审核中页面 
此页面展示的是所有在申请页面中提交审核的数据。 
1） 详情按钮：点击此按钮进入到申请详情页面，可切换到审核详情，查看审核进度。 
6.审核退回页面 
CAN/LIN 采集任务配置-审核退回页面 
此页面展示的是所有在审核中页面中被审核驳回的数据。 
1）详情按钮：点击此按钮进入到申请详情页面，可切换到审核详情，查看审核进度。 
2）重新编辑按钮：点击此按钮，将审核退回的数据，重新更新为申请状态。 
7.审核通过页面 
59
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
CAN/LIN 采集任务配置-审核通过页面 
此页面展示的是所有在审核中页面中被审核通过的数据。 
1）详情按钮：点击此按钮进入到申请详情页面，可切换到审核详情，查看审核进度。 
2）新任务按钮：点击此按钮，将复制原有的采集任务的所有数据（但需要重置采集任务起始时
间以及结束时间，显示默认时间）。 
8.列表排序：默认根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
注：  
1.当在 2.1 确定信号范围中，点击添加信号按钮后，弹出标签选择弹框，标签选择弹框中，根
据标签选择对应的信号时，当无 CAN/LIN 信号时，“添加关联信号”按钮灰色不可点击。 
3.审核中页面：审核环节： 表现形式：a/b，a 表示当前审核节点， b 代表全部审
核节点数量，此审核节点数量在【采集审核配置】中设置。 
3.审核退回页面：审核环节： 表现形式：a/b，a 表示当前审核节点，且表示在当
前节点被审核退回，b 代表全部审核节点数量，此审核节点数量在【采集审核配置】中设置。 
3.4.3 ASF 采集任务配置 
0.使用对象：系统管理员、采集申请人。 
1.定义：基于周期采集设定 ASF-SOMEIP 状态类数据，支持通过数据标签快速获取和筛选信号。
采集配置支持增量累加方式叠加之前的采集任务。 
2.查询按钮：可根据申请编号、申请标题、最新修改人进行模糊查询。 
3.重置按钮：点击“重置”按钮可以清空搜索条件。 
4.申请页面： 
60
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
ASF 采集任务配置 
1）删除按钮：点击“删除”，弹出“您确定要删除申请任务吗？”的提示。点击“取
消”，用户可以取消删除申请，点击“确定”，可以成功删除申请，并提示删除成功 
2）编辑按钮：将原有信息带入，操作步骤同 3）新建任务配置一样。 
3）新建任务配置按钮：点击“编辑”，进入新建采集任务配置页面。见下图： 
 
新建采集任务配置 
第一步：填写申请信息，步骤规则与【3.4.2 CANLIN 采集任务配置】相同  
第二步：点击下一步按钮，进入到 2确定采集配置页面-2.1确定信号范围页。 
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围 
第三步：选择信号范围。 
在此弹框中有 2 种添加信号的方式“通过标签选择”“通过信号选择”。 
61
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
信号选择： 
点击信号选择按钮后，将切换到信号选择列表弹框页面，将该 ASF-SOMEIP 信号池版本下的所有
信号展示出来， 
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围-信号选择 
4） 添加按钮：单个信号。 
5）批量添加：点击当前页面序号左上角的选择框，可以选择当前页的所有服务，可以根据需
要勾选当前页某几个信号，然后点击批量添加按钮，则将此某几个信号添加到确定信号范围页
面中。 
第四步：当信号范围确定后，则在 2.1 确定信号范围页点击下一步按钮，进入到 2.2 确定采集
参数页面。 
 
新建采集任务配置-2 确定采集配置-2.2确定采集参数 
2.2 确定采集参数页面中：左侧展示 ASF 下信号密级的设置页面。 
SOMEIP 周期采集： 
在此页面需要设置： 
62
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
A.采集任务配置目标 ECU,上传周期，优先级及采集任务开关。 
 
目标 EUC 默认 ICC. 
上传周期：大于 0 秒，默认 10 秒。必须输入正整数。 
优先级：高/中/低。 
：默认开，点击后按钮变为关闭状态，SOA 周期此种采集类型变为关闭采集状态。 
注：同一采集类型存在多种密级，需要设置不同优先级。 
    当选择的信号范围密级只有一种（例如普通时）其它密级则不可设置且不可点
击。 
    当设置未完成时，点击下一步按钮，则弹出提示“设置未完成”。 
B.采集信号配置：设置采样周期 
 
设置“采样周期”按钮:点击“设置采样周期”按钮，弹出“设置采样周期”框，可以进行设置
选择。点击“确定”按钮，设置完成；点击“取消”按钮，可以取消。 
如下图：设置采样周期 
 
设置采样周期 
第五步：在 2.2确定采集参数页面中点击下一步按钮，进入到“3 提交申请”页面。 
63
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务配置-3 提交申请 
提交审核按钮；点击提交审核按钮，返回到 ASF 采集任务配置-申请页面，并提示“提交成
功”。但此条提交数据将在“审核中”页面中生成。 
保持按钮：点击此按钮，保存填写信息，返回到 ASF 采集任务配置-申请页面，并产生一条数
据，操作下显示编辑、删除按钮。 
5.审核中、审核退回、审核通过页面：与【3.4.2 CANLIN 采集任务配置】规则相同 
3.4.4 DC/TP 采集任务配置 
0.使用对象：系统管理员、采集申请人。 
1.定义：基于周期采集设定 DC/TP 数据，支持通过数据标签快速获取和筛选信号。采集配置支
持增量累加方式叠加之前的采集任务。 
2.查询按钮：可根据申请编号、申请标题、最新修改人进行模糊查询。 
3.重置按钮：点击“重置”按钮可以清空搜索条件。 
4.申请页面： 
 
DC/TP 采集任务配置 
1）删除按钮：点击“删除”，弹出“您确定要删除申请任务吗？”的提示。点击“取
消”，用户可以取消删除申请，点击“确定”，可以成功删除申请，并提示删除成功 
2）编辑按钮：将原有信息带入，操作步骤同 3）新建任务配置一样。 
64
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3）新建任务配置按钮：点击“新建任务配置”，进入新建采集任务配置页面。见下图： 
 
新建采集任务配置 
第一步： 填写申请信息的步骤规则与【3.4.2 CANLIN 采集任务配置】相同 
第二步：点击下一步按钮，进入到 2确定采集配置页面-2.1确定信号范围页。 
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围 
第三步：选择信号范围。 
在此弹框中有 2 种添加信号的方式“通过标签选择”“通过信号选择”。规则与【3.4.3 ASF
采集任务配置】相同 
65
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务配置-2 确定采集配置-2.1 确定信号范围-标签选择添加信号 
第四步：当信号范围确定后，则在 2.1 确定信号范围页点击下一步按钮，进入到 2.2 确定采集
参数页面。 
 
新建采集任务配置-2 确定采集配置-2.2确定采集参数 
DC.DC/TP 周期采集： 
在此页面需要设置： 
A.采集任务配置目标 ECU,上传周期，优先级及采集任务开关。 
66
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
1）目标 EUC 默认 ICM。 
2）上传周期：大于等于 0 秒，默认 10 秒。输入正整数。可手动修改填写。 
3）优先级：手动选择高/中/低。 
4） ：默认开，点击后按钮变为关闭状态， DC/TP 周期此种采集类型变为关闭采集
状态。 
注：同一采集类型存在多种密级，需要设置不同优先级。 
    当选择的DataID范围密级只有一种（例如普通时）其它密级则不可设置且不可点
击。 
    当设置未完成时，点击下一步按钮，则弹出提示“设置未完成”。 
B.采集信号配置：信号源 ECU、控制参数、设置采样周期及增加SinkAPP。 
 
1）信号源ECU：默认选择 ICC，可切换选择 ICM、IPD、IAM、IMATE。 
2）控制参数：默认开启，可选择关闭，关闭后默认此 DataID 不采集。 
3）设置“采样周期”:默认 100ms，可手动修改填写。不能大于上传周期。 
4）增加SinkAPP，点击 按钮，弹出“SinkAPP 选择”弹
框， ，可单个添加
也可批量添加。 
67
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
添加按钮：选择单条记录点击”添加“后 提示"  SinkApp 已添加  "；当此 “SinkApp 已被添
加时，则提示”此 SinkApp 以添加“。 
批量添加按钮：选多条记录，点击“批量添加”后提示“SinkApp 已添加”  。 
第五步：在 2.2确定采集参数页面中点击下一步按钮，进入到“3 提交申请”页面。 
 
新建采集任务配置-3 提交申请 
提交审核按钮：点击提交审核按钮，返回到 DC/TP 采集任务配置-申请页面，并提示“提交成
功”。但此条提交数据将在“审核中”页面中生成。 
保持按钮：点击此按钮，保存填写信息，返回到 DC/TP采集任务配置-申请页面，并产生一条数
据，操作下显示编辑、删除按钮。 
5.审核中、审核退回、审核通过页面：规则与【3.4.2 CANLIN 采集任务配置】相同 
 
3.4.5 CAN/LIN 过滤任务配置 
0.使用对象：系统管理员、采集申请人。 
1.定义：设定 Can 和 Lin 指令过滤范围、生效时间、采集车辆后进入审核流程。*采集配置为覆
盖之前同类型采集任务。 
2.查询按钮：可根据申请编号、申请标题、最新修改人进行模糊查询。 
3.重置按钮：点击“重置”按钮可以清空搜索条件。 
4.申请页面： 
 
CANLIN 过滤任务配置 
68
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
1） 删除按钮：点击“删除”，弹出“您确定要删除申请任务吗？”的提示。点击“取
消”，用户可以取消删除申请，点击“确定”，可以成功删除申请，并提示删除成 
2） 编辑按钮：将原有信息带入，操作步骤同 3）新建任务配置一样。 
3）新建任务配置按钮：点击“新建任务配置”，进入新建采集任务配置页面。见下图： 
 
数据采集申请 
第一步： 填写申请信息，步骤规则与【3.4.2 CANLIN 采集任务配置】相同 
第二步：在数据采集申请页面点击下一步按钮，进入到 2 确定采集配置页面。 
 
确定CAN、LIN 的 BitMap Type 
 
确定采集配置-CAN BitMap  
69
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
确定采集配置-LIN BitMap  
CAN/LIN BitMap:默认全部关闭；灰色表示关闭，绿色表示打开。 
全部打开按钮：点击后 CAN BitMap/ LIN BitMap 全部打开，变为绿色。 
全部关闭：点击后 CAN BitMap/ LIN BitMap 全部关闭，变为灰色。 
每一行后的打开按钮，点击当前这一行变为打开状态。 
每一行后的关闭按钮，点击当前这一行变为关闭状态。 
单元格设置：点击某一单元格，切换打开/关闭状态 
第三步：点击下一步按钮，进入到 3 提交申请页面。 
 
提交申请页面 
提交审核按钮；点击提交审核按钮，返回到 CANLIN 过滤任务配置-申请页面，并提示“提交成
功”。但此条提交数据将在“审核中”页面中生成。 
保持按钮：点击此按钮，保存填写信息，返回到 CANLIN 过滤任务配置 -申请页面，并产生一条
数据，操作下显示编辑、删除按钮。 
5.审核中、审核退回、审核通过页面：规则与【3.4.2 CANLIN 采集任务配置】相同 
70
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3.4.6 事件融合采集任务配置 
0.使用对象：系统管理员、采集申请人。 
1.定义：基于边缘计算的触发事件实现 canlin、ASF-someip 信号的融合采集 
2.查询按钮：可根据申请编号、申请标题、最新修改人进行模糊查询。 
3.重置按钮：点击“重置”按钮可以清空搜索条件。 
4.申请页面： 
 
1） 删除按钮：点击“删除”，弹出“您确定要删除申请任务吗？”的提示。点击“取
消”，用户可以取消删除申请，点击“确定”，可以成功删除申请，并提示删除成 
2） 编辑按钮：将原有信息带入，操作步骤同 3）新建任务配置一样。 
3）新建任务配置按钮：点击“新建任务配置”按钮，进入新建采集任务配置页面。见下
图： 
 
第一步：填写申请信息，步骤规则与【3.4.2 CANLIN 采集任务配置】相同 
第二步：点击“下一步”按钮，进入 2.1 确定信号范围页面 
71
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
第三步：点击左侧事件采集栏的“增加”按钮，弹出“事件选择”的弹窗 
 
第四步：点击“添加”按钮，弹窗消失，返回 2.1 确定信号范围页面 
 
第五步：填写“触发条件前持续时间、触发条件后持续时间”； 
第六步：点击“添加采集数据池”按钮，进入添加采集信号页面 
72
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
第七步：点击“添加信号”按钮，跳出选择信号的弹窗，规则与【3.4.2 CANLIN 采集任务配
置】相同； 
第八步：点击“下一步”按钮，设置信号的采集参数，规则与【3.4.2 CANLIN 采集任务配置】
【3.4.3 ASF 采集任务配置】相同； 
第九步：点击“完成”按钮，返回 2.1 确定信号范围页面，点击“下一步”，进入确认采集配
置页面 
 
第十步：点击“下一步”，进入“提交申请”页面，点击“提交审核”按钮，返回“事件融合
采集任务配置-审核中”页面，新建任务成功； 
5.审核中、审核退回、审核通过：规则与【3.4.2 CANLIN 采集任务配置】相同 
3.4.7 采集任务调度管理 
0.使用对象：系统管理员、采集申请人。 
1.定义：针对采集任务进行调度管理，如任务暂停、任务恢复、任务停止等。 
2.查询按钮：可以对用户输入的内容进行查询，输入搜索条件，点击查询按钮，可以完成查询
操作。 
3.重置按钮：用户输入搜索条件，点击重置，可以取消输入结果。 
4.删除按钮：查询出来的结果列表右侧，点击“删除”按钮，可以删除一条查询记录； 
5.编辑按钮：点击“编辑”按钮，进入记录编辑页面，将原有数据系统自动带入，可在原有基
础上就行修改。 
73
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
6.新建任务调度按钮： 
第一步：点击新建任务调度按钮，进入得到新建采集任务调度页面。 
 
新建任务调度 
第二步： “填写申请标题，非空，字母、中文、数字、下划线，最长 30 个字符。 
当没有输入申请标题时，输入框下弹出红色文字提示“仅支持字母、中文、数字、下划
线”。备注（选填）。 
第三步：在新建任务调度页面，点击下一步。进入”确定任务调度配置“页面 
 
新建采集任务调度-2 确定任务调度配置 
第四步：点击“添加任务调度”按钮，弹出添加任务调度弹框，在此弹框中选择任意一条采集
任务类型，点击操作下的（暂停、停止、恢复）按钮，点击后此条数据进入到确定任务调度配
置页面。 
74
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
新建采集任务调度-2 确定任务调度配置-添加任务调度 
第五步：在 2 确定任务调度配置页面，可对单个任务设置不调度或批量设置不调度。 
不调度按钮：批量选择当前页面任务数据，不调度按钮点亮，点击弹出提示
“ ”，确定则对应的采集任务不参与调度。 
调度动作操作步骤： 
当任务状态为待运行/运行中时，可以点击暂停或停止。 
当任务状态为暂停状态时：可以点击停止或恢复。 
第六步：在 2 确定任务调度配置页面，点击下一步按钮进入到 3 提交申请页面。 
 
75
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
新建采集任务调度-3 提交申请 
在 3 提交申请页面，点击”上一步“可以返回”确定任务调度配置“页面。 
点击“保存”按钮，可以保存配置，则“采集任务调度管理-申请界面”生成一条记录。 
点击”提交审核“，则“采集任务调度管理-审核中界面”生成一条记录。 
7.审核中、审核退回、审核通过页面：规则与【3.4.2 CANLIN 采集任务配置】相同 
3.4.8 数据采集审核 
0.使用对象：采集审核员。 
1.定义：对采集申请的任务及调度任务进行审核，审核环节可配置支持不超过 5个环节，
其中任何一个审核环节退回则需重新修改发布，只有所有环节都通过才能提供给其他模块
使用。 
2.查询按钮：根据任务类型、申请标题、申请人进行模糊搜索。  
4.列表排序：根据申请时间倒序排序。最新修改的记录，排在最上方。 
5.待审核页面. 
当前页面展示的是所有提交审核的采集任务以及采集任务调度的数据。 
 
数据采集审核页面 
1）审核环节： 表现形式：a/b，a 表示当前审核节点，且表示在当前节点，b 代表
全部审核节点数量，此审核节点数量在【采集审核配置】中设置。 
 
2）审核通过/审核驳回按钮：点击此按钮，弹出审核意见弹框。 
 
76
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
数据采集审核—审核意见弹框 
    第一步：选择审核意见：审核通过/驳回 
第二步：当用户选择驳回时，需要填写 “意见描述”，规则：字母、中文、数字下划线，
最长300 个字符。 
第三步：点击确认按钮，则提示“操作成功”。 
如果存在多个审核节点，那么每个审核人员点击审核流程都是一致的。 
当点击审核驳回后，则下一个审核人员无需操作审核，直接将审核驳回的数据打回到对应
的信号池/服务池中，状态“审核驳回”列表中。 
3）详情按钮：点击进入到【3.4.8.1数据采集申请详情】。 
5.已审核页面。 
 
数据采集审核—已审核 
5.1 详情按钮：点击进入到【3.4.8.1数据采集申请详情】。 
3.4.8.1 数据采集申请详情 
 
数据采集审核—审核详情 
此页面根据不同的采集类型进入到不同的采集任务审核详情页面。 
3.5 业务监控统计 
3.7.1 数据采集任务统计 
0.使用对象：系统管理员、采集申请人。 
1.定义：以数据采集任务为轴心进行统计，提供当前数据任务的各类状态以及相关数据统
计。 
2.查询按钮：根据车辆分组、采集类型、目标 ECU、任务优先级、数据密级、任务状态、
任务编号、任务申请人进行模糊匹配查询。 
77
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
3．重置按钮：对选择的查询条件，进行清空操作。 
 
数据采集任务统计 
4.列表排序：默认根据任务编号顺序排列。 
支持用户修改排序规则为按照对应字段（任务起始时间、任务结束时间）数据进行顺序、逆序
排列。 
5.车辆运行详情按钮：点击后跳转到车辆采集状态统计页面。 
 
数据采集任务统计-车辆运行详情 
1） 此页面展示任务相关车辆配置脚本的执行清空，包括车辆配置脚本云端状态以及脚本
反馈信息，每一个版本号一条记录。 
2） 版本号：将鼠标放到每条信息的版本号上面，点击后可将 js脚本下载的本地。 
3） 列表顺序：默认根据车辆VIN、版本号正序排序。 
3.7.2 车辆采集状态统计 
0.使用对象：系统管理员、采集申请人。 
1.定义：以车辆采集状态为轴心进行统计，提供车辆执行配置脚本清空的相关数据统计。 
2.查询按钮：根据车辆分组、采集类型、目标 ECU、任务优先级、数据密级、VIN进行模糊
匹配查询。 
3．重置按钮：对选择的查询条件，进行清空操作。 
 
车辆采集状态统计 
4.列表排序：默认根据车辆 VIN、版本号顺序排序。 
5.版本号：将鼠标放到每条信息的版本号上面，点击后可将 js脚本下载的本地。 
6.相关任务详情按钮：点击进入到相关任务详情页面。 
78
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
车辆采集状态统计-相关采集任务 
1） 展示特定车上配置脚本所相关联的任务信息，包括任务申请信息等。 
2） 排序：根据任务编号顺序排序。 
3.7.3 流量监控与统计 
0.使用对象：系统管理员、采集申请人。 
1.定义：以车辆采集状态为轴心进行统计，提供车辆执行配置脚本清空的相关数据统计。 
 
流量监控与统计-按车辆查询 
2.查询按钮-按车辆查询：根据品牌名称、车型项目、销售状态、车辆类型、车辆状态、
VIN进行模糊匹配查询  
3.统计周期： 
1）统计周期：日、周、月，只能选其一，默认为日 
2）统计时间段： 
   统计周期：日，选择特定日期，默认昨日 
   统计周期：周，选择特定星期，默认为本周 
   统计周期：月，选择特定星期，默认为本月 
5．重置按钮：对选择的查询条件，进行清空操作。 
 
流量监控与统计-按车辆分组查询 
6.列表排序：根据流量大小逆序排序。 
7.统计单位：KB，MB,GB,TB，统计数四舍五入，小数点后保留两位，无流量时显示 0.00KB 
8.车辆总数：基于查询条件的所有车辆数。 
79
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
9.总流量：基于查询条件的所有上报流量总和。 
10.平均流量：基于查询条件的车辆流量平均数（总流量/上报车辆）。 
11.最大流量：基于查询条件的单车最大流量数。 
12.最小流量：基于查询条件的单车最小流量数。 
13 上报车辆数：根据上报车辆按月，周，日 0 点后统计并更新。 
14.流量详情：点击进入到【流量详情】页面。 
 
流量监控与统计-流量详情 
1）流量详情排序： 
先按照流量大小逆序排序，再按照采集方式按照技术规范的编号顺序排序再按照优先级高、中、
低排序。 
2)相关任务-详情按钮：点击弹出到相关任务信息弹框。 
 
流量监控与统计-流量详情-相关任务详情 
3） 相关任务： 
3.1）检索与此期间车辆采集相关的任务信息，默认根据任务编号顺序排列。 
3.2）只展示：当前处于运行中、暂停的任务。 
3.3）排序，按照任务编号，顺序排序。 
注：系统最多支持最近三个月的流量数据查询。 
3.8 系统管理 
3.8.1 采集审核配置 
0.使用对象：采集审核员。 
1.定义：对采集审核的环节数量以及各环节通知进行配置管理。 
2.审核环节数量：默认为 1，取值是大于等于 1 小于等于 5，设置后自增减审核通知邮箱中的
列表。输入正整数。 
3.审核通知邮箱设置：审核环节邮箱输入框： 必填，300 个字符，邮箱格式“*@*.*”，多个
邮箱时以“;” 分隔。 
4.保存按钮：默认不可用，只有用户修改过某一个字段后，此按钮可用。 
80
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
保存前，提示用户“确认保存修改信息吗？” 
保存成功后，提示用户“最新配置信息已保存”， 同时，保存按钮不可用 
5.重置按钮：点击后恢复进入此页面时的数据状态 
 
采集审核配置 
3.8.2 信号审核配置 
0.使用对象：信号审核员。 
1.定义：对信号池审核的环节数量以及各环节通知进行配置管理。 
2.审核环节数量：默认为 1，取值是大于等于 1 小于等于 5，设置后自增减审核通知邮箱中的
列表。输入正整数。 
3.审核通知邮箱设置： 
审核环节邮箱输入框： 必填，300 个字符，邮箱格式“*@*.*”，多个邮箱时以“;” 分隔。 
4.保存按钮：默认不可用，只有用户修改过某一个字段后，此按钮可用。 
保存前，提示用户“确认保存修改信息吗？” 
保存成功后，提示用户“最新配置信息已保存”， 同时，保存按钮不可用 
5.重置按钮：点击后恢复进入此页面时的数据状态 
 
信号审核配置 
3.8.3 操作日志 
0.使用对象：系统管理员。 
1.定义：记录用户的关键操作。 
2.查询按钮：根据账号、姓名、时间进行模糊匹配查询。 
3.操作人账号：为邮箱格式的操作人。 
4.操作人姓名：定义同姓名。 
5.操作时间：用户操作成功时间。 
6.列表排序：根据“最新修改时间”倒序排，最新修改的记录，排在最上方。 
81
零束 科技有限公司  Z-ONE Technology Co., Ltd.  
 
操作日志 
 
82

---

## PDF: 埋点\AF\SDK\大众AB车-Android侧数据埋点SDK空接口包及接口使用说明\datamining.pdf

datamining
概述
概述
 
本文档介绍了datamining 模块的zoneapi 接口使用方式，描述了datamining 模块 基础功能 及接口，以 及提供 示例代码作 为参 功能使用
考。 1 SDK 引用说明
2 流程图
功能使用
3 代码示例
3.1 连接datamining 服务
1 SDK 引用说明
3.2 监听连接状态
3.3 调用datamining 功…
下载sdk后，放到本地工程，例如libs目录下，然后在build.gradle 里面需 要添 加： 4 API 详细说明
dependencies { 4.1 com.zone.api.dat…
compileOnly files(‘libs\datamining-0.0.3.jar’) 4.1.1 public static 
String getApiVersion()
}
4.1.2 public 
另外，部分接口使用时有权限控制 ，需要在AndroidManifest.xml 里面声明 ，并 且使用系 统签名。
synchronized static 
DataMiningManager 
1 <uses-permission android:name="zone.permission.datamining.DATA_MINING_NORMAL" />
getInstance(Context 
context)
4.1.3 public 
2 流程图
boolean 
getServiceConnectState()
datamining datamining
Apps
4.1.4 public void 
SDK Service
registerServiceConnectionL
istener(ServiceConnectionL
istener listener)
getInstance(context)
4.1.5 public void 
return
unregisterServiceConnectio
nListener(ServiceConnectio
registerServiceConnectionListener(listener)
nListener listener)
post message
return 4.1.6 public 
boolean 
sendStructedData(EventData 
eventDataInfo)
tryConnectService()
4.1.7 public 
return
boolean 
sendUnStructedData(String 
onServiceConnected()
dataId, ArrayList<String> 
return uploadFilePathList)
4.2 com.zone.api.dat…
4.2.1 public String 
getPageId()
sendStructedData(eventDataInfo)
dispatch 4.2.2 public void 
setPageId(String pageId)
return
4.2.3 public long 
return
getEntryTime()
4.2.4 public void 
setEntryTime(long 
entryTime)
3 代码示例
4.2.5 public long 
getExitTime()
4.2.6 public void 
3.1 连接datamining 服务
setExitTime(long 
exitTime)
private boolean mIsDataManagerServiceConnected;
1
4.3 com.zone.api.dat…
private Context mContext;
2
4.3.1 public String 
private DataMiningManager mDataManager;
3
4 getKeyword()
public void init() {
5
4.3.2 public void 
    mIsDataManagerServiceConnected = false;
6
setKeyword(String 
    mDataManager = DataMining.getInstance(mContext);
7
keyword)
    mDataManager.registerServiceConnectionListener(mServiceConnection);
8
4.3.3 public int 
}
9
getIndex()
4.3.4 public void 
setIndex(int index)
4.3.5 public int 
getPages()
4.3.6 public void 
setPages(int pages)
4.3.7 public int 
3.2 监听连接状态
getCount()
4.3.8 public void 
private ServiceConnectionListener mServiceConnection = new ServiceConnectionListener() {
1
setCount(int count)
    @Override
2
4.3.9 public String 
 
    public void onServiceConnected() {
3
getSortType()
        mIsDataManagerServiceConnected = true;
4
4.3.10 public void 
    }
5
6 setSortType(String 
7    @Override
sortType)
    public void onServiceDisconnected() {
8
4.4 com.zone.api.dat…
        mIsDataManagerServiceConnected = false;
9
4.4.1 public int 
    }
10
getSpeed()
};
11
4.4.2 public void 
setSpeed(int speed)
4.4.3 public int 
getCarGearStatus()
4.4.4 public void 
setCarGearStatus(int 
carGear)
4.4.5 public int 
getBatteryLevel()
4.4.6 public void 
setBatteryLevel(int 
batteryLevel)
4.4.7 public int 
getOdometer()
4.4.8 public void 
setOdometer(int 
carOdometer)
4.5 com.zone.api.dat…
4.6 com.zone.api.dat…
4.6.1 public String 
getDataId()
4.6.2 public int 
getTriggerMethod()
4.6.3 public int 
getTriggerDetailMethod()
4.6.4 public long 
getEventTime()
4.6.5 public String 
getUserId()
4.6.6 public String 
getVinCode()
4.6.7 public int 
getAccountType()
4.6.8 public int 
getCarModel()
4.6.9 public int 
getProtoVersion()
4.6.10 public 
String getAppId()
4.6.11 public 
String getAppVersion()
4.6.12 public 
AppInfo getAppInfo()
4.6.13 public 
BrowseInfo 
getBrowserInfo()
4.6.14 public 
CarInfo getCarInfo()
4.6.15 public 
LocationInfo 
getLocationInfo()
4.6.16 public 
MediaInfo getMediaInfo()
4.6.17 public 
NetInfo getNetInfo()
4.6.18 public 
PoiInfo getPoiInfo()
4.6.19 public 
3.3 调用datamining 功能接 口
CustomInfo[] 
getParamInfo()
private void entryPage() {
1
4.6.20 public void 
    mPageEntryTime = System.currentTimeMillis();
2
 
setDataId(String dataId)
}
3
4.6.21 public void 
4
private void entryPage() { setTriggerMethod(int 
5
    mPageExitTime = System.currentTimeMillis();
6 triggerMethod)
}
7
4.6.22 public void 
8
setTriggerDetailMethod(int 
public void doSomething() {
9
triggerDetailMethod)
    if (!mIsDataManagerServiceConnected) {
10
4.6.23 public void 
        Log.e(TAG, "DataManager service is not connected!");
11
        return;
12 setEventTime(long 
    }
13
eventTime)
14
4.6.24 public void 
    try {
15
setUserId(String userId)
        EventData eventDataInfo;
16
4.6.25 public void 
17        eventDataInfo = new EventData();
setAccountType(int 
18
        // 必填字段：不填充的话，调用sendStructedData() 接口会返回失败。
19
accountType)
        eventDataInfo.setDataId("03000000000000000000000000000001");
20
4.6.26 public void 
        eventDataInfo.setTriggerMethod(5);
21
setCarModel(int carModel)
        eventDataInfo.setTriggerDetailMethod(500);
22
4.6.27 public void 
        eventDataInfo.setEventTime(System.currentTimeMillis());
23
        eventDataInfo.setAppId("iqiyi"); setVinCode(String 
24
        eventDataInfo.setAppVersion("1.0.0");
25
vinCode)
26
4.6.28 public void 
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
27
setAppId(String appId)
28        AppInfo appInfo = new AppInfo();
4.6.29 public void 
        appInfo.setEntryTime(mPageEntryTime);
29
        appInfo.setExitTime(mPageExitTime); setAppVersion(String 
30
        appInfo.setPageId("PageId");
31 appVersion)
        eventDataInfo.setAppInfo(appInfo);
32
4.6.30 public void 
33
setProtoVersion(int 
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
34
protoVersion)
        LocationInfo locationInfo = new LocationInfo();
35
4.6.31 public void 
        locationInfo.setAddress(" 上海市嘉定区安研路201 号");
36
37        locationInfo.setAltitude(100); setAppInfo(AppInfo 
        locationInfo.setCity("Shanghai");
38
appInfo)
        locationInfo.setCountry("China");
39
4.6.32 public void 
        locationInfo.setLatitude(26.57f);
40
setBrowserInfo(BrowseInfo 
        locationInfo.setLongitude(106.72f);
41
browserInfo)
        eventDataInfo.setLocationInfo(locationInfo);
42
43 4.6.33 public void 
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
44
setCarInfo(CarInfo 
        NetInfo netInfo = new NetInfo();
45
carInfo)
        netInfo.setIp("172.31.3.48");
46
4.6.34 public void 
        netInfo.setIsp(0x00);
47
setLocationInfo(LocationIn
48        netInfo.setMacAddress("c6:cc:19:91:56:3d");
        netInfo.setNetFlow(10); fo locationInfo)
49
        netInfo.setNetworkType(0x01);
50
4.6.35 public void 
        eventDataInfo.setNetInfo(netInfo);
51
setMediaInfo(MediaInfo 
52
mediaInfo)
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
53
4.6.36 public void 
        PoiInfo poiInfo = new PoiInfo();
54
setNetInfo(NetInfo 
        poiInfo.setAverageCost(100);
55
        poiInfo.setName(" 北京奥林匹克公园");
56 netInfo)
57        poiInfo.setScore(6);
4.6.37 public void 
        poiInfo.setStyle("relax");
58
setPoiInfo(PoiInfo 
        poiInfo.setType(0x02);
59
poiInfo)
        poiInfo.setWaitTime(15);
60
4.6.38 public void 
        eventDataInfo.setPoiInfo(poiInfo);
61
62 setParamInfo(CustomInfo[] 
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
63
paramInfo)
        CarInfo carInfo = new CarInfo();
64
4.7 com.zone.api.dat…
        carInfo.setBatteryLevel(70);
65
4.7.1 public float 
        carInfo.setCarGearStatus(0x03);
66
getLongitude()
        carInfo.setOdometer(100);
67
68        carInfo.setSpeed(80); 4.7.2 public void 
        eventDataInfo.setCarInfo(carInfo);
69
setLongitude(float 
70
longitude)
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
71
4.7.3 public float 
        BrowseInfo browseInfo = new BrowseInfo();
72
getLatitude()
        browseInfo.setCount(100);
73
        browseInfo.setIndex(1); 4.7.4 public void 
74
        browseInfo.setKeyword(" 娱乐");
75 setLatitude(float 
        browseInfo.setPages(10);
76
latitude)
77        browseInfo.setSortType(" 按时间排序");
4.7.5 public float 
        eventDataInfo.setBrowserInfo(browseInfo);
78
getAltitude()
79
80
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
4.7.6 public void 
81
        MediaInfo mediaInfo = new MediaInfo();
setAltitude(float 
82
        mediaInfo.setAlbum(" 专辑");
altitude)
83
        mediaInfo.setArtist(" 艺术家");
4.7.7 public String 
84
        mediaInfo.setChannelId("ChannelId");
85
getCountry()
        mediaInfo.setDuration(180);
 
86
        mediaInfo.setName(" 星星点灯"); 4.7.8 public void 
87
        mediaInfo.setStyle(0x00);
setCountry(String 
88
        eventDataInfo.setMediaInfo(mediaInfo);
country)
89
4.7.9 public String 
90
        // 可选字段：不填充的话，不会导致调用sendStructedData() 接口返回失败。
91
getCity()
        CustomInfo customInfo = new CustomInfo();
92
        customInfo.setKey("testkey1"); 4.7.10 public void 
93
        customInfo.setValue("testvalue1");
setCity(String city)
94
        eventDataInfo.setParamInfo(new CustomInfo[]{customInfo});
4.7.11 public 
95
        customInfo.setKey("testkey2");
String getAddress()
96
        customInfo.setValue("testvalue3");
97 4.7.12 public void 
        eventDataInfo.setParamInfo(new CustomInfo[]{customInfo});
98
setAddress(String 
        customInfo.setKey("testkey3");
99
        customInfo.setValue("testvalue3");
address)
100
        eventDataInfo.setParamInfo(new CustomInfo[]{customInfo});
4.8 com.zone.api.dat…
101
4.8.1 public String 
102
        if (!mDataManager.sendStructedData(eventDataInfo)) {
103 getName()
            Log.e(TAG, "sendStructedData failed!");
104
4.8.2 public void 
        }
105
    } catch (RemoteException ex) {
setName(String songName)
106
        ex.printStackTrace();
4.8.3 public int 
107
    }
getDuration()
108
}
4.8.4 public void 
setDuration(int 
4 API 详细说明
songDuration)
4.8.5 public int 
4.1 com.zone.api.datamining.DataMiningManager getStyle()
4.8.6 public void 
package com.zone.api.datamining
setStyle(int songStyle)
4.8.7 public String 
数据埋点接口类.
getAlbum()
4.1.1 public static String getApiVersion() 4.8.8 public void 
setAlbum(String 
获取API 版本号.
songAlbum)
4.8.9 public String 
Returns: 版本号
getArtist()
4.1.2 public synchronized static DataMiningManager getInstance(Context context)
4.8.10 public void 
获取DataMining 的实例. setArtist(String artist)
4.8.11 public 
Parameters: context — context
String getChannelId()
Returns: DataMining 的实例
4.8.12 public void 
4.1.3 public boolean getServiceConnectState() setChannelId(String 
channelId)
获取服务连接状态.
4.9 com.zone.api.dat…
Returns: 服务连接状态 4.9.1 public int 
getNetworkType()
4.1.4 public void registerServiceConnectionListener(ServiceConnectionListener listener)
4.9.2 public void 
注册服务连接状态监听器.
setNetworkType(int 
networkType)
Parameters: listener — 监听器对象
4.9.3 public int 
4.1.5 public void unregisterServiceConnectionListener(ServiceConnectionListener listener)
getIsp()
4.9.4 public void 
取消注册服务连接状态监听器.
setIsp(int isp)
Parameters: listener — 监听器对象 4.9.5 public String 
getIp()
4.1.6 public boolean sendStructedData(EventData eventDataInfo)
4.9.6 public void 
发送结构型埋点数据。
setIp(String ipAddress)
4.9.7 public String 
Parameters: eventDataInfo — 埋点数据
getMacAddress()
Returns: 埋点数据发送结果
4.9.8 public void 
调用该接口，需要的权限： setMacAddress(String 
macAddress)
权限名称 安全级别
4.9.9 public int 
getNetFlow()
zone.permission.datamining.DATA_MINING_NORMAL signature
4.9.10 public void 
4.1.7 public boolean sendUnStructedData(String dataId, ArrayList<String> uploadFilePathList)
setNetFlow(int netFlow)
4.10 com.zone.api.da…
发送非结构型埋点数据。
Deprecated 4.10.1 public 
Parameters: String getName()
dataId — dataId 埋点事件ID
4.10.2 public void 
uploadFilePathList — 待发送的非结构化埋点文件路径列表
setName(String poiName)
 
4.10.3 public int 
Returns: 埋点数据发送结果
getType()
调用该接口，需要的权限：
4.10.4 public void 
setType(int poiType)
权限名称 安全级别
4.10.5 public int 
getScore()
zone.permission.datamining.DATA_MINING_NORMAL signature
4.10.6 public void 
setScore(int poiScore)
4.2 com.zone.api.datamining.bean.AppInfo
4.10.7 public 
String getStyle()
package com.zone.api.datamining.bean
4.10.8 public void 
页面信息.
setStyle(String poiStyle)
4.10.9 public int 
4.2.1 public String getPageId()
getAverageCost()
页面id.
4.10.10 public void 
setAverageCost(int 
Returns: 页面id
averageCost)
4.2.2 public void setPageId(String pageId)
4.10.11 public int 
getWaitTime()
设置页面id.
4.10.12 public void 
Parameters: pageId — 页面id
setWaitTime(int waitTime)
4.2.3 public long getEntryTime()
进入页面时间.
Returns: 进入页面时间
4.2.4 public void setEntryTime(long entryTime)
设置进入页面时间.
Parameters: entryTime — 进入页面时间
4.2.5 public long getExitTime()
离开页面时间.
Returns: 离开页面时间
4.2.6 public void setExitTime(long exitTime)
设置离开页面时间.
Parameters: exitTime — 离开页面时间
4.3 com.zone.api.datamining.bean.BrowseInfo
package com.zone.api.datamining.bean
用户搜索及浏览信息.
4.3.1 public String getKeyword()
关键词.
Returns: 关键词
4.3.2 public void setKeyword(String keyword)
设置关键词.
Parameters: keyword — 关键词
4.3.3 public int getIndex()
用户选择的条目序号.
Returns: 用户选择的条目序号
4.3.4 public void setIndex(int index)
设置用户选择的条目序号.
Parameters: index — 用户选择的条目序号
4.3.5 public int getPages()
页数.
Returns: 页数
4.3.6 public void setPages(int pages)
设置页数.
 
Parameters: pages — 页数
4.3.7 public int getCount()
数量.
Returns: 数量
4.3.8 public void setCount(int count)
设置数量.
Parameters: count — 数量
4.3.9 public String getSortType()
排序方式.
Returns: 排序方式
4.3.10 public void setSortType(String sortType)
设置排序方式.
Parameters: sortType — 排序方式
4.4 com.zone.api.datamining.bean.CarInfo
package com.zone.api.datamining.bean
车机信息.
4.4.1 public int getSpeed()
车速.
Returns: 车速
4.4.2 public void setSpeed(int speed)
设置车速.
Parameters: speed — 车速
4.4.3 public int getCarGearStatus()
档位.
Returns: 档位
4.4.4 public void setCarGearStatus(int carGear)
设置档位.
Parameters: carGear — 档位
4.4.5 public int getBatteryLevel()
电量状态.
Returns: 电量状态
4.4.6 public void setBatteryLevel(int batteryLevel)
设置电量状态.
Parameters: batteryLevel — 电量状态
4.4.7 public int getOdometer()
里程.
Returns: 里程
4.4.8 public void setOdometer(int carOdometer)
设置里程.
Parameters: carOdometer — 里程
4.5 com.zone.api.datamining.bean.CustomInfo
package com.zone.api.datamining.bean
自定义参数.
4.6 com.zone.api.datamining.bean.EventData
package com.zone.api.datamining.bean
 
埋点数据结构.
4.6.1 public String getDataId()
事件编号.
Returns: 事件编号
4.6.2 public int getTriggerMethod()
触发方式.
Returns: 触发方式
4.6.3 public int getTriggerDetailMethod()
触发方式（详）.
Returns: 触发方式（详）
4.6.4 public long getEventTime()
事件时间.
Returns: 事件时间
4.6.5 public String getUserId()
用户id.
Returns: 用户id
4.6.6 public String getVinCode()
Vin 码.
Returns: Vin 码
4.6.7 public int getAccountType()
账号类型.
Returns: 账号类型
4.6.8 public int getCarModel()
车型.
Returns: 车型
4.6.9 public int getProtoVersion()
.proto 版本.
Returns: .proto 版本
4.6.10 public String getAppId()
应用Id.
Returns: 应用Id
4.6.11 public String getAppVersion()
应用版本.
Returns: 应用版本
4.6.12 public AppInfo getAppInfo()
页面信息.
Returns: 页面信息
4.6.13 public BrowseInfo getBrowserInfo()
用户搜索及浏览信息.
Returns: 用户搜索及浏览信息
4.6.14 public CarInfo getCarInfo()
车辆信息.
Returns: 车辆信息
4.6.15 public LocationInfo getLocationInfo()
地理位置信息.
Returns: 地理位置信息
 
4.6.16 public MediaInfo getMediaInfo()
媒体信息.
Returns: 媒体信息
4.6.17 public NetInfo getNetInfo()
网络信息.
Returns: 网络信息
4.6.18 public PoiInfo getPoiInfo()
POI 信息.
Returns: POI 信息
4.6.19 public CustomInfo[] getParamInfo()
自定义信息.
Returns: 自定义信息
4.6.20 public void setDataId(String dataId)
设置事件编号.
Parameters: dataId — 事件编号
4.6.21 public void setTriggerMethod(int triggerMethod)
设置触发方式.
Parameters: triggerMethod — 触发方式
4.6.22 public void setTriggerDetailMethod(int triggerDetailMethod)
设置触发方式( 详).
Parameters: triggerDetailMethod — 触发方式( 详)
4.6.23 public void setEventTime(long eventTime)
设置事件时间.
Parameters: eventTime — 事件时间
4.6.24 public void setUserId(String userId)
设置用户id.
Parameters: userId — 用户id
4.6.25 public void setAccountType(int accountType)
设置账号类型.
Parameters: accountType — 账号类型
4.6.26 public void setCarModel(int carModel)
设置车型.
Parameters: carModel — 车型
4.6.27 public void setVinCode(String vinCode)
设置Vin 码.
Parameters: vinCode — Vin 码
4.6.28 public void setAppId(String appId)
设置应用Id.
Parameters: appId — 应用Id
4.6.29 public void setAppVersion(String appVersion)
设置应用版本.
Parameters: appVersion — 应用版本
4.6.30 public void setProtoVersion(int protoVersion)
设置.proto 版本.
Parameters: protoVersion — .proto 版本
4.6.31 public void setAppInfo(AppInfo appInfo)
设置页面信息.
 
Parameters: appInfo — 页面信息
4.6.32 public void setBrowserInfo(BrowseInfo browserInfo)
设置用户搜索及浏览信息.
Parameters: browserInfo — 用户搜索及浏览信息
4.6.33 public void setCarInfo(CarInfo carInfo)
设置车辆信息.
Parameters: carInfo — 车辆信息
4.6.34 public void setLocationInfo(LocationInfo locationInfo)
设置地理位置信息.
Parameters: locationInfo — 地理位置信息
4.6.35 public void setMediaInfo(MediaInfo mediaInfo)
设置媒体信息.
Parameters: mediaInfo — 媒体信息
4.6.36 public void setNetInfo(NetInfo netInfo)
设置网络信息.
Parameters: netInfo — 网络信息
4.6.37 public void setPoiInfo(PoiInfo poiInfo)
设置POI 信息.
Parameters: poiInfo — POI 信息
4.6.38 public void setParamInfo(CustomInfo[] paramInfo)
设置自定义信息.
Parameters: paramInfo — 自定义信息
4.7 com.zone.api.datamining.bean.LocationInfo
package com.zone.api.datamining.bean
地理位置.
4.7.1 public float getLongitude()
经度.
Returns: 经度
4.7.2 public void setLongitude(float longitude)
设置经度.
Parameters: longitude — 经度
4.7.3 public float getLatitude()
纬度.
Returns: 纬度
4.7.4 public void setLatitude(float latitude)
设置纬度.
Parameters: latitude — 纬度
4.7.5 public float getAltitude()
海拔.
Returns: 海拔
4.7.6 public void setAltitude(float altitude)
设置海拔.
Parameters: altitude — 海拔
4.7.7 public String getCountry()
国家.
Returns: 国家
 
4.7.8 public void setCountry(String country)
设置国家.
Parameters: country — 国家
4.7.9 public String getCity()
城市.
Returns: 城市
4.7.10 public void setCity(String city)
设置城市.
Parameters: city — 城市
4.7.11 public String getAddress()
地址.
Returns: 地址
4.7.12 public void setAddress(String address)
设置地址.
Parameters: address — 地址
4.8 com.zone.api.datamining.bean.MediaInfo
package com.zone.api.datamining.bean
媒体设置信息.
4.8.1 public String getName()
歌曲.
Returns: 歌曲
4.8.2 public void setName(String songName)
设置歌曲.
Parameters: songName — 歌曲
4.8.3 public int getDuration()
音乐播放时长（秒）.
Returns: 音乐播放时长（秒）
4.8.4 public void setDuration(int songDuration)
设置音乐播放时长（秒）.
Parameters: songDuration — 音乐播放时长（秒）
4.8.5 public int getStyle()
歌曲风格.
Returns: 歌曲风格
4.8.6 public void setStyle(int songStyle)
设置歌曲风格.
Parameters: songStyle — 歌曲风格
4.8.7 public String getAlbum()
专辑.
Returns: 专辑
4.8.8 public void setAlbum(String songAlbum)
设置专辑.
Parameters: songAlbum — 专辑
4.8.9 public String getArtist()
歌手.
Returns: 歌手
4.8.10 public void setArtist(String artist)
 
设置歌手.
Parameters: artist — 歌手
4.8.11 public String getChannelId()
电台id.
Returns: 电台id
4.8.12 public void setChannelId(String channelId)
设置电台id.
Parameters: channelId — 电台id
4.9 com.zone.api.datamining.bean.NetInfo
package com.zone.api.datamining.bean
车机网络信息.
4.9.1 public int getNetworkType()
网络类型.
Returns: 网络类型
4.9.2 public void setNetworkType(int networkType)
设置网络类型.
Parameters: networkType — 网络类型
4.9.3 public int getIsp()
网络运营商.
Returns: 网络运营商
4.9.4 public void setIsp(int isp)
设置网络运营商.
Parameters: isp — 网络运营商
4.9.5 public String getIp()
IP 地址.
Returns: IP 地址
4.9.6 public void setIp(String ipAddress)
设置IP 地址.
Parameters: ipAddress — IP 地址
4.9.7 public String getMacAddress()
网卡网络地址.
Returns: 网卡网络地址
4.9.8 public void setMacAddress(String macAddress)
设置网卡网络地址.
Parameters: macAddress — 网卡网络地址
4.9.9 public int getNetFlow()
流量.
Returns: 流量
4.9.10 public void setNetFlow(int netFlow)
设置流量.
Parameters: netFlow — 流量
4.10 com.zone.api.datamining.bean.PoiInfo
package com.zone.api.datamining.bean
POI 点属性信息.
 
4.10.1 public String getName()
poi 信息点名称.
Returns: poi 信息点名称
4.10.2 public void setName(String poiName)
设置poi 信息点名称.
Parameters: poiName — poi 信息点名称
4.10.3 public int getType()
poi 信息点类型.
Returns: poi 信息点类型
4.10.4 public void setType(int poiType)
设置poi 信息点类型.
Parameters: poiType — poi 信息点类型
4.10.5 public int getScore()
poi 评分.
Returns: poi 评分
4.10.6 public void setScore(int poiScore)
设置poi 评分.
Parameters: poiScore — poi 评分
4.10.7 public String getStyle()
poi 风格.
Returns: poi 风格
4.10.8 public void setStyle(String poiStyle)
设置poi 风格.
Parameters: poiStyle — poi 风格
4.10.9 public int getAverageCost()
poi 人均消费.
Returns: poi 人均消费
4.10.10 public void setAverageCost(int averageCost)
设置poi 人均消费.
Parameters: averageCost — poi 人均消费
4.10.11 public int getWaitTime()
poi 等待时长(min).
Returns: poi 等待时长(min)
4.10.12 public void setWaitTime(int waitTime)
设置poi 等待时长(min).
Parameters: waitTime — poi 等待时长(min)

---

## PDF: 埋点\C\1.X埋点PRD\PDD_埋点项目_V1.0_外发版.pdf

PRD_埋点_V1.0
1简介Introduction
1.1版本和状态VersionandStatus
当前版本：V 1. 0
评审状态：已评 审
开发状态：未开始
1.2修订历史History
版 本号 日期 修 订人 修 订 记 录
V 0 .1 2 0 2 5 . 0 3 .2 4
...
创 建 文 档
V 0 .2 2 0 2 5 . 0 6 .0 6
X u Sh i q i
更 新 4 . 4 . 3 埋 点 权 限 管 理
D o n g M e n g l i n
增 加 第 2 章 需 求 描 述
增 加 3 . 1 埋 点 流 程 描 述
V 0 .3 2 0 2 5 . 0 6 .1 2
X u Sh i q i 更 新 1 . 5 功 能 列 表
D o n g M e n g l i n 增 加 第 5 章 系 统 依 赖
更 新 第 三 章 业 务 架 构
V 1 .0 2 0 2 5 . 0 6 .1 9
D o n g M e n g l i n
更 新 4 . 7 . 3 ： 用 户 隐 私 协 议 相 关 PO+ 文 档 链 接 补 充 描
述 增 加第 7 章 附件
1.3目的Functionalobjective(benefit)
.
本文 档旨 在统 一规 范车 机端 各应 用（ 包括 H M I ）的 埋 点工具接入方式 与数据结构要求。
.
通过 标准 化埋 点基 础能 力， 确保 各端 一致 性的 数据 采集 、上 传与 分析 支持 ，构 建完 整的 用户 行为 数据 链路，支撑产品 运营与数据决策。
1.4定义和缩写Abbreviations
定义和缩写 描述
Session
是指用户在 A P P上连续活跃时的 一系列行为（例如浏览、点 击、播放）
事件 是指用户的一种 或一类行为，例如：用户观 看视频、用户评论等
1.5功能列表
F u P riority
L0 L1 L2 L3 CEA功能描述 FO IPD
li
ID
CEA- 2644 联网 埋点数据采集和上传 埋点数据采集和上 座舱Ap p埋点 通过全局+自定义埋点S DK收集车机端的用户行为数据 P 0 IPD5.0
H uan g
Bu ryPo intData Collect i 传
服务 Co ckp itApp Buried ，并上传到云端埋点平台 ,Xinyu
o nan du ploa d Bu ryPo intData Coll P oint s
IOV Co llect u serb e h a vio ront hevehiclesid ethrou gha glo bal (CARTSE)
ection and up load
serv
an d
ice
cu sto mb uriedp oint SDK,and up load itto thecloud bu ri
ed p ointp latfo rm .
CEA- 2646 联网 埋点数据采集和上传 埋点数据采集和上 J iang , P 0 IPD5.0
埋点平台 埋点平台具有埋点数据存储，分析/报表，同步至J V后台
Xia
服务 Bu ryPo intData Collect i 传
Bu ried Poin tsPlatfor 的能力
(C|GC-3)
o nan du ploa d Bu ryPo intData Coll
m
IOV
Bu ried p o in t p la t fo rm h a sth eab ilit ytosto reb uri
ection and up load
serv
ed po intd a ta ,a n alyz e/re p o rt ,a n d syn c h ro nizet
ice
o JV backend .
联网
CEA- 2645 埋点数据采集和上传 埋点数据采集和上 M ob ileSDK埋点 在手机远控 S DK中加入埋点 S DK，并上传到云端埋点平台 Xiao , P 0 IPD5.0
Bu ryPo intData Collect i 传 W enjin
服务 M obileSDKBuried
Ad dt hebu ried po intS DK tot hemo bileremot eco nt
o nan du ploa d Bu ryPo intData Coll P oint s (C|GC-3)
IOV rolS DK and up load itto thecloud bu ried po intp latfo
ection and up load
serv
rm
ice
2需求描述 Requestdescription
2.1应用场景Storyline
随着 智能 网联 汽车 的普 及， 车机 系统 作为 用户 与车 辆交 互的 核心 枢纽 ，其 体验 优劣 直接 影响 用户 满意 度和 品牌 忠诚 度。 然而，当前车机 系统在运营和优化过
程中面临以下关键挑战：
1.用户行为分析盲区
.
用户 操作 路径 （如 频繁 跳转 的菜 单、 未完 成的 语音 指令 ）缺 乏完 整埋 点记 录， 导致 产品 团队 无法 精准 定位 交互 卡点 ，优 化方 向依 赖主 观猜
测。
2.性能问题响应滞后
.
现有 监控 仅能 捕捉 系统 级崩 溃， 对界 面加 载延 迟、 语音 唤醒 失败 等细 分场 景的 性能 瓶颈缺乏实时追 踪，问题修复周期长。
3.营销资源浪费
.
用户 画像 停留 在基 础标 签（ 如地 域、 车型 ） ， 无法 识别 “ 通勤 时段 偏好 导航 ”“ 周末 高频 使用 亲子 娱乐 功能 ”等场 景化 需求 ，推 送内 容转
化率低下。
4.售后诊断效率低下
.
车辆 出现 车机 死机 或功 能异 常时 ， 4S 店难 以通过模糊描述 复现问题，需反复调试。
应用场景列表Storylinelist
场景 埋点数据示例 数据应用(仅作为示例，具体数据应用取决于实际需求)
用户行为分析优 化
.
.
建立 用户 操作 路径 图谱
功能 点击 事件 （空 调 /导航 /
. .
语音等） 识别 高频 操作 优化 UI 布局
. .
分析 中断 点改 进交 互流 程
页面 停留 时长
操作 中断 记录
性能监控
.
.
实时 性能 监控 看板
关键 性能 指标 （启 动 /加载 时
. .
间）
智能 阈值 告警 系统
. .
系统 资源 占用 数据 场景 化性 能分 析
异常 事件 错误 码
精准营销推荐
. . .
场景 化行 为数 据 动态 用户 分群 模型
. 场景 化实 时推 荐
第三 方服 务使 用记 录
.
营销 效果 闭环 分析
智能故障诊断
. .
系统 异常 事件 捕获 基于 埋点 数据 重建 故障 场景
. .
崩溃 前操 作路 径 输出 可视 化报 告， 自动 标注 可能 故障 模块
3业务架构
3.1埋点全链路流程图（初版）
一、标准数据采集处理流程
1.数据采集：车机 端需按规范接入 S DK，支持全埋点和 自定义埋点两种采集方式。
2. 数据 处理 ：采 集数 据统 一上 报至 CE A O ne B ac k en d 平台 ， OneB ack end 需将埋点数据同 步至J V s后台。
3. 数据分析工具： O neB ackend需集成火山提供 的数据分析平台。
二、自主数据采集模式
1.适用场景：JV s自研的O neApp可选择独立采集方案；
2. 特点说明：数据 不经过CEA 平台处理，相关 规范不在本方案范围内。
4详细功能说明
4 .1车机端埋点模块
.
CEA 埋点S DK能力由供应商提 供
.
各应 用可 根据 需求 进行 代码 埋点 的开 发工 作
4.1.1接入规范
主要覆盖安卓， IO S，小程序，H 5等
连接地址：
.
S DK 集成 - - 增长 分析 Dat aF i nd e r - 火山 引擎
.
F in d er 数据 接入 概述 - - 增长 分析 Da taF in d er - 火山 引擎
各业务及功能可参考接入规范，按需接入。
4.1.2埋点类型
参考 埋点 类型 介绍 ： 埋点 、全 埋点 - - 增长 分析 Dat aF i nd er- 火山引擎
4.1.2.1全埋点
.
全量 埋点 的适 用场 景： 适用 于应 用首 页、 子级 页面 、按 钮状 态等 ，简 单分 析 UV 、P V 、点 击量 等基 础指 标； 分析 或统 计需 求简 单， 不需 要对 埋点 事件
进行传参等自定义属性设置的事件；
.
全量 埋点 的优 势： 不需 要开 发人 员手 动录 入， 对业 务代 码侵 入性 最小 ，工 作量少；部署 S DK后数据就一直在 收集，支持数据回溯；
.
全埋 点预 置事 件和 属性 可参 考： 全埋 点预 置事 件和 属性 - - 增长 分析 Da taF in d er - 火山 引擎
4.4.2.2代码埋点（自定义埋点）
.
代码 埋点 的适 用场 景： 适用 于采 集分 析业 务相 关字 段逻 辑紧 密的 场景 ，分 析更 聚焦 ；尤 其是 一些 非点 击的 、不 可视 的行 为， 非代 码埋 点实 现不 可例
如： 搜索 结果 返回 、注 册结 果返 回、 B an ne r 、楼 层、 个性 化推 荐/千人千面页面
.
代码埋点的优势 ：业务信息完善；事件、属 性、上报时机等可以自定义 和控制能够完整还原用户行 为链路；
.
代码 埋点 数据 规范 参考 ： 预置 属性 总表 - - 增长 分析 Dat aF in d er - 火山 引擎
.
各业 务及 功能 可参 考代 码埋 点规 范， 按需 埋点
.
各类 型 S DK 集成 概述 参考 ：F in d er 数据 接入 概述 - - 增长 分析 Dat aF i nd e r - 火山 引擎
.
细分 类型 S DK 集成 说明 ，以 安卓 举例 ： A nd r o id S D K A P I 说明 - - 增长 分析 Dat aF in d er - 火山 引擎 ，其 它类 型， 如 iO S ，小 程序 ，H 5 等可 遵循 火山 开发
者指南页面指导
4 .2 Mobi leSDK埋点
M ob i le S D K需具 备埋 点和 数据 上传 到 O neB ac k e nd的能力，需提供 给宿主A P P数据开关的能力 。
4 .3埋点权限管理
4.3.1功能概述
埋点 数据 上报 功能 严格 遵循 合规 要求 ，通 过隐 私协 议向 用 户明示采集内容 ，并提供开关控件供用户自 主管理数据采集权限。
*注： 用户 隐私 协议 弹窗 逻辑 及交 互请 以隐 私协 议P R D 为主 ，本 章节 不做 阐述 ，待 用户 隐私 协议 P O @j u nxiang Zhang 更新后在此处补 充文档链接。
4.3.2功能细节
1、开关位置：
.
位于【大屏车控车设- 通用】界面；
.
开 关 项 名 称 参 考 " 允 许 数 据 采 集 " 、 “ 加 入 智 能 用 户 体 验 改 进 计 划 ”
.
副标 题文 案参 考 "允许 将用 户数 据用 于提 升交 互整 体体 验 “
*具体的开关项名称及文案以H MI确认为主。
2、开关采集状态：
.
首次激活车辆时：默认关闭；
.
采集 开关 需主 动监 听隐 私协 议状 态， 用户 同意 隐私 协议 后： 自 动开启，用户不 同意则保持默认关闭。
3、交互逻辑：
①、用 户首 次激 活车 辆， 弹出 隐私 协议 ，用 户同意后，数据 采集开关自动开启，开始采 集用户行为数据。
②、用户手动操作：
.
用户 将开 关按 钮从 开启 状态 手动 关闭 ，立 即停 止埋点数据采集 行为，无需二次确认。
.
用户将开关按钮 从关闭状态手动打开，正常采集数据。
4、数据处理规则：
①、数据采集开关操作：
.
关闭 状态 下的 数据 处理 ：立 即停 止采 集新 数据 ，已 上传 的数 据按 隐私 协议 规定 处理 ，本 地未 上传 的原 始数 据应 进行 匿名 化处 理上 传。 （匿 名化 处理
标准 ：移 除所 有直 接个 人标 识符 包含 UID 、设备ID等） ;
.
开启状态下的数 据处理：正常采集所有埋点 数据上传。
② 、无 网络 情况 下： 本地 缓存 ，需 根据 车机 容量 设定 上限 （如 15 天的 数据 量， 可根 据实 际数 据量 的大小进行动态调 整），若达到上限，按照先 进先出原则
由 新数据覆盖掉之前数据，待网络恢复后再上报数据。
5、账号独立授权
.
每个 用户 账号 应维 护独 立的 数据 采集 状态 ，需 存本地+云端，本地实时 同步给云端。
.
未登录用户应使 用设备本地默认设置，登录 后同步账号设置；
.
账号切换时应立 即加载相应用户的授权状态 。
6、日志记录
.
记录所有开关操 作（时间、设备、操作人、 数据收集开关操作） ， 至少保留6个月；
操 作 时 间 操 作 设 备 操 作 人 操 作 类 型
X X X
精 确 到 毫 秒 设 备 I D 埋 点 数 据 采 集 开 启 / 埋 点 数 据 采 集 关 闭
.
日志记录存储位 置：本地+云端
5系统依赖说明
依赖项 内容描述 参考章
节
用户隐私协议 埋点权限管理， 交互逻辑，状态同步等
4. 4. 3
H M I 按照 用户 隐私 协议 统一 位置 要求 ，在 用户 界面 设置 “ 埋点 数据 采集 ”开关 ，用 于用 户自 行控 制是 否 允许收集用户行 为数
4. 4. 3
据
H M I及用户隐私 用户隐私协议文 言
4. 4. 3. 1
协议
6附件
已完 成 J V s 的埋 点需 求确 认， 并将 埋点 需求 给到前端S EXiny uH uang 进行技术侧细节 梳理。
针对 埋点 ，从 产品 侧主 要负 责埋 点整 体方 案的 沟通 ，以 及技 术通 道的 搭建 ， 已将 附件 作为 初始 输入 进行 埋点 通道 开发 ，在 P R D冻结 之后 的埋 点需求变化，
由O neTeam及J V s各功能F O和相关P O 根据需要自行进 行代码埋点调整。

---

## PDF: 静采_AF\开发相关材料\BP_车辆埋点(文件)网关服务_接口说明书_(外发版))2.pdf

零束 BP_ 埋点 （文件） 网关服务_ 接口说明书 
V1.8 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
目录 
1 介绍 .................................................................................... 3 
1.1 概述 ................................................................................. 3 
1.2 业务流程 说明 ......................................................... 错误! 未 定义 书 签。 
1.3 接口调用 说明 ......................................................................... 3 
2 埋 点 数 据网 关 ............................................................................ 3 
2.1 上报埋点 数据 ......................................................................... 3 
请求时序 ................................................................. 错误! 未 定义 书 签。 
请求地址 ................................................................................. 3 
请求头 4 
请求参数 ................................................................................. 4 
响应参数 ................................................................................. 4 
响应示例 ................................................................................. 4 
2.2 埋点数据 网关响 应结果 说明 ............................................................. 5 
3 文 件 数 据网 关 ............................................................................ 7 
3.1 小文件上 传（非 分片上 传） ............................................................. 7 
请求时序 ................................................................. 错误! 未 定义 书 签。 
请求地址 ................................................................................. 7 
请求头 7 
请求参数 ................................................................................. 7 
响应参数 ................................................................................. 8 
响应示例 ................................................................................. 8 
3.2 文件分片 上传（ 非断点 续传 ） ........................................................... 8 
请求时序 ................................................................. 错误! 未 定义 书 签。 
请求地址 ................................................................................. 9 
请求头 9 
请求参数 ................................................................................ 10 
响应参数 ................................................................................ 11 
响应示例 ................................................................................ 12 
3.3 小文件上 传& 文件分 片上传 （非断点 续传） 错误码 ......................................... 12 
3.4 文件分片 上传（ 断点续 传） ............................................................ 12 
3.4.1 上传机制 ........................................................................... 13 
3.4.2 请求地址 ........................................................................... 14 
3.4.3 请求头 ............................................................................. 14 
3.4.4 响应头 ............................................................................. 15 
3.4.5 请求参数和响 应结果 ................................................................. 15 
3.4.6 文件分片上传 （断点 续传）错 误码 ..................................................... 19 
1 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.4.7 请求示例 ........................................................................... 21 
3.4.8 注意事项 ........................................................................... 22 
3.5 OSS 签名接口 ......................................................................... 23 
3.5.1 请求头 ............................................................................. 23 
3.5.2 请求参数 ........................................................................... 24 
3.5.3 响应结果 ........................................................................... 24 
2 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
1 介绍 
1.1 概述 
本文档描述零束科技基础平台结构化/非结构化数据上传 网关服务 数据上传接口设计说
明 
 
1.2 接口调用说明 
本文档上传接口是基于上汽 SAICTLS 安全层协议的。 
本文档上传接口的定义是基于 http 协议，并且要求请求的 URL 都是以 UTF-8 编码 
本文档接口返回值为标准化的 json，并且接口 返回值都是以UTF-8 编码（message 部分
全部修改为英文）。 
1.3 公共 Header 约束 
为了便于后期的运维 及服务升级，业务监控 等，平台需要了解终端的请求来源、设备、
版本等情况，这些信息统一添加到 http 请求的 header 中请求格式如下： 
键 值 必填 说明 
暂无    
注：网关header 遵循首字母大写中划线分隔规范 
2 埋点数据 网关 
2.1 上报埋点数据 
此接口用于上报埋点数据 。File 文件名称格式为 
VIN_Date_Time_E _Version.bl.gz 
(例：LSJWK4093NS001969_20230601_135448_E_V2.0.6.8.bl.gz) 
 请求地 址 
请 求方 式 URL 地址 
POST http(s)://域名/{车型}/data/upload 
 
注意: 具体各环境（DEV,SIT,PRE 以及PROD ）以车型项目释放的域名为准。 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
请求头 
参数 类型 必填 说明 
Content-Type String 是 multipart/form-data 
 请求参 数 
参数 类型 必填 说明 
无    
body 中 form-data 
参数 类型 必填 说明 
数据 MIME Type（content-type）：
application/octet-stream 
file 文件 是 
MIME File Name 为文件名 
 
 响应参 数 
字段 类型 说明 
code int 返回码：200 请求成功 
message String success，返回操作成功 
 响应示 例 
{ 
    "code": 200, 
    "message": "success" 
} 
 
 
 
 
 
 
 4 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
2.2 埋 点 数 据 网 关 响应 结 果 说 明 
 
httpStatus http message 说明 重 传机 制 
body 
code 
200 200 success 文件上传成功 / 
499 / / 客户端请求超时  延迟 10s 进行
重新上传 
502 / / 云端链路中某节点响
 为避免持续的
504 应异常时, 云 端 入 口 给
车 端 的 响 应 http 重 试 给 云 端 造 成 压 力
以及流量浪费，重新上
status 状态码 
传后仍出现此错误，延
迟时间按照10s 递增，
/ / 最 大 延 迟 不 超 过 3 分
钟，到达3 分钟后，以
3 分钟的固定频率进行
数据包的上传，直至无
此错误后，恢复正常的
上传速度。 
500 400401 param error 请求参数/包名有误 无需重试 
200 包名时间超过有效时 无需重试 
段，属正常情况但数据
会被过滤。 
valid time 
400701 有效时段判断逻辑：
limiting 
-10 分钟<=网关接收时
间- 上 传 数 据 采 集 时 间
（ct）<=7 天 
503 / / 云端入口网关繁忙 ⚫ 延迟 10s 进行重新
500 限流 上传 
⚫ 为避免持续的重试
给云端造成压力以
及流量浪费，重新
上传后仍出现此错
误，延迟时间按照
400700 downgrade 
10s 递增，最大延迟
不超过 3 分钟，到
达 3 分钟后，以 3
分钟的固定频率进
行数据包的上传，
 5 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
直至无此错误后，
恢复正常的上传速
度。 
404 400404 not found 资源不存在 无需重试 
500 未知异常 ⚫ 延迟 10s 进行重新
上传 
⚫ 为避免持续的重试
给云端造成压力以
及流量浪费，重新
上传后仍出现此错
误，延迟时间按照
400500 unknown error 10s 递增，最大延迟
不超过 3 分钟，到
达 3 分钟后，以 3
分钟的固定频率进
行数据包的上传，
直至无此错误后，
恢复正常的上 传速
度。 
     
     
 
注： 
 文件上传成功的定义：车端接收到上传的响应结果，并且响应结果的 http status 为
200,http body 中的code 为200,表示车端数据上传成功。其他非此响应结果均为上传失败。 
 不可重试错误：文件上传失败，响应结果的 http status 以及http body 中的code 为
【（500,400401）、（200,400701）、（404,400404 ）】时无需重试，不重试的原因是上述
错误为类似参数错误、上传地址错误等不能通过重试恢复的错误 
 文件上传失败，如果错误为 非不可重试错误 时，上传的数据文件都需要重新上传 （包括
车端接收响应超时场景），重试机制优先根据表格中【重传机制】列执行，不在表格范围内
的，按照通用重传机制执行。 
 通用重传机制 
 延迟10s 进行重新上传 
 为避免持续的重试给云端造成压力以及流量浪费，重新上传后仍出现此错误，延迟时间
按照10s 递增，最大延迟不超过 3 分钟，到达 3 分钟后，以3 分钟的固定频率进行数据包的
上传，直至无此错误后，恢复正常的上传速度 
 
 
 6 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3 文件数据网关 
3.1 小文件上传 （ 非分 片 上 传 ） 
对 于文 件 大小 小于 1MB 的 文件 可以使 用此 接口进 行上 传，对 于大 于 1MB 的 文件不 适用 此
接口 
此接口用于上报埋点 数据，上传数据的命名规范遵循数据架构埋点数据命名规范, 例如： 
EvtID_VIN_Date_Time_{0}_{1}_{2}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}.tar.gz 
（备注：文件名称以下划线“_ ”区分元素，所以{x}内不能含 有下划线。） 
注： 
1.后 续新的 车型 ，建议使 用文 件分片 上传 （断点 续传 ） 
 请求地 址 
请 求方 式 URL 地址 
http(s)://域名
POST /{vehicleModel}/cloud/gateway/file-access/file/uploa
d 
 
 注意: 具体各环境（DEV,SIT,PRE 以及PROD ）以车型项目释放的域名为准。 
 请求头 
参数 类型 必填 说明 
Content-Type String 是 multipart/form-data 
来源，如：IAM,ICC,IMATE… 
不同业务（如 OTA 升级日志，RDS 车端日志）
Source String 是 
支持的来源范围不同，具体支持的范围 ，对接
前请联系 SC-基础平台进行确认 
车型，如：EP33L,ES33… 
Vehicle-Model String 是 具体支持的车型 范围，对接前 请联系SC-基础
平台进行确认 
 请求参 数 
参数 类型 必填 说明 
 7 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
无    
body 中 form-data 
参数 类型 必填 说明 
数据 MIME Type（content-type）：
application/octet-stream 
file byte[] 是 
MIME File Name 为文件名 
 
 
 响应参 数 
字段 类型 说明 
code int 返回码：200 请求成功 
message String success 
data Object 响应数据 
 
 
 
 响应示 例 
{ 
    "code": 200, 
    "message": "success", 
    "data": null 
} 
 
3.2 文件 分片上传 （非 断点续传） 
注： 
1.后 续新的 车型 ，建议使 用文 件分片 上传 （断点 续传 ） 
 
 
 
 8 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
请求地 址 
请 求方 式 业务 接 口地 址 
http(s)://域名
分片上
/{vehicleModel}/cloud/gateway/part-file-access/file
传 
/upload 
http(s)://域名
/{vehicleModel}/cloud/gateway/rds-part-file-access/
RDS 分 file/upload 
POST 
片上传  
http(s)://域名/{vehicleModel}/file/upload/{version} 
(消息格式采用最新规范) 
不限定
http(s)://域名/{vehicleModel}/cloud/gateway/ 
命名条
multiple-file-access/file/upload 
件上传 
 
注意: 具体各环境（DEV,SIT,PRE 以及PROD）以车型项目释放的域名为准。 
 
 请求头 
1）以下适用于分片上传和不限定命名条件上传 
参数 类型 必填 说明 
Content-Type String 是 multipart/form-data 
分段上传 值域信息bytes x-y/z 
x:起始字节位 
Content-Range String 是 
y:结束字节位 
z:总字节数 
来源，如：OTA,IAM,ICC,IMATE… 
Source String 是 不同业务支持的来源范围不同，具体支持的范
围，对接前请联系 SC-基础平台进行确认 
车型，如：EP33L,ES33… 
Vehicle-Model String 是 具体支持的车型范围，对接前请联系 SC-基础
平台进行确认 
 
 9 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
2）以下适用于RDS 分片上传 
参数 类型 必填 说明 
Content-Type String 是 multipart/form-data 
分段上传 值域信息bytes x-y/z 
x:起始字节位 
Content-Range String 是 
y:结束字节位 
z:总 字节数 
来源。（如 IAM，ICMAndroid 等） 
Source String 是 存储 OSS 层级使用，网关不作限制，但需避免
使用部分特殊字符，如空格等。 
Vehicle-Model String 否 非必填 
 
 请求参 数 
参数 类型 必填 说明 
无    
body 中 form-data（三路由通用） 
参数 类型 必填 说明 
数据 MIME Type（content-type）：
application/octet-stream 
file byte[] 是 
MIME File Name 为文件名 
 
3.2.4.1 文 件命名规范 
文件上传时，各业务的文件命名规范以业务系统需求为准，当前 OTA 升级日志以及 RDS 车端
日志的文件命名规范参考如下。 
  
EvtID_VIN_Date_Time_{0}_{1}_{2}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}.tar.gz 
分片上传命名
 10 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
（例：1685453654828_0123456789123C160_20230530_213416_52268_ota_V1.zip ） 
规范 
 
EvtID_VIN_Date_Time_{0}_{1}_{2}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}.tar.gz 
RDS 分片上传文
（例：B100_TSTBENCHES3300001_20190101_081834_ICCQnx_V1.0.0_65535-33-5-A004.zip） 
件命名规范
（旧）  
EvtID_VIN_Date_Time_{0}_{1}_{2}_{3}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}_{3}.tar.gz 
RDS 分片上传文
（例：
件命名规范
B200_LSJWM4090NS002183_20230607_170411_ICMAndroid_V5.11.1_257-8-2_ICM-1-backlight-black-
（新） 
screen.zip ） 
 
ES39 v1 文件上传名称： 
* 新：VIN_Date_Time_ECUName_PackageNumber_UniqueId_VehicleType_Version.zip 
* 例：LSJE36095MS143940_20220512_062351_IAM_65535-19-14_C024_EP33L_V1.1.1.zip 
或 
* 新：VIN_Date_Time_ECUName_PackageNumber_EventTriggerScenario_VehicleType_Version.zip 
* 例：LSJE36095MS143940_20220512_062351_IAM_65534-15-5_2-NoLocation_EP33L_V1.1.1.zip 
（备注：文件名称以下划线“_ ”区分元素，所以{x}内不能含 有下划线。） 
 
 响应参 数 
字段 类型 说明 
code int 返回码：200 请求成功 
message String success 
data Object 响应数据 
上传文件 OSS 地址。 
只有数据包最后一片上传成功时，响应结果才包含
fileUrl 
 
fileUrl String 注意： 
 只有数据包最后一片上传成功时，响应结果才包
含fileUrl 
 RDS 车端日志 fileUrl 为空（减少文件暴露进行
屏蔽） 
注：OTA 升 级日 志长期方 案会 屏蔽 fileUrl 内容 ，不 再填充 OSS 路 径地 址 
 11 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
响应示 例 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "fileUrl": "/EP33/20221110/1668041281198_LSP11LOTA12345679_20221110_084802_
16088_ota_V1.zip" 
    } 
} 
 
 
3.3 小文件上传& 文件 分 片 上 传 （ 非断 点 续 传 ） 错 误码 
httpStatus 错 误码 错 误消 息 备注 
500 900401 param error 请求参数/包名有误 
404 900404 not found 资源不存在 
418 900418 Part upload error 分片上传错误 
500 900402 internal error 服务端异常 
500 900700 limiting 预留。 
500 900701 downgrade 限流 
500 900500 unknown error 预留。 
 
3.4 文件 分 片 上传 （断 点 续 传 ） 
文件分片上传（非断点续传）存在如下问题： 
1. 在大文件进行上传时，对于 3.2 中的文件分片上传的分片大小为车端固定大小 5MB，超过
此大小的文件才会进行分片上传，此策略 不能 动态修改分片大小。 
2．由于网络、车辆熄火等因素的不确定性，会造成文件上传失败，上传失败后，下次点火
车辆又重复从头开始上传文件，此种情况会造成 
 a.从头开始上传文件，造成流量的浪费 
 b.从头开始上传文件，文件上传失败的概率较大 
 c.上传失败导致OSS 碎片残留 
 
基于上述原因，对于大文件上传车云需要一套 替代现有分片上传的上传机制，支持断点续传。 
 
注： 
1.后 续新的 车型 ，不建议 使用 文件分 片上 传（非 断点 续传） ，转为 使用 此接 口进行 文件 上传 
 12 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.4.1 上传机制 
文件上 传流程 
 
 
 13 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
分片文 件 云端保存策略 
 对于车端初始化文件上传的 Upload ID 以及后续分片数据上传的分片信息 
 云端以UploadId 生成为起始时间往后推移保存一周（云端可配置），对于在后续时间完
成整个文件整体上传的，由于文件合并成功，清除分片信息 。 
 对于在一周内也未完成最终上传的，清除分片缓存信息 ，同时清理 OSS 分片文件数据 
 
3.4.2 请求地址 
请 求方 式 URL 地址 
POST http(s)://域名/{vehicleModel}/multipart/upload 
注意: 具体各环境（DEV,SIT,PRE 以及PROD）以车型项目释放的域名为准。 
 
3.4.3 请求头 
参数 类型 必填 说明 
Content-Type String 是 multipart/form-data 
接口协议版本 
P-Version String 是 
P-Version 当前为0.0.1 
约定文件上传的加解密方式 
Cipher-Mode int 是 
0-不加密 
Sign-Mode int 是 0-不签名 
对应 Sign-Mode 不为0 时，需要对上传的文件
Signature String 否 
数据进行签名 
应用 ID 
1- OTA 升级日志 
2- RDS 车端日志 
Aid int 是 3- 智能泊车泊车轨迹 
4- 远程查看 
5- 停车拍照 
6- 哨兵模式 
 14 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
Vin String 是 车辆 VIN 码 
Eid String 是 事件的唯一标识(全局唯一) 
来源。（如 IAM，ICMAndroid 等） 
Source String 是 存储 OSS 层级使用，网关不作限制，但需避免
使用部分特殊字符，如空格等。 
Vehicle-Model String 否 非必填 
3.4.4 响应头 
参数 类型 必填 说明 
事件的唯一标识(全局唯一) ，为请求时的
Eid String 是 
event  
 
3.4.5 请求参数和响应结 果 
初始化 分片信息 
初始化分片信息请求参数 
参数 类型 必填 说明 
type int 是 type=1 初始化分片信息 
fileName String 是 待上传的文件名称 
fileSize int 是 待上传的文件总大小 ，单位（byte） 
 
初始化分片信息响应结果 
字段 类型 必填 说明 
code int 是 返回码：200 请求成功 
message String 是 success 
data Object 是  
type int 是 type=1 初始化分片信息 
 15 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
total int 是 分片总数 
size int 是 分片大小 
tid String 是 分片上传事务 ID 
List<i
exist 是 已上传的分片序号，分片序 号从1 开始 
nt> 
fileUrl String 是  
 
响应示例（正常情况） 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "type": 1, 
        "total": 3, 
        "size": 5400000, 
        "tid": "xxxxxxxxxx", 
        "exist": [1], 
        "fileUrl": "" 
    } 
} 
 
响应示例（已完成上传合并 文件再次初始化时，此处 fileUrl 是否会有 key 填充与type 为3
时逻辑同步；如果已经完成过上传 或分片上传齐全但未合并 ，exist 会为 从1 至total） 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "type": 1, 
        "total": 3, 
        "size": 5400000, 
        "tid": "xxxxxxxxxx", 
        "exist": [1, 2, 3], 
        "fileUrl": "" 
    } 
} 
 
 
 16 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
分片文 件上传 
分片文件上传请求参数 
参数 类型 必填 说明 
type int 是 type=2 分片文件上传 
index int 是 分片序号，分片需要从 1 开始 
数据 MIME Type（content-type）：
application/octet-stream 
file byte[] 是 
MIME File Name 为文件名 
分片文件上传响应结果 
字段 类型 必填 说明 
code int 是 返回码：200 请求成功 
message String 是 success 
data Object 是  
type int 是 type=2 分片文件上传 
 
响应示例 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "type": 2 
    } 
} 
 
 
 
 
 
 
 
 
 17 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
分片文 件合并 
分片文件合并请求参数 
参数 类型 必填 说明 
type int 是 Type=3 分片文件合并 
fileName String 是 分片上传 文件名 
其他自定义上传参数，Json 字符串,该字段会
JsonSt 通过 kafka 透传给网关下游业务方， 如： 
extParams 否 
ring extParams: 
"{\"vin\":\"\",\"version\":\"\"}" 
 
分片文件合并响应结果 
字段 类型 必填 说明 
code int 是 返回码：200 请求成功 
message String 是 success 
data Object 是  
type int 是 type=3 分片文件合并 
文件 OSS Key(OSS 唯一路径) 
fileUrl String 是 （ 为尽 可能减 少暴 露，网 关会 根据业 务需 求动
态 选择 是否填 充 key） 
 
响应示例 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "type": 3, 
        "fileUrl": 
"/EP33/20221110/1668041281198_LSP11LOTA12345679_20221110_084802_16088_ota_V1.zip" 
    } 
} 
 
 
 
 18 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
响应示例（不暴露key） 
{ 
    "code": 200, 
    "message": "success", 
    "data": { 
        "type": 3, 
        "fileUrl": "" 
    } 
} 
 
 
3.4.6 文件分片上传 （断 点续传）错误码 
 
 
httpStatus http message 说明 重 传机 制 
body 
code 
200 200 success 文件上传成功 / 
499 / / 客户端请求超时  延迟 10s 进行重新上传 
 为 避 免 持 续 的 重 试 给 云
502 / / 云端链路中某节
端 造 成 压 力 以 及流 量 浪费 ， 重 新
504 点响应异常时,
云端入口给车端 上 传 后 仍 出 现 此错 误 ， 延迟时间
的响应 http 按照 10s 递增，最大延迟不超过
3 分钟，到达 3 分钟后，以 3 分
/ / status 状态码 
钟 的 固 定 频 率 进 行 数 据 包 的 上
传 ， 直 至 无 此 错误 后 ，恢 复 正 常
的上传速度。 
200 请求参数/ 包名 无需重试 
900401 param error 
有误 
200 包名时间超过有 无需重试 
效时段，属正常
情况但数据会被
valid time 过滤。 
900701 
limiting 有效时段判断逻
辑：-10 分钟<=
网关接收时间-
上传数据采集时
 19 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
间（ct）<=7 天 
503 云端入口网关繁 ⚫ 延迟10s 进行重新上传 
/ / 
忙 ⚫ 为 避 免 持 续 的 重 试 给 云 端 造
200 限流 成压力以及流量浪费，重新上
传后仍出现此错误，延迟时间
按照10s 递增，最大延迟不超
900700 downgrade 过3 分钟，到达 3 分钟后，以
3 分 钟 的 固 定 频 率 进 行 数 据
包的上传，直至无此错误后，
恢复正常的上传速度。 
404 900404 not found 资源不存在 无需重试 
500 未知异常 ⚫ 延迟10s 进行重新上传 
⚫ 为 避 免 持 续 的 重 试 给 云 端 造
成压力以及流量浪费，重新上
传后仍出现此错误，延迟时间
900500 unknown error 按照10s 递增，最大延迟不超
过3 分钟，到达 3 分钟后，以
3 分 钟 的 固 定 频 率 进 行 数 据
包的上传，直至无此错误后，
恢复正常的上传速度。 
200 Part upload 分片上传错误  
900418 
error 
     
 
注： 
 文 件上 传成功 的定 义：车 端接 收到上 传的 响应结 果， 并且响 应结 果的 http status 为
200,http body 中的 code 为 200, 表 示车 端数据 上传 成功 。其他 非此响 应结 果均为 上传 失败。 
 不 可重 试错误 ：文 件上传 失败 ，响应 结果 的 http status 以及http body 中的code 为
【（200,900401 ）、（200,900701 ）、（404,900404 ）】时 无需 重试，不 重试的 原因 是上述
错 误为 类似参 数错 误、上 传地 址错误 等不 能通过 重试 恢复的 错误 
 文 件上 传失败 ，如 果错误 为非 不可重 试错 误时， 上传 的数据 文件 都需要 重新 上传（ 包括
车 端接 收响应 超时 场景） ，重 试机制 优先 根据表 格中 【重传 机制 】列执 行， 不在表 格范 围内
的 ，按 照通用 重传 机制执 行。 
 通 用重 传机制 
 延迟10s 进行重 新上 传 
 为 避免 持续的 重试 给云端 造成 压力以 及流 量浪费 ，重 新上传 后仍 出现此 错误 ，延 迟 时间
按照10s 递增，最 大延迟 不超 过 3 分钟，到达 3 分 钟后， 以 3 分钟的 固定 频率进 行数 据包的
上 传， 直至无 此错 误后， 恢复 正常的 上传 速度 
 
 20 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.4.7 请求示例 
CURL 方式： 
curl --location 'http://127.1.0.1:8080/ep33l/file/upload' \ 
--header 'Source: OTA' \ 
--header 'P-Version: 0.0.1' \ 
--header 'Cipher-Mode: 0' \ 
--header 'Sign-Mode: 0' \ 
--header 'Aid: 1' \ 
--header 'Vin: LSJWM4093NS999907' \ 
--header 'Eid: 全局唯一' \ 
--form 'type="1"' \ 
--form 'fileSize="1000000000"' \ 
--form 'fileName="1685453654828_0123456789123C160_20230530_213416_52268_ota_V1.zip"' 
 
 
 
JAVA Okhttp 方式： 
OkHttpClient client = new OkHttpClient().newBuilder() 
  .build(); 
MediaType mediaType = MediaType.parse("text/plain"); 
RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM) 
  .addFormDataPart("type","1") 
  .addFormDataPart("fileSize","1000000000") 
  .addFormDataPart("fileName","1685453654828_0123456789123C160_20230530_213416_52268_ota_
V1.zip") 
  .build(); 
Request request = new Request.Builder() 
  .url("http://127.1.0.1:8080/ep33l/file/upload") 
  .method("POST", body) 
  .addHeader("Source", "OTA") 
  .addHeader("P-Version", "0.0.1") 
  .addHeader("Cipher-Mode", "0") 
  .addHeader("Sign-Mode", "0") 
  .addHeader("Aid", "1") 
  .addHeader("Vin", "LSJWM4093NS999907") 
  .addHeader("Eid", "全局唯一") 
  .build(); 
Response response = client.newCall(request).execute(); 
 
 21 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.4.8 注意事项 
文件命 名规范 
EvtID_VIN_Date_Time_{0}_{1}_{2}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}.tar.gz 
OTA 网关文件命
（例：1685453654828_0123456789123C160_20230530_213416_52268_ota_V1.zip ） 
名规范 
 
EvtID_VIN_Date_Time_{0}_{1}_{2}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}.tar.gz 
RDS 网关（旧版）
（例：B100_TSTBENCHES3300001_20190101_081834_ICCQnx_V1.0.0_65535-33-5-A004.zip） 
文件命名规范 
 
EvtID_VIN_Date_Time_{0}_{1}_{2}_{3}.zip 或 EvtID_VIN_Date_Time_{0}_{1}_{2}_{3}.tar.gz 
RDS 网关（新版）
（例：
文件命名规范 
B200_LSJWM4090NS002183_20230607_170411_ICMAndroid_V5.11.1_257-8-2_ICM-1-backlight-black-
screen.zip ） 
（ 备注：文 件名称 以下划 线“_” 区分元素 ，所以{x}内 不能含有 下划线。 ） 
 
 22 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.5 OSS 签名接口 
请 求方 式 URL 地址 
POST http(s)://域名/oss/generatePresignedUrl 
注意: 具体各环境（DEV,SIT,PRE 以及PROD）以车型项目释放的域名为准。 
3.5.1 请求头 
 
参数 类型 必填 说明 
Content-Type String 是 application/json 
接口协议版本 
P-Version String 是 
P-Version 当前为0.0.1 
约定文件上传的加解密方式 
Cipher-Mode int 是 
0-不加密 
Sign-Mode Int 是 0-不签名 
对应 Sign-Mode 不为0 时，需要对上传的文件
Signature string 否 
数据进行签名 
应用 ID 
1- OTA 升级日志 
2- RDS 车端日志 
Aid int 是 3- 智能泊车泊车轨迹 
4- 远程查看 
5- 停车拍照 
6- 哨兵模式 
Eid String 是 事件的唯一标识(全局唯一) 
来源。（如 IAM，ICMAndroid 等） 
Source String 是 存储 OSS 层级使用，需避免使用部分特殊字符，
如空格等。 
Vehicle-Model String 否 非必填 
 
 
 
 
 23 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
3.5.2 请求参数 
 
参数 类型 必填 说明 
ossId String 是 Oss 文件全路径 
授权 URL 的有效时长，单位秒 
time String 是 
 
示例： 
[ 
  { 
    "ossId":"", 
    "time": 0// 如一天： 1 * 60 * 60 * 24 
  },{ 
    "ossId":"", 
    "time": 0// 如一天 ： 1000 * 60 * 60 * 24 
  },{ 
    "ossId":"", 
    "time": 0// 如一天： 1000 * 60 * 60 * 24 
  } 
] 
 
 
 
 
3.5.3 响应结果 
接口响应头Content-Type 为application/json 
参数 类型 必填 说明 
ossId String 是 Oss 文件全路径 
url String 否 生成的授权 URL 
200- 成功 
900419-超出最大授权时间 
businessCode int 否 
900420-文件不存在或被删除 
900421-生成URL 错误 
message String 否 错误说明 
 
 24 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
备注： 
⚫ 阿里云OSS 签名最大不超过 7 天，不包含7 天 
 
示例 
{ 
    "code": 200, 
    "message": "操作成功", 
    "data": [ 
        { 
            "ossId": "/sit-ddc-oss-sjjg/ddc/script/test/2023-09-24/1.txt", 
            "url": 
"http://s3-zz-prda.sail-cloud.com/sit-ddc-oss-sjjg/ddc/script/test/2023-09-24/1.
txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231120T030212Z&X-Amz-SignedHea
ders=host&X-Amz-Expires=395867&X-Amz-Credential=VTFPE5T3YAUMV0P04UGE%2F20231120%
2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Signature=0e27397326058df3aabec01ccf77767
4a370375471a59f1894e39b1dc5b2cf86", 
            "businessCode":200, 
            "message":"success" 
          }, 
        { 
            "ossId": "/sit-ddc-oss-sjjg/ddc/script/test/2023-09-24/1.txt", 
            "url": "", 
            "businessCode":900419, 
            "message":" 授权时间超出最大支持范围，请确认授权时间在 7 天内" 
          }, 
        { 
            "ossId": "/sit-ddc-oss-sjjg/ddc/script/test/2023-09-24/1.txt", 
            "url": "", 
            "businessCode":900420,  
            "message":"OSS 文件不存在或者被清理" 
        } 
    ], 
    "extraData": {} 
} 
 
 25 
 
@Z-ONE 19102020 
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用
上汽零束保密文档，仅用于大众和上汽零束项目使用

---
