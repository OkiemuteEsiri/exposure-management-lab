import unittest

from src.exposure_engine import Asset, Finding, calculate_exposure_score, prioritize, risk_tier


class ExposureEngineTests(unittest.TestCase):
    def setUp(self):
        self.asset = Asset(
            asset_id="A-1",
            hostname="edge-01",
            asset_group="Internet Services",
            owner="Security",
            criticality=5,
            internet_facing=True,
            edr_present=True,
            segmented=True,
        )

    def test_known_exploitation_increases_score(self):
        base = Finding("F-1", "A-1", "CVE-X", 9.0, False, 0.5)
        kev = Finding("F-2", "A-1", "CVE-X", 9.0, True, 0.5)
        self.assertGreater(
            calculate_exposure_score(self.asset, kev)["score"],
            calculate_exposure_score(self.asset, base)["score"],
        )

    def test_internet_exposure_increases_score(self):
        internal = Asset(**{**self.asset.__dict__, "internet_facing": False})
        finding = Finding("F-1", "A-1", "CVE-X", 8.0, False, 0.2)
        self.assertGreater(
            calculate_exposure_score(self.asset, finding)["score"],
            calculate_exposure_score(internal, finding)["score"],
        )

    def test_missing_controls_increase_score(self):
        weak = Asset(**{**self.asset.__dict__, "edr_present": False, "segmented": False})
        finding = Finding("F-1", "A-1", "CVE-X", 7.0, False, 0.1)
        self.assertGreater(
            calculate_exposure_score(weak, finding)["score"],
            calculate_exposure_score(self.asset, finding)["score"],
        )

    def test_risk_tier_boundaries(self):
        self.assertEqual(risk_tier(85), "Critical")
        self.assertEqual(risk_tier(70), "High")
        self.assertEqual(risk_tier(45), "Medium")
        self.assertEqual(risk_tier(44.9), "Low")

    def test_prioritize_skips_unknown_assets_and_sorts(self):
        assets = {self.asset.asset_id: self.asset}
        findings = [
            Finding("F-low", "A-1", "CVE-L", 4.0, False, 0.05),
            Finding("F-high", "A-1", "CVE-H", 9.8, True, 0.9),
            Finding("F-missing", "NOPE", "CVE-M", 10.0, True, 1.0),
        ]
        results = prioritize(assets, findings)
        self.assertEqual([row["finding_id"] for row in results], ["F-high", "F-low"])


if __name__ == "__main__":
    unittest.main()
