# Nouvelle Workz SEO & AEO Automation Package

本项目为 **Nouvelle Workz Pte. Ltd.**（新加坡直属装修工程承包商）的官方 SEO/AEO 增长、内容发布与自动化运营代码库。

---

## 🚀 接手人快速上手 (1 分钟)

请直接阅读 **[📘 完整交接操作手册 (HANDOVER_MANUAL.md)](HANDOVER_MANUAL.md)**。

日常撰写与发布博客，**只需在 AI 编程助手（Claude Code / Cursor / Antigravity 等）中输入：**
> **“我现在要发一篇关于 [主题] 的 blog”**  
> *(或：“我现在要发 blog，帮我推荐选题并写一篇”)*

系统将自动读取 [`AGENTS.md`](AGENTS.md)、[`SKILL.md`](SKILL.md) 与 [`llms.txt`](llms.txt)，全自动执行：
- GSC 机会词挖掘与 59 篇老文章查重排重；
- 结合新加坡 2026 市场工料价格与法定资质生成 AEO 标准长文；
- 规划 3 张 16:9 场景施工配图；
- 本地质量门禁 `validate_aeo_elementor.py` 自动化检测（5/5 必须全过）；
- WordPress REST API 自动推送为草稿，并生成 SureRank SEO 标题与描述。

---

## 📁 核心资产架构

```text
├── HANDOVER_MANUAL.md       # 【核心交接手册】包含发文闭环、API 凭证生成、5大避坑红线
├── AGENTS.md / CLAUDE.md    # 【AI 全局行为指令】定义对话时自动执行的 SOP
├── SKILL.md                 # 【技能规范】AEO 博客撰写样式、代码标准与 8 步闭环
├── llms.txt                 # 【官方实体知识库】供 AI 查阅的 2026 报价、资质与品牌信息
├── robots.txt               # 【爬虫协议】
├── scripts/                 # 【7 个高价值核心复用脚本】
│   ├── validate_aeo_elementor.py   # AEO/Elementor 自动化门禁检验 (5/5 必须全过)
│   ├── find_gsc_opportunities.py   # GSC 挖掘 5~20 名机会词
│   ├── audit_blog_clusters.py      # 全站 12 大博客集群审计与防排重排查
│   ├── fetch_all_wp_posts.py       # 同步线上文章列表
│   ├── submit_to_google_indexing.py# Google Indexing API 快速提交收录
│   ├── wp_api_runner.py            # WordPress REST API 通信底座
│   └── publish_jtc_reinstatement_guide.py # 标准发布示例模板参考
├── data/                    # 【核心一手数据源】
│   ├── all_wp_posts_live.json      # 全站 59+ 篇已发文章实时备份（排重核心）
│   ├── gsc_28d.json                # GSC 28 天真实搜索词与展现量
│   └── gsc_90d_query.json          # GSC 90 天搜索表现
└── reports/                 # 【战略方案底稿】90 天规划与逐页调整报告
```

---

## 🔍 全站 SEO / GEO 审计

全站分析无需运行散装脚本，直接使用 `claude-seo` 套件：
- 全站综合体检：`/seo-audit`
- 技术与抓取检测：`/seo-technical`
- AI 搜索引擎与 GEO 表现：`/seo-geo`
- 重点单页深度诊断：`/seo-page <URL>`
