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
- Checking palette, tone, or voice consistency
- Referenced by creative-agency pipeline at Stage 0 and Stage 4

## Brand DNA Structure

Each brand is a JSON file at `~/.hermes/skills/brand-dna/brands/<brand-name>.json`

```json
{
  "brand": "Brand Name",
  "version": "1.0.0",
  "created": "2026-06-27",
  "visual": {
    "palette": {
      "primary": "#1E3C78",
      "secondary": "#C8A028",
      "accent": "#FF6B6B",
      "background": "#F5F1E8",
      "text": "#10100F",
      "neutrals": ["#F5F1E8", "#E8E0D0", "#C0B8A8", "#908878", "#605850", "#303028", "#10100F"]
    },
    "typography": {
      "headings": { "family": "Inter", "weight": 700, "case": "sentence" },
      "body": { "family": "Inter", "weight": 400, "size": "16px" },
      "accent": { "family": "Inter", "weight": 600, "case": "uppercase" }
    },
    "spacing": { "unit": 8, "grid": "12-column" },
    "logo": "path/to/logo.png"
  },
  "voice": {
    "tone": "professional-warm",
    "adjectives": ["confident", "approachable", "expert", "human"],
    "avoid": ["jargon", "hype", "superlatives", "corporate-speak"],
    "principles": [
      "Clear over clever",
      "Evidence over assertion",
      "Human-scale language"
    ]
  },
  "positioning": {
    "audience": "Description of target audience",
    "differentiator": "What sets this brand apart",
    "mission": "Brand mission statement"
  },
  "constraints": {
    "formats": ["social", "web", "print", "video"],
    "platforms": ["linkedin", "twitter", "instagram", "web"],
    "restrictions": ["no competitor mentions", "no political content"]
  }
}
```

## Commands

### Create a new brand
```
/agency dna create <brand-name>
```
Interactive: I'll ask you for palette, voice, audience details.

### View brand
```
/agency dna view <brand-name>
```
Returns full brand DNA profile.

### Validate output against brand
```
/agency dna check <brand-name> <file-or-url>
```
Runs conformance check: palette match, tone alignment, voice consistency. Returns score %.

### List all brands
```
/agency dna list
```

## Brand Memory & Context

- Brand DNA files persist in `~/.hermes/skills/brand-dna/brands/`
- Once created, brand is available for all future agency work
- Brands are loaded automatically by `creative-agency` at Stage 0
- Brand verification runs at Stage 4 review (palette match %, tone alignment)

## Common Pitfalls

1. **Incomplete brand data.** A brand with only colors and no voice/tone produces weak creative. Always fill all sections.
2. **Not creating a brand before starting work.** The agency needs brand context — always create brand-dna first.
3. **Stale brands.** Brand guidelines evolve. Update the JSON when the brand changes.
4. **Palette without hex values.** Always provide specific hex codes, not "blue" or "dark".
