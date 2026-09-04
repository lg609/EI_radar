# 具身智能情报前沿｜开源模型进入推理栈竞争

**作者：具身视界** · 2026.08.07

---

> 今天最值得关注的变化，是具身开源模型的竞争正在从“谁开放一个模型”转向“谁能把 VLA、WAM 和机器人策略稳定跑在云端、边缘和本体上”。PhyAI、MiniWorld、Track4Action、Teleopit 等近期工作共同说明，开源生态的下一步重点是运行时、训练栈、示教数据和部署效率。

## 💥 今日重磅

### [PhyAI：一个运行时覆盖 VLA、WAM、云端 rollout 和本体部署](https://arxiv.org/abs/2608.03682)

**摘要：** 8 月 4 日提交的 PhyAI 把具身开源模型生态的一个关键问题摆到台前：同一个机器人策略 checkpoint，在模型评估、云端强化学习 rollout、边缘 GPU serving 和本体部署中，往往需要不同推理程序，导致开发者反复适配。PhyAI 提出面向 Physical AI 的统一推理引擎，把架构相关的 conditioning、solver、cache 和输出逻辑放进 model adapters，把图执行、kernel、内存管理和并行服务抽成共享运行时。论文称同一套代码可运行 VLA 和 WAM，支持单卡、多卡、本体、边缘和云端部署，并已适配 pi0、pi0.5、GR00T N1.7、MiniCPM-Robot 等模型；相对官方实现获得 1.40 倍至 4.65 倍加速。它的意义不只是又多了一个开源仓库，而是说明具身开源模型正在进入“模型、运行时、benchmark、硬件部署”一体化竞争。

- **来源：** arXiv
- **核心价值：** 具身开源模型要真正可用，关键不只是开放权重和代码，还要有统一、低延迟、可扩展的推理运行时。
- **行业判断：** 下一阶段开源具身生态会从“模型榜单”转向“谁能让模型在真实控制周期里稳定执行”。

---

## 📰 行业新闻

### 1. [世界机器人大会整机预告：开放、轻量、易部署成为机器人平台关键词](https://www.worldrobotconference.com/news/3240.html)

**摘要：** 8 月 4 日，世界机器人大会发布“机器人整机阵容第一弹”。其中，星尘智能 Astribot T1 被描述为以“更开放、更轻量、更易部署”为核心理念的新一代绳驱机器人平台，支持多样末端配置、自主回充和软硬件扩展接口，面向科研教学、展厅导览、零售服务和快速场景落地。对开源模型生态来说，这类硬件平台的价值在于降低模型部署和二次开发门槛。

- **来源：** 世界机器人大会官网
- **核心价值：** 开源模型需要可复用硬件平台承接，否则模型能力很难从论文和仓库进入真实场景。

### 2. [世界机器人大会消费街预告：机器人 4S 店和 C 端体验给模型落地提供展示窗口](https://www.worldrobotconference.com/news/3241.html)

**摘要：** 8 月 5 日，世界机器人大会发布机器人消费街预告，提到第二届“E-TOWN 机器人消费节”将在大会同期举办，并设置 Robot-Mall 机器人 4S 店、产品创新展示厅、智能厨站、机器人售货员、机器人乐队等体验内容。虽然这不是开源模型发布，但它给产业侧一个信号：开源模型最终要进入可体验、可交互、可演示的机器人产品和服务，而不是停留在离线 benchmark。

- **来源：** 世界机器人大会官网
- **核心价值：** 开源具身模型的商业化检验，会发生在真实交互、连续服务和用户体验中。

### 3. [PhyAI GitHub：Physical AI 推理引擎仓库已开放，包含 benchmark 和多模型目录](https://github.com/mingti-org/phyai)

**摘要：** PhyAI 的 GitHub 仓库可访问，页面显示其定位为面向 Physical AI 的 latency-first serving engine，目录包含 benchmark、docker、docs、examples、phyai-kernel、phyai-model-optimizer 等模块。仓库页面显示 73 stars、19 forks，并在 README 中强调支持 VLA、WAM 以及云端 serving 和设备端部署。对开发者而言，这类仓库比单个论文 PDF 更重要，因为它决定模型能否被复现、接入、剖析和优化。

- **来源：** GitHub
- **核心价值：** 开源模型生态正在把“仓库工程质量”变成竞争要素，benchmark、kernel、adapter 和部署文档会直接影响采用率。

---

## 📚 前沿论文

### 1. [MiniWorld：从零训练视频世界模型的开源训练栈](https://arxiv.org/abs/2608.01127)

**摘要：** 8 月 2 日提交的 MiniWorld 关注视频世界模型从零训练的可复现性。论文认为，视频世界模型能根据历史观测和控制信号预测未来观测，是具身智能和交互式仿真的基础，但现有路线常依赖复杂后训练和大量算力。MiniWorld 提供 block-causal Video Diffusion Transformer、Flow Matching、滚动 KV cache 和流水线异步去噪，并称可在单台 8-GPU 服务器上数天内训练。

- **作者团队：** Yian Zhao / Ruochong Zheng / Hongcan Guo / Yu Yan / Jian Zhang / Jie Chen
- **来源：** arXiv
- **核心价值：** 开源世界模型训练栈会降低研究门槛，让更多团队能复现实验、改训练流程和做具身仿真。

### 2. [Teleopit：96 条成功示教训练 ACT 和 GR00T N1.7](https://arxiv.org/abs/2608.01834)

**摘要：** 8 月 3 日提交的 Teleopit 面向人形机器人全身遥操作和示教数据采集。系统把 VR 中的身体、手和头部信号映射到人形机器人、可配置灵巧手和 2-DoF 主动视觉模块，并通过历史编码器、failure-aware rewind sampling 和手部重定向提升跟踪质量。论文报告，用 Teleopit 收集的 96 条成功示教训练 ACT 和 GR00T N1.7 后，在人形机器人部署中分别达到 90.0% 和 95.0% 任务成功率。

- **作者团队：** Bingqian Wu / Zicheng Xu / Xianghui Fan / Dayu Li / Xiangru Huang
- **来源：** arXiv
- **核心价值：** 数据相关报道：开源模型要提升真机表现，仍然离不开高质量全身示教数据和可复用遥操作系统。

### 3. [LiLa-WAM：单张 24GB GPU 上训练轻量世界动作模型](https://arxiv.org/abs/2608.03701)

**摘要：** 8 月 4 日提交的 LiLa-WAM 面向 WAM 训练成本。论文认为，现有世界动作模型常在像素空间或多阶段 latent 空间中承担较高计算开销，不利于中小团队训练。LiLa-WAM 在紧凑 latent 空间中同时塑造未来状态预测和动作生成，并提出 Visual Transition Token 作为语言无关任务表示。论文称该模型可在单张 24GB GPU 上端到端训练，在 RoboTwin 2.0 的 50 个任务上达到 90.48% 成功率。

- **作者团队：** Fan Yang / Yuting Su / Xiaobo Wang / Yuncheng You / Fugui Fan / Yuting Wu 等
- **来源：** arXiv
- **核心价值：** 轻量 WAM 会让开源具身模型从“大机构可训练”走向“更多实验室可验证”。

### 4. [Faster-WAM：单层动作头降低世界动作模型推理延迟](https://arxiv.org/abs/2608.02365)

**摘要：** 8 月 3 日提交的 Faster-WAM 关注 WAM 中动作模块是否必须很深。论文提出 Dock of Transformer，把预训练视频 Transformer 作为 representation hub，用 docking interface 接入轻量输出头；Faster-WAM 将单层动作头接到 30 层视频 backbone 上。论文称无需额外 embodied pretraining，就能在 LIBERO 和 RoboTwin 2.0 上保持竞争表现，并实现 66.5 ms 推理延迟，相比 Fast-WAM 加速 3.2 倍。

- **作者团队：** Liheng Ma / Rui Heng Yang / Zhanguang Zhang / Mateo Clemente / Ziwen Hu / Tongtong Cao / Yingxue Zhang
- **来源：** arXiv
- **核心价值：** 开源 WAM 的部署瓶颈不只在模型大小，也在动作头设计、延迟和硬件适配。

### 5. [GSR：小模型也能提升 VLA 指令泛化](https://arxiv.org/abs/2608.02497)

**摘要：** 8 月 3 日提交的 Grounded Semantic Re-Binding 研究 VLA 对指令改写的脆弱性。论文认为问题根源不是语义理解缺失，而是动态视觉和文本联合编码导致动作策略对特征漂移敏感。GSR 通过独立提取任务语义并与视觉特征显式融合，重新训练 action expert。论文称在 LIBERO-Para 上成功率最高提升 44.6 个百分点，并提出 0.33B 参数 ParaVLA，在指令重写鲁棒性上接近完美。

- **作者团队：** Zhaokai Yin / Zhipeng Zhang
- **来源：** arXiv
- **核心价值：** 开源模型不一定只能靠堆参数提升泛化，结构设计和语义绑定也能显著改善真实指令鲁棒性。

---

## 💻 开源生态

### 1. [PhyAI 仓库：VLA/WAM 统一推理引擎进入开发者视野](https://github.com/mingti-org/phyai)

**摘要：** PhyAI 仓库将 Physical AI 推理拆成 adapter、kernel、model optimizer、benchmark、examples 等模块，目标是让不同 VLA/WAM 使用同一套底层执行、内存管理和并行服务能力。它适合关注开源模型部署的团队跟进：当模型生态越来越多，统一运行时会降低测试、上线和跨硬件迁移成本。

- **来源：** GitHub
- **核心价值：** 开源模型生态的基础设施化，正在从训练代码扩展到高性能推理和部署运行时。

### 2. [MiniWorld GitHub：视频世界模型训练代码仓库可访问](https://github.com/zhao-yian/MiniWorld)

**摘要：** MiniWorld 论文关联 GitHub 仓库可访问，仓库描述为“Democratizing the Training of Video World Models from Scratch”。结合论文看，它提供的是视频世界模型训练与推理的可复现入口，而不是只发布结果图。对具身开发者来说，世界模型训练栈会成为未来 VLA/WAM 研究的重要公共底座。

- **来源：** GitHub / arXiv
- **核心价值：** 世界模型如果有可复现代码和 checkpoint，才可能成为开源机器人模型生态的通用组件。

### 3. [Track4Action 项目页：提供 Paper、Checkpoints、Demo 和 Code 入口](https://wing0night.github.io/track4action-project-page)

**摘要：** Track4Action 项目页显示其提供 Paper、Checkpoints、Demo 和 Code 入口。该方法把 world-centric 3D tracker 的几何、运动、可见性和相机信息作为训练时监督，让 VLA 部署时不依赖 tracker。对开源生态而言，它提供了一个方向：用更强的离线视觉/3D 模型增强 VLA 训练，而不增加部署时推理负担。

- **来源：** 项目主页
- **核心价值：** 开源模型训练可以借助 privileged supervision 提升能力，同时保持部署图简洁。

### 4. [Teleopit 项目页：全身遥操作、灵巧手和主动视觉示例可查看](https://botrunner64.github.io/teleopit-page)

**摘要：** Teleopit 项目页展示全身控制、灵巧手控制、移动抓取、开门、货架取物、VLA policy rollout 等视频入口。它对开源模型社区的价值在于补齐数据侧工具：如果没有可复用的全身遥操作和示教采集系统，ACT、GR00T N1.7 这类开放模型很难持续获得高质量真机数据。

- **来源：** 项目主页
- **核心价值：** 开源模型生态需要数据采集工具链，否则模型迭代会被示教数据质量卡住。

---

## 🏢 机器人公司情报

### 1. [NVIDIA Isaac GR00T：近期论文中的重要被适配对象](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** NVIDIA Isaac-GR00T GitHub 仓库可访问，仓库标题显示其为 “NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots”。近期 PhyAI、Teleopit、piR2 等工作都把 GR00T N1.7 作为适配、训练或加速对象，说明 GR00T 已经不只是单个模型发布，而是在被外部研究者放进推理运行时、遥操作数据和实时控制实验中检验。

- **来源：** GitHub / arXiv（背景参照，近期增量来自 PhyAI、Teleopit、piR2 等论文）
- **核心价值：** 开源基础模型的影响力，最终要看是否被第三方系统持续适配和复用。

### 2. [Physical Intelligence openpi：pi0/pi0.5 成为近期 VLA 研究基座](https://github.com/Physical-Intelligence/openpi)

**摘要：** Physical Intelligence 的 openpi 仓库可访问，页面显示其 GitHub 热度较高。近期 PhyAI、Faster-WAM、DRIFT、GSR 等论文频繁以 pi0 或 pi0.5 为研究对象，覆盖推理加速、世界动作模型、安全攻击、语义泛化等方向。这说明开源 VLA 生态正在形成“基础策略 + 外围改进 + 部署优化”的研究分工。

- **来源：** GitHub / arXiv（背景参照，近期增量来自 PhyAI、Faster-WAM、DRIFT、GSR 等论文）
- **核心价值：** 当一个开源 VLA 被大量论文复用，它就从模型变成了研究基础设施。

### 3. [Hugging Face LeRobot：机器人 AI 开源工具链的背景参照](https://github.com/huggingface/lerobot)

**摘要：** Hugging Face LeRobot 仓库可访问，仓库描述为 “Making AI for Robotics more accessible with end-to-end learning”。虽然 LeRobot 不是今天新发布，但它仍是观察机器人 AI 开源工具链的重要入口。放到今天的主线里看，PhyAI 解决推理运行时，MiniWorld 提供世界模型训练栈，LeRobot 则代表数据、策略训练和教育型工具链的社区底座。

- **来源：** GitHub（背景参照）
- **核心价值：** 开源具身生态需要多层工具协同：数据、训练、模型、推理、部署缺一不可。

---

## 结尾总结

今天的主线可以概括为：具身开源模型正在从“模型开放”进入“系统开放”。PhyAI 把 VLA、WAM、云端 rollout、边缘 serving 和本体部署接到同一运行时；MiniWorld、Track4Action、Teleopit 则分别补上世界模型训练、3D 监督和示教数据工具链。开源生态的下一个分水岭，不是仓库数量，而是模型能否被第三方稳定复现、加速、部署和持续采数。

---

> 💬 你认为具身开源模型生态最缺的环节是什么：高质量权重、统一推理运行时、真机数据、仿真评测，还是低成本本体平台？

---

## 关键词索引

**公司 / 机构：** PhyAI / NVIDIA / Physical Intelligence / Hugging Face / 世界机器人大会 / 星尘智能 / Carnegie Mellon University / 上海交通大学 / 浙江大学

**项目 / 论文：** PhyAI / MiniWorld / Track4Action / Teleopit / LiLa-WAM / Faster-WAM / GSR / ParaVLA / Isaac GR00T N1.7 / openpi / LeRobot / pi0 / pi0.5 / MiniCPM-Robot

**技术：** 具身智能 / 开源模型 / VLA / WAM / Physical AI / 推理运行时 / 云边端部署 / edge serving / onboard deployment / world model / action model / GR00T / pi0 / pi0.5 / ACT / 遥操作数据 / 示教数据 / 3D tracker / 低延迟推理 / 模型适配器 / benchmark

---

## 值得分享

1. PhyAI 把 pi0、pi0.5、GR00T N1.7、MiniCPM-Robot 等模型放进统一推理运行时，开源竞争开始转向部署栈。
2. Teleopit 用 96 条成功示教训练 ACT 和 GR00T N1.7，在人形机器人上报告 90.0% 和 95.0% 任务成功率。
3. 具身开源模型下一步不只比权重开放，更要比谁能稳定采数、训练、推理、加速并跑上真实机器人。
