# 具身智能情报前沿｜2026.03.26

**作者：具身视界**

> 今天最值得看的信号，是具身智能开始同时补齐“端侧模型、工业产能、物理对齐世界模型、开源空间理解”四条线。平台公司在把 VLA 下沉到本地推理，工业巨头在提前扩产，学界在修正 world model 的物理错误，开源社区则把 3D 空间先验做成工具，这说明竞争正在从 demo 转向可部署、可训练、可复制的系统能力。

---

## 🔥 今日最重要的 4 个信号

1. **FANUC America 宣布 9000 万美元扩建美国机器人制造能力，Physical AI 已经开始倒逼产业端提前备产**
2. **ABot-PhysWorld 把“物理可信”写进 14B 世界模型，world model 开始从“像视频”转向“像物理”**
3. **VEGA-3D 开源，把视频生成模型里的空间先验直接拿来做 3D 场景理解与具身决策**
4. **Agile Robots 联手 Google DeepMind，把 Gemini Robotics 接进 2 万套已部署系统，工业具身智能进入数据飞轮阶段**

---

## 📰 行业新闻

### 1. [FANUC America 投资 9000 万美元扩建美国机器人制造能力，工业客户开始为 Physical AI 提前备产](https://www.prnewswire.com/news-releases/fanuc-america-announces-90-million-investment-to-create-production-ready-capacity-for-robot-manufacturing-in-the-us-302722608.html)

**摘要：** 3 月 24 日，FANUC America 宣布将在密歇根投资 9000 万美元，新建约 84 万平方英尺设施，为其在美国扩展机器人制造能力预留“production-ready”空间，项目预计到 2027 年底完工，并新增 225 个岗位。对具身智能行业来说，这条消息的意义并不只是传统工业机器人厂商又扩了一处厂房，而是头部自动化企业已经开始把产能、工程能力和培训体系一起前置，去迎接未来几年对 Physical AI、数字孪生和虚拟调试的需求增长。因为当工业客户真正开始采购更智能、更可适配的机器人系统时，决定交付速度的不会只是模型能力，还包括谁能把制造、集成和服务网络同步铺开。

- **来源：** PR Newswire
- **核心价值：** **工业机器人龙头开始为 AI 驱动自动化提前备产，说明 Physical AI 的竞争正在从软件栈外溢到制造能力和交付能力。**

### 2. [Google DeepMind 推出可本地运行的 Gemini Robotics On-Device，并同步开放机器人 SDK 测试入口](https://www.therobotreport.com/google-deepmind-introduces-on-device-gemini-ai-model-robots/)

**摘要：** 本周，Google DeepMind 推出面向双臂机器人的 `Gemini Robotics On-Device`，主打低算力、本地运行和低时延推理，并同步提供 `Gemini Robotics SDK` 的测试接入方式。公开信息显示，该模型可在无网络或弱网络环境下运行，支持自然语言指令、快速任务适配，并可通过 50 到 100 次示范完成针对特定任务的微调；官方还展示了其从 ALOHA 迁移到 Franka FR3 与 Apptronik Apollo 的能力。对行业而言，这条信息的重要性在于，VLA 终于不再只适合云端演示或高算力实验室，而是开始面向更真实的现场部署条件优化。因为在工厂、仓储和服务场景里，低时延、断网可用和可快速适配，往往比单次 benchmark 分数更决定系统能否上岗。

- **来源：** The Robot Report
- **核心价值：** **机器人基础模型开始把“端侧可运行”作为核心卖点，意味着 VLA 的竞争重心正在从模型展示转向现场部署可行性。**

---

## 📑 前沿论文

### 1. [ABot-PhysWorld：把物理对齐真正写进机器人世界模型](https://arxiv.org/abs/2603.23376)

**摘要：** 3 月 24 日提交到 arXiv 的 `ABot-PhysWorld`，直指当前 video-based world model 最尴尬的短板：画面可以很像，但物理过程常常不对，比如穿模、反重力运动或动作与环境反馈不一致。作者提出一个 14B 的 Diffusion Transformer 世界模型，基于 300 万段带物理感知标注的操作视频训练，并引入基于 DPO 的后训练框架与解耦判别器，在保持视觉质量的同时压制不符合物理规律的生成结果。论文还提出 `EZSbench`，用于评估机器人、任务和场景都未见过时的零样本泛化。它值得关注，不只是因为模型更大，而是因为它开始把“物理可信”当成世界模型的第一公民。对于具身智能来说，这意味着下一阶段 world model 的关键，不是再生成更像真的视频，而是生成足够可信、能用于规划和训练的视频。

- **作者团队：** Yuzhi Chen、Ronghan Chen、Dongjie Huo 等
- **来源：** arXiv
- **核心价值：** **world model 若不能遵守物理规律，就很难真正成为机器人训练和规划的底座；ABot-PhysWorld 代表行业开始正面补这块短板。**

### 2. [SIMART：把静态 3D 网格直接转成可仿真的关节化资产](https://arxiv.org/abs/2603.23386)

**摘要：** 同样在 3 月 24 日提交的 `SIMART`，瞄准的是具身智能训练里经常被忽视、却非常耗工程的一环：高质量、可交互、可仿真的 articulated 3D 资产仍然稀缺。论文提出统一式 MLLM 框架，同时完成部件级拆解和运动学预测，并通过 Sparse 3D VQ-VAE 将 3D token 数量相较密集体素表示压缩约 70%。这让复杂多部件物体的 sim-ready 生成更可扩展，也让从 3D 资产到机器人仿真这条链路更顺。对具身智能研发来说，这类工作很重要，因为很多训练瓶颈并不在控制器本身，而在“有没有足够多、足够真实、可交互的仿真对象”。

- **作者团队：** Chuanrui Zhang、Minghan Qin、Yuang Wang 等
- **来源：** arXiv
- **核心价值：** **如果 sim-ready 资产能更低成本地产生，机器人训练的瓶颈就会从“缺场景”转向“谁能更快组织场景与任务”。**

---

## 💻 开源生态

### 1. [VEGA-3D 开源：把视频生成模型中的空间先验转成 3D 场景理解工具](https://github.com/H-EmbodVis/VEGA-3D)

**摘要：** GitHub 项目 `VEGA-3D` 于 3 月 19 日创建，并在 3 月 20 日放出论文、训练与评测代码，截至目前 Star 已达到 236。项目的核心思路不是继续堆显式 3D 监督，而是把大规模视频生成模型内部已经学到的时空先验提取出来，作为 latent world simulator，为多模态模型补上更强的 3D 场景理解、空间推理与具身决策能力。仓库同时给出了完整训练脚本、评测流程以及所需的模型准备说明，覆盖 `Wan2.1`、`SD2.1`、`V-JEPA V2`、`VGGT` 等多种可选骨干。它值得关注的原因在于，社区正在尝试把“视频生成模型懂空间”这件事，变成能被机器人和具身模型直接复用的工程资产。

- **来源：** GitHub
- **核心价值：** **开源社区正在把视频生成模型的空间先验重新包装成具身工具链，这有机会降低 3D 理解和空间推理的门槛。**

---

## 🏢 机器人公司情报

### 1. [Agile Robots 联手 Google DeepMind：把 Gemini Robotics 接进已部署的工业机器人体系](https://www.prnewswire.com/news-releases/agile-robots-and-google-deepmind-partner-to-bring-intelligence-to-robotics-302723217.html)

**摘要：** 3 月 24 日，Agile Robots 宣布与 Google DeepMind 建立战略研究合作，将把 `Gemini Robotics` 基础模型接入其工业机器人平台。更值得注意的是，这并不是一场停留在实验室层面的“联合发论文”，而是直接绑定到了已有部署基础之上。根据公告，Agile Robots 已在全球安装超过 2 万套机器人解决方案，双方将围绕制造、电子、汽车、数据中心和物流等高价值工业场景，共同推进部署、采数、训练和迭代，形成持续增强的 AI flywheel。对具身智能行业来说，这条信息非常关键，因为它说明头部机器人公司与顶级模型实验室的合作方式，正在从“技术展示”转向“拿真实部署数据换更快模型迭代，再反过来扩大部署”的闭环模式。

- **来源：** PR Newswire
- **核心价值：** **当基础模型进入已有大规模工业机器人网络后，具身智能的真正壁垒会越来越像“部署规模 + 数据回流 + 迭代速度”的组合。**

### 2. [Amazon 收购 Fauna Robotics：消费级 humanoid 再次进入大厂视野](https://techcrunch.com/2026/03/24/amazon-just-bought-a-startup-making-kid-size-humanoid-robots/)

**摘要：** 3 月 24 日，TechCrunch 报道 Amazon 已确认收购成立仅两年的 Fauna Robotics。这家创业公司由前 Meta 和 Google 工程师创立，主打面向家庭场景的儿童体型 humanoid，首款 59 磅双足机器人 `Sprout` 已在今年早些时候向研发合作伙伴小批量发货。更值得注意的是，这是 Amazon 本月确认的第二笔机器人收购，前一笔是楼梯配送机器人公司 Rivr。对行业来说，这说明大厂正在同时押注家庭 humanoid 和末端配送两类 physical AI 路线，背后反映的不是单一产品兴趣，而是平台型公司对“现实世界自动化入口”的系统性布局。

- **来源：** TechCrunch
- **核心价值：** **巨头连续出手机器人并购，说明具身智能正在进入“平台公司主动卡位入口”的阶段，而不再只是创业公司单边冲锋。**

---

## 结尾总结

今天的几条信号串起来，指向同一个趋势：

**具身智能正在从“会不会做 demo”，转向“能不能把模型、产能、数据和仿真一起做厚”。**

FANUC 代表的是工业产能与交付体系正在提前到位，Google DeepMind 与 Agile Robots 代表的是端侧模型和真实部署网络开始形成闭环，ABot-PhysWorld 与 SIMART 则说明学界正在补 world model 物理可信性与 sim-ready 资产两块基础设施短板，而 VEGA-3D 进一步把空间先验工具化。因为当行业进入下一阶段后，真正拉开差距的往往不是单次演示效果，而是**谁能更快把世界模型、开源工具、产业部署和制造能力串成同一条能力生产线**。

---

> 💬 **如果你来判断下一波具身智能赢家，你会更看重端侧模型和世界模型的成熟度，还是更看重制造、部署和数据回流这些更“重”的能力？欢迎留言讨论。**
