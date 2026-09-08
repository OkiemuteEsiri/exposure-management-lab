# Exposure Management Lab

A recruiter-facing security engineering project demonstrating how vulnerability, asset, exploitability, exposure, and business-context data can be normalized into an explainable exposure-prioritization workflow.

> **Scope:** defensive, synthetic, and lab-only. This repository contains no employer/client data, production targets, credentials, or fabricated real-world findings.

## Why this project exists

Traditional vulnerability management often ranks findings by severity alone. Exposure management requires broader context: whether an asset is internet-facing, business critical, exploitable, associated with known exploitation, poorly controlled, or strategically important.

This lab models that decision process as an engineering pipeline:

```text
Synthetic Assets + Vulnerability Findings + Threat Context
                         |
                         v
              Data Normalization Layer
                         |
                         v
                Exposure Scoring Engine
                         |
          +--------------+--------------+
          |                             |
          v                             v
 Prioritized Findings             Exposure Metrics
          |                             |
          +--------------+--------------+
                         v
               Remediation Decisions
                         |
                         v
                 Validation / Retest
```

## Capabilities demonstrated

- Risk-based vulnerability prioritization
- Asset criticality and external-exposure context
- KEV/EPSS-style threat enrichment concepts
- Explainable weighted scoring
- Remediation SLA assignment
- Exposure aggregation by owner and asset group
- Defensive attack-surface reasoning
- Synthetic security-data engineering
- Unit-testable Python implementation
- Executive and technical reporting concepts

## Repository structure

```text
.
├── README.md
├── src/
│   └── exposure_engine.py
├── data/
│   ├── synthetic_assets.csv
│   └── synthetic_findings.csv
├── tests/
│   └── test_exposure_engine.py
├── docs/
│   ├── architecture.md
│   ├── scoring-methodology.md
│   └── remediation-validation.md
└── reports/
    └── example-exposure-report.md
```

## Exposure model

The engine combines five context dimensions:

| Dimension | Purpose |
|---|---|
| Vulnerability severity | Technical consequence if exploited |
| Known exploitation | Raises urgency for vulnerabilities associated with active exploitation |
| External exposure | Distinguishes internet-reachable from internal-only assets |
| Asset criticality | Represents business/process importance |
| Control weakness | Captures weak segmentation, missing EDR, or weak compensating controls |

Scores are intentionally explainable. Each component is retained so an analyst can answer **why** a finding was prioritized.

## Example usage

```bash
python src/exposure_engine.py \
  --assets data/synthetic_assets.csv \
  --findings data/synthetic_findings.csv
```

Example output:

```text
EXP-001 | score=94.0 | tier=Critical | owner=Platform Security
EXP-004 | score=77.0 | tier=High     | owner=Infrastructure
EXP-002 | score=58.0 | tier=Medium   | owner=Business Apps
```

## Risk tiers

| Score | Tier | Example handling |
|---:|---|---|
| 85–100 | Critical | Immediate triage and accelerated remediation |
| 70–84 | High | Prioritized remediation and owner escalation |
| 45–69 | Medium | Planned remediation with context review |
| 0–44 | Low | Standard backlog or accepted control review |

These are lab thresholds, not claims about a real organization's policy.

## Engineering workflow

1. Normalize asset and vulnerability records.
2. Enrich findings with asset and threat context.
3. Calculate an explainable exposure score.
4. Group findings by risk tier, owner, and asset group.
5. Assign remediation urgency.
6. Track remediation evidence.
7. Reassess after patching or compensating controls.
8. Confirm residual exposure has reduced.

## Testing

The unit tests validate:

- criticality normalization
- score boundaries
- known-exploitation weighting
- external-exposure weighting
- missing-asset handling
- tier assignment

Run with:

```bash
python -m unittest discover -s tests -v
```

## Security and ethics

All datasets are synthetic. The project is designed to demonstrate defensive exposure-management engineering, not scanning or targeting live systems.

## Skills demonstrated

`Python` · `Vulnerability Management` · `Exposure Management` · `Risk Prioritization` · `Security Data Engineering` · `Threat Context` · `Asset Criticality` · `Remediation Governance` · `Testing`

## Roadmap

- [x] Explainable exposure scoring engine
- [x] Synthetic asset and finding datasets
- [x] Unit tests
- [x] Architecture and scoring documentation
- [x] Example executive exposure report
- [ ] JSON/CSV export pipeline
- [ ] Trend analysis across reporting periods
- [ ] Dashboard visualization layer
- [ ] Policy-as-code thresholds
- [ ] CI workflow for automated tests
