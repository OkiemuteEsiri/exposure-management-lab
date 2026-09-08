# Scoring Methodology

The lab uses a transparent 0–100 model. It is illustrative rather than a claim about any employer or industry-standard production policy.

## Components

| Component | Maximum | Rationale |
|---|---:|---|
| CVSS-derived severity | 35 | Captures technical consequence |
| Threat context | 25 | Prioritizes known exploitation and exploit probability |
| External exposure | 15 | Increases urgency for internet-reachable assets |
| Business criticality | 15 | Represents organizational importance |
| Control weakness | 10 | Accounts for missing EDR or segmentation |

## Threat context

Known exploitation contributes up to 20 points. EPSS-style probability contributes up to 10 points, with the combined threat component capped at 25.

## Criticality

Asset criticality is represented on a 1–5 scale and normalized to 15 points. A production implementation should define criticality through governed business-impact criteria such as confidentiality, integrity, availability, regulatory impact, revenue dependency, safety, or operational dependency.

## Controls

The synthetic model adds risk when endpoint protection or segmentation is absent. A real implementation would include control confidence and evidence age rather than treating controls as simple booleans.

## Explainability

The engine returns every scoring component with the total. Analysts can therefore challenge data quality, override incorrect context, and explain prioritization to asset owners.

## Limitations

- Synthetic thresholds are not calibrated against real incident outcomes.
- CVSS and EPSS values are illustrative inputs in the sample dataset.
- Asset dependencies and attack paths are not yet modeled.
- Compensating controls are simplified.
- No temporal decay or vulnerability age weighting is included yet.

These limitations are intentionally documented so the portfolio does not imply unsupported precision.
