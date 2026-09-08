# Example Exposure Report

> Synthetic demonstration only. Values below do not describe a real organization.

## Executive summary

The synthetic portfolio contains five example findings across five assets. Priority is determined by combining technical severity with known exploitation, exploit probability, internet exposure, business criticality, and control weakness.

The highest-priority examples are expected to be the internet-facing assets with high CVSS values and known-exploitation context. Internal assets may still rank highly when business criticality is high and compensating controls are weak.

## Example decision view

| Finding | Asset | Key drivers | Recommended response |
|---|---|---|---|
| EXP-001 | edge-web-01 | internet-facing, high severity, known exploitation, critical asset | immediate triage and accelerated remediation |
| EXP-004 | remote-gateway-01 | internet-facing, known exploitation, weak segmentation | urgent remediation plus segmentation review |
| EXP-003 | legacy-db-01 | critical asset, weak controls, elevated exploit probability | prioritized remediation and compensating-control review |
| EXP-002 | finance-app-02 | important business application, internal exposure | planned remediation |
| EXP-005 | dev-api-03 | lower criticality but internet exposure and missing EDR | engineering review and control improvement |

## Questions for an exposure review meeting

1. Are asset owners and business-criticality values current?
2. Are internet-exposure labels validated from authoritative sources?
3. Which critical/high exposures have exceeded remediation expectations?
4. Are accepted risks documented with expiry dates?
5. Did completed remediation measurably reduce residual exposure?
6. Are recurring exposure patterns pointing to systemic control gaps?

## Validation statement

This report is intentionally qualitative until the engine is executed against the included synthetic data. It avoids claiming test results that have not been independently executed in GitHub CI.
