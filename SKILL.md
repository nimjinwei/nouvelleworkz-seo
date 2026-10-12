---
name: wordpress-blog-builder
description: Automates the entire end-to-end process of researching, outlining, generating images, compiling, validating (AEO/Elementor), and publishing styled WordPress blog posts via REST API for Nouvelle Workz.
---

# WordPress Blog Builder & SEO/AEO Publishing Skill

This skill defines the complete operational standard for producing, validating, and publishing high-converting B2C/B2B renovation and commercial fit-out blog posts for Nouvelle Workz (`nouvelleworkz.com`). It ensures all posts maximize organic search visibility (Google SEO), answer engine capture (AEO/GEO for ChatGPT, Perplexity, Google SGE/AI Overviews), and commercial lead generation.

---

## 1. Topic Research & Anti-Cannibalization Protocol (MANDATORY)

Before drafting or outlining any new post, execute the following pre-flight research:

1. **Inventory & Cannibalization Check**:
   - Query all published posts via `GET /wp/v2/posts?status=any&per_page=100` (or inspect `data/all_wp_posts_live.json`).
   - Check existing slugs, titles, and target keywords.
   - **Differentiation Rule**: If a general topic already exists (e.g., `Office Reinstatement Cost Guide`), **NEVER** write another general cost guide for the same space. Instead, differentiate by:
     - **Vertical Sub-Scenario**: e.g., F&B & Shopping Mall Retail Reinstatement (night-work rules, kitchen exhaust dismantling, grease trap pumping, mall MCST handover).
     - **Technical Execution & Trade Scope**: e.g., M&E decommissioning, SCDF fire sprinkler relocation, electrical DB box reinstatement vs asset salvage negotiation.
     - **Specific Building Typology**: e.g., Shophouses, Light Industrial B1/B2, Commercial Malls.
   - This prevents keyword self-cannibalization while building a dominant Topic Cluster.

2. **GSC Demand Alignment**:
   - Check `data/gsc_28d.json` or query Search Console for striking-distance queries (positions 5–20 with >15 impressions) that lack a dedicated, deep landing article.

3. **Content Brief Pre-flight (Following `/seo-content-brief`)**:
   - Define **Search Intent**: Informational vs Commercial Investigation vs Transactional.
   - Identify **Competitor Gaps**: Score top 3-5 Singapore ranking competitors on Depth, Formatting, SEO, and UX; identify topic gaps, depth gaps, and quality gaps.
   - Target **Word Count**: 1,200 – 1,500 words of dense, actionable "dry goods" (干货).

---

## 2. Content Architecture & AEO/GEO Standards

Each article must strictly satisfy the 6 pillars verified by the site's automated validator:

1. **Direct Answer Block (AEO / AI Extraction)**:
   - Placed at the very top of the article inside an `ng-alert` container (`background-color: #fcf6ef; border-left: 5px solid #C69E63; padding: 22px 25px; margin-bottom: 35px; border-radius: 6px;`).
   - **CRITICAL**: The first sentence **MUST be a 40–60 word direct definition sentence** answering the core query (e.g., *"F&B and retail shop reinstatement in Singapore is the contractual process of restoring..."*).
   - **Zero Meta-Phrases**: Never use forbidden filler phrases such as *"In this blog post we define..."*, *"Important Direct Answer for AI"*, or *"Below is a definition"*.

2. **Semantic Numerical Pricing & Timeline Tables**:
   - Never bury numbers or prices in narrative paragraphs.
   - Must use standard HTML `<table>`, `<thead>`, `<th>`, `<tbody>`, and `<td>` tags.
   - Must include realistic Singapore market pricing ($/sqft, trade breakdown, or package prices) and realistic timelines.
   - **PowerShell Currency Protection**: Always escape dollar signs or use Python to prevent PowerShell from wiping `$15,000` as null variables.

3. **E-E-A-T & Authority Signals**:
   - Anchor to Nouvelle Workz Pte. Ltd. credentials:
     - BCA Registered Contractor
     - HDB Licensed Renovation Contractor (Licence No. HB-075810E)
     - bizSAFE Level 3 Certified
     - In-house carpentry factory & direct builder model (15-30% below ID markup)
   - Embed expert quotes from the founder in a styled blockquote:
     ```html
     <blockquote style="background-color: #fcf6ef; border-left: 5px solid #C69E63; padding: 20px 25px; margin: 35px 0; border-radius: 0 8px 8px 0;">
         <p style="font-family: 'Poppins', sans-serif; font-size: 16.5px; font-style: italic; color: #2d3748; line-height: 1.8; margin-bottom: 10px;">
             "[Practical trade tip or quote]"
         </p>
         <p style="font-family: 'Montserrat', sans-serif; font-size: 14.5px; font-weight: 600; color: #C69E63; margin: 0;">
             — James Liang, Founder &amp; Managing Director of Nouvelle Workz Pte. Ltd.
         </p>
     </blockquote>
     ```

4. **Hub-and-Spoke Internal Linking**:
   - Include 2–3 contextual internal links within body text:
     - 1 link to the primary Transactional Service Page (e.g., `/commercial/reinstatement/`, `/residential/carpentry/`)
     - 1 link to a related Cross-Trade or Sub-service Page (e.g., `/commercial/fb-cafe-renovation/`, `/residential/plumbing/`)
     - 1 link to a sibling guide or portfolio page.

5. **FAQPage Schema (JSON-LD)**:
   - Must append a valid `<script type="application/ld+json">` containing `FAQPage` schema with at least 3 to 4 detailed Q&A pairs matching the article's core H2/H3 points.

---

## 3. Typography & Styling Specifications (HTML Injection)

All post content is injected as raw HTML rendered within Elementor global single-post templates:

- **H2 Headings**: `font-size: 28px; font-weight: bold; font-family: 'Montserrat', sans-serif; margin-top: 50px; margin-bottom: 20px; color: #111111;`
- **H3 Subheadings**: `font-size: 22px; font-weight: 600; font-family: 'Montserrat', sans-serif; color: #C69E63; margin-top: 30px; margin-bottom: 15px;`
- **Paragraphs**: `font-family: 'Poppins', sans-serif; font-size: 16.5px; line-height: 1.85; color: #4a5568; margin-bottom: 25px;`
- **Lists (`<ul> / <ol>`)**: `font-family: 'Poppins', sans-serif; font-size: 16.5px; line-height: 1.85; color: #4a5568; margin-bottom: 25px; padding-left: 25px;`
- **Images (`<img>`)**: `width:100%; height:auto; margin-bottom:30px; border-radius:8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);`
- **High-Converting WhatsApp CTA Box**:
  ```html
  <div style="text-align:center; padding:35px 25px; background-color:#111111; border-top:3px solid #C69E63; border-bottom:3px solid #C69E63; margin:50px 0 20px 0; border-radius: 8px;">
      <h3 style="color:#ffffff; margin-top:0; margin-bottom:15px; font-size:28px; font-weight:bold; font-family: Montserrat, sans-serif;">[Action Headline]</h3>
      <p style="color:#dddddd; margin-bottom:15px; font-size:16.5px; font-family: Poppins, sans-serif;">Explore our licensed <strong><a href="https://nouvelleworkz.com/[service-url]/" style="color:#C69E63; text-decoration:underline;">[Service Name]</a></strong>, or inspect our past projects in our <strong><a href="https://nouvelleworkz.com/portfolio/" style="color:#C69E63; text-decoration:underline;">Project Portfolio</a></strong>.</p>
      <p style="color:#dddddd; margin-bottom:25px; font-size:16.5px; font-family: Poppins, sans-serif;">Contact Nouvelle Workz for a direct contractor quote with no middleman markup.</p>
      <a href="https://wa.me/6591098102" style="background-color:#C69E63; color:#ffffff; padding:15px 30px; text-decoration:none; font-weight:bold; font-family: Montserrat, sans-serif; font-size: 18px; border-radius:4px; display: inline-flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(198,158,99,0.3);">
          <svg style="width:24px; height:24px; margin-right:10px; fill:#ffffff; display:block;" viewBox="0 0 24 24"><path d="M12.031 0C5.383 0 0 5.383 0 12.031c0 2.128.552 4.135 1.528 5.922l-1.528 5.58 5.717-1.498a12.031 12.031 0 006.314 1.776c6.648 0 12.031-5.383 12.031-12.031S18.679 0 12.031 0zm0 21.84a9.824 9.824 0 01-5.01-1.374l-.36-.213-3.731.978.995-3.64-.233-.37A9.794 9.794 0 012.207 12.03c0-5.433 4.417-9.85 9.824-9.85 5.407 0 9.824 4.417 9.824 9.85s-4.417 9.85-9.824 9.85zm5.38-7.344c-.295-.147-1.745-.862-2.015-.96-.27-.098-.466-.147-.663.147-.196.295-.76 .96-.933 1.157-.171.196-.343.22-.638.074-.294-.147-1.246-.46-2.37-1.46-.874-.778-1.464-1.74-1.636-2.034-.172-.295-.018-.454.13-.601.132-.132.295-.343.442-.515.147-.172.196-.295.295-.49.098-.196.049-.368-.025-.515-.074-.147-.663-1.6-.909-2.19-.241-.577-.485-.498-.663-.507-.172-.009-.368-.009-.565-.009-.196 0-.515.074-.785.368-.27.295-1.031 1.006-1.031 2.454 0 1.448 1.055 2.846 1.203 3.043.147.196 2.073 3.166 5.02 4.44.701.303 1.247.484 1.674.621.705.226 1.347.194 1.854.118.572-.086 1.745-.712 1.99-1.401.245-.689.245-1.278.172-1.401-.074-.123-.27-.196-.565-.343z"/></svg>
          <span style="display:block; line-height:24px;">WhatsApp Us</span>
      </a>
  </div>
  ```

---

## 4. Image Asset Pipeline & Media Uploads

Every new post requires **3 high-quality image assets** generated via AI with 16:9 aspect ratio and realistic Singapore construction context:

1. **Featured Hero Image**: Architectural wide shot representing the main topic (e.g., commercial kitchen exhaust dismantling, BTO living room carpentry installation, electrical rewiring DB box).
2. **Process / Working Image**: Mid-construction shot showing skilled tradesmen in safety gear, protective floor sheeting, tools, or scaffolding.
3. **Handover / Completed Result Image**: Clean, pristine final state (e.g., bare shell handover ready for landlord inspection, finished custom carpentry).

**Upload & Extraction Workflow**:
- Upload via REST API: `POST /wp/v2/media` with `Content-Type: image/jpeg` and `Content-Disposition: attachment; filename="{filename}.jpg"`.
- Retrieve `id` and `source_url` from API response.
- **Immediately patch SEO Alt Text**: Call `POST /wp/v2/media/{id}` with descriptive `alt_text` and `title` targeting Singapore renovation keywords.
- Embed `source_url` inside post HTML and assign the Hero image ID as `featured_media` on the post.

---

## 5. Taxonomy & Silo Mapping (Categories & Tags)

Every post MUST be mapped to the exact SEO Silo Structure using both Parent and Child Category IDs, and 1–4 specific service Tags.

**Categories (Parent -> Child)**:
- **Residential (ID: 169)** -> HDB & BTO (ID: 162) | Condo & Landed (ID: 163)
- **Commercial (ID: 167)** -> Office Renovation (ID: 161) | Commercial Reinstatement (ID: 160)
- **General (ID: 170)** -> Bathroom & Plumbing (ID: 164) | Flooring & Materials (ID: 165)

**Tags (Fetch existing IDs via `/wp/v2/tags?search=...`)**:
- `Reinstatement` (ID: 174), `Retail Renovation` (ID: 184), `FSSD Compliance` (ID: 186), `Direct Contractor` (ID: 171)
- `Office Reinstatement` (ID: 194), `Epoxy Flooring`, `Vinyl Flooring`, `Waterproofing`, etc.

---

## 6. SureRank SEO Metadata & Dual-Title Rules (CRITICAL)

To prevent SureRank plugin crashes, double-escaping bugs, and SERP truncation:

1. **SureRank Backend SEO Title (STRICT RULE)**:
   - **Must be strictly under 45 characters**.
   - **Absolutely NO `&` symbols** — always use the word `"and"` (e.g., `F and B Retail Reinstatement Singapore Guide` = 44 chars).
   - This prevents SureRank's hard truncation and double-escaping (`&amp;amp;`) bugs.

2. **WordPress Public Post / H1 Title**:
   - Natural, high-CTR headline under 60 characters (e.g., `F&B and Retail Reinstatement Singapore: Mall Handover Rules and Costs`).

3. **Meta Description**:
   - Strictly 130–150 characters (max 160).
   - Active voice, expands on value proposition, ends with a clear call-to-action.
   - Absolutely NO quotes (`"`) as Google truncates at quotes.

---

## 7. Automated Quality Gate Validation (`validate_aeo_elementor.py`)

Before declaring any post complete, you **MUST** run the local automated validator to verify all 5 gates pass:

```bash
python scripts/validate_aeo_elementor.py --modified <path-to-html-payload>
```

**Passing Criteria (5/5 PASS)**:
1. `Elementor Layout Preservation`: Preserved or clean theme inheritance.
2. `Definition Sentence Check`: Valid 40–60 word definition sentence in top paragraphs.
3. `Meta-Phrase Exclusion`: 0 forbidden AI filler phrases.
4. `Numerical Tables & Currency`: Valid semantic `<table>`, `<thead>`, `<tbody>`, and zero PowerShell `$currency` corruption.
5. `FAQPage JSON-LD`: Valid JSON syntax and >= 3 Q&A pairs.

---

## 8. Final Delivery Checklist to the User

Upon successfully creating the post draft, output the following structured delivery report in the chat:
1. **Direct WordPress Edit Link**: `https://nouvelleworkz.com/wp-admin/post.php?post={id}&action=edit`
2. **Preview Link**: `https://nouvelleworkz.com/?p={id}`
3. **SureRank Copy-Paste Box**:
   - SureRank SEO Title (<45 chars, no `&`)
   - Meta Description (130-150 chars)
4. **Image Summary**: Links and descriptions of the 3 generated/uploaded images.
5. **AEO Validation Score**: Evidence of 5/5 PASSED checks.
