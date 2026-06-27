# Architecture Review Findings — Post-Build Audit

## Source: Independent Architecture Review (deleg_807fb63e)

### Critical Findings (Must Fix)

| # | Issue | Impact | Action |
|---|---|---|---|
| 1 | No Brief Refinement Loop | Ideation happens *against* a brief, not before it | Add loop: Stage -1 can push back to Stage 0 |
| 2 | No Account Manager Role | No relationship manager / client context across projects | Create `account-manager` profile |
| 3 | No Asset Versioning | FIX iterations can't track previous state | Add version tracking to delivery |
| 4 | Serial Review Gate = Bottleneck | 50-slide deck waits for full completion before review | Implement sub-gate reviews per component |
| 5 | Researcher Model Too Weak | DeepSeek Flash may hallucinate competitive research | Upgrade researcher to DS V4 Pro |

### Recommended Improvements

| # | Issue | Impact | Action |
|---|---|---|---|
| 6 | No Finance/Operations Layer | No cost tracking per project | Add compute/credit tracking |
| 7 | No Media Planner | No distribution strategy (where/when to post) | Future P2 skill |
| 8 | No "Force Ship" Override | AI could loop on subjective review indefinitely | Add human escalation with force-ship |
| 9 | CLI-first documentation weak | Power users need structured commands | Beef up /agency command docs |

### Soft Recommendations

- Sub-gate review pattern: review copy as generated, images as rendered
- Critic-handbook must be extremely specific to avoid subjective loops
- Account Manager maintains thread context per client across sessions
