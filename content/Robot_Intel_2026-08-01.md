# 具身智能情报前沿｜数据引擎支撑机器人基础模型

**作者：具身视界** · 2026.08.01

---

> 今天最值得关注的变化，是机器人基础模型竞争正在从“谁的模型更大”转向“谁能持续生产可对齐物理世界的数据”。Google Gemini Robotics 给出了从多模态理解到动作执行的路线参照，而近 7 天新论文集中补上数据引擎、世界模型、执行校验和失败修正这些落地环节。

## 💥 今日重磅

### [ACE-Data-0：150 小时、1700 万帧家庭交互数据，瞄准具身数据瓶颈](https://arxiv.org/abs/2607.28625)

**摘要：** 7 月 30 日提交的 ACE-Data-0 把“具身智能缺数据”拆成了更具体的问题：机器人需要同时理解第一视角感知、全身运动、灵巧操作、物体状态、声音和触觉如何随任务推进共同变化。论文提出 Ambient Capture Engine，把真实家庭环境改造成空间标定、时间同步的多传感记录系统，覆盖桌面尺度的手物操作和房间尺度的全身移动交互。ACE-Data-0 包含 150 小时、1700 万帧视频、200 类任务、50 名参与者、2 个环境和 7.5 万段交互 episode，并提供从信号、场景组件到交互行为的分层基准。它的重要性不在于又多了一个数据集，而在于把 Gemini Robotics 这类机器人基础模型所需的“多模态物理世界经验”变成可采集、可同步、可评测的基础设施。

- **来源：** arXiv
- **核心价值：** 数据相关报道：具身智能的数据竞争正在从单机遥操作素材，升级为多视角、多模态、可对齐动作和接触的家庭级数据引擎。
- **行业判断：** 下一阶段机器人基础模型的差距，很可能先体现在数据生产系统，而不是模型参数规模。

---

## 📰 行业新闻

### 1. [Gemini Robotics 路线参照：Google DeepMind 把 Gemini 推向物理世界](https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/)

**摘要：** Google DeepMind 此前发布 Gemini Robotics，目标是把 Gemini 的多模态理解能力扩展到机器人动作执行。该方向强调三类能力：理解自然语言和视觉环境，迁移到新物体、新任务和新场景，并在物理交互中保持安全约束。虽然这不是 8 月 1 日新发布，但它仍是今天观察具身基础模型的重要背景：近期 ACE-Data-0、World Action Planner、CheckVLA 等工作，实际上都在补齐这条路线从模型到真机部署所需的数据、规划和验证环节。

- **来源：** Google DeepMind
- **核心价值：** 背景参照：Gemini Robotics 把行业问题从“机器人能不能听懂指令”推进到“模型能不能在真实物理世界稳定行动”。

### 2. [Gemini Robotics On-Device：基础模型能力开始进入本地机器人设备](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

**摘要：** Google DeepMind 的 Gemini Robotics On-Device 进一步强调端侧部署：机器人不能总依赖云端闭环，低延迟、隐私、本地可靠性和设备适配会成为实际落地条件。把这条背景放到今天看，近期 CoTinyVLA、TurboVLA 等小模型和实时 VLA 工作，都在解决同一类工程问题：让机器人策略从演示视频走向可持续运行的设备侧系统。

- **来源：** Google DeepMind
- **核心价值：** 背景参照：端侧机器人基础模型会倒逼模型压缩、数据蒸馏、低显存推理和硬件适配能力同步升级。

### 3. [世界机器人大会同期活动：场景数据采集与多模态训练被写入商业化讨论](https://www.worldrobotconference.com/news/3233.html)

**摘要：** 世界机器人大会 7 月 29 日披露的同期活动中，“场景破局—机器人商业化落地的探索与实践”明确提到场景数据采集、运动模型构建、多模态训练迭代和本体整机适配。这个表述与今天的论文趋势一致：具身智能商业化不只是卖一台本体，而是把场景、数据、模型、控制和运维连成闭环。

- **来源：** 世界机器人大会官网
- **核心价值：** 商业化讨论正在从单点 demo 转向全链路能力，数据采集和模型迭代会成为客户判断供应商的重要依据。

---

## 📚 前沿论文

### 1. [World Action Planner：用动作条件世界模型做可泛化决策](https://arxiv.org/abs/2607.27599)

**摘要：** 7 月 30 日提交的 World Action Planner 把 VLM 的推理能力和多任务 pose-image 条件世界模型结合起来，让机器人先提出动作计划，再通过想象中的 world model rollout 进行优化和搜索。论文称该系统在组合任务、新布局和零样本泛化场景中显著优于端到端 VLA 与 WAM。它代表的趋势是：机器人基础模型不只要直接输出动作，还要能预测动作之后世界会怎样变化。

- **作者团队：** Xiangcheng Zhang / Yilun Du
- **来源：** arXiv
- **核心价值：** 世界模型正在成为 VLA 之后的关键补件，尤其适合长程任务、布局变化和跨场景决策。

### 2. [CheckVLA：用动作条件世界模型校验长程移动操作](https://arxiv.org/abs/2607.26789)

**摘要：** 7 月 29 日提交的 CheckVLA 针对 VLA 长程移动操作中的开环 action chunk 问题。它用冻结的动作条件世界模型验证执行过程，并通过风险阈值决定是否介入修正。在 RoboCasa365 上，CheckVLA 平均成功率达到 36.1%，高于周期性重规划的 27.6%；在 5% episode 级误报目标下，动作条件方法的及时召回达到 77.9%。

- **作者团队：** Yushan Liu / Peibo Sun / Xintao Chao / Zhenyang Yang 等
- **来源：** arXiv
- **核心价值：** 真机部署不能只看出发时的策略置信度，执行中校验和低延迟修正会决定长程任务能否稳定完成。

### 3. [RoboBRIDGE：把预训练 VLA 包装成更可靠的机器人智能体](https://arxiv.org/abs/2607.27881)

**摘要：** 7 月 30 日提交的 RoboBRIDGE 提出一个模块化编排框架，在预训练 VLA 外增加 Monitor、Perceptor、Planner、Controller 和 Robot Interface 五个模块。论文认为，VLA 作为动作预测器并不等于完整机器人智能体，因为真实部署还需要失败检测、层级恢复、异步场景更新、重规划和本体接口。该工作已被 IROS 2026 接收。

- **作者团队：** Sihyung Yoon / Minjong Yoo / Sanghyun Ahn / Seojeong Choi 等
- **来源：** arXiv
- **核心价值：** 可靠机器人智能体不会只靠扩大 VLA 得到，还需要围绕模型建立监控、规划、控制和接口层。

### 4. [RedFlow：把失败经验转成 VLA 的动作级修正信号](https://arxiv.org/abs/2607.27782)

**摘要：** 7 月 30 日提交的 RedFlow 面向 flow-matching VLA 部署时的分布偏移和错误累积。它把失败轨迹拆到动作级别，识别导致失败的动作，并从相似上下文中检索成功替代动作作为修正监督。论文报告，在三个真实操作任务中，RedFlow 将真实世界成功率从 56.7% 提升到 74.7%，同时所需训练样本约比多种 on-policy 方法少一个数量级。

- **作者团队：** Zhengyang Yan / Junhao Li / Fangqi Zhu / Zijun Wang 等
- **来源：** arXiv
- **核心价值：** 失败数据不再只是被丢弃的噪声，而可以成为策略迭代中最有价值的纠错资源。

### 5. [CG-World：85 万段世界状态数据服务 world model 与 Physical AI](https://arxiv.org/abs/2607.26452)

**摘要：** 7 月 29 日提交的 CG-World 从工业计算机图形生产管线中构建大规模 world-state 数据集。CG-World v1 包含约 85 万段 1 至 5 秒的时间对齐片段，记录语义、空间结构、骨骼与控制器状态、运动曲线、相机和灯光参数、物理缓存、接触事件及多通道渲染。它还定义事实轨迹、观察干预、动作干预和反事实分支，用于支持干预学习和反事实推理。

- **作者团队：** Yiming Cai / Fangjie Yu / Meiqing Yu / Ziyue Shi 等
- **来源：** arXiv
- **核心价值：** 数据相关报道：世界模型需要的不只是视频，而是带状态、事件、关系和干预分支的结构化物理世界数据。

---

## 💻 开源生态

### 1. [ACE-Data-0 项目页：多模态家庭交互数据引擎开放展示](https://ace-data-engine.github.io/ACE-Data-0/)

**摘要：** ACE-Data-0 项目页展示了 Ambient Capture Engine 的采集配置、数据构成和任务覆盖。对开发者来说，项目页的价值在于把“家庭任务数据”从视频素材变成可拆解的工程对象：相机视角、身体动作、手部动作、物体 6-DoF 轨迹、触觉和声音需要同步到同一条时间线上。

- **来源：** 项目主页
- **核心价值：** 数据采集系统的可复现程度，会直接影响后续 imitation learning、world model 和 VLA 训练的质量。

### 2. [World Action Planner 项目页：动作条件世界模型规划流程可查看](https://worldactionplanner.github.io)

**摘要：** World Action Planner 项目页开放了方法介绍和示例，展示机器人如何基于语言与视觉提出计划，并借助世界模型预测动作后果。它适合关注 VLA 后续路线的团队跟进：当任务变长、场景变新，单步动作预测很难覆盖全部不确定性，基于想象 rollout 的搜索会更有工程意义。

- **来源：** 项目主页
- **核心价值：** 开源项目页让世界模型规划从论文概念变成可跟踪的实现路线。

### 3. [CoTinyVLA：0.9B 参数小型 VLA 仓库开放](https://github.com/BrainJellyPie/CoTinyVLA)

**摘要：** 7 月 28 日提交的 CoTinyVLA 论文关联 GitHub 仓库可访问。该工作用 0.9B 参数 Qwen3.5-0.8B backbone，通过双视角时序输入、35B 教师模型的层级思维链蒸馏，以及指令改写增强，在 LIBERO-Plus 多类扰动任务上超过更大的 7B 基线。论文还报告闭环推理峰值显存约 2.25GiB。

- **来源：** GitHub / arXiv
- **核心价值：** Gemini Robotics On-Device 代表端侧方向，小型 VLA 的开源实现则给开发者提供了可落地的工程参照。

---

## 🏢 机器人公司情报

### 1. [Google DeepMind：Gemini Robotics 是机器人基础模型竞赛的关键参照系](https://arxiv.org/abs/2503.20020)

**摘要：** Gemini Robotics 论文与官方发布共同说明，Google DeepMind 正在把 Gemini 的视觉、语言和推理能力扩展到低层动作控制。对国内外机器人公司而言，Gemini Robotics 的意义不只是一个模型名称，而是重新定义了竞争坐标：本体厂、数据平台、模型团队和端侧算力供应商都要回答同一个问题，即如何把通用多模态能力稳定接到真实执行链路。

- **来源：** arXiv / Google DeepMind
- **核心价值：** 背景参照：Gemini Robotics 抬高了机器人基础模型的评价标准，单纯会对话已经不够，必须能理解环境、生成动作并处理物理反馈。

### 2. [Google DeepMind：Gemini Robotics 1.5 强调具身智能体能力](https://arxiv.org/abs/2510.03342)

**摘要：** Gemini Robotics 1.5 进一步把话题推向具身智能体：机器人不仅要根据指令执行动作，还要能在复杂任务中分解目标、理解环境变化并跨场景泛化。放在今天的情报池里看，World Action Planner、CheckVLA、RoboBRIDGE 和 RedFlow 都是在解决同一组部署难题：计划如何生成，执行如何监控，失败如何修复，数据如何回流。

- **来源：** arXiv
- **核心价值：** 背景参照：具身智能体竞争的焦点会落到计划、验证、恢复和数据闭环，而不是只比较一次性动作生成。

### 3. [北京人形机器人创新中心：具身智能应用活动将发布方案并签约](https://www.worldrobotconference.com/news/3233.html)

**摘要：** 世界机器人大会预告显示，北京人形机器人创新中心主办的“具身觉醒·智定未来”应用创新主题活动，将围绕具身智能从技术突破到产业应用、敏捷运动与多感知操作、灯塔工厂选型逻辑等议题展开，并计划发布具身智能“最强大小脑”、Omni、搬运分拣解决方案和计量检测方案。

- **来源：** 世界机器人大会官网
- **核心价值：** 国内产业侧也在把本体、大小脑、场景方案和客户签约放到同一张桌上，基础模型路线最终要接受应用场景检验。

---

## 结尾总结

8 月 1 日的主线可以概括为：Gemini Robotics 提供了机器人基础模型的方向感，但真正决定落地速度的，是数据引擎、世界模型、执行校验、失败修正和端侧部署这些工程环节。ACE-Data-0、CG-World、World Action Planner、CheckVLA、RoboBRIDGE 和 RedFlow 的共同信号是，具身智能正在从“模型能输出动作”走向“系统能持续理解、预测、验证和修正物理世界”。

---

> 💬 你认为机器人基础模型接下来最稀缺的能力是什么：高质量数据、端侧算力、世界模型、失败恢复，还是可量产的本体平台？

---

## 关键词索引

**公司 / 机构：** Google DeepMind / 世界机器人大会 / 北京人形机器人创新中心

**项目 / 论文：** Gemini Robotics / Gemini Robotics On-Device / Gemini Robotics 1.5 / ACE-Data-0 / World Action Planner / CheckVLA / RoboBRIDGE / RedFlow / CG-World / CoTinyVLA

**技术：** 具身智能 / 机器人基础模型 / VLA / 世界模型 / 动作条件世界模型 / 数据引擎 / 多模态数据采集 / 家庭交互数据 / 失败恢复 / 执行校验 / 端侧部署 / 小型 VLA / 物理世界数据

---

## 值得分享

1. Gemini Robotics 给出了机器人基础模型的方向，但近期论文显示，真正的落地瓶颈在数据、规划、验证和失败修正。
2. ACE-Data-0 用 150 小时、1700 万帧、7.5 万段交互，把家庭具身数据采集做成了多模态数据引擎。
3. 机器人基础模型下一步不只是输出动作，而是要能预测动作后果、发现执行偏差，并把失败经验转成可学习的数据。
