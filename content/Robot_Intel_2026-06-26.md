# 具身智能情报前沿｜灵巧手与关节硬件开始反向定义算法

**作者：具身视界** · 2026.06.26

> 今天最值得关注的变化，是具身智能的焦点从 VLA、世界模型继续下沉到“手、关节、触觉和上肢控制”这些硬件底座。PDS Joint、Tactile Genesis、STIR Hand、CoorDex 和 ABB × PSYONIC 的动态共同说明：灵巧操作不只靠更大的模型，真正决定落地上限的，是关节顺应性、触觉覆盖、手—臂—身体协同，以及能从真实硬件持续回流的数据闭环。

---

## 今日重磅

### [PDS Joint：面向灵巧手的双螺旋柔顺关节，把安全、刚度和本体感知集成到指关节里](https://arxiv.org/abs/2606.24377)

**摘要：** 6 月 23 日提交的 `PDS Joint` 把今天的硬件主线讲得很清楚：灵巧手不能只追求自由度数量，还要在关节层面解决安全接触、大行程拟人运动、方向相关刚度和可靠本体感知。论文提出 Parametric Double-Spiral compliant joint，使用阿基米德螺旋与对数螺旋模板，为不同手指关节定制屈伸、外展 / 内收、旋前 / 旋后等多种变形模式下的刚度分布，并引入 asymmetry ratio 来同时兼顾抓取稳定和抗过伸。更关键的是，团队把嵌入式电感本体感知与柔顺关节协同设计，再用 ArUco 标记跟踪产生标定数据，训练 MLP 将原始电感信号映射为关节状态；在最难的外展 / 内收估计中，相比传统曲线拟合误差降低 41.6%。最后，该关节被集成到开源灵巧手演示平台，完成 9 种日常物体抓取和安全的人机接触交互。

- **来源：** arXiv
- **核心价值：** 这说明灵巧手竞争正在从“电机和自由度堆叠”转向“关节即传感器、结构即安全、材料即控制”的硬件智能路线；未来 VLA 和操作策略能否可靠落地，很大程度取决于这类可感知、可顺应、可参数化的底层关节。

---

## 行业新闻

### 1. [Agility Robotics 拟通过 SPAC 上市：Digit v5 已获超 3 亿美元多年订单](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility Robotics 6 月 24 日宣布，将与 Churchill Capital Corp XI 合并上市，交易给予公司约 25 亿美元 pre-money 股权价值，预计带来超 6.2 亿美元总收益，其中约 2 亿美元来自 PIPE。公司称 Digit 已在 Schaeffler、GXO、Toyota Motor Manufacturing Canada、Mercado Libre 等客户环境中运行，累计超过 65,000 小时，并已为下一代 Digit v5 获得超过 3 亿美元多年订单。

- **来源：** Agility Robotics / TechCrunch
- **核心价值：** 这是人形机器人从样机展示走向资本市场和规模制造的强信号。对供应链而言，腿部执行器、整机制造、云端调度、安全系统和维护体系都会被订单牵引进入量产验证。

### 2. [Agility Digit v5 强调“协作安全”：人形硬件的下一道门槛不是会走，而是能与人同场工作](https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/)

**摘要：** TechCrunch 报道称，Agility 将利用上市交易资金扩大下一代 Digit v5 产能、履行订单并拓展客户。Agility 官方进一步强调，Digit v5 被设计为 AI-enabled cooperatively safe humanoid robot，目标是在制造、仓储、配送等真实工作环境中与人安全协同，而不是被隔离在固定工位里。

- **来源：** TechCrunch
- **核心价值：** 人形机器人的商业化评价标准正在变化：从“能否稳定运动”升级为“能否在有人、有叉车、有临时障碍的现场持续、安全、可审计地工作”。这会倒逼硬件冗余、碰撞检测、控制频率和安全认证体系升级。

### 3. [ABB Robotics × PSYONIC：用真实人手触觉与握持数据推进机器人灵巧性](https://www.abb.com/global/en/news/136690/prsrl-abb-robotics-and-psyonic-use-human-generated-data-to-advance-robotic-dexterity)

**摘要：** IEEE Spectrum 6 月 19 日 Video Friday 收录 ABB Robotics 与 PSYONIC 的合作：PSYONIC Ability Hand 已被数百名用户日常佩戴，可产生真实世界的触摸、压力和握持数据；ABB 的 GoFa 协作机器人则提供工业级精度与重复性，用于把人类手部数据转化为更可靠的机器人灵巧操作能力。

- **来源：** ABB Robotics / IEEE Spectrum
- **核心价值：** 这是今天的数据相关报道。灵巧操作数据不一定只来自机器人遥操作，假肢手在真实生活中的触觉和抓握数据，可能成为训练机器人手、机械臂末端执行器和触觉策略的低成本数据源。

### 4. [Sanctuary AI：Physical AI 转向硬件无关，先在工业灵巧任务中验证价值](https://sanctuary.ai/)

**摘要：** Sanctuary AI 官网最新定位强调“production-ready Physical AI for industrial work”，并称其 Physical AI 支持多种硬件配置、移动方式和末端执行器，路径包括 humanoids。其页面还突出“optimized for dexterous and dynamic work”，显示公司正从单一人形本体叙事转向可部署到不同商用机器人系统上的灵巧任务 AI。

- **来源：** Sanctuary AI
- **核心价值：** 这代表一种务实路线：在硬件形态尚未完全收敛前，先让 Physical AI 适配不同机械臂、夹爪、移动底盘和人形平台。对客户来说，价值不在“像不像人”，而在能否完成高频、动态、难以传统自动化的工序。

---

## 前沿论文

### 1. [CoorDex：Unitree G1 + 20 自由度灵巧手实现边走边操作](https://arxiv.org/abs/2606.23680)

**摘要：** `CoorDex` 针对人形机器人常见的“先走到物体前、停下、再操作”流程，提出身体与灵巧手协同的 latent residual control。系统先分别训练全身和手部 privileged motion tracking teachers，再蒸馏为本体感知条件的 latent priors，最后用协同残差策略组合身体和手部先验。论文展示 Unitree G1 搭载 20-DoF WUJI hand，可完成不停步抓瓶搬运、边走边开冰箱门、拿方块并旋转等任务。

- **来源：** arXiv / 项目页
- **核心价值：** 人形机器人真正进入工厂和家庭后，不可能每次都“停稳再抓”。CoorDex 把腿、躯干、手臂和手指放进同一个接触丰富控制问题，是高自由度硬件走向实用操作的重要一步。

### 2. [Tactile Genesis：2 万并行环境模拟触觉传感器，给机器人手硬件设计提供定量答案](https://arxiv.org/abs/2606.22332)

**摘要：** `Tactile Genesis` 是面向灵巧操作的 GPU 并行触觉传感器仿真平台，可在统一接口下模拟二值接触、接触深度、每 taxel 力 / 力矩、弹性体标记位移、几何接近、接触音频和体素化温度场。平台可在单 GPU 上超过 20,000 并行环境和 1,000 taxels，吞吐比此前触觉仿真器提升 3 到 20 倍。研究发现，本体感知单独不足以完成所有任务，传感器覆盖位置比类型更关键，全手覆盖明显优于仅指尖覆盖；200 个 taxels 分布全手已经足够，per-taxel force / torque 最稳定有效。

- **来源：** arXiv
- **核心价值：** 这篇论文直接回答硬件团队关心的问题：触觉传感器到底装在哪里、装多少、装哪种更值。它把触觉硬件设计从经验判断推向可仿真、可消融、可迁移到真实 XHand1 的数据驱动流程。

### 3. [One Body, Two Minds：可穿戴机器人手用“人机共身”完成辅助任务，用户成功率达 93.6%](https://arxiv.org/abs/2606.25575)

**摘要：** `One Body, Two Minds` 提出 co-embodiment with variable autonomy：人和机器人共享同一个可穿戴机器人手，但在不同任务阶段拥有不同自主权。系统在物体搜索和抓取阶段可由视觉运动扩散策略自主完成，抓取成功后通过信号告知用户，再由用户用免手部头部手势驱动电钻、喷壶、红外测温仪、打火机和冰淇淋勺等工具；用户始终保留释放手势作为 veto。44 名参与者用户研究显示，完成时间随试次提升 23.3%，最佳策略达到 93.6% 任务成功率，整体接受度为 5.70/7。

- **来源：** arXiv
- **核心价值：** 这给辅助机器人硬件一个新方向：不是把人完全排除在控制环外，而是让机器人手接管抓取等高负担阶段，人保留意图、工具使用和否决权。

### 4. [STIR Hand：两指软关节 + 应变片，也能感知尺寸、形状和材料硬度](https://arxiv.org/abs/2606.21245)

**摘要：** `Safe Thumb-Index Robotic Hand` 受人手拇指—食指结构启发，采用轻量低成本的两指非对称构型，结合欠驱动腱传动和嵌入硅胶软关节的柔性应变片。系统在抓取 20 种物体的数据集上进行无监督分析，并通过物体分类任务验证软关节传感贡献：不依赖额外指尖触觉或外部视觉，也能区分物体尺寸、形状和材料刚度。

- **来源：** arXiv
- **核心价值：** 灵巧不一定等于昂贵和复杂。STIR Hand 说明，结构顺应性 + 软关节内嵌传感，可以让低自由度手获得更安全、更敏感的抓取能力，适合低成本服务机器人和教育 / 研究平台。

### 5. [APR Pianist：用少量人类弹琴数据约束高自由度灵巧手姿态](https://arxiv.org/abs/2606.23848)

**摘要：** `Adversarial Posture Regularization` 关注双手高自由度灵巧手弹钢琴。仅靠任务奖励或 IK 反解，强化学习策略容易出现不自然姿态和关节过伸。APR 使用少量非对齐的人类随手弹琴数据，通过对抗目标匹配策略姿态分布与人类先验，无需昂贵的逐曲示范数据。团队还用消费级 Meta Quest 3 采集并释放非结构化手部弹琴运动数据，重定向到 Shadow Hand。

- **来源：** arXiv / GitHub
- **核心价值：** 对灵巧手来说，“成功按下琴键”不等于“安全、自然、可长期执行”。APR 说明人类姿态先验可以作为硬件保护和动作质量约束，减少关节过伸等真实硬件风险。

### 6. [异步上肢轨迹跟踪：让人形机器人上半身更好执行低频任务空间指令](https://arxiv.org/abs/2606.25706)

**摘要：** `Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots` 针对一个很实际的控制问题：高层规划器常输出稀疏、低频任务空间轨迹，但全身控制器需要高频执行。论文提出异步上肢任务空间跟踪框架，用 teacher-student distillation 初始化学生策略，并在执行时利用缓存未来轨迹和时间索引；后训练阶段用 MPC 补全稀疏参考到浮动基座和上肢引导。仿真和 Unitree G1 硬件实验显示，该方法在低更新率下跟踪更稳，对分布外动作适应更安全。

- **来源：** arXiv
- **核心价值：** 机械臂和人形上肢要接 VLA / 任务规划，必须解决低频语义指令和高频硬件控制之间的时间错位。这类上肢控制器会成为“模型大脑”落到真实手臂的关键中间层。

---

## 开源生态

### 1. [CoorDex 项目页开放：身体与灵巧手协同控制的可视化样板](https://skevinci.github.io/coordex/)

**摘要：** CoorDex 项目页展示了方法流程、仿真、真实机器人演示和动作空间对比。真实演示使用 Unitree G1 搭载 7-DoF Dex3-1 dexterous hand，展示 WalkGrab、OpenFridge、WalkPickTurn；仿真中则使用 20-DoF WUJI hand，并在 Isaac Lab 中训练。

- **来源：** 项目页
- **核心价值：** 对硬件和算法团队都很有参考价值：它把高维手部控制从直接 joint-space PPO 转成 latent-prior residual，降低了边走边抓这类复杂任务的训练难度。

### 2. [APR Pianist 仓库发布：人类手部姿态先验进入灵巧手强化学习](https://github.com/APRProject/APRPianist)

**摘要：** APR Pianist 论文给出项目仓库，用于展示高自由度灵巧手弹钢琴的对抗姿态正则方法。该项目的重点不是单纯追求音符准确率，而是让 Shadow Hand 的姿态更接近人类手部运动分布，减少不自然关节形态。

- **来源：** GitHub
- **核心价值：** 真实灵巧手训练必须考虑机械寿命、关节限位和动作可解释性。把人类姿态数据开源出来，有助于社区构建更安全、更自然的手部控制基准。

### 3. [TurboMPC 开源：GPU 可微 MPC 可服务人形控制和机器人强化学习](https://github.com/ToyotaResearchInstitute/turbompc)

**摘要：** Toyota Research Institute 的 `TurboMPC` 是全 GPU 运行的可微 MPC 求解器，支持状态 / 控制不等式约束、隐式积分器、跨时间耦合代价和 slack variables。论文显示，它在约束规划、人形模仿学习、带神经网络代价的强化学习任务中，相比 SOTA CPU 和 GPU 可微求解器分别最高加速 15 倍和 58 倍。

- **来源：** GitHub / arXiv
- **核心价值：** 人形和机械臂控制越来越需要把学习策略与可解释约束控制结合。TurboMPC 这类工具能让硬件团队在高频控制、参数调优和安全约束之间获得更高迭代速度。

### 4. [Tactile Genesis 项目页：触觉仿真成为灵巧手硬件选型工具](https://neuroagents-lab.github.io/2026-tactile-genesis/)

**摘要：** Tactile Genesis 项目页展示了多种触觉抽象、噪声模型、覆盖位置和分辨率消融，并验证到真实 XHand1。项目的核心价值在于把“触觉传感器该怎么布置”转化为可重复仿真实验，而不是只靠单个硬件样机试错。

- **来源：** 项目页
- **核心价值：** 对灵巧手厂商来说，触觉覆盖和传感类型直接影响成本、布线和可靠性。这个项目为下一代传感手提供了更接近工程决策的评估框架。

---

## 公司情报

### 1. [Agility Robotics：上市资金将用于 Digit v5 量产、部署和安全平台](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility 表示，交易资金将用于履行现有客户订单、扩大商业部署、提升 Digit v5 产能，并继续投资机器人、Physical AI、软件、安全系统和制造基础设施。公司还披露 RoboFab 目标支持最高 10,000 台年产能，Digit 约 75% 零部件来自美国本土供应链。

- **来源：** Agility Robotics
- **核心价值：** 人形机器人进入量产阶段后，硬件能力不只体现在单台 demo，而体现在产能、供应链、维修、云平台、真实运行小时数和安全认证的系统能力。

### 2. [ABB Robotics：协作机械臂开始吸收假肢手的真实触觉数据](https://www.abb.com/global/en/news/136690/prsrl-abb-robotics-and-psyonic-use-human-generated-data-to-advance-robotic-dexterity)

**摘要：** ABB 与 PSYONIC 的合作把人类日常使用 Ability Hand 产生的触摸、压力、握持数据，与 ABB GoFa 协作机器人平台结合，目标是提升机器人处理精细、不规则和不可预测物体的能力。

- **来源：** ABB Robotics
- **核心价值：** 这是机械臂公司补齐灵巧末端能力的一条现实路径：不一定从零设计一只全新手，而是利用真实人手—假肢手数据，训练更可靠的抓握和接触策略。

### 3. [Sanctuary AI：从人形本体叙事转向硬件无关的工业 Physical AI](https://sanctuary.ai/)

**摘要：** Sanctuary AI 官网强调，其 Physical AI 可支持多种硬件配置、移动方案和末端执行器，并面向“traditional automation can’t reliably handle”的工业任务。公司把重点放在 production-ready performance，而非只展示某一款机器人本体。

- **来源：** Sanctuary AI
- **核心价值：** 对工业客户而言，硬件形态可以多样，但任务成功率、节拍、稳定性和集成成本必须清晰。Sanctuary 的定位变化说明 Physical AI 正在与机械臂、夹爪、移动平台和人形本体同时耦合。

### 4. [Unitree G1：成为多篇人形上肢、全身控制和灵巧手论文的真实验证平台](https://arxiv.org/abs/2606.23680)

**摘要：** 最近一批论文中，Unitree G1 频繁作为真实人形硬件平台出现：CoorDex 在 G1 上验证灵巧手边走边操作；异步上肢轨迹跟踪论文也在 G1 硬件上验证低频任务空间轨迹执行。这说明通用研究平台正在从桌面机械臂扩展到完整人形本体。

- **来源：** arXiv
- **核心价值：** 硬件平台一旦被大量论文、开源项目和实验室采用，就会形成数据、控制器、仿真模型和开发者工具的生态复利。G1 的研究密度值得国内具身硬件厂商关注。

---

## 结尾总结

6 月 26 日这期的主线，是具身智能正在重新重视“身体”。过去几天我们持续看到 VLA、世界模型和数据闭环的进展，但今天的硬件线索提醒我们：模型再强，也必须通过关节、执行器、触觉传感器、灵巧手、机械臂和全身控制器与世界发生接触。

PDS Joint 把柔顺结构和本体感知合进关节，Tactile Genesis 给触觉硬件选型提供仿真依据，STIR Hand 证明低成本软关节也能产生有效感知，CoorDex 让人形机器人从“停下再抓”走向“边走边操作”，Agility 则用 Digit v5 的订单和上市计划证明硬件量产正在成为资本市场关注点。

可以下一个判断：**具身智能的下一轮竞争，不会只发生在模型参数里，而会发生在“能被模型充分利用的身体”里。** 谁能把硬件顺应性、触觉覆盖、控制频率、真实数据回流和量产能力连成闭环，谁才更接近可规模化部署的机器人。

**互动问题：** 你认为未来一年具身硬件最值得突破的是高扭矩关节、灵巧手、触觉皮肤、低成本机械臂，还是整机量产能力？欢迎留言讨论。

## 关键词索引

**公司与机构：** Agility Robotics、ABB Robotics、PSYONIC、Sanctuary AI、Unitree、Toyota Research Institute、University of North Carolina at Chapel Hill、University of California Berkeley  
**模型与项目：** PDS Joint、CoorDex、Tactile Genesis、STIR Hand、APR Pianist、TurboMPC、Digit v5、GoFa、Ability Hand、Unitree G1、WUJI Hand、Dex3-1、XHand1  
**技术方向：** 具身硬件、灵巧手、柔顺关节、双螺旋关节、本体感知、嵌入式电感传感、触觉仿真、触觉覆盖、软关节应变片、欠驱动手、全身控制、上肢轨迹跟踪、边走边操作、协作安全、人形机器人量产、数据闭环  
**关键数字：** PDS Joint 关节状态估计误差降低 41.6%、开源灵巧手抓取 9 种日常物体、Agility 估值约 25 亿美元 / 预计收益超 6.2 亿美元 / Digit 超 65,000 小时运行 / Digit v5 超 3 亿美元多年订单、Tactile Genesis 超 20,000 并行环境 / 1,000 taxels / 3-20 倍吞吐提升、One Body Two Minds 用户完成时间提升 23.3% / 任务成功率 93.6%、TurboMPC 最高 15 倍和 58 倍加速

## 值得分享

1. **灵巧手竞争正在下沉到关节层：** PDS Joint 把柔顺、安全和本体感知做进指关节，在复杂外展 / 内收估计中误差降低 41.6%。
2. **触觉硬件开始有数据驱动的设计答案：** Tactile Genesis 显示全手覆盖比只装指尖更关键，约 200 个 taxels 分布全手就能覆盖多类灵巧任务。
3. **人形机器人量产进入资本市场验证：** Agility 拟以约 25 亿美元估值上市，Digit 已累计超 65,000 小时真实运行，Digit v5 获超 3 亿美元多年订单。
