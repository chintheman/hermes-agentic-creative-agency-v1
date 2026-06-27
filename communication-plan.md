# Hermes Agentic Creative Agency V1 — Communication Plan

## How You (Human) Interact With the Agency

### Entry Points

| Method | Example | Best For |
|---|---|---|
| **Natural Language** | "Design a social post for my brand about our product launch" | Quick, single-format requests |
| **/agency command** | `/agency create ad --brand mybrand --brief "Q3 campaign"` | Complex, multi-format projects |
| **/random trigger** | `/random` + creative content | Capturing inspiration, quick bursts |
| **Feedback / iteration** | "The font is too small" or "Make it more blue" | Refining output |

### Your Role in the Process

| You Say / Do | Agency Does |
|---|---|
| "Make a [format] for [brand] about [topic]" | Loads brand, runs pipeline, delivers output |
| "Review this" | Runs full quality gate, reports scores |
| "Change [specific thing]" | Applies specific change (not full redo) |
| "Make another version" | Iterates with learned feedback |
| "What can you make?" | Lists capabilities, formats, brands loaded |

### What to Expect

| Stage | What Happens | You See |
|---|---|---|
| Brief | I clarify format, brand, audience, deadline | ✅ "Brief locked" |
| Ideation | 3-5 creative directions | Optional — only if you want |
| Creation | Copy + Visual generation | Silent — working |
| Review | Quality gate runs | Scores + SHIP/FIX/REVISE/BLOCK verdict |
| Delivery | Output shared | ✅ MEDIA: file + gate report |

### When I'll Ask You

1. **First use of a new brand** — Need you to confirm brand details
2. **Ambiguous brief** — Need clarification on format or audience
3. **BLOCK verdict** — Creative direction problem, needs your input
4. **After 2 FIX cycles** — Escalating to you for decision

### When I Won't Ask

- Normal pipeline execution — I just do it
- Minor format decisions — I pick the right format
- Tool/model selection — I route to the best model per task
- Quality checks — Built into the pipeline

## Scenario Cards

### Scenario 1: Quick Social Post
```
You: "Make a LinkedIn post about our new AI feature"
Me:  ✅ Brand? (asks if first time or uses default)
     ✅ Copy written, reviewed
     ✅ Visual generated, gate passed
     ✅ Here's your post + brand-check scores
```

### Scenario 2: Full Campaign
```
You: "Create a launch campaign for Product X"
Me:  ✅ Clarify: format, audience, channels
     ✅ Research: competitive landscape
     ✅ Ideation: 3 directions
     ✅ You pick one → I execute
     ✅ Review gate → SHIP
     ✅ Deliverables: social post, landing page, email copy
```

### Scenario 3: Review Existing Work
```
You: "Review this logo"
Me:  ✅ Loads brand DNA
     ✅ Image critique: technical, color, composition  
     ✅ Brand check: palette, tone, positioning
     ✅ Critic handbook: 5-dimension score
     ✅ Verdict: SHIP / FIX / REVISE / BLOCK
```

### Scenario 4: Iterate
```
You: "The colors don't work, make it warmer"
Me:  ✅ Records feedback in agency memory
     ✅ Adjusts palette to warmer spectrum
     ✅ Re-runs appropriate stages
     ✅ New output with updated brand check
```

### Scenario 5: Multi-Format Campaign
```
You: "Create a campaign for Q3 launch"
Me:  ✅ Clarifies: brand, message, platforms
     ✅ Routes: copy → visual → video → web (parallel)
     ✅ All outputs through review gate
     ✅ Delivers: 3 social posts, 1 video, 1 landing page
     ✅ All with brand scores
```
