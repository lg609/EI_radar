# 具身智能情报前沿｜数字遥操作重塑采数

**作者：具身视界** · 2026.07.13

> 今天最值得关注的变化，是具身智能数据采集正在从“人守着真机遥操作”走向“数字遥操作、少标定映射、低疲劳采集和标准化数据格式”。RynnWorld-Teleop 把真实机器人替换为生成式世界模型，AnyDexRT、Smooth Operator、DexVerse 和 LeRobot 生态则共同指向一个趋势：数据采集的瓶颈正在从数量转向质量、可迁移性和可复用格式。

---

## 💥 今日重磅

### [RynnWorld-Teleop：用世界模型做数字遥操作，把采集从真机里解耦出来](https://arxiv.org/abs/2607.06558v1)

**摘要：** 7 月 7 日发布的 RynnWorld-Teleop 提出“数字遥操作”范式：不再让操作者每次绑定某台真实机器人、某个工位和某套硬件，而是用操作者手部姿态流驱动 robot-centric generative world model，从单张参考图生成高保真第一视角视频；记录下来的手部姿态流则作为 embodiment-agnostic action label，经标准 retargeting 转移到目标机器人，从而形成完整 state-action 轨迹。系统结合深度感知骨架条件、human-to-robot 逐步训练的视频 Diffusion Transformer 和 streaming autoregressive distillation，在单张 H100 GPU 上实现 40+ FPS 实时交互生成。论文称，仅用 RynnWorld-Teleop 生成数据训练的策略可在灵巧和双臂任务上实现有效 zero-shot Sim2Real，叠加真实数据后还能稳定提升成功率。它的意义在于把采数成本从“真机时间”转向“世界模型能力”。

- **来源：** arXiv
- **核心价值：** 数据相关报道：如果数字遥操作成立，机器人数据采集会从硬件密集型流程转向可并行、可复用、跨本体的数据生产引擎。

---

## 📰 行业新闻

### 1. [LeRobot 7 月 12 日继续推送：数据采集格式正在成为开发者入口](https://github.com/huggingface/lerobot)

**摘要：** GitHub API 显示，huggingface/lerobot 7 月 12 日仍有推送，星标约 25725。LeRobot README 强调提供真实机器人模型、数据集和工具，并推动硬件无关的 Python 原生接口和标准化 LeRobotDataset 格式。数据采集相关开源项目不断围绕 LeRobot 扩展，说明它正在成为低成本机械臂、遥操作、训练和部署的公共接口。

- **来源：** GitHub API / LeRobot README
- **核心价值：** 数据采集工具链的事实标准一旦形成，后续模型、硬件、质检和可视化工具都会围绕同一格式聚集。

### 2. [Mnesis Canonical Schema：提出具身空间-动作数据的开放标准](https://github.com/Mnesis-Labs/mnesis-canonical)

**摘要：** Mnesis-Labs/mnesis-canonical 7 月 12 日有推送。README 将其定义为 embodied spatial-action data 的开放标准，称为“robot-trainable data 的 USB-C”，并提供 SPEC、Python reference implementation、frame validator、JSONL 读写、示例 episode，以及与 LeRobot columnar layout 互转的能力。

- **来源：** GitHub API / README
- **核心价值：** 数据相关报道：当采集来源扩展到手机、Quest、机器人回放和遥操作时，统一 schema 会决定数据能否进入同一训练和评测流水线。

### 3. [天工 VLA 数据采集工程开源：人形机器人采数开始暴露真实工程细节](https://github.com/Knight1112D/Tienkung_vla_collect_data)

**摘要：** Knight1112D/Tienkung_vla_collect_data 7 月 6 日有推送。README 显示，该工程用于天工 2.0 PRO 的 VLA 数据采集，按固定频率采集三路 RGB 图像、机械臂 command/state、灵巧手 command/state，并最终转换为 LeRobot 数据集。硬件拓扑包括机器人本体、同构遥操作臂、上位机、机器人 x86 控制机、采集 AGX 和相机 AGX；为避免跨设备图像订阅阻塞，稳定流程选择在采集 AGX 本地录制到 `/dev/shm`，再上传回上位机长期保存。

- **来源：** GitHub API / README
- **核心价值：** 真实采数不是一句“遥操作采集”能概括的，它涉及多机同步、相机稳定性、内存盘缓存、上传流程和 LeRobot 格式转换。

---

## 📑 前沿论文

### 1. [AnyDexRT：少量人类指导实现免标定灵巧手重定向](https://arxiv.org/abs/2607.08341v1)

**摘要：** 7 月 9 日发布的 AnyDexRT 面向灵巧手遥操作中的核心环节：把操作者手部动作映射为机器人手可执行、直观的动作。传统方法常依赖手工目标、精确标定或人手/机器人手空间的全局形状匹配，跨不同灵巧手时调参成本高。AnyDexRT 结合自监督指尖对应学习和 few-shot human guidance，并用接触分类器优化 pinch 相关姿态。实验显示，它能在多种灵巧手和真实遥操作任务上提升重定向质量、减少人工调参，并提供更直观高效的控制。

- **作者团队：** Chenxi Wang、Ying Feng、Hongjie Fang、Shangning Xia、Lixin Yang、Chuan Wen、Cewu Lu
- **来源：** arXiv / 项目页
- **核心价值：** 数据相关报道：灵巧操作数据的质量上限取决于重定向质量；少标定、跨手型映射会直接提高多平台采数效率。

### 2. [Smooth Operator：低抖动实时手部重定向降低操作者疲劳](https://arxiv.org/abs/2607.07491v1)

**摘要：** Smooth Operator 指出，VLA 和 Video Action Model 的能力受高质量遥操作数据上限约束，而现有基于梯度的手部重定向方法常陷入不同局部最优，造成抖动，影响数据质量和操作者体验。论文提出 Sampling-Based Retargeter，一种无梯度、低抖动、实时运动学重定向方法，并在 18 名参与者、3 个复杂操作任务中做真实用户研究。相比基线，SBR 达到最高总体任务成功率 54.1%，并取得最低 NASA-TLX 工作负荷分数 36.4/100。

- **作者团队：** Robert Jomar Malate、Erik Bauer、Norica Bacuieti、Stefanos Charalambous、Elvis Nava、Robert K. Katzschmann、Benedek Forrai
- **来源：** arXiv
- **核心价值：** 采集系统不是只看能不能控制机器人，还要看是否稳定、低疲劳、低抖动；否则采到的数据会把人的负担和系统噪声一起写进模型。

### 3. [DexVerse：100 个任务、3 种机械臂、6 种灵巧手，采集 3180 条多模态示范](https://arxiv.org/abs/2607.08751v1)

**摘要：** DexVerse 7 月 9 日发布，定位为多任务、多本体灵巧操作模块化基准。它包含 100 个任务，覆盖抓取搬移、铰接物体交互、工具使用、双手协作、非抓取控制、接触丰富行为、多目标执行和长程任务；支持 3 种机械臂和 6 种灵巧手，并提供 VR 遥操作接口以及 3180 条同步本体感知、RGB、深度、点云和状态观测的示范。

- **作者团队：** Yunchao Yao、Zhuxiu Xu、Tianqi Zhang、Zixian Liu、Sikai Li、Zhenyu Wei、Feng Chen、Dihong Huang、Kechang Wan、Chenyang Ma、Shuqi Zhao、Shenghua Gao、Masayoshi Tomizuka、Yi Ma、Mingyu Ding
- **来源：** arXiv / 项目页
- **核心价值：** 数据相关报道：下一阶段的灵巧操作采集不只是轨迹数量竞争，而是任务覆盖、本体覆盖、视觉变化和多模态同步能力竞争。

### 4. [ABot-C0：四足机器人用 16074 条运动片段构建多源数据金字塔](https://arxiv.org/abs/2607.07370v2)

**摘要：** 7 月 8 日发布的 ABot-C0 技术报告面向四足机器人行为基础模型。论文指出，四足动物动作数据比人类动作更难大规模捕获，跨本体重定向也更脆弱，因此构建了由条件视频生成合成、标注动作捕捉、遥操作和人工设计组成的 multi-source motion-data pipeline，形成 16074 条物理可行动作片段。基于大规模运动数据，Flow-Matching generalist policy 在四足 motion tracking 上表现出随训练规模提升的 scaling law，并具备 zero-shot 跟踪未见动作能力。

- **作者团队：** Xufeng Zhao、Fuzhi Yang、Jianhui Chen、Li Gao、Zhang Meng、Jie Gao、Yao Zheng、Congyang Zhao、Tianxiong Lv、Menglin Yang、Minqi Gu、Yaru Zhao、Wenyu Liu、Honglin Han、Shihui Su、Zixiao Tang、Liu Liu、Mu Xu、Yang Cai、Wenbin Tang
- **来源：** arXiv
- **核心价值：** 数据相关报道：四足具身智能需要把合成、动捕、遥操作和人工设计合成数据金字塔，单一来源很难覆盖产品级行为。

### 5. [VR + LLM 人形遥操作：Apple Vision Pro 记录多模态示范数据](https://arxiv.org/abs/2607.07430v1)

**摘要：** Immersive Social Interaction with VR and LLM-Assisted Humanoids 提出把语音控制移动、VR 操作和双向社交交互整合进人形机器人遥操作。操作者用 Apple Vision Pro 获得第一视角反馈，通过自然语言发出移动命令，并用腕部和手指追踪控制手臂与灵巧手。系统同时记录第一视角 RGB、语音/文本命令、关节状态、手部动作和眼动信号，用于后续模仿学习和自主能力训练；在 Unitree H1 上，初学者完成物体操作成功率 80%、社交递方块成功率 70%。

- **作者团队：** Niraj Pudasaini、Geeta Chandra Raju Bethala、Pranav Doma、Anthony Tzes、Yi Fang
- **来源：** arXiv
- **核心价值：** 数据采集会越来越多模态：眼动、语音、第一视角、关节和手部动作一起记录，才能支撑更自然的人形机器人交互学习。

---

## 💻 开源生态

### 1. [lerobot-xense：把触觉相机、多机器人和多遥操作器接入 LeRobot](https://github.com/Vertax42/lerobot-xense)

**摘要：** Vertax42/lerobot-xense 7 月 12 日有推送，星标约 17。README 显示，该仓库是 XenseRobotics 基于 LeRobot 的分支，用于 multimodal tactile data acquisition system，并在 upstream LeRobot v5.1 上叠加 Flexiv Rizon4 RT、Elite CS66 RT、ARX5、Franka Research3、TacCap tactile grippers，以及 Pico4 VR、双 SpaceMouse、Vive tracker、TRLC leader、gamepad 等遥操作器。

- **来源：** GitHub API / README
- **核心价值：** 数据相关报道：具身数据采集正在从 RGB + 关节状态，扩展到触觉、VR、多品牌机械臂和多种遥操作入口的组合系统。

### 2. [Almond Axol SDK：双臂机器人开放 VR 遥操作、ZED 相机和 LeRobot 绑定](https://github.com/almond-bot/axol)

**摘要：** almond-bot/axol 7 月 11 日有推送，星标约 19。README 显示，它是 Almond Axol 双臂机器人的 CLI 和 Python SDK，包含双臂 IK solver、底层 CAN motor interface、VR teleoperation pipeline、ZED camera streaming、LeRobot bindings 和 joint tuning toolkit；网页前端包括 WebXR VR 遥操作、浏览器控制面板和电机诊断仪表盘。

- **来源：** GitHub API / README
- **核心价值：** 双臂采数平台正在把遥操作、相机流、运动控制、诊断和 LeRobot 数据绑定做成 SDK，而不是零散脚本。

### 3. [SO101-Nexus：低成本 SO-101 从示范到策略的一体化工具链](https://github.com/johnsutor/so101-nexus)

**摘要：** johnsutor/so101-nexus 7 月 12 日有推送，星标约 20。README 将其定义为 SO-101 robot learning, from demos to policies，组合实体 leader-arm teleoperation、LeRobot-compatible dataset recording、Gymnasium/MuJoCo manipulation environments、模仿学习和强化学习流程。它反映出低成本机械臂采集正在向“从示范到策略”的全链条工具转变。

- **来源：** GitHub API / README
- **核心价值：** 低成本采数硬件只有接上数据记录、仿真环境和训练策略，才会真正降低具身智能入门门槛。

### 4. [LeRobot Recorder Web：面向触屏设备的本地采集控制台](https://github.com/nomorewzx/lerobot-record-webui)

**摘要：** nomorewzx/lerobot-record-webui 7 月 11 日有推送。README 显示，这是面向 Rock 5B+ 和 10 英寸 HDMI 触屏的本地控制器，用于管理 `lerobot-record`。它支持编辑机器人、串口、相机、数据集、时长和编码配置；提供本地数据集发现、resume metadata 检查、带确认的本地删除、独立 recorder worker、Unix-socket IPC，以及 15 FPS MJPEG 浏览器预览。

- **来源：** GitHub API / README
- **核心价值：** 采集效率不仅来自算法，也来自现场操作界面；触屏控制台能减少键盘依赖和误操作，让边缘设备上的采数更接近生产流程。

---

## 🏢 机器人公司情报

### 1. [XenseRobotics：围绕触觉数据采集扩展 LeRobot 生态](https://github.com/Vertax42/lerobot-xense)

**摘要：** XenseRobotics 的 lerobot-xense 把多款机械臂、触觉夹爪和多种遥操作器叠加到 LeRobot 上，说明具身智能公司正在把“采集硬件 + 传感器 + 数据格式 + 训练工具”组合成平台。触觉数据尤其重要，因为接触丰富任务中，纯视觉很难稳定判断滑移、压力和接触状态。

- **来源：** GitHub API / README
- **核心价值：** 数据相关报道：触觉采集会成为灵巧操作和工业装配数据闭环的重要差异化入口。

### 2. [Almond：Axol SDK 把双臂机器人采数能力做成开发者工具](https://github.com/almond-bot/axol)

**摘要：** Almond Axol SDK 提供一键安装、WebXR VR 遥操作、浏览器控制、诊断仪表盘、ZED 相机数据流和 LeRobot 绑定。相比单纯发布双臂硬件，这类 SDK 更接近开发者平台：用户可以从遥操作、调参、采集、诊断直接进入模型训练流程。

- **来源：** GitHub API / README
- **核心价值：** 双臂机器人公司如果想获得开发者生态，必须把采集体验和数据接口做成产品能力，而不是只开放机械结构。

### 3. [Hugging Face：LeRobot 成为数据采集工具的公共底座](https://github.com/huggingface/lerobot)

**摘要：** 近期多个仓库围绕 LeRobot 扩展采集、记录、可视化、格式标准和硬件接口，说明 Hugging Face 的机器人生态正在从训练库变成数据层入口。对整机厂和创业团队来说，接入 LeRobotDataset 意味着数据更容易上传、共享、训练、质检和复用。

- **来源：** GitHub API / LeRobot README
- **核心价值：** 当数据格式成为公共底座，平台方会影响采集工具、模型训练和硬件适配的事实标准。

---

## 结尾总结

7 月 13 日的主线可以概括为：具身智能数据采集正在从“真机遥操作堆轨迹”升级为“数字生成、低抖动重定向、多本体基准、多模态同步和标准格式”的系统工程。RynnWorld-Teleop 试图用世界模型释放真机资源，AnyDexRT 和 Smooth Operator 改善人手到机器人手的映射质量，DexVerse 和 ABot-C0 则证明高质量数据集必须覆盖任务、本体、传感器和行为来源。下一阶段，谁能更稳定地生产可迁移、可验证、可复用的数据，谁就更接近具身模型的规模化训练入口。

---

> 💬 你认为机器人数据采集最先被重塑的环节会是哪一个：数字遥操作、灵巧手重定向、触觉采集、数据格式标准，还是现场采集控制台？

---

## 关键词索引

**公司：** Hugging Face / XenseRobotics / Almond / Unitree / Rynn Labs / Mnesis Labs / Tiangong
**技术：** 具身智能数据采集 / 数字遥操作 / 世界模型 / 视频 Diffusion Transformer / 遥操作重定向 / 灵巧手 / 触觉数据 / LeRobotDataset / 多模态同步 / VR 遥操作 / 数据 schema / Sim2Real
**项目 / 数据：** RynnWorld-Teleop / AnyDexRT / Smooth Operator / DexVerse / ABot-C0 / LeRobot / Mnesis Canonical Schema / Tienkung VLA Collect Data / lerobot-xense / Almond Axol SDK / SO101-Nexus / LeRobot Recorder Web

---

## 值得分享

1. 数据采集开始脱离真机束缚：RynnWorld-Teleop 用世界模型实现 40+ FPS 数字遥操作，并生成可训练 state-action 轨迹。
2. 灵巧手采数的关键是重定向质量：AnyDexRT 减少标定和调参，Smooth Operator 用低抖动方法降低操作者疲劳。
3. 采集工具链正在标准化：LeRobot、Mnesis Canonical Schema、天工 VLA 工程和触屏采集控制台都在把数据变成可复用资产。
