# 具身智能情报前沿｜推理与动作开始合流

**作者：具身视界** · 2026.08.13

---

> 今天最值得关注的变化，是具身智能最新趋势正在从“模型会看、会说、会出动作”推进到“推理与动作同流、数据合成规模化、平台开放化、真实场景连续作业”。G0.5、HandEdit、WRC 新整机阵容共同说明，行业正在把机器人能力拆成可训练、可验证、可部署、可迭代的系统工程。

## 💥 今日重磅

### [G0.5：一个自回归流同时输出机器人推理和动作](https://arxiv.org/abs/2608.11739)

**摘要：** 8 月 12 日提交的 G0.5 是今天最值得关注的具身模型进展。论文指出，当前主流 VLA 常把预训练 VLM 和单独训练的 flow-matching action expert 组合起来，结果是 VLM 更像上下文编码器，而不是直接参与决策的机器人“大脑”。G0.5 改用单个 transformer decoder，在统一目标下同时生成 reasoning token 和 action token。它的关键组件包括：可学习的跨本体动作 tokenizer，把异构机器人动作映射到共享词表；原生 chain-of-thought 流，把任务分解、物体 grounding、动作提示与动作 token 交织在一起；视觉记忆模块，通过视觉编码器注入数秒历史。论文称，G0.5 在 7 类独立评测中超过多条基线：R1lite / R1pro 真实机器人微调达到 76.7%，高于 pi0.5 的 53.3% 和 GR00T-N1.7 的 24.4%；2025 BEHAVIOR Challenge 50 个长程家庭移动操作任务达到 31.4%；DROID 后训练后 zero-shot 迁移到未知环境和物体达到 82.5%；LIBERO、RoboTwin 2.0、SimplerEnv-Bridge 分别达到 98.9%、93.3%、87.3%。这条路线的重要性在于，机器人模型不再只是“语言模型理解、动作头执行”的拼接，而是开始让推理和动作在同一个序列空间里共同学习。

- **来源：** arXiv
- **核心价值：** G0.5 把机器人推理、物体 grounding、历史记忆和动作 token 统一到一个自回归流，代表 VLA 从模块拼接向推理-动作一体化演进。
- **行业判断：** 具身模型竞争的最新趋势，是让“大脑”和“动作头”的边界变薄，模型既要会想，也要能把思考直接落到可执行动作。

---

## 📰 行业新闻

### 1. [WRC 整机第四弹：VLOA、PSI 基座模型和长程自主作业进入产品描述](https://www.worldrobotconference.com/news/3579.html)

**摘要：** 8 月 10 日，世界机器人大会发布整机阵容第四弹。机器科学 Rex 轮式仿人形通用机器人提出 Visics 通用具身大模型，采用 VLOA（Vision-Language-Object-Action）架构，强调本体、物体、任务三维泛化；灵初智能 Ψ-SynRobot 搭载 PSI 基座模型，面向复杂物流、零售和工业场景，支持超过 30 分钟连续任务，并具备任务中断后自主恢复能力。产品侧已经开始把模型架构、长程任务和恢复能力写进卖点。

- **来源：** 世界机器人大会官网
- **核心价值：** 最新产业趋势不是单纯展示机器人外形，而是公开说明模型架构、任务时长、恢复能力和场景泛化方式。

### 2. [WRC 整机第五弹：天工 Omni、Monte02、DexForce W1 Pro 指向开放平台和世界模型落地](https://www.worldrobotconference.com/news/3580.html)

**摘要：** 8 月 11 日，世界机器人大会发布整机阵容第五弹。北京人形天工 Omni 被定位为小人形机器人开放平台；源络 Monte02 融合多模态感知、自主决策、精细操作与持续学习能力，可执行跨设备、多步骤任务；跨维智能 DexForce W1 Pro 被描述为实现“AI 引擎-视觉-大脑-本体”全链路自研，并以纯视觉双目与 Sim2Real VLA 架构完成咖啡制作、划火柴、打螺丝等灵巧任务。最新趋势很明确：开放平台、大小脑、世界模型和真实场景正在汇合。

- **来源：** 世界机器人大会官网
- **核心价值：** 具身智能从 Demo 走向产品时，关键会变成开放生态、连续任务、跨设备操作和生成式世界模型驱动的落地能力。

### 3. [RealBot-L2 与 FARMSBOT：数据采集正在嵌入服务、零售和农业场景](https://www.worldrobotconference.com/news/3579.html)

**摘要：** WRC 整机第四弹中，睿尔曼 RealBot-L2 适用于家庭服务、零售引导数据采集等场景，具备 0.3m 升降行程、2.1m 工作范围和升降过程单臂 5kg 负载；THEIMC FARMSBOT 智能农业 AI 机器人系统则通过机器人与传感器采集数据，实时分析作物生长状态、病害风险和成熟度，并自动调控温湿度与光照。数据采集不再只是实验室训练流程，而是在服务、零售、农业等场景中变成产品功能。

- **来源：** 世界机器人大会官网
- **核心价值：** 数据相关报道：具身智能最新发展趋势之一，是把场景数据采集、环境理解和决策调控直接嵌入机器人产品。

---

## 📚 前沿论文

### 1. [HandEdit：2 亿级人手到机器人灵巧手图像编辑基准](https://arxiv.org/abs/2608.12122)

**摘要：** 8 月 12 日提交的 HandEdit 针对灵巧手数据短缺问题，提出面向第一视角人类视频的人手到机器人灵巧手图像编辑数据集和基准。HandEdit 包含超过 2 亿个 editing instances，来自 5 个源数据集，覆盖 26 个 URDF，其中包括 13 种 hand-only 和 13 种 hand-arm 配置；评测分为 Hand-only 与 Hand-Arm 两条 track，并支持 URDF-conditioned evaluation。它的价值在于把人类第一视角视频转成机器人灵巧手可用训练资源的关键中间环节标准化。

- **作者团队：** 复旦大学 / 因时机器人 / 上海交通大学 / 香港大学 / 南洋理工大学 / 上海人工智能实验室等
- **来源：** arXiv
- **核心价值：** 数据相关报道：具身数据生产正在从“采更多真机示教”扩展到“把人类视频编辑成多种机器人本体可用数据”。

### 2. [Policy-Induced Hand Priors：人形双臂 VLA 存在初始姿态诱导的用手偏置](https://arxiv.org/abs/2608.11769)

**摘要：** 8 月 12 日提交的这项研究诊断 VLA 在人形双臂操作中的初始姿态依赖。论文提出 policy-induced hand prior，并用 HandPriorScore、residual hand bias 和 target responsiveness 量化早期用手偏好。多策略、17 种初始配置评估显示，同一初始姿态在不同策略上会产生显著不同成功率，单一策略也会随姿态出现大幅性能波动。扩大训练数据中的初始姿态覆盖能显著提升鲁棒性。

- **作者团队：** Chaeyeon Jung / Juyoun Park
- **来源：** arXiv
- **核心价值：** VLA 真实部署要解决的不只是语言理解，还包括初始关节姿态、腕部视角和训练数据覆盖造成的隐性偏置。

### 3. [Learning Loco-Manipulation：用 SMPC 示教数据训练稀疏奖励 RL](https://arxiv.org/abs/2608.12063)

**摘要：** 8 月 12 日提交的这项工作关注移动操作中的奖励设计瓶颈。论文用 Sample-based Model Predictive Control 在仿真中自动生成大规模离线数据，解决探索问题后，再用纯稀疏任务奖励训练 off-policy RL agent，从而减少手工 dense reward shaping。系统将高层 agent 与低层动态稳定控制器结合，并在带机械臂的 Spot 四足机器人和 G1 人形机器人上部署复杂 loco-manipulation 技能。

- **作者团队：** Martin Schuck / Maks Sorokin / Simone Manni / Duy Ta / Angela P. Schoellig / Marco Hutter / Simon Le Cleac'H / Jan Brudigam
- **来源：** arXiv
- **核心价值：** 具身智能训练趋势正在从手写奖励转向“自动专家数据 + 稀疏奖励 + sim-to-real”组合。

### 4. [HarnessWAM：长程任务要求世界动作模型具备任务图和失败恢复](https://arxiv.org/abs/2608.09516)

**摘要：** 8 月 10 日提交的 HarnessWAM 指出，WAM 的有限时域预测和动作生成不足以处理复杂具身任务，因为机器人还需要全局规划、跨阶段状态维护、执行验证和失败恢复。论文用视觉语言模型 Task Manager 维护场景信念和结构化任务图，并用双时间尺度反馈进行计划推进、观察补充、计划修订和局部恢复。它与 G0.5 共同说明：具身模型正在从短动作输出走向长程任务执行。

- **作者团队：** Zhaopeng Gu / Bingke Zhu / Tianxi Lin / Guibo Zhu / Yingying Chen / Kai Wang / Tingyu Yuan / Chaoyang Zhao / Zhaowen Li / Peng Su / Jinqiao Wang
- **来源：** arXiv
- **核心价值：** 最新模型趋势不是只追求单步动作精度，而是引入任务状态、执行验证和恢复机制。

---

## 💻 开源生态

### 1. [HandEdit 项目页：Code、Dataset、Results 入口已开放](https://handedit.github.io/)

**摘要：** HandEdit 项目页可访问，页面提供 Code、Dataset、Results 和 BibTeX 入口，并展示 EgoDex、ARCTIC、OakInk2、HOI4D、HO-Cap 等来源。项目页将任务定义为在第一视角图像中把可见人手或手臂区域替换为指定机器人灵巧手，同时保持物体状态、任务语义、接触关系、视角和周围场景结构。对开发者来说，这类基准会成为人类视频到机器人数据迁移的基础工具。

- **来源：** 项目主页
- **核心价值：** 具身数据生态正在从数据集发布，升级到数据转换、编辑质量评测和本体条件泛化评估。

### 2. [FluxVLA：VLA 工程平台继续代表数据到真机部署链路](https://github.com/FluxVLA/FluxVLA)

**摘要：** FluxVLA 仓库定位为从数据到真实机器人部署的一站式 VLA 工程平台，覆盖数据、训练、评估、推理和真机部署。放到今天的趋势里看，G0.5 强调推理与动作同流，HandEdit 强调数据转换，FluxVLA 这类平台则负责把模型和数据接到评测、推理和真实设备。具身智能的最新竞争形态，越来越像完整软件栈竞争。

- **来源：** GitHub
- **核心价值：** 模型进步必须落到工程平台，否则很难变成可复现、可对比、可部署的机器人能力。

### 3. [Hy-Embodied-0.5-VLA：真实机器人学习栈仍是大模型落地参照](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA)

**摘要：** 腾讯混元 Hy-Embodied-0.5-VLA 仓库标题显示其定位为从 Vision-Language-Action Models 到真实机器人学习栈，覆盖模型、数据、后训练和部署链路。今天的 G0.5、HandEdit、HarnessWAM 等工作分别推进模型结构、数据生产和任务执行，而 Hy-Embodied 这类项目提醒行业：最终必须把这些能力接成可运行学习栈。

- **来源：** GitHub
- **核心价值：** 最新发展趋势不是单点论文突破，而是模型、数据、训练、评测和真机部署的持续集成。

### 4. [SimWAM：开源世界动作模型补充“训练重、部署轻”路线](https://github.com/H-EmbodVis/SimWAM/)

**摘要：** SimWAM 仓库可访问，项目对应“Simple World Action Model for End-to-End Autonomous Driving”。其论文提出视频生成仅作为训练信号，部署时丢弃视频分支，保留轻量 planner 预测轨迹。尽管它面向自动驾驶，其思想对具身智能仍有参考意义：世界模型可以帮助训练，但执行端要满足低延迟和可部署约束。

- **来源：** GitHub
- **核心价值：** WAM 与 VLA 的共同趋势，是把复杂监督留在训练侧，把可执行策略压到部署侧。

---

## 🏢 机器人公司情报

### 1. [机器科学 Rex：VLOA 架构强调本体、物体、任务三维泛化](https://www.worldrobotconference.com/news/3579.html)

**摘要：** WRC 整机第四弹显示，机器科学 Rex 是全尺寸轮式半人形通用操作机器人，面向商超、物流、工业和家庭场景。其 Visics 通用具身大模型采用 VLOA（Vision-Language-Object-Action）架构，强调实现本体、物体、任务三大维度泛化。这说明具身公司正在从 VLA 扩展到更显式的“物体”与“本体”建模。

- **来源：** 世界机器人大会官网
- **核心价值：** 企业模型架构开始把物体和本体作为独立维度纳入泛化目标，说明通用操作正在走向更细粒度建模。

### 2. [灵初智能 Ψ-SynRobot：30 分钟连续任务和中断恢复成为产品能力](https://www.worldrobotconference.com/news/3579.html)

**摘要：** 灵初智能 Ψ-SynRobot 是轮式双臂通用具身机器人，搭载 PSI 基座模型，面向复杂物流、零售和工业场景。官方信息强调其支持超过 30 分钟连续任务，具备任务中断后自主恢复能力，关节力控带来更安全、更精细操作，并覆盖抓取、放置、搬运、扫码、贴标、分拣、供包和工具使用等技能。

- **来源：** 世界机器人大会官网
- **核心价值：** 最新产业趋势从“单项技能演示”转向“长程连续作业 + 中断恢复 + 多技能工具使用”。

### 3. [北京人形天工 Omni：小人形开放平台瞄准生态建设](https://www.worldrobotconference.com/news/3580.html)

**摘要：** WRC 整机第五弹显示，北京人形机器人创新中心推出天工 Omni，小人形机器人开放平台，定位为面向具身智能未来生态的轻量化创新载体，以开放架构与灵活形态汇聚科研、教育和产业力量。它的信号在于，人形机器人不只向大型整机卷参数，也在向低成本、开放、可教学、可实验的平台扩展。

- **来源：** 世界机器人大会官网
- **核心价值：** 开放平台会降低具身智能研发和教学门槛，推动模型、数据和本体生态扩散。

### 4. [跨维智能 DexForce W1 Pro：AI 引擎、视觉、大脑、本体全链路自研](https://www.worldrobotconference.com/news/3580.html)

**摘要：** WRC 整机第五弹显示，跨维智能 DexForce W1 Pro 是第二代通用人形机器人，官方称其实现“AI 引擎-视觉-大脑-本体”全链路自研，依托纯视觉双目与 Sim2Real VLA 架构，可完成全自主咖啡制作、划火柴、打螺丝等灵巧任务，并以生成式世界模型驱动多场景落地。这类描述反映公司竞争正在从单个部件，转向全链路系统能力。

- **来源：** 世界机器人大会官网
- **核心价值：** 具身智能公司开始把视觉、模型、大脑、本体和世界模型整合成完整技术叙事。

---

## 结尾总结

今天的主线可以概括为：具身智能最新发展趋势正在同时向三处推进。模型侧，G0.5 让推理和动作进入同一自回归流；数据侧，HandEdit 把人类第一视角视频转换为灵巧手训练资源；产品侧，WRC 新整机把开放平台、VLOA、PSI 基座模型、连续任务、中断恢复、大小脑和生成式世界模型写进公开卖点。行业正在从“单点能力演示”进入“模型、数据、平台、场景连续作业”的系统竞争。

---

> 💬 你认为具身智能接下来最值得关注的趋势是什么：推理动作一体化、灵巧手数据合成、长程连续作业、开放小人形平台，还是生成式世界模型落地？

---

## 关键词索引

**公司 / 机构：** 世界机器人大会 / 北京人形机器人创新中心 / 机器科学 / 灵初智能 / 跨维智能 / 源络科技 / 腾讯混元 / FluxVLA / 复旦大学 / 因时机器人 / 上海交通大学 / 上海人工智能实验室

**项目 / 论文：** G0.5 / HandEdit / Policy-Induced Hand Priors / Learning Loco-Manipulation From SMPC Demonstrations / HarnessWAM / FluxVLA / Hy-Embodied-0.5-VLA / SimWAM / 天工 Omni / Rex / Visics / Ψ-SynRobot / PSI / DexForce W1 Pro / Monte02 / RealBot-L2 / FARMSBOT

**技术：** 具身智能 / 最新发展趋势 / VLA / VLOA / WAM / 自回归 VLA / 推理动作一体化 / action token / chain-of-thought / 跨本体动作 tokenizer / 视觉记忆 / 灵巧手 / 数据合成 / 图像编辑基准 / URDF-conditioned evaluation / 长程任务 / 中断恢复 / Sim2Real / 稀疏奖励 RL / 开放平台 / 生成式世界模型 / 真机部署

---

## 值得分享

1. G0.5 用单个 transformer decoder 同时输出 reasoning token 和 action token，在真实机器人微调、BEHAVIOR、LIBERO、RoboTwin 2.0 等多类评测中给出明确增量。
2. HandEdit 提供超过 2 亿个第一视角人手到机器人灵巧手编辑实例，覆盖 26 个 URDF，灵巧手数据生产开始规模化。
3. WRC 最新整机阵容显示，具身产品卖点正在从本体参数转向开放平台、VLOA 架构、基座模型、连续作业、中断恢复和生成式世界模型。
