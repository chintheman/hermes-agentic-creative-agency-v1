# Hermes Agentic Creative Agency V1 — Architecture

## 1. Research Synthesis

### 1.1 What We Studied
**Zo Blueprint** (the zip):
- 7-stage pipeline: Ideation → Brief → CD Delegation → Copy → Visual → Review → Delivery
- 33 skills (23 Zo-native + 10 Hermes-delegated)
- CLI: `zo-agency` with 8 subcommands
- Brand DNA system, creative review gate (image-critique, design-lint, critic-handbook)
- Three entry points: Natural language, CLI, Hermes `/agency`

**Real-World Creative Agency Anatomy (from research)**:
| Department | Human Role | AI Agent Equivalent |
|---|---|---|
| Account Management | Account Director, AM | Intake + Briefing Agent |
| Strategy & Planning | Strategist, Researcher | Research + Insights Agent |
| Creative | Creative Director, Copywriters, Designers, Art Directors, Animators, Videographers | Creative Director Agent, Copy Agent, Visual Generation Agents |
| Production | Producer, Production Manager | Pipeline Orchestrator + Delivery Agent |
| Media | Media Buyer, Media Planner | Distribution Agent |
| Quality/Review | QA, Brand Guardian | Review Gate Agent |
| Finance/Operations | CFO, Ops Manager | Budget + Resource Agent |

### 1.2 What We Have on Hermes (Existing Creative Skills — 16)
- `ai-video-generation`, `ai-video-production-pipeline`
- `api-image-generation`, `direct-text-to-video`
- `claude-design`, `architecture-diagram`, `concept-diagrams`, `excalidraw`
- `html-comparison-report`, `hyperframes`
- `creative-ideation`, `humanizer`, `flux-prompt-guide`
- `pexels-image-populator`, `skillui-extractor`, `design-md`

### 1.3 Gaps Identified vs Zo Blueprint + Real Agency

| Missing Component | Zo Had It? | Real Agency Need | Priority |
|---|---|---|---|
| Pipeline Orchestrator (creative-agency skill) | ✅ | ✅ Core | P0 |
| Brand DNA system | ✅ | ✅ Core | P0 |
| Creative Review Gate (comprehensive) | ✅ | ✅ Core | P0 |
| Image Critique (multi-pass analysis) | ✅ | ✅ | P0 |
| Design Lint (a11y + perf + CSS) | ✅ | ✅ | P0 |
| Critic Handbook (5-dimension review) | ✅ | ✅ | P0 |
| Account/Client Management layer | ❌ | ✅ | P1 |
| Strategy & Research Agent | ❌ | ✅ | P1 |
| Media Planning/Distribution | ❌ | ✅ | P1 |
| Budget/Resource Management | ❌ | ✅ | P2 |
| Performance Analytics/Reporting | ❌ | ✅ | P1 |
| Client Feedback Loop | ❌ | ✅ | P2 |
| Multi-format Output System | Partial | ✅ | P1 |
| Versioning/Iteration Tracking | ❌ | ✅ | P2 |
| Creative Collaboration (multi-agent handoff) | Partial | ✅ | P1 |

---

## 2. Agentic Creative Agency Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER                             │
│                                                                     │
│  Telegram DM        Telegram Group        M4 Desktop App            │
│  /agency create..   "design a post.."     Cron/Profile Mgmt         │
│  /agency status     Natural Language      Visual Dashboard          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                     INTAKE & BRIEFING LAYER                          │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Account/Client Agent — Interprets requests, clarifies      │   │
│  │  scope, format, timeline, budget, expectations. Outputs:    │   │
│  │  structured creative brief (format, audience, tone, brand,  │   │
│  │  deadline, deliverables, reference material).               │   │
│  └──────────────────────┬──────────────────────────────────────┘   │
│                         │                                           │
├─────────────────────────┼───────────────────────────────────────────┤
│                     ORCHESTRATION LAYER                             │
│                         │                                           │
│  ┌──────────────────────▼──────────────────────────────────────┐   │
│  │  Creative Director Agent — Routes to departments, manages   │   │
│  │  the pipeline, quality gates, iteration decisions.          │   │
│  │  Owns the 7-stage pipeline execution.                      │   │
│  │                                                             │   │
│  │  Pipeline:                                                   │   │
│  │  Stage -1: IDEATION (creative-ideation skill)               │   │
│  │  Stage  0: BRIEF (brand-dna + structured brief)             │   │
│  │  Stage  1: CD DELEGATION (route by format to departments)   │   │
│  │  Stage  2: COPY (copywriting + humanizer)                   │   │
│  │  Stage  3: VISUAL (image/video/web/3D/deck generation)      │   │
│  │  Stage  4: REVIEW (review gate — mandatory)                 │   │
│  │  Stage  5: DELIVERY (export + publish + share)              │   │
│  └──────────────────────┬──────────────────────────────────────┘   │
│                         │                                           │
├─────────────────────────┼───────────────────────────────────────────┤
│                     SPECIALIST DEPARTMENT LAYER                     │
│                         │                                           │
│  ┌────────┬────────┬────┴────┬────────┬────────┬────────┐          │
│  ▼        ▼        ▼        ▼        ▼        ▼        ▼           │
│ Copy    Image    Video     Web      3D      Audio    Research      │
│ Dept    Dept     Dept     Dept     Dept    Dept     Dept           │
│                                                                    │
│  COPY DEPARTMENT:                                                  │
│  ├── Copywriter Agent → headlines, body, scripts, CTAs, taglines   │
│  ├── Humanizer Pass → de-AI-ify, add brand voice                   │
│  ├── Brand Voice Enforcer → verify brand tone alignment            │
│  └── SEO/Content Strategist → keyword-aware copy                   │
│                                                                    │
│  IMAGE DEPARTMENT:                                                 │
│  ├── Canvas Designer → brand-aligned compositions                  │
│  ├── FLUX/Replicate Pipeline → AI image generation                 │
│  ├── Photo Editor → adjustments, color grading                     │
│  └── Format Exporter → PNG/JPG/SVG/WebP for destination            │
│                                                                    │
│  VIDEO DEPARTMENT:                                                 │
│  ├── AI Video Generator → text-to-video + image-to-video           │
│  ├── Hyperframes Composer → HTML-based video + captions            │
│  ├── Video Editor → trim, overlay, transitions                     │
│  └── Audio Layer → TTS, music, sound effects                       │
│                                                                    │
│  WEB DEPARTMENT:                                                   │
│  ├── Frontend Designer → HTML/CSS/JS, Tailwind, shadcn             │
│  ├── Claude Design → one-off artifacts (landing, deck, prototype)  │
│  ├── Architecture Diagrammer → SVG/Excalidraw system diagrams      │
│  └── Interactive Prototyper → rich HTML experiences                │
│                                                                    │
│  3D DEPARTMENT:                                                    │
│  ├── Three.js Specialist → 3D scenes, animations, interactions     │
│  └── SVG/Vector Artist → 2D illustrations, icons, graphics         │
│                                                                    │
│  AUDIO DEPARTMENT:                                                 │
│  ├── TTS Voice Agent → text-to-speech production                   │
│  ├── Music/Sound Designer → background scores, SFX                 │
│  └── Audio Editor → mixing, trimming, mastering                    │
│                                                                    │
│  RESEARCH DEPARTMENT:                                              │
│  ├── Market Researcher → competitive analysis, trends              │
│  ├── Content Strategist → SEO insights, content gaps               │
│  └── Brand Analyst → brand positioning, audience research          │
│                                                                    │
├─────────────────────────────────────────────────────────────────────┤
│                     REVIEW LAYER                                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Creative Review Gate — MANDATORY before delivery            │   │
│  │                                                             │   │
│  │  IMAGE REVIEW                       WEB REVIEW              │   │
│  │  ├── image-critique                ├── design-lint           │   │
│  │  │   Technical quality             │   Lighthouse (perf)    │   │
│  │  │   Color analysis                │   axe-core (a11y)      │   │
│  │  │   Composition scoring            │   Stylelint (CSS)     │   │
│  │  │   Brand palette conformity       │   Visual regression   │   │
│  │  └── Score: 1-10                   └── Score: PASS/WARN/FAIL│   │
│  │                                                             │   │
│  │  VIDEO REVIEW                       COPY REVIEW             │   │
│  │  ├── Frame analysis                ├── Brand voice check    │   │
│  │  ├── Audio sync check              ├── Grammar/spelling     │   │
│  │  ├── Duration/format check         ├── Tone consistency     │   │
│  │  └── Brand alignment              ├── CTA effectiveness    │   │
│  │                                    └── Humanizer quality    │   │
│  │                                                             │   │
│  │  CRITIC HANDBOOK — 5-Dimension Review:                      │   │
│  │    Craft · Coherence · Brand Alignment ·                    │   │
│  │    Emotional Resonance · Creative Ambition                  │   │
│  │                                                             │   │
│  │  BRAND DNA VERIFICATION:                                    │   │
│  │    Palette match % · Tone alignment · Voice check            │   │
│  │    Positioning consistency · Audience targeting             │   │
│  │                                                             │   │
│  │  GATE VERDICT:  SHIP ✅ | FIX 🔧 | REVISE 🔄 | BLOCK 🛑   │   │
│  │                                                             │   │
│  │  SHIP → Stage 5 Delivery                                    │   │
│  │  FIX → Back to Stage 3 Visual with notes                   │   │
│  │  REVISE → Back to Stage 1 CD Delegation                    │   │
│  │  BLOCK → Back to Intake for scope clarification            │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                     DELIVERY LAYER                                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Delivery Agent — Export + Publish + Notify                  │   │
│  │                                                             │   │
│  │  FORMAT                       DESTINATION                   │   │
│  │  ├── Image files              ├── Telegram (direct share)   │   │
│  │  ├── Video files              ├── Zo Computer (hosting)     │   │
│  │  ├── HTML artifacts           ├── here.now (static site)    │   │
│  │  ├── Audio files              ├── GitHub (open source)      │   │
│  │  ├── Zip bundles              ├── Local filesystem          │   │
│  │  └── Text/markdown            └── Dashboard preview          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                     KNOWLEDGE & SYSTEMS LAYER                        │
│                                                                     │
│  BRAND SYSTEM           REFERENCE LIBRARY        AGENCY MEMORY      │
│  ┌─────────────┐       ┌──────────────┐       ┌────────────────┐   │
│  │ brand-dna   │       │ design refs  │       │ client history  │   │
│  │ brand-book  │       │ style guides │       │ project arc     │   │
│  │ palette     │       │ competitor   │       │ iteration log   │   │
│  │ typography  │       │ moodboards   │       │ decisions       │   │
│  │ voice/tone  │       │ inspiration  │       │ feedback        │   │
│  └─────────────┘       └──────────────┘       └────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Hermes Profile Structure (Agent Roles)

| Profile Name | Model | Role | Skills Loaded | When Activated |
|---|---|---|---|---|
| `creative-director` | DeepSeek V4 Pro | Orchestrator — pipeline runner, quality gate, routing decisions | creative-agency, brand-dna, critic-handbook | `/agency` command or NL trigger |
| `copywriter` | Claude Sonnet 4.6 | Copy generation, headlines, scripts, CTAs, humanizer pass | humanizer, brand-dna | Delegated by CD |
| `visual-designer` | DeepSeek V4 Pro | Image generation, brand-aligned visuals | api-image-generation, flux-prompt-guide, creative-ideation | Delegated by CD |
| `video-producer` | DeepSeek V4 Flash | Video generation, compositing, audio | ai-video-generation, hyperframes, direct-text-to-video | Delegated by CD |
| `web-developer` | Claude Sonnet 4.6 | HTML/CSS/JS, landing pages, prototypes | claude-design, architecture-diagram, concept-diagrams | Delegated by CD |
| `researcher` | DeepSeek V4 Flash | Market research, competitive analysis, trends | N/A (web search tools) | Delegated by CD or Intake |
| `reviewer` | DeepSeek V4 Pro | Gate review, critique, brand verification | critic-handbook, brand-dna | Automatic Stage 4 |
| `delivery-agent` | DeepSeek V4 Flash | Export, format conversion, file delivery | N/A (file + terminal tools) | Automatic Stage 5 |

---

## 4. Skills Inventory (Hermes-Native)

### P0 — Core Agency Infrastructure (Must Build)

| Skill | Type | Description | Depends On |
|---|---|---|---|
| `creative-agency` | Orchestrator | 7-stage pipeline, route by format, manage state | All below |
| `brand-dna` | Knowledge | Brand system of record: palette, type, voice, tone, positioning | — |
| `creative-review` | Gate | Meta-review orchestrator, collects all gate verdicts | image-critique, design-lint, critic-handbook |
| `image-critique` | Analysis | Multi-pass image quality: technical, color, composition | — |
| `design-lint` | Analysis | Lighthouse, a11y, CSS, visual regression | — |
| `critic-handbook` | Methodology | 5-dimension review: Craft, Coherence, Brand, Emotion, Ambition | — |

### P1 — Department Skills (Integrate from Existing + Build)

| Skill | Source | Notes |
|---|---|---|
| `creative-ideation` | ✅ Existing | Stage -1 brainstorming |
| `humanizer` | ✅ Existing | De-AI-ify copy |
| `api-image-generation` | ✅ Existing | FLUX/Replicate pipeline |
| `flux-prompt-guide` | ✅ Existing | Prompt templates |
| `claude-design` | ✅ Existing | One-off HTML artifacts |
| `architecture-diagram` | ✅ Existing | SVG diagrams |
| `concept-diagrams` | ✅ Existing | Educational diagrams |
| `excalidraw` | ✅ Existing | Hand-drawn diagrams |
| `hyperframes` | ✅ Existing | HTML-based video |
| `ai-video-generation` | ✅ Existing | Video from text/image |
| `html-comparison-report` | ✅ Existing | Data-heavy reports |
| `direct-text-to-video` | ✅ Existing | Text-to-video |
| `pexels-image-populator` | ✅ Existing | Stock photography |
| `skillui-extractor` | ✅ Existing | Design system extraction |
| `design-md` | ✅ Existing | DESIGN.md token spec |
| `ai-video-production-pipeline` | ✅ Existing | End-to-end video pipeline |

### P2 — Future Skills

| Skill | Notes |
|---|---|
| `audio-production` | TTS + music + sound design |
| `motion-graphics` | Animation overlays, transitions |
| `media-buying` | Ad placement, budget optimization |
| `performance-analytics` | Campaign reporting, ROI tracking |
| `client-portal` | Dashboard for client feedback |
| `project-management` | Timeline, task tracking, resource allocation |
| `A/B-testing` | Creative variant testing |
| `social-media-scheduler` | Auto-posting to platforms |

---

## 5. Task Routing & Communication Flow

```
                    ┌─────────────────────────────────────┐
                    │          Human (You)                 │
                    │  "Design a launch campaign.."        │
                    │  "/agency create ad --brand X"       │
                    │  "Review this output"                │
                    └─────────────┬───────────────────────┘
                                  │
                    ┌─────────────▼───────────────────────┐
                    │  INTAKE: Session Detection           │
                    │  ──────────────────────────          │
                    │  NL trigger words → Agency mode      │
                    │  /agency command → Route directly    │
                    │  /random + creative intent → Agency  │
                    │                                      │
                    │  Clarify: format, brand, audience,   │
                    │  deadline, deliverables              │
                    └─────────────┬───────────────────────┘
                                  │ Structured Brief
                    ┌─────────────▼───────────────────────┐
                    │  CREATIVE DIRECTOR AGENT             │
                    │  ──────────────────────────          │
                    │  1. Load brand-dna for brand         │
                    │  2. Run creative-ideation (optional)  │
                    │  3. Determine format(s) needed       │
                    │  4. Delegate to departments:         │
                    │     ├─→ Copy Dept (parallel)         │
                    │     ├─→ Visual Dept (parallel)       │
                    │     ├─→ Research Dept (if needed)    │
                    │     └─→ Audio Dept (if needed)       │
                    │  5. Collect all outputs              │
                    │  6. Route to Review Gate             │
                    └─────────────┬───────────────────────┘
                                  │ All outputs collected
                    ┌─────────────▼───────────────────────┐
                    │  REVIEW GATE                         │
                    │  ──────────────────────────          │
                    │  Run applicable gates:               │
                    │  ├─ Image Critique (if images)       │
                    │  ├─ Design Lint (if web)             │
                    │  ├─ Copy Review (if text)            │
                    │  ├─ Brand DNA Check (always)         │
                    │  └─ Critic Handbook (always)         │
                    │                                      │
                    │  GATE VERDICT                         │
                    │  SHIP → Delivery                     │
                    │  FIX  → Back to Visual Dept          │
                    │  REVISE → Back to CD                 │
                    │  BLOCK → Human intervention          │
                    └─────────────┬───────────────────────┘
                                  │ SHIP
                    ┌─────────────▼───────────────────────┐
                    │  DELIVERY AGENT                      │
                    │  ──────────────────────────          │
                    │  Export in requested format          │
                    │  Deliver to Telegram / filesystem     │
                    │  Save to project archive             │
                    │  Notify human                        │
                    └─────────────────────────────────────┘
```

---

## 6. Communication Plan (Human ↔ Agency)

### 6.1 Entry Points

1. **Natural Language** (primary): "Design a social post for [brand] about [topic]"
2. **`/agency` commands**: Structured requests for complex projects
3. **`/random` trigger**: Quick creative bursts, inspiration capture

### 6.2 Human Role

| What You Do | What The Agency Does |
|---|---|
| Set objective & brand | Execute pipeline autonomously |
| Provide reference material | Research + incorporate references |
| Approve/reject at key gates | Route through quality gates |
| Give creative direction feedback | Learn from feedback (agency memory) |
| Define scope & deadline | Manage timeline & deliver on schedule |
| Review final output | Deliver with evidence of quality checks |

### 6.3 Notification Cadence

| Event | Notification |
|---|---|
| Brief received & clarified | ✅ "Brief locked — proceeding" |
| Pipeline started | "Stage 1/7: Ideation →" |
| Stage completions (non-blocking) | Silent — error-only reporting |
| Review gate verdict | 🔴 SHIP/FIX/REVISE/BLOCK with summary |
| Delivery ready | ✅ MEDIA: output files + gate scores |
| Human action needed | 🔴 "Need you: [specific decision needed]" |

### 6.4 Quality Gates that Require Human Input

- **Ambiguous brief** → Clarify format, brand, or audience
- **BLOCK verdict** → Creative direction mismatch, needs human judgment
- **Brand creation** → First-time brand setup needs approval
- **Major iteration** → After 2 FIX cycles, escalate to human

---

## 7. Directory Structure

```
~/.hermes/
├── skills/
│   ├── creative-agency/
│   │   └── SKILL.md                    ← Pipeline orchestrator
│   ├── brand-dna/
│   │   ├── SKILL.md                    ← Brand system
│   │   └── brands/                      ← Per-brand DNA files
│   │       └── <brand-name>.json
│   ├── creative-review/
│   │   └── SKILL.md                    ← Review gate orchestrator
│   ├── image-critique/
│   │   └── SKILL.md                    ← Image quality analysis
│   ├── design-lint/
│   │   └── SKILL.md                    ← Web design QA
│   └── critic-handbook/
│       └── SKILL.md                    ← Review methodology
├── scripts/
│   └── agency-*.sh                     ← Supporting scripts
├── wiki/
│   └── agentic-creative-agency/        ← Architecture, processes, references
├── profiles/
│   ├── creative-director/              ← CD agent profile
│   ├── copywriter/                     ← Copy agent profile
│   ├── visual-designer/                ← Visual agent profile
│   ├── video-producer/                 ← Video agent profile
│   ├── web-developer/                  ← Web agent profile
│   ├── researcher/                     ← Research agent profile
│   ├── reviewer/                       ← Review gate agent profile
│   └── delivery-agent/                 ← Delivery agent profile
└── config.yaml                         ← Tool + model configs
```

---

## 8. Model Routing Strategy

| Task Type | Model | Rationale |
|---|---|---|
| Orchestration, routing, gate decisions | DeepSeek V4 Pro | Strong reasoning, structured output |
| Copywriting, creative writing | Claude Sonnet 4.6 | Superior tone, voice, creativity |
| Image/visual generation | DeepSeek V4 Pro + FAL/FLUX | Practical generation pipeline |
| Video production | DeepSeek V4 Flash | Fast, cost-effective for pipeline work |
| Web development | Claude Sonnet 4.6 | Better HTML/CSS artifacts |
| Research, data collection | DeepSeek V4 Flash | Fast, cheap, sufficient |
| Review, critique, quality analysis | DeepSeek V4 Pro | Needs strong analytical reasoning |
| File handling, delivery | DeepSeek V4 Flash | Mechanical, no reasoning needed |

---

## 9. Comparison: Zo Blueprint vs Hermes Implementation

| Dimension | Zo Blueprint | Hermes (This Build) | Improvement |
|---|---|---|---|
| Platform | Zo Computer ($ expensive) | Hermes on M1 (local) | Free to run, iterate on me |
| Pipeline | 7-stage CLI-driven | NL + commands + auto-detect | More accessible |
| Skills | 33 (23 Zo + 10 Hermes) | 16 existing + 6 to build | Fewer but all Hermes-native |
| Review | Gate with 4 checks + verdict | Same + Copy Review + Video Review | Broader format coverage |
| Profiles | Single agent | 8 specialized profiles | Proper role separation |
| Human interface | CLI only | Telegram NL + commands + Desktop | Multiple entry points |
| Cost model | Zo compute credits | Local execution (cheap) | Sustainable iteration |
| Quality | Automated + critic-handbook | Same + Copy/Video specific checks | More comprehensive |
| Iteration | Manual re-run | Auto-reroute FIX → Stage 3 | Faster cycle |
