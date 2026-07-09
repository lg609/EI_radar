# 具身智能情报前沿｜VLA 从“离线模仿”走向“在线自适应”

**作者：具身视界** · 2026.06.25

> 今天的主线继续放在 VLA 和世界模型，但关注点从“模型架构”推进到“部署后如何变强”。最新一批论文集中指向同一个问题：VLA 不能只靠离线示范训练，一旦进入真实家庭、工厂和物流现场，就必须能在线适应、记住动作后果、自己补技能、评估混合质量数据，并把世界模型变成价值评估器。ROAD-VLA、Reflective VLA、InSight 和 World Value Model 分别从在线自蒸馏、动作后果记忆、自主技能获取、世界模型价值评估四个方向补上这块短板。

---

## 今日重磅

### [ROAD-VLA：用动作空间自蒸馏解决 VLA 在线适应难题，部署后学习成为新主线](https://arxiv.org/abs/2606.25800)

**摘要：** 6 月 24 日提交的 `ROAD-VLA` 聚焦一个非常现实的问题：Vision-Language-Action 模型在真实部署后如何在线适应。论文指出，高维自回归动作策略很难直接从稀疏奖励中学习；虽然自蒸馏理论上可以提供更密集的训练信号，但基于文本的 privileged teacher——例如示范、检索经验或高层规划——对 VLA 适应效果有限，因为符号指导和低层机器人动作之间存在 modality gap。ROAD-VLA 的核心做法，是构造一个直接位于动作空间的 proximal teacher：它用校准后的 advantage estimates 扰动 action-token logits，把稀疏奖励转化为密集 token-level 监督，同时让 teacher 保持接近当前策略。论文还给出在校准优势和准确 teacher matching 条件下的策略改进下界。实验覆盖 7 个机器人操作环境，包含分布内和分布外变化，ROAD-VLA 在几乎所有设置中优于 PPO，展示出更稳健的在线 VLA 适应能力。

- **来源：** arXiv
- **核心价值：** 这是 VLA 从“离线模仿学习”走向“部署后持续适应”的关键方向。真实机器人进入家庭、仓储或工厂后，环境分布一定会漂移；如果每次都要重新采集大规模示范，商业化就很难成立。ROAD-VLA 说明，未来 VLA 的竞争不只是预训练多强，而是能否把真实运行中的稀疏反馈转化为可学习的密集信号。

---

## 行业新闻

### 1. [1X World Model Lab：把世界模型预训练、在策略数据和机器人部署闭环连成一条链](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X World Model Lab 的核心判断是：机器人不是 fine-tuning 问题，通用人形机器人需要从一开始就在最关键的物理世界数据上预训练。1X 给出的数据配方包括 web-scale media、egocentric human videos、simulation、dexterous remote operated robot data 和 on-policy NEO data，并通过真实部署进行 robot data collection 和 RL。公司表示，NEO 工厂上线后，扩大 fleet 以支持真实世界数据采集已不再是瓶颈，因此要提高世界模型创新速度。

- **核心价值：** 这是今天的数据相关报道。1X 把世界模型、机器人 fleet、真实部署和在策略数据串成闭环，代表了人形机器人公司从“做本体”转向“做持续学习系统”的战略变化。

### 2. [Figure Helix 物流版：VLA 商业化开始考验吞吐、自校准和数据筛选](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure 将 Helix VLA 扩展到物流包裹处理与分拣场景。该任务要求机器人处理刚性箱子、柔性袋子、不同重量和尺寸的动态包裹，并将标签调整到可扫描方向。Figure 在报告中强调，8 小时高质量示范数据即可训练出灵巧策略；立体视觉让系统相对非立体基线吞吐提升 60%；精心筛选后的高质量示范在少三分之一数据量时仍带来 40% 更高吞吐；learned visual proprioception 让单一策略可迁移到多台机器人。

- **核心价值：** Helix 物流版说明 VLA 商业化首先要过“工程指标”这一关：吞吐、跨机迁移、在线校准、数据质量和纠错行为，都会直接影响 ROI。

### 3. [NVIDIA Isaac GR00T：人形机器人基础模型正在平台化](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA Isaac GR00T 是面向通用人形机器人的开放参考平台，覆盖开放数据与数据管线、开放机器人基础模型、Omniverse / Cosmos 仿真框架、中间件、CUDA-X 加速库和 Jetson Thor 实时推理控制。GR00T 模型接受语言、图像等多模态输入，可用于抓取、搬运、双臂传递、多步骤任务，并支持对具体本体、任务和环境做 post-training。

- **核心价值：** GR00T 把 VLA / 机器人基础模型从单点论文变成全栈平台：数据、仿真、训练、部署和算力一起标准化。这会加速开发者生态，也会抬高非平台型团队的基础设施门槛。

### 4. [智元 Rich Interaction：真实失败数据继续成为世界模型训练的重要燃料](https://www.agibot.com/article/231/detail/72.html)

**摘要：** 智元机器人 AGIBOT WORLD 2026 Theme 2：Rich Interaction 数据集继续值得关注。该数据集 100% 来自真实世界，用探索性遥操作采集丰富物理交互，记录抓取失败、碰撞、物体掉落、不稳定接触、液体飞溅等事件。智元明确表示，这类数据面向世界模型、神经仿真器、物理感知表征和鲁棒表示学习。

- **核心价值：** 世界模型需要的不只是“成功任务视频”，而是物理世界的完整分布。失败、接触、变形、液体、碰撞这些难采数据，会成为训练可靠 VLA 和世界模型的稀缺资产。

### 5. [WOLF-VLA：VLA 开始从机械臂操作扩展到全身人形运动](https://arxiv.org/abs/2606.25591)

**摘要：** `WOLF-VLA` 针对目前 VLA 在全身、接触丰富的人形 locomotion 场景研究不足的问题，提出结合 whole-body optimal-control motion synthesis 和大规模多模态数据集的框架。团队构建了覆盖 6 类运动相关任务的动态可行人形轨迹数据集，每类任务包含环境变化、物体颜色、位置和视觉干扰。模型输入关节轨迹、第一视角视觉观测和自然语言指令，输出具备推理能力和初始条件鲁棒性的 locomotion policy。论文表示完整数据集、模型 checkpoint 和 benchmark simulation suite 将开放。

- **核心价值：** VLA 不会长期停留在桌面操作。全身运动、接触、平衡和安全约束将把 VLA 推向更难的物理控制问题，也会让“动态一致示范数据”变得更重要。

---

## 前沿论文

### 1. [Reflective VLA：把“动作后果”放进上下文，提升跨环境泛化](https://arxiv.org/abs/2606.25215)

**摘要：** 多数 VLA 是 reactive policy：只根据当前指令和观测预测下一步动作，默认当前观测已经包含所有动作相关状态。但真实部署中，摄像头—机器人几何、相机标定、执行器偏差等因素很难从单帧观测中识别。`Reflective VLA` 将每次决策条件扩展为 observation-action-consequence triplets，即不仅记录机器人看到了什么、做了什么，还记录动作之后场景如何变化，从而暴露部署环境中“动作到观测后果”的映射。项目页显示，Reflective VLA 在 SimplerEnv 平均成功率从 72.9 提升到 78.2，在 LIBERO-Plus 从 82.3 提升到 87.7，在 LIBERO-Plus-Hard 从 64.6 提升到 68.8。

- **核心价值：** 机器人真正需要的不是更长上下文，而是有因果含义的动作后果记忆。Reflective VLA 让模型通过历史交互理解当前本体和环境偏差，是部署泛化的重要方向。

### 2. [InSight：VLA 自主发现缺失原语，无目标技能人类示范也能学会倾倒、旋转和清扫](https://arxiv.org/abs/2606.24884)

**摘要：** `InSight` 让 VLA 在 primitive-action level 变得可 steer，然后用 VLM 发现新任务缺失的动作原语，并自动尝试、验证、标注和回灌成功示范，形成 data flywheel。项目页显示，InSight 在没有目标技能人类示范的情况下，可从不同任务示范中自主获取 block flipping、drawer closing、twisting、pouring、sweeping 等技能。真实任务中，pouring 达到 96% 成功率，对比 CaP-X 为 16%；twist-then-pour 14 原语长程任务达到 80%，对比 CaP-X 为 4%；基础技能保持 100%。

- **核心价值：** InSight 把 VLA 从“学会已有示范”推进到“主动补齐缺失技能”。这对家庭机器人尤其关键，因为真实家庭任务组合无限，不可能为每个目标技能都收集完整示范。

### 3. [World Value Models：用世界模型评估混合质量数据，给机器人策略学习提供价值信号](https://arxiv.org/abs/2606.24742)

**摘要：** `World Value Model`（WVM）提出把世界模型和价值估计结合起来，构建通用机器人 value model。论文指出，准确价值估计需要深层时间理解：既要用历史上下文 grounding 当前 belief，又要规划未来结果。而现有机器人 value model 多基于 VLM backbone，预训练主要来自静态或时间稀疏视觉观测，不擅长时间建模。WVM 利用世界模型的时间建模和未来规划能力评估 task progression，并引入 `Suboptimal-Value-Bench`，包含 800 条多本体 suboptimal trajectories 和高质量人工帧级标注。实验显示 WVM 在标准 benchmark 和 Suboptimal-Value-Bench 上保持 SOTA Value-Order Correlation，并能提升仿真和真实部署中的策略学习表现。

- **核心价值：** 这是世界模型很实际的落地方式：不一定直接生成动作，而是先用来评估混合质量数据、排序轨迹、指导策略学习。随着机器人数据越来越杂，value model 会成为数据筛选和策略提取的核心工具。

### 4. [G3VLA：给 VLA 注入相机几何先验，多相机不是独立图片](https://arxiv.org/abs/2606.24472)

**摘要：** `G3VLA` 认为现有 VLA 虽然利用了预训练 VLM 的语义知识，但视觉 token 多停留在 2D 图像坐标，未充分利用机器人相机的内参、外参等几何结构，尤其在多相机设置中，各视角明明由标定几何相互耦合，却常被当成独立图像处理。G3VLA 提出 camera-aware geometric module，向预训练 VLA 的 visual-token stream 注入校准结构，包括 intrinsic-conditioned ray embeddings、projective positional encoding（PRoPE）和双向跨视角融合。方法不改变动作空间和模仿学习目标，并在 π0、π0.5、GR00T 1.5 等模型上验证。

- **核心价值：** VLA 要可靠操作三维物理世界，不能只靠 2D 语义。相机标定、射线、跨视角融合等几何先验，可能成为提高空间任务成功率的关键模块。

### 5. [SVP-IL：把语义推理和几何 grounding 解耦，50-100 条示范也能提升语言条件操作](https://arxiv.org/abs/2606.25360)

**摘要：** `SVP-IL` 针对端到端 VLA 将语义推理和空间控制耦合在一起导致的 alignment bottleneck，提出解耦架构。它用视觉语言基础模型把指令解析为 zero-shot geometric masks，再转化为 Spatial Visual Prompts（SVP），注入连续动作生成器。这样可以给低数据模仿学习提供明确空间梯度指导。实验显示，在高度模糊的语言条件任务中，仅用 50-100 条示范，SVP-IL 将平均成功率从 24.0% 提升到 39.5%，标准 benchmark 达到 67.8%，真实机器人实验也验证其数据效率和鲁棒性。

- **核心价值：** 端到端不是唯一答案。对低数据真实场景，先把“指令对应哪个空间目标”显式 grounding，再生成动作，可能比纯黑箱 VLA 更稳。

### 6. [GRA：从生成机器人视频中只监督“几何”，不强行恢复伪动作](https://arxiv.org/abs/2606.24448)

**摘要：** `Supervise What Survives` 提出 Geometry-guided Representation Alignment（GRA）。论文认为，VLA 需要大规模视频—动作对，但真实遥操作稀缺；生成机器人视频虽然可扩展，但从合成像素中恢复低层控制是错位抽象。视频生成过程保留下来的主要是可见几何，即任务的“where”，而真实示范才包含 motor command 的“how”。因此，GRA 只从生成视频中提取未来 2D 末端执行器 waypoint 作为几何监督，训练视觉 backbone；action head 仍只用真实示范训练。

- **核心价值：** 这对数据扩展非常重要。生成视频可以补几何表征，但不能假装拥有真实控制信号。未来 VLA 数据管线需要更精细地决定“哪类数据监督哪一部分模型”。

### 7. [MANGO：自动生成 VLA 测试 oracle，让机器人测试从终态判断走向细粒度诊断](https://arxiv.org/abs/2606.24815)

**摘要：** `MANGO` 面向 VLA-enabled robots 的测试问题。现有测试通常依赖人工构建 symbolic test oracles，只从最终状态判断任务是否成功，成本高、绑定具体任务且难以定位中间错误。MANGO 使用多智能体框架从自然语言任务描述自动生成细粒度 oracle：先生成可复用 atomic task 库，再生成 simulator-grounded oracle definition，最后将复杂指令分解为有序 atomic actions 和对应 oracle。实验覆盖 LIBERO_10 和 RoboCasa Humanoid Tabletop，能检测与人工 symbolic oracle 相近数量的故障，并提供更丰富诊断。

- **核心价值：** VLA 要上线，测试系统必须规模化。MANGO 说明未来机器人测试不只是“成功 / 失败”，而是要能自动定位哪个中间原语、哪个状态转换出了问题。

---

## 开源生态

### 1. [InSight 项目页开放：VLA 自主技能获取的 data flywheel 样板](https://insight-vla.github.io/)

**摘要：** InSight 项目页展示了从 demonstration segmentation、primitive steerability 到 VLM-guided skill acquisition 的完整流程。系统基于 π0.5 + LoRA，并使用 Gemini 3 Flash 承担示范分割、任务规划、原语缺口发现和图像成功检查等角色。

- **核心价值：** InSight 的开源展示为 VLA 连续学习提供了清晰路径：把任务拆成可复用原语，再让机器人围绕缺失原语自动采数据。

### 2. [Reflective VLA 项目页开放：动作后果 triplets 支持实时部署](https://lianqing11.github.io/reflective-vla-page/)

**摘要：** Reflective VLA 项目页展示了 observation-action-consequence triplets、block-causal training 和 cached inference。代码标注为 Coming Soon。其核心机制是在 rolling context buffer 中复用已完成 triplets，支持实时在线部署。

- **核心价值：** 这类上下文机制会成为 VLA 部署的重要基础设施：机器人不只看当前画面，还要看自己刚才做了什么、环境如何响应。

### 3. [NVIDIA Isaac GR00T 模型与工具链开放](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** NVIDIA Isaac GR00T 提供面向通用人形机器人的开放基础模型和相关工具链，官方页面显示其覆盖开放数据、数据管线、仿真、训练、部署和 Jetson Thor 实时控制。

- **核心价值：** 对开发者来说，GR00T 是人形机器人 VLA / 基础模型的统一入口；对硬件厂商来说，能否适配 GR00T 生态会影响其研究和商业采用速度。

### 4. [AGIBOT WORLD Rich Interaction 数据集开放：真实失败与接触数据进入世界模型训练](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)

**摘要：** 智元 AGIBOT WORLD 2026 Theme 2 已在 Hugging Face 开放，聚焦真实世界接触丰富交互，包含抓取失败、碰撞、掉落、不稳定接触和液体飞溅等事件。

- **核心价值：** VLA 和世界模型要学会物理世界，必须从干净示范走向混乱真实分布。Rich Interaction 是国内公司在开放具身数据基础设施上的重要动作。

---

## 公司情报

### 1. [1X：世界模型实验室成为全自主 humanoid 的核心引擎](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X 明确表示 World Model Lab 将专注于大规模 embodied world model pretraining，并强调要掌握从数据整理、预训练、机器人学习、评估、部署到真实机器人在策略数据采集的完整学习闭环。

- **核心价值：** 这说明 1X 的长期竞争重点不只是 NEO 本体，而是围绕 NEO fleet 构建可持续增长的数据和世界模型系统。

### 2. [Figure AI：Helix 物流版验证 VLA 从家庭泛化到工业吞吐](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure 把 Helix 应用于物流包裹处理，强调 implicit stereo vision、multi-scale visual representation、learned visual proprioception 和 Sport Mode。报告中 8 小时高质量示范、60% 吞吐提升、50% 测试时加速等数字，体现了 VLA 的工程优化方向。

- **核心价值：** Figure 正在用商业场景反向优化 VLA 架构。物流场景的吞吐和稳定性要求，会倒逼 Helix 在视觉、控制、校准和数据管线上的迭代。

### 3. [NVIDIA：GR00T 平台把机器人基础模型和硬件部署绑定](https://developer.nvidia.com/isaac/gr00t)

**摘要：** GR00T 生态不仅有模型，还包含 Omniverse、Cosmos、Isaac Lab、CUDA-X、Jetson Thor 和 DGX Cloud 等训练部署基础设施。NVIDIA 同时列出多家 humanoid robotics ecosystem 成员，包括 Unitree Robotics 等。

- **核心价值：** NVIDIA 在机器人领域的打法越来越像 AI 基础设施平台：用模型牵引工具链，用工具链牵引硬件，用硬件绑定开发者和机器人厂商。

### 4. [智元机器人：开放真实物理交互数据，补齐世界模型训练稀缺样本](https://www.agibot.com/article/231/detail/72.html)

**摘要：** 智元 Rich Interaction 数据集以探索性遥操作方式采集真实物理交互，特别强调 failure、edge-case behavior 和 contact-rich interactions。公司表示，该数据集将支持 world models、neural simulators、physics-informed perception 和 robust representation learning。

- **核心价值：** 智元的数据路线很清楚：通过真实机器人操作和失败数据开源，抢占具身基础模型的数据生态入口。

---

## 结尾总结

6 月 25 日这期继续跟踪 VLA 和世界模型，可以看到一个清晰变化：行业正在从“训练一个会做动作的 VLA”转向“构建一个会部署后变强的机器人学习系统”。

ROAD-VLA 解决在线适应，把稀疏奖励变成动作 token 级监督；Reflective VLA 让模型记住动作后果，用历史交互理解本体和环境偏差；InSight 让 VLA 围绕缺失原语自主采集新技能；World Value Model 用世界模型评估混合质量轨迹，服务数据筛选和策略学习；G3VLA、SVP-IL 和 GRA 则从几何先验、空间视觉提示和生成视频监督边界出发，补 VLA 的空间 grounding 短板。

这意味着，VLA 的真正落地不会是一条单模型路线，而是一套系统工程：预训练模型、世界模型、在线适应、动作后果记忆、技能数据飞轮、价值评估、安全测试、几何 grounding 和真实数据闭环共同构成下一代机器人智能栈。

**互动问题：** 如果只能优先补一个能力，你认为家庭机器人最需要的是在线适应、长期记忆、自主学新技能，还是世界模型价值评估？欢迎留言讨论。

## 关键词索引

**公司与机构：** 1X Technologies、Figure AI、NVIDIA、智元机器人（AGIBOT）、Unitree Robotics、Stanford University、Princeton University、IDEA  
**模型与项目：** ROAD-VLA、Reflective VLA、InSight、World Value Model、WOLF-VLA、G3VLA、SVP-IL、GRA、MANGO、Isaac GR00T、AGIBOT WORLD 2026 Theme 2、Helix、NEO、Suboptimal-Value-Bench  
**技术方向：** VLA、Vision-Language-Action、世界模型、World Model、World-Action Model、在线适应、动作空间自蒸馏、动作后果记忆、observation-action-consequence triplets、自主技能获取、primitive steerability、data flywheel、value model、几何 grounding、多相机几何、Spatial Visual Prompts、生成机器人视频、混合质量数据、在策略数据  
**关键数字：** ROAD-VLA 覆盖 7 个机器人操作环境、Reflective VLA 在 SimplerEnv 从 72.9 提升到 78.2 / LIBERO-Plus 从 82.3 提升到 87.7、InSight pouring 96% / twist-then-pour 80% / 基础技能保留 100%、World Value Model 引入 800 条 suboptimal trajectories、Figure Helix 物流 8 小时示范数据、立体视觉提升 60% 吞吐、高质量示范少三分之一数据仍提升 40% 吞吐、SVP-IL 50-100 条示范从 24.0% 提升到 39.5%、WOLF-VLA 覆盖 6 类人形运动任务

## 值得分享

1. **VLA 正在进入部署后学习阶段：** ROAD-VLA 用动作空间自蒸馏把稀疏奖励转成 token 级监督，在 7 个机器人操作环境中几乎全面优于 PPO。
2. **机器人要记住“动作后果”：** Reflective VLA 不只看当前画面，而是记录观察、动作和结果，在 LIBERO-Plus 上将成功率从 82.3 提升到 87.7。
3. **世界模型开始服务数据筛选和策略学习：** World Value Model 用世界模型评估混合质量轨迹，并引入 800 条人工标注 suboptimal trajectories，为大规模机器人数据训练提供价值信号。