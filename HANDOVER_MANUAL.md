# Nouvelle Workz 极简交接与全自动运营手册 (Handover Manual)

> **交付对象：** Nouvelle Workz SEO / AEO / GEO 增长与内容发布接手人  
> **官网地址：** [nouvelleworkz.com](https://nouvelleworkz.com)  
> **整理时间：** 2026年10月  
> **工作区路径：** `d:\nouvelleworkz`  

---

## 目录
1. [快速上手：只需对 AI 说一句话](#一快速上手只需对-ai-说一句话)
2. [全站分析与审计：统一使用 claude-seo 套件](#二全站分析与审计统一使用-claude-seo-套件)
3. [核心交付资产目录](#三核心交付资产目录)
4. [账号与 API 凭证获取指南 (必读)](#四账号与-api-凭证获取指南-必读)
5. [必须牢记的 5 大“避坑红线”](#五必须牢记的-5-大避坑红线)


---

## 一、 快速上手：只需对 AI 说一句话

接手人无论使用 Claude Code、Cursor、Antigravity 还是任何现代 AI 编码助手打开本项目，本项目已内置全局指令体系（`AGENTS.md` / `SKILL.md`）。

**日常发文章，你只需要直接在对话框输入：**
> **“我现在要发一篇关于 [选题/方向] 的 blog”**  
> *(或者甚至只说：“我现在要发 blog，帮我推荐选题并写一篇”)*

**AI 会全自动完成以下所有专业动作：**
1. 自动读取 `data/all_wp_posts_live.json` 对全站 59+ 篇已有文章排重（防关键词同室操戈）；
2. 若没有明确选题，自动调取 GSC 数据推荐排名第 5~20 名有展现但缺乏深度承接页的高潜力机会词；
3. 自动对照 `llms.txt` 校准新加坡本地资质（BCA/HDB/bizSAFE）、最低消费 SGD $3,000 门槛与 2026 市场工料行情；
4. 自动生成符合 Google SGE/ChatGPT/Perplexity 抓取标准的 AEO 结构（首屏 40-60 词黄金定义句、原生价格表格、创始人 James Liang 专家背书、FAQPage Schema）；
5. 自动运行本地门禁 `python scripts/validate_aeo_elementor.py`，确保 5/5 项检查全部通过；
6. 自动通过 WordPress REST API 推送为草稿（Draft）或直接发布，并输出 SureRank 双标题与 Meta Description 复制面板。

---

## 二、 全站分析与审计：统一使用 `claude-seo` 套件

**问：全站 SEO / AEO 巡检需要手动跑各种乱七八糟的 Python 脚本吗？**  
**答：完全不需要！** 本项目已接入成熟的专业本地 SEO 套件 `claude-seo`，在 AI 聊天中直接输入内置斜杠指令即可进行多专家级分析：

| 想要做的分析 | 对应指令 | 作用说明 |
|---|---|---|
| **全站综合体检** | `/seo-audit` | 自动爬取全站页面，委托多位专家并发诊断全站健康度并打分 |
| **技术 SEO 与抓取审计** | `/seo-technical` | 检测全站状态码、抓取预算、Core Web Vitals、Sitemap 合规性 |
| **AI 搜索引擎 (GEO/AEO) 审计** | `/seo-geo` | 检测品牌在 ChatGPT / Perplexity / Google SGE 中的可引用度与 AI 抓取友好度 |
| **单页面深度诊断** | `/seo-page <URL>` | 针对某篇重点博客或服务落地页进行全维度单页优化诊断 |
| **内容质量与 E-E-A-T 审查** | `/seo-content` | 检测文章阅读深度、信息密度与行业专家权威信号 |

> 💡 **注：** 过去用于单项检查的零散一次性脚本已全部精简下线，接手人无需记忆复杂的脚本参数，统一使用 `claude-seo` 即可。

---

## 三、 核心交付资产目录

交接包 `handover_package/`（或解压 `NouvelleWorkz_Handover_Package.zip`）仅保留最核心、日常必用的资产：

```text
handover_package/
├── HANDOVER_MANUAL.md       # 【本交接手册】
├── AGENTS.md / CLAUDE.md    # 【AI 自动行为准则】定义“发blog”一键触发全部流程与 API 说明
├── SKILL.md                 # 【技能规范】AEO 博客撰写样式、代码标准与 8 步闭环
├── README.md                # 【项目总览】
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

## 四、 账号与 API 凭证获取指南 (必读)

为了让自动化发布与数据提交正常工作，接手人需要掌握以下两个关键凭证的获取方式：

### 1. WordPress REST API 应用程序密码（发布博客必用）
- **凭证原理**：使用 WordPress 原生的 Application Passwords（应用程序密码）。它专用于外部 API 通信，独立于你的主登录密码，支持单独撤销且不受二次验证干扰。
- **当前默认配置**：当前脚本内置了现有的工作账号 `nouvelle.workz`。
- **接手人如何生成属于自己的新密码（步骤）**：
  1. 登录 WordPress 管理后台：`https://nouvelleworkz.com/wp-admin`（需具备 Editor 或 Administrator 权限）；
  2. 进入左侧菜单：**用户 (Users) -> 个人资料 (Profile)**（或编辑目标用户）；
  3. 滚动到页面底部，找到 **应用程序密码 (Application Passwords)** 设置区块；
  4. 在 **新应用程序密码名称 (New Application Password Name)** 输入框输入备注（例如 `seo-assistant-bot`）；
  5. 点击 **添加新应用程序密码 (Add New Application Password)** 按钮；
  6. 页面顶部会立即生成一段 24 位的独立密码（形如 `abcd efgh ijkl mnop qrst uvwx`）：
     > ⚠️ **特别提醒**：该密码**只会在创建时显示一次**，一旦刷新页面将无法再查看，请务必立即复制并妥善保存！
  7. **配置生效**：将生成的用户名与密码填入 `scripts/wp_api_runner.py` 的 `DEFAULT_USER` 和 `DEFAULT_PASS`，或各 `publish_*.py` 脚本中的认证字段即可。

---

### 2. Google Indexing API 凭证（快速收录选填）
- **凭证原理**：通过 Google Cloud Platform (GCP) 的服务账号私钥（`service_account.json`）直接通知 Google 蜘蛛抓取更新。
- **当前配置路径**：`scripts/submit_to_google_indexing.py`。
- **全新配置方法**：
  1. 打开 [Google Cloud Console](https://console.cloud.google.com/)，启用 **Web Search Indexing API**；
  2. 创建 Service Account 并生成下载一个 `.json` 私钥文件；
  3. 复制该服务账号生成的邮箱（如 `indexing-bot@your-project.iam.gserviceaccount.com`）；
  4. 登录 [Google Search Console](https://search.google.com/search-console)，在“设置” -> “用户和权限”中将该邮箱添加为 **所有者 (Owner)**；
  5. 将私钥文件路径填写到 `scripts/submit_to_google_indexing.py` 的 `key_path`。
- **零门槛替代方案（推荐新手使用）**：
  > 如果接手人没有 GCP 账号或觉得配置复杂，**完全不需要 Indexing API 脚本**！发完新博客后，只需打开 [Google Search Console](https://search.google.com/search-console)，在顶部检查栏粘贴新文章链接，点击 **“请求编入索引 (Request Indexing)”** 即可，两者的收录效果完全相同！

---

## 五、 必须牢记的 5 大“避坑红线”

1. **SureRank 标题绝不能有 `&` 符号**：
   - SureRank 插件在后台解析 `&` 符号时有 bug（会产生 `&amp;amp;` 导致乱码崩溃）。后台 SEO 标题必须用 `and`，且字符数严格控制在 **45 字符以内**。
2. **Meta Description 禁含双引号**：
   - 控制在 **130 ~ 150 字符**，不要出现英文双引号 `"`（Google 会截断引号后的内容）。
3. **编写脚本首选 Python，警惕 PowerShell 吞 `$`**：
   - PowerShell 会把 `$15,000` 或 `$25/sqft` 中的 `$数字` 当成空变量吞掉，造成正文乱码。所有发文与数据处理一律使用 Python。
4. **Elementor 布局防损**：
   - 推送博客直接以 HTML 注入 `content` 字段即可，切勿用 API 随意清空或覆盖页面的 `_elementor_data` 原生元字段。
5. **最低消费门槛（SGD $3,000）**：
   - 任何文章中的业务引导与 CTA，始终贯彻最低消费 **SGD $3,000** 政策，明确不接零碎小修补。
