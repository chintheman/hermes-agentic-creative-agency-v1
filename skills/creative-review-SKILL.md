---
name: creative-review
description: "Meta-review orchestrator — runs all applicable review gates (image-critique, design-lint, brand-dna check, critic-handbook) and produces unified SHIP/FIX/REVISE/BLOCK verdict."
version: 1.0.0
author: Hermes Agent
tags: [creative, review, quality-gate, agency]
related_skills: [image-critique, design-lint, brand-dna, critic-handbook, creative-agency]
---
# Creative Review — Unified Quality Gate

## When to Use

- Stage 4 of creative-agency pipeline
- User asks to review existing creative output
- Before delivering any creative work to human
- After any visual or copy generation

## Review Process

### Step 1: Identify Output Types
Determine what was generated:
- Images/visuals → image-critique
- Web pages/HTML → design-lint
- Copy/text → copy review (inline)
- Video → frame analysis (inline)
- All → brand-dna check + critic-handbook

### Step 2: Run Applicable Gates (Parallel)

#### Image Critique (if images)
Load `image-critique` skill. Evaluate:
- Technical quality (resolution, artifacts, noise)
- Color analysis (palette match, harmony, contrast)
- Composition (rule of thirds, balance, focal point)
- Score: 1-10 per dimension

#### Design Lint (if web/HTML)
Load `design-lint` skill. Evaluate:
- Performance (Lighthouse scores where applicable)
- Accessibility (contrast, alt text, semantic HTML)
- CSS quality (no inline styles, responsive)
- Score: PASS / WARN / FAIL per category

#### Copy Review (always if text)
- Brand voice alignment
- Grammar and spelling
- Tone consistency with brand DNA
- CTA effectiveness
- Humanizer quality (no AI-isms)
- Score: 1-10

#### Brand DNA Check (always)
- Palette conformity (% match against brand palette)
- Tone alignment (matches brand voice adjectives)
- Positioning consistency
- Score: PASS / WARN / FAIL

#### Critic Handbook (always)
Load `critic-handbook` skill. 5-dimension review:
1. Craft — technical execution quality
2. Coherence — internal logic, message clarity
3. Brand Alignment — consistency with brand identity
4. Emotional Resonance — audience impact
5. Creative Ambition — originality, risk-taking
- Score: 1-10 per dimension

### Step 3: Gate Verdict

| Condition | Verdict | Action |
|---|---|---|
| All scores ≥ 7/10 AND brand check PASS | SHIP ✅ → Stage 5 |
| Any score 5-6/10 OR brand WARN | FIX 🔧 → Stage 3 with notes |
| Any score < 5/10 OR multiple WARNs | REVISE 🔄 → Stage 1 |
| Brand check FAIL or critic < 4/10 | BLOCK 🛑 → Human intervention |

### Step 4: Report

Produce structured review report:
```markdown
## Review Report
**Verdict:** SHIP ✅

### Scores
| Dimension | Score | Status |
|---|---|---|
| Image Technical | 8.5/10 | ✅ |
| Color Analysis | 9.0/10 | ✅ |
| Composition | 7.5/10 | ✅ |
| Brand Palette Match | 94% | ✅ |
| Critic: Craft | 8/10 | ✅ |
| Critic: Coherence | 9/10 | ✅ |
| Critic: Brand | 9/10 | ✅ |
| Critic: Emotion | 7/10 | ✅ |
| Critic: Ambition | 6/10 | ✅ |

### Notes
- Composition could be stronger — consider rule of thirds
- Creative ambition is average — safe but effective
```
