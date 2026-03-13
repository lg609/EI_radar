# 机器人情报日报

## 今日核心摘要
- [清华与北大联合开源基础模型 $\Psi_0$ (Psi-Zero)：面向通用人形机器人，通过视觉-动作预训练和流匹配控制实现强泛化，大幅击败基线。]
- [OmniStream：一种统一的流式视觉主干网络，通过因果时空注意力和3D-RoPE实现对连续视觉流的实时感知与机器人操作。]
- [具身果蝇开源项目 (fly-brain)：将真实的果蝇脑网络(约13.8万神经元)引入 MuJoCo 具身化环境中，实现纯生物连接组的机器人仿真。]

## 行业新闻
今日主流媒体无符合条件的高价值具身智能与机器人核心新闻，暂无更新。

## 前沿论文

### [$\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12263v1
- 摘要：针对通用人形机器人的运动与操作难题，提出解耦训练范式 $\Psi_0$（Psi-Zero）。先在大规模第一人称人类视频上预训练 VLM，再利用高质量机器人数据微调流控制（Flow-based）专家模型。
- 核心价值：仅用少量的机器人数据即可在多项任务上提升 40% 成功率，证明了“高质量人类第一视角数据 + 特定领域真实机器人数据微调”的高效性。代码与模型生态即将开源。

### [OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12265v1
- 摘要：现有的视觉基础模型大多功能单一（仅限语义、时序或几何）。OmniStream 提出一种统一的视觉流处理主干，引入因果时空注意力和 3D-RoPE，并通过持续的 KV-cache 支持逐帧在线处理。
- 核心价值：向“通用视觉理解”迈出了关键一步，无需针对特定任务微调，冻结主干网络即可在语义、三维重建及机器人控制（未知训练任务）中取得出色表现。

### [HumDex: Humanoid Dexterous Manipulation Made Easy]
- 来源：arXiv
- 日期：2026-03-12
- 链接：http://arxiv.org/abs/2603.12260v1
- 摘要：针对人形机器人全身灵巧操作的高质量示教数据收集瓶颈，提出了一种基于 IMU 的便携式全身动捕系统 HumDex。结合基于学习的手部动作重定向与两阶段模仿学习框架，显著缩小了由于形态差异导致的执行鸿沟。
- 核心价值：极大降低了真实环境下全身人形机器人多模态数据采集成本和部署门槛，且该系统已完全开源（软硬件复现指引齐备）。

## 开源生态 (GitHub)

### [erojasoficial-byte/fly-brain]
- 来源：GitHub
- 日期：2026-03-13
- 链接：https://github.com/erojasoficial-byte/fly-brain
- 摘要：具身果蝇项目（Embodied Drosophila）。将包含 138,639 个神经元的全脑连接组（FlyWire v783）置入生物力学躯体（NeuroMechFly v2 / MuJoCo）中，完全基于真实连接组实现了视觉、嗅觉、味觉、飞行及涌现行为。
- 核心价值：展示了如何将生物大脑连接组（Connectome）直接应用于具身仿真与控制，是类脑计算与具身智能结合的前沿工程实践。

### [hamoudi123-9/dreamdojo-aegis-sdk]
- 来源：GitHub
- 日期：2026-03-13
- 链接：https://github.com/hamoudi123-9/dreamdojo-aegis-sdk
- 摘要：正在建设中的安全防御系统 SDK，通过实时验证输入和动作来保护具身人工智能系统，防止机器人在物理应用中进入不安全状态。
- 核心价值：为开发者提供具身系统安全护栏的早期实现思路。

## 值得跟进
- [关注 $\Psi_0$ (Psi-Zero) 论文的官方开源进度，评估其全生态流水线（包含实时动作推理引擎）对实验室机器人的适配成本。]
- [研究 HumDex 开源仓库中的两阶段模仿学习方案，测试基于 IMU 获取人体全身数据的质量及微调性能。]