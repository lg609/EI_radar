# 具身智能情报前沿20260313

**作者：具身视界**
**日期：2026-03-13**

## 核心摘要
- **[公司情报最重磅] Rhoda AI 携 4.5 亿美元巨额融资走出隐身模式，主攻从海量视频中提取策略来直接训练机器人（Video-to-Action）。此次融资额度在初创期公司中极其罕见，标志着大资本对跨形态、无监督视觉动作学习在通用机器人控制上的极高期待。他们试图跳过昂贵的真实世界遥操作数据采集阶段，通过直接理解人类视频来赋予机器人常识与动作直觉。**
- **[新闻最重磅] Rivian 拆分的 Mind Robotics 斩获 5 亿美元 A 轮融资。作为从领先造车新势力中剥离出的初创团队，Mind Robotics 带着雄厚的资金和成熟的自动驾驶 AI 技术积累入局，致力于开发工业级、由 AI 驱动的新一代通用工业机器人。这一事件再次印证了“自动驾驶技术降维打击工业机器人”的行业大趋势，资金加速向能真正落地于工业制造场景的智能体集中。**
- **[论文最重磅] 清华与北大联合开源基础模型 $\Psi_0$ (Psi-Zero)。针对当前人形机器人多模态数据稀缺且异构的痛点，研究团队提出了一种解耦的阶段性训练范式：首先在大规模第一人称的人类视频数据上预训练一个强大的视觉-语言-动作 (VLM) 主干模型以获取通用表征，然后再利用高质量的机器人领域数据微调流匹配 (Flow-based) 动作专家。该方法仅需极少的真实机器人数据，便在多项全身灵巧操作任务上将成功率提升了惊人的 40%。**
- **[GitHub最重磅] Learn-It-All-Full-Stack-EmbodiedAI-Quadruped-Robot。这是一个全栈式的具身智能四足机器人开源项目，完整覆盖了从机械设计、硬件搭建、运动学计算到强化学习训练的全流程闭环。对于研究人员、教育工作者和 DIY 爱好者来说，这提供了一个极为罕见的“从零到一”的参考架构，直观展示了物理硬件如何与 AI 驱动控制融合以涌现出具身智能。**

## 行业新闻
### [Rivian spin-out Mind Robotics raises $500M for industrial AI-powered robots](https://techcrunch.com/2026/03/11/rivian-mind-robotics-series-a-500m-fund-raise-industrial-ai-powered-robots/)
- 来源：TechCrunch
- 日期：2026-03-11
- 摘要：由电动汽车制造商 Rivian 拆分出来的初创公司 Mind Robotics 在 A 轮融资中筹集了高达 5 亿美元的巨额资金。该团队计划利用其在自动驾驶领域积累的视觉和决策 AI 优势，开发能够适应复杂工厂环境的工业级智能机器人。这标志着车企的 AI 能力正在大规模向重工业制造和柔性生产线外溢，资本正在加速押注能切实解决劳动力短缺的“AI+制造”方向。
- 核心价值：由车企剥离孵化并获得巨额 A 轮融资，说明自动驾驶领域的 AI 积累和资金正在加速溢出至重工业制造机器人领域。

### [Canopii looks to succeed where past indoor farms have not](https://techcrunch.com/2026/03/11/canopii-looks-to-succeed-where-past-indoor-farms-have-not/)
- 来源：TechCrunch
- 日期：2026-03-11
- 摘要：Canopii 公司探索通过自动化和智能系统革新室内农业。
- 核心价值：体现了机器人技术在农业垂直场景中的商业探索。

## 前沿论文
### [$\Psi_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](http://arxiv.org/abs/2603.12263v1)
- 来源：arXiv
- 日期：2026-03-12
- 摘要：我们引入了 $\Psi_0$ (Psi-Zero)，这是一个旨在解决具有挑战性的人形机器人全身运动和操作任务的开放基础模型。研究提出了解耦学习范式：首先在海量第一人称人类视频上自回归预训练 VLM 主干以获取视觉动作先验，随后在高质量机器人数据上后训练基于流（flow-based）的动作专家以实现精确的关节控制。实验表明，相较于直接在异构数据上混合训练，这种“先人类第一视角、后机器人领域微调”的方法极为高效，仅用基线 1/10 的数据量，就在多个任务的整体成功率上取得了超过 40% 的提升，突破了从人类演示向机器人跨形态迁移的瓶颈。整个生态系统（包括数据处理、基础模型和实时推理引擎）即将开源。
- 核心价值：仅用少量的机器人数据即可在多项任务上提升 40% 成功率，证明了“高质量人类第一视角数据 + 特定领域真实机器人数据微调”的高效性。

### [OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](http://arxiv.org/abs/2603.12265v1)
- 来源：arXiv
- 日期：2026-03-12
- 摘要：现有的视觉基础模型大多功能单一。OmniStream 提出一种统一的视觉流处理主干，引入因果时空注意力和 3D-RoPE，支持逐帧在线处理。
- 核心价值：向“通用视觉理解”迈出了关键一步，无需针对特定任务微调即可胜任机器人控制。

### [HumDex: Humanoid Dexterous Manipulation Made Easy](http://arxiv.org/abs/2603.12260v1)
- 来源：arXiv
- 日期：2026-03-12
- 摘要：提出了一种基于 IMU 的便携式全身动捕系统 HumDex，结合手部动作重定向与两阶段模仿学习框架，降低全身数据采集难度。
- 核心价值：极大降低了真实环境下全身人形机器人多模态数据采集成本和部署门槛。

## 开源生态 (GitHub)
### [12311112/Learn-It-All-Full-Stack-EmbodiedAI-Quadruped-Robot](https://github.com/12311112/Learn-It-All-Full-Stack-EmbodiedAI-Quadruped-Robot)
- 来源：GitHub
- 日期：2026-03-13
- 摘要：这是一个令人瞩目的开源项目，完整展示了开发一只由具身智能驱动的四足机器人的全生命周期。项目不仅开源了底层算法，还包含了机械结构设计图纸、硬件组装指南、底层电机驱动与运动学算法，最终串联到高层的强化学习（RL）训练与 Sim2Real 部署流程。对于想要系统学习或复现最新具身四足控制框架的研究人员与工程师而言，这是一个绝佳的全栈式脚手架，打破了以往“算法与硬件分离”的开源孤岛现象。
- 核心价值：提供了一个极佳的端到端具身智能学习和研发参考基准。

### [webthree549-bot/agent-ros-bridge](https://github.com/webthree549-bot/agent-ros-bridge)
- 来源：GitHub
- 日期：2026-03-13
- 摘要：一个通用的 ROS1/ROS2 桥接器，专为 AI 智能体控制机器人系统设计。
- 核心价值：降低了上层大模型 AI 智能体接入底层 ROS 硬件的开发门槛。

## 机器人公司情报
### [Rhoda AI exits stealth with $450M to train robots from video](https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/)
- 来源：The Robot Report
- 日期：2026-03-12
- 摘要：初创公司 Rhoda AI 终于撕下神秘面纱，宣布以惊人的 4.5 亿美元融资额正式亮相。在当前高昂的机器人真实遥操作数据成本下，Rhoda AI 另辟蹊径，致力于构建从互联网海量视频中提取物理世界运行规律和操作策略的基础模型。这笔巨额资金将主要用于购买庞大的算力集群以及支付互联网视频的数据授权费用。此举标志着业界对 Video-to-Action 这一极具挑战性但上限极高的技术路线投下了重注，试图通过规模化定律（Scaling Law）在机器人领域复现 LLM 的成功。
- 核心价值：大规模的资金注入标志着资本对“跨形态无监督学习”在机器人领域商业化的高度看好。

## 值得跟进
- [行动项 1：深入跟踪 Rhoda AI 的后续商业化路径及技术论文发布情况，评估其“Video-to-Action”的具体实现架构。]
- [行动项 2：关注 $\Psi_0$ (Psi-Zero) 论文的官方开源进度，并评估其第一视角视频预训练部分对其他灵巧手操作的迁移效果。]
- [行动项 3：尝试拉取 `agent-ros-bridge` 仓库，验证其与常见 VLA 模型连接时的通信延迟。]