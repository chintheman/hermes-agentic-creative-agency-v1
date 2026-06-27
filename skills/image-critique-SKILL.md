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
- Before delivering image-based creative work

## Multi-Pass Analysis

### Pass 1: Technical Quality
Evaluate using vision_analyze:
- Resolution and clarity (pixelation, blur)
- Compression artifacts
- Noise levels
- Edge sharpness
- Lighting consistency

**Factors:**
- ✅ Sharp focus on subject
- ✅ Natural-feeling lighting
- ✅ No visible artifacts or noise
- ⚠️ Slight softness (acceptable for artistic effect)
- ❌ Pixelation, banding, or obvious AI artifacts

**Score:** 1-10

### Pass 2: Color Analysis
- Dominant color harmony (complementary, analogous, monochromatic)
- Contrast levels (text vs background readability)
- Brand palette match (if brand-dna loaded)
- White balance accuracy
- Color psychology appropriateness for message

**Brand Palette Conformance:**
- Extract dominant colors from image via vision_analyze
- Compare against brand-dna palette
- Calculate match % (exact matches + harmonizing colors)

**Score:** 1-10 + Brand Match %

### Pass 3: Composition
- Rule of thirds / golden ratio
- Balance (symmetrical or intentional asymmetry)
- Focal point clarity
- Leading lines and flow
- Negative space usage
- Text placement (if copy overlaid)

**Score:** 1-10

### Pass 4: Intent Alignment
- Does the image match the creative brief?
- Appropriate for target audience
- Correct format/dimensions for platform
- Message clarity (can you tell what it's about at a glance?)

**Score:** 1-10

## Scoring Rubric

| Score | Meaning |
|---|---|
| 9-10 | Professional grade — ready for prime time |
| 7-8 | Good — minor improvements possible |
| 5-6 | Acceptable — needs noticeable improvements |
| 3-4 | Poor — significant issues |
| 1-2 | Failing — fundamental quality problems |

## Output Format

```markdown
## Image Critique
### Technical: 8/10 ✅
- Sharp focus on subject
- Slight noise in shadows
### Color: 9/10 ✅
- Brand palette match: 94%
- Good complementary harmony
### Composition: 7/10 ✅
- Strong focal point
- Could use more negative space
### Intent: 9/10 ✅
- Matches brief perfectly
## Overall: 8.3/10 — GOOD
```
