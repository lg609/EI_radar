# 具身智能情报前沿｜头部企业从 Demo 走向部署闭环

**作者：具身视界** · 2026.06.29

> 明天最值得关注的变化，是具身智能头部企业正在从“展示机器人能力”转向“证明部署闭环”。Agility 用上市计划、Digit v5 订单和真实运行小时数验证商业化；1X 把世界模型实验室升级为公司战略；Figure 用 Helix 物流版量化吞吐、数据筛选和跨机迁移；NVIDIA、NEURA、智元、宇树则分别从平台、训练场、开放数据和参考本体补齐生态基础设施。

---

## 今日重磅

### [Agility Robotics 拟通过 SPAC 上市：Digit v5 超 3 亿美元订单，把人形机器人推向资本市场验证](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility Robotics 6 月 24 日宣布将与 Churchill Capital Corp XI 合并上市，交易给予公司约 25 亿美元 pre-money 股权价值，预计带来超过 6.2 亿美元总收益，其中约 2 亿美元来自 PIPE。更关键的是，Agility 披露 Digit 已在 Schaeffler、GXO、Toyota Motor Manufacturing Canada、Mercado Libre 等客户环境中运行，累计超过 65,000 小时，并已为下一代 Digit v5 获得超过 3 亿美元多年订单。相比许多还停留在展台演示的人形机器人公司，Agility 正在用客户、订单、工厂和真实工时证明“类人形态 + 仓储 / 制造任务”可以被资本市场按商业公司定价。公司还提到 RoboFab 目标支持最高 10,000 台年产能，Digit v5 强调 AI-enabled cooperatively safe，即与人同场协作的安全能力。这件事的重要性在于，人形机器人第一次越来越接近“以订单和产能讲故事”的阶段；受影响的不只是整机厂，还包括执行器、传感器、安全系统、云端调度、维护服务和场景集成商。

- **来源：** Agility Robotics 官方公告
- **核心价值：** 头部企业竞争正在从“谁的演示更像未来”转向“谁能交付、运行、维护并获得多年订单”。Agility 的上市计划把人形机器人商业化从技术叙事推进到资本市场和规模制造叙事。

---

## 行业新闻

### 1. [1X World Model Lab：头部人形企业把“世界模型 + 数据闭环”写进组织架构](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X 宣布成立 World Model Lab，专注于面向全自主 humanoid 的 embodied world model pretraining，并任命 Sam Sinha 负责世界模型方向。1X 给出的数据配方包括 web-scale media、egocentric human videos、simulation、dexterous remote operated robot data 和 on-policy NEO data，再通过真实部署继续收集机器人数据并用于 RL。

- **来源：** 1X Technologies
- **核心价值：** 这是今天的数据相关报道。1X 的信号很明确：头部人形公司不只是在做硬件，而是在围绕真实 fleet 构建数据、预训练、部署回流和强化学习闭环。

### 2. [Figure Helix 物流版：用 8 小时高质量示范、60% 吞吐提升证明 VLA 商业化指标](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure 将 Helix VLA 扩展到物流包裹处理场景，要求机器人处理刚性箱子、柔性袋子、不同尺寸重量包裹，并把标签转向可扫描方向。Figure 披露，仅 8 小时高质量示范数据即可训练出可用策略；立体视觉相对非立体基线吞吐提升 60%；高质量数据在少三分之一数据量时仍带来 40% 更高吞吐；learned visual proprioception 支持跨机器人迁移。

- **来源：** Figure AI
- **核心价值：** Figure 正在把 VLA 从“泛化演示”推向“可计算 ROI 的物流任务”。吞吐、数据质量、自校准和跨机迁移，会成为头部企业比拼的硬指标。

### 3. [NVIDIA Isaac GR00T：头部平台公司用模型、仿真、数据和部署工具链绑定人形生态](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA Isaac GR00T 覆盖开放数据与数据管线、开放机器人基础模型、Omniverse / Cosmos 仿真框架、中间件、CUDA-X 加速库和 Jetson Thor 实时推理控制。GR00T 模型面向通用人形机器人，可接受语言、图像等多模态输入，并通过 post-training 适配不同本体、任务和环境。

- **来源：** NVIDIA Developer
- **核心价值：** NVIDIA 的打法不是只卖芯片，而是把具身智能的训练、仿真、模型、部署和硬件加速整合成平台。头部企业如果不能接入这类生态，研发效率和开发者吸引力都会受到影响。

### 4. [NEURA Robotics：Neuraverse 与 NEURA Gyms 把每次部署变成 Physical AI 数据回流](https://neura-robotics.com/neura-robotics-showcases-full-stack-robotics-platform-at-automate-2026/)

**摘要：** NEURA Robotics 在 Automate 2026 前披露 Neuraverse 平台和 NEURA Gyms 训练环境，强调 Physical AI 必须在真实世界训练、验证和持续改进。Neuraverse 连接机器人、开发者和产业伙伴，每一次机器人部署都会贡献到不断增长的 physical intelligence 池；NEURA Gyms 则把真实训练设施和高保真仿真结合起来，用于工业部署前验证用例。

- **来源：** NEURA Robotics
- **核心价值：** NEURA 代表了欧洲头部企业的“部署即训练场”路线。对客户来说，价值不只是买一台机器人，而是接入一个会随部署不断变聪明的物理智能网络。

### 5. [智元机器人：从 VivaTech、印尼 APC 到 AGIBOT WORLD，国内头部企业同时推进出海和开放数据](https://www.agibot.com/news)

**摘要：** 智元机器人近期在巴黎 VivaTech 展示“三智合一”架构和多款人形 / 服务机器人，在印尼 APC 2026 Indonesia 推出 RaaS 模式，并发布 AGIBOT WORLD 2026 Theme 2：Rich Interaction 数据集，记录抓取失败、碰撞、掉落、不稳定接触和液体飞溅等真实物理交互事件。

- **来源：** 智元机器人官方新闻
- **核心价值：** 智元的动作说明国内头部企业正在双线推进：海外市场用 RaaS 和本地伙伴降低部署门槛，技术生态用开放真实失败数据争夺开发者和研究者入口。

---

## 前沿论文

### 1. [ABC-130K：Amazon FAR、UC Berkeley、MIT 等发布 3,553 小时双臂操作开放栈](https://arxiv.org/abs/2606.27375)

**摘要：** `Scalable Behavior Cloning with Open Data, Training, and Evaluation` 发布 ABC 全栈，核心数据集 ABC-130K 包含 134,806 条双臂遥操作轨迹、3,553 小时真实交互、195 个任务；同时开放硬件方案、训练基础设施、MuJoCo 仿真管线、400 小时 sim-teleop 数据和超过 100 小时真实评测日志。团队比较 DiT 与 VLA 架构，并证明仿真评测与真实表现相关性较高，task progress 相关系数 r=0.91。

- **作者团队：** UC Berkeley、MIT、Amazon FAR、XDOF、CMU 等
- **来源：** arXiv / ABC 项目页
- **核心价值：** 头部企业和顶级机构正在把操作数据、训练和评测做成开放基础设施。Amazon FAR 参与说明，双臂操作数据栈与仓储、包装、分拣等商业场景高度相关。

### 2. [OmniAct：长期自治机器人需要规划、记忆、验证和物理执行的分层运行时框架](https://arxiv.org/abs/2606.27251)

**摘要：** `OmniAct` 面向长期日常物理自治，提出分层异步架构：multimodal semantic planner 负责 cyber / physical unified action space 中的技能路由，adaptive hierarchical memory 用事件边界压缩控制上下文增长，asynchronous visual preemption engine 在 VLA 执行过程中持续监测视觉状态并在失败前打断。实验覆盖两个机器人平台、四个 IoT 设备和 40 个真实长程任务，并在累计超过 100k 交互 tokens 时保持近似平坦的 token 消耗。

- **作者团队：** 复旦大学、上海人工智能实验室等
- **来源：** arXiv
- **核心价值：** 对头部企业来说，长期自治不会由单个 VLA 解决，而需要类似机器人“操作系统”的运行时框架，把工具调用、IoT、导航、操作、记忆和失败恢复统一起来。

### 3. [RouterVLA：用 34,752 条预部署 rollout 做策略路由，让多 VLA 系统比单模型更稳](https://arxiv.org/abs/2606.27355)

**摘要：** `RouterVLA` 研究如何把机器人部署前 smoke tests 转化为 VLA policy selection 监督。论文在 34,752 条 LIBERO-Plus rollout records 上构建 outcome-disjoint cross-fitting：一部分试运行用于建立冻结专家 profile，另一部分单独评分所选专家，避免复用同一试验导致虚高。透明 probe-success 规则将 held-out success 从 0.4686 提升到 0.6149，增益 14.64 个百分点。

- **作者团队：** Xingyu Ren、Chugang Yi、Ge Ma、Youran Sun
- **来源：** arXiv
- **核心价值：** 头部企业未来可能不会只部署一个“全能模型”，而是部署模型组合和路由器。RouterVLA 把部署前验收测试变成系统能力，适合真实客户现场的多策略选择。

### 4. [REGEN：世界动作模型生成伪回放，减少持续学习中的灾难性遗忘](https://arxiv.org/abs/2606.27374)

**摘要：** `World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays` 提出 REGEN，利用 World Action Models 生成 future visual observations 的能力，在连续模仿学习中合成 pseudo-replay trajectories，让机器人学习新任务时无需保存原始人类示范也能复习旧任务。仿真和真实操作实验显示，REGEN 相比顺序微调最多减少 50% 灾难性遗忘，并接近使用真实 replay data 的 privileged experience replay。

- **作者团队：** Manish Kumar Govind、Dominick Reilly、Smit Patel、Hieu Le、Srijan Das
- **来源：** arXiv
- **核心价值：** 头部机器人公司一旦有大量客户数据，就必须处理隐私、存储和持续学习问题。REGEN 为“少存原始数据、仍能持续学习”提供了技术路径。

### 5. [MMBench2：世界模型幻觉可预测、可补数据，50 条轨迹即可适应未见任务](https://arxiv.org/abs/2606.27326)

**摘要：** MMBench2 包含 427 小时、210 任务、10 个 domain，配有 ground-truth actions、rewards 和 live simulators。研究训练 350M 参数世界模型，识别 perceptual、action-marginalized、scene-diverging 三类幻觉，并用无标签预测信号定位低覆盖区域。针对未见任务，基于幻觉信号的 curiosity 数据采集每任务只需 50 条轨迹，就能接近专家 / 人类采集效果的 90%。

- **作者团队：** Nicklas Hansen、Xiaolong Wang
- **来源：** arXiv / 项目页
- **核心价值：** 世界模型是头部企业的战略方向，但可靠性取决于覆盖诊断和补数据能力。MMBench2 把“模型会不会瞎想”变成可测、可修的工程问题。

### 6. [OctoSense：59 小时八传感器同步数据，补齐头部机器人公司的鲁棒感知底座](https://arxiv.org/abs/2606.27317)

**摘要：** `OctoSense` 发布开放传感平台与数据集，覆盖 stereo RGB、event camera、LiDAR、thermal、IMU、RTK GPS、CAN / 关节本体感知等八类同步传感器，共 59 小时、2,474 公里数据。其 late-fusion masked autoencoder 在深度、光流、语义分割、ego-motion 上优于图像基础模型，尤其在夜间和传感退化场景优势更明显。

- **作者团队：** University of Pennsylvania、Brown University
- **来源：** arXiv / 项目页
- **核心价值：** 头部企业要进入工厂、园区、户外、夜间和康养场景，不能只依赖 RGB。多传感器同步、标定、压缩和自监督表征会成为真实部署的感知基础设施。

---

## 开源生态

### 1. [NVIDIA Isaac GR00T 开放模型与工具链：人形基础模型生态的统一入口](https://github.com/NVIDIA/Isaac-GR00T)

**摘要：** Isaac GR00T GitHub 仓库提供人形机器人基础模型和相关工具链入口，官方生态覆盖开放数据、数据管线、仿真、训练、部署和 Jetson Thor 实时控制。对硬件公司而言，适配 GR00T 生态意味着更容易进入全球研究者和开发者网络。

- **来源：** GitHub / NVIDIA Developer
- **核心价值：** 头部平台的价值在于把碎片化模型和工具收敛到标准接口。GR00T 正在成为人形机器人基础模型与硬件本体之间的重要连接层。

### 2. [ABC 代码、数据和评测日志开放：双臂操作从论文结果变成可复现实验底座](https://github.com/amazon-far/abc)

**摘要：** ABC 项目开放训练代码、仿真管线、硬件设置和真实评测日志，并在 Hugging Face 发布 ABC-130K 数据。其 abcdl 分布式 dataloader 将 episode 编码为 MP4 堆叠相机视角加二进制 state/action 文件，并通过 keyframe 编码优化随机访问，解决千小时级机器人数据训练中的 I/O 压力。

- **来源：** GitHub / ABC 项目页
- **核心价值：** 对头部企业和创业公司来说，数据加载、评测日志和真实 rollout 记录会越来越像“基础设施资产”，而不是论文附属品。

### 3. [AGIBOT WORLD Rich Interaction 开放：国内头部公司把失败、碰撞和液体飞溅数据推向社区](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)

**摘要：** 智元 AGIBOT WORLD 2026 Theme 2 已在 Hugging Face 开放，聚焦真实世界接触丰富交互，记录抓取失败、碰撞、掉落、不稳定接触、液体飞溅等事件。这类数据面向世界模型、神经仿真器、物理感知表征和鲁棒表示学习。

- **来源：** Hugging Face / 智元机器人
- **核心价值：** 国内头部企业不再只展示成功动作，而是开放失败数据。谁能系统记录真实物理世界的“糟糕情况”，谁就更接近长期部署所需的鲁棒性。

### 4. [OctoSense 开放硬件与数据：多传感器机器人感知开始社区化](https://github.com/anthonytec2/OctoSense)

**摘要：** OctoSense 开放机械 CAD、传感器安装、同步电路、采集处理工具和数据集。数据每 5 秒窗口生成 caption，并用 Qwen3 embedding 建立 FAISS + BM25 检索索引，可按自然语言查询“wet road at night”“police vehicle”等片段。

- **来源：** GitHub / Hugging Face / 项目页
- **核心价值：** 机器人公司要积累场景数据，不能只靠文件夹存视频。可检索、可同步、可标定、可复用的数据平台，正在成为感知基础设施的标配。

---

## 机器人公司情报

### 1. [Agility Robotics：Digit v5 订单、RoboFab 产能和上市融资构成商业化三件套](https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi)

**摘要：** Agility 披露 Digit 已累计超过 65,000 小时真实运行，下一代 Digit v5 获得超过 3 亿美元多年订单，RoboFab 目标支持最高 10,000 台年产能。公司表示上市交易资金将用于履行订单、扩大部署、提升产能，并继续投资 Physical AI、软件、安全系统和制造基础设施。

- **来源：** Agility Robotics
- **核心价值：** Agility 是当前最接近“人形机器人规模商业化叙事”的海外公司之一。其核心看点不只是机器人会走会搬，而是订单、工厂、真实运行小时数和安全协作体系。

### 2. [Figure AI：Helix 从家庭操作扩展到物流吞吐，商业化路径更聚焦](https://www.figure.ai/news/helix-logistics)

**摘要：** Figure 的 Helix 最初展示自然语言驱动的家庭物品抓取和双机器人协作，近期进一步扩展到物流包裹分拣。物流版强调 implicit stereo vision、multi-scale visual representation、learned visual proprioception 和 Sport Mode，并用 8 小时高质量示范、60% 吞吐提升等指标呈现工程进展。

- **来源：** Figure AI
- **核心价值：** Figure 正在用物流场景反向打磨 VLA。相比家庭全场景，物流更容易计算 ROI，也更适合通过吞吐、误抓率、跨机迁移和数据质量衡量模型价值。

### 3. [1X Technologies：NEO 的长期竞争力越来越依赖世界模型和在策略数据](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X 认为通用人形机器人不是简单 fine-tuning 问题，而是需要从一开始就在关键物理世界数据上预训练。World Model Lab 将围绕数据整理、预训练、机器人学习、评估、部署和真实机器人在策略数据采集构建完整闭环。

- **来源：** 1X Technologies
- **核心价值：** 1X 的护城河不只是 NEO 本体，而是 NEO fleet 带来的真实数据和世界模型学习系统。人形机器人公司正在变成数据公司。

### 4. [NVIDIA：从芯片供应商升级为人形机器人基础设施平台](https://developer.nvidia.com/isaac/gr00t)

**摘要：** NVIDIA GR00T 生态列出多家 humanoid robotics ecosystem 成员，并用 Omniverse、Cosmos、Isaac Lab、CUDA-X、Jetson Thor 和 DGX Cloud 等工具覆盖训练、仿真和部署。其目标不是只发布一个模型，而是成为机器人基础模型和硬件部署的统一底座。

- **来源：** NVIDIA Developer
- **核心价值：** NVIDIA 在机器人领域的角色越来越像 AI 基础设施平台：用模型牵引工具链，用工具链牵引硬件，用硬件绑定开发者和机器人公司。

### 5. [宇树科技：H2 Plus 成为 NVIDIA Isaac GR00T 参考人形平台，国内硬件进入全球模型生态](https://www.unitree.com/news/40)

**摘要：** 宇树科技宣布 H2 Plus 成为 NVIDIA Isaac GR00T Reference Humanoid Robot for Academic Research，面向学术研究开放。H2 Plus 基于宇树 H2 人形机器人产品线，进入 NVIDIA 人形机器人生态。

- **来源：** Unitree Robotics
- **核心价值：** 对国内头部硬件公司来说，成为全球基础模型平台的参考本体，比单纯销售机器人更有长期生态价值。它会带来研究者、开源项目和工具链适配的复利。

---

## 结尾总结

6 月 29 日这期聚焦头部企业，可以看到一个清晰变化：具身智能行业正在从“谁的 demo 更震撼”转向“谁的闭环更完整”。Agility 用订单、工时和上市路径证明商业化；Figure 用物流吞吐和数据筛选证明 VLA 能进入 ROI 场景；1X 把世界模型和在策略数据变成公司战略；NVIDIA 用 GR00T 争夺平台入口；智元和宇树则代表国内公司在出海、开源数据和参考本体上加速卡位。

未来头部企业的竞争不会只发生在机器人外形或模型参数上，而会发生在五个闭环里：**数据闭环、部署闭环、评测闭环、供应链闭环和生态闭环。** 谁能把真实客户、真实工时、真实失败、真实数据回流和可扩展工具链接起来，谁才更接近具身智能规模化。

---

> 💬 在 Agility、Figure、1X、NVIDIA、智元、宇树这些头部玩家里，你更看好哪家公司率先跑通可规模化商业闭环？欢迎留言讨论。

---

## 关键词索引

**公司：** Agility Robotics、Figure AI、1X Technologies、NVIDIA、NEURA Robotics、智元机器人、宇树科技、Amazon FAR、XDOF、Schaeffler、GXO、Toyota Motor Manufacturing Canada、Mercado Libre  
**技术：** VLA、World Model、World Action Model、Physical AI、Helix、Isaac GR00T、ABC-130K、OmniAct、RouterVLA、REGEN、MMBench2、OctoSense、DAgger、sim-to-real、在策略数据、数据闭环、RaaS  
**产品：** Digit v5、RoboFab、NEO、H2 Plus、Jetson Thor、Omniverse、Cosmos、Neuraverse、NEURA Gyms、AGIBOT WORLD 2026 Theme 2

---

## 值得分享

1. **人形机器人开始接受资本市场和订单验证：** Agility 拟以约 25 亿美元估值上市，Digit 已超 65,000 小时真实运行，Digit v5 获超 3 亿美元多年订单。
2. **头部公司越来越像数据公司：** 1X 把世界模型数据配方写进组织架构，Figure 用 8 小时高质量示范验证物流 VLA，智元开放真实失败数据。
3. **平台生态正在重塑人形机器人格局：** NVIDIA GR00T、宇树 H2 Plus、ABC 开源栈和 OctoSense 多传感平台说明，未来竞争不只是整机，而是模型、工具链、数据和参考本体的生态闭环。
