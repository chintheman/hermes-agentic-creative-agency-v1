---
name: creative-agency
description: "Creative agency orchestrator. Route requests through a task-based 6-stage pipeline: Brief → CD Delegation → Copy → Visual → Review → Delivery, managed by state.json."
version: 1.2.0
author: Hermes Agent
tags: [creative, agency, orchestrator, pipeline, state-management]
related_skills: [brand-dna, creative-review, image-critique, design-lint, critic-handbook, creative-ideation, humanizer, api-image-generation, claude-design]
changelog:
  "1.2.0": "Jun 27, 2026 — Implemented task-based orchestration, state.json management, sub-gate reviews, and human checkpointing for visual generation."
  "1.1.0": "Jun 27, 2026 — Added references/pipeline-routing.md with full format→skill→model mapping, delegate_task patterns, error recovery, brand lifecycle."
---
# Creative Agency — Pipeline Orchestrator

## When to Use
- User says "design", "create", "make a [format]", "agency", "campaign"
- `/agency` command is invoked
- NL request to produce creative work (ad, social, video, website, deck, copy)

## Pipeline Orchestration

The pipeline is managed by a central Orchestrator. Each stage operates as a task handler that:
1. Reads `~/agency_workspace/projects/<project-id>/state.json`.
2. Checks completion status of required inputs.
3. Executes processing.
4. Writes results and updates completion status back to `state.json`.

### Pipeline Stages

#### Stage 0: BRIEF
Load brand-dna. Extract: objective, format, audience, tone, constraints. Write initial plan to `state.json`.

#### Stage 1: CD DELEGATION
Review `state.json`. Determine skill assignments based on `references/pipeline-routing.md`. Write assignments to `state.json`.

#### Stage 2: COPY & SUB-GATE
Generate copy.
- **Sub-gate**: Review copy against brand voice.
- **Human Checkpoint**: 🟡 "Checkpoint: approve copy direction before visual generation?"
- Update `state.json` with copy result and approval status.

#### Stage 3: VISUAL & SUB-GATE
If approved, begin Stage 3.
- **Drafting**: Generate low-resolution drafts.
- **Sub-gate**: Review low-res drafts for alignment.
- **Final Render**: Generate high-resolution assets upon approval.
- Update `state.json`.

#### Stage 4: REVIEW
Load creative-review. Run final gates. GATE VERDICT: SHIP/FIX/REVISE/BLOCK. Update `state.json`.

#### Stage 5: DELIVERY
Export, deliver via Telegram, save to archive, present final status.

## Entry Points
### Natural Language
"Design a social post for my brand about product launch"

### /agency Command
```
/agency create <format> --brand <name> --brief "..."
/agency review <file> --brand <name>
/agency status
```

## Reference Files
- `references/pipeline-routing.md` — Full format→skill→model mapping table, delegate_task patterns, error recovery, brand lifecycle.
