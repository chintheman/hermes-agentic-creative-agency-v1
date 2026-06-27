---
name: design-lint
description: "Web design quality assurance — checks performance, accessibility, CSS quality, responsiveness, and brand consistency."
version: 1.0.0
author: Hermes Agent
tags: [creative, review, web, design, quality]
related_skills: [creative-review, brand-dna, claude-design]
---
# Design Lint — Web Design QA

## When to Use
- Reviewing HTML/CSS web pages, landing pages, or prototypes
- Stage 4 of creative-agency pipeline (web branch)
- Before delivering any web-based creative output

## Quality Checks

### 1. Performance (PASS/WARN/FAIL)
No heavy unoptimized assets, CSS efficiency, font loading, image optimization.

### 2. Accessibility (PASS/WARN/FAIL)
Color contrast (WCAG AA 4.5:1), semantic HTML, alt text, focus indicators, ARIA.

### 3. CSS Quality (PASS/WARN/FAIL)
No inline styles, responsive design, consistent spacing, no !important, CSS custom properties.

### 4. Visual Consistency (PASS/WARN/FAIL)
Brand palette applied, typography correct, spacing grid, component consistency.

### 5. Brand DNA (PASS/WARN/FAIL)
Palette exact match, typography match, tone alignment, logo placement.

## Scoring
| Rating | Criteria |
|---|---|
| PASS | All checks pass or minor warnings |
| WARN | 1-2 failures in non-critical areas |
| FAIL | 3+ failures or any critical failure |

## Output Format
```markdown
## Design Lint Report
### Performance: PASS ✅
### Accessibility: WARN ⚠️ (contrast 3.8:1)
### CSS Quality: PASS ✅
### Visual Consistency: PASS ✅
### Brand DNA: PASS ✅
## Overall: PASS ✅ (1 warning)
```
