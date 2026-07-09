# 具身智能情报前沿｜OmniAct 把机器人从技能演示推向长期自治框架

**作者：具身视界** · 2026.06.28

> 今天最值得关注的变化，是具身智能的焦点从“单项技能能不能做”继续上移到“长期自治系统怎么搭”。OmniAct、RouterVLA、MMBench2、OctoSense、BOWConnect 和 REGEN 共同指向一条主线：机器人要进入家庭、工厂和园区，不能只依赖一个 VLA 模型，而需要规划、记忆、验证、路由、世界模型、多传感器感知和持续学习共同组成基础设施。

---

## 今日重磅

### [OmniAct：用分层异步架构把网络工具、IoT、导航和操作统一到长期物理自治](https://arxiv.org/abs/2606.27251)

**摘要：** 6 月 25 日提交的 `Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy` 把今天的基础设施主线讲得很清楚：真正可用的具身智能不是单个模型会抓取、会导航或会调用 API，而是能在长期任务中统一调度网络工具、IoT 设备、物理导航、机器人操作，并在失败时自动恢复。论文提出 OmniAct，一个分层异步框架：上层 multimodal semantic planner 负责在统一 cyber-physical action space 中做技能路由；中层 adaptive hierarchical memory 通过 event-boundary-driven compression 让上下文增长保持近似平坦，避免长期交互 token 爆炸；底层 asynchronous visual preemption engine 在 VLA 执行时持续检查视觉状态，一旦发现物理执行偏离预期就打断并修正。实验覆盖两个机器人平台、四类 IoT 设备和 40 个真实长程任务，在不同复杂度任务上均提升端到端成功率，并在累计超过 100k 交互 tokens 时保持近似平坦的 token 消耗。

- **来源：** arXiv
- **核心价值：** OmniAct 的意义在于把具身智能从“技能库”推进到“自治操作系统”：规划、记忆、验证和物理执行不再是论文里的孤立模块，而是被设计成可组合、可打断、可恢复的运行时框架。未来家庭机器人、服务机器人和工业移动操作机器人要长期在线，竞争重点会从单项技能成功率转向整套系统能否持续、安全、低成本地闭环运行。

---

## 行业新闻

### 1. [MMBench2 发布：427 小时、210 任务世界模型测试床，把“模型幻觉”变成可检测的数据覆盖问题](https://arxiv.org/abs/2606.27326)

**摘要：** `Hallucination in World Models is Predictable and Preventable` 发布 MMBench2，包含 427 小时、210 个任务、10 个 domain，并配有 ground-truth actions、rewards 和 live simulators。团队训练 350M 参数世界模型后发现，幻觉集中在低覆盖状态—动作区域，并提出 tokenizer round-trip residual、flow instability、inter-seed variance 三类无标签信号来预测幻觉；在 10 个未见任务上，每任务只用 50 条轨迹进行针对性补数据，就能显著改善世界模型。

- **来源：** arXiv / MMBench2 项目页
- **核心价值：** 这是今天的数据相关报道。世界模型要成为机器人基础设施，必须知道自己在哪里不可靠；MMBench2 把“幻觉”从主观现象转化为可评测、可定位、可主动采集补齐的数据问题。

### 2. [OctoSense：开放八传感器同步平台，机器人感知基础设施从 RGB-only 走向多模态](https://arxiv.org/abs/2606.27317)

**摘要：** `OctoSense` 发布开放传感平台和 59 小时、2,474 公里同步数据，包含 stereo RGB、event camera、LiDAR、thermal、IMU、RTK GPS、CAN / 关节本体感知等八类传感器，并覆盖白天、夜间、眩光和传感退化条件。其 late-fusion masked autoencoder 使用 modality-specific tokenizers 和 token caching，在深度、光流、语义分割、ego-motion 等任务上优于图像基础模型，嵌入式 Orin NX 编码约 112ms。

- **来源：** arXiv / OctoSense 项目页
- **核心价值：** 机器人基础设施不只包括模型和数据，还包括传感器同步、标定、压缩、检索和多模态表征。OctoSense 代表了面向真实环境的感知底座升级。

### 3. [RouterVLA：把部署前 smoke tests 变成 VLA 路由监督，系统成功率提升 14.64 个百分点](https://arxiv.org/abs/2606.27355)

**摘要：** `RouterVLA` 研究一个很工程化的问题：机器人团队部署前通常会对多个 VLA 策略做 smoke test，但往往只选一个全局赢家。论文把这些预部署试运行记录重新利用为 policy selection 监督，在 34,752 条 LIBERO-Plus rollout records 上，用 outcome-disjoint cross-fitting 构建专家 profile，再用单独试验评分所选专家。透明的 probe-success 规则将 held-out success 从 0.4686 提升到 0.6149，增益 14.64 个百分点。

- **来源：** arXiv
- **核心价值：** 模型路由会成为机器人部署基础设施的一部分。不同 VLA 在不同任务、场景和本体上表现不同，与其押注单一模型，不如让系统根据 commissioning 数据自动选择最合适的专家。

### 4. [ABC 全栈继续发酵：开源数据、仿真、训练和真实评测成为操作学习基础设施样板](https://abc.bot/)

**摘要：** ABC 项目释放 ABC-130K、400 小时 sim-teleop 数据、硬件设置、训练代码、仿真管线和超过 100 小时真实评测日志。其核心贡献不只是 3,553 小时双臂遥操作数据，而是建立从数据采集、分布式 dataloader、MuJoCo 仿真、Blender 重渲染、DiT / VLA 模型训练到真实机器人评测的完整工程闭环。

- **来源：** ABC 项目页 / arXiv
- **核心价值：** 机器人操作研究正在进入“可复现实验底座”阶段。未来高质量开源栈的价值，可能不低于单个大模型 checkpoint。

---

## 前沿论文

### 1. [REGEN：世界动作模型生成伪回放，让机器人持续学习时少忘旧任务](https://arxiv.org/abs/2606.27374)

**摘要：** `World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays` 提出 REGEN。它利用 World Action Models 同时预测动作和未来视觉观测的能力，在连续模仿学习中递归合成 pseudo-replay trajectories，让机器人在学习新任务时“复习”旧任务，而无需保存原始人类示范。仿真和真实操作实验显示，REGEN 相比顺序微调最多减少 50% 灾难性遗忘，并接近需要真实 replay data 的 privileged experience replay。

- **作者团队：** Manish Kumar Govind、Dominick Reilly、Smit Patel、Hieu Le、Srijan Das
- **来源：** arXiv
- **核心价值：** 机器人长期部署必然持续学习新技能，但真实示范数据不能无限保存和回放。REGEN 把世界动作模型变成“记忆基础设施”，为隐私、存储和持续学习之间提供新平衡。

### 2. [Continual Robot Policy Learning：用变分神经动力学让控制器识别风、载荷、电池和磨损变化](https://arxiv.org/abs/2606.27353)

**摘要：** 这篇论文面向真实部署中持续变化的动力学条件：风变了、载荷变了、电池电量下降、接触状态变化、硬件磨损都会让一次性训练的控制器失效。方法用分析物理先验加 neural residual 学习 condition-aware dynamics model，再用 recurrent encoder 从近期交互中推断隐藏条件，并把该条件同时输入动力学残差和策略。真实四旋翼轨迹跟踪实验中，策略在约 1 秒内从重复扰动中恢复，比在线 residual re-fitting 快约 5 倍，并将大扰动悬停和跟踪误差分别降低 65.7% 和 53.3%。

- **作者团队：** Jiaxu Xing、Zhiyuan Zhu、Yunfan Ren、Ismail Geles、Yifan Zhai、Rudolf Reiter、Davide Scaramuzza
- **来源：** arXiv
- **核心价值：** 这是部署级控制基础设施：机器人不能假设世界动力学固定不变，而要把真实交互变成在线识别和恢复能力。

### 3. [BOWConnect：用并行贝叶斯优化窗口学习局部代价图，提升动态运动规划基础设施](https://arxiv.org/abs/2606.27292)

**摘要：** `BOWConnect` 是一个双向并行 kinodynamic motion planner，针对高维状态采样效率低、动态约束下代价启发不可靠、狭窄通道表现差三类问题。它把 Bayesian Optimization over Windows 作为学习型 steering function，多个 worker 学习局部代价图和约束，引导采样到动态可行、无碰撞控制；双向树并行生长，并用 spatial hashing 加速连接查询。在 10 个 benchmark 中达到 100% 成功率，真实地面车和四旋翼部署实现实时无碰撞规划。

- **作者团队：** Sourav Raxit、Abdullah Al Redwan Newaz、Jose Fuentes、Leonardo Bobadilla
- **来源：** arXiv / IROS 2026
- **核心价值：** 运动规划仍是具身系统的底层硬骨头。BOWConnect 的价值在于把学习型局部代价估计嵌入经典规划框架，而不是完全替代安全可解释的规划结构。

### 4. [E-TTS：具身测试时扩展框架，用历史、推理和验证器提升机器人操作](https://arxiv.org/abs/2606.27268)

**摘要：** `E-TTS` 提出 Embodied Test-Time Scaling 框架，在不重新训练、不增加专家数据的情况下，对 VLA 的推理和动作候选进行联合采样与评分。框架使用 history buffer 保存历史上下文，再由 reasoning verifier 和 action verifier 评估候选，并通过反馈生成形成闭环迭代。实验覆盖 4 个 benchmark、6 个环境、3 种本体和 4 个基础 VLA，仿真最高提升 33.14%，真实场景提升 26.62%。

- **作者团队：** Wen Ye、Peiyan Li、Tingyu Yuan 等
- **来源：** arXiv / ECCV 2026
- **核心价值：** 测试时扩展正在从大语言模型进入机器人运行时。它让部署端的算力、历史和验证器成为提升成功率的基础设施，而不是只依赖训练阶段。

### 5. [LA4VLA：语言—动作预训练框架，让 VLA 少依赖视觉捷径](https://arxiv.org/abs/2606.27295)

**摘要：** `LA4VLA` 将示范轨迹拆成原子动作段，并为每段配对低层动作描述，构造 33K 个 Language-Action episodes，无需额外采集机器人数据。团队提出 1B 参数 LA4VLA，并比较 LA-only、LA-to-VLA、mixed LA-VLA 三种预训练方式。结果显示，语言—动作预训练在仿真和真实任务中稳定优于常规 VLA 预训练，mixed LA-VLA 最高可带来 17.8 和 45.0 个百分点成功率提升。

- **作者团队：** 上海交通大学等
- **来源：** arXiv / GitHub
- **核心价值：** 语言—动作对齐会成为 VLA 数据基础设施的重要组成。机器人需要的不只是图像到动作，还要理解“按压、旋转、倒出、对齐”等动作语义如何约束控制。

### 6. [PhysReflect-VLA：给 VLA 加物理可行性检查和在线自反思](https://arxiv.org/abs/2606.27146)

**摘要：** `PhysReflect-VLA` 针对长程接触丰富操作中的不可行动作、接触扰动和缺少自纠错问题，提出执行时可靠性框架。系统包含 Feasibility Operator，用于评估候选动作是否产生动力学一致状态转移；Action Explanation Operator，用于验证转移连贯性；以及 LLM-based Reflection Module，根据状态偏差生成后续修正指令。多阶段真实操作实验中，该框架相对代表性 VLA baseline 平均提升 5.4% 总任务成功率。

- **作者团队：** Jiayu Yang、Tao Yang、Weijun Li 等
- **来源：** arXiv
- **核心价值：** 具身框架不能只会生成动作，还要会检查动作是否物理可行，并在执行中诊断错误。PhysReflect-VLA 是 VLA 运行时安全层的一种可组合实现。

---

## 开源生态

### 1. [MMBench2 开放代码、数据、模型和 live demo：世界模型评测进入可交互时代](https://github.com/nicklashansen/mmbench2)

**摘要：** MMBench2 项目页提供交互式论文、live demo、代码、数据集和模型。用户可以直接控制 350M 参数世界模型，并实时观察幻觉预测信号；项目还展示如何用幻觉预测指导 targeted data collection，在低覆盖区域主动补数据。

- **来源：** GitHub / 项目页
- **核心价值：** 对世界模型社区来说，这相当于提供了一套“测幻觉、找覆盖缺口、补数据、再评测”的基础设施闭环。

### 2. [OctoSense 开放硬件与数据：从传感器同步板到自然语言检索全部打包](https://github.com/anthonytec2/OctoSense)

**摘要：** OctoSense 开放机械 CAD、传感器安装、同步电路、采集处理工具和数据集。其数据每 5 秒窗口用 Gemma 4 生成 caption，并用 Qwen3 embedding 建立 FAISS + BM25 检索索引，用户可按“wet road at night”“police vehicle”等自然语言检索传感片段。

- **来源：** GitHub / Hugging Face / 项目页
- **核心价值：** 机器人感知数据未来不能只是离线下载文件，而要能被搜索、对齐、标定、复用。OctoSense 把多传感器数据基础设施做到了工程可用级别。

### 3. [BOWConnect 开源：动态运动规划可复现实验与真实部署视频同步发布](https://bow-connect.github.io/)

**摘要：** BOWConnect 论文说明项目页提供开源代码、仿真与真实实验视频、高分辨率图表。方法面向地面车、四旋翼等动态系统，强调在狭窄通道和非凸空间中保持动态可行与无碰撞规划。

- **来源：** 项目页 / arXiv
- **核心价值：** 对移动机器人和无人系统团队来说，可复现的 kinodynamic planning 框架仍然是底层刚需，尤其是在学习控制与安全规划结合越来越紧密的阶段。

### 4. [ABC 工具链继续值得关注：大规模机器人数据加载和真实评测日志成为开源资产](https://github.com/amazon-far/abc)

**摘要：** ABC 开放分布式 dataloader、训练代码、推理优化、仿真管线和评测日志。其 abcdl 将 episode 编码为 MP4 堆叠相机视角加二进制 state/action 文件，并通过 keyframe 编码优化随机帧访问，降低大规模机器人数据训练中的 I/O 压力。

- **来源：** GitHub / ABC 项目页
- **核心价值：** 随着具身数据从几百小时走向几千小时，数据加载、评测日志、仿真代理评测这些“脏活累活”会变成决定训练效率的关键基础设施。

---

## 机器人公司情报

### 1. [NVIDIA Isaac GR00T：人形机器人基础模型平台价值继续被开放框架放大](https://developer.nvidia.com/isaac/gr00t)

**摘要：** GR00T 覆盖开放数据与数据管线、机器人基础模型、Omniverse / Cosmos 仿真、中间件、CUDA-X 加速库和 Jetson Thor 部署。近期 ABC、OctoSense、MMBench2、E-TTS、LA4VLA 等工作不断开放数据、评测和运行时框架，客观上会推动类似 GR00T 的平台成为机器人开发默认底座。

- **来源：** NVIDIA Isaac GR00T
- **核心价值：** 平台型公司最大的优势，是能把碎片化论文成果吸收到统一工具链中。未来机器人厂商的差异化，可能建立在平台基础设施之上的本体、数据和场景能力。

### 2. [Amazon FAR：参与 ABC 显示产业界正在押注可复现双臂操作基础设施](https://abc.bot/)

**摘要：** ABC 项目作者团队中包含 Amazon FAR，工作在双臂遥操作数据、真实评测、仿真—真实相关性、DAgger 介入和长程操作上投入大量工程细节。这些方向与仓储、分拣、装箱、包装、袋装物处理等真实商业任务高度一致。

- **来源：** ABC 项目页
- **核心价值：** 产业界开始把“数据栈和评测栈”视为竞争核心。对仓储机器人而言，谁能更快采集失败、评估策略、回灌干预数据，谁就能更快逼近稳定 ROI。

### 3. [1X World Model Lab：公司级世界模型基础设施路线与 MMBench2 形成呼应](https://www.1x.tech/discover/1x-world-model-lab)

**摘要：** 1X World Model Lab 强调大规模 embodied world model pretraining，并把 web-scale media、egocentric human videos、simulation、dexterous remote operated robot data 和 on-policy NEO data 写入数据配方。MMBench2 最新工作进一步表明，世界模型的可靠性本质上取决于数据覆盖，幻觉检测可反过来指导补数据。

- **来源：** 1X Technologies / arXiv
- **核心价值：** 世界模型正在从“生成未来视频”变成公司级基础设施：数据混合、覆盖诊断、在线补数据和真实部署回流会共同决定人形机器人学习速度。

### 4. [NEURA Robotics：Neuraverse 与 NEURA Gyms 代表商业部署回流型基础设施](https://neura-robotics.com/neura-robotics-showcases-full-stack-robotics-platform-at-automate-2026/)

**摘要：** NEURA Robotics 在 Automate 2026 前披露 Neuraverse 平台和 NEURA Gyms 训练环境，强调 Physical AI 必须在真实世界中训练、验证和持续改进。Neuraverse 连接机器人、开发者和产业伙伴，每次部署都会贡献到 physical intelligence 池；NEURA Gyms 则把真实训练设施与高保真仿真结合。

- **来源：** NEURA Robotics
- **核心价值：** 这是商业部署版的数据基础设施路线：不是只发布一次性数据集，而是让每个客户站点、每台机器人、每次任务执行都成为持续学习网络的一部分。

---

## 结尾总结

6 月 28 日这期的共同趋势，是具身智能正在从模型竞赛进入基础设施竞赛。OmniAct 关注长期自治的运行时架构，RouterVLA 关注部署前试运行如何变成模型路由监督，MMBench2 关注世界模型幻觉与数据覆盖，OctoSense 关注多传感器同步与鲁棒表征，BOWConnect 关注动态规划底层能力，REGEN 和 Continual Dynamics 则关注机器人如何在部署后持续学习而不遗忘、不失稳。

可以下一个判断：**机器人真正走向规模部署时，最稀缺的不是某一个“最强模型”，而是一套能长期运行、持续学习、可评测、可回滚、可路由、可补数据的具身智能基础设施。** 模型会变强，但决定它能不能进家庭、进工厂、进园区的，是模型之外的系统工程。

---

> 💬 你认为未来一年具身智能最该补齐哪类基础设施：世界模型评测、机器人数据平台、VLA 路由与运行时、安全验证，还是多传感器感知底座？欢迎留言讨论。

---

## 关键词索引

**公司与机构：** NVIDIA、Amazon FAR、1X Technologies、NEURA Robotics、UC San Diego、University of Pennsylvania、Brown University、上海交通大学  
**技术与项目：** OmniAct、MMBench2、OctoSense、RouterVLA、ABC-130K、REGEN、World Action Models、BOWConnect、E-TTS、LA4VLA、PhysReflect-VLA、Isaac GR00T、Neuraverse、NEURA Gyms  
**产品与硬件：** Jetson Thor、Jetson Orin NX、Omniverse、Cosmos、八传感器同步平台、stereo RGB、event camera、LiDAR、thermal camera、IMU、RTK GPS、Unitree Go2-W  
**关键方向：** 具身智能基础设施、长期自治、cyber-physical action space、分层记忆、视觉抢占、VLA 路由、世界模型幻觉、数据覆盖、主动补数据、多模态感知、持续模仿学习、动态运动规划、测试时扩展、物理可行性检查

---

## 值得分享

1. **具身智能正在从技能演示进入系统架构竞争：** OmniAct 把规划、记忆、验证、IoT、导航和操作统一进分层异步框架，面向 40 个真实长程任务验证长期自治。
2. **世界模型的关键问题是数据覆盖：** MMBench2 用 427 小时、210 任务测试床证明幻觉可预测、可补齐，每个未见任务 50 条针对性轨迹就能显著改善模型。
3. **机器人基础设施不只在云端，也在传感器和运行时：** OctoSense 开放八传感器同步平台，RouterVLA 用 34,752 条预部署 rollout 做模型路由，说明真实部署需要完整工程底座。
