# Hermes Agentic Creative Agency V1

> An AI-powered creative agency built on Hermes Agent — delivering design, copy, video, web, and strategic creative work through autonomous agent pipelines.

## Overview

The Hermes Agentic Creative Agency is a complete multi-agent system that handles the full creative workflow: from brief intake through ideation, copywriting, visual generation, quality review, and delivery. It brings together 24+ Hermes skills, 8 specialized agent profiles, and a 7-stage quality-gated pipeline.

## Quick Start

```bash
# 1. Load the agency orchestrator
hermes -s creative-agency

# 2. Create a brand (one-time)
# Say: "Create a new brand called [name]"
# Or edit: ~/.hermes/skills/creative/brand-dna/brands/<name>.json

# 3. Start creating
# Say: "Design a social post for [brand] about [topic]"
# Or: /agency create social --brand [name] --brief "[description]"
```

## Architecture

```
User Request → Creative Director (orchestrator)
  │
  ├── Stage -1: IDEATION (optional)
  │   └── creative-ideation → 3-5 directions
  │
  ├── Stage 0: BRIEF
  │   └── brand-dna → lock brand params
  │
  ├── Stage 1: CD DELEGATION
  │   └── Route by format → specialist
  │
  ├── Stage 2: COPY
  │   └── humanizer → brand voice pass
  │
  ├── Stage 3: VISUAL
  │   ├── Image → api-image-generation / FLUX
  │   ├── Web → claude-design / HTML
  │   ├── Video → ai-video-generation
  │   └── Deck → claude-design
  │
  ├── Stage 4: REVIEW (MANDATORY)
  │   ├── image-critique → technical/color/composition
  │   ├── design-lint → a11y/CSS/perf
  │   ├── brand-dna check → palette/tone/voice
  │   └── critic-handbook → 5-dimension review
  │   └── GATE: SHIP ✅ | FIX 🔧 | REVISE 🔄 | BLOCK 🛑
  │
  └── Stage 5: DELIVERY
      └── Export → Telegram / filesystem / archive
```

## Skills (6 P0 Core + 18 Existing)

### P0 — Core Agency Infrastructure
| Skill | Purpose |
|---|---|
| `creative-agency` | 7-stage pipeline orchestrator |
| `brand-dna` | Brand system of record |
| `creative-review` | Meta-review gate orchestrator |
| `image-critique` | Multi-pass image quality analysis |
| `design-lint` | Web design QA |
| `critic-handbook` | 5-dimension creative review methodology |

### P1 — Creative Production (Existing Hermes Skills)
| Skill | Department | Purpose |
|---|---|---|
| `creative-ideation` | Strategy | Brainstorming & direction generation |
| `humanizer` | Copy | De-AI-ify text, add voice |
| `api-image-generation` | Visual | FLUX/Replicate image pipeline |
| `flux-prompt-guide` | Visual | Prompt templates & model selection |
| `claude-design` | Web | One-off HTML artifacts |
| `architecture-diagram` | Web | SVG system diagrams |
| `concept-diagrams` | Web | Educational diagrams |
| `excalidraw` | Web | Hand-drawn diagrams |
| `hyperframes` | Video | HTML-based video composition |
| `ai-video-generation` | Video | Text-to-video generation |
| `direct-text-to-video` | Video | Single-shot T2V |
| `html-comparison-report` | Delivery | Data-heavy HTML reports |
| `pexels-image-populator` | Visual | Stock photography |
| `skillui-extractor` | Research | Design system extraction |
| `design-md` | Quality | DESIGN.md token spec |
| `ai-video-production-pipeline` | Video | End-to-end video pipeline |

## Profiles (8 Specialized Agents)

| Profile | Model | Role |
|---|---|---|
| `creative-director` | DeepSeek V4 Pro | Orchestrator, pipeline runner, gate decisions |
| `copywriter` (existing) | Claude Sonnet 4.6 | Copy generation, humanizer |
| `visual-designer` | DeepSeek V4 Pro | Image generation, brand visuals |
| `video-producer` | DeepSeek V4 Flash | Video generation, compositing |
| `web-developer` | Claude Sonnet 4.6 | HTML/CSS/JS, prototypes |
| `researcher` (existing) | DeepSeek V4 Flash | Market research, trends |
| `reviewer` (existing) | DeepSeek V4 Pro | Gate review, critique |
| `delivery-agent` | DeepSeek V4 Flash | Export, delivery, archive |

## Model Routing Strategy

| Task | Model | Why |
|---|---|---|
| Orchestration, routing | DeepSeek V4 Pro | Strong reasoning, structured output |
| Copy, creative writing | Claude Sonnet 4.6 | Superior tone, voice, creativity |
| Image generation | DeepSeek V4 Pro + FLUX | Practical generation pipeline |
| Video production | DeepSeek V4 Flash | Fast, cost-effective |
| Web development | Claude Sonnet 4.6 | Better HTML/CSS artifacts |
| Research | DeepSeek V4 Flash | Fast, cheap |
| Review & critique | DeepSeek V4 Pro | Strong analytical reasoning |
| File handling, delivery | DeepSeek V4 Flash | Mechanical, no reasoning needed |

## Communication Plan

### Entry Points
1. **Natural Language** — "Design a social post for [brand] about [topic]"
2. **`/agency` commands** — Structured requests for complex projects
3. **`/random` trigger** — Quick creative bursts, inspiration capture

### Your Role
| You Do | Agency Does |
|---|---|
| Set objective & brand | Executes pipeline autonomously |
| Provide reference material | Researches + incorporates |
| Approve/reject at key gates | Routes through quality gates |
| Give creative direction | Learns from feedback |
| Define scope & deadline | Manages timeline |

### When You'll Be Asked
1. First use of a new brand — confirm brand details
2. Ambiguous brief — clarify format or audience
3. BLOCK verdict — creative direction problem
4. After 2 FIX cycles — escalation decision

## Directory Structure

```
~/.hermes/
├── skills/
│   └── creative/
│       ├── creative-agency/        ← Pipeline orchestrator
│       ├── brand-dna/              ← Brand system + brands/
│       ├── creative-review/        ← Review gate orchestrator
│       ├── image-critique/         ← Image quality analysis
│       ├── design-lint/            ← Web design QA
│       └── critic-handbook/        ← Review methodology
├── profiles/
│   ├── creative-director/          ← CD agent profile
│   ├── visual-designer/            ← Visual agent profile
│   ├── video-producer/             ← Video agent profile
│   ├── web-developer/              ← Web agent profile
│   └── delivery-agent/             ← Delivery agent profile
└── wiki/agentic-creative-agency/   ← Architecture & references
```

## License

MIT — see LICENSE file.
