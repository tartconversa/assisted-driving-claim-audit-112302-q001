from __future__ import annotations

import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MaterialTests(unittest.TestCase):
    def test_files_have_declared_headers_and_rows(self):
        expected = EXPECTED
        for filename, (columns, minimum_rows) in expected.items():
            with self.subTest(filename=filename):
                with (ROOT / "data" / filename).open(encoding="utf-8-sig", newline="") as stream:
                    reader = csv.DictReader(stream)
                    rows = list(reader)
                self.assertEqual(reader.fieldnames, columns)
                self.assertGreaterEqual(len(rows), minimum_rows)
                self.assertTrue(all(None not in row for row in rows))


EXPECTED = {'claims.csv': (['claim_id', 'version', 'region', 'scenario_scope', 'wording', 'status'], 2), 'trip_summaries.csv': (['trip_id', 'version', 'vehicle_group', 'region', 'weather', 'trip_km', 'upload_coverage'], 30), 'scenario_events.csv': (['event_id', 'trip_id', 'scenario', 'event_type', 'review_status', 'review_batch'], 30), 'reviews.csv': (['review_id', 'claim_id', 'source_ref', 'scope_hash', 'decision', 'reviewed_at'], 12)}


if __name__ == "__main__":
    unittest.main()
