# Nouvelle Workz 逐页 SEO / GEO 调整执行报告

**网站：** [nouvelleworkz.com](https://nouvelleworkz.com)  
**审计日期：** 2026-09-15  
**报告目的：** 在保留现有小服务页面的前提下，明确哪些页面承担核心关键词，哪些页面仅作为施工能力、案例和内部链接资产，并逐页列出问题、修改方式与优先级。  
**审计依据：** 网站首页、服务总览页、项目类型页面、小服务页面、Contact、About、Blog 入口、XML sitemap 以及页面可抓取正文。

---

## 1. 先确定正确的 SEO 策略

你目前的策略是合理的：**不让每一个小服务页面都承担独立的主关键词排名，而是让 HDB、BTO、Condo、Landed、Office、Commercial、Reinstatement 等项目类型页面负责高商业意图搜索；小服务页面保留为施工能力说明、专业证明和内部链接节点。**

因此，本报告不建议你重复创建以下页面：

- HDB renovation 页面；
- BTO renovation 页面；
- Condo renovation 页面；
- Landed renovation 页面；
- Commercial renovation 页面；
- Office renovation 页面；
- Commercial reinstatement 页面；
- 小服务页面。

这些页面已经存在。真正需要做的是**重新定义页面职责、统一内容、修复质量问题、建立内部链接和实体信号**。

### 1.1 推荐的三层页面模型

| 页面层级 | 主要页面 | SEO 职责 | 是否主动争夺主关键词 |
|---|---|---|---|
| A 层：核心商业页面 | HDB、BTO、Condo、Landed、Office、Commercial、Reinstatement、Renovation Package | 获取项目类型、装修需求和高商业意图搜索 | 是 |
| B 层：专业能力页面 | Plumbing、Electrical、Carpentry、Tiling、Vinyl、Epoxy、Sintered Stone、Painting 等 | 解释施工能力，支撑 A 层页面的可信度和专业覆盖 | 不必全部争夺；选择性争夺 |
| C 层：信任与转化页面 | Home、About、Contact、Portfolio、FAQ、Residential Hub、Commercial Hub | 解释企业实体、资质、案例、联系方式和转化路径 | 承担品牌、本地和导航型搜索 |

### 1.2 关于 sitemap 中的小服务页面数量

目前 XML page sitemap 中可以看到的专业/小服务 URL 不止 15 个，至少包括 Plumbing、Electrical Works、Carpentry、Demolition & Hacking、Metallic Epoxy、Vinyl Flooring、Tiling、Table Top、Sintered Stone、Plastering、Painting、Mirror & Glass、Decorative Wall Panels、Decorative Paint、Ceiling & Partition、Epoxy Grout 等。

这不代表所有页面都必须排名。**页面进入 sitemap 只是说明希望搜索引擎发现它，不等于页面必须成为关键词 landing page。** 你可以保留页面，同时通过内容定位、内部链接、标题描述和转化路径，让它们成为辅助页面。

---

## 2. 总体优先级

| 优先级 | 含义 | 建议处理时间 |
|---|---|---|
| P0 | 会直接影响可信度、理解、转化或造成明显错误 | 立即处理 |
| P1 | 会影响核心页面排名、GEO 引用和询盘质量 | 第一阶段 |
| P2 | 有助于长期内容资产和专业实体建设 | 第二阶段 |
| P3 | 可选的扩展或页面级细节 | 有资源时处理 |

### 2.1 全站 P0 问题

1. **修复乱码和模板残留。** 服务页出现 `u2014`、`u2026`、`Translator`、`Contact Form Demo` 和 `quota` 等明显问题。
2. **统一品牌与事实口径。** 当前审计页面主要显示 `Nouvelle Workz`，但 `/services/` 抓取标题出现过 `Nouvelle Works's Services`；首页项目数同时出现 `1099+` 和 `over 1,100 projects`。后台应检查 SEO Title、页面标题、Open Graph、Schema 和旧模板字段。
3. **统一资质名称。** 不要在不同页面随意混用 `BCA approved`、`BCA licensed`、`BCA registered`。应根据实际证书或登记资料使用准确名称。
4. **统一价格口径。** BTO、HDB、Landed、Reinstatement 和案例页面都出现价格，但有些页面没有清楚说明价格是 package starting price、case-specific price、促销价还是完整项目价。
5. **降低不可控的绝对承诺。** 例如 `100% deposit return`、`guaranteed approval`、`guaranteed on-time`、`last a lifetime`。最终结果可能取决于房东、MCST、监管机构、基层情况、材料和工程范围。
6. **验证所有 CTA 和表单。** 每一个 WhatsApp、电话、邮件、Contact Form 的点击与提交都应能被真实接收，并在 GA4 中记录事件。

---

# 3. A 层：核心商业页面逐页调整

## 3.1 首页 `/`

### 页面职责

首页应定位为：**Singapore residential and commercial renovation contractor**。它负责企业实体、服务总览、核心差异化、主要信任证明和询盘入口，不应承担所有 HDB、BTO、材料和施工细节关键词。

### 已发现问题

| 问题 | 具体表现 | 影响 |
|---|---|---|
| 事实口径不一致 | `1099+` 与 `over 1,100 projects` 并存 | 降低实体可信度，也可能造成 AI 抽取冲突 |
| 绝对化表述 | `Singapore's best`、`most trusted`、`100% work quality` | 缺少定义或第三方证据时显得像宣传口号 |
| 页面职责过重 | 同时覆盖 HDB、BTO、Condo、Commercial、Epoxy、Wall Panels 等 | 核心主题不够集中 |
| 表单残留 | `Contact Form Demo`、`Submit to get a quota !` | 直接影响专业度和转化 |
| 结构化事实不够集中 | 公司名、UEN、地址、负责人、服务区域和资质分散 | AI 需要从多个位置拼接实体信息 |

### 建议修改

1. 在首屏使用一句可直接引用的企业定义：

   > Nouvelle Workz Pte Ltd is a BCA-registered and HDB-licensed renovation contractor in Singapore, providing end-to-end residential and commercial renovation with direct project management and in-house trade capabilities.

2. 将首页主服务入口集中为：
   - HDB / BTO；
   - Condo；
   - Landed；
   - Office / Commercial Fit-Out；
   - Commercial Reinstatement；
   - Renovation Packages。

3. 将 Plumbing、Carpentry、Tiling、Electrical 等小服务放在较低层级的 `Our In-House Capabilities` 区块，并明确：

   > These specialist trades are delivered as part of our turnkey renovation and commercial project scope. Standalone small repair jobs may not be available.

4. 统一项目数量，例如只保留：

   > Completed 1,099+ projects

   前提是这个数字有内部记录支持。

5. 将 “best” 和 “most trusted” 替换为可验证事实：
   - HDB Registered Renovation Contractor；
   - BCA Registered Contractor；
   - bizSAFE Level 3；
   - 5.0 rating based on 78 Google reviews；
   - one-year workmanship warranty（如当前合同确实如此）。

### 优先级

**P0。**

---

## 3.2 服务总览页 `/services/`

### 页面职责

这个页面现在已经从“小服务目录”调整为**项目类型导向的服务总览页**，这个方向是合理的。它不需要恢复为原来单纯摆放小服务页面的目录，也不需要把每个小服务都做成主关键词页面。

### 已发现问题

| 问题 | 页面证据 | 建议 |
|---|---|---|
| 页面标题风险 | 抓取结果顶部出现 `Nouvelle Works's Services` | 后台检查 SEO Title、H1、OG Title、Schema，统一为 Nouvelle Workz |
| 乱码 | `renovationsu2014`、`guaranteesu2014`、`quality guaranteesu` | 直接清理数据库或 Elementor 文本中的错误转义 |
| 模板残留 | `Translator`、`Contact Form Demo` | 删除，不应出现在公开页面 |
| 拼写错误 | `quota` | 改为 `quote` |
| 绝对承诺 | `100% deposit return` | 改为协助完成 landlord/MCST handover |
| 层级混杂 | Project Pillars 与 In-House Crafts 同时出现，层级不够明显 | 先展示项目类型，再展示专业能力 |
| FAQ 过度重复 | FAQ 中大量 “get a quote now” | 保留真正回答问题的内容，减少每个答案末尾重复 CTA |

### 建议页面结构

```text
H1: Residential & Commercial Renovation Services in Singapore

首屏定义：我们做什么、服务谁、覆盖哪里

Section 1: Choose Your Project Type
- HDB / BTO
- Condo
- Landed
- Office
- Commercial Fit-Out
- Commercial Reinstatement

Section 2: Our Turnkey Delivery Scope
- Design / planning
- Permits and approvals
- Demolition / hacking
- M&E
- Carpentry
- Flooring / surfaces
- Painting / finishing
- Handover / warranty

Section 3: In-House Trade Capabilities
- Link to small service pages as supporting evidence

Section 4: Process
Section 5: Certifications and proof
Section 6: Selected portfolio
Section 7: FAQ
Section 8: CTA
```

### 小服务页面如何放在这里

小服务页面可以继续出现，但按钮文案不要全部写成独立销售入口。例如：

- `View technical scope`
- `See our carpentry capabilities`
- `Understand our waterproofing process`
- `See materials and workmanship`

如果你不希望获取 standalone plumbing 或 standalone painting 的关键词，服务总览页可以明确写：

> Our specialist trades are delivered within complete residential, commercial, fit-out and reinstatement projects. We do not generally undertake ad-hoc handyman or small repair requests.

### 优先级

**P0。** 这是全站信息架构的中心页面。

---

## 3.3 Residential Hub `/residential/`

### 页面职责

作为住宅项目类型入口，链接至 HDB、BTO、Condo、Landed、Partial Makeover 和相关 package 页面。

### 建议修改

- H1 直接说明 `Residential Renovation Contractor in Singapore`。
- 首屏只说明住宅项目类型，不要堆叠 Plumbing、Painting、Sintered Stone 等细节。
- 每个项目类型卡片加入一句独特描述：
  - HDB resale：hacking、waterproofing、rewiring；
  - BTO：key collection、defect check、package planning；
  - Condo：MCST、lift protection、developer fittings；
  - Landed：A&A、structural work、URA/BCA coordination。
- 加一段解释小服务的归属：专业工种是 turnkey renovation 的组成部分。

### 优先级

**P1。**

---

## 3.4 HDB 页面 `/residential/hdb-renovation/`

### 当前实际定位

这个页面不是泛 HDB 页面，而是非常明显的：

> **HDB Resale Renovation Contractor Singapore**

页面已经有 3-room、4-room、5-room package、hacking、waterproofing、rewiring、carpentry、case studies 和 FAQ。

### 已发现问题

| 问题 | 具体表现 | 建议 |
|---|---|---|
| 页面名称可能过宽 | 页面标题为 `HDB Renovation Package`，H1 却是 resale contractor | Title、H1、首段统一围绕 HDB resale |
| 价格口径不清 | Package 从 $18,799；案例出现 $14,000、$17,000、$26,000 等 | 明确 package price、case price、scope 和更新时间 |
| 资质命名不一致 | `BCA-approved Direct Contractor`、`BCA Licensed Builder` 等表述 | 使用证书和登记资料中的正式名称 |
| 结果承诺过强 | `zero hidden structural violations` | 改为遵守审批流程、由合资格人员处理相应工作 |
| 重点信息较多但缺少摘要 | 读者需要滚动才能判断适合哪类 resale flat | 首屏增加 scope、典型时间、适合对象和 CTA 摘要 |

### 建议主关键词与页面标题

- **Primary topic:** HDB resale renovation contractor Singapore
- **Secondary topics:** HDB resale renovation package、HDB resale renovation cost、HDB hacking and waterproofing
- **建议 Title：** HDB Resale Renovation Contractor Singapore | Packages & Cost Guide
- **建议 H1：** HDB Resale Renovation Contractor in Singapore

### 建议新增或重排的内容

1. 首屏放 `Who this page is for`：3-room、4-room、5-room resale owners。
2. 用表格解释 package starting price 与实际案例价格的区别。
3. 将 Plumbing、Tiling、Electrical、Carpentry 页面作为相关技术说明链接，而不是首页级入口。
4. 每个案例增加项目类型、区域、范围、工期和最终价格口径。
5. 增加 `HDB resale vs BTO renovation` 的内部链接，但不要让该页面吞掉 BTO 页面关键词。

### 优先级

**P1。**

---

## 3.5 BTO 页面 `/residential/bto-renovation/`

### 页面职责

BTO renovation contractor / package 的核心商业页面。现有结构已经相当完整。

### 已发现问题

| 问题 | 具体表现 | 建议 |
|---|---|---|
| 价格口径不一致 | 页面 package 从 $5,999；案例有 $5,000 和 $7,000 | 标注 exact scope、促销或案例日期 |
| 信息较密 | Package、流程、defect check、案例同时展开 | 在首屏增加摘要表格，减少用户寻找答案的时间 |
| 2026 内容需要维护 | 价格和 defect check 都写 2026 | 未来每次规则/价格更新时记录 `Last updated` |
| 案例连接不足 | 有 BTO 案例，但应更明显链接回服务页 | 每篇 BTO 文章与案例均链接到本页 |

### 建议主关键词与页面标题

- **Primary topic:** BTO renovation contractor Singapore
- **Secondary topics:** BTO renovation package、BTO renovation cost、BTO renovation timeline
- **建议 Title：** BTO Renovation Contractor Singapore | Packages, Cost & Timeline
- **建议 H1：** BTO Renovation Contractor and Packages in Singapore

### 建议重点

- 用表格区分 2-room、3-room、4-room、5-room package 的包含项目。
- 明确 `from` 价格不等于完整装修总价。
- 将 BTO timeline 博客作为信息型文章，链接回本页作为商业转化页。
- 加 `Key collection → defect check → permit → works → handover` 的可引用摘要。

### 优先级

**P1。**

---

## 3.6 Condo 页面 `/residential/condo-renovation/`

### 当前状态

这是一个结构较完整的 Condo 服务页，已经覆盖 MCST、lift protection、deposit、developer fittings、workflow、case study 和 FAQ。

### 主要问题与建议

| 问题 | 建议 |
|---|---|
| 案例相对少 | 增加新 Condo、二手 Condo、部分翻新三个不同案例 |
| 页面图片 alt 可能错配 | 抓取结果出现 `hdb resale electrical bundle` 等可能不适合 Condo 的 alt 文本，逐张检查 |
| MCST 说明可以更具体 | 增加 quiet hours、deposit、lift protection、permit submission、common-area protection |
| 缺少 scope 边界 | 说明哪些是完整装修、哪些是 carpentry/painting-only，哪些不承接 |
| 评分重复但未必与页面相关 | 保留真实评价，但尽量展示与 Condo 项目相关的评价或案例证明 |

### 建议定位

- **Primary topic:** Condo renovation contractor Singapore
- **Secondary topics:** MCST renovation approval、condo renovation cost、new condo renovation、resale condo renovation

### 优先级

**P1。**

---

## 3.7 Landed 页面 `/residential/landed-renovation/`

### 当前状态

页面覆盖 A&A、reconstruction、rebuild、URA/BCA/PUB/SCDF、PE、soil test、成本、时间和 TOP/CSC，主题方向正确。

### 主要风险

| 风险 | 页面表现 | 修改方向 |
|---|---|---|
| 法规表达过度简化 | 例如用 GFA 50% 作为 A&A / Reconstruction 判断 | 增加官方来源，并说明具体分类需由合资格专业人士判断 |
| 绝对化节省承诺 | `saving $50,000 to $100,000` | 改为案例或估算条件，不要当成普遍结果 |
| 审批承诺 | `seamless submissions`、`guarantee` 类表达 | 改为 coordination / preparation / submission support |
| 价格敏感 | $900k–$2.5M+ 等价格 | 标注更新时间、项目条件、是否含 GST、设计费、PE、材料和土地条件 |
| 工程责任边界 | Soil、piling、foundation、TOP 等 | 明确由相关 QP/PE、建筑师或合资格顾问负责审核和签署 |

### 建议内部链接

- A&A vs rebuild 博客 → 本服务页。
- Landed portfolio 项目 → 本服务页。
- Hacking、Plumbing、Carpentry 等小服务不要作为本页主导航，而作为工程范围说明。

### 优先级

**P1。**

---

## 3.8 Commercial Hub `/commercial/`

### 页面职责

商业项目入口，链接至 Commercial Renovation、Office、F&B、Retail/Salon 和 Reinstatement。

### 建议修改

- 用项目类型作为第一层，不要先展示小工种。
- 明确 `Fit-out` 与 `Reinstatement` 的差别。
- 每个卡片加客户决策信息：用途、审批、典型项目阶段、交付范围。
- 将 Demolition、Ceiling、Carpentry、Electrical 等页面设为施工能力支持页面。

### 优先级

**P1。**

---

## 3.9 Commercial Renovation `/commercial/commercial-renovation/`

### 建议

- 作为 commercial renovation / fit-out 的综合页。
- 与 Office、F&B、Retail 页面区分清楚：综合页讲项目管理和交付，子页讲特定空间。
- 增加 B2B 询盘字段：面积、用途、租约/交付日期、消防/MCST 状态、是否需要设计、是否需要 reinstatement。
- 加真实商业案例，不要只展示住宅项目。

### 优先级

**P1。**

---

## 3.10 Office `/office-renovation/`

### 建议

- 明确主要关键词为 Office Renovation / Office Fit-Out，而不是泛商业装修。
- 加入面积、座位数量、会议室、M&E、消防、数据布线、搬迁和 handover 的内容。
- 使用 office-specific case studies。
- 将 `/residential/electrical-works/` 和 `/residential/ceiling-partition/` 作为 supporting links，但不要让它们抢 Office 页面主角。

### 优先级

**P1。**

---

## 3.11 F&B 页面 `/commercial/fb-cafe-renovation/`

### 建议

- 明确 `F&B renovation / cafe fit-out Singapore`。
- 重点展示厨房、排烟、grease trap、gas、SCDF、SFA/NEA、夜间施工和开业时间表。
- 加一个“需要客户提前准备的资料”区块：平面图、租约、landlord requirements、设备清单、营业时间限制。
- 相关小服务链接到 Commercial 页面，而不是把页面写成普通 Plumbing/Carpentry 页面。

### 优先级

**P1。**

---

## 3.12 Retail / Salon 页面 `/commercial/salon-retail-shop-renovation/`

### 建议

- 明确 Retail shop / Salon renovation Singapore。
- 增加 visual merchandising、display carpentry、shopfront、lighting、signage、night works、mall rules 和 handover。
- 将 Carpentry、Glass、Electrical、Ceiling 等作为实施能力证明。
- 增加真实 retail / salon 项目案例和交付日期。

### 优先级

**P1。**

---

## 3.13 Commercial Reinstatement `/commercial/reinstatement/`

### 当前状态

这是目前较强的商业页面之一，已经覆盖 lease clause、MCST、FSSD/SCDF、PE、office、retail、F&B、价格、时间和 handover。

### 主要问题

- `Guaranteed Deposit Return` 和 `100% security deposit return` 风险较高。
- 价格区间应注明是 market reference，不是报价。
- `guarantee seamless approval` 应改为协助准备和协调审批。
- 加入真实案例，特别是 office、retail、F&B 三类。
- FAQ 需要避免过多重复“contact us”，改为直接回答 landlord、lease、M&E、deposit 和 timeline 问题。

### 建议替换用语

| 当前用语 | 建议用语 |
|---|---|
| Guaranteed Deposit Return | Deposit-Handover Support |
| 100% security deposit return | We coordinate the required scope for landlord and MCST inspection |
| Guarantee seamless approval | We prepare and coordinate the required submissions |
| Guarantee timely completion | We provide a defined schedule and manage works towards the lease deadline |

### 优先级

**P0/P1。** 关键词页面本身很重要，绝对承诺应优先修复。

---

## 3.14 Renovation Package `/renovation-package-singapore/`

### 页面职责

作为 package 主题综合页，承接 HDB/BTO package、预算、范围和价格比较，但不能与 BTO 和 HDB 页面完全重复。

### 建议修改

- 明确这是 package overview，不是某一种房型的服务页。
- 用表格比较 BTO、HDB resale、Condo 和 partial makeover 的 package 逻辑。
- 每个 package 只展示 starting price 和包含范围。
- 链接到具体页面：BTO、HDB resale、Condo、Partial Makeover。
- 在页面顶部说明：价格取决于范围、房屋现状、材料、面积和审批条件。

### 优先级

**P1。**

---

# 4. B 层：小服务页面的统一策略

## 4.1 小服务页面的共同定位

这些页面不需要全部被删除，也不需要全部争夺主关键词。建议将它们统一定位为：

> **Specialist trade capability pages supporting complete residential, commercial, fit-out and reinstatement projects.**

每个小服务页都应包含一个清晰的范围声明：

> This specialist trade is generally delivered as part of a complete renovation, fit-out or reinstatement project. Standalone small repair or handyman requests may not be available.

这样做有三个好处：

1. 搜索引擎可以理解页面内容，但不会误解你的主要商业模式。
2. 用户不会因为看见某个小服务页就误以为你一定接受单项小维修。
3. 核心项目页面可以自然链接到相关专业能力页，形成 GEO 的实体证据链。

## 4.2 小服务页面的共同模板

每个小服务页建议统一为以下结构：

```text
H1: [Trade] as Part of Complete Renovation Projects in Singapore

Short answer: what the trade does and which project types use it

Where this trade fits:
- HDB / BTO
- Condo
- Landed
- Office / commercial
- Reinstatement / fit-out

Scope of work
Materials and workmanship standards
Process and dependencies
Typical project factors, not generic promises
Relevant case studies
FAQ
CTA: project assessment / complete renovation quote
```

CTA 不建议统一写成“book standalone plumbing service”。更适合写：

> Discuss this scope as part of your renovation or commercial project.

---

# 5. 小服务页面逐页问题与修改建议

## 5.1 Plumbing `/residential/plumbing/`

### 当前定位

页面已经从普通水管工页面升级为 bathroom renovation、waterproofing、repiping 和 plumbing capability 页面，内容实际上很完整。

### 问题

- URL 位于 `/residential/`，但正文同时覆盖 commercial plumbing、scheduled maintenance 和 standalone repairs。
- 页面前段同时争取 `bathroom renovation contractor` 和 `plumbing contractor`，主题有些分散。
- 页面中出现 standalone repair、leak investigation、choke clearing 等内容，可能吸引你不想承接的小维修询盘。
- `licensed plumber`、PUB compliance 等表达需要准确对应实际人员资质。

### 建议

- 保留页面，但主定位改为：
  - `Bathroom Renovation, Waterproofing & Plumbing Scope`
  - 或 `Plumbing and Wet-Area Works for Renovation Projects`
- 在首屏明确：完整浴室翻新、重铺管线和商业 M&E 是主要项目；小维修是否承接需单独说明。
- 将 standalone repair 放到页面下部，并加 `availability varies` 的边界。
- 链接至 HDB、BTO、Condo、F&B、Reinstatement 页面。
- 增加 bathroom case study，特别是 waterproofing、floor trap、repiping 前后。

### 优先级

**P1。** 内容资产很强，但需要防止吸引不符合业务范围的小询盘。

---

## 5.2 Electrical Works `/residential/electrical-works/`

### 当前问题

- 页面 H1 是 `Commercial Electrical & M&E Works in Singapore`，但 URL 是 `/residential/electrical-works/`。
- SEO 标题抓取为 `Eletrical M&E Works`，有拼写错误。
- 页面上半部分是 commercial electrical，后半部分又出现 HDB 与 landed price list，主题和 URL 层级冲突。
- 价格表重复，例如 `2WAY water heater point` 出现两次。
- 价格表中的拼写和格式问题较多：`deta point`、`doo bell`、`openet point`、`changing exising` 等。
- `in-house LEW` 只有在实际确有相应 Licensed Electrical Worker 安排和签署能力时才能使用。

### 建议

二选一：

**方案 A：保留一个通用能力页。**

- 将 URL 迁移到更中性的 `/electrical-m-and-e-works/`，设置 301 redirect。
- 页面分为 Commercial、HDB、Landed 三个 scope。
- 价格表放在折叠区域或单独 PDF/报价说明中，并标注价格有效日期、GST、材料品牌和现场条件。

**方案 B：以 Commercial 为主。**

- 保持页面 H1 为 Commercial Electrical & M&E Works。
- 从 `/residential/` hub 的小服务导航中降级或移除。
- 通过 Office、F&B、Retail、Reinstatement 页面链接到它。

我更建议方案 A，因为你同时展示 HDB 和 Landed 价格，但必须修复 URL 与 H1 的冲突。

### 优先级

**P0/P1。**

---

## 5.3 Carpentry `/residential/carpentry/`

### 当前定位

当前页面实际是 Commercial Custom Carpentry & Woodwork 页面。

### 问题

- URL 位于 `/residential/`，H1 却是 Commercial Custom Carpentry。
- 页面没有充分覆盖住宅 carpentry，但服务总览和 HDB/BTO 页面又强调 in-house carpentry。
- `save up to 30%`、`within 24 to 48 hours` 等数字需要案例或条件说明。
- 页面把商业 carpentry 的内容写得很完整，但没有直接连接到 Office、Retail、F&B、Commercial Fit-Out 案例。

### 建议

- 如果它主要服务商业项目，迁移到 `/commercial/carpentry/`，并做 301 redirect；或者改为中性 `/specialist/carpentry/`。
- 页面首屏明确：该页面是 turnkey projects 的 carpentry capability，不是默认承接单个衣柜或小型 carpentry job。
- 加住宅项目区块：kitchen cabinet、wardrobe、TV feature wall、BTO/HDB package。
- 链接到 HDB、BTO、Condo、Office、Retail、F&B 页面。
- 增加一个 factory process 和真实项目案例。

### 优先级

**P1。**

---

## 5.4 Vinyl Flooring `/residential/vinyl-flooring/`

### 问题

- H1 中 `SIngapore` 大小写错误。
- 页面定位同时覆盖 HDB、BTO、Condo、commercial，但缺少具体 installation process、substrate requirements、moisture limits、warranty 和 case studies。
- “Water-resistant” 与不同产品的 waterproof 能力要区分，不能泛化。
- 页面与 SPC vinyl flooring blog 有潜在主题重复。

### 建议

- 保留为材料/施工能力页，不主动争夺泛化的 `vinyl flooring Singapore` 主词，除非这是你确实想发展的业务。
- 主服务页面链接到它时使用上下文锚文本，例如 `SPC vinyl flooring options for HDB and commercial projects`。
- 增加适用/不适用条件、基层平整度、潮湿区域限制、维护和保修。
- 将“SPC vs porcelain tiles”文章设为信息页，链接回相关住宅项目页和该能力页。

### 优先级

**P2。**

---

## 5.5 Tiling `/residential/tiling-works/`

### 问题

- `HDB approved tiling contractor` 的表达需要与真实 HDB 登记/许可范围匹配。
- `Zero Hollow Spots Guarantee` 和 `100% coverage` 过于绝对，现场施工不宜用无条件保证。
- 页面同时覆盖住宅、商业、浴室、厨房、户外和 reinstatement，需加项目归属。
- 缺少真实案例与施工阶段照片。

### 建议

- 改成 `Tiling, Screeding & Waterproofing Works for Renovation Projects`。
- 将 `guarantee` 改为 `quality-control process` 或 `we inspect for hollow spots before handover`。
- 链接到 HDB、BTO、Condo、Reinstatement 和 Epoxy Grout 页面。
- 增加 tile overlay 与 hacking/retiling 的选择条件。

### 优先级

**P1。** 该页会涉及用户高风险的防水和结构判断，应提高准确度。

---

## 5.6 Sintered Stone `/residential/sintered-stone/`

### 问题

- 页面同时称 supplier、fabricator、installer 和 renovation contractor，需要明确公司真实角色。
- `100% heat-proof`、`will never leave a permanent stain`、`performs far better` 等表达过度绝对。
- 对 sintered stone 与 quartz、marble 的比较缺少产品和品牌条件。
- 页面有产品集合，但缺少具体项目案例和边缘/开孔/运输风险说明。

### 建议

- 定位为 `Sintered Stone Countertops & Surfaces for Renovation Projects`。
- 改成条件表达：heat-resistant、low-porosity、performance depends on product specification and installation。
- 增加 measurement、cutting、edge profile、sink cut-out、transport、installation 和 care。
- 链接到 HDB、BTO、Condo、Table Top 和 Carpentry 页面。

### 优先级

**P2。**

---

## 5.7 Table Top `/residential/table-top/`

### 问题

- H1 只有 `Table Top`，不够描述性。
- 与 Sintered Stone 页面、Countertop、Kitchen renovation 内容重叠。
- 页面混合 dining table、study table、commercial countertop、quartz、marble、epoxy resin，范围较宽。
- `100% heat-proof` 等比较需要修改。

### 建议

- H1 改为 `Custom Countertops, Islands & Table Tops in Singapore`。
- 作为 Sintered Stone / Carpentry 的 supporting page，避免与核心项目页面竞争。
- 将 Sintered Stone vs Quartz 文章作为 supporting article，并链接到本页和 BTO/HDB/Condo 页面。
- 增加按用途分类的案例：kitchen island、dining table、office reception、retail counter。

### 优先级

**P2。**

---

## 5.8 Plastering `/residential/plastering/`

### 问题

- 页面内容较薄，主要是服务列表，没有过程、基层条件、问题诊断、案例或 FAQ。
- 图片 alt 中出现 `Singapore Interior Design and Renovation Services` 和 `hdb full house flooring bundle`，可能与真实图片不匹配。
- 页面同时讲住宅、commercial、drywall 和 decorative plaster，层级较宽。

### 建议

- 不必把它打造为独立主关键词页，可作为 supporting capability page。
- H1 改为 `Plastering, Skim Coat & Wall Repair for Renovation Projects`。
- 增加 surface preparation、crack repair、drying time、paint readiness 和 project dependencies。
- 链接到 HDB resale、BTO、Office、Ceiling & Partition 和 Painting 页面。
- 修正所有图片 alt。

### 优先级

**P2。**

---

## 5.9 Painting `/residential/painting/`

### 问题

- 页面内容较薄，缺少具体 paint system、surface preparation、number of coats、drying time、occupied-home process 和 warranty。
- 主题同时覆盖 interior、exterior、feature wall、HDB、BTO、commercial。
- “eco-friendly” 和 “long-lasting” 没有产品或测试说明。

### 建议

- 作为 supporting page，H1 改为 `Painting and Surface Finishing for Renovation Projects in Singapore`。
- 增加 Nippon/Dulux 实际使用的产品与适用区域，但不要泛化所有项目。
- 链接到 HDB、BTO、Condo、Office、Decorative Paint 和 Plastering。
- 增加颜色选择、表面修补、入住中施工和维护说明。

### 优先级

**P2。**

---

## 5.10 Mirror & Glass `/residential/mirror-glass/`

### 问题

- H1 只有 `Mirror & Glass`，搜索语义不够清楚。
- 页面内容较完整，但 `interior designers can visually double the size` 之类表述偏营销，最好改成 “create the perception of a larger space”。
- `harmless pebbles` 是常见解释，但仍应以产品标准和实际 tempered glass specification 为准。
- 页面缺少具体产品、厚度、edge treatment、installation limitations 和案例归属。

### 建议

- H1 改为 `Custom Mirrors, Shower Screens & Glass Partitions in Singapore`。
- 明确该页面是 renovation scope，不是单纯零售玻璃服务。
- 增加 HDB bathroom、Condo、Office partition 三类案例。
- 链接到 Condo、BTO、Office、Carpentry 和 Ceiling & Partition。

### 优先级

**P2。**

---

## 5.11 Decorative Wall Panels `/residential/decorative-wall-panels/`

### 问题

- 页面有明确产品介绍，但“acoustic & thermal insulation”“anti-termite”“heat-resistant”等性能需要具体产品资料支撑。
- 语法问题：`All existing items that is attached`，应改为 `All existing items attached to the wall surface...`。
- 页面缺少真实项目类型、基层要求、开孔、接缝、维修和防火等级说明。
- H1 同时涵盖 homes and offices，但页面层级位于 residential。

### 建议

- H1 改为 `Decorative Wall Panels for HDB, Condos and Commercial Interiors`。
- 只保留有产品资料支持的性能表述。
- 增加尺寸、厚度、材料、安装条件、清洁和维修说明。
- 链接到 Condo、BTO、Office、Carpentry 和 Decorative Paint。

### 优先级

**P1/P2。**

---

## 5.12 Decorative Paint `/residential/decorative-paint/`

### 问题

- 页面主题清楚，但同时覆盖 limewash、concrete、metallic、faux marble、suede 和 velvet，缺少实际案例和适用条件。
- `will never curl or peel`、`zero peeling issues` 过度绝对。
- `$800–$1,800` 价格需要说明面积、基层和 finish 条件。
- “exploded in popularity this year” 不属于必要的专业事实，且没有数据来源。

### 建议

- 定位为 `Decorative Paint and Feature Wall Finishes as Part of Renovation Projects`。
- 改为“降低剥落风险”而不是“永不剥落”。
- 加入 surface preparation、primer、sealer、drying time、maintenance 和 touch-up。
- 以 2–3 个真实案例替代泛化趋势语句。

### 优先级

**P2。**

---

## 5.13 Ceiling & Partition `/residential/ceiling-partition/`

### 问题

- URL 位于 `/residential/`，H1 是 `Commercial Ceiling & Partition Services`，与 URL 层级不一致。
- 页面只覆盖商业，缺少 HDB/Condo residential scope。
- `FSSD regulations`、`SCDF and BCA fire safety codes` 需要根据实际系统、材料和项目要求准确表述。
- 缺少 fire rating、acoustic rating、ceiling height、M&E coordination 和案例资料。

### 建议

- 如果主要服务商业项目，迁移到 `/commercial/ceiling-partition/` 或 `/specialist/ceiling-partition/`，并设置 301 redirect。
- 如果保留原 URL，则 H1 改为中性：`Ceiling, Drywall & Partition Works for Renovation Projects`，并分 residential/commercial scope。
- 链接到 Office、Commercial Fit-Out、F&B、Reinstatement 和 HDB 页面。

### 优先级

**P1。** URL 与页面目标明显冲突。

---

## 5.14 Epoxy Grout `/residential/epoxy-grout/`

### 当前状态

这是小服务页中内容质量较好的一页。它有清晰定义、cement vs epoxy 对比、适用场景、regrouting、施工风险、价格因素、FAQ 和服务区域。

### 需要改进的点

- 页面内容较长，需在首屏增加 2–3 句直接答案和 scope boundary。
- `100% waterproof`、`never discolors` 等表述需改为材料和施工条件下的性能描述。
- 需要增加真实 before/after 案例。
- 需要明确是否承接 standalone regrouting，避免与实际业务政策冲突。
- 该页面可以链接至 Tiling、Bathroom、HDB、Condo、F&B 和 Commercial Reinstatement。

### 优先级

**P1/P2。**

---

## 5.15 Metallic Epoxy `/residential/metallic-epoxy-flooring/`

### 已发现的明确问题

| 原文问题 | 建议修正 |
|---|---|
| `Wateproof` | `Waterproof` |
| `Requirments` | `Requirements` |
| `Preperation` | `Preparation` |
| `installtion` | `installation` |
| `upto` | `up to` |
| `groutline` | `grout line` |
| `last for a lifetime` | 改为预计使用寿命取决于基层、产品、使用和维护 |
| `certified non-toxic by the Food and Drug Administration` | 提供真实产品、认证和适用地区依据，否则删除 |
| `withstand temperature up to 200°C` | 提供测试条件、产品说明或改为 heat-resistant |

### 建议页面结构

1. What metallic epoxy flooring is。
2. Suitable residential and commercial applications。
3. Where it should not be installed。
4. Surface preparation requirements。
5. Six-step installation process。
6. Completion and curing timeline。
7. Bathroom anti-slip options。
8. Maintenance and aftercare。
9. Real HDB / Condo / Commercial case studies。
10. Cost factors and quote CTA。

### 页面职责

该页面可以选择性争夺 `metallic epoxy flooring Singapore`，因为它是你的特色服务之一。但需要先修复英文、性能宣称和案例证据。

### 优先级

**P0/P1。**

---

## 5.16 Demolition & Hacking `/commercial/demolition-hacking-services/`

### 问题

- 页面主要是商业服务，但 URL 归在 `/commercial/`，这一点合理；需要进一步连接到 Reinstatement、Commercial Fit-Out、Office、Retail 和 F&B。
- 出现明显重复错误：`creating the perfect foundation for your your new commercial fit-out`。
- `safe structural hacking` 需要明确由 PE 或合资格专业人员判断和监督，不要让用户理解为所有结构拆除都可直接承接。
- `NEA regulations`、debris disposal 需要说明是承包范围内的安排，而不是泛化的法律保证。

### 建议

- H1 可以保留。
- 增加 method statement、risk assessment、noise hours、dust control、debris disposal、permit/PE coordination。
- 加 2–3 个 commercial case studies。
- 将页面定位为 supporting capability，并在首屏说明主要服务于 fit-out / reinstatement projects。

### 优先级

**P1。**

---

# 6. C 层：信任、实体和转化页面

## 6.1 About `/about-us/`

### 建议

- 统一公司正式名称、UEN、地址、负责人、成立/经验年份和项目数量。
- James Liang 页面应增加：职位、实际职责、资质、项目经验、审核文章列表。
- 证书图片应标注发证机构、证书名称、编号或日期（公开安全的前提下）。
- 加一段“我们承接什么、通常不承接什么”。
- 加团队或工厂真实照片，避免只有徽章和抽象描述。

### 优先级

**P1。**

---

## 6.2 Contact `/contact-us/`

### 已发现问题

- 抓取到 `Contact Form Demo`，需要确认后台是否仍然存在。
- `Submit to get a quota !` 应改为 `Submit to get a quotation` 或更自然的 `Request a quotation`。
- 页面有地址、电话、邮箱、WhatsApp 和评价，这是优势，但可以补充营业时间、服务区域、回复时间和询盘流程。

### 建议表单字段

- Name；
- Phone / WhatsApp；
- Project type；
- Property type；
- Location；
- Estimated floor area；
- Estimated budget；
- Target completion or key collection date；
- Message；
- Floor plan / tenancy agreement upload（如系统支持）。

### 转化文案

> Submit your project details. We usually reply via WhatsApp with the next steps, required documents and whether a site assessment is needed.

### 优先级

**P0。**

---

## 6.3 Portfolio `/portfolio/` 和项目案例

### 当前优势

sitemap 中已经有多个具体项目 URL，例如 HDB resale、BTO、Condo 和商业项目，这是 SEO 和 GEO 的重要资产。

### 案例页应统一包含

| 项目字段 | 示例内容 |
|---|---|
| Project type | 4-room HDB resale / 3-room BTO / Condo / Office |
| Location | 区域或街道，公开程度由客户授权决定 |
| Scope | Hacking、carpentry、flooring、M&E 等 |
| Client objective | 业主希望解决的问题 |
| Key challenge | 基层、时间、MCST、租约、空间限制 |
| Solution | 你如何处理 |
| Timeline | 开始到 handover |
| Budget | 如可公开，说明是否为 final scope |
| Materials | 品牌、规格或 finish |
| Outcome | 交付结果 |
| Review | 客户真实评价 |
| Related service | 链接至 HDB/BTO/Condo/Commercial 页面 |

案例页不要只有大量图片。**对 GEO 来说，项目事实、过程和结果比图片数量更容易被引用。**

### 优先级

**P1。**

---

## 6.4 FAQ `/faq-page/`

### 建议

- 作为全站常见问题中心，不要与每个服务页完整复制同一套 FAQ。
- FAQ 中加入页面级链接：HDB permit、BTO timeline、MCST、reinstatement、warranty、variation order。
- 每个问题只回答一个明确问题。
- 真实存在且页面可见的问题才使用 FAQ schema。

### 优先级

**P2。**

---

# 7. Blog 与核心页面的连接方式

你目前已经有大量文章，重点不是继续大量生产，而是整理“文章 → 核心服务页”的关系。

| 信息型文章主题 | 应主要链接到 |
|---|---|
| HDB renovation cost / permit | `/residential/hdb-renovation/` |
| BTO timeline / key collection / defect check | `/residential/bto-renovation/` |
| Condo renovation / MCST | `/residential/condo-renovation/` |
| Landed A&A vs rebuild | `/residential/landed-renovation/` |
| Office fit-out / office cost | `/office-renovation/` |
| Commercial reinstatement / FSSD / landlord deposit | `/commercial/reinstatement/` |
| F&B renovation / exhaust / grease trap | `/commercial/fb-cafe-renovation/` |
| Retail / salon renovation | `/commercial/salon-retail-shop-renovation/` |
| SPC vs tiles / epoxy grout / flooring | 相关核心项目页 + Tiling / Vinyl / Epoxy capability page |
| Quartz vs sintered stone | BTO / HDB / Condo + Sintered Stone / Table Top |
| Electrical / plumbing / hacking guides | 对应项目页 + 相关能力页 |

每一篇文章建议采用以下结构：

1. 首段 40–70 字直接回答问题。
2. 明确更新时间。
3. 引用 HDB、URA、BCA、SCDF、FSSD 等官方来源（涉及规定时）。
4. 提供项目类型、成本影响因素、时间和风险。
5. 中段链接到核心商业页面。
6. 结尾链接到一个真实案例和一个咨询 CTA。

---

# 8. 内部链接架构

## 8.1 核心页面之间

- Homepage → Residential / Commercial hubs。
- Residential hub → HDB / BTO / Condo / Landed / Partial Makeover。
- Commercial hub → Office / Commercial / F&B / Retail / Reinstatement。
- Services → 所有核心项目类型页面。
- 每个核心项目页 → 2–4 个相关小服务页。
- 每个小服务页 → 2–4 个核心项目页和 1–3 个案例页。
- 每个案例页 → 一个核心服务页和一个相关专业能力页。

## 8.2 锚文本建议

不要所有链接都使用 `click here` 或 `learn more`。使用描述性锚文本：

- `HDB resale renovation process`
- `BTO renovation package details`
- `MCST-compliant condo renovation`
- `commercial reinstatement scope`
- `in-house carpentry capabilities`
- `bathroom waterproofing and plumbing scope`
- `metallic epoxy flooring installation`

---

# 9. GEO 专项执行清单

## 9.1 每个核心页面都要有一个直接答案

例如 HDB 页面：

> Nouvelle Workz provides end-to-end HDB resale renovation in Singapore, including hacking, waterproofing, electrical rewiring, carpentry, tiling, painting and handover coordination.

例如 Reinstatement 页面：

> Nouvelle Workz coordinates commercial reinstatement in Singapore based on the tenant’s lease clause, covering demolition, M&E termination, MCST coordination, making-good works and landlord handover.

## 9.2 每个核心页面都要有事实表

| Fact | 内容 |
|---|---|
| Service type | HDB / BTO / Condo / etc. |
| Service area | Singapore |
| Main scope | 页面专属施工范围 |
| Typical timeline | 仅在有依据时提供 |
| Price basis | Starting price / indicative range / quote required |
| Approvals | HDB / MCST / URA / BCA / SCDF 等 |
| Project lead | James 或实际负责人 |
| Warranty | 准确说明范围和期限 |
| Last updated | 页面最后审核日期 |

## 9.3 Schema 建议

按页面真实内容使用：

- `Organization`；
- `LocalBusiness` 或更具体的业务类型；
- `Person`；
- `Service`；
- `Article`；
- `BreadcrumbList`；
- `Review` / `AggregateRating`，仅在页面真实展示并符合平台政策时使用；
- `FAQPage`，仅在 FAQ 真实展示且没有大量重复时使用。

小服务页不必全部加成独立的商业实体，也不需要把每个页面都标成独立 LocalBusiness。实体名称、地址、电话和品牌应保持一致。

---

# 10. 具体执行顺序

## 第一阶段：P0 清理

1. 清理 `/services/` 的乱码、Translator、Contact Form Demo 和 quota。
2. 清理首页 Contact Form Demo 和 quote 文案。
3. 检查所有页面的公司名、项目数、资质名称和电话号码。
4. 修复 Electrical、Metallic Epoxy、Demolition 等页面的拼写错误。
5. 调整 Reinstatement、Landed 和 Metallic Epoxy 的绝对承诺。
6. 验证表单、WhatsApp、电话和 GA4 事件。

## 第二阶段：核心页面优化

1. 重排 `/services/` 为项目类型优先。
2. 完善 HDB 和 BTO 的价格解释。
3. 增加 Condo、Commercial、Office、F&B、Retail 的真实案例。
4. 强化 Landed 的法规来源和专业责任边界。
5. 统一各页面 CTA 和询盘字段。

## 第三阶段：小服务页面降级但不删除

1. 保留小服务页面 URL，除非页面内容确实无价值。
2. 添加 turnkey scope boundary。
3. 修正 URL 与页面目标冲突的页面，特别是 Electrical、Carpentry、Ceiling & Partition。
4. 将小服务页从“单项小维修销售页”改为“项目能力证明页”。
5. 增加核心项目页与案例页内部链接。

## 第四阶段：GEO 与案例

1. 为每个核心项目页加入直接答案和事实表。
2. 统一作者、更新时间和审阅信息。
3. 为真实案例补充结构化项目事实。
4. 增加官方法规来源。
5. 检查 JSON-LD、canonical、sitemap 和 indexability。

---

# 11. 最终判断

你的现有网站不是“缺少 SEO 页面”，而是已经形成了一个相对完整的页面资产库。正确调整方向是：

- **核心项目页面负责主要关键词和询盘；**
- **小服务页面保留为专业能力和内部链接资产；**
- **Residential / Commercial 页面负责导航和主题聚合；**
- **Portfolio 页面负责真实经验和 GEO 证据；**
- **About / Contact 页面负责实体、资质和本地信任；**
- **Blog 页面负责问题型搜索，并把权重和用户导向核心服务页。**

最优先的工作不是增加更多 URL，而是修复现有页面中的乱码、模板残留、品牌/价格/资质不一致、绝对化承诺、URL 与 H1 冲突，以及案例页缺少项目事实的问题。

---

## References

[1]: https://nouvelleworkz.com/ "Nouvelle Workz homepage"
[2]: https://nouvelleworkz.com/services/ "Nouvelle Workz services overview"
[3]: https://nouvelleworkz.com/residential/hdb-renovation/ "HDB resale renovation page"
[4]: https://nouvelleworkz.com/residential/bto-renovation/ "BTO renovation page"
[5]: https://nouvelleworkz.com/residential/condo-renovation/ "Condo renovation page"
[6]: https://nouvelleworkz.com/residential/landed-renovation/ "Landed property renovation page"
[7]: https://nouvelleworkz.com/commercial/reinstatement/ "Commercial reinstatement page"
[8]: https://nouvelleworkz.com/residential/plumbing/ "Plumbing and bathroom renovation page"
[9]: https://nouvelleworkz.com/residential/electrical-works/ "Electrical and M&E page"
[10]: https://nouvelleworkz.com/residential/carpentry/ "Commercial carpentry page"
[11]: https://nouvelleworkz.com/residential/metallic-epoxy-flooring/ "Metallic epoxy flooring page"
[12]: https://nouvelleworkz.com/robots.txt "Nouvelle Workz robots.txt"
[13]: https://nouvelleworkz.com/sitemap_index.xml "Nouvelle Workz XML sitemap index"
