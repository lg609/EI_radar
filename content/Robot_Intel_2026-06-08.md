# 具身智能情报前沿｜具身大脑正在从动作模型升级为世界模型

**作者：具身视界** · 2026.06.08

> 明天最值得关注的变化，是“具身大脑”的定义正在变窄也变深：它不再只是把视觉、语言和动作接起来的 VLA，而是开始同时具备世界预测、任务分解、动作合成和闭环评测能力。机器人模型竞争正在从“能不能输出动作”转向“能不能在脑内推演未来、评估风险，再决定怎么动”。

---

## 💥 今日重磅

### [World-Language-Action提出WLA模型，把世界建模、语言推理和动作合成合成一个具身大脑接口](https://arxiv.org/abs/2606.05979)

**摘要：** 6 月 4 日提交的 `World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis` 提出一类新的具身基础模型 WLA。不同于只从图像和指令直接输出动作的 VLA，WLA 同时接收文本指令、图像和机器人状态，联合预测文本子任务、子目标图像和机器人动作。其核心是自回归 Transformer，把“下一状态”拆成语义层面的意图和细粒度物理动态；物理动态由 World Expert 监督，再影响 Action Expert 的动作生成。原型 WLA-0 拥有 2B active parameters，在 NVIDIA RTX 5090 上单次推理约 40 ms，并在 RoboTwin2.0 Clean 上达到 92.94% 成功率、在 RMBench 上达到 56.5% 成功率。

- **来源：** arXiv
- **核心价值：** 这说明具身大脑正在从“语言理解 + 动作头”升级为“世界预测 + 语言推理 + 动作执行”的统一模型。对机器人公司来说，未来的核心壁垒不是单个策略网络，而是能否让模型先在内部预测任务进展和物理后果，再把预测转化为可执行动作。

---

## 📰 行业新闻

### 1. [HANDOFF在Unitree G1上展示自然语言驱动的人形全身控制，VLM planner连接任务规划与控制接口](https://arxiv.org/abs/2606.06493)

**摘要：** `HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers` 面向人形机器人真实部署中的关键问题：任务规划器输出的语义意图，如何稳定传给全身控制器。HANDOFF 通过一个紧凑、显式的 task-space command interface，将 whole-body motion tracking、locomotion 和 fall-recovery 三类教师蒸馏到 mixture-of-experts 学生控制器，并在 Unitree G1 上展示自然语言驱动的任务 rollout，背后由 VLM-driven agentic planner 负责规划。

- **来源：** arXiv
- **核心价值：** 具身大脑不能只停留在高层推理，必须有一个足够简洁又可控的接口连接全身控制。HANDOFF 的价值在于把“看懂任务”向“全身执行”推进了一步。

### 2. [MotionDisco用LLM引导进化搜索，自动发现并部署人形长时程移动操作技能](https://arxiv.org/abs/2606.06139)

**摘要：** `MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation` 不依赖遥操作或人类动作重定向，而是用 LLM-guided evolutionary search 在交互序列空间中搜索候选动作，再结合 kinodynamic trajectory optimizer 生成可跟踪轨迹。论文称这是首次完全通过自动进化搜索发现并部署长时程人形 loco-manipulation 技能的工作，并将轨迹训练成强化学习跟踪策略后迁移到真实人形机器人。

- **来源：** arXiv / 项目视频
- **核心价值：** 这代表具身大脑的一条新路线：不是人类示范喂给机器人，而是让模型自己提出交互顺序、优化轨迹，再训练控制器执行。自动技能发现会直接影响人形机器人技能库扩展速度。

### 3. [TempoVLA让VLA具备速度可控能力，可在低风险阶段加速、高风险接触阶段减速](https://arxiv.org/abs/2606.06491)

**摘要：** `TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies` 指出当前 VLA 通常继承训练示范中的固定速度，无法根据风险动态调节执行节奏。TempoVLA 通过 Variable-Speed Trajectory Augmentation 对示范轨迹重新定时，再把目标速度作为条件输入模型，使同一个 VLA 能在仿真和真实任务中实现加速与减速。论文还展示了与大型多模态模型协作，根据场景风险动态控制速度。

- **来源：** arXiv
- **核心价值：** 速度控制是具身大脑走向真实部署的必要能力。真正可用的机器人不是一直“快”或一直“稳”，而是能判断什么时候快速通过、什么时候慢下来精细接触。

---

## 📑 前沿论文

### 1. [MPCoT为VLA引入多路径潜空间推理，零文本思维链实现测试时可扩展决策](https://arxiv.org/abs/2606.06245)

**摘要：** `MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action` 关注 VLA 在长时程、高不确定性控制中的脆弱性。它不输出显式文本 CoT，而是在潜空间初始化多条假设路径，通过 K 步 weight-tied refinement 和 soft aggregation 后再解码动作。训练阶段用 expert-action consistency、world-model / VLM-based progress 和 success feedback 指导路径偏好。该方法保持原有 8-step action interface，不生成推理 token，同时可以通过 K、M 控制测试时计算量。

- **来源：** arXiv
- **核心价值：** 具身大脑的“思考”未必需要变成文字。潜空间多路径推理更接近机器人控制需求：在不增加语言 token 延迟的情况下，让模型在动作前多比较几种未来。

### 2. [PiL-World将世界模型用于VLA闭环评测，把真机成功率估计误差从63.2%降到12.0%](https://arxiv.org/abs/2606.05773)

**摘要：** `PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation` 针对现有机器人世界模型只做开环预测的问题，提出 chunk-wise world model。它交替执行 VLA 推理和世界模型预测，根据上一动作 chunk 生成的观测继续下一轮决策，从而模拟闭环执行。PiL-World 不只学习成功示范，也学习失败执行轨迹，使想象 rollout 更接近真实策略分布。在 3 个真实双臂操作任务上，它将真实 rollout 成功率与世界模型估计成功率之间的误差从 63.2% 降到 12.0%。

- **来源：** arXiv
- **核心价值：** 这是今天的数据相关报道。闭环评测需要失败数据、动作轨迹和多视角观测共同支撑；PiL-World 说明世界模型正在从“生成好看的未来视频”变成“替代部分真机测试的评测基础设施”。

### 3. [OSCAR用跨本体动作条件视频世界模型评估机器人策略，构建标准化数据清洗与去重管线](https://arxiv.org/abs/2606.04463)

**摘要：** `OSCAR: Omni-Embodiment Action-Conditioned World Model for Robotics` 面向真实机器人策略评估，提出跨本体动作条件视频世界模型。OSCAR 的重点之一是大规模标准化数据管线：对机器人和 egocentric human datasets 进行策展、过滤和去重，形成覆盖多任务、多场景、多动作和多机器人本体的联合训练数据。模型使用 2D kinematic skeleton rendering 作为统一动作条件表示，并基于 Cosmos-Predict2.5-2B 在单张 GH200 GPU 上微调，最终用于 RoboArena 策略评估。

- **来源：** arXiv / 项目页
- **核心价值：** 具身大脑要跨机器人泛化，数据管线比模型尺寸同样重要。OSCAR 表明“本体无关”的世界模型需要先把异构机器人、人手和操作视频清洗到统一动作表示。

### 4. [Flash-WAM把World-Action Model推理压缩到单步，延迟从8.1秒降到348毫秒](https://arxiv.org/abs/2606.05254)

**摘要：** `Flash-WAM: Modality-Aware Distillation for World Action Models` 解决世界动作模型实时性不足的问题。WAM 同时生成未来视频和机器人动作，性能强但迭代扩散带来高延迟。Flash-WAM 针对视频流和动作流不同噪声分布设计 modality-aware step distillation，在 LingBot-VA 上把每个 chunk 的延迟从 8.1 秒压缩到 348 ms，速度提升 23 倍；在 RoboTwin 2.0 上保持 85.5% 成功率、LIBERO 上保持 95.7%，并在 Unitree G1 真实机器人上恢复 60% 平均成功率。

- **来源：** arXiv
- **核心价值：** 具身大脑如果不能实时，就无法进入闭环控制。Flash-WAM 的意义在于把“边想象未来边行动”的路线向真实机器人控制周期推进。

---

## 💻 开源生态

### 1. [AffordanceVLA开放代码和项目页，用可供性中间表征增强VLA动作生成](https://github.com/Skywalker-yqz/AffordanceVLA)

**摘要：** `AffordanceVLA` 将可供性预测作为 VLA 的中间表征，分为 Which2Act、Where2Act 和 How2Act 三个模块，分别处理物体级 grounding、2D 交互定位和 3D 几何推理。项目提供代码和项目页，并通过自动数据增强缓解 dense affordance label 稀缺问题。

- **来源：** GitHub / arXiv
- **核心价值：** 具身大脑不能只“看见物体”，还要知道哪里能抓、怎么接触、用什么几何方式行动。可供性表征是连接视觉语义和真实动作的重要桥梁。

### 2. [MPC-RL开源GPU并行MPC求解器，用训练时MPC指导人形移动与操作强化学习](https://github.com/junhengl/mpc-rl)

**摘要：** `Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation` 开源 `mpc-rl` 代码库，提出训练时 MPC guidance 和 `π^nMPC` batched GPU MPC solver。该方法避免高内存和预编译问题，在大规模并行 RL 中直接用时变动力学提供 MPC 轨迹指导，并在多种移动和操作技能中做硬件验证。

- **来源：** GitHub / arXiv
- **核心价值：** 具身大脑的底层控制仍需要物理约束。MPC-RL 提供了一条实用路径：用 MPC 提供物理先验，用 RL 学鲁棒执行。

### 3. [M3imic开源多模态全身控制器，在Unitree G1上统一关节、人类姿态和末端位姿参考](https://github.com/Renforce-Dynamics/MultiModalWBC)

**摘要：** `M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking` 开源 MultiModalWBC。它用 modality-specific encoders 将 robot joint angles、human pose trajectories 和 end-effector poses 映射到共享潜空间，训练一个可跨参考模态迁移的全身控制策略。论文报告仿真中 unseen test dataset 峰值成功率达到 98.42%，并在 Unitree G1 上验证 sim-to-real。

- **来源：** GitHub / arXiv
- **核心价值：** 上层具身大脑会产生不同形态的运动意图，底层控制器必须能理解多种参考格式。M3imic 的价值在于让全身控制接口更通用。

---

## 🏢 产品与平台情报

### 1. [物流具身智能数据飞轮提出WM-DAgger，用世界模型生成长尾包裹操作恢复数据](https://arxiv.org/abs/2606.05960)

**摘要：** `Towards a Data Flywheel for Embodied Intelligence in Logistics` 将物流场景视为具身智能产业部署的重要试验场，提出数据中心化框架：把日常运营数据转成可复用资产，用 World Models 为长尾包裹操作生成可靠监督，再把部署反馈回流到策略改进。其中 `WM-DAgger` 作为初步结果，用世界模型合成 out-of-distribution recovery data，以增强模仿学习鲁棒性。

- **来源：** arXiv
- **核心价值：** 这是平台层的数据闭环信号。物流机器人每天都在产生真实操作视频、系统日志和失败记录，如果这些数据能进入世界模型和恢复策略训练，就会形成持续改进的工业具身大脑。

### 2. [VISTA发布UMI-VQA和物理验证管线，让人类采集数据更适合VLA训练](https://arxiv.org/abs/2606.04708)

**摘要：** `VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training` 解决 UMI 数据用于 VLA 训练时的两类错配：腕部鱼眼视角与预训练 VLM 的视觉分布不一致，以及人类采集轨迹可能违反机器人运动学、碰撞或控制带宽约束。VISTA 提供 UMI-VQA 数据集、轨迹连续性 / 自碰撞风险 / 执行保真度评分的物理验证管线，以及视觉语言 grounding 与动作预测的两阶段联合训练。

- **来源：** arXiv
- **核心价值：** 具身大脑的数据不是越多越好，而是要物理可执行。VISTA 把“数据能不能教会机器人”转化为可评分、可筛选、可训练的流程。

---

## 结尾总结

6 月 8 日这期的主线很明确：具身大脑正在从 VLA 扩展为包含世界模型、潜空间推理、可供性理解、闭环评测和全身控制接口的系统工程。

WLA 把世界预测、语言推理和动作合成统一到一个模型中；MPCoT 让 VLA 在潜空间多路径思考；PiL-World、OSCAR 和物流数据飞轮把世界模型推向闭环评测和数据回流；Flash-WAM 解决实时推理；HANDOFF、M3imic 和 MPC-RL 则提醒我们，真正的具身大脑必须接得住底层全身控制。下一阶段，机器人公司的差异化不会只来自一个大模型，而会来自“能预测、能评估、能纠错、能控制”的完整具身系统。

---

> 💬 **互动问题：你认为真正的具身大脑最先应该补齐哪一块能力？世界模型、长时程推理、失败数据闭环、可供性理解，还是全身控制接口？欢迎留言聊聊你的判断。**

---

## 关键词索引

**公司 / 平台：** Unitree G1、WLA-0、RoboTwin2.0、RMBench、RoboArena、LingBot-VA、AffordanceVLA、MPC-RL、M3imic、OSCAR、PiL-World、VISTA  
**技术：** 具身大脑、World-Language-Action、Vision-Language-Action、World-Action Model、世界模型、潜空间推理、可供性预测、闭环评测、数据飞轮、MPC-guided RL、全身控制、跨本体泛化  
**产品 / 数据：** 2B active parameters、40 ms inference、92.94% RoboTwin2.0 Clean、56.5% RMBench、63.2% 到 12.0% 成功率估计误差、23 倍推理加速、8.1 秒到 348 ms、UMI-VQA、WM-DAgger

---

## 值得分享

1. **具身大脑开始从VLA升级到WLA：** WLA-0 同时预测子任务、子目标图像和动作，在 RTX 5090 上实现约 40 ms 推理，并在 RoboTwin2.0 Clean 达到 92.94% 成功率。
2. **世界模型正在成为机器人评测基础设施：** PiL-World 通过闭环 imagined rollout，把 VLA 成功率估计误差从 63.2% 降到 12.0%。
3. **实时性是具身大脑落地的硬门槛：** Flash-WAM 将 World-Action Model 每个 chunk 延迟从 8.1 秒压缩到 348 ms，推动“边想象边行动”接近真实控制周期。

