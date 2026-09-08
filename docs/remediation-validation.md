# Remediation and Validation Workflow

## 1. Confirm the exposure

Before escalation, validate the asset identity, vulnerability match, network exposure, business owner, and control state. Incorrect ownership or stale inventory can distort prioritization.

## 2. Select a treatment

Possible treatments include:

- patch or upgrade the vulnerable component
- remove the vulnerable service
- restrict external exposure
- strengthen segmentation
- deploy or restore compensating controls
- decommission the asset
- formally accept residual risk through governance

## 3. Capture remediation evidence

Evidence should identify the affected asset, action taken, change timestamp, implementation owner, and relevant validation source.

## 4. Reassess

After treatment, update the synthetic asset/finding context and re-run the scoring engine. A score reduction is meaningful only when supported by changed evidence, not by manually lowering the score.

## 5. Closure criteria

A finding can be considered validated when one or more of the following are evidenced:

- vulnerable package/version is no longer present
- vulnerability scanner no longer detects the condition
- exposed service is no longer reachable from the relevant zone
- compensating control is verified and monitored
- affected asset has been retired

## 6. Exceptions

Accepted risks should have an owner, rationale, compensating controls, expiry/review date, and revalidation trigger.

## Governance metrics

Useful measures include critical exposure count, high exposure count, age of open critical exposures, internet-facing exposure count, remediation throughput, reopen rate, exception count, and residual exposure trend.
