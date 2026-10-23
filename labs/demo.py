"""Run all ten illustrative cases: python -m labs.demo"""
import hashlib
import json
from .core import (historical_distance, replica_read, energy_budget, retention,
                   allocate, trusted_replicas, phase_fraction, memory_index,
                   repetition_decode, ecosystem_step)


def run():
    return {
        '01_cdo': historical_distance({'synthetic_score': 7}, {'synthetic_score': 5}),
        '02_concurrency': replica_read(['v1', 'v1', None]),
        '03_energy': energy_budget(3, 5, 1),
        '04_learning': retention({'task_a': .8}, {'task_a': .7}),
        '05_mutual_aid': allocate(5, [{'id': 'a', 'need': 4, 'severity': 5}, {'id': 'b', 'need': 3, 'severity': 2}]),
        '06_archives': trusted_replicas([b'bad', b'original'], hashlib.sha256(b'original').hexdigest()),
        '07_materials': phase_fraction(50, 1, 100),
        '08_memory': memory_index([{'category': 'learning', 'text': 'synthetic note'}]),
        '09_correction': repetition_decode([1, 0, 1]),
        '10_ecosystem': ecosystem_step({'nursery': 10, 'habitat': 2}, [('nursery', 'habitat', 3)])
    }


if __name__ == '__main__':
    print(json.dumps({'scope': 'illustrative software outputs, not physical validation', 'results': run()}, indent=2))
