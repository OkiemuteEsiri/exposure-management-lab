# Architecture

## Objective

Transform heterogeneous security findings into a prioritized, explainable exposure backlog without relying on severity alone.

## Logical components

1. **Asset inventory** — owner, group, criticality, internet exposure, control state.
2. **Finding inventory** — vulnerability ID, CVE, CVSS, known exploitation flag, exploit-probability signal.
3. **Normalization** — convert source fields into consistent types and bounded ranges.
4. **Context join** — map each finding to the affected asset.
5. **Exposure scoring** — calculate transparent weighted components.
6. **Prioritization** — sort findings by residual exposure score.
7. **Reporting** — present technical and governance views.
8. **Validation** — re-score after remediation or compensating controls.

## Data flow

```text
asset inventory ----+
                    |
                    +--> normalize --> join --> score --> prioritize --> report
                    |
finding inventory --+
```

## Design principles

- Explainability over opaque scoring.
- Deterministic results for identical inputs.
- Synthetic data for public portfolio safety.
- Separation of business context from technical severity.
- Revalidation after remediation.
- No live scanning or production targeting.

## Extension points

The current CSV implementation can be replaced with API adapters for vulnerability scanners, CMDBs, cloud inventories, threat-intelligence feeds, or ticketing systems. Those integrations are intentionally omitted from the public lab because the goal is to demonstrate the engineering pattern without depending on proprietary systems.
