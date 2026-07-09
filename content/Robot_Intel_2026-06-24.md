# 具身智能情报前沿｜VLA 正在补上安全、记忆与世界模型短板

**作者：具身视界** · 2026.06.24

> 今天最值得关注的变化，是 VLA 和世界模型路线正在从“能不能按语言做动作”进入“能不能安全、长期、可持续部署”的阶段。6 月 22 日 arXiv 集中出现一批新工作：LIBERO-Safety 用 19,664 条严格无碰撞示范测试 VLA 的物理与语义安全；KEMO 给长程操作 VLA 加事件记忆；LaST-HD 用世界模型把人手数据和机器人轨迹对齐；1X World Model Lab 则把大规模世界模型预训练提升为公司战略。VLA 的下一场竞争，不只是端到端控制，而是安全、记忆、数据闭环和物理推理。

---

## 今日重磅

### [LIBERO-Safety 发布：19,664 条无碰撞示范，系统评测 VLA 的物理安全与语义安全](https://arxiv.org/abs/2606.23686)

**摘要：** 6 月 22 日，`LIBERO-Safety` 发布，目标是补上 VLA 部署中长期被低估的安全评测缺口。论文指出，尽管 Vision-Language-Action 模型已经展现出强操作能力，但它们在严格约束下的运行安全仍缺少系统验证。为此，团队构建了参数化安全 benchmark，可程序化生成带有随机性的安全关键场景，并通过 keypose-driven data generation pipeline 扩展数据生成能力，最终整理出 19,664 条严格 collision-free 的示范数据，覆盖大量 domain randomization。研究进一步评测 8 个 VLA 模型和 2 个具身基础模型，发现当前模型面临明显的“泛化—安全张力”：高多样性训练能让轨迹更安全，但任务成功率仍受限于次优轨迹合成和语义错配。项目页还总结了两类典型失败：一是 collision-free incompletion，即动作没有碰撞但陷入运动学死锁或时间溢出；二是 semantic misalignment，即机器人安全地抓住了错误物体。这个结果对真实部署非常关键，因为家庭、医疗和工业场景中，“没撞到人”只是底线，“按正确语义做正确事”才是真正的安全。

- **来源：** arXiv / LIBERO-Safety 项目页
- **核心价值：** VLA 的竞争正在从“任务成功率”转向“成功率 + 物理安全 + 语义安全”的三重约束。对准备落地家庭机器人、康养机器人和工业人形机器人的公司来说，安全评测基准将成为模型上线前的必选项。

---

## 行业新闻

### 1. [1X 成立 World Model Lab：把世界模型预训练变成人形机器人公司的核心战略](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X 宣布成立 1X World Model Lab，定位为面向全自主 humanoid 的前沿研究组织，并任命曾参与 Luma AI 多模态生成视频模型扩展的 Sam Sinha 为 Founding AI Researcher and Head of World Models。1X 给出的路线非常明确：web-scale media + egocentric human videos + simulation + dexterous remote operated robot data + on-policy NEO data，再通过真实部署进行 robot data collection 和 RL。1X 表示，机器人不是 fine-tuning 问题，通用人形机器人需要从一开始就在关键物理世界数据上预训练。

- **核心价值：** 这是今天的数据相关报道。1X 把“世界模型”从论文概念升级为公司组织架构，说明头部玩家已经认为具身智能的长期护城河是数据混合、预训练、部署回流和在策略数据闭环。

### 2. [Figure Helix：System 2 负责语义理解，System 1 负责 200Hz 连续控制](https://www.figure.ai/news/helix)

**摘要：** Figure 的 Helix 是一个 System 1 / System 2 架构的 VLA。System 2 是 7B 参数 VLM，以 7-9Hz 运行，负责场景理解和语言理解；System 1 是 80M 参数 visuomotor transformer，以 200Hz 输出连续控制，覆盖手腕、手指、头部、躯干等 35 自由度上半身动作。Helix 用约 500 小时多机器人、多操作者高质量遥操作数据训练，并使用 VLM 自动生成 hindsight instruction，让同一套权重完成拿取、放置、开抽屉、双机器人协作等任务。

- **核心价值：** Helix 代表一条典型 VLA 工程路线：慢思考的 VLM 负责语义，快反应的控制策略负责动作。它说明端到端不等于一个模型包打天下，而是需要在不同时间尺度上组织智能。

### 3. [Figure Helix 物流版：8 小时高质量示范数据、立体视觉和自校准推动商业场景落地](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure 将 Helix 扩展到物流包裹分拣场景，要求机器人从传送带上抓取不同尺寸、形状、重量和刚性的包裹，并调整标签方向供扫描。报告显示，仅 8 小时经过精心筛选的示范数据就能训练出可用策略；加入立体视觉后，吞吐相对非立体基线提升 60%；高质量数据在少三分之一数据量的情况下，仍能带来 40% 更高吞吐。Figure 还引入 learned visual proprioception，让机器人通过视觉自校准，提高跨机器人迁移能力。

- **核心价值：** 这是 VLA 从实验演示走向 ROI 场景的关键样本。物流场景强调吞吐、鲁棒性和跨机部署，说明 VLA 商业化不只看泛化能力，还看数据筛选、自校准和速度优化。

### 4. [NVIDIA Isaac GR00T：开放人形机器人基础模型平台，覆盖数据、仿真、训练与部署](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA Isaac GR00T 是面向通用人形机器人的开放参考平台，包括开放数据和数据管线、开放机器人基础模型、基于 Omniverse 和 Cosmos 的仿真框架、中间件、CUDA-X 加速运行库，以及 Jetson Thor 实时推理和控制。NVIDIA 表示，GR00T 模型接受语言和图像等多模态输入，可进行抓取、搬运、双臂传递和多步骤任务，并可通过 post-training 适配具体本体、任务和环境。

- **核心价值：** GR00T 把 VLA / 机器人基础模型的工程栈标准化了：数据、仿真、训练、部署和硬件加速一起提供。未来人形机器人竞争会越来越依赖完整工具链，而不是单点模型。

### 5. [宇树 H2 Plus 成为 NVIDIA Isaac GR00T 参考人形机器人平台](https://www.unitree.com/news/40)

**摘要：** 宇树科技官网 6 月新闻列表显示，Unitree H2 Plus 被宣布为 NVIDIA Isaac GR00T Reference Humanoid Robot for Academic Research。H2 Plus 位于宇树 H2 人形机器人产品线之上，并进入 NVIDIA 人形机器人生态。NVIDIA GR00T 生态页面也列出 Unitree Robotics 作为 humanoid robotics ecosystem 成员。

- **核心价值：** 这说明国内硬件公司正在进入全球 VLA / 机器人基础模型生态。硬件不只是本体销售，更是承载世界模型、VLA 策略和开发者工具链的标准平台。

---

## 前沿论文

### 1. [LaST-HD：用动作条件世界模型，把人手示范和机器人轨迹对齐到同一潜在推理空间](https://arxiv.org/abs/2606.23685)

**摘要：** `LaST-HD` 提出一种 human-to-robot action learning 范式，将 reasoning-before-acting VLA 扩展到人手数据迁移。它不是简单模仿人手几何轨迹，而是训练 action-conditioned world model，将未配对的人手轨迹和机器人轨迹对齐到共享 forward-dynamics latent space，再用统一 latent target 监督 VLA 的推理过程。团队还开发了低成本 Out-of-Lab Glove，用于采集高精度人手关键点数据。实验中，混合人机共训练可提升新物体、新场景和新位置泛化；通过在线校正，仅 20 分钟 OOL glove 数据即可在新环境达到超过 90% accuracy。

- **核心价值：** 这篇论文把 VLA、世界模型和低成本数据采集连在一起。它说明人类手部数据可以通过世界模型对齐到机器人动作空间，从而降低机器人数据采集成本。

### 2. [KEMO：给长程操作 VLA 加事件驱动关键帧记忆，任务成功率提升 23.6%](https://arxiv.org/abs/2606.23589)

**摘要：** `KEMO` 面向长程机器人操作提出轻量级 plug-in memory 框架。长程任务中，相似视觉观测可能出现在不同阶段，正确动作依赖此前完成过的步骤。KEMO 结合机器人运动学和视觉过滤，自动选择与任务状态变化相关的关键帧，将其编码为时间有序 memory tokens，再通过 cross-attention 和 gated residual fusion 融入 VLA 训练。真实双臂操作任务覆盖 2-6 个评分子任务，轨迹长度 830-2846 步、时长 28-95 秒。相比无记忆 baseline（如 π0.5），KEMO 将 Task Success Rate 提高 23.6%，Stage Completion Rate 提高 34.1%。

- **核心价值：** VLA 如果没有记忆，很容易在长程任务中“忘了自己做到哪一步”。KEMO 提供了一个工程上很实用的方向：不是保留所有历史，而是保留任务状态变化的关键帧。

### 3. [Flatness Preserves Instruction Following：VLA 微调会出现“指令失明”，SAM 可提升 60% 以上指令跟随](https://arxiv.org/abs/2606.23641)

**摘要：** 该论文指出，VLA 在小规模机器人数据上微调时，可能破坏预训练视觉语言表征，导致策略忽视语言指令、依赖视觉捷径，作者称为 instruction blindness。研究团队在相同数据、无需额外架构修改的情况下，引入 sharpness-aware minimization（SAM）进行 flatness-preserving finetuning。结果显示，SAM 在多个仿真和真实 benchmark 上将指令跟随能力提升超过 60%，尤其在有干扰物的 object grounding 任务上改善明显。

- **核心价值：** VLA 落地不是简单 fine-tune 越多越好。小数据微调可能让模型失去语言理解能力，未来机器人公司需要把“保住指令跟随”作为模型微调的核心指标。

### 4. [dVLA-RL：把离散扩散 VLA 的去噪过程建模为 MDP，LIBERO 成功率达 99.7%](https://arxiv.org/abs/2606.23623)

**摘要：** `dVLA-RL` 面向 Discrete Diffusion VLA，提出在 denoising trajectories 上进行强化学习。离散扩散 VLA 将视觉、语言和动作统一到离散 token 空间，但此前主要依赖 supervised fine-tuning。dVLA-RL 将去噪过程建模为 MDP，把学习目标从最终动作边缘概率转向采样生成路径的联合概率，并提出可根据任务复杂度调整 denoising steps 的调度策略。实验显示，该方法在 LIBERO 上达到 99.7% 成功率，在 RoboTwin 2.0 上比 SFT baseline 提升 30.6%。

- **核心价值：** 这说明 VLA 训练范式正在从 SFT 扩展到 RL。对复杂多任务机器人而言，强化学习可能成为 VLA 从“模仿示范”走向“策略优化”的关键补充。

### 5. [RECALL：面向 VLA 的恢复经验主动采集，让机器人少浪费示范数据](https://arxiv.org/abs/2606.23617)

**摘要：** `RECALL` 研究 VLA 的 active lifelong learning。传统做法是在策略表现差时被动收集更多示范，但这要求机器人先失败、难以判断哪些状态需要监督，也会浪费人类示范在已学会的任务片段上。RECALL 证明，基于不确定性的主动数据采集比被动示范更高效；但如果只用主动采集的 recovery data 微调，又会出现灾难性遗忘。论文进一步比较 replay-based data mixing 和 elastic weight consolidation 等连续学习方法。

- **核心价值：** VLA 的数据闭环不能只是“失败后再录一遍”。未来机器人需要知道哪些状态最值得请人示范，同时还不能忘记原有技能。

### 6. [SkyJEPA：面向四旋翼的长程世界模型，实现零样本 sim-to-real 控制](https://arxiv.org/abs/2606.23444)

**摘要：** `SkyJEPA` 将 JEPA 风格 latent dynamics model 用于实时四旋翼控制。传统神经动态模型在长程预测中容易因自回归误差累积而退化，SkyJEPA 在 latent space 中建模动力学，并引入 physics-inspired prober，将冻结 latent 映射到可解释状态，实现物理一致的长程预测。团队还开发结构化自动数据生成 pipeline，减少昂贵且危险的真实采集依赖，并在室外闭环实验中展示零样本 sim-to-real transfer 和跨工况泛化。

- **核心价值：** 世界模型不只服务家庭操作，也能服务高速控制。SkyJEPA 说明 latent world model 与物理先验结合，可能成为机器人长程预测和实时控制的重要方向。

### 7. [BiliVLA：VLA 进入胆道内镜导航，真实 phantom 实验成功率 84.85%](https://arxiv.org/abs/2606.23531)

**摘要：** `BiliVLA` 将胆道内镜导航建模为 instruction-conditioned visuomotor learning 问题。模型输入内镜观测和阶段性语言指令，同时预测目标类别、grounded bounding box 和 3 自由度离散电机命令。训练采用 grounding-enhanced SFT + Group Relative Policy Optimization（GRPO）两阶段流程，并加入 scene-aware supervision 与 safety-aware recovery supervision。三个 ERCP 子任务中，BiliVLA 在真实 phantom 实验中达到 91.96% 平均动作精度和 84.85% 总成功率。

- **核心价值：** VLA 正在进入医疗机器人等高约束场景。医疗场景对语义 grounding、安全恢复和动作一致性要求极高，是检验 VLA 是否可靠的重要试金石。

---

## 开源生态

### 1. [LIBERO-Safety 项目页开放：VLA 安全基准覆盖物理安全和语义安全](https://libero-safety.github.io/)

**摘要：** LIBERO-Safety 项目页展示了其 VLA 安全 benchmark、数据生成 pipeline、数据对比、评测结果和失败案例。项目使用 keypose-driven trajectory generation 生成可扩展的 collision-free 示范，并按物理安全、语义安全、任务难度和环境随机性进行评估。

- **核心价值：** 这是 VLA 走向部署前必须补上的工具。只有同时评估碰撞、安全约束、语义错配和长程失败，模型上线才有工程可信度。

### 2. [NVIDIA Isaac GR00T 模型开放下载，工具链覆盖数据、仿真、训练和部署](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** NVIDIA Isaac GR00T 提供面向通用人形机器人的开放基础模型与配套工具，官方页面显示其组成包括开放数据和数据管线、仿真框架、中间件、CUDA-X 加速库和 Jetson Thor 部署能力。

- **核心价值：** GR00T 的意义在于降低人形机器人开发门槛：开发者不必从零搭建基础模型、仿真、训练和部署链路，而是可以在统一生态中迭代。

### 3. [Flatness-VLA 项目页开放：同样数据，通过 SAM 微调减少指令失明](https://haochenz11.github.io/papers/flatness-vla/)

**摘要：** 项目页展示了 SAM 微调在 LIBERO-PRO、LIBERO-CF、LangGap 以及真实 DROID pick-and-place 任务中的结果。π0.5 + SAM 在多项 counterfactual instruction 测试中显著提升 object grounding 和 task success。

- **核心价值：** 很多公司会用有限客户场景数据微调 VLA。这个项目提醒行业：微调方法本身会决定模型是否仍听得懂语言指令。

### 4. [ROBOSHACKLES 数据集开放：世界模型和 VLA 的安全拒绝学习需要危险场景数据](https://huggingface.co/datasets/YZW00/RoboShackles)

**摘要：** ROBOSHACKLES 数据集开放 10,000 段安全关键机器人视频，覆盖电气危险等家庭危险场景。其目标是用于具身基础模型的拒绝学习和危险预判，避免机器人在执行前生成不安全动作。

- **核心价值：** VLA 与世界模型不仅要学会“怎么做”，还要学会“什么时候不能做”。安全拒绝数据会成为家庭机器人部署的关键资源。

---

## 公司情报

### 1. [1X：World Model Lab 把世界模型、数据和 NEO 部署闭环打通](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X World Model Lab 将重点放在大规模 AI 预训练、frontier world models 和 reasoning models。1X 认为，拥有从预训练、机器人学习、评估、部署到在策略数据收集的完整闭环，是其加速人形机器人自主性的关键。

- **核心价值：** 1X 的战略判断很直接：机器人公司要掌握整个学习闭环，不能只依赖外部模型或后期微调。

### 2. [Figure AI：Helix 展示 VLA 的商业化路线，从家庭泛化抓取走向物流吞吐](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure Helix 先展示自然语言驱动的家庭物品抓取和双机器人协作，再扩展到物流包裹分拣。物流场景中，Helix 的 System 1 加入隐式立体视觉、多尺度视觉表征、视觉本体感知校准和 Sport Mode 加速。

- **核心价值：** Figure 的路径说明 VLA 商业化可能先从高价值物流任务验证，再反哺家庭机器人能力，而不是直接进入复杂家庭全场景。

### 3. [NVIDIA：GR00T 正在把人形机器人开发从单点模型变成平台生态](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA GR00T 生态覆盖 Agility Robotics、Apptronik、Boston Dynamics、NEURA Robotics、Sanctuary AI、Unitree Robotics 等企业。其目标不是只发布一个模型，而是提供训练、仿真、数据、部署和加速硬件的一体化参考平台。

- **核心价值：** 这会改变机器人公司的研发结构：未来很多团队可能围绕 GR00T 工具链开发差异化本体和场景能力，而不是从底层基础模型开始重复建设。

### 4. [宇树科技：H2 Plus 进入 GR00T 参考平台后，国内硬件厂商加速连接全球基础模型生态](https://www.unitree.com/news)

**摘要：** 宇树官网 6 月新闻显示 H2 Plus 成为 NVIDIA Isaac GR00T Reference Humanoid Robot for Academic Research。宇树产品线已覆盖 H2、R1、G1、H1 / H1-2 等人形机器人以及 Go2、B2、A2 等四足机器人。

- **核心价值：** 国内硬件公司若能成为全球基础模型平台的标准本体，将获得研究者、开发者和产业伙伴的长期生态入口。

---

## 结尾总结

6 月 24 日这期的主线，是 VLA 和世界模型正在走出“会按语言做动作”的第一阶段，进入更现实的第二阶段：安全、记忆、长期任务、数据闭环和物理推理。

LIBERO-Safety 说明，VLA 需要同时通过物理安全和语义安全考验；KEMO 说明，长程任务必须具备事件记忆；Flatness-VLA 说明，小数据微调可能让模型产生“指令失明”；dVLA-RL 说明，VLA 正在从 SFT 扩展到强化学习；LaST-HD 和 SkyJEPA 则把世界模型用于人手数据迁移和长程动力学预测。公司侧，1X 把世界模型实验室独立出来，Figure 用 Helix 验证 VLA 的家庭与物流路线，NVIDIA 用 GR00T 把基础模型、仿真、数据和部署标准化。

可以下一个判断：**VLA 的上半场是“语言到动作”，下半场是“可安全部署的物理智能系统”。** 未来能跑出来的公司，不一定是 demo 最炫的公司，而是能把世界模型、VLA、安全评测、数据采集和硬件平台接成闭环的公司。

**互动问题：** 你认为 VLA 真正落地家庭机器人，最先要补齐的是安全评测、长期记忆、世界模型，还是低成本数据采集？欢迎留言交流。

## 关键词索引

**公司与机构：** 1X Technologies、Figure AI、NVIDIA、Unitree Robotics、Agility Robotics、Apptronik、Boston Dynamics、NEURA Robotics、Sanctuary AI、Carnegie Mellon University  
**模型与项目：** LIBERO-Safety、Helix、Isaac GR00T、LaST-HD、KEMO、Flatness-VLA、dVLA-RL、RECALL、SkyJEPA、BiliVLA、ROBOSHACKLES、π0.5、GR00T-N1.5、Out-of-Lab Glove  
**技术方向：** VLA、Vision-Language-Action、世界模型、World Model、World Action Model、具身基础模型、System 1 / System 2、事件驱动记忆、长程操作、物理安全、语义安全、instruction blindness、SAM 微调、离散扩散 VLA、强化学习、在策略数据、human-to-robot learning、sim-to-real  
**关键数字：** LIBERO-Safety 19,664 条无碰撞示范、评测 8 个 VLA 和 2 个具身基础模型、Figure Helix 500 小时高质量数据、System 2 7B 参数 / 7-9Hz、System 1 80M 参数 / 200Hz、Helix 控制 35 自由度、Figure 物流 8 小时示范数据、立体视觉提升 60% 吞吐、KEMO 提升 23.6% 任务成功率和 34.1% 阶段完成率、dVLA-RL 在 LIBERO 达 99.7% 成功率、LaST-HD 20 分钟 OOL glove 数据超过 90% accuracy、BiliVLA 84.85% 总成功率

## 值得分享

1. **VLA 的下一场竞争是安全：** LIBERO-Safety 用 19,664 条无碰撞示范评测 VLA，发现模型即使不碰撞，也会出现语义错配和长程任务失败。
2. **世界模型正在成为公司战略：** 1X 成立 World Model Lab，把 web 视频、人类第一视角、仿真、遥操作和 NEO 在策略数据写进人形机器人预训练路线。
3. **VLA 不能只靠短程反应：** KEMO 证明给 VLA 加事件关键帧记忆，可让真实双臂长程操作任务成功率提升 23.6%，长期记忆将成为家庭机器人刚需。