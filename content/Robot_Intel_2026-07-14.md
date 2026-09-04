# 具身智能情报前沿｜轮式双臂平台进入仿真栈

**作者：具身视界** · 2026.07.14

---

> 今天最值得关注的变化，是轮式双臂移动平台正在从“硬件本体展示”走向“可仿真、可控制、可采数、可部署”的工程栈。OpenFleX 把移动底盘、升降机构、双臂和头部整合进 MuJoCo，OpenAMRobot、RoSys 和移动操作论文则共同说明：下一阶段的移动操作竞争，核心不只是机械结构，而是本体、仿真、数据和现场控制能否打通。

## 💥 今日重磅

### 1. [OpenFleX 开源 MuJoCo 全身模型：轮式底盘 + 升降 + 双臂 + 头部进入可控仿真](https://github.com/OpenFleX-Wheeled-Humanoid/openflex_mujoco)

**摘要：** OpenFleX-Wheeled-Humanoid/openflex_mujoco 7 月 13 日仍有推送，仓库说明显示，该项目把 OpenFlex v10 全身机器人模型从 ROS2/RViz 转换为可直接在 MuJoCo viewer 打开的自包含 MJCF，形态覆盖 mobile base、lift、dual arms 和 head。项目提交了 `openflex_mujoco.xml`、`openflex_mujoco_selfcol.xml` 和 `mujoco_meshes/`，普通克隆后无需重新跑转换脚本即可查看；如需跟随上游模型，可通过 5 个 submodule 重新编译 xacro/URDF，再转换成 MuJoCo。更关键的是，转换脚本补回了 MuJoCo 导入 URDF 时会丢失的 gripper mimic coupling，并注入 23 个 position actuators，覆盖 14 个手臂关节、2 个主夹爪、2 个头部关节、1 个升降和 4 个转向关节。

- **核心价值：** 轮式双臂移动平台的研发正在从“画 URDF、看 RViz”进入“能做碰撞、能调关节、能接策略”的仿真阶段；这会影响移动操作算法团队、低成本硬件团队和想做仓储/服务场景验证的开发者。
- **行业判断：** 下一批移动操作平台的分水岭，不是有没有双臂，而是能否把整机模型、碰撞、夹爪耦合、升降自由度和控制接口做成可复用资产。

---

## 📰 行业新闻

### 1. [OpenAMRobot v0.0.1 生态拆分：低成本 AMR 正在向双臂移动操作平台演进](https://github.com/openAMRobot/openamr)

**摘要：** openAMRobot/openamr 7 月 12 日有推送，GitHub 星标约 120。README 显示，OpenAMRobot 已从单体仓库转向模块化生态，拆分为硬件、软件、固件、接口、通信、UI 和文档等仓库；其定位也从低成本 AMR 扩展为 Physical AI development platform，覆盖 teleoperation、data collection、imitation learning、deployment 和 mobile manipulation。原有 AMR 指标包括差速底盘、约 60 kg 车重、600 x 800 mm 尺寸、最高 150 kg 载荷、8 小时电池和自动充电能力。

- **核心价值：** 数据相关报道：OpenAMRobot 把示教、ROS bag 记录、数据集生成、模仿学习和策略部署写进平台能力，说明轮式移动平台正在从物流底盘升级为可采数、可训练的具身智能底座。

### 2. [Ati Motors 更新 Sherpa-Research：室内外 AMR 研究平台强调可换算力、传感器和执行器](https://github.com/AtiMotors/Sherpa-Research)

**摘要：** AtiMotors/Sherpa-Research 7 月 13 日有推送。README 显示，Sherpa Research 面向 autonomous mobile robots 和 multi-robot navigation 研究，定位为模块化 drive-by-wire Indoor / Outdoor AMR，允许研究人员集成自选 compute、sensors 和 actuators。当前文档列出 Raspberry Pi 5 + RPLidar C1、Jetson Orin Nano + Livox MID-360 两类版本，并支持 ROS 与 ROS2 相关资料。

- **核心价值：** 对移动操作平台来说，底盘不再只是承载结构；开放算力、传感器和执行器接口，才有机会承接双臂、视觉模型和场景任务的持续迭代。

### 3. [RoSys 持续活跃：移动机器人控制系统转向 Web UI、仿真和 Python 工作流](https://github.com/zauberzeug/rosys)

**摘要：** zauberzeug/rosys 7 月 13 日有推送，GitHub 星标约 128。RoSys 是一个面向移动机器人的 all-Python robot system，基于 NiceGUI 和现代 Web 技术，提供模块化事件系统、自动化任务、持久化、仿真模式、pytest 集成测试和浏览器操作界面。README 强调，其目标类似 ROS，但更关注移动机器人业务逻辑和离线可操作的人机界面。

- **核心价值：** 轮式双臂平台进入真实场景后，需要的不只是控制器，还包括调试界面、远程运维、仿真测试和任务自动化；Web 化机器人系统会降低现场集成门槛。

---

## 📚 前沿论文

### 1. [Multi-Agent Robotic Control with Onboard Vision-Language Models：本地 VLM 控制移动操作机器人](https://arxiv.org/abs/2607.07403)

**摘要：** 7 月 8 日提交的论文提出一种多智能体机器人控制系统，用 onboard vision-language models 控制多用途 autonomous mobile manipulator，并在模拟工业仓库中验证安全检查、仓库维护、仓库搜索、包裹质量核验和响应人类请求等任务。论文重点不是把大模型放在云端，而是在本地算力约束下组织感知、规划和控制代理。

- **核心价值：** 轮式移动操作平台要进入仓储和工业场景，必须处理导航、识别、任务分解和执行闭环；本地 VLM 路线把“能看懂现场”和“能移动执行”放到同一控制架构里。

### 2. [Validating Virtual Reality for Studying Multimodal HRI：用 PR2 移动操作机器人验证 VR 社交导航实验](https://arxiv.org/abs/2607.09261)

**摘要：** 7 月 10 日提交的论文研究 VR 是否可以可靠用于多模态人机交互和 socially aware robot navigation 实验。研究让参与者分别在真实动捕空间和 VR 复刻空间中与 PR2 mobile manipulator 互动，并比较社交感知、舒适度、轨迹和头部朝向等行为差异。

- **核心价值：** 移动操作机器人进入家庭、医院、办公室等人类空间后，评测不只看导航成功率，还要看人是否感到安全和自然；VR 可降低早期 HRI 数据采集与实验成本。

### 3. [FlowDAgger：用少量人类干预适配生成式机器人策略](https://arxiv.org/abs/2607.08877)

**摘要：** 7 月 9 日提交的 FlowDAgger 关注 human-in-the-loop adaptation，把冻结的生成式机器人策略放在 latent space 中进行在线适配，并在真实双臂和单臂操作任务上验证。项目页已开放：[microsoft.github.io/FlowDAgger](https://microsoft.github.io/FlowDAgger/)。

- **核心价值：** 数据相关报道：轮式双臂平台进入开放场景后，完全离线训练很难覆盖所有失败；少量人类干预形成的部署数据，会成为现场策略快速修正的重要来源。

### 4. [EgoWAM：用野外第一视角人类数据训练双臂世界动作模型](https://arxiv.org/abs/2607.08436)

**摘要：** 7 月 8 日提交的 EgoWAM 研究 world action models beyond pixels，强调使用 in-the-wild egocentric human data 支撑真实双臂任务学习。项目页显示，论文关注如何让模型从人类第一视角数据中获得动作预测能力，并提升对新物体和新场景的泛化。项目页：[gatech-rl2.github.io/egowam.github.io](https://gatech-rl2.github.io/egowam.github.io/)。

- **核心价值：** 双臂移动平台如果要处理货架、厨房、实验室和服务场景，不能只依赖固定工位示教；第一视角人类数据可能成为低成本扩展任务覆盖面的训练来源。

---

## 🧩 开源生态

### 1. [openflex_mujoco：把 ROS2/RViz 本体资产转成 MuJoCo 可执行资产](https://github.com/OpenFleX-Wheeled-Humanoid/openflex_mujoco)

**摘要：** openflex_mujoco 的关键价值在于把上游 xacro/URDF、mesh、夹爪 mimic coupling、碰撞设置和 actuator 注入流程固化下来。仓库提供 floor-only 和 full self-collision 两个构建版本，其中 full self-collision 保留手臂与身体/底盘/升降柱/头部之间的碰撞，同时排除非手臂刚体之间的内建 mesh 重叠，以避免启动抖动。

- **核心价值：** 移动双臂机器人做策略训练时，碰撞建模不是细节；夹爪、升降和底盘自碰撞如果不可控，仿真数据会很难迁移到真机。

### 2. [OpenAMRobot：从开源 AMR 走向 Physical AI 平台化](https://github.com/openAMRobot/openamr)

**摘要：** OpenAMRobot README 把平台能力明确分成 reference hardware、ROS 2 software infrastructure 和 Physical AI infrastructure，覆盖 autonomous mobile robot platform、dual-arm mobile manipulation、adjustable lift systems、navigation、autodocking、teleoperation、simulation、demonstration data collection 和 imitation learning pipelines。

- **核心价值：** 对中小团队而言，移动操作的门槛不在单个算法，而在硬件、固件、导航、UI、数据和训练链路同时可用；模块化开源生态会加速低成本样机验证。

### 3. [RoSys：用 Web 技术重构移动机器人高层系统](https://github.com/zauberzeug/rosys)

**摘要：** RoSys 提供仿真模式、自动化任务、事件系统和浏览器 UI，并建议安全相关动作放在微控制器侧，高层业务逻辑则用 Python 和 WebSocket 组织。对移动底盘和现场机器人来说，这种架构便于快速开发巡检、搬运、遥控和调试界面。

- **核心价值：** 移动操作平台的产品化，需要让非算法工程师也能看状态、改任务、复现实验和定位故障；UI 与仿真并重会成为开发者工具链的一部分。

---

## 🏢 机器人公司情报

### 1. [成都长枢机器人：OpenFleX 生态继续补齐仿真与开发者入口](https://github.com/OpenFleX-Wheeled-Humanoid/openflex_mujoco)

**摘要：** openflex_mujoco README 标注项目属于 OpenFlex full-body humanoid robot platform ecosystem，版权方为 Chengdu Changshu Robot Co., Ltd.，并提供 openarmx.com 与 docs.openarmx.com 文档入口。相比只发布硬件图片，把全身模型、MuJoCo XML 和转换脚本开放出来，更接近面向研究与工业应用的开发者入口。

- **核心价值：** 轮式双臂平台要建立生态，必须让外部开发者能低成本复现本体、调策略和验证碰撞；仿真资产是硬件公司走向平台公司的第一层接口。

### 2. [OpenAMRobot：用赞助和模块化仓库探索开源机器人商业化](https://github.com/openAMRobot/openamr)

**摘要：** OpenAMRobot 在 README 中列出一次性赞助和月度订阅层级，同时把仓库拆成硬件、软件、固件、UI、通信和文档等模块。其目标用户包括 robotics startups、universities、research laboratories、corporate innovation teams 和 venture builders。

- **核心价值：** 低成本移动操作平台可能先从“开源硬件 + 文档 + 社区支持 + 专业咨询”切入，而不是一开始就卖封闭整机。

### 3. [Ati Motors：Sherpa Research 把商用 AMR 经验开放给研究场景](https://github.com/AtiMotors/Sherpa-Research)

**摘要：** Ati Motors 在 Sherpa-Research README 中介绍自己是位于班加罗尔的 Autonomous Mobile Robotics 公司，业务覆盖 AI、电力电子、控制、机械、系统软件、电子和制造，并开发 Sherpa 系列 AMR。Sherpa Research 则面向高校和研发团队，提供可改算力和传感器的研究底盘。

- **核心价值：** 商用 AMR 公司开放研究平台，有助于把室内外导航、多机器人协同和移动操作扩展研究连接到真实产业底盘。

---

## 结尾总结

7 月 14 日的主线可以概括为：轮式双臂移动平台正在补齐“整机可仿真、底盘可扩展、策略可适配、数据可闭环”的工程基础。OpenFleX 解决的是全身本体进入 MuJoCo 的第一步，OpenAMRobot 和 RoSys 说明低成本移动平台需要完整工具链，VLM、VR HRI、FlowDAgger 和 EgoWAM 则把控制、交互、数据和适配问题推到同一张桌面上。接下来谁能把移动底盘、升降、双臂、夹爪、视觉和任务数据稳定连起来，谁就更接近可复制的移动操作产品。

> 💬 你认为轮式双臂平台最先规模化落地的场景会是哪一个：仓储拣选、实验室自动化、商超补货、医院后勤，还是家庭服务？

## 关键词索引

**公司 / 机构：** OpenFleX / Chengdu Changshu Robot Co., Ltd. / OpenAMRobot / Ati Motors / Zauberzeug / Microsoft / Georgia Tech

**项目 / 论文：** openflex_mujoco / OpenAMRobot / Sherpa-Research / RoSys / Multi-Agent Robotic Control with Onboard Vision-Language Models / FlowDAgger / EgoWAM / PR2 mobile manipulator

**技术：** 轮式双臂移动平台 / mobile manipulation / MuJoCo / MJCF / ROS2 / RViz / URDF / xacro / gripper coupling / self-collision / onboard VLM / human-in-the-loop / egocentric human data / VR HRI / demonstration data collection

## 值得分享

1. 轮式双臂平台开始补齐仿真资产：OpenFleX 已把 mobile base、lift、dual arms 和 head 转成可直接打开的 MuJoCo MJCF。
2. 移动操作的竞争点正在从本体转向工程栈：底盘、升降、双臂、夹爪、碰撞、数据采集和部署接口必须一起可用。
3. 数据闭环会决定平台价值：OpenAMRobot、FlowDAgger 和 EgoWAM 都指向同一件事，真实示教、人类干预和第一视角数据正在成为移动操作系统的训练燃料。
