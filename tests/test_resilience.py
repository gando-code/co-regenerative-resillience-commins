import unittest
import tempfile
from pathlib import Path
from resilience import assess, digest


class EvidenceTests(unittest.TestCase):
    def test_conflict_cannot_verify_recovery(self):
        result = assess([{'asset': 'pump', 'severity': 5, 'observations': ['pass', 'fail']}])[0]
        self.assertEqual(result['status'], 'conflicting')
        self.assertFalse(result['recovery_verified'])

    def test_missing_observations_are_unknown(self):
        self.assertEqual(assess([{'asset': 'pump', 'severity': 5, 'observations': []}])[0]['status'], 'unknown')

    def test_priority_and_pass(self):
        result = assess([{'asset': 'b', 'severity': 1, 'observations': ['pass']}, {'asset': 'a', 'severity': 5, 'observations': ['fail']}])
        self.assertEqual(result[0]['asset'], 'a')
        self.assertEqual(result[1]['status'], 'observed_pass')
        self.assertFalse(result[1]['recovery_verified'])

    def test_invalid_values(self):
        for value in (-1, 6, float('nan'), True):
            with self.assertRaises(ValueError):
                assess([{'asset': 'a', 'severity': value, 'observations': []}])

    def test_corruption_changes_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'evidence'
            file.write_bytes(b'original')
            original = digest(file)
            file.write_bytes(b'corrupted')
            self.assertNotEqual(original, digest(file))


if __name__ == '__main__':
    unittest.main()
