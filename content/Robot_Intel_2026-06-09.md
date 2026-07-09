# 具身智能情报前沿｜机器人的算法架构正在从单一策略走向多引擎协同

**作者：具身视界** · 2026.06.09

> 今天最值得关注的变化，是机器人算法架构正在从"一个模型包办所有"走向多引擎协同。Spline Policy 用样条参数替代固定动作分块让轨迹可编辑、VOLT 用视觉语言分割轨迹实现变速执行、MiTaS 用多分辨率触觉融合提升精细操作成功率、而"Robots Need More than VLA and World Models"一文则直指核心：缺失的四个接口才是机器人智能规模化真正的瓶颈。

---

## 💥 今日重磅

### [Robots Need More than VLA and World Models：机器人学习基建的四个缺失接口](https://arxiv.org/abs/2606.06556)

**摘要：** 6 月 4 日发表的这篇 position paper 提出了一个尖锐的判断：当前机器人智能的主流路线——收集更多机器人示范、训练更大的 VLA 模型——是不够的。真正的瓶颈不是策略本身，而是缺少四个关键接口：（1）**数据接口**，利用无结构行为数据进行自动标注；（2）**本体接口**，将人类运动重定向到机器人动作；（3）**世界模型接口**，基于物理的 3D 推理；（4）**奖励接口**，从视频和语言中推断任务进度与成功。文章认为，只有补齐这四类接口，机器人系统才能真正从"只能学机器人示范"扩展到"从整个物理世界的无结构数据中学习"。

- **来源：** arXiv（ETH Zurich、UC Berkeley、IIT、Imperial College London 等联合团队）
- **核心价值：** 这是今天明确指向"具身算法架构"的标志性观点文章。VLA 和世界模型跑再快，如果没有标准化的数据接口、本体映射接口和奖励接口，它们就只能在狭窄的机器人示范数据上打转。这篇论文给出了一个清晰的路线图：在训练更大的模型之前，先把基础设施层的接口定义清楚，可能是更紧迫的事。

---

## 📰 行业新闻

### 1. [COP-Q 提出Cholesky-Ordered Projection Q-learning，用安全优先RL框架提升机器人控制的样本效率](https://arxiv.org/abs/2606.04749)

**摘要：** 安全约束是机器人控制的核心挑战。现有 off-policy safe RL 方法通常独立学习奖励和安全 Q 值，忽略目标间相关性的建模，导致价值估计保守、样本效率低。COP-Q 提出一个安全优先的 RL 框架，通过 Cholesky-ordered projection 同时建模奖励与安全约束的联合分布，在保持安全性的前提下减少了保守偏差。实验在多个机器人安全控制任务中显示出显著的样本效率提升。

- **来源：** arXiv
- **核心价值：** 算法架构的前端需要解决"怎么保证安全"的问题，而不是先学动作再套安全滤波。COP-Q 提供了一种在价值学习阶段就融合安全约束的思路。

### 2. [Inverse Manipulation提出符号规划+残差操作学习的混合框架，让机器人学会反操作](https://arxiv.org/abs/2606.05248)

**摘要：** 机器人学会推箱子，能不能学会反向操作把箱子放回去？这篇工作研究"逆向操作"问题，提出一种混合框架：从人类示范中自动提取 STRIPS-like 算子和软几何谓词，构建逆向操作目标；符号任务规划器先尝试用动作原语满足目标；未解决的谓词再通过 RL 残差策略进行物理求精。在 ManiSkill3 PushCube 任务上，符号逆操作完成粗粒度 pick-and-place 恢复后，残差 SAC 策略再精细调整 cube 位姿。

- **来源：** arXiv / PlanRob26 录用
- **核心价值：** 算法架构需要具备"可逆性"——机器人不能只会单向执行，还要能推理反向操作。符号规划 + 残差学习的混合架构可能成为未来机器人技能的通用设计模式。

### 3. [Shield-Loco提出预测式安全滤波器，用全物理模型保护足式机器人RL策略](https://arxiv.org/abs/2606.07193)

**摘要：** RL 策略虽然可以让足式机器人实现动态移动，但在训练中未出现的危险场景下缺乏安全保证。Shield-Loco 设计了一个预测式安全滤波器，以 post-hoc 方式过滤 RL 策略输出的接触位置：当预测到碰撞风险时，一个基于全物理模型的采样优化器异步搜索更安全的接触序列，用学习到的价值函数引导长时程回报。在密集杂乱环境下的四足机器人仿真和真实实验中，该滤波器大幅减少了安全违规，同时对名义输入的影响最小。

- **来源：** arXiv
- **核心价值：** 算法架构的安全侧需要"防护罩"而不是"只靠训练"。预测式安全滤波器的思路——不改变主策略、仅在后端过滤危险接触——对工业部署非常实用。

---

## 📑 前沿论文

### 1. [Spline Policy用样条参数替代固定动作分块，让机器人策略的轨迹可编辑、可约束、可评估不确定性](https://arxiv.org/abs/2606.07386)

**摘要：** `Spline Policy: A Structured Representation for Robot Policies` 提出用样条参数替代现有模仿学习策略中的固定分辨率动作分块。样条被解码为连续的紧凑轨迹，可在不同时间分辨率上查询、在参数空间中编辑和约束，并传递给下游控制器。对于二次样条输出，还能通过解析距离场构造转换为状态依赖的向量场，实现围绕预测运动的局部矫正机制。样条输出还支持从观测到样条参数、轨迹再到流场的不确定性传播。作者在 diffusion、flow-matching、transformer-based 和 VLA 等多种策略骨干上实例化了 Spline Policy。

- **来源：** arXiv / submitted to IEEE
- **核心价值：** 这是今天"算法架构"主线的核心论文之一。它不改变策略骨干，而是改变策略的输出表示——从"一维动作序列"升级为"可编辑、可约束、可评估不确定性的轨迹参数"。这种结构化表示对具身算法架构的意义，类似于 CNN 对视觉架构的意义。

### 2. [VOLT用视觉语言分割轨迹实现机器人变速执行，安全段加速、精准段保留](https://arxiv.org/abs/2606.06323)

**摘要：** `VOLT: Vision and Language Trajectory Segmentation for Faster-than-Demonstration Policies` 观察到人类演示通常比机器人执行更慢。理想的方式是变速执行：无约束运动段加速，精细操作段减速。VOLT 通过视觉和语言线索对视频演示进行分段，识别出哪些段需要慢速精确运动、哪些段可以安全降采样。生成的变速轨迹可用于标准模仿学习方法。实验表明分段质量至关重要，VOLT 在保持高成功率的前提下显著提升了机器人执行速度。

- **来源：** arXiv
- **核心价值：** 算法架构需要具备"时序理解"能力，不能简单地对齐演示速度。VOLT 的轨迹分割方法为机器人策略提供了一个实用的"加速什么地方、减速什么地方"的架构层。

### 3. [MiTaS用多分辨率触觉传感器融合实现接触丰富操作的模仿学习](https://arxiv.org/abs/2606.06281)

**摘要：** `Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation` 提出 MiTaS 表示框架，同时利用不同时间分辨率的多模态触觉传感器（RGB相机 + GelSight Mini 视觉触觉 + Evetac 事件触觉），通过 modality-specific convolutional stems 和 transformer-based fusion 融合特征，再用 flow-matching policy 解码。在 5 个接触丰富操作任务上，MiTaS 平均成功率 80%，而纯视觉 baseline 仅 31%、视觉 + 单触觉 baseline 仅 54%。混合训练还能让模型在不接入 Evetac 的情况下性能提升超 10%。

- **来源：** arXiv / 项目页 mitas-touch.github.io
- **核心价值：** 算法架构的多模态融合需要时间分辨率对齐。MiTaS 证明高帧率事件触觉和低帧率视觉触觉可以互补，这种"异构传感器+异构时间分辨率"的融合方法对机器人精细操作有直接工程价值。

### 4. [Auditing Demonstration Curation Metrics发现动作打分器对结构缺陷无效](https://arxiv.org/abs/2606.05588)

**摘要：** 模仿学习策略继承了训练数据的质量，因此出现了各种自动样本质控指标。这篇工作构建了受控测试平台，向示范数据中注入已知类型的缺陷，并审计 7 种样本质控指标。发现：对于微妙扰动（相关动作噪声、抖动、截断），多元离群点检测有效；对于结构性错误（关键步执行错误），所有纯动作指标都失效，有两种甚至出现了反选——把有缺陷的样本打为高质量。

- **来源：** arXiv / UC Berkeley
- **核心价值：** 算法架构不只是"学什么"，还有"筛什么"。这篇文章提醒我们，数据筛选本身就是一个需要精心设计的模块，尤其当缺陷藏在状态轨迹中而非动作本身时。

### 5. [Predictive Style Matching实现自然鲁棒的人形步态，用状态条件化预测改善运动质量](https://arxiv.org/abs/2606.07083)

**摘要：** `Predictive Style Matching: Natural and Robust Humanoid Locomotion` 解决 RL 人形移动中运动质量与鲁棒性的矛盾：任务奖励收敛出僵硬步态，动作模仿改善外观但降低抗扰动能力。PSM 在训练时引入一个离线预测器，根据机器人下半身状态历史映射可解释的上半身关节目标和步态目标，因为目标是状态条件化的而非时间索引的，部署后的控制器保持了 task-only RL baseline 的 proprioceptive 接口和推理成本。在 Unitree G1 上，PSM 将上半身姿态误差减少约一个数量级，同时保持了任务奖励方法的 fall-recovery 能力。

- **来源：** arXiv
- **核心价值：** 算法架构需要区分"训练时的辅助模块"和"部署时的轻量执行"。PSM 用 offline predictor 只在训练时提供风格指导，推理时零额外成本——这种"训练重、推理轻"的设计模式值得借鉴。

---

## 💻 开源生态

### 1. [MoDex开源扩散策略用于灵巧手多物体顺序抓取，用opposition space条件保留手指冗余](https://arxiv.org/abs/2606.05407)

**摘要：** `MoDex: A Diffusion Policy for Sequential Multi-Object Dexterous Grasping` 解决了灵巧手逐个抓取多个物体且不释放已抓物体的挑战。通过 opposition space 条件指定当前抓取使用哪些手指，保留其余 DOF 供后续抓取。两阶段训练：先模仿学习预训练，再 RL 微调。在仿真和 Franka + Allegro Hand 真实平台上成功率均超过 baseline 2.92-17.92%。项目页：modex2026.github.io。

- **来源：** arXiv / submitted to CoRL 2026
- **核心价值：** 算法架构的"动作空间管理"——让灵巧手在顺序操作中保持自由度冗余——是对 VLA 简单输出动作分块的必要补充。

### 2. [COP-Q 安全RL框架已公开方法细节（见上文行业新闻）](https://arxiv.org/abs/2606.04749)

**摘要：** 本论文方法已开源部分框架细节，重点是解决了 off-policy safe RL 中多目标关联性建模问题。通过 Cholesky 分解实现的安全确定性投影，让 RL 策略在保持安全约束的同时显著提升样本效率。适合作为机器人安全学习基线的参考实现。

- **来源：** arXiv
- **核心价值：** 开源的 safe RL 基线一直是机器人社区的稀缺资源。COP-Q 的方法透明性使其可以成为"安全优先"算法架构的参考 benchmark。

---

## 🏢 产品与平台情报

### 1. [Prosthetic Grasping用仿真数据驱动的模仿学习实现免生物信号义手抓取](https://arxiv.org/abs/2606.07389)

**摘要：** `Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping` 面向上肢义手的免生物信号共享自主控制，构建了一套可扩展的仿真框架，自动生成从腕部虚拟摄像头出发的多样化 reach-to-grasp 示范——包括物理可行的抓取合成、自然到达轨迹重定向和程序化环境生成。使用这些仿真数据训练的 sim-to-real 策略在 3 个真实场景中抓取成功率超 90%，超越了基线方法。

- **来源：** arXiv / 项目页
- **核心价值：** 这是"数据接口"在助残场景的落地案例。当真实医疗数据难以大规模采集时，仿真驱动的数据生成 + 模仿学习提供了一个可操作的算法架构模板。

### 2. [Affordance-Based Hierarchical RL用可供性引导四足机器人 Pedipulation，实现自主交互点选择](https://arxiv.org/abs/2606.07506)

**摘要：** `Affordance-Based Hierarchical Reinforcement Learning for Quadruped Pedipulation` 提出三层分层强化学习框架：pose affordance 引导导航策略、navigation 策略驱动 locomotion 策略、interaction-point affordance 指导 pedipulation 策略。在 IsaacSim 中训练并在真实环境中验证了多种物体交互任务，无需人类干预即可自主选择候选基座位姿和执行操作。

- **来源：** arXiv / submitted to Wiley Journal of Field Robotics
- **核心价值：** 算法架构的分层设计——从"可供性评估"到"导航规划"到"足部操作执行"——展示了四足机器人从移动能力向操作能力扩展的架构路径。可供性在每一层都充当了任务抽象的接口。

---

## 结尾总结

6 月 9 日这期的主线是机器人算法架构的系统性升级。

Spline Policy 改变策略输出表示，让轨迹从动作分块变成可编辑的样条参数；VOLT 给策略加上了"时序理解"层，知道什么时候该快、什么时候该慢；MiTaS 教会策略融合不同时间分辨率的触觉传感器；COP-Q 在价值学习阶段就内置安全约束；而"Robots Need More than VLA and World Models"则提出了更大尺度的问题：在模型变大之前，先把数据接口、本体接口、世界模型接口和奖励接口做出来。

这些工作共同指向一个趋势：下一阶段的机器人算法架构不会只靠一个骨干模型，而是多个专门引擎的协同——数据筛选模块、时序分割模块、多模态融合模块、安全滤波模块、轨迹优化模块，各自负责一层能力，通过标准接口连接。算法架构的竞争正在从"谁的 VLA 更大"转向"谁的引擎设计更合理"。

---

> 💬 **互动问题：你觉得机器人算法的标准化接口应该先标准化哪一层——动作/轨迹表示、数据筛选标准、安全约束接口，还是跨本体映射？欢迎留言说说你的判断。**

---

## 关键词索引

**公司 / 平台：** Unitree G1、Franka Emika Panda、Allegro Hand、IsaacSim、MANI-Skill3、LIBERO、RoboTwin2.0、RMBench  
**技术：** 算法架构、Spline Policy、样条参数化、轨迹编辑、变速执行、多分辨率触觉、Cholesky-Ordered Projection、安全 RL、符号规划、残差学习、预测式安全滤波器、动作空间管理、可供性分层 RL  
**概念 / 数据：** 四种缺失接口、数据自动标注、本体映射、奖励推断、80% vs 31% 触觉融合提升、2.92-17.92% 灵巧手抓取提升、90% 义手成功率

---

## 值得分享

1. **机器人算法架构的关键不是模型更大，而是接口更完善：** "Robots Need More than VLA and World Models" 指出四个缺失接口——数据自动标注、本体映射、3D 物理推理、奖励推断——是机器人智能规模化真正的天花板。
2. **Spline Policy改变策略输出表示：** 用样条参数替代固定动作分块，让机器人轨迹可编辑、可约束、可评估不确定性，对 diffusion、flow-matching、Transformer 和 VLA 骨干都适用。
3. **MiTaS多分辨率触觉融合：** 同时利用 RGB 相机、GelSight Mini 和 Evetac 事件传感器，在接触丰富任务中将成功率从视觉基线 31% 提升到 80%，验证了"异构时间分辨率"融合的工程价值。
