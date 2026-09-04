# 具身智能情报前沿｜WAIC 聚焦身体落地

**作者：具身视界** · 2026.07.19

---

> 今天最值得关注的变化，是 2026 世界人工智能大会正在把 AI 讨论重新拉回“身体、场景和产业生态”。官方页面显示，WAIC 于 7 月 17-20 日在中国上海举行，设置论坛活动、领军人物、新闻、展览亮点和大会生态等模块。对具身智能来说，这类大会的意义不只是展示机器人，而是把本体、数据、控制、零部件和评测放到同一个产业窗口里比较。

## 💥 今日重磅

### 1. [2026 世界人工智能大会开幕窗口：具身机器人进入“论坛 + 展览 + 生态”综合检验](https://www.worldaic.com.cn/)

**摘要：** WAIC 官方网站显示，2026 世界人工智能大会时间为 7 月 17 日至 7 月 20 日，地点为中国上海；页面包含“论坛活动”“领军人物”“新闻”“展览亮点”“大会生态”“合作伙伴”等模块，并列明主办单位包括外交部、国家发展改革委、工业和信息化部、教育部、科学技术部、国务院国资委、国家网信办、中国科学院、中国科协和上海市人民政府，承办单位包括上海市经济信息化委、上海市发改委、上海市科委、上海市浦东新区人民政府、上海市徐汇区人民政府、东浩兰生集团等。对具身机器人行业来说，WAIC 的价值在于提供一个横向比较窗口：同一时间观察本体是否可复现、数据是否可沉淀、模型是否能上真机、控制接口是否稳定、零部件是否进入训练闭环。过去一周 OpenArm、LeRobot、Isaac Lab-Arena、PACE、HandUMI 等项目持续活跃，恰好说明“机器人展示”正在升级为“机器人生态能力展示”。

- **核心价值：** WAIC 不是单点技术发布会，而是产业级筛选场；具身机器人能否从展台走向客户现场，取决于本体、数据、控制、零部件和场景闭环是否同时成立。
- **行业判断：** 2026 年的具身智能叙事正在从“模型很强”转向“身体能落地、数据能回流、生态能复制”。

---

## 📰 行业新闻

### 1. [WAIC 官方论坛页上线：大会议程从单点演示转向多主题生态组织](https://www.worldaic.com.cn/events/forum)

**摘要：** WAIC 官方“论坛”页面可访问，页面显示“2026 论坛”“筛选”“搜索”等议程入口，并与大会主办、承办和服务信息相连。对具身智能从业者来说，论坛页面的信号是：机器人不再只是展览区设备，而是要与大模型、产业应用、治理、算力、数据和开发者生态一起被讨论。

- **核心价值：** 具身智能的产业化议题正在从“机器人会不会动”扩展到“谁来定义场景、谁来提供数据、谁来承担安全责任、谁来维护现场系统”。

### 2. [LeRobot 7 月 19 日继续活跃：开源机器人数据与模型工具链可作为 WAIC 观察底座](https://github.com/huggingface/lerobot)

**摘要：** GitHub API 显示，huggingface/lerobot 7 月 19 日仍有推送，星标约 25947。LeRobot README 强调硬件无关的 Python 原生机器人接口、LeRobotDataset 数据格式、真实机器人模型、数据集、训练工具和 Hugging Face Hub 生态。它不是某台机器人，而是具身 AI 的数据和模型工具层。

- **核心价值：** 数据相关报道：如果 WAIC 是产业展示窗口，LeRobot 这类开源工具链就是展后真正沉淀数据、复现实验和扩散模型能力的基础设施。

### 3. [Isaac Lab-Arena 7 月 19 日更新：大会展示背后需要可组合仿真评测](https://github.com/isaac-sim/IsaacLab-Arena)

**摘要：** isaac-sim/IsaacLab-Arena 7 月 19 日有推送，星标约 487。README 显示，它是 NVIDIA Isaac Lab 的开源扩展，将仿真环境拆为 Scene、Embodiment 和 Task 三类可组合原语，并支持大规模并行评测、长时序任务链和自然语言物体摆放。

- **核心价值：** 展台演示只能说明“这一次能跑”；可组合仿真评测才能回答“换本体、换场景、换物体后是否还能跑”。

---

## 📚 前沿论文

### 1. [Jetson-PI：让 VLA 在机载设备上进入实时控制闭环](https://arxiv.org/abs/2607.12659)

**摘要：** 7 月 14 日提交的 Jetson-PI 面向 onboard real-time robot control，关注在 Jetson Orin 等低功耗机载设备上部署 VLA。论文指出，VLA 模型复杂度高，会带来推理延迟和闭环控制问题，因此提出 foresight-aligned asynchronous inference，让推理调度更贴合机器人执行时序。

- **核心价值：** WAIC 上的具身机器人如果要离开展台，必须解决机载算力和控制延迟；低延迟推理调度会成为模型上真机的关键工程能力。

### 2. [Robust bipedal locomotion on flowable slopes：双足机器人开始挑战非刚性地形](https://arxiv.org/abs/2607.11855)

**摘要：** 7 月 13 日提交的论文研究双足机器人在 flowable slopes 上的鲁棒行走。论文指出，双足机器人接近不稳定状态，足地接触的微小变化可能破坏步态；在可流动坡面上，接触不确定性会进一步放大。

- **核心价值：** 人形机器人走向真实世界时，地面并不总是展台地毯；足端接触、地形适应和动态稳定性会决定本体能力上限。

### 3. [NeuralActuator：执行器动力学建模成为 sim2real 关键](https://arxiv.org/abs/2607.11734)

**摘要：** 7 月 13 日提交的 NeuralActuator 指出，执行器动力学仍是仿真到真实误差的重要来源，尤其在低成本平台上，线性电流到力矩关系并不可靠。论文提出神经执行器建模，用于机器人动力学和外力感知。

- **核心价值：** 具身机器人产业化不能只看整机外观，执行器真实动态是否可建模，决定仿真策略能否稳定迁移到真机。

### 4. [Whole-Body Social Tactile Sensing：服务机器人需要从需求反推全身触觉布局](https://arxiv.org/abs/2607.11690)

**摘要：** 7 月 13 日提交的论文关注 social-physical HRI 中的全身触觉设计。论文认为，传统触觉传感常由硬件预设布局驱动，限制覆盖范围、空间分辨率和可识别手势；因此提出 requirement-driven 设计路径。

- **核心价值：** 当机器人进入 WAIC 这类公众场景，全身触觉、安全交互和社交距离感会从研究问题变成产品问题。

---

## 🧩 开源生态

### 1. [OpenArm：开源人形手臂提供从本体到数据的完整入口](https://github.com/enactic/openarm)

**摘要：** enactic/openarm 7 月 16 日有推送，星标约 2739。README 显示，OpenArm 是开源 7DOF humanoid arm，完整双臂系统约 6500 美元，并拆分出硬件、URDF/xacro、CAN、ROS2、遥操作、Isaac Lab、MuJoCo、数据集和 Dora 数据流等子仓库。

- **核心价值：** WAIC 观察具身机器人，不应只看本体能否亮相，还要看本体是否能被第三方复现、采数、训练和评测。

### 2. [PACE：把执行器和关节动力学纳入零部件数据闭环](https://github.com/leggedrobotics/pace-sim2real)

**摘要：** leggedrobotics/pace-sim2real 7 月 14 日有推送，星标约 596。README 显示，PACE 通过数据驱动 system identification 和 CMA-ES 参数优化，从实测数据估计 actuator and joint dynamics，并将学习到的参数用于改善 sim-to-real locomotion performance。

- **核心价值：** 数据相关报道：机器人零部件如果不能被数据化建模，就很难进入训练闭环；执行器参数会成为机器人公司隐藏但关键的工程资产。

### 3. [HandUMI 软件 7 月 19 日更新：机器人采数接口从固定工位走向可穿戴](https://github.com/robonet-ai/handumi-sw)

**摘要：** robonet-ai/handumi-sw 7 月 19 日有推送。README 显示，HandUMI 软件覆盖同步数据采集、校准、验证、回放、遥操作和机器人重定向，核心流程是 tracking、cameras、gripper widths 进入 synchronized raw dataset，再进行 validate、convert 和 replay。

- **核心价值：** 数据相关报道：大会展示之后最重要的是持续采数；可穿戴采集接口能把双臂操作数据从固定机器人工作站中释放出来。

---

## 🏢 机器人公司情报

### 1. [WAIC 主办与承办架构：上海继续把 AI 大会作为产业协同平台](https://www.worldaic.com.cn/)

**摘要：** WAIC 官方页面列出多部委、中科院、中国科协和上海市人民政府作为主办单位，上海市经信委、发改委、科委、浦东新区、徐汇区和东浩兰生集团等作为承办单位。对机器人产业链而言，这种组织结构意味着展览、政策、产业招商、应用场景和开发者生态会被放在同一平台上组织。

- **核心价值：** 具身智能不是单家公司能单独推起来的市场；它需要政策、场景、供应链、数据和资本共同形成试验场。

### 2. [RoboParty：全开源 DIY 人形本体继续代表国产开放工程路线](https://github.com/Roboparty/roboto_origin)

**摘要：** Roboparty/roboto_origin 7 月 15 日有推送，星标约 2054。README 显示，ROBOTO_ORIGIN 是 fully open-source DIY humanoid robot，聚合机械结构、CAD、PCB、BOM、ROS2 部署、训练环境、URDF/MJCF、固件、导航和 XR 遥操作等子仓库。

- **核心价值：** 国产人形机器人如果要建立开发者生态，公开本体工程细节比单纯发布演示视频更有长期价值。

### 3. [robot-descriptions：URDF/MJCF 索引继续成为跨本体评测入口](https://github.com/robot-descriptions/awesome-robot-descriptions)

**摘要：** robot-descriptions/awesome-robot-descriptions 7 月 17 日有推送，星标约 1595。项目整理 URDF、Xacro、MJCF 等机器人描述文件，并标注 visuals、inertias、collisions 和 license，覆盖机械臂、双足、人形、移动操作、四足、轮式和末端执行器等类别。

- **核心价值：** 数据相关报道：跨本体评测需要先有可靠的本体描述；惯量、碰撞和许可信息不完整，会直接影响仿真数据和策略评估质量。

---

## 结尾总结

7 月 19 日的主线可以概括为：WAIC 正在提供一个观察具身智能产业成熟度的窗口。真正值得看的不是哪台机器人最吸睛，而是哪套系统已经具备本体复现、数据采集、控制闭环、零部件建模、仿真评测和场景部署能力。LeRobot、OpenArm、Isaac Lab-Arena、PACE、HandUMI 与 robot-descriptions 的近期活跃说明，具身智能的基础设施正在逐层补齐。大会热度会过去，留下来的会是可复用的数据、可验证的本体和可部署的工程栈。

> 💬 如果你去 WAIC 看具身机器人，你会优先看什么：整机外观、现场任务完成度、数据采集能力、控制稳定性、零部件供应链，还是真实客户场景？

## 关键词索引

**公司 / 机构：** WAIC / 世界人工智能大会 / 上海市人民政府 / Hugging Face / NVIDIA Isaac Lab / Enactic / OpenArm / RoboParty / ETH Zurich RSL / Robonet AI

**项目 / 论文：** LeRobot / OpenArm / Isaac Lab-Arena / PACE / HandUMI / robot-descriptions / Roboto Origin / Jetson-PI / NeuralActuator / Robust bipedal locomotion / Whole-Body Social Tactile Sensing

**技术：** 具身智能 / 世界人工智能大会 / WAIC / 人形机器人 / 机器人本体 / LeRobotDataset / robot embodiment / sim2real / actuator dynamics / onboard VLA / tactile sensing / URDF / MJCF / 数据闭环 / 仿真评测

## 值得分享

1. WAIC 的具身智能看点不是单台机器人，而是本体、数据、控制、零部件和场景能否形成闭环。
2. 开源基础设施正在接住大会热度：LeRobot、OpenArm、Isaac Lab-Arena 和 robot-descriptions 都在解决“展示之后如何复现”。
3. 数据闭环决定长期价值：PACE 建模执行器，HandUMI 采集双臂数据，LeRobot 标准化数据格式，都是机器人从展台走向现场的底层能力。
