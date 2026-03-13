# 机器人情报日报

## 今日核心摘要
- [行业巨额融资：Rhoda AI 以 4.5 亿美元的巨额融资走出隐身模式，专注于通过视频训练机器人。]
- [行业巨额融资：Rivian 剥离出的创业公司 Mind Robotics 筹集了 5 亿美元，用于开发工业级 AI 驱动机器人。]
- [前沿基础模型开源：清华与北大联合开源基础模型 $\Psi_0$ (Psi-Zero)，面向通用人形机器人，通过视觉-动作预训练和流匹配控制实现强泛化。]

## 行业新闻
### [Rhoda AI exits stealth with $450M to train robots from video]
- 来源：The Robot Report
- 日期：2026-03-12
- 链接：https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/
- 摘要：初创公司 Rhoda AI 宣布走出隐身模式并获得了高达 4.5 亿美元的巨额融资，其核心技术路径在于利用海量视频数据来训练机器人模型。
- 核心价值：视频到机器人动作（Video-to-Action）的策略学习是具身智能极具潜力的方向，如此大规模的资金注入标志着资本对“跨形态无监督学习”在机器人领域商业化的高度看好。

### [Rivian spin-out Mind Robotics raises $500M for industrial AI-powered robots]
- 来源：TechCrunch
- 日期：2026-03-11
- 链接：https://techcrunch.com/2026/03/11/rivian-mind-robotics-series-a-500m-fund-raise-industrial-ai-powered-robots/
- 摘要：由电动汽车制造商 Rivian 拆分出来的初创公司 Mind Robotics 在 A 轮融资中筹集了 5 亿美元，旨在利用 AI 赋能新一代工业机器人。
- 核心价值：由车企剥离孵化并获得巨额 A 轮融资，说明自动驾驶领域的 AI 积累和资金正在加速溢出至重工业制造机器人领域。

## 前沿论文

### [$\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12263v1
- 摘要：针对通用人形机器人的运动与操作难题，提出解耦训练范式 $\Psi_0$（Psi-Zero）。先在大规模第一人称人类视频上预训练 VLM，再利用高质量机器人数据微调流控制（Flow-based）专家模型。
- 核心价值：仅用少量的机器人数据即可在多项任务上提升 40% 成功率，证明了“高质量人类第一视角数据 + 特定领域真实机器人数据微调”的高效性。

### [OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12265v1
- 摘要：现有的视觉基础模型大多功能单一。OmniStream 提出一种统一的视觉流处理主干，引入因果时空注意力和 3D-RoPE，并通过持续的 KV-cache 支持逐帧在线处理。
- 核心价值：向“通用视觉理解”迈出了关键一步，无需针对特定任务微调，冻结主干网络即可在语义、三维重建及机器人控制中取得出色表现。

### [HumDex: Humanoid Dexterous Manipulation Made Easy]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12260v1
- 摘要：提出了一种基于 IMU 的便携式全身动捕系统 HumDex，结合基于学习的手部动作重定向与两阶段模仿学习框架，缩小由于形态差异导致的执行鸿沟。
- 核心价值：极大降低了真实环境下全身人形机器人多模态数据采集成本和部署门槛，且软硬生态完全开源。

## 开源生态 (GitHub)

### [Maheee000/embodied-temporal-reasoning]
- 来源：GitHub
- 日期：2026-03-13
- 链接：https://github.com/Maheee000/embodied-temporal-reasoning
- 摘要：一个专注于通过持续视觉-语言理解增强具身人工智能的新项目，旨在提升动态环境适应能力并实现准确的多步时序推理。
- 核心价值：对于探索动态开放环境中的长时间跨度任务规划具有参考价值。

### [erojasoficial-byte/fly-brain]
- 来源：GitHub
- 日期：2026-03-13
- 链接：https://github.com/erojasoficial-byte/fly-brain
- 摘要：将包含 138,639 个神经元的全脑连接组（FlyWire v783）置入生物力学躯体（基于 MuJoCo）中，完全基于真实连接组实现了多种涌现行为。
- 核心价值：展示了如何将生物大脑连接组直接应用于具身仿真与控制，是类脑计算极度硬核的仿真实现。

## 值得跟进
- [行动项 1：深入跟踪 Rhoda AI 的后续商业化路径及技术论文发布情况，评估其“Video-to-Action”的具体实现架构。]
- [行动项 2：关注 $\Psi_0$ (Psi-Zero) 论文的官方开源进度，并评估其第一视角视频预训练部分对其他灵巧手操作的迁移效果。]