# 具身智能情报前沿｜失败样本成为机器人训练入口

**作者：具身视界** · 2026.08.02

---

> 今天最值得关注的变化，是机器人基础模型开始把“失败”当成训练资产，而不是演示中的异常噪声。Google Gemini Robotics 建立在 Gemini 2.0 多模态能力之上，推动行业关注物理世界执行；近 7 天的新论文则进一步说明，真正能落地的机器人系统必须会发现高风险状态、修正动作、压低延迟，并把失败数据回流到下一轮训练。

## 💥 今日重磅

### [Self-Evolving Learning：用失败风险模型主动筛选具身智能训练数据](https://arxiv.org/abs/2607.28251)

**摘要：** 7 月 30 日提交的 Self-Evolving Learning for Embodied AI with Criticality Model 直接瞄准机器人策略微调中的一个常见问题：默认数据采集流程往往随机收集样本，结果训练集被大量正常场景占满，真正能提升系统鲁棒性的稀有失败案例反而不足。论文提出 state-wise criticality model，根据策略自身执行结果预测未来失败概率，再把采样重点转向高风险、失败易发的状态，并用重要性权重重采样训练数据。实验覆盖四足运动、多任务操作、VLA 基准和真实机器人任务，报告相对已训练基线失败率下降 51% 至 67%，相对现有 VLA 方法下降 8% 至 25%。这条工作的重要性在于，它把“机器人哪里会失败”变成可建模、可采样、可回流的数据闭环；对 Gemini Robotics 这类通用机器人基础模型而言，规模化部署不可能只靠成功样本堆出来，必须让系统主动盯住高风险边界。

- **来源：** arXiv
- **核心价值：** 数据相关报道：失败样本开始成为高价值训练数据，具身智能的数据闭环正在从“多收集”转向“有目的地收集关键失败”。
- **行业判断：** 机器人基础模型下一步竞争的关键，不只是能做多少任务，而是能否持续识别自己最容易失败的地方。

---

## 📰 行业新闻

### 1. [Google Gemini Robotics 2.0 路线：可验证公开资料指向 Gemini 2.0 基座，而非独立“Robotics 2”版本](https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/)

**摘要：** Google DeepMind 官方资料显示，Gemini Robotics 是建立在 Gemini 2.0 之上的机器人模型家族，目标是把多模态理解、空间推理和动作控制带入物理世界；可验证的后续论文则是 Gemini Robotics 1.5，而不是一个独立命名的 “Gemini Robotics 2” 正式版本。把这条路线放到今天看，它的真正行业含义是：机器人基础模型已经从“看懂和说清楚”进入“能否安全、稳定、可泛化地执行动作”的阶段。

- **来源：** Google DeepMind
- **核心价值：** 对 Google Gemini Robotics 2 相关说法，当前更严谨的表达是“基于 Gemini 2.0 的 Gemini Robotics 路线”；这条路线正在推动行业把部署可靠性作为核心指标。

### 2. [Gemini Robotics 论文：从 Gemini 2.0 扩展到直接控制机器人](https://arxiv.org/abs/2503.20020)

**摘要：** Gemini Robotics 论文介绍的模型家族包括直接控制机器人的 VLA 模型，以及面向空间、时间和物理场景理解的 Gemini Robotics-ER。论文强调，模型可以处理开放词汇指令、未见物体和环境变化，并讨论长程灵巧任务、少量示范学习和新本体适配。虽然该论文不是近 7 天新发布，但它是理解今天 VLA 自我修正、失败采样和端侧执行工作的背景坐标。

- **来源：** arXiv
- **核心价值：** 背景参照：Gemini 2.0 机器人路线把“多模态模型”推向“物理动作系统”，因此执行时校验、失败回流和实时部署会越来越重要。

### 3. [世界机器人大会：场景数据采集和多模态训练继续进入商业化议程](https://www.worldrobotconference.com/news/3233.html)

**摘要：** 世界机器人大会 7 月 29 日发布的同期活动预告显示，“场景破局—机器人商业化落地的探索与实践”明确把场景数据采集、运动模型构建、多模态训练迭代和本体整机适配放进讨论。与今天的失败采样和执行修正论文合在一起看，商业落地不再是单个 demo 的问题，而是场景数据、失败诊断、模型迭代和本体适配能否形成闭环。

- **来源：** 世界机器人大会官网
- **核心价值：** 商业化场景会倒逼机器人公司披露更真实的失败处理能力，而不只是展示成功片段。

---

## 📚 前沿论文

### 1. [DLAM：从无动作视频中学习分布式 latent action](https://arxiv.org/abs/2607.27138)

**摘要：** 7 月 29 日提交的 DLAM 针对 VLA 缺少动作标注数据的问题。论文认为，大量无动作视频包含物理变化先验，但现有 latent action 方法容易在递归组合时积累误差。DLAM 将每个视觉转移表示为对角高斯分布，并通过等间隔三元组约束组合和反转关系，再把编码器冻结后用于 flow-matching 策略联合生成 latent transition 和机器人动作。

- **作者团队：** Zuojin Tang / Feifan Luo / Haoyun Liu / Botai Yuan 等
- **来源：** arXiv
- **核心价值：** 数据相关报道：如果无动作视频能稳定转成可用的动作先验，机器人训练数据来源会从遥操作扩展到更大规模的物理视频。

### 2. [FutureRTC：让 VLA 在异步执行中提前预测未来观测](https://arxiv.org/abs/2607.24008)

**摘要：** 7 月 27 日提交的 FutureRTC 面向 VLA 实时部署中的异步执行问题。机器人在执行当前 action chunk 时，下一段动作往往已经并行计算，导致预测输入和真实执行时状态错位。FutureRTC 通过状态校正模块和观测预测模块，利用机器人运动作为物理先验预测执行时视觉表征，并在仿真和真实环境中提升对推理延迟的鲁棒性。

- **作者团队：** Hai Jiang / Yixian Zou / Binbin Liang / Boqian Liu 等
- **来源：** arXiv
- **核心价值：** 端侧机器人不是只要模型准确，还要能在延迟和异步控制下保持轨迹连续。

### 3. [IDR：测试时动态判断视觉信息对 VLA 动作的因果作用](https://arxiv.org/abs/2607.25516)

**摘要：** 7 月 28 日提交的 IDR 框架关注 VLA 多模态融合。机器人在远距离移动和近距离接触阶段，对视觉、语言和本体状态的依赖并不相同。IDR 通过事实与反事实视觉观测推断动作，诊断视觉观测的动态因果重要性，再以训练无关方式修正动作预测。论文称该方法可接入多种 VLA 架构，并在仿真和真实任务中提升整体表现。

- **作者团队：** Haoyu Zhang / Yuwei Wu / Jin Chen / Gao Zhi 等
- **来源：** arXiv
- **核心价值：** 具身模型要想可靠执行，不能固定相信某一种模态，而要按任务阶段动态判断信息来源是否有效。

### 4. [VQVLA：动作状态感知量化加速 VLA 推理](https://arxiv.org/abs/2607.24148)

**摘要：** 7 月 27 日提交的 VQVLA 提出算法硬件协同框架，用 motion-aware vector quantization 根据机器人执行状态动态调整量化精度，并通过 centroid reuse 减少冗余乘法。论文报告，VQVLA 相比 A100 GPU、Dadu-Corki、LUT-DLA、CodeGEMM 和 ShiftAddLLM 分别取得 6.5 倍、2.8 倍、1.9 倍、3.3 倍和 4.3 倍加速，同时精度损失可忽略。

- **作者团队：** Zhuoran Song / Haozhe Jiang / Chunyu Qi / Minnan Pei 等
- **来源：** arXiv
- **核心价值：** Gemini Robotics On-Device 代表端侧趋势，VLA 加速则是让机器人在真实控制周期内行动的基础工程。

### 5. [Cross-Embodiment Transfer：用行为对齐表示提升跨本体迁移](https://arxiv.org/abs/2607.27549)

**摘要：** 7 月 30 日提交的 Cross-Embodiment Transfer 研究如何让 VLA 更好利用多种机器人本体的数据。论文比较物体框、语言动作、末端执行器轨迹等行为对齐表示，发现末端执行器轨迹对跨本体迁移尤其有帮助，并能利用 action-free data。实验显示，该方法在仿真到真实跨本体迁移中将真实机器人策略任务完成进度提升 28%。

- **作者团队：** Ajay Sridhar / Jensen Gao / Jonathan Yang / Jean Mercat 等
- **来源：** arXiv
- **核心价值：** 通用机器人模型要跨本体复用数据，必须找到比关节坐标更抽象、又和动作结果强相关的行为表示。

---

## 💻 开源生态

### 1. [FutureRTC 项目页：实时 VLA 异步执行方案开放展示](https://jianghaiscu.github.io/FutureRTC_proj/)

**摘要：** FutureRTC 项目页展示了 anticipatory-conditioned action chunking 的方法示意和实验结果。对开发者来说，这类项目的价值在于把“模型推理慢”拆成控制系统问题：机器人不是等模型算完才动，而是在执行、预测、校正之间并行运行。

- **来源：** 项目主页
- **核心价值：** 实时 VLA 的工程难点正在从模型结构延伸到执行调度、状态预测和控制连续性。

### 2. [BARX 项目页：跨本体行为对齐表示可查看](https://ajaysridhar.com/barx/)

**摘要：** Cross-Embodiment Transfer 关联项目页开放视频示例，展示不同本体间如何借助行为对齐表示迁移策略。它适合关注多机器人数据复用的团队跟进：如果一个模型要同时服务机械臂、人形、移动双臂平台，数据不能只停留在某一台机器人的关节空间。

- **来源：** 项目主页
- **核心价值：** 跨本体迁移会影响数据资产复用效率，也会影响机器人公司能否把同一套模型扩展到多条产品线。

### 3. [ARCHITECT 项目页：用程序合成和人类纠错构建可解释技能库](https://robo-architect.github.io/)

**摘要：** 7 月 26 日提交的 ARCHITECT 把机器人策略获取视为交互式程序合成任务，用 LLM coding agent 生成模块化机器人程序，并让人类通过自然语言纠正失败。系统把纠错信息落到执行轨迹和代码层，再蒸馏进持久技能库，在 Franka Panda 长程任务上优于多种 VLA 和程序合成基线。

- **来源：** 项目主页 / arXiv
- **核心价值：** 当黑盒 VLA 难以解释失败时，程序化技能库提供了另一条可调试、可复用、可累积的路线。

---

## 🏢 机器人公司情报

### 1. [Google DeepMind：Gemini Robotics On-Device 强调本地机器人设备](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

**摘要：** Google DeepMind 的 Gemini Robotics On-Device 把机器人基础模型从云端能力进一步推向本地设备。对机器人公司而言，这意味着低延迟、隐私、离线可靠性和硬件适配不再是附加项，而是产品化前提。今天的 VQVLA、FutureRTC 和 IDR 都在补同一块短板：模型必须在真实控制周期内可靠运行。

- **来源：** Google DeepMind
- **核心价值：** 端侧部署会重排机器人基础模型竞争：谁能在有限算力下稳定行动，谁才更接近产品。

### 2. [Google DeepMind：Gemini Robotics 1.5 把“思考后行动”写进机器人模型路线](https://arxiv.org/abs/2510.03342)

**摘要：** Gemini Robotics 1.5 报告强调多本体 VLA、Motion Transfer 和内在推理过程，让机器人在复杂多步任务中“先思考再行动”。放到今天看，Self-Evolving Learning、FutureRTC、IDR 和 Cross-Embodiment Transfer 都是在回答后续问题：模型思考之后，如何在执行中发现偏差、应对延迟、融合模态并迁移到新本体。

- **来源：** arXiv
- **核心价值：** 背景参照：具身智能体不只是会规划，还要能把规划转成可靠执行，并在失败边界上持续改进。

### 3. [北京人形机器人创新中心：具身智能应用活动将发布大小脑和场景方案](https://www.worldrobotconference.com/news/3233.html)

**摘要：** 世界机器人大会预告显示，北京人形机器人创新中心主办的具身智能应用创新主题活动，将围绕从技术突破到产业应用、敏捷运动与多感知操作、灯塔工厂选型逻辑等议题展开，并计划发布具身智能“最强大小脑”、Omni、搬运分拣解决方案和计量检测方案。

- **来源：** 世界机器人大会官网
- **核心价值：** 国内产业侧正在把大小脑、场景方案和客户验证放到一起，说明基础模型路线最终要落到具体工艺和流程。

---

## 结尾总结

8 月 2 日的主线可以概括为：机器人基础模型正在从“展示能力”进入“处理失败”的阶段。Google Gemini Robotics 的 Gemini 2.0 路线提供了物理世界智能的参照，但近期更值得看的增量，是 Self-Evolving Learning、FutureRTC、IDR、VQVLA 和跨本体迁移这些工作正在把失败采样、执行校正、端侧加速和数据复用做成系统能力。

---

> 💬 你认为机器人走向真实部署时，最应该优先公开哪类指标：成功率、失败恢复率、端侧延迟、跨本体迁移效果，还是现场数据回流能力？

---

## 关键词索引

**公司 / 机构：** Google DeepMind / 世界机器人大会 / 北京人形机器人创新中心

**项目 / 论文：** Gemini Robotics / Gemini Robotics On-Device / Gemini Robotics 1.5 / Self-Evolving Learning / DLAM / FutureRTC / IDR / VQVLA / Cross-Embodiment Transfer / BARX / ARCHITECT

**技术：** 具身智能 / Gemini 2.0 / 机器人基础模型 / VLA / 失败样本 / criticality model / 数据闭环 / 动作级修正 / 异步执行 / 端侧推理 / 多模态因果适配 / 跨本体迁移 / 行为对齐表示

---

## 值得分享

1. Google Gemini Robotics 可验证公开资料指向“基于 Gemini 2.0 的机器人路线”，目前未见独立正式版本名叫 Gemini Robotics 2。
2. Self-Evolving Learning 用失败风险模型主动筛选训练数据，在多类任务中报告失败率相对基线下降 51% 至 67%。
3. 机器人基础模型要走向产品，必须同时解决失败数据回流、实时执行、端侧推理和跨本体迁移。
