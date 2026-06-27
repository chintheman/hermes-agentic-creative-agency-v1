---
name: design-lint
description: "Web design quality assurance — checks performance, accessibility, CSS quality, responsiveness, and visual consistency."
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
- User asks "is this page production-ready?"

## Quality Checks

### 1. Performance
- Page load considerations (no heavy unoptimized assets)
- CSS efficiency (no unused styles, minified where possible)
- JavaScript impact (no blocking scripts)
- Font loading strategy
- Image optimization

**Score:** PASS / WARN / FAIL

### 2. Accessibility
- Color contrast ratios (WCAG AA minimum: 4.5:1 for text)
- Semantic HTML (proper heading hierarchy, landmarks)
- Alt text on images
- Focus indicators for keyboard navigation
- ARIA attributes where needed

**Score:** PASS / WARN / FAIL

### 3. CSS Quality
- No inline styles (use classes/IDs)
- Responsive design (works at multiple breakpoints)
- Consistent spacing (follows brand spacing unit)
- No !important overrides
- CSS custom properties for brand tokens
- Browser prefix considerations

**Score:** PASS / WARN / FAIL

### 4. Visual Consistency
- Brand palette applied correctly
- Typography follows brand specifications
- Spacing grid adherence
- Component consistency (buttons, inputs, cards look the same)
- Dark/light mode handling (if applicable)

**Score:** PASS / WARN / FAIL

### 5. Brand DNA Conformance
- Palette colors match brand-dna exactly
- Typography matches brand specs
- Tone of any copy aligns with brand voice
- Logo/branding correctly placed

**Score:** PASS / WARN / FAIL

## Scoring

| Rating | Criteria |
|---|---|
| PASS | All checks pass or minor warnings |
| WARN | 1-2 failures in non-critical areas |
| FAIL | 3+ failures or any critical failure (a11y, brand) |

## Output Format

```markdown
## Design Lint Report
### Performance: PASS ✅
- Lightweight page, optimized assets
### Accessibility: WARN ⚠️
- Color contrast on secondary button is 3.8:1 (needs 4.5:1)
- Missing alt text on decorative image
### CSS Quality: PASS ✅
- Well-structured, responsive, uses CSS custom properties
### Visual Consistency: PASS ✅
- Brand palette followed correctly
### Brand DNA: PASS ✅
- Full brand conformance
## Overall: PASS ✅ (1 warning — fix contrast)
```
