# 具身智能情报前沿｜零部件进入数据化校准

**作者：具身视界** · 2026.07.17

---

> 今天最值得关注的变化，是具身机器人核心零部件正在从“采购规格表”走向“可建模、可校准、可记录数据、可接训练闭环”。PACE 把执行器和关节动力学识别作为 sim2real 的中心问题，HandUMI、Robotiq 夹爪驱动、rm_control 和触觉论文则共同说明：执行器、夹爪、触觉传感器和硬件接口，正在成为模型落地的真实边界。

## 💥 今日重磅

### 1. [PACE 7 月 14 日更新：执行器和关节动力学识别成为 sim2real 的核心零部件问题](https://github.com/leggedrobotics/pace-sim2real)

**摘要：** GitHub API 显示，leggedrobotics/pace-sim2real 7 月 14 日有推送，星标约 590。PACE 全称 Precise Adaptation through Continuous Evolution，README 将其定义为面向多类机器人系统 sim-to-real transfer 的框架，核心是结合数据驱动 system identification 和 evolutionary optimization，直接从测量数据估计 actuator and joint dynamics，并用 CMA-ES 做参数优化，再把学习到的物理参数用于改善仿真到真实硬件的运动性能。它明确强调 actuator modeling，因为执行器和关节动力学是仿真与真实之间的重要误差来源。项目支持多种机器人平台和执行器类型，设计上可与 NVIDIA Isaac Lab 集成，并建议使用 Isaac Sim 5.0 或更新版本以获得更好的物理属性支持。

- **核心价值：** 数据相关报道：核心零部件不再只是电机、减速器、编码器的静态参数，而是需要通过实测数据识别动态模型；谁能把执行器数据变成可复用仿真参数，谁就能更快缩短 sim2real 距离。
- **行业判断：** 具身机器人硬件的下一步竞争，不只是零部件性能堆料，而是“零部件能否被准确建模并进入训练闭环”。

---

## 📰 行业新闻

### 1. [HandUMI 硬件 7 月 15 日更新：夹爪数据采集接口走向可穿戴和模块化](https://github.com/robonet-ai/handumi-hw)

**摘要：** robonet-ai/handumi-hw 7 月 15 日有推送，Apache-2.0 许可。README 显示，HandUMI 是 UMI 的手戴式开源变体，用于在没有机器人本体参与的情况下采集双臂操作数据，面向 parallel-jaw gripper。一个单元零部件成本约 110 美元，配合 PICO 4 Ultra 或 Meta Quest 3 等 VR 头显使用；其模块化 gripper tip 可适配 AgileX Piper、ARX X5、Dream Gripper、Trossen WidowX AI 和原始 UMI gripper 等目标。

- **核心价值：** 数据相关报道：末端执行器正在从“机器人上的夹爪”扩展为“人手上的采数零部件”；夹爪开合宽度、腕部 SE(3) 位姿和腕部视频会一起成为部署数据来源。

### 2. [pyRobotiqGripper 7 月 13 日更新：工业夹爪 Python 驱动继续补齐末端执行器软件层](https://github.com/castetsb/pyRobotiqGripper)

**摘要：** castetsb/pyRobotiqGripper 7 月 13 日有推送，星标约 81。README 显示，这是用于控制 Robotiq 夹爪的 Python 驱动，支持 Modbus RTU 串口或以太网通信，兼容 2F85、2F140 和 Hand-E，可完成激活、标定、开合、位置读取、毫米级位置控制和实时运动控制，并提供 joystick CLI。

- **核心价值：** 工业末端执行器的价值不只在机械夹持力，还在驱动接口、反馈读取和实时控制是否容易接入上层机器人策略。

### 3. [PAR6 开源协作机械臂 7 月 12 日更新：开源本体继续暴露 BOM、打印件和控制盒生态](https://github.com/Source-Robotics/PAR6-Collaborative-Robot-Arm)

**摘要：** Source-Robotics/PAR6-Collaborative-Robot-Arm 7 月 12 日有推送，CERN-OHL-S-2.0 许可。README 显示，PAR6 是面向教育、研发和 AI 的开源协作机械臂，目前处于 beta release，文档、BOM、3D 打印文件和源代码仍在迭代，并关联 STEPFOC stepper controller 与 RCB Robot Control Box 等相关仓库。

- **核心价值：** 开源机械臂的意义在于把关节结构、控制盒、打印件和装配文档一起开放；这会降低小团队验证具身算法和零部件方案的门槛。

---

## 📚 前沿论文

### 1. [NeuralActuator：用神经执行器模型同时处理动力学和外力感知](https://arxiv.org/abs/2607.11734)

**摘要：** 7 月 13 日提交的 NeuralActuator 指出，差分仿真器推动了策略学习和模型控制，但 actuator dynamics 仍是 sim-to-real 误差的重要来源；在低成本平台上，线性电流到力矩关系并不总是可靠。论文提出 neural actuation modeling，用于机器人动力学建模和外部力感知。

- **核心价值：** 执行器模型正在从固定力矩常数走向数据驱动；这对低成本关节、电机控制和力感知闭环都有直接影响。

### 2. [TAC-LOCO：触觉进入四足全身移动操作控制](https://arxiv.org/abs/2607.10132)

**摘要：** 7 月 11 日提交的 TAC-LOCO 面向 quadrupedal tactile-informed loco-manipulation，研究腿足机器人在抓取物体时如何协调全身运动，并在不确定外力下保持稳定物理交互。论文强调，触觉不仅用于手部操作，也可进入腿足移动操作的全身控制。

- **核心价值：** 触觉传感器正在从“手指局部反馈”扩展到全身控制信号；移动操作机器人需要把接触数据纳入步态、身体姿态和物体交互控制。

### 3. [TACTIC：视觉 + 触觉条件下的全臂接触控制](https://arxiv.org/abs/2607.09218)

**摘要：** 7 月 10 日提交的 TACTIC 聚焦 whole-arm manipulation，机器人需要通过多个手臂连杆与环境接触完成任务。论文认为，常见学习式操作方法隐含了接触局限于末端的假设，而全臂操作需要在接触形成、滑动和断开时持续分配接触。

- **核心价值：** 触觉和力接触能力不应只堆在夹爪上；未来机械臂核心零部件可能需要在腕部、臂段和柔顺结构上共同布置感知。

### 4. [TactiDex：真实触觉引导灵巧操作基准](https://arxiv.org/abs/2607.09190)

**摘要：** 7 月 10 日提交的 TactiDex 指出，触觉反馈决定接触形成、力调节和稳定操作，是人类级灵巧操作的基础。论文提出真实世界 tactile-guided benchmark，用于评估类人灵巧操作中的触觉能力。

- **核心价值：** 数据相关报道：灵巧手和触觉传感器需要可比较的真实基准；否则硬件厂商很难证明“多一个触觉阵列”到底带来多少操作收益。

### 5. [Requirement-Driven Whole-Body Social Tactile Sensing：从需求反推全身触觉布局](https://arxiv.org/abs/2607.11690)

**摘要：** 7 月 13 日提交的论文关注 social-physical HRI 中的 whole-body social tactile sensing。论文指出，传统触觉设计常由硬件预设配置驱动，限制了覆盖范围、空间分辨率和可识别手势；因此提出 requirement-driven 设计思路，通过虚拟人机交互反推传感布局需求。

- **核心价值：** 人形机器人核心零部件不只是手部执行器；如果要进入社交和服务场景，全身触觉皮肤的覆盖、分辨率和手势识别能力会成为设计变量。

---

## 🧩 开源生态

### 1. [HandUMI 软件 7 月 16 日更新：采集、校准、质检、重定向连成零部件数据链](https://github.com/robonet-ai/handumi-sw)

**摘要：** robonet-ai/handumi-sw 7 月 16 日有推送，README 显示其提供 HandUMI 的同步数据采集、校准、验证、回放、遥操作和机器人重定向软件。核心流程是 tracking + cameras + gripper widths 进入 synchronized raw dataset，再进行 validate、convert 和 replay；原始采集保持 robot-agnostic，机器人配置和物理 controller-to-TCP 标定会写入数据集元数据。

- **核心价值：** 数据相关报道：零部件采数如果没有校准、质检和元数据，后续很难重定向到真实机器人；HandUMI 把末端执行器数据变成可复用训练资产。

### 2. [rm_control：面向高性能机器人开发的硬件/仿真接口](https://github.com/rm-controls/rm_control)

**摘要：** rm-controls/rm_control 7 月 11 日有推送，星标约 295。仓库描述显示，它是基于 ros-controls 的硬件/仿真接口，用于 RoboMaster robots 和 high-performance robots 开发，并提供 CI、格式检查、Doxygen 文档和在线文档入口。

- **核心价值：** 核心零部件要进入机器人系统，必须先被硬件接口抽象出来；仿真和真机共用接口会减少电机、传感器和控制板适配成本。

### 3. [PACE：把 Isaac Lab 与执行器参数优化连接起来](https://github.com/leggedrobotics/pace-sim2real)

**摘要：** PACE 支持从数据中估计执行器和关节参数，并将结果存入日志，用于改善后续 sim2real 运动性能。README 中 ANYmal D 示例先采集 excitation data，再通过 `fit.py` 做参数拟合，说明执行器调参正从手工经验走向数据化流程。

- **核心价值：** 腿足机器人研发会越来越依赖“零部件参数数据库”：不同电机、减速器、编码器和关节摩擦的真实动态，决定仿真策略能否上真机。

---

## 🏢 机器人公司情报

### 1. [ETH Zurich RSL：PACE 代表零部件建模走向研究基础设施](https://github.com/leggedrobotics/pace-sim2real)

**摘要：** PACE README 显示项目由 ETH Zurich Robotic Systems Lab 相关维护者维护，目标是通过执行器和关节动力学参数识别缩小仿真与真实硬件差距。对机器人公司而言，这类工具能把零部件采购后的真实动态纳入算法训练，而不是只依赖供应商规格表。

- **核心价值：** 高性能硬件不等于高性能机器人；只有把执行器真实动态识别进仿真，硬件优势才会转化为策略稳定性。

### 2. [Robonet AI / HandUMI：用低成本可穿戴夹爪接口降低双臂采数门槛](https://github.com/robonet-ai/handumi-hw)

**摘要：** HandUMI 硬件和软件仓库显示，团队正在把双臂操作采集从固定机器人工作站转向手戴式接口。一个 HandUMI 单元约 110 美元零部件成本，目标是把机器人本体留给部署，把人类演示采集从昂贵 leader-follower 硬件中释放出来。

- **核心价值：** 末端执行器不只是执行零部件，也可以成为数据入口；低成本可穿戴夹爪会改变双臂机器人训练数据成本结构。

### 3. [Source Robotics：PAR6 把协作机械臂零部件开放给教育、研发和 AI 场景](https://github.com/Source-Robotics/PAR6-Collaborative-Robot-Arm)

**摘要：** PAR6 仓库显示，Source Robotics 正在围绕开源协作机械臂迭代硬件、BOM、打印件、控制盒和文档。虽然项目仍处 beta，但它体现了一个方向：核心零部件和整机结构不再完全封闭，教育和研发团队可以参与测试与改进。

- **核心价值：** 开源本体会带动零部件透明化，尤其是关节、控制盒、3D 打印结构和末端接口，适合早期算法团队快速搭建可改造平台。

---

## 结尾总结

7 月 17 日的主线可以概括为：具身机器人核心零部件正在进入数据化、模块化和可校准阶段。PACE 把执行器和关节动力学从“硬件参数”变成“可识别的仿真参数”，HandUMI 把夹爪和腕部采集接口变成低成本数据入口，Robotiq 驱动和 rm_control 则说明末端执行器与硬件接口仍是工程落地的关键。触觉论文密集出现也说明，未来核心零部件不会只看电机和减速器，还会看触觉、力反馈、传感布局和数据闭环。

> 💬 你认为具身机器人核心零部件里，最先形成国产化和平台化突破的会是哪一类：关节执行器、灵巧手、触觉传感器、夹爪末端，还是控制板和驱动接口？

## 关键词索引

**公司 / 机构：** ETH Zurich RSL / Legged Robotics / Robonet AI / Source Robotics / Robotiq / rm-controls

**项目 / 论文：** PACE / HandUMI / handumi-sw / pyRobotiqGripper / PAR6 Collaborative Robot Arm / rm_control / NeuralActuator / TAC-LOCO / TACTIC / TactiDex / Whole-Body Social Tactile Sensing

**技术：** 核心零部件 / 执行器 / 关节动力学 / actuator modeling / joint dynamics / CMA-ES / Isaac Lab / sim2real / 灵巧手 / parallel-jaw gripper / 触觉传感器 / whole-body tactile sensing / gripper width / VR tracking / Modbus RTU / hardware interface

## 值得分享

1. 零部件开始数据化：PACE 用实测数据识别执行器和关节动力学，把电机/关节参数转成可训练、可仿真的资产。
2. 末端执行器正在变成数据入口：HandUMI 约 110 美元零部件成本，可记录腕部位姿、夹爪宽度和腕部视频，用于双臂操作采数。
3. 触觉会成为下一代核心零部件：TactiDex、TACTIC、TAC-LOCO 和全身触觉设计都说明，接触数据正在进入灵巧手、机械臂和全身控制闭环。
