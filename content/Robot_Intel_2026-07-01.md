# 具身智能情报前沿｜Agility 25 亿美元 SPAC 定价人形机器人

**作者：具身视界** · 2026.07.01

> 今天最值得关注的变化，是具身智能正在被资本市场用“订单、客户、产能和数据验证”重新定价。Agility 拟通过 SPAC 上市，把 NVIDIA、Amazon、Toyota、SoftBank、Foxconn 等上市公司和产业资本一起推到台前，也让人形机器人从技术叙事进入财务与规模化验证阶段。

---

## 💥 今日重磅

### [Agility Robotics 拟 SPAC 上市：25 亿美元估值、超 6.2 亿美元融资，把人形机器人推向资本市场验证](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility Robotics 6 月 24 日宣布与 Churchill Capital Corp XI 达成合并上市协议，交易预计使 Agility 成为美国市场少见的纯人形机器人上市标的。公司披露投前股权价值 25 亿美元，预计获得超过 6.2 亿美元总收益，其中约 2 亿美元来自每股 10 美元的普通股 PIPE；Digit v5 已获得超过 3 亿美元多年订单，并在 Schaeffler、GXO、Toyota Motor Manufacturing Canada、Mercado Libre 等客户环境中运行。更关键的是，Agility 背后同时出现 NVIDIA、Amazon、SoftBank Vision Fund 2、Foxconn、Schaeffler 等战略投资方和产业伙伴。这说明资本市场不再只看“人形机器人能否演示”，而是开始追问订单是否可交付、产线是否可复制、客户现场是否能持续产生运维与数据闭环。对整机厂、零部件公司、模型平台和上市公司投资人来说，Agility 这次交易提供了一个新的估值锚点：具身智能公司的价值将越来越由真实部署密度来决定。

- **来源：** Agility Robotics
- **核心价值：** 人形机器人融资正在从“技术想象力定价”转向“订单、客户和部署数据定价”。

---

## 📰 行业新闻

### 1. [TechCrunch 解读 Agility SPAC：30 多个潜在客户评估大规模部署](https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/)

**摘要：** TechCrunch 报道称，Agility 本轮 SPAC 交易估值约 25 亿美元，预计带来超过 6.2 亿美元资金，其中约 2 亿美元来自新老机构投资者。报道称 Digit 正用于 9 个客户站点，公司已获得超过 3 亿美元多年订单，并有 30 多个潜在客户评估大规模部署。资金用途包括提升 Digit v5 产能、履行现有订单、扩展新老客户。

- **来源：** TechCrunch
- **核心价值：** 资本市场开始把“大规模部署管线”作为人形机器人公司估值的重要证据。

### 2. [NVIDIA Isaac GR00T：上市公司把具身智能入口从芯片扩展到数据、仿真和实时控制](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA Isaac GR00T 官方页面显示，其人形机器人开放参考平台包含开放数据与数据管线、机器人基础模型、Omniverse / Cosmos 仿真框架、中间件、CUDA-X 加速运行时库，以及用于实时机器人推理和控制的 Jetson Thor。对上市公司 NVIDIA 来说，具身智能不只是卖算力，而是把训练、仿真、部署和控制工具链变成生态入口。

- **来源：** NVIDIA Developer
- **核心价值：** 上市公司正在用平台化方式卡位具身智能，把机器人公司变成模型、仿真和边缘算力生态的用户。

### 3. [ABC 双臂操作开放栈：Amazon FAR、MIT、UC Berkeley 等把真实评测日志推向社区](https://abc.bot/)

**摘要：** ABC 项目页显示，该开放栈由 UC Berkeley、MIT、Amazon FAR、XDOF、CMU 等参与，释放 3,553 小时、134,806 条 episode、195 个任务的双臂操作数据，同时包括 400 小时仿真遥操作数据、真实评测日志、训练基础设施和硬件方案。Amazon FAR 的参与说明上市公司研究团队正在通过开放数据栈影响机器人基础模型和操作策略路线。

- **来源：** ABC 项目页
- **核心价值：** 数据和评测日志正在成为产业资本判断具身模型路线的重要公共基准。

---

## 📑 前沿论文

### 1. [REPAIR-Bench：214 次交互试验评测机器人失败感知与恢复](https://arxiv.org/abs/2606.29937v1)

**摘要：** REPAIR-Bench 基于 41 名参与者、214 次交互试验构建，覆盖 4 类诱发失败，并同步记录面部动作单元、头部姿态、语音转录、交互后情绪和恢复报告。它不只做二分类失败检测，还评测连续交互中的失败识别、失败类型分类和以用户为中心的恢复策略预测。基线中，分层循环模型 strict F1 从 0.68 提升到 0.80，QLoRA 微调 Mistral-7B 在恢复预测上达到 Hit@5=0.76。

- **作者团队：** Giuliano Pioldi、Yashika Batra、Arman Ibrayeva、Yuanchen Bai、Purnjay Maruur、Promise Ekpo、Angelique Taylor
- **来源：** arXiv
- **核心价值：** 这是今天的数据相关报道：上市和融资之后，机器人公司需要用标准化失败数据证明系统可靠，而不是只展示成功案例。

### 2. [Critical Interval MSE：让离线验证更接近真实机器人 rollout 表现](https://arxiv.org/abs/2606.29898v1)

**摘要：** 真实机器人评测成本高、难复现，导致策略迭代速度受限。Critical Interval MSE 提出只在任务关键片段计算误差，并配合动作对齐，使离线验证更接近 rollout 时的表现。论文显示，CI-MSE 与真实表现的 Spearman 排名相关达到 -0.87，明显优于原始 MSE 的 -0.61。对产业化机器人公司而言，这类指标能降低每次模型选择都依赖真机大规模试错的成本。

- **作者团队：** Haoxu Huang、Tongsam Zheng、Yifan Chen、Jiacheng You、Yang Gao
- **来源：** arXiv
- **核心价值：** 资本市场要看规模化，研发团队则需要更便宜、更稳定的离线验证指标来支撑快速迭代。

### 3. [CSAR：面向机器人团队的容器化系统架构](https://arxiv.org/abs/2606.30293v1)

**摘要：** CSAR 面向嵌入式设备、边缘服务器和云资源混合的机器人系统，提出基于 LXC/LXD、ROS 2/DDS 和三层边缘基础设施的容器化架构。论文强调依赖隔离、兼容性、可复现、专用硬件共享和异构环境部署，并通过边缘卸载 3D SLAM、GPU 加速语义建图等用例验证。融资后的机器人团队往往面临多人协作和跨场景交付，CSAR 这类基础设施能降低工程复制成本。

- **作者团队：** Ambrosio-Cestero、Gregorio、Galindo Andrades、Cipriano、Gonzalez-Jimenez、Javier、Ruiz-Sarmiento、Jose-Raul
- **来源：** arXiv
- **核心价值：** 机器人公司从 Demo 走向交付，软件架构的可复制性会直接影响资金使用效率。

---

## 💻 开源生态

### 1. [NVIDIA Isaac-GR00T：人形基础模型仓库星标超过 7,400，继续吸附开发者生态](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** GitHub 数据显示，NVIDIA/Isaac-GR00T 仓库 6 月 30 日星标约 7,467，仓库定位为 Isaac GR00T N1.7 通用机器人基础模型。结合官方页面的开放数据、仿真、实时推理和全身控制组件，GR00T 已经成为上市公司进入具身智能生态的典型入口：先开放模型和工具链，再把开发者、硬件平台和部署需求导向自家算力体系。

- **来源：** GitHub
- **核心价值：** 上市公司参与具身智能，最强的抓手往往不是单个机器人产品，而是开发者平台和工具链标准。

### 2. [ABC 仓库：Amazon FAR 参与的行为克隆开放栈星标超过 200](https://github.com/amazon-far/abc)

**摘要：** amazon-far/abc 仓库 6 月 30 日星标约 217，描述为“Scalable Behavior Cloning with Open Data, Training, and Evaluation”。项目释放数据、训练、评测与日志，让双臂操作策略能在社区里做可复现实验。对融资和上市公司观察者来说，这类开放栈能帮助判断哪些模型路线具备真实任务可迁移性。

- **来源：** GitHub
- **核心价值：** 开源数据栈正在把具身智能的竞争从“谁有内部数据”推进到“谁能形成公共基准和生态影响力”。

### 3. [TurboMPC：Toyota Research Institute 的 GPU 可微 MPC 工具链持续更新](https://github.com/ToyotaResearchInstitute/turbompc)

**摘要：** ToyotaResearchInstitute/turbompc 仓库 6 月 29 日仍有推送，6 月 30 日星标约 93，描述为“Fast, Scalable, and Differentiable Model Predictive Control on the GPU”。Toyota 同时出现在 Agility 客户名单和机器人控制开源生态里，说明传统制造上市公司正在从应用、客户场景和底层控制工具多线接入具身智能。

- **来源：** GitHub
- **核心价值：** 产业上市公司不只会采购机器人，也会通过控制、仿真和制造场景塑造机器人技术路线。

---

## 🏢 机器人公司情报

### 1. [Agility Robotics：拟以 AGLT 代码登陆北美交易所](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility 公告称，交易完成后合并公司预计继续以 Agility 运营，并以 “AGLT” 为代码在北美主要交易所上市。公司定位为 humanoid robotics 与 physical AI 企业，资金将用于履行订单、扩大商业部署、提升 Digit v5 产能和继续投资集成平台。

- **来源：** Agility Robotics
- **核心价值：** 如果交易完成，二级市场将首次更直接地给“纯人形机器人商业化”定价。

### 2. [NVIDIA：从 Agility 投资方到 GR00T 平台方，构建具身智能资本与工具双入口](https://developer.nvidia.com/isaac/gr00t)

**摘要：** Agility 公告列出 NVIDIA 为其战略投资方之一；与此同时，NVIDIA 通过 Isaac GR00T 提供开放基础模型、数据管线、仿真框架、CUDA-X 运行时库和 Jetson Thor。资本参与和平台供给叠加，让 NVIDIA 在具身智能产业链中同时具备投资收益、算力需求和生态标准三重位置。

- **来源：** Agility Robotics / NVIDIA Developer
- **核心价值：** NVIDIA 的具身智能打法不是单点押注，而是用资本和工具链同时绑定未来机器人公司。

### 3. [Amazon：既是 Agility 背后资本，又通过 Amazon FAR 参与 ABC 数据栈](https://abc.bot/)

**摘要：** Agility 公告列出 Amazon 为其支持方之一；ABC 项目页则显示 Amazon FAR 参与开放双臂操作数据、训练基础设施和真实评测日志。一个方向连接人形机器人部署公司，另一个方向连接操作学习公共底座，说明 Amazon 在具身智能里既关注物流/仓储场景，也关注可复现研究基础设施。

- **来源：** Agility Robotics / ABC 项目页
- **核心价值：** 拥有真实物流场景的上市公司，将越来越能影响机器人公司优先解决哪些任务。

### 4. [Toyota：从 Agility 客户到 TRI 开源控制工具，制造业场景继续牵引人形机器人](https://github.com/ToyotaResearchInstitute/turbompc)

**摘要：** Agility 披露 Digit 已服务 Toyota Motor Manufacturing Canada；Toyota Research Institute 的 TurboMPC 又持续更新 GPU 可微 MPC 工具链。制造业客户不仅提供订单和真实工位，也通过控制、规划和仿真研究影响机器人可交付能力。对人形机器人公司来说，制造场景仍是最现实的商业化试金石之一。

- **来源：** Agility Robotics / GitHub
- **核心价值：** 制造业上市公司正在从“买方”变成具身智能技术路线的共同定义者。

---

## 结尾总结

今天的主线不是“又一家机器人公司融资”，而是具身智能开始进入资本市场可量化验证阶段：订单、客户站点、产能、真实评测数据和开源工具链都会影响估值。Agility 给出了人形机器人上市样本，NVIDIA、Amazon、Toyota 则从算力、数据、客户场景和控制工具四个方向说明，上市公司正在成为具身智能产业化的关键变量。

---

> 💬 你认为人形机器人公司真正进入二级市场后，投资人最该盯的指标是订单金额、部署小时数、单机毛利，还是数据闭环能力？

---

## 关键词索引

**公司：** Agility Robotics / Churchill Capital Corp XI / NVIDIA / Amazon / Toyota / SoftBank Vision Fund 2 / Foxconn / Schaeffler / GXO / Mercado Libre / Amazon FAR / Toyota Research Institute
**技术：** Physical AI / 人形机器人 / SPAC / PIPE / 具身智能融资 / 机器人上市 / 开放数据栈 / 真实评测日志 / 离线验证 / 容器化机器人系统 / VLA / MPC
**产品：** Digit v5 / Isaac GR00T / Jetson Thor / ABC-130K / TurboMPC / REPAIR-Bench / Critical Interval MSE / CSAR

---

## 值得分享

1. Agility 拟以 25 亿美元估值 SPAC 上市，Digit v5 已披露超过 3 亿美元多年订单。
2. 具身智能正在被上市公司重塑：NVIDIA 押平台，Amazon 押数据与场景，Toyota 押制造部署和控制工具。
3. 资本市场要看的不只是机器人会动，还包括失败恢复数据、真实评测日志和可复制部署架构。
