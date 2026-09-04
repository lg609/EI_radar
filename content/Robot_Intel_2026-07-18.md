# 具身智能情报前沿｜开源本体走向可复现

**作者：具身视界** · 2026.07.18

---

> 今天最值得关注的变化，是具身机器人本体正在从“单台硬件展示”走向“可购买、可装配、可仿真、可遥操作、可采数、可复现实验”的工程资产。OpenArm 把 7DOF 人形手臂拆成硬件、描述、CAN、ROS2、遥操作、Isaac Lab、MuJoCo 和数据集仓库，Roboto Origin、robot descriptions 和 Isaac Lab-Arena 则说明：本体生态正在变成模型落地的公共底座。

## 💥 今日重磅

### 1. [OpenArm 7 月 16 日更新：7DOF 人形手臂把本体、仿真、遥操作和数据集打包开放](https://github.com/enactic/openarm)

**摘要：** GitHub API 显示，enactic/openarm 7 月 16 日有推送，星标约 2733，Apache-2.0 许可。README 将 OpenArm 定义为面向 physical AI research 和 contact-rich deployment 的开源 7DOF humanoid arm，强调 human-scale proportions、高 backdrivability、compliance、安全人机交互和实际 payload 能力。项目给出一个关键价格信号：完整双臂系统约 6500 美元。更重要的是，它不是只开放一套机械结构，而是把本体拆成多个工程入口：openarm_hardware 提供 CAD、STL、STEP 和 Fusion 360 assembly；openarm_description 提供 URDF/xacro；openarm_can 提供底层电机 CAN 通信；openarm_ros2 提供 ROS2 节点；openarm_teleop 支持单向和双向遥操作；openarm_isaac_lab 与 openarm_mujoco 支持仿真；openarm_dataset 和 dora-openarm 则服务数据采集、推理和遥操作。OpenArm Cell 还定义了统一背景、光照和相机摆放的标准化环境。

- **核心价值：** 数据相关报道：本体开源不再只是“给 CAD”，而是要把本体描述、控制接口、仿真资产、采集环境和数据格式一起开放，才能让不同实验室复现实验并积累可比较数据。
- **行业判断：** 下一阶段开源机器人本体的门槛，会从“能不能造出来”转向“能不能成为模型训练、评测和部署的标准身体”。

---

## 📰 行业新闻

### 1. [Roboto Origin 7 月 15 日更新：全开源 DIY 人形机器人把结构、电子、训练和部署一起开放](https://github.com/Roboparty/roboto_origin)

**摘要：** Roboparty/roboto_origin 7 月 15 日有推送，星标约 2045。README 显示，ROBOTO_ORIGIN 是 fully open-source DIY humanoid robot，项目方为上海 RoboParty Technology Co., Ltd.，称其从 2025 年 4 月开始研发并在四个月内完成原型机。仓库定位为核心子仓库的日更快照聚合，覆盖机械结构、CAD、PCB、BOM、ROS2 部署、训练环境、URDF/MJCF、固件、导航和 XR 遥操作等模块。

- **核心价值：** 人形本体开源正在从“展示外壳”走向“结构、电控、训练、部署和仿真描述全链路透明”，这会降低开发者理解整机工程的门槛。

### 2. [Isaac Lab-Arena 7 月 18 日更新：把 Scene、Embodiment、Task 做成可组合评测单元](https://github.com/isaac-sim/IsaacLab-Arena)

**摘要：** isaac-sim/IsaacLab-Arena 7 月 18 日有推送，星标约 486。README 显示，Arena 是 NVIDIA Isaac Lab 的开源扩展，用于简化机器人任务整理和策略评测，核心是把环境拆成三个可复用原语：Scene、Embodiment 和 Task。开发者可以在不复制大量配置的情况下更换机器人本体、对象或场景，并支持长时序任务链、自然语言物体摆放和大规模并行评测。

- **核心价值：** 本体开始成为仿真评测中的一等公民；当模型需要跨本体评估时，谁能快速替换 robot embodiment，谁就能更快比较策略泛化能力。

### 3. [LeRobot Anything U-Arm 7 月 15 日更新：低成本遥操作系统尝试覆盖 95% 商用机械臂](https://github.com/MINT-SJTU/LeRobot-Anything-U-Arm)

**摘要：** MINT-SJTU/LeRobot-Anything-U-Arm 7 月 15 日有推送，星标约 296。README 将其定位为低成本、通用 leader-follower teleoperation system，目标是用三种硬件配置适配大多数商用机械臂，并标注“starts from 60$”。项目强调 ROS1 集成、低延迟关节空间控制、可扩展 follower-arm 接口和仿真测试，近期说明中还提到加入 OpenArm-based dual-arm teleoperation support。

- **核心价值：** 机械臂本体生态的关键不只是硬件本身，还包括低成本示教和遥操作接口；通用遥操作会让更多存量机械臂进入具身数据闭环。

---

## 📚 前沿论文

### 1. [Robust bipedal locomotion on flowable slopes：双足本体开始处理可流动坡面接触](https://arxiv.org/abs/2607.11855)

**摘要：** 7 月 13 日提交的论文研究双足机器人在 flowable slopes 上的鲁棒行走。论文指出，双足机器人本身接近不稳定状态，足地接触的微小变化就可能破坏步态；在刚性地形上可以依赖成熟接触模型，但可流动坡面会放大接触不确定性。

- **核心价值：** 双足本体能力不只看关节数和外观，足端、接触建模和地形交互决定它能否进入真实复杂环境。

### 2. [Towards Human-level Dexterous Teleoperation：灵巧手本体需要支持工具使用、换抓和指间步态](https://arxiv.org/abs/2607.11481)

**摘要：** 7 月 13 日提交的论文关注接近人类水平的 dexterous teleoperation。论文指出，人类能够在单手内完成工具使用、换抓、物体重新定位和 finger gaiting，而机器人灵巧手要达到这一水平，必须处理复杂接触转换和高维手部动作。

- **核心价值：** 人形本体不是只有腿和躯干；灵巧手是否能承接高质量遥操作和复杂接触，会直接决定整机能做什么任务。

### 3. [TAC-LOCO：四足本体把触觉纳入全身移动操作](https://arxiv.org/abs/2607.10132)

**摘要：** 7 月 11 日提交的 TAC-LOCO 研究 quadrupedal tactile-informed loco-manipulation，关注腿足机器人在抓取物体时如何协调全身运动，并在未知外力下保持稳定接触。论文把触觉从手部操作扩展到四足机器人全身移动操作控制。

- **核心价值：** 本体形态正在从“移动底盘 + 机械臂”扩展为“身体本身参与操作”；触觉、足端、躯干和夹持对象会共同影响动作策略。

### 4. [Whole-Body Social Tactile Sensing：社交服务本体需要从需求反推触觉皮肤](https://arxiv.org/abs/2607.11690)

**摘要：** 7 月 13 日提交的论文提出 requirement-driven whole-body social tactile sensing。论文指出，传统触觉系统常由硬件预设布局驱动，限制了覆盖范围、空间分辨率和可识别交互手势；社交物理人机交互需要从任务需求反推全身触觉布局。

- **核心价值：** 服务型人形本体的差异化可能来自全身皮肤，而不是只来自头部表情或手部自由度；触觉覆盖会影响安全交互和场景接受度。

---

## 🧩 开源生态

### 1. [awesome-robot-descriptions 7 月 17 日更新：URDF/MJCF 本体描述成为公共资产索引](https://github.com/robot-descriptions/awesome-robot-descriptions)

**摘要：** robot-descriptions/awesome-robot-descriptions 7 月 17 日有推送，星标约 1595。README 显示，该项目整理 URDF、Xacro、MJCF 等机器人描述文件，并按 Arms、Bipeds、Dual Arms、Humanoids、Mobile Manipulators、Quadrupeds、Wheeled、End Effectors 等类别组织，同时标注 license、visuals、inertias 和 collisions。

- **核心价值：** 数据相关报道：本体描述文件是机器人数据和仿真的入口；如果 URDF/MJCF 缺少惯量、碰撞或许可信息，下游训练和评测就很难稳定复现。

### 2. [fiveages robot_descriptions 7 月 17 日更新：人形、四足和机械臂 ROS2 描述包集中化](https://github.com/fiveages-sim/robot_descriptions)

**摘要：** fiveages-sim/robot_descriptions 7 月 17 日有推送，星标约 72。README 显示，该仓库收集 humanoid、quadruped 和 manipulator 的 URDF 文件，并按 ROS2 package 组织，部分模型还经过 Blender 重新上色。列表包含 DexForce W1、智元 G1、Airbot MMK2、Astribot S1、Galaxea R1/R1 Pro、Realman AIDAL 等轮式人形或人形相关本体。

- **核心价值：** 国内外机器人本体开始形成可下载、可渲染、可比较的描述包集合；这会加速仿真、教学、视觉识别和策略迁移测试。

### 3. [Teleopit 7 月 16 日更新：Unitree G1 全身遥操作把本体模型、VR 和真机录制连起来](https://github.com/BotRunner64/Teleopit)

**摘要：** BotRunner64/Teleopit 7 月 16 日有推送，星标约 132。README 将其定义为轻量、可扩展的 humanoid whole-body teleoperation framework，支持从 BVH 或 Pico 4 VR 到 Unitree G1 的实时动作重定向，可在 MuJoCo 仿真或真实硬件上运行。项目使用统一的 Unitree G1 `g1_29dof.xml`，并支持 Pico sim2real HDF5 录制，记录低维状态、模式、动作和视频同步元数据。

- **核心价值：** 数据相关报道：本体数据采集正在从单关节日志走向全身动作、VR 参考、相机视频和 HDF5 schema 的组合；这类数据会决定人形本体能否持续训练。

---

## 🏢 机器人公司情报

### 1. [Enactic / OpenArm：把人形手臂做成开放本体生态](https://github.com/enactic/openarm)

**摘要：** OpenArm README 提供官网、文档、采购入口和社区入口，并列出硬件、控制、仿真、遥操作、数据集等子仓库。其价值不只是降低单套双臂价格，而是提供可复现的 physical AI 本体基准。

- **核心价值：** 对创业公司和实验室来说，OpenArm 这类开放本体能减少从零搭建双臂平台的时间，把研发重点转向策略、数据和任务验证。

### 2. [RoboParty：全开源 DIY 人形机器人把国产本体工程公开到子仓库层级](https://github.com/Roboparty/roboto_origin)

**摘要：** Roboto Origin README 显示，项目方将机械、电子、训练、部署和外观等模块拆分为子仓库，并说明可通过淘宝采购和嘉立创打样实现 DIY 组装。虽然这种路线仍需要较强工程能力，但它把人形机器人本体研发过程以较高颗粒度公开出来。

- **核心价值：** 国产人形本体如果能形成开放知识库，会让更多开发者理解结构、电控、固件和训练之间的真实耦合关系。

### 3. [Unitree G1 社区生态：从导航到全身遥操作，G1 成为高频实验本体](https://github.com/BotRunner64/Teleopit)

**摘要：** 近一周 GitHub 中出现多条 Unitree G1 相关项目，包括 Teleopit 全身遥操作、g1_real_ws 导航适配、mjlab-homierl 下肢运动训练复现等。它们共同说明 G1 正在成为开发者用于导航、遥操作、仿真到真机和人形运动控制的常用本体。

- **核心价值：** 一旦某个本体拥有足够多社区工具，算法团队就更容易在同一硬件上比较结果，形成事实上的实验平台。

---

## 结尾总结

7 月 18 日的主线可以概括为：具身机器人本体正在从“厂商展示的整机”变成“开发者可复现的身体资产”。OpenArm 把人形手臂拆成硬件、描述、控制、仿真、遥操作和数据集，Roboto Origin 把 DIY 人形整机拆到结构、电控、固件和训练子仓库，robot descriptions 与 Isaac Lab-Arena 则把本体纳入可检索、可组合、可评测的公共基础设施。接下来，真正有生命力的机器人本体，不只是能跑 demo，而是能被更多团队复现、采数、训练、评测和改造。

> 💬 你认为最适合作为具身智能公共实验本体的是哪一类：开源双臂、人形整机、Unitree G1 这类商用人形、四足移动操作平台，还是低成本机械臂？

## 关键词索引

**公司 / 机构：** Enactic / OpenArm / RoboParty / NVIDIA Isaac Lab / Unitree / robot-descriptions / fiveages-sim / MINT-SJTU

**项目 / 论文：** OpenArm / Roboto Origin / Isaac Lab-Arena / LeRobot Anything U-Arm / awesome-robot-descriptions / fiveages robot_descriptions / Teleopit / Robust bipedal locomotion / Towards Human-level Dexterous Teleoperation / TAC-LOCO / Whole-Body Social Tactile Sensing

**技术：** 机器人本体 / humanoid embodiment / 7DOF humanoid arm / URDF / Xacro / MJCF / ROS2 package / Isaac Lab / MuJoCo / CAN control / whole-body teleoperation / robot description / bipedal locomotion / dexterous teleoperation / tactile sensing / sim2real HDF5

## 值得分享

1. 开源本体开始平台化：OpenArm 约 6500 美元双臂系统，同时开放硬件、URDF/xacro、CAN、ROS2、遥操作、Isaac Lab、MuJoCo 和数据集入口。
2. 人形整机也在走向开放工程：Roboto Origin 把结构、电控、训练、部署、URDF/MJCF、固件和 XR 遥操作拆成子仓库。
3. 本体描述文件正在成为数据入口：URDF/MJCF 的惯量、碰撞、视觉和许可信息，决定模型训练和仿真评测能否复现。
