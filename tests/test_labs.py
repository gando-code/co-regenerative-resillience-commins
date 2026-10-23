import copy
import hashlib
import unittest
from labs import core


class LabTests(unittest.TestCase):
    def test_cdo_matching_keys(self):
        self.assertEqual(core.historical_distance({'x': 3}, {'x': 1}), 2)
        with self.assertRaises(ValueError):
            core.historical_distance({'x': 3}, {'y': 1})

    def test_quorum_counts_unavailable_nodes(self):
        self.assertFalse(core.replica_read(['v1', None, None])['quorum'])
        self.assertFalse(core.replica_read(['v1', 'v2'])['quorum'])
        self.assertTrue(core.replica_read(['v1', 'v1', None])['quorum'])

    def test_no_energy_creation(self):
        self.assertEqual(core.energy_budget(1, 4, 2)['remaining_j'], -1)
        self.assertFalse(core.energy_budget(1, 4, 2)['sustainable_for_interval'])

    def test_forgetting_visible(self):
        self.assertAlmostEqual(core.retention({'a': .9}, {'a': .6})['mean_change'], -.3)
        with self.assertRaises(ValueError):
            core.retention({'a': .9}, {'b': .6})

    def test_aid_conservation(self):
        result = core.allocate(5, [{'id': 'b', 'need': 5, 'severity': 1}, {'id': 'a', 'need': 3, 'severity': 5}])
        self.assertEqual(result['allocations'][0]['id'], 'a')
        self.assertEqual(sum(r['allocated'] for r in result['allocations']) + result['remaining'], 5)
        self.assertEqual(result['allocations'][1]['unmet'], 3)

    def test_external_digest(self):
        target = hashlib.sha256(b'original').hexdigest()
        self.assertEqual(core.trusted_replicas([b'bad', b'original'], target), [1])
        self.assertEqual(core.trusted_replicas([b'bad'], target), [])

    def test_phase_energy_bound(self):
        self.assertEqual(core.phase_fraction(50, 1, 100), .5)
        self.assertEqual(core.phase_fraction(150, 1, 100), 1)
        with self.assertRaises(ValueError):
            core.phase_fraction(10, 0, 100)

    def test_memory_remains_unchanged(self):
        events = [{'category': 'a', 'text': 'one'}, {'category': 'a', 'text': 'two'}]
        original = copy.deepcopy(events)
        self.assertEqual(core.memory_index(events)['groups'], {'a': [0, 1]})
        self.assertEqual(original, events)

    def test_single_bit_corrected_double_bit_not(self):
        for bits in ([1, 1, 1], [0, 1, 1], [1, 0, 1], [1, 1, 0]):
            self.assertEqual(core.repetition_decode(bits), 1)
        self.assertEqual(core.repetition_decode([0, 0, 1]), 0)

    def test_ecosystem_conservation_and_overspend(self):
        out = core.ecosystem_step({'a': 10, 'b': 2}, [('a', 'b', 3)])
        self.assertEqual(sum(out.values()), 12)
        with self.assertRaises(ValueError):
            core.ecosystem_step({'a': 10, 'b': 2}, [('a', 'b', 6), ('a', 'b', 6)])

    def test_bad_numbers_rejected(self):
        for invalid in (float('nan'), float('inf'), -1, True):
            with self.assertRaises(ValueError):
                core.energy_budget(invalid, 1)


if __name__ == '__main__':
    unittest.main()
