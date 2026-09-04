# 具身智能情报前沿｜人机交互进入示范学习

**作者：具身视界** · 2026.07.27

---

> 今天最值得关注的变化，是具身智能的人机交互正在从“人遥控机器人”升级为“机器人理解人如何示范、如何递交、如何共处、如何记住上下文”。近 7 天，多篇论文集中指向同一条线：单个人类视频学技能、语音驱动工具递交、社交导航、长期记忆和人体姿态感知，正在把 HRI 从界面问题推进到数据与行为建模问题。

## 💥 今日重磅

### [HOST：机器人可从单个人类视频中平均 29 秒习得新操作技能](https://arxiv.org/abs/2607.20033)

**摘要：** 7 月 22 日提交的 `Robots Acquire Manipulation Skills in Seconds from a Single Human Video` 提出 HOST，即 Human-to-robot One-Shot Skill AcquisiTion。它的核心价值在于把“人教机器人”从重遥操作、重多轮采集，压缩成从单个人类视频快速适配到机器人本体。论文称，HOST 先估计机器人在示范任务中的进展，再把人类视频的下一步进展翻译成机器人自己的未来观测，最后从预测观测中推导动作；这种级联通过共享任务进度流形把人类示范和机器人轨迹对齐。实验结果显示，HOST 在推理阶段从单个人类视频平均 29 秒获得新技能，平均成功率 62%，比 zero-shot baseline 高 45%；相比每个任务用 50 条机器人示范微调的基线，HOST 需要 50 倍更少示范，技能获取速度快 507 倍。对具身智能公司来说，这意味着人机交互不只是语音按钮或遥控器，而是把普通人的视频、动作和意图转化为机器人可执行策略的数据入口。

- **来源：** arXiv
- **核心价值：** 数据相关报道：人类视频正在变成低成本具身数据来源；未来机器人学习的关键，不只是采多少真机数据，而是能否把人的示范快速映射到机器人的身体上。
- **行业判断：** 人机交互的下一阶段，是让普通人自然示范任务，而不是让专业操作员反复遥控采数。

---

## 📰 行业新闻

### 1. [移动机器人行人交互研究：把“舒适度”纳入公共空间导航指标](https://arxiv.org/abs/2607.17604)

**摘要：** 7 月 20 日提交的 Stability and Comfort in Mobile Robot-Pedestrian Interactions 面向公共空间里的非完整约束移动机器人，提出基于 Social Force Model 和 projected Time-to-collision Social Force Model 的社会化导航框架。论文不仅证明系统稳定性，还通过行人-机器人交互实验收集行人主观舒适度反馈，并用统计工具分析问卷结果。

- **来源：** arXiv
- **核心价值：** 服务机器人进入商场、医院、园区和展会后，导航指标不能只看是否避障，还要看人是否觉得安全、自然、可预测。

### 2. [NICO 手势模仿：单目 RGB 到半人形机器人动作映射](https://arxiv.org/abs/2607.18197)

**摘要：** 7 月 20 日提交的 Imitation of Arm Gestures by the Semi-Humanoid Robot NICO，用 MediaPipe 从单目 RGB 图像估计人体上肢和手部关键点，再通过解析几何计算关节角，并映射到 NICO 半人形机器人的电机配置。作者在 6 名不同身高参与者的代表性手势上做了初步实验，能生成有意义的模仿动作，同时指出复杂姿态和腕部动作仍是短板。

- **来源：** arXiv
- **核心价值：** 手势模仿是低门槛 HRI 的基础能力；如果机器人能直接从普通摄像头理解人的动作，示教、陪伴和服务交互都会降低部署成本。

### 3. [动作基元识别：NICO 用自组织映射学习“正在做什么阶段”](https://arxiv.org/abs/2607.18737)

**摘要：** 7 月 21 日提交的 Motion Primitive Discovery in a Humanoid Robot via Self-Organising Maps for Phase Recognition，受镜像神经元系统启发，在 NICO 人形机器人上用两层结构识别动作阶段：先用 SOM 学习手臂和手部运动表征，再用 Echo State Network 判断连续动作当前处在哪个阶段。

- **来源：** arXiv
- **核心价值：** 机器人要与人自然协作，必须识别人类动作不是静态姿态，而是一个持续过程；阶段识别会直接影响递交、跟随、协作装配等任务的时机判断。

---

## 📚 前沿论文

### 1. [语音驱动工具递交：机器人按人的抓取方式调整递交姿态](https://arxiv.org/abs/2607.17839)

**摘要：** 7 月 20 日提交的 Receiver-Centered Robot-to-Human Handover 关注协作机器人向人递交机械工具这一高频微交互。系统基于 Franka 协作臂，用 LLM 做意图识别，MediaPipe 做实时 3D 手部跟踪，并动态调整末端姿态，以 handle-first 的方式递交非对称工具。用户研究显示，自适应策略可减少非对称工具抓取延迟，并改善运动可预测性和任务简单性感知。

- **作者团队：** Federico Biagi / Dario Onfiani / Simone Silenzi / Luigi Biagiotti
- **来源：** arXiv
- **核心价值：** 好的人机交互不是把物体递到人面前，而是按接收者的抓取方式、工具形状和信任预期来递交。

### 2. [平面激光雷达人体姿态估计：服务机器人可在低算力平台感知人的朝向](https://arxiv.org/abs/2607.21309)

**摘要：** 7 月 23 日提交的论文用全向平面 LiDAR 序列估计附近行人的位置和朝向，面向安全导航和 socially aware HRI。模型基于 Space-Time Blocks，在 360 度 LiDAR 序列上输出每条射线上的人体存在、距离和相对方向，并通过 RGB-D body tracker 做跨模态自监督，减少人工 LiDAR 标注需求。实验显示，距离、位置、朝向误差分别降低 38%、28%、15%，并支持服务机器人实时 CPU 推理。

- **作者团队：** Simone Arreghini / Mirko Nava / Nicholas Carlotti / Antonio Paolillo / Alessandro Giusti
- **来源：** arXiv
- **核心价值：** 数据相关报道：人机共处需要低成本人体状态数据；仅靠摄像头或高端 3D LiDAR 不足以覆盖大量服务机器人部署。

### 3. [SOPD-SocialNav：把大型 VLM 的社交导航知识蒸馏到轻量模型](https://arxiv.org/abs/2607.19850)

**摘要：** 7 月 22 日提交的 SOPD-SocialNav 关注机器人在排队、会话、拥挤空间中的社会化导航。论文用选择性 on-policy distillation，将大型教师 VLM 的社交导航知识迁移到轻量学生 VLM；通过 teacher uncertainty 选择社交信息量高的决策 token，避免把 trivial navigation state 也当成重点学习。真实 Scout Mini 部署显示，蒸馏模型能在对话和排队场景生成更合适的导航行为。

- **作者团队：** Xinyu Zhang / Zishuo Wang / Ling Xiao
- **来源：** arXiv
- **核心价值：** 社交导航不是简单避障，而是理解人正在排队、交谈、等待或让路；这会决定服务机器人能否进入公共空间。

### 4. [Sequential EQA：连续具身问答要求机器人记住同一场景里的历史互动](https://arxiv.org/abs/2607.21571)

**摘要：** 7 月 23 日提交的 Beyond Episodic Evaluation 指出，传统具身问答常把每个任务独立评测，但真实机器人需要连续回答同一场景里的多个问题，并保留过去互动。论文发现，仅保留 2D 占据图只能记住走过哪里，不能保存后续问答所需的视觉语义证据；将持续视觉观察映射到 3D 几何的空间化记忆更适合真实物理环境。

- **作者团队：** Zikui Cai / Kaushal Janga / Bo Li / Yuke Zhu / Roberto Martin-Martin 等
- **来源：** arXiv
- **核心价值：** 机器人若要像助理一样服务人，必须记住刚才看过什么、问过什么、答过什么，而不是每次重新开始。

---

## 🧩 开源生态

### 1. [AnyDexRetarget：多灵巧手手部姿态重定向继续服务人类示范到机器人手](https://github.com/qqsq12321/AnyDexRetarget)

**摘要：** AnyDexRetarget 项目页可访问，项目定位为面向 multiple dexterous hands 的高精度手部姿态重定向，支持 Vision Pro、Quest 3、camera 等输入。它与 HOST 的人类视频示范主线一致：人机交互的核心是把人的手势、姿态和意图转换到不同机器人手的自由度与约束里，而不是只采集单一硬件上的遥操作数据。

- **来源：** GitHub
- **核心价值：** 手部重定向是人类示范进入机器人操作策略的关键接口；没有统一重定向，示范数据很难跨本体复用。

### 2. [HandUMI：穿戴式双臂采数把人的操作变成可校准、可质检的数据链](https://github.com/robonet-ai/handumi-sw)

**摘要：** HandUMI 软件项目页可访问，项目说明其支持同步双臂数据采集、任意双臂机器人重定向、校准、QA、回放和遥操作；硬件项目则面向无机器人在环的手戴式双臂操作数据采集。对 HRI 来说，这类工具把“人会做什么”转成机器人可学习的数据，而校准和质检决定了这批示范数据能否真正训练模型。

- **来源：** GitHub
- **核心价值：** 数据相关报道：人机交互的商业价值会落到采数链路上，示范、校准、质检和重定向必须连成闭环。

### 3. [ModPack：可穿戴背包把触觉反馈、关节级遥操作和移动操作模块化](https://modpack-robotics.github.io/)

**摘要：** ModPack 项目页可访问，对应论文提出面向双臂移动操作的模块化遥操作系统，核心是集成 onboard computation、power、communication 和 data storage 的可穿戴背包，并支持带触觉反馈的关节级遥操作、移动操作和主动感知模块。它适合连接“人如何控制机器人”和“机器人如何采集可训练数据”两个问题。

- **来源：** 项目主页
- **核心价值：** 好的遥操作界面不是临时外设，而是带算力、电源、通信、存储和触觉反馈的数据采集基础设施。

---

## 🏢 机器人公司情报

### 1. [Franka 协作臂成为工具递交 HRI 研究平台：工业协作开始关注人的抓取舒适度](https://arxiv.org/abs/2607.17839)

**摘要：** Receiver-Centered Robot-to-Human Handover 基于 Franka 协作臂构建语音驱动工具递交系统，并通过用户研究评估抓取延迟、运动可预测性和任务简单性感知。Franka 这类成熟协作臂频繁作为 HRI 研究平台，说明工业协作机器人正在从“避开人”走向“理解人如何接物、如何信任、如何协作”。

- **来源：** arXiv
- **核心价值：** 协作机器人下一轮竞争会更关注微交互质量：递交姿态、运动可预测性、信任感和人体工学。

### 2. [Scout Mini 出现在社交导航真机部署：移动机器人要学会排队与会话场景规则](https://arxiv.org/abs/2607.19850)

**摘要：** SOPD-SocialNav 在 Scout Mini 机器人上做真实部署，验证轻量学生 VLM 在 conversational 和 queuing scenarios 中生成更社会化的导航行为。这个信号对移动服务机器人公司很直接：在商场、医院、展会、园区和酒店里，机器人不能只会避障，还要理解人群结构和社交规则。

- **来源：** arXiv
- **核心价值：** 服务机器人进入公共空间后，能不能“懂礼貌地移动”会和安全、效率一样重要。

### 3. [NICO 半人形机器人连续出现在 HRI 论文中：手势和动作阶段成为社交能力底座](https://arxiv.org/abs/2607.18197)

**摘要：** 7 月 20 日与 7 月 21 日，两篇围绕 NICO 半人形机器人的论文分别讨论手势模仿和动作阶段识别。前者把单目 RGB 人体关键点映射为机器人上肢动作，后者用 SOM 和 ESN 学习动作基元与在线阶段识别。这类平台信号说明，半人形机器人在 HRI 研究中仍有价值：它足够接近人的身体结构，又比全尺寸人形更适合快速验证感知-动作闭环。

- **来源：** arXiv
- **核心价值：** 对本体公司和实验室来说，HRI 平台不一定先追求全身复杂度，稳定复现手势、阶段和协作时机，反而更接近可迭代产品能力。

---

## 结尾总结

7 月 27 日的主线可以概括为：人机交互正在从控制界面变成学习入口。HOST、HandUMI、AnyDexRetarget 和 ModPack 指向人类示范数据；工具递交、手势模仿、社交导航、人体姿态估计和连续问答则说明，机器人必须理解人的动作、距离、舒适度、历史上下文和信任预期。

---

> 💬 你认为具身机器人最先需要突破哪类人机交互能力：看视频学技能、听语音递工具、在人群中懂礼让，还是记住长期上下文？

---

## 关键词索引

**公司 / 机构：** NICO / Franka / Scout Mini / Robonet AI / AnyDexRetarget / MediaPipe

**项目 / 论文：** HOST / Stability and Comfort in Mobile Robot-Pedestrian Interactions / Imitation of Arm Gestures by NICO / Motion Primitive Discovery / Receiver-Centered Handover / Factorized Spatio-Temporal Convolutions / SOPD-SocialNav / Sequential EQA / AnyDexRetarget / HandUMI / ModPack

**技术：** 具身智能 / 人机交互 / HRI / 人类视频示范 / 单样本技能习得 / 手部姿态重定向 / 遥操作 / 社交导航 / 手势模仿 / 动作基元 / 人体姿态估计 / 长期记忆 / 机器人递交

---

## 值得分享

1. HOST 让机器人从单个人类视频平均 29 秒学会新技能，成功率 62%，比 zero-shot baseline 高 45%。
2. 人机交互正在变成数据入口：视频示范、手部重定向、穿戴式采数和触觉反馈会共同决定机器人学习效率。
3. 服务机器人不能只会避障，还要理解人的朝向、队列、会话、舒适距离和历史上下文。
