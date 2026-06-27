---
name: creative-agency
description: "Creative agency orchestrator. Route requests through 7-stage pipeline: Ideation → Brief → CD Delegation → Copy → Visual → Review → Delivery."
version: 1.0.0
author: Hermes Agent
tags: [creative, agency, orchestrator, pipeline]
related_skills: [brand-dna, creative-review, image-critique, design-lint, critic-handbook, creative-ideation, humanizer, api-image-generation, claude-design]
---
# Creative Agency — Pipeline Orchestrator

## When to Use

- User says "design", "create", "make a [format]", "agency", "campaign", "brand"
- `/agency` command is invoked
- Natural language request to produce creative work (ad, social post, video, website, deck, logo, copy)
- User asks for creative review or critique of existing work

## 7-Stage Pipeline

### Stage -1: IDEATION (optional)
- Load `creative-ideation` skill
- Generate 3-5 creative directions based on brief
- Present to user for selection, or auto-select if clear

### Stage 0: BRIEF
- Load `brand-dna` for target brand
- Extract: objective, format, audience, tone, constraints, deadline
- Define deliverables list
- Confirm brief with user (one question, one answer)

### Stage 1: CD DELEGATION
- Route by format to specialist departments:

| Format | Primary Skill | Secondary | Model |
|---|---|---|---|
| Ad / Social Post | api-image-generation + humanizer | creative-ideation | Claude Sonnet (copy) + DS Pro (image) |
| Landing Page / Web | claude-design | concept-diagrams | Claude Sonnet |
| Video / Animation | ai-video-generation | hyperframes | DS Flash |
| Deck / Slides | claude-design | excalidraw | Claude Sonnet |
| Logo / Brand Asset | api-image-generation | flux-prompt-guide | DS Pro |
| Copy / Script | humanizer | brand-dna | Claude Sonnet |
| Diagram / Infographic | architecture-diagram | concept-diagrams | DS Pro |
| 3D / Interactive | claude-design | — | Claude Sonnet |
| Research / Strategy | web_search | market intel | DS Flash |

### Stage 2: COPY
- Write all copy first (headlines, body, scripts, CTAs, taglines)
- Route through `humanizer` for de-AI-ification
- Verify against brand voice (from brand-dna)
- Output: copy block with line-by-line breakdown

### Stage 3: VISUAL
- Generate visuals using assigned tools and skills
- Image: api-image-generation → FLUX/Replicate pipeline
- Web: claude-design → HTML/CSS artifact
- Video: ai-video-generation → text-to-video or image-to-video
- Deck: claude-design → reveal.js / HTML
- Diagram: architecture-diagram / concept-diagrams → SVG

### Stage 4: REVIEW (MANDATORY — NEVER SKIP)
- Load `creative-review` skill
- Run applicable review gates:
  - image-critique (if images generated)
  - design-lint (if web/HTML generated)
  - brand-dna: brand check (palette, tone, voice)
  - critic-handbook: 5-dimension review
- Collect all scores → GATE VERDICT:

| Verdict | Meaning | Action |
|---|---|---|
| SHIP ✅ | All gates pass | Proceed to Stage 5 |
| FIX 🔧 | Minor issues | Back to Stage 3 with notes |
| REVISE 🔄 | Major issues | Back to Stage 1 |
| BLOCK 🛑 | Fundamental problem | Escalate to human |

### Stage 5: DELIVERY
- Export to appropriate format
- Deliver via Telegram (MEDIA for images, direct for text)
- Save to project archive (~/wiki/agentic-creative-agency/deliveries/)
- Present gate scores alongside deliverable
- Log to agency memory

## Entry Points

### Natural Language
```
"Design a social post for my brand about product launch"
"Create a landing page for our new SaaS"
"Make a 30-second video ad for the campaign"
"Review this output against our brand"
```

### /agency Command
```
/agency create ad --brand <name> --brief "..."
/agency create social --brand <name> --brief "..."
/agency create landing-page --brand <name> --brief "..."
/agency create video --brand <name> --brief "..."
/agency create deck --brand <name> --brief "..."
/agency create logo --brand <name> --brief "..."
/agency review <file> --brand <name>
/agency status
```

## Output Format

Each pipeline run produces:
1. Brief summary (1-2 sentences)
2. Stage-by-stage completion log
3. Gate scores with verdict
4. Deliverable (file, link, or text)
5. Any human action items

## Common Pitfalls

1. **Skipping Stage 4 Review.** NEVER skip. The review gate is mandatory.
2. **Not loading brand-dna first.** Always verify brand exists before starting.
3. **Running stages sequentially that could be parallel.** Copy + Research can run simultaneously.
4. **Not saving deliverables.** Always save to ~/wiki/agentic-creative-agency/deliveries/ with timestamps.
5. **Forgetting humanizer pass on copy.** AI-generated copy needs de-AI-ification.
6. **Using wrong model for the task.** Copy → Claude Sonnet. Visual → DS Pro. Video → DS Flash.
