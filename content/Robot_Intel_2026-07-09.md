# 具身智能情报前沿｜人形本体走向重载全身控制

**作者：具身视界** · 2026.07.09

> 今天最值得关注的变化，是人形机器人本体讨论正在从“像不像人、能不能走”转向“全尺寸、重载、受力交互和可部署控制”。HEFT、ThorArena、WristMimic、Athena-WBC 与 OpenArm 等新动态共同说明，本体竞争的核心开始回到工程能力：尺寸、载荷、关节、传感、全身协调和真实接触。

---

## 💥 今日重磅

### [HEFT：175cm、65kg 全尺寸人形机器人实现 24kg 载荷遥操作跟踪](https://arxiv.org/abs/2607.02332v1)

**摘要：** HEFT 针对全尺寸人形机器人在真实载荷下的遥操作问题，提出 Heavy-Payload Full-size Humanoid Teleoperation 框架。论文指出，许多人形遥操作系统只在小型平台或无真实负载条件下验证，而全尺寸本体会遇到更大的惯性、更窄的平衡裕度，以及消费级 VR tracker 噪声、漂移和重定向误差。HEFT 用 Privileged Motion Guidance 从可部署的噪声 VR 参考中学习物理合理参考，再用 Windowed Payload Curriculum 逐步提升载荷上限。团队在 L7 人形机器人上验证，该本体身高 175cm、体重 65kg，可在最高 24kg 载荷下跟踪转身、前后移动和深蹲等动作。这件事的价值不只是“能搬重物”，而是把人形本体从轻量演示推向真实工况：仓储、制造、巡检等场景需要机器人在负载、惯性和接触扰动下稳定工作，本体结构、驱动能力和控制策略必须一起过关。

- **来源：** arXiv
- **核心价值：** 人形机器人进入工程化阶段后，关键指标会从演示动作数量转向全尺寸本体在真实载荷下的稳定性、可控性和安全裕度。

---

## 📰 行业新闻

### 1. [Unitree G1 官方页显示 23 自由度、约 35kg、起价 1.35 万美元：可购买本体继续降低研究门槛](https://www.unitree.com/g1)

**摘要：** Unitree G1 官方页面可访问，页面列出站立尺寸约 1320x450x200mm、含电池重量约 35kg、关节自由度 23、膝关节最大扭矩 90N.m、智能快拆电池 9000mAh、续航约 2 小时、税费和运费前起价 1.35 万美元，并支持二次开发版本。这类可购买、规格明确、社区使用频繁的人形本体，正在成为论文验证和数据采集的重要底座。

- **来源：** Unitree Robotics
- **核心价值：** 人形本体生态的分水岭之一，是谁能把“研究平台”做成可复现、可购买、可二次开发的工程产品。

### 2. [NVIDIA Isaac GR00T N1.7 仓库继续活跃：本体能力需要基础模型和仿真平台接住](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** GitHub API 显示，NVIDIA/Isaac-GR00T 7 月 7 日仍有推送，7 月 8 日星标约 7533，仓库描述为 Isaac GR00T N1.7 通用机器人基础模型。随着 HEFT、Athena-WBC、ThorArena 等工作把全尺寸、全身控制和受力交互推到前台，基础模型平台需要处理的不只是动作生成，还包括本体差异、关节限制、负载变化和仿真到真实的动力学一致性。

- **来源：** GitHub API / NVIDIA Developer
- **核心价值：** 人形机器人本体越复杂，越需要模型、仿真、数据和运行时共同支撑，而不是单靠硬件规格取胜。

### 3. [OpenArm 星标约 2702：开源人形上肢成为本体生态的新入口](https://github.com/enactic/openarm)

**摘要：** GitHub API 显示，enactic/openarm 7 月 6 日仍有推送，7 月 8 日星标约 2702。仓库描述为面向 physical AI 研究和接触丰富环境部署的完全开源人形手臂。本体生态不只包括整机人形，也包括可替换、可复现、可部署的上肢组件；这对实验室、创业团队和灵巧操作研究尤其重要。

- **来源：** GitHub API
- **核心价值：** 人形本体的开放化会先从上肢、关节、SDK 和仿真描述等模块切入，逐步降低整机研发和复现实验门槛。

---

## 📑 前沿论文

### 1. [ThorArena：采集人体运动与双手受力，评测人形机器人真实物理交互](https://arxiv.org/abs/2607.06052v1)

**摘要：** ThorArena 面向人形机器人接触丰富任务，指出现有数据集和基准多关注运动学轨迹，忽略同步交互力。论文采集真实世界中全身人体运动和双手施力数据，覆盖 6 类代表性物理交互任务，并提出 Force-Aware Tracking Score 等指标，把全身跟踪精度、不同受力水平下的鲁棒性、控制代价和 episode 存活率放在同一评测协议中。该基准还可在仿真中回放记录的交互力，标准化比较不同人形控制策略。

- **作者团队：** Chenhao Yu、Hongwu Wang、Weitao Zhang、Youhao Hu、Jiachen Zhang、Gangyang Li、Alois Knoll、Shaqi Luo
- **来源：** arXiv
- **核心价值：** 数据相关报道：人形本体要进入真实世界，评测数据必须从“姿态像不像”升级到“受力后稳不稳、能不能活下来”。

### 2. [WristMimic：用腕部引导全身控制，降低人形手部迁移对手型的依赖](https://arxiv.org/abs/2607.06438v1)

**摘要：** WristMimic 提出以腕部为分界的人形全身控制框架：身体和腕部跟踪运动学目标，手指不直接监督人手姿态，而是从物体跟踪和接触结果中学习抓取与操作。论文认为，腕部处在自由运动和接触丰富操作之间，既能稳定放置手部，又不会过度约束不同手型的手指接触行为。实验显示，该方法可达到或超过使用完整手指姿态监督的方法，并支持跨多种手部本体迁移。

- **作者团队：** Wongyun Yu、Youngwoon Kim、Minsu Cho
- **来源：** arXiv
- **核心价值：** 人形本体的手部硬件不会统一，能否用腕部和接触结果做跨手型迁移，会影响灵巧操作生态扩展速度。

### 3. [Athena-WBC：用能力对齐专家解决人形全身控制长尾动作](https://arxiv.org/abs/2607.04837v2)

**摘要：** Athena-WBC 关注大规模人形 motion tracking 中的长尾失败：即便对难动作增加采样、切分子集或训练专家，仍有高动态转移和平衡关键动作难以恢复。论文提出紧凑 teacher-student 流水线，让动态专家去掉保守努力和时间控制惩罚，保留物理可行约束；平衡专家用重力课程提升早期训练存活率。随后通过 DAgger 蒸馏和 RL 微调压缩为单一可部署控制器，在全尺寸人形上提升训练集长尾动作恢复和 held-out 跟踪表现。

- **作者团队：** Yuan Jiang、Ningyuan Zhang、Xicun Yang、Yuzhi Jiang、Jie Chen
- **来源：** arXiv
- **核心价值：** 人形本体控制的难点不是平均动作，而是长尾、高动态、接近平衡边界的动作能否稳定落地。

### 4. [LingBot-VLA 2.0：6 万小时数据覆盖 20 种机器人配置和全身自由度](https://arxiv.org/abs/2607.06403v1)

**摘要：** LingBot-VLA 2.0 从应用落地角度改进 VLA 模型，重新整理数据处理管线，并构建约 6 万小时预训练数据，其中包括 5 万小时机器人轨迹，覆盖 20 种机器人配置，以及 1 万小时人类第一视角视频。系统扩展动作空间，纳入头部、腰部、移动底盘和灵巧手自由度，并加入未来预测作为代理任务。论文称，扩展预训练数据覆盖全身自由度后，模型在两种机器人平台上表现出跨本体长时序移动操作能力。

- **作者团队：** Wei Wu、Fangjing Wang、Fan Lu、He Sun、Shi Liu、Yunnan Wang 等
- **来源：** arXiv
- **核心价值：** 数据相关报道：人形基础模型不能只学手臂轨迹，必须把头、腰、底盘、灵巧手和不同本体配置一起纳入训练分布。

### 5. [Actuator Reality Shaping：把真实电机塑造成仿真参考，改善人形零样本迁移](https://arxiv.org/abs/2607.02205v2)

**摘要：** Actuator Reality Shaping 反过来处理 sim-to-real 问题：不是不断让仿真匹配真实电机，而是通过双自由度前馈-反馈控制器，把真实执行器闭环行为塑造成训练时假设的理想二阶参考动态。论文在单关节高减速比伺服、7 自由度机械臂、轮腿机器人和人形机器人行走中验证，显示该方法可减少跟踪误差并提升零样本任务表现。

- **作者团队：** Satoshi Yamamori、Koji Ishihara、Kenjiro Minamikawa、Ryosei Ohmori、Taiyo Yasaki、Norikazu Sugimoto、Jun Morimoto
- **来源：** arXiv / 项目页
- **核心价值：** 对人形本体来说，执行器接口标准化可能比单纯提高仿真精度更直接影响策略迁移成功率。

---

## 💻 开源生态

### 1. [ProtoMotions：NVIDIA 开源人形/数字人运动训练框架持续更新](https://github.com/NVlabs/ProtoMotions)

**摘要：** GitHub API 显示，NVlabs/ProtoMotions 7 月 6 日仍有推送，7 月 8 日星标约 1991。项目定位为 GPU 加速仿真与学习框架，用于训练物理仿真的 digital humans 和 humanoid robots。它与 GR00T 形成互补：一个偏基础模型入口，一个偏运动与仿真训练底座。

- **来源：** GitHub API
- **核心价值：** 人形本体控制需要大规模仿真训练，GPU 加速的人形运动框架会成为本体能力迭代的基础设施。

### 2. [Asimov-1：开源人形机器人仓库星标约 981](https://github.com/asimovinc/asimov-1)

**摘要：** GitHub API 显示，asimovinc/asimov-1 7 月 3 日仍有推送，7 月 8 日星标约 981，仓库描述为 open-source humanoid robot。与单纯算法仓库不同，开源人形整机项目把机械、电控、软件和文档共同暴露给社区，适合教育、研究和低成本本体验证。

- **来源：** GitHub API
- **核心价值：** 开源整机本体虽未必直接替代商业人形，但会推动零部件选型、结构设计和二次开发方法更透明。

### 3. [bipedal-locomotion-framework：双足运动库 7 月 2 日仍有推送](https://github.com/gbionics/bipedal-locomotion-framework)

**摘要：** GitHub API 显示，gbionics/bipedal-locomotion-framework 7 月 2 日仍有推送，星标约 224。仓库描述为一组用于人形机器人双足运动的库。对本体团队来说，稳定行走、状态估计、接触切换和控制接口仍是上层 VLA 或遥操作系统能否落地的基本盘。

- **来源：** GitHub API
- **核心价值：** 人形本体工程不是只堆模型，底层双足运动软件库仍决定机器人能不能稳定站住、走稳和承受扰动。

### 4. [EngineAI Native Control SDK：人形机器人原生控制 SDK 7 月 2 日更新](https://github.com/engineai-robotics/engineai_robotics_native_sdk)

**摘要：** GitHub API 显示，engineai-robotics/engineai_robotics_native_sdk 7 月 2 日仍有推送，仓库描述为面向人形机器人应用开发和系统集成的 EngineAI Native Control SDK。虽然星标约 44，社区规模仍小，但 SDK 方向说明整机厂正在把本体能力包装成开发接口，而不是只发布硬件视频。

- **来源：** GitHub API
- **核心价值：** 本体公司如果想形成生态，必须开放稳定控制接口，让开发者能在真实硬件上构建应用和收集数据。

---

## 🏢 机器人公司情报

### 1. [Unitree：G1、H1 / H1-2、H2、R1 等本体矩阵显示“多规格人形”路线](https://www.unitree.com/g1)

**摘要：** Unitree 官网的人形机器人导航已同时列出 H2、R1、G1、H1 / H1-2，以及 G1-D、G1-Comp、G1-Boxing 等应用计划。结合 G1 起价、二次开发和可公开访问规格，Unitree 的优势不只是单台机器人，而是用多规格本体覆盖教育、研究、开发和应用验证。

- **来源：** Unitree Robotics
- **核心价值：** 人形本体竞争会从单一旗舰机，转向价格、尺寸、载荷、自由度和开发者接口的产品矩阵竞争。

### 2. [NVIDIA：GR00T 与 ProtoMotions 共同强化人形本体训练生态](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** NVIDIA 一边通过 Isaac GR00T 提供通用机器人基础模型入口，一边通过 NVlabs/ProtoMotions 提供 GPU 加速人形运动训练框架。对整机厂来说，这意味着本体能力未来会越来越依赖平台化工具链：仿真训练、基础模型、数据管线、运行时推理和硬件加速需要协同。

- **来源：** GitHub API / NVIDIA Developer
- **核心价值：** 上游平台公司正在把人形本体从“硬件项目”变成“模型 + 仿真 + 控制 + 算力”的系统工程。

### 3. [EngineAI：Native Control SDK 显示人形整机厂开始开放集成接口](https://github.com/engineai-robotics/engineai_robotics_native_sdk)

**摘要：** EngineAI Native Control SDK 面向人形机器人应用开发和系统集成。对本体公司来说，SDK 是连接硬件销售、开发者生态和真实应用的关键环节；如果没有稳定接口，下游团队很难把人形本体接入任务规划、遥操作、数据采集和业务系统。

- **来源：** GitHub API
- **核心价值：** 人形本体商业化不能只靠整机性能，还要靠可开发、可集成、可维护的软件接口。

### 4. [Enactic OpenArm：开源上肢说明本体生态会先从模块化部件扩散](https://github.com/enactic/openarm)

**摘要：** OpenArm 把人形上肢作为开源模块开放，定位 physical AI 研究和接触丰富环境部署。它说明本体生态并不一定从整机开源开始，上肢、手、关节、电控和仿真模型都可能先形成社区标准。对灵巧操作和移动操作研究来说，模块化上肢能降低复现实验成本。

- **来源：** GitHub API
- **核心价值：** 人形本体生态的开放入口可能不是整机，而是那些最影响操作能力、又最需要复现实验的核心模块。

---

## 结尾总结

7 月 9 日的主线很明确：人形机器人本体正在从“外形和演示”进入“全尺寸工程能力”验证。HEFT 证明重载和全身遥操作正在成为硬指标，ThorArena 把受力交互纳入数据和评测，WristMimic、Athena-WBC、Actuator Reality Shaping 则分别从手部迁移、长尾动作和执行器接口解决本体控制问题。下一阶段，人形公司真正需要证明的是：本体能否承受真实负载、真实接触和真实开发者使用。

---

> 💬 你认为人形机器人本体最先拉开差距的会是哪一项：载荷能力、关节可靠性、双足稳定性、灵巧手，还是开放 SDK？

---

## 关键词索引

**公司：** Unitree / NVIDIA / EngineAI / Enactic / Asimov
**技术：** 人形机器人本体 / 全尺寸人形 / 重载遥操作 / 全身控制 / 双足运动 / 受力交互评测 / 执行器接口 / sim-to-real / VLA / 机器人 SDK
**项目 / 数据：** HEFT / ThorArena / WristMimic / Athena-WBC / LingBot-VLA 2.0 / Actuator Reality Shaping / OpenArm / ProtoMotions / Asimov-1 / bipedal-locomotion-framework / EngineAI Native Control SDK / Isaac GR00T / Unitree G1

---

## 值得分享

1. 人形本体开始进入重载验证：HEFT 在 175cm、65kg 的全尺寸人形上实现最高 24kg 载荷跟踪。
2. 人形评测开始看受力数据：ThorArena 采集全身人体运动和双手施力，专门评测接触任务下的稳定性。
3. 开放生态正在扩展到硬件本体：OpenArm、Asimov-1、EngineAI SDK 说明上肢、整机和控制接口都在走向社区化。
