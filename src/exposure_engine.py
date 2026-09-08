from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List


@dataclass(frozen=True)
class Asset:
    asset_id: str
    hostname: str
    asset_group: str
    owner: str
    criticality: int
    internet_facing: bool
    edr_present: bool
    segmented: bool


@dataclass(frozen=True)
class Finding:
    finding_id: str
    asset_id: str
    cve: str
    cvss: float
    kev: bool
    epss: float


def _as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def load_assets(path: Path) -> Dict[str, Asset]:
    assets: Dict[str, Asset] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            asset = Asset(
                asset_id=row["asset_id"],
                hostname=row["hostname"],
                asset_group=row["asset_group"],
                owner=row["owner"],
                criticality=max(1, min(5, int(row["criticality"]))),
                internet_facing=_as_bool(row["internet_facing"]),
                edr_present=_as_bool(row["edr_present"]),
                segmented=_as_bool(row["segmented"]),
            )
            assets[asset.asset_id] = asset
    return assets


def load_findings(path: Path) -> List[Finding]:
    findings: List[Finding] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            findings.append(
                Finding(
                    finding_id=row["finding_id"],
                    asset_id=row["asset_id"],
                    cve=row["cve"],
                    cvss=float(row["cvss"]),
                    kev=_as_bool(row["kev"]),
                    epss=max(0.0, min(1.0, float(row["epss"]))),
                )
            )
    return findings


def calculate_exposure_score(asset: Asset, finding: Finding) -> dict:
    severity = min(35.0, (finding.cvss / 10.0) * 35.0)
    threat = (20.0 if finding.kev else 0.0) + (finding.epss * 10.0)
    threat = min(25.0, threat)
    exposure = 15.0 if asset.internet_facing else 4.0
    business = (asset.criticality / 5.0) * 15.0

    control_weakness = 0.0
    if not asset.edr_present:
        control_weakness += 5.0
    if not asset.segmented:
        control_weakness += 5.0

    total = round(min(100.0, severity + threat + exposure + business + control_weakness), 1)
    return {
        "severity_component": round(severity, 1),
        "threat_component": round(threat, 1),
        "exposure_component": round(exposure, 1),
        "business_component": round(business, 1),
        "control_component": round(control_weakness, 1),
        "score": total,
        "tier": risk_tier(total),
    }


def risk_tier(score: float) -> str:
    if score >= 85:
        return "Critical"
    if score >= 70:
        return "High"
    if score >= 45:
        return "Medium"
    return "Low"


def prioritize(assets: Dict[str, Asset], findings: Iterable[Finding]) -> List[dict]:
    results: List[dict] = []
    for finding in findings:
        asset = assets.get(finding.asset_id)
        if asset is None:
            continue
        score = calculate_exposure_score(asset, finding)
        results.append(
            {
                "finding_id": finding.finding_id,
                "asset_id": asset.asset_id,
                "hostname": asset.hostname,
                "asset_group": asset.asset_group,
                "owner": asset.owner,
                "cve": finding.cve,
                **score,
            }
        )
    return sorted(results, key=lambda item: item["score"], reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Synthetic exposure-management prioritization engine")
    parser.add_argument("--assets", type=Path, required=True)
    parser.add_argument("--findings", type=Path, required=True)
    args = parser.parse_args()

    for item in prioritize(load_assets(args.assets), load_findings(args.findings)):
        print(
            f"{item['finding_id']} | score={item['score']:.1f} | "
            f"tier={item['tier']:<8} | owner={item['owner']}"
        )


if __name__ == "__main__":
    main()
