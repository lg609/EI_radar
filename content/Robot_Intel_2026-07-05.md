# 具身智能情报前沿｜灵巧手开始补齐真实接触几何

**作者：具身视界** · 2026.07.05

> 今天最值得关注的变化，是灵巧手研究正在从“生成好看的抓取姿态”走向“建模真实手物接触、适配不同手型，并接入可训练工程栈”。EPIC-Contact、DCGrasp、GraspXL、unitree_lerobot 等信号显示，灵巧手的竞争点正在从硬件自由度扩展到接触几何、数据规模和训练接口。

---

## 💥 今日重磅

### [EPIC-Contact：2.3K 第一视角片段补齐真实手物接触几何](https://arxiv.org/abs/2606.30598v1)

**摘要：** 6 月 29 日发布的 Towards in-the-wild Egocentric 3D Hand-Object Pose Estimation 直指灵巧手学习里的一个基础短板：真实世界第一视角下，手和物体经常互相遮挡，接触关系模糊，模型即使能估计手姿态，也未必理解“哪里真正接触、如何稳定抓握”。论文提出 EPIC-Contact 数据集，包含 2.3K 个野外第一视角片段、62.3K 帧，并提供稠密、双向的 3D 手物接触对应关系和姿态网格；同时提出 HOPformer，在一次前向推理中联合预测双手与物体姿态。结果显示，HOPformer 在 ARCTIC 上达到 82.4% 成功率，比当前 SOTA 高 6.2 个百分点；在 EPIC-Contact 上几乎将成功率翻倍，并将接触偏差降低 75%。这说明灵巧手要进入真实场景，不能只靠合成抓取或单帧手势，必须把第一视角、人手-物体接触几何和可迁移姿态估计放进同一数据闭环。

- **来源：** arXiv
- **核心价值：** 灵巧手的数据底座正在从“手型轨迹”升级为“真实手物接触几何”，这会直接影响抓取、重定向和多指控制的上限。

---

## 📰 行业新闻

### 1. [Unitree LeRobot 仓库吸引 700+ 星：G1 双臂灵巧手训练栈进入开源视野](https://github.com/unitreerobotics/unitree_lerobot)

**摘要：** GitHub API 显示，unitreerobotics/unitree_lerobot 7 月 4 日前后仍有更新记录，星标约 708。仓库描述明确指出，它基于 LeRobot 开源训练框架改造，用于训练和测试 Unitree G1 机器人双臂灵巧手采集的数据。相比单独发布本体或数据集，这类仓库更接近工程入口：它把硬件、本体数据和模仿学习训练流程连接起来。

- **来源：** GitHub
- **核心价值：** 灵巧手生态的下一步不是单点论文，而是把数据采集、训练和测试流程做成可复用开源栈。

### 2. [GraspXL 更新数据入口：50 万+ 物体抓取动作覆盖多种灵巧手](https://eth-ait.github.io/graspxl/)

**摘要：** GraspXL 项目页可访问，GitHub API 显示仓库星标约 256，7 月 4 日仍有更新记录。README 信息显示，GraspXL 已提供数据集入口，并包含 50 万+ 物体的抓取动作序列，覆盖 MANO、Allegro、Shadow 等手型。对灵巧手研究者来说，这类大规模跨手型抓取数据是训练手型适配和接触先验的重要来源。

- **来源：** 项目页 / GitHub
- **核心价值：** 灵巧手泛化需要跨物体、跨手型的大规模抓取数据，而不是只在单一机械手上调参。

### 3. [UniDex 仓库持续被关注：从第一视角人类视频走向通用灵巧手控制](https://github.com/unidex-ai/UniDex)

**摘要：** GitHub API 显示，unidex-ai/UniDex 星标约 157，仓库描述为 CVPR 2026 工作：Universal Dexterous Hand Control from Egocentric Human Videos。它与 EPIC-Contact、H-Tac/TTP、DexUMI 等路线共同说明，人类第一视角视频正在成为灵巧手控制的重要数据来源，尤其适合覆盖真实世界长尾手物交互。

- **来源：** GitHub
- **核心价值：** 第一视角人类视频正在从“辅助观察”变成灵巧手策略学习的核心数据资产。

---

## 📑 前沿论文

### 1. [DCGrasp：用距离剖面生成可控、跨手型抓取](https://arxiv.org/abs/2606.29924v1)

**摘要：** DCGrasp 面向 3D 手物交互生成，提出 Distance Profile：从每个手部顶点到最近物体点的有符号距离，并用距离感知权重捕捉近接触区域的语义相似交互。方法先用 Diffusion Transformer 生成 Distance Profile 和候选手姿态，再通过优化保证手姿态与近接触几何一致。实验显示，该方法能生成高质量、物理合理、可由用户控制的抓取，并泛化到不同物体和手型尺度。

- **作者团队：** Hiroyasu Akada、Jesús Pérez、Emre Aksan、Vasileios Choutas、Cristian Romero、Alberto Garcia-Garcia、Vladislav Golyanik、Christian Theobalt、Thabo Beeler
- **来源：** arXiv
- **核心价值：** 灵巧手控制需要从“输出关节角”上升到“显式约束近接触几何”，这会提升跨手型迁移能力。

### 2. [Graspability Field：把推、拨、滚变成通向抓取的前置动作](https://arxiv.org/abs/2606.30474v1)

**摘要：** Grasp-Oriented Non-Prehensile Manipulation 关注抓取前的非抓取操作。现实里物体不一定一开始就处在可抓状态，机器人需要先推动、旋转或重新摆放物体。论文不要求预设目标姿态，而是从合成抓取中构建可抓集合，学习 graspability field，用连续可抓性信号指导强化学习策略。仿真和真实机器人实验显示，该策略能闭环把物体调整到可抓状态，并无需外部规划器或人工停止条件。

- **作者团队：** Licheng Zhong、Gim Hee Lee
- **来源：** arXiv
- **核心价值：** 灵巧手落地不只是最后一抓，还包括抓取前如何把物体变成“可被抓”。

### 3. [TacEvo：用 LLM 自动搜索触觉感知网络结构](https://arxiv.org/abs/2606.30109v1)

**摘要：** TacEvo 面向视觉触觉传感器的模型设计问题。触觉图像高度依赖传感器和物理结构，传统网络结构往往靠专家反复试。TacEvo 用 LLM 生成代码级结构变异和交叉，再用 MAP-Elites 质量多样性搜索保留不同结构的优秀候选。在 ViTacTip 力回归和 grating 分类任务上，TacEvo 的可训练结构生成可靠性达到 96.0%/94.5%，20 代搜索后验证适应度提升 56.1%/96.1%。

- **作者团队：** Mohammed AbuSadeh、Lan Wei、Dandan Zhang
- **来源：** arXiv
- **核心价值：** 触觉模型设计正在从专家手工调结构，转向自动搜索与下游反馈闭环。

### 4. [JointHOI：接触图成为手物交互生成的内部约束](https://arxiv.org/abs/2607.01768v1)

**摘要：** JointHOI 用单阶段扩散框架同时生成 3D 手物运动和动态距离接触图，把接触图作为辅助内部模态。它解决的问题很具体：手和物体的动作看起来自然，但一点点接触误差就会导致悬浮和穿模。GRAB 和 ARCTIC 实验显示，接触引导采样能提升文本一致性和物理可信度。对灵巧手而言，这意味着接触图不只是评估标签，也可以成为动作生成时的约束。

- **作者团队：** Mingyeong Song、Jungbin Cho、Jisoo Kim、Ananya Bal、Kartik Sharma、Youngjae Yu、Laszlo A. Jeni、Junhyug Noh
- **来源：** arXiv
- **核心价值：** 如果手物交互生成要服务机器人训练，接触一致性必须成为模型内部变量。

### 5. [CoDex：16 自由度多指手零示范完成喷瓶、胶枪等功能操作](https://arxiv.org/abs/2606.31909v1)

**摘要：** CoDex 研究组合式灵巧功能物体操作，例如对植物使用喷瓶、在木板上使用热熔胶枪。方法用 VLM 推断任务和场景约束，再通过解析约束优化生成少量功能抓取候选，最后用强化学习细化抓取-移动-触发策略。实验在 7 自由度机械臂和 16 自由度多指手上完成 6 类任务，覆盖喷瓶、热熔胶枪、气吹、手电筒、胡椒研磨器等未见物体。

- **作者团队：** Bowen Jiang、William Painter Reger、Roberto Martin-Martin
- **来源：** arXiv
- **核心价值：** 灵巧手真正的价值不在于“握住”，而在于理解物体功能并触发内部机构。

### 6. [RoboTacDex：Unitree G1 灵巧手数据继续提供工程底座](https://arxiv.org/abs/2606.31836v1)

**摘要：** RoboTacDex 基于公开可获得的 Unitree G1 采集，包含 6000 条轨迹、19 个任务、23 种技能和 22 个物体，记录多视角 RGB、深度、触觉反馈和细粒度语义标注。它的重要性在今天仍然成立：灵巧手算法需要真实本体、多模态同步和任务语义共同支撑，而不是只在仿真中生成单手抓取姿态。

- **作者团队：** Xinyi Wang、Donghan Li、Zi'Ang Chen、Chong Yu、Chen Xin、Peng Ye、Yingkai Sun、Tao Chen
- **来源：** arXiv
- **核心价值：** 数据相关报道：真实灵巧手轨迹、触觉和语义标注正在成为训练通用操作策略的底层资产。

---

## 💻 开源生态

### 1. [unitree_lerobot：LeRobot 接入 Unitree G1 双臂灵巧手数据](https://github.com/unitreerobotics/unitree_lerobot)

**摘要：** unitree_lerobot 的核心价值在于把 LeRobot 训练框架和 Unitree G1 双臂灵巧手数据连接起来。GitHub API 显示该仓库星标约 708，说明社区对“可买到的本体 + 开源训练框架 + 灵巧手数据”的组合有明确需求。

- **来源：** GitHub
- **核心价值：** 灵巧手开源生态会优先围绕可复现实机和成熟训练框架形成聚集。

### 2. [GraspXL：50 万+ 物体、多手型抓取动作数据可作为预训练资源](https://eth-ait.github.io/graspxl/)

**摘要：** GraspXL 项目页和 README 显示，其数据集覆盖 50 万+ 物体的抓取动作序列，并支持 MANO、Allegro、Shadow 等手型。它还提供 30 个样例物体和可视化工具，适合研究不同灵巧手之间的动作迁移、抓取先验和大规模合成数据预训练。

- **来源：** 项目页 / GitHub
- **核心价值：** 跨手型大规模数据会成为灵巧手算法从单一硬件走向通用控制的重要桥梁。

### 3. [NVIDIA Isaac GR00T 星标约 7498：基础模型平台等待灵巧手接口标准化](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** GitHub API 显示，NVIDIA/Isaac-GR00T 7 月 5 日星标约 7498。近期灵巧手相关工作正在把接触几何、触觉预测、多指动作和真实本体数据推到前台。对 GR00T 这类平台而言，后续关键不只是支持人形全身控制，还要在数据格式、动作空间和传感器接口上接住多指手。

- **来源：** GitHub
- **核心价值：** 机器人基础模型平台要进入真实操作，必须把灵巧手作为一级接口，而不是末端执行器附属件。

---

## 🏢 机器人公司情报

### 1. [Unitree：G1 正在从本体产品变成灵巧手数据与训练生态入口](https://github.com/unitreerobotics/unitree_lerobot)

**摘要：** Unitree G1 已在 RoboTacDex 数据集和 unitree_lerobot 开源训练栈中反复出现。对整机厂来说，这类生态曝光比单次演示更重要：研究者一旦围绕同一本体采数据、训练策略和复现实验，硬件就会形成默认平台效应。

- **来源：** GitHub / arXiv
- **核心价值：** 人形机器人公司的长期壁垒，会部分来自它是否成为灵巧手数据和算法复现的公共底座。

### 2. [Allegro / Shadow 等灵巧手模型继续出现在大规模抓取数据中](https://eth-ait.github.io/graspxl/)

**摘要：** GraspXL 覆盖 MANO、Allegro、Shadow 等手型，并面向 50 万+ 物体生成抓取动作。这说明灵巧手硬件生态正在被数据集和仿真工具重新组织：哪些手型被纳入大规模数据和基准，哪些手型就更容易被算法社区优先适配。

- **来源：** 项目页
- **核心价值：** 灵巧手硬件竞争不只看机械性能，也看能否进入主流数据集、仿真环境和控制基准。

### 3. [触觉传感器生态：TacEvo 指向自动化模型适配需求](https://arxiv.org/abs/2606.30109v1)

**摘要：** TacEvo 的意义不在于替代触觉硬件，而在于降低不同触觉传感器适配模型的成本。随着视觉触觉、柔性触觉、指尖触觉和多指手结合，传感器厂商需要提供的不只是硬件读数，还包括可训练模型、评测任务和下游策略接口。

- **来源：** arXiv
- **核心价值：** 触觉传感器的商业价值会越来越依赖软件栈，而不是单点硬件参数。

---

## 结尾总结

今天的主线是，灵巧手正在补齐“真实接触几何 + 大规模跨手型数据 + 可复现实机训练栈”。EPIC-Contact 把野外第一视角手物接触做成数据集，DCGrasp 和 JointHOI 把接触约束放进生成过程，GraspXL 提供跨手型大规模抓取动作，unitree_lerobot 则把 Unitree G1 双臂灵巧手数据接入 LeRobot。下一阶段，真正有竞争力的灵巧手系统，要同时回答三个问题：接触数据从哪里来、不同手型如何迁移、训练栈能否被社区复现。

---

> 💬 你认为灵巧手最先标准化的会是哪一层：手物接触数据格式、跨手型动作表示、触觉传感器接口，还是 LeRobot / GR00T 这类训练平台适配？

---

## 关键词索引

**公司 / 机构：** Unitree / NVIDIA / Stanford / ETH AI Center / Max Planck Institute / Allegro Hand / Shadow Hand
**技术：** 灵巧手 / 手物接触几何 / 第一视角视频 / 3D hand-object pose / 接触图 / 多指手 / 触觉感知 / 抓取生成 / 非抓取操作 / LeRobot / VLA / 世界模型
**项目 / 数据：** EPIC-Contact / HOPformer / DCGrasp / Graspability Field / TacEvo / JointHOI / CoDex / RoboTacDex / GraspXL / unitree_lerobot / UniDex / Isaac GR00T

---

## 值得分享

1. 灵巧手数据正在从手势轨迹升级为真实接触几何：EPIC-Contact 包含 2.3K 第一视角片段和 62.3K 帧稠密 3D 手物接触标注。
2. 跨手型数据开始成为关键资产：GraspXL 覆盖 50 万+ 物体，并支持 MANO、Allegro、Shadow 等多种手型。
3. 灵巧手生态正在工程化：unitree_lerobot 把 LeRobot 训练框架接入 Unitree G1 双臂灵巧手数据，说明开源训练栈会影响硬件平台扩散。
