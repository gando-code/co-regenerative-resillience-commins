"""Local evidence triage demonstrator. Does not execute recovery actions."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def assess(records):
    """Use explicit uncertainty; conflicting observations never verify recovery."""
    if not isinstance(records, list):
        raise ValueError('Input must be a list')
    results = []
    for record in records:
        asset = record['asset']
        if not isinstance(asset, str) or not asset.strip():
            raise ValueError('asset must be nonempty text')
        severity = record['severity']
        if type(severity) not in (int, float) or not math.isfinite(severity) or not 0 <= severity <= 5:
            raise ValueError('severity must be between 0 and 5')
        observations = record['observations']
        if not isinstance(observations, list) or any(x not in ('pass', 'fail', 'unknown') for x in observations):
            raise ValueError('Invalid observations')
        conflict = 'pass' in observations and 'fail' in observations
        if conflict:
            status = 'conflicting'
        elif 'fail' in observations:
            status = 'failed'
        elif observations and all(x == 'pass' for x in observations):
            status = 'observed_pass'
        else:
            status = 'unknown'
        results.append({'asset': asset, 'severity': severity, 'status': status,
                        'next_step': 'review_evidence' if status != 'observed_pass' else 'independent_retest',
                        'recovery_verified': False})
    return sorted(results, key=lambda x: (-x['severity'], x['asset']))


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(65536), b''):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    triage = sub.add_parser('triage')
    triage.add_argument('input', type=Path)
    checksum = sub.add_parser('checksum')
    checksum.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        result = assess(json.loads(args.input.read_text())) if args.command == 'triage' else {'sha256': digest(args.file)}
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f'Invalid input: {exc}\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
