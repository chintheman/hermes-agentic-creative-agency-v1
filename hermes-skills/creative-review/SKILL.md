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

## Review Process

### Step 1: Identify Output Types
Determine what was generated:
- Images/visuals → image-critique
- Web pages/HTML → design-lint
- Copy/text → copy review (inline)
- All → brand-dna check + critic-handbook

### Step 2: Run Applicable Gates (Parallel)

#### Image Critique (if images)
Load `image-critique`. Evaluate: technical, color, composition, intent. Score 1-10.

#### Design Lint (if web/HTML)
Load `design-lint`. Evaluate: perf, a11y, CSS, visual, brand. Score PASS/WARN/FAIL.

#### Copy Review (always if text)
Brand voice, grammar, tone consistency, CTA, humanizer quality. Score 1-10.

#### Brand DNA Check (always)
Palette %, tone alignment, positioning consistency. Score PASS/WARN/FAIL.

#### Critic Handbook (always)
5-dimension: Craft, Coherence, Brand, Emotion, Ambition. Score 1-10 each.

### Step 3: Gate Verdict
| Condition | Verdict |
|---|---|
| All scores ≥ 7/10 AND brand PASS | SHIP ✅ |
| Any score 5-6/10 OR brand WARN | FIX 🔧 |
| Any score < 5/10 OR multiple WARNs | REVISE 🔄 |
| Brand FAIL or critic < 4/10 | BLOCK 🛑 |
