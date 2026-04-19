# 具身智能情报前沿｜2026.03.27

**作者：具身视界**

> 今天最值得看的信号，是具身智能的竞争正从“谁先做出 demo”转向“谁先建成数据飞轮、物理可信模型、开源空间工具和产业部署网络”。数据采集、世界模型、3D 先验和真实工厂落地，正在同时变成下一阶段的核心底座。

---

## 🔥 今日最重要的 4 个信号

1. **Universal Robots 联手 Scale AI，把训练数据采集直接搬到 10 万台工业机器人部署网络前面**
2. **ABot-PhysWorld 用 300 万段操作视频和新基准 EZSbench，把“物理可信”抬成世界模型新门槛**
3. **VEGA-3D 开源，开始把视频生成模型里的隐式 3D 先验做成具身可复用工具**
4. **AI2 Robotics 完成 12 亿元人民币 B 轮融资，轮式人形路线开始把产能扩张和场景复用写进增长逻辑**

---

## 📰 行业新闻

### 1. [Universal Robots 联手 Scale AI 推出 UR AI Trainer，工业机器人训练开始进入“同机采数、同机部署”阶段](https://www.prnewswire.com/apac/news-releases/universal-robots-and-scale-ai-launch-imitation-learning-system-to-accelerate-ai-model-training-bridging-the-lab-to-factory-gap-302717348.html)

**摘要：** 3 月 19 日，Universal Robots 与 Scale AI 在 GTC 2026 上发布 `UR AI Trainer`。这套系统最关键的地方，不是再做一个示教 demo，而是把高保真、同步化的机器人与视觉数据采集，直接放到真实工业机器人硬件上完成。官方强调，它可基于 UR 的力控与力反馈能力，在 leader-follower 架构下实时记录多模态演示数据，并运行在 `AI Accelerator` 平台上，用于训练 VLA 模型；更值得注意的是，UR 明确提到其底座来自全球超过 10 万台已部署 cobot 网络，且双方计划在年内发布大规模工业数据集。对具身智能行业来说，这是一条非常典型的**数据基础设施**信号，因为它把“实验室采数据、工厂再重做一遍”的割裂流程，往“同一套硬件采、训、部署、回流”的闭环推进。因为谁能先把数据采集嵌进生产环境，谁就更可能先建立稳定的物理 AI 迭代飞轮。

- **来源：** PR Newswire
- **核心价值：** **具身智能下一阶段的护城河，不只是模型大小，而是谁先掌握真实工业环境里的持续采数与回流能力。**

### 2. [FANUC America 投资 9000 万美元扩建美国机器人制造能力，Physical AI 开始反向拉动产能准备](https://www.prnewswire.com/news-releases/fanuc-america-announces-90-million-investment-to-create-production-ready-capacity-for-robot-manufacturing-in-the-us-302722608.html)

**摘要：** 3 月 24 日，FANUC America 宣布将在密歇根投资 9000 万美元，新建约 84 万平方英尺设施，项目预计 2027 年底完成，并新增 225 个岗位。公告特别提到，这一扩产将服务北美市场对 physical AI、虚拟调试和数字孪生相关自动化需求的增长。对行业而言，这意味着传统工业机器人龙头已经不再把 AI 视为远期概念，而是在制造、培训和交付网络上提前卡位。

- **来源：** PR Newswire
- **核心价值：** **当工业机器人龙头为 Physical AI 提前扩产时，行业竞争就已经从模型栈外溢到制造与交付体系。**

---

## 📑 前沿论文

### 1. [ABot-PhysWorld：把物理对齐真正写进机器人世界模型](https://arxiv.org/abs/2603.23376)

**摘要：** 3 月 24 日提交到 arXiv 的 `ABot-PhysWorld`，直指当前 video-based world model 最核心的短板：视觉上像真，不代表物理上可信。论文提出一个 14B 的 Diffusion Transformer 世界模型，基于 300 万段带物理感知标注的操作视频训练，并引入基于 DPO 的后训练框架与解耦判别器，目标是在保持视觉质量的同时压制穿模、反重力和动作错位等不符合物理规律的生成结果。作者还同步提出 `EZSbench`，用来评估未见机器人、未见任务和未见场景组合下的 embodied zero-shot 泛化。它值得重点看，不只是因为参数更大，而是因为它第一次把“物理可信”和“动作对齐”分开评测。因为如果世界模型未来要承担规划、仿真和训练数据生成，它就不能只是会生成好看的视频，而必须生成能被机器人真正相信的视频。

- **作者团队：** Yuzhi Chen、Ronghan Chen、Dongjie Huo 等
- **来源：** arXiv
- **核心价值：** **world model 的下一道门槛不再只是视觉逼真度，而是能否成为可规划、可训练、可评测的物理世界代理。**

### 2. [SIMART：把静态 3D 网格直接转成可仿真的关节化资产](https://arxiv.org/abs/2603.23386)

**摘要：** 同样在 3 月 24 日提交的 `SIMART`，聚焦的是具身智能训练里一个很“基础设施”的问题：可交互、可仿真的 articulated 3D 资产仍然稀缺。论文提出统一式 MLLM 框架，同时完成部件级拆解与运动学预测，并通过 Sparse 3D VQ-VAE 将 3D token 数量相对密集体素表示压缩约 70%，从而提高复杂多部件物体的 sim-ready 生成效率。

- **作者团队：** Chuanrui Zhang、Minghan Qin、Yuang Wang 等
- **来源：** arXiv
- **核心价值：** **如果 sim-ready 资产生成更便宜，机器人训练的瓶颈就会从“缺对象”转向“谁更快组织场景与任务”。**

---

## 💻 开源生态

### 1. [VEGA-3D 开源：把视频生成模型里的隐式空间先验转成场景理解与具身决策工具](https://github.com/H-EmbodVis/VEGA-3D)

**摘要：** 对应论文 `Generation Models Know Space` 于 3 月 19 日提交 arXiv，官方代码仓库 `VEGA-3D` 已公开，目前 GitHub Star 超过 250。项目的核心思路不是继续依赖昂贵的显式 3D 监督，而是把预训练视频扩散模型内部已经学到的时空结构先验提取出来，作为 `Latent World Simulator`，再与多模态大模型做自适应融合，用于 3D 场景理解、空间推理和 embodied manipulation 基准。它值得关注，是因为社区开始把“生成模型其实懂空间”这件事，从论文判断变成可复用工程工具。因为一旦这类隐式 3D 先验能稳定迁移到具身任务，空间理解的门槛就可能明显下降。

- **来源：** GitHub
- **核心价值：** **开源社区正在把视频生成模型的空间能力重新包装成具身工具链，这会直接影响 3D 理解和空间推理的普及速度。**

---

## 🏢 机器人公司情报

### 1. [AI2 Robotics 完成 12 亿元人民币 B 轮融资：轮式人形公司开始把 VLA、量产和行业落地一起往前推](https://www.therobotreport.com/ai2-robotics-raises-series-b-funding-advance-alphabot-embodied-ai/)

**摘要：** The Robot Report 本周披露，深圳具身智能公司 `AI2 Robotics` 完成 12 亿元人民币 B 轮融资，估值升至约 100 亿元人民币。公司表示，这笔资金将继续推进具身 AI 模型与 `AlphaBot` 系列轮式人形机器人，并计划把年产能从 2025 年的 1000 台提升到 2026 年的 1 万台。更值得注意的是，这家公司强调自己的路线不是单纯做展示型 humanoid，而是围绕零售、公共服务、生物科技、汽车和半导体制造等场景，把自研 `GOVLA` 模型、硬件平台和商业部署一起推进；报道还提到，其方法论强调“data closed-loop + scenario compounding”。这条信息值得保留，是因为它反映出新一批具身公司已经开始用“模型、量产、场景复用”三件事同时讲增长逻辑，而不再只讲单机能力。

- **来源：** The Robot Report
- **核心价值：** **当轮式人形公司开始同步扩模型、扩产能、扩场景时，具身智能公司的竞争标准就从“能不能做出来”转向“能不能批量交付并快速复制”。**

### 2. [Amazon 收购 Fauna Robotics：家庭 humanoid 再次进入大厂长期布局清单](https://techcrunch.com/2026/03/24/amazon-just-bought-a-startup-making-kid-size-humanoid-robots/)

**摘要：** 3 月 24 日，TechCrunch 报道 Amazon 已确认收购成立两年的 Fauna Robotics。Fauna 由前 Meta 和 Google 工程师创立，主打家用儿童体型 humanoid，首款 59 磅双足机器人 `Sprout` 已在今年早些时候向研发合作伙伴小批量发货。这也是 Amazon 本月确认的第二笔机器人收购，前一笔是楼梯配送机器人公司 Rivr，说明其正在同时押注家庭与配送两类 physical AI 入口。

- **来源：** TechCrunch
- **核心价值：** **平台型公司连续并购机器人团队，说明具身智能正在从创业公司赛道，进入大厂提前卡位入口的阶段。**

---

## 结尾总结

今天的几条信号串起来，指向同一个趋势：

**具身智能正在从“拼模型演示”，转向“拼数据闭环、物理可信、开源工具和部署网络”。**

Universal Robots 与 Scale AI 代表的是训练数据基础设施开始贴近真实工厂，ABot-PhysWorld 和 SIMART 说明学界正在补物理可信世界模型与 sim-ready 资产两层底座，VEGA-3D 则把视频生成模型的空间先验工具化，而 Agile Robots 与 Google DeepMind 的合作进一步证明，真实部署网络正在成为模型迭代的关键燃料。因为当行业进入下一阶段后，真正拉开差距的往往不是谁先做出惊艳 demo，而是**谁能更快把数据、模型、仿真和部署压成同一条能力生产线**。

---

> 💬 **如果你来判断下一波具身智能赢家，你会更看重世界模型和 VLA 本身，还是更看重真实部署网络带来的数据飞轮？欢迎留言讨论。**
