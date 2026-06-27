---
name: brand-dna
description: "Brand system of record — palette, typography, voice, tone, positioning, audience. Create, view, validate brand DNA files."
version: 1.0.0
author: Hermes Agent
tags: [creative, brand, identity, design-system]
related_skills: [creative-agency, creative-review, critic-handbook]
---
# Brand DNA — Brand System of Record

## When to Use
- Creating a new brand for the agency
- Loading brand context before creative work
- Validating output against brand guidelines
- Referenced by creative-agency pipeline at Stage 0 and Stage 4

## Brand DNA Structure
Each brand is a JSON file at `~/.hermes/skills/brand-dna/brands/<brand-name>.json`

```json
{
  "brand": "Brand Name",
  "version": "1.0.0",
  "created": "2026-06-27",
  "version_history": [
    {
      "version": "1.0.1",
      "date": "2026-07-01",
      "file_path": "/path/to/asset",
      "changes": "Updated primary color, adjusted tone"
    }
  ],
  "visual": {
    "palette": {
      "primary": "#1E3C78",
      "secondary": "#C8A028",
      "accent": "#FF6B6B",
      "background": "#F5F1E8",
      "text": "#10100F"
    },
    "typography": {
      "headings": { "family": "Inter", "weight": 700, "case": "sentence" },
      "body": { "family": "Inter", "weight": 400, "size": "16px" },
      "accent": { "family": "Inter", "weight": 600, "case": "uppercase" }
    },
    "spacing": { "unit": 8, "grid": "12-column" }
  },
  "voice": {
    "tone": "professional-warm",
    "adjectives": ["confident", "approachable", "expert", "human"],
    "avoid": ["jargon", "hype", "superlatives", "corporate-speak"]
  },
  "positioning": {
    "audience": "Description of target audience",
    "differentiator": "What sets this brand apart",
    "mission": "Brand mission statement"
  }
}
```

## Structured Feedback Injection
The `brand-dna` skill automatically monitors `~/agency_workspace/feedback/` for feedback files related to brand projects. When a new creative project is initiated, `brand-dna` reads `~/agency_workspace/feedback/<project-id>.json` and injects this past human feedback directly into the creative brief, ensuring that past corrections and pivots are incorporated into future outputs.

## Feedback Schema
Feedback files must follow this format:
```json
{
  "project_id": "string",
  "brand": "string",
  "likes": ["array of what worked"],
  "changes": ["array of what was corrected"],
  "direction_changes": ["array of major pivots"],
  "applied_to": ["array of project IDs this feedback influenced"]
}
```

## Commands
- `/agency dna create <name>` — Create new brand (interactive Q&A)
- `/agency dna view <name>` — View full brand profile
- `/agency dna check <name> <file>` — Validate output against brand
- `/agency dna list` — List all brands

## Common Pitfalls
1. **Incomplete brand data.** A brand with only colors and no voice/tone produces weak creative.
2. **Not creating a brand first.** The agency needs brand context — always create brand-dna first.
3. **Stale brands.** Update the JSON when the brand evolves.
4. **Palette without hex values.** Always provide specific hex codes.
