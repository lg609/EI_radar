# 具身智能情报前沿｜WAIC 筛选本体工程栈

**作者：具身视界** · 2026.07.20

---

> 今天最值得关注的变化，是 WAIC 把具身机器人从“看一台机器表演”推向“看一套本体工程栈是否成立”。官方页面显示，2026 世界人工智能大会于 7 月 17-20 日在中国上海举行，主题为“智能伙伴 共创未来”。对机器人公司来说，展台只是入口，本体、控制、仿真、数据和供应链能否被连续验证，才是明天真正值得写的主线。

## 💥 今日重磅

### 1. [WAIC 进入 7 月 20 日收官窗口：机器人本体从展示件变成工程能力考场](https://www.worldaic.com.cn/)

**摘要：** WAIC 官方网站显示，2026 世界人工智能大会时间为 7 月 17 日至 7 月 20 日，地点为中国上海，主题为“智能伙伴 共创未来”，页面设置论坛活动、新闻、展览亮点、大会生态、合作伙伴等模块，并列出多部委、中科院、中国科协和上海市人民政府等主办单位。对具身智能行业而言，7 月 20 日的关键不是“又有多少机器人亮相”，而是同一批本体能否经受工程化追问：是否有可复现机械结构，是否有 URDF/MJCF 等本体描述，是否能接入仿真评测，是否支持真机采数和模型训练，是否能在展台之外进入客户场景。过去一周 OpenArm、Roboto Origin、robot-descriptions、IsaacLab-Arena、LeRobot 和 HandUMI 持续活跃，正好构成一套可观察的本体工程栈。

- **来源：** 世界人工智能大会官网
- **核心价值：** WAIC 正在把机器人本体从“硬件外观竞争”推向“工程栈完整度竞争”；谁能让本体被描述、仿真、采数、训练和部署，谁才更接近产业化。
- **行业判断：** 具身智能的下一轮竞争，不只是人形机器人站得稳、走得像人，而是本体能否成为可复制的数据生产平台。

---

## 📰 行业新闻

### 1. [WAIC 论坛页面持续开放：机器人议题被放入产业生态议程](https://www.worldaic.com.cn/events/forum)

**摘要：** WAIC 官方论坛页可访问，页面提供 2026 论坛、筛选和搜索入口。对具身机器人从业者来说，这意味着机器人不再只是展台设备，而是要与大模型、算力、数据、治理、应用和开发者生态一起被组织讨论。论坛化的意义在于，机器人本体的价值会被放到产业链协同中评估。

- **来源：** 世界人工智能大会官网
- **核心价值：** 本体公司如果只讲单机性能，很难穿透客户决策；能解释场景、数据、安全和维护责任的方案，才更容易被产业方理解。

### 2. [WAIC 展商页面可访问：具身机器人进入集中比较窗口](https://www.worldaic.com.cn/exhibitors)

**摘要：** WAIC 官方展商页面可访问，并提供 exhibitor 相关页面入口。对于机器人本体方向，展会的价值在于让整机、零部件、算法平台和行业客户在同一窗口比较：同样是人形或双臂平台，真正拉开差距的往往不是外形，而是负载、续航、关节可靠性、接口开放度和二次开发成本。

- **来源：** 世界人工智能大会官网
- **核心价值：** 展商集中展示会压缩信息不对称，推动客户从“看演示视频”转向“问接口、问维护、问数据、问交付”。

### 3. [LeRobot 7 月 19 日仍有推送：开源数据工具链成为展会之后的沉淀层](https://github.com/huggingface/lerobot)

**摘要：** GitHub API 显示，huggingface/lerobot 7 月 19 日有推送，星标约 25947。项目定位为让机器人端到端学习更易用，围绕机器人数据集、模型训练、真实机器人接口和 Hugging Face Hub 生态展开。WAIC 现场能制造关注，但真正的行业资产要在展后沉淀到数据格式、训练流程和复现实验中。

- **来源：** GitHub
- **核心价值：** 数据相关报道：LeRobot 代表的是具身智能的数据基础设施，能把不同本体上的采集数据转化为可训练、可共享、可复用的模型资产。

---

## 📚 前沿论文

### 1. [Jetson-PI：机载实时 VLA 让本体能力不再依赖云端](https://arxiv.org/abs/2607.12659)

**摘要：** 7 月 14 日提交的 Jetson-PI 面向 onboard real-time robot control，关注在 Jetson Orin 等低功耗机载设备上部署 VLA。论文指出，VLA 推理复杂度会带来闭环控制延迟，因此提出 foresight-aligned asynchronous inference，让模型推理调度更贴近机器人动作执行时序。

- **来源：** arXiv
- **核心价值：** WAIC 上的人形本体如果要走向真实场景，必须摆脱“展台联网演示”的脆弱性；机载实时推理会直接决定本体能否独立工作。

### 2. [Human-level Dexterous Teleoperation：高质量遥操作数据继续决定灵巧本体上限](https://arxiv.org/abs/2607.11481)

**摘要：** 7 月 13 日提交的论文关注 human-level dexterous teleoperation for robotic hands。灵巧手和人形上肢的难点不只是硬件自由度，而是如何让人的操作意图、接触状态和手指协调稳定迁移到机器人本体上。遥操作系统越接近人类水平，越可能生成可用于模仿学习的高质量操作数据。

- **来源：** arXiv
- **核心价值：** 数据相关报道：本体不是数据的被动承载物，遥操作接口、手部映射和接触反馈会直接决定灵巧操作训练数据的质量。

### 3. [Robust bipedal locomotion on flowable slopes：双足本体开始面对非刚性地形](https://arxiv.org/abs/2607.11855)

**摘要：** 7 月 13 日提交的论文研究双足机器人在 flowable slopes 上的鲁棒行走。论文指出，双足系统接近不稳定状态，足地接触的微小变化都可能破坏步态；当坡面可流动时，接触不确定性会进一步放大。这个问题直指人形本体从平整展台走向真实地面的关键障碍。

- **来源：** arXiv
- **核心价值：** 本体能力不能只用平地行走视频证明；足端接触、地面适应和动态稳定性会成为人形机器人商业部署的硬门槛。

---

## 🧩 开源生态

### 1. [OpenArm：开源 7DOF 仿人手臂继续提供可复现本体样板](https://github.com/enactic/openarm)

**摘要：** GitHub API 显示，enactic/openarm 7 月 16 日有推送，星标约 2739。项目描述为面向 physical AI research and deployment in contact-rich environments 的 fully open-source humanoid arm，并在 README 中给出双臂系统约 6500 美元的成本信息，覆盖硬件、URDF/xacro、CAN、ROS2、遥操作、仿真和数据等子模块。

- **来源：** GitHub
- **核心价值：** OpenArm 的意义不只是便宜，而是把人形上肢从展示硬件拆成可制造、可描述、可控制、可采数的工程组件。

### 2. [Roboto Origin：国产 DIY 人形本体继续补齐全开源工程细节](https://github.com/Roboparty/roboto_origin)

**摘要：** GitHub API 显示，Roboparty/roboto_origin 7 月 15 日有推送，星标约 2054。项目描述为 Fully Open-Source DIY Humanoid Robot，README 聚合机械结构、CAD、PCB、BOM、ROS2 部署、训练环境、URDF/MJCF、固件、导航和 XR 遥操作等内容。

- **来源：** GitHub
- **核心价值：** 国产人形机器人生态要吸引开发者，不能只发布整机视频；开放 BOM、描述文件、固件和训练环境，才有机会形成外部共创。

### 3. [robot-descriptions：URDF/MJCF 索引成为跨本体评测入口](https://github.com/robot-descriptions/awesome-robot-descriptions)

**摘要：** GitHub API 显示，robot-descriptions/awesome-robot-descriptions 7 月 17 日有推送，星标约 1595。项目整理 URDF、Xacro、MJCF 等机器人描述文件，并标注 visuals、inertias、collisions 和 license，覆盖机械臂、双足、人形、移动操作、四足、轮式和末端执行器等类别。

- **来源：** GitHub
- **核心价值：** 数据相关报道：跨本体训练和评测首先依赖可靠的本体描述；惯量、碰撞和许可信息不完整，会直接污染仿真数据和策略对比结果。

### 4. [Isaac Lab-Arena：可组合仿真评测开始服务多本体策略验证](https://github.com/isaac-sim/IsaacLab-Arena)

**摘要：** GitHub API 显示，isaac-sim/IsaacLab-Arena 7 月 19 日有推送，星标约 487。项目描述称其增强 NVIDIA Isaac Lab，提供 composable、scalable 的机器人仿真环境，用于创建多样化仿真场景，并评估不同 robot embodiments、objects 和 environments 下的机器人学习策略。

- **来源：** GitHub
- **核心价值：** 真机展示回答“这台机器这次能不能跑”，仿真评测回答“换本体、换物体、换环境后还能不能跑”。后者才是规模化部署前的工程筛选器。

---

## 🏢 机器人公司情报

### 1. [WAIC 主承办架构：上海继续把 AI 大会作为机器人产业协同平台](https://www.worldaic.com.cn/)

**摘要：** WAIC 官方页列出外交部、国家发展改革委、工业和信息化部、教育部、科学技术部、国务院国资委、国家网信办、中国科学院、中国科协和上海市人民政府等主办单位，以及上海市经信委、发改委、科委、浦东新区、徐汇区、东浩兰生集团等承办单位。对机器人公司来说，这种组织方式意味着政策、展览、产业招商和应用场景会在同一平台上交汇。

- **来源：** 世界人工智能大会官网
- **核心价值：** 具身机器人本体要商业化，不能只依赖单家公司推销；政策窗口、场景方、供应链和开发者生态需要共同形成试验场。

### 2. [HandUMI 软件 7 月 19 日更新：双臂采数接口走向可穿戴与可迁移](https://github.com/robonet-ai/handumi-sw)

**摘要：** GitHub API 显示，robonet-ai/handumi-sw 7 月 19 日有推送。项目描述为 open-source HandUMI software，用于 synchronized bimanual data collection，并可 retargeting to any bimanual robot，包含 calibration、QA、replay 和 teleoperation。它补上的不是单台机器人能力，而是双臂本体之间迁移操作数据的接口。

- **来源：** GitHub
- **核心价值：** 数据相关报道：人形本体商业化之后，最稀缺的是高质量双臂操作数据；可迁移采数接口会影响不同本体之间的模型复用效率。

### 3. [OpenArm 与 Roboto Origin 的共同信号：本体公司要回答“开发者怎么接入”](https://github.com/enactic/openarm)

**摘要：** OpenArm 和 Roboto Origin 近期均保持 GitHub 活跃，且都把机械结构、描述文件、控制接口、仿真或训练环境纳入公开工程范围。对人形机器人公司而言，这类开源项目会提高行业参照系：客户和开发者会更自然地追问整机是否支持标准接口、是否能导出模型、是否能接入 ROS2、是否方便采数和二次开发。

- **来源：** GitHub
- **核心价值：** 开源本体正在改变市场提问方式；未来客户买的不是“一个会动的机器人”，而是一套能被自己团队继续开发的身体平台。

---

## 结尾总结

7 月 20 日的主线可以概括为：WAIC 把机器人本体放进了产业级比较场，而开源生态正在提供判断本体成熟度的技术标尺。本体描述、仿真评测、机载控制、遥操作采数和训练数据闭环，正在变成观察人形机器人公司的关键问题。相比泛泛讨论“机器人很热”，更值得追问的是：什么样的本体能留下数据、接口和复用能力。

> 💬 如果你在 WAIC 现场只问机器人公司一个问题，你会问：本体成本、关节寿命、开放接口、数据采集能力，还是已经落地的客户场景？

## 关键词索引

**公司 / 机构：** 世界人工智能大会 / WAIC / 上海市人民政府 / Hugging Face / NVIDIA Isaac Lab / Enactic / OpenArm / RoboParty / Robonet AI

**项目 / 论文：** OpenArm / Roboto Origin / robot-descriptions / Isaac Lab-Arena / LeRobot / HandUMI / Jetson-PI / Human-level Dexterous Teleoperation / Robust bipedal locomotion on flowable slopes

**技术：** 具身智能 / 人形机器人 / 机器人本体 / URDF / MJCF / robot embodiment / VLA / onboard real-time control / sim2real / 双臂遥操作 / 数据闭环 / 仿真评测 / 本体描述

## 值得分享

1. WAIC 的机器人看点不只是“谁最像人”，而是谁的本体能被描述、仿真、采数、训练和部署。
2. 开源本体正在抬高行业标尺：OpenArm 公开 7DOF 仿人手臂，Roboto Origin 公开 DIY 人形工程栈。
3. 数据闭环决定本体长期价值：LeRobot 管数据格式，HandUMI 管双臂采数，robot-descriptions 管跨本体描述入口。
