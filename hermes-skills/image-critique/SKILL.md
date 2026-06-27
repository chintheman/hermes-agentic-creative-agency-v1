---
name: image-critique
description: "Multi-pass image quality analysis — technical, color, composition, brand palette conformity. Scores 1-10 per dimension."
version: 1.0.0
author: Hermes Agent
tags: [creative, review, image, quality]
related_skills: [creative-review, brand-dna, flux-prompt-guide]
---
# Image Critique — Visual Quality Analysis

## When to Use
- Reviewing any AI-generated or human-created image
- Stage 4 of creative-agency pipeline (image branch)
- User asks "does this image look good?"

## Multi-Pass Analysis

### Pass 1: Technical Quality (1-10)
Evaluate using vision_analyze: resolution, artifacts, noise, sharpness, lighting.

### Pass 2: Color Analysis (1-10 + Brand Match %)
Dominant color harmony, contrast, brand palette match via vision_analyze, white balance.

### Pass 3: Composition (1-10)
Rule of thirds, balance, focal point, leading lines, negative space, text placement.

### Pass 4: Intent Alignment (1-10)
Does the image match the brief? Appropriate for audience? Correct format?

## Scoring Rubric
| Score | Meaning |
|---|---|
| 9-10 | Professional grade |
| 7-8 | Good — minor improvements |
| 5-6 | Acceptable — needs work |
| 3-4 | Poor — significant issues |
| 1-2 | Failing — fundamental problems |

## Output Format
```markdown
## Image Critique
### Technical: 8/10 ✅
### Color: 9/10 ✅ (94% brand match)
### Composition: 7/10 ✅
### Intent: 9/10 ✅
## Overall: 8.3/10 — GOOD
```
