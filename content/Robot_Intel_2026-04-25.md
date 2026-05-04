# 具身智能情报前沿｜Wall-B要在35天内进家，模型开始按部署结果说话

**作者：具身视界** · 2026.04.25

> 今天最值得关注的变化，不是哪家又发了一个更大的具身模型，而是越来越多公司开始直接给出部署时间表、训练闭环和真实场景目标。对行业来说，这意味着具身模型竞争正在从“谁的概念更完整”，转向“谁能更快把模型变成可持续运行的真实能力”。

---

## 💥 今日重磅

### [X Square Robot 发布具身基础模型 Wall-B，并称首批机器人将在 35 天内进入真实家庭](https://en.prnasia.com/releases/global/x-square-robot-unveils-new-embodied-ai-model-says-robots-will-arrive-in-homes-in-35-days-530306.shtml)

**摘要：** 4 月 23 日，X Square Robot 发布面向家庭场景的具身基础模型 `Wall-B`，并同步提出其 `World Unified Model (WUM)` 架构，最硬的一点不是“又有新架构”，而是公司直接宣布首批机器人将在 `35 天` 内进入真实家庭。按照官方说法，`WUM` 从一开始就把视觉、语言、动作和物理预测放进同一网络里联合优化，让力、摩擦、碰撞等物理结果不再是动作之后的附属补丁，而是模型内部原生的一部分。更关键的是，这套模型明确围绕真实家庭的长尾问题设计，包括错放物品、动态遮挡、突发人类活动和环境变化等；公司还在发布现场演示了花艺整理等在视觉遮挡下的实时抓取调整任务。它真正重要的地方在于，行业终于开始把“具身模型”从论文式描述拉回到一个最现实的问题：模型能不能很快进入家庭这种最复杂、最非结构化、也最不容错的场景。如果 35 天内真能交付，这会成为今年具身模型最有传播力的一次公开兑现测试。

- **来源：** PR Newswire APAC
- **核心价值：** 这说明具身模型的竞争焦点开始从“谁先讲清架构”切换到“谁先给出真实部署时间表并敢于兑现”。

---

## 📰 行业新闻

### 1. [NEURA 与 AWS 合作扩展 Neuraverse，具身模型训练开始按“云 + 真机 + 仓储验证”一体化来搭](https://www.businesswire.com/news/home/20260420236297/en/NEURA-Robotics-and-Amazon-Web-Services-Enter-Strategic-Collaboration-to-Accelerate-Physical-AI-at-Scale)

**摘要：** 4 月 21 日，NEURA Robotics 与 AWS 宣布合作，AWS 将作为 `Neuraverse` 的主要云基础设施提供方，承接 Physical AI 训练、实时数据处理和机器人群体的智能共享；`NEURA Gym` 也将接入 `Amazon SageMaker`，把真实传感器数据与高保真仿真结合进同一训练管线。更值得看的是，Amazon 还将探索在部分履约中心部署 NEURA 的机器人系统，让模型直接进入全球最复杂的仓储环境之一做验证。

- **来源：** Business Wire
- **核心价值：** 当具身模型开始绑定云基础设施和真实仓储场景，行业就在从“能训模型”升级到“能持续训练、持续验证、持续部署模型”。

### 2. [Foxglove 推出机器人数据搜索与整理平台，模型落地开始争夺“关键 1% 数据”](https://www.businesswire.com/news/home/20260421818840/en/Foxglove-Launches-Unified-Data-Search-and-Curation-Platform-to-Accelerate-Physical-AI-Development)

**摘要：** 4 月 21 日，Foxglove 发布 `Data Search and Curation` 与 `BYOS` 能力，强调机器人团队真正缺的不是更多数据，而是能否快速找到最关键的那 `1%` 任务事件、异常行为和系统故障样本。它的新能力允许团队直接查询多模态机器人数据，并把关键事件整理成训练集、验证集和可复用分析资产。这条消息看似更偏工具层，但其实直指具身模型迭代的核心瓶颈。

- **来源：** Business Wire
- **核心价值：** 这是一条明确的数据相关报道，说明具身模型迭代正在从“拼数据总量”转向“拼关键数据检索与整理效率”。

### 3. [Proximie 借 NVIDIA 基础模型与 Cosmos-H 推进智能手术室，具身模型开始进入高价值专业场景](https://www.businesswire.com/news/home/20260420010687/en/Global-Healthtech-Proximie-Advances-the-Intelligent-Operating-Room-of-the-Future-With-NVIDIA)

**摘要：** 4 月 21 日，Proximie 宣布与 NVIDIA 在 `Project Rheo` 下合作，利用 `NVIDIA Cosmos`，尤其是 `Cosmos-H` 的手术世界合成数据能力，开发一个能实时监控手术室流程、识别关键里程碑并触发物理动作的视觉语言模型。其目标并不只是做“看懂手术室”的软件，而是进一步连接机器人助手，在手术器械准备、设备取放等环节执行实际动作。

- **来源：** Business Wire
- **核心价值：** 这意味着具身模型不再只盯着通用机器人 demo，而开始瞄准医疗这类高价值、高门槛的专业环境。

---

## 📑 前沿论文

### 1. [PokeVLA：把 2.4M 样本知识预训练塞进轻量 VLA，小模型也开始冲真实部署](https://arxiv.org/abs/2604.20834)

**摘要：** 4 月 22 日提交的 `PokeVLA` 很值得看，因为它给出了一条与“大模型堆参数”不同的路线。作者先用 `2.4M` 样本的多模态数据训练紧凑视觉语言模型 `PokeVLM`，再把空间 grounding、affordance 和 embodied reasoning 等知识注入动作学习，最终在 `LIBERO-Plus` 和真实部署中同时拿到强表现。它释放出的信号是，轻量级具身模型也开始有机会冲击真实机器人落地。

- **作者团队：** Yupeng Zheng 等
- **来源：** arXiv
- **核心价值：** 这说明具身模型不一定只能靠更大参数取胜，更高效的小模型路线也在逼近真实部署门槛。

### 2. [Hi-WM：让人直接在世界模型里纠错，具身模型后训练开始从“真机耗时”转向“模型内复用”](https://arxiv.org/abs/2604.21741)

**摘要：** 4 月 23 日提交的 `Hi-WM` 提出一个很实用的后训练思路：与其每次都在真机上重复失败、重置场景、人工纠错，不如先在世界模型里闭环 rollout，再由人类直接在模型中对失败状态进行短轨迹修正。论文显示，该方法在 3 个真实操作任务上平均比基础策略高 `37.9` 个点，也比世界模型闭环 baseline 高 `19.0` 个点。

- **作者团队：** Zhongyi Zhou 等
- **来源：** arXiv
- **核心价值：** 这说明世界模型正在从“想象器”和“评估器”升级成真正可复用的后训练工作台。

### 3. [LoHo-Manip：给 VLA 加进度记忆与视觉轨迹提示，长程任务终于开始更像“规划问题”而不是“连续碰运气”](https://arxiv.org/abs/2604.21924)

**摘要：** 同样在 4 月 23 日提交的 `Long-Horizon Manipulation via Trace-Conditioned VLA Planning`，试图解决 VLA 在多步长程任务上的脆弱性。作者将任务管理 VLM 与执行 VLA 解耦，让前者持续生成“已完成 + 剩余”的轻量语言记忆与 2D 视觉轨迹提示，再由后者按轨迹做局部闭环执行，并在真实 `Franka` 机器人上验证了更好的鲁棒性和长程成功率。

- **作者团队：** Isabella Liu 等
- **来源：** arXiv
- **核心价值：** 这说明 VLA 正在从“一步一动作”的执行器，逐步变成能处理中间状态、失败延续和局部重规划的长程控制系统。

---

## 💻 开源生态

### 1. [WholeBodyVLA 项目页集中展示全身 VLA 在 AgiBot X2 上的真实任务结果，具身模型开源开始强调“先给演示闭环”](https://wholebodyvla.github.io/)

**摘要：** `WholeBodyVLA` 项目页最近集中展示了其在 `AgiBot X2` 上完成整箱装载、推车、长程双臂协同和复杂日常 loco-manipulation 的结果，覆盖未见物体、重载、地形变化和导航等场景。相比只给 benchmark 数字，这类项目页更像是把具身模型的真实任务闭环先公开摆出来，让社区先看系统到底能不能连续做事。

- **来源：** Project Page
- **核心价值：** 这说明具身模型的“开源呈现方式”也在变化，真实视频闭环和任务串联能力正在成为比单点指标更重要的说服材料。

---

## 🏢 机器人公司情报

### 1. [Fujitsu 与卡耐基梅隆共建 Physical AI 研究中心，Kozuchi Physical OS 开始承接“云到边”的具身模型底座](https://global.fujitsu/en-global/pr/news/2026/04/23-01)

**摘要：** 4 月 23 日，Fujitsu 与 Carnegie Mellon University 宣布成立 `Fujitsu-Carnegie Mellon Physical AI Research Center`，并明确围绕动作生成与学习、空间感知、多人/多机器人协调、人机协作以及仿真与现实融合展开研究。更关键的是，Fujitsu 还点名 `Fujitsu Kozuchi Physical OS`，希望把机器人、传感器、系统与物理空间纳入统一平台，逐步从 `2026 财年` 开始吸收研究成果。

- **来源：** Fujitsu Global
- **核心价值：** 当大厂开始把 Physical AI 做成“云到边”的操作系统平台，具身模型就不再只是研究成果，而是在向企业级基础设施靠拢。

---

## 结尾总结

4 月 25 日这期最值得记住的，不是又多了几篇 VLA 和世界模型论文，而是具身模型已经越来越多地开始直接绑定部署承诺、后训练效率、关键数据平台和企业级基础设施。

如果这条线继续推进，接下来大家评判具身模型时，问的将不再只是“这个模型有多大”，而是“它多久能部署、如何持续学习、失败后怎么纠正、以及能不能在真实场景里稳定变强”。

---

> 💬 如果要判断一个具身模型是否真的成熟，你会更看重哪一项：部署时间表、真实场景成功率、失败纠错效率，还是背后的数据闭环能力？

---

## 关键词索引

**公司：** X Square Robot、NEURA Robotics、AWS、Foxglove、Proximie、NVIDIA、Fujitsu、Carnegie Mellon University  
**技术：** 具身基础模型、VLA、世界模型、后训练、数据整理、Physical AI、云到边部署  
**产品：** Wall-B、WUM、Neuraverse、NEURA Gym、Cosmos-H、PokeVLA、Hi-WM、LoHo-Manip、WholeBodyVLA、Kozuchi Physical OS

---

## 值得分享

1. `Wall-B` 最狠的不是新架构，而是 `35 天内进家庭` 的交付承诺，具身模型终于开始按部署时间表说话。
2. `Foxglove` 提醒了一个关键事实：Physical AI 竞争不只是拼模型，而是拼谁能更快找到真正有价值的那 `1%` 机器人数据。
3. `Hi-WM` 把人类纠错搬进世界模型里，真实任务成功率平均提升 `37.9` 个点，说明后训练效率正在成为具身模型的新胜负手。
