# 微信公众号数据自动化

这套脚本用于：

1. 调用微信公众号官方 `datacube` 接口抓取数据。
2. 把原始返回保存为 JSON，并同步写入本地 SQLite。
3. 根据文章表现自动识别异常高/异常低样本。
4. 生成可直接继续编辑的周复盘 Markdown。

## 目录结构

```text
wechat-analytics/
  common.py
  fetch_wechat_data.py
  analyze_weekly.py
  render_weekly_review.py
  run_weekly_pipeline.py
  config/
    wechat_config.example.json
    source_aliases.json
    article_topic_overrides.json
  data/
    raw/
    exports/
    wechat_analytics.db
```

## 前置条件

- 公众号具备官方数据接口权限。
- 你有 `appid` 和 `appsecret`。
- 当前运行机器的公网 IP 已加入公众号后台的开发者 IP 白名单。
- 建议每天上午 8 点后抓取前一天数据。
- Python 3.10+。

## 第一次配置

1. 复制 `wechat-analytics/config/wechat_config.example.json`
2. 重命名为 `wechat-analytics/config/wechat_config.json`
3. 填入真实的 `appid` 和 `appsecret`

## 抓取昨天数据

```bash
python wechat-analytics/fetch_wechat_data.py
```

指定日期：

```bash
python wechat-analytics/fetch_wechat_data.py --date 2026-04-15
```

跳过分时接口：

```bash
python wechat-analytics/fetch_wechat_data.py --date 2026-04-15 --skip-hourly
```

## 生成周分析 JSON

```bash
python wechat-analytics/analyze_weekly.py --week-of 2026-04-16
```

输出文件默认写到：

- `wechat-analytics/data/exports/latest_weekly_analysis.json`

## 生成周复盘 Markdown

```bash
python wechat-analytics/render_weekly_review.py
```

默认输出到：

- `reviews/weekly-review-YYYY-WW.md`

## 一键跑完整流水线

```bash
python wechat-analytics/run_weekly_pipeline.py --date 2026-04-15 --week-of 2026-04-16
```

如果当天已经抓过数据：

```bash
python wechat-analytics/run_weekly_pipeline.py --week-of 2026-04-16 --skip-fetch
```

## 数据来源说明

当前脚本主要使用这些官方接口：

- `getusersummary`
- `getusercumulate`
- `getarticlesummary`
- `getarticletotal`
- `getuserread`
- `getuserreadhour`
- `getusershare`
- `getusersharehour`

## 关于来源分析

`source_aliases.json` 用于把接口里的来源代码映射成可读名称。

如果你后台返回的 `user_source` 或 `share_source` 代码和当前样例不一致：

1. 先查看 `wechat-analytics/data/raw/YYYY-MM-DD/*.json`
2. 找到真实返回值
3. 补充到 `source_aliases.json`
4. 重新运行 `analyze_weekly.py` 和 `render_weekly_review.py`

## 关于 topic 和收藏模块

脚本会优先从现有 `content/Robot_Intel_*.md` 中自动推断：

- 主条 topic
- 关键词索引
- 收藏模块类型

如果自动识别不准，可以在：

- `wechat-analytics/config/article_topic_overrides.json`

里按日期手工覆盖。

## 当前限制

- 官方 `datacube` 不直接提供完整的“在看 / 留言”指标。
- 搜一搜关键词明细通常仍需要结合后台人工补录。
- 如果你的公众号后台只提供更细颗粒度的来源视图而未开放到 API，需要额外做浏览器自动化。
