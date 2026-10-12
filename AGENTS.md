# Nouvelle Workz AI Assistant Operating Instructions

This project is the official SEO, AEO/GEO growth, and content management repository for Nouvelle Workz Pte. Ltd. (`nouvelleworkz.com`), a premier direct renovation contractor and commercial fit-out specialist in Singapore.

---

## 🚀 核心自动化触发：当用户说“我现在要发blog”或类似发文指令时

当用户发出任何关于写博客、发文章的指令（例如：`我现在要发blog`、`帮我写一篇blog`、`发布关于xxx的文章`）：

你**必须且自动**执行以下 6 步标准流程（基于 [`SKILL.md`](file:///d:/nouvelleworkz/SKILL.md) 与 [`llms.txt`](file:///d:/nouvelleworkz/llms.txt)），无需用户多余提示：

### 1. 自动选题与防蚕食排查 (Anti-Cannibalization Check)
- 读取 `data/all_wp_posts_live.json` 中全站 59+ 篇已有文章。
- 若用户未提供明确主题，自动运行 `python scripts/find_gsc_opportunities.py`，根据 GSC 第 5~20 名有展现但缺页面的潜力词推荐 2~3 个精准垂直选题。
- 若用户提供了主题，排查是否与已有文章主词冲突。若已有泛词（如已存在 Office Reinstatement 概览），自动建议下钻细分场景（如 JTC 厂房退租、F&B 商场退租、SCDF 消防改造等）。

### 2. 事实校准与大纲策划 (E-E-A-T & Brand Ground Truth)
- 严格遵循 [`llms.txt`](file:///d:/nouvelleworkz/llms.txt) 的品牌事实：
  - 资质：HDB 执照承包商 (`HB-075810E`)、BCA 注册、bizSAFE Level 3。
  - 模式：Direct Contractor（无 ID 中间商溢价，节省 15%~30%）。
  - 业务门槛：最低消费 SGD $3,000，不接散单小维修。
  - 真实新加坡 2026 工料价格（必须使用表格展示，严禁正文叙述）。
  - 专家背书：必须嵌入创始人 James Liang 的实际行业引言引用框。

### 3. AEO / GEO 标准正文生成
- **字数**：1,200 ~ 1,500 词硬核干货。
- **首屏 AEO 块**：必须在 `#fcf6ef` 浅色背景加 `#C69E63` 金色边框的容器内，首句必须是 **40–60 词严格定义句**（严禁包含 *"In this article..."* 等 AI 废话词）。
- **语义化价格表格**：必须使用完整 `<table><thead><tbody>` 输出，注意防止 PowerShell 吞掉 `$` 符号。
- **内链绑定**：内嵌 2~3 个锚文本链接到核心商业服务页（如 `/commercial/reinstatement/`）。
- **FAQ Schema**：文末附带 3~4 组 Q&A 的 JSON-LD 结构化数据。

### 4. 三图视觉规划 (16:9)
- 规划 3 张符合新加坡真实工程场景的配图（Hero 首图、Process 施工中、Handover 完工交付）。

### 5. 质量门禁验证 (Quality Gate - 必须通过)
- 将生成的 HTML 保存为临时文件，运行：
  ```bash
  python scripts/validate_aeo_elementor.py --modified <temp_html_path>
  ```
- 确保 5/5 PASSED（Elementor 布局、40-60词定义句、0 AI废话、完整表格、FAQ Schema）。

### 6. WordPress REST API 发布与交付报告
- 推送文章至 WordPress REST API 为 `draft`（草稿）或 `publish`。
- 输出给用户清晰的交付卡片：
  - **预览与编辑链接**：`https://nouvelleworkz.com/wp-admin/post.php?post={id}&action=edit`
  - **SureRank SEO Title**：**严格 < 45 字符，且绝对不含 `&` 符号（必须用 `and`）**。
  - **Meta Description**：**严格 130 ~ 150 字符**，不含双引号。
  - 自动化提交索引命令：`python scripts/submit_to_google_indexing.py --url {link}`

---

## 🔍 全站 SEO / AEO 审计规范

针对全站分析与健康检查，**直接使用 claude-seo 套件**：
- 全站综合体检：使用 `/seo-audit`
- 技术与抓取检测：使用 `/seo-technical`
- AI 搜索引擎与 GEO 表现：使用 `/seo-geo`
- 单页面深度审查：使用 `/seo-page <URL>`
无需维护和运行零散的一次性巡检脚本。

---

## 🔑 API 凭证与发布权限
- **WordPress REST API**：使用 WordPress 原生 Application Passwords（用户 -> 个人资料 -> 应用程序密码生成）。在 `scripts/wp_api_runner.py` 配置 `DEFAULT_USER` 与 `DEFAULT_PASS`。
- **Google Indexing API**：在 `scripts/submit_to_google_indexing.py` 配置 Service Account JSON 密钥；若无权限可直接在 GSC 后台手动请求编入索引。详见 [`HANDOVER_MANUAL.md`](file:///d:/nouvelleworkz/HANDOVER_MANUAL.md)。

---

## ⛔ 避坑红线 (Critical Watch-outs)
1. **SureRank 标题禁止 `&` 符号**：必须用 `and`，否则插件乱码崩溃；长度严格 `< 45` 字符。
2. **Meta Description 严禁英文双引号**：限制 130~150 字符。
3. **编写脚本首选 Python**：不要用 PowerShell 拼接含 `$价格` 的字符串（会被当成空变量吞掉）。
4. **禁止对现有线上页面执行批量修改/注入脚本**。

