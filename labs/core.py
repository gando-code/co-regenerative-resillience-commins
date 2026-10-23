"""Pure, dependency-free research demonstrations; no biological interventions."""
import math
import hashlib
import json
from collections import Counter


def number(value, low=0, high=float('inf')):
    if type(value) not in (int, float) or not math.isfinite(value) or not low <= value <= high:
        raise ValueError('Expected finite number within bounds')
    return value


def historical_distance(current, baseline):
    """CDO analogue: distance from a historical measured state, not time reversal."""
    if not current or set(current) != set(baseline):
        raise ValueError('Nonempty matching measurement keys required')
    return sum(abs(number(current[k], -1e12) - number(baseline[k], -1e12)) for k in current) / len(current)


def replica_read(values):
    """Concurrency analogue: only accept a strict majority of ALL registered nodes."""
    if not values:
        raise ValueError('At least one registered node required')
    if any(v is not None and not isinstance(v, str) for v in values):
        raise ValueError('Node state must be a string or None')
    votes = Counter(v for v in values if v is not None)
    winner = votes.most_common(1)
    if winner and winner[0][1] > len(values) / 2:
        return {'state': winner[0][0], 'quorum': True}
    return {'state': None, 'quorum': False}


def energy_budget(harvested_j, load_j, reserve_j=0):
    """Bio-resonance analogue: expose energy shortfalls instead of hiding them."""
    balance = number(harvested_j) + number(reserve_j) - number(load_j)
    return {'remaining_j': balance, 'sustainable_for_interval': balance >= 0}


def retention(before, after):
    """Lattice analogue: average accuracy change on the SAME named tasks."""
    if not before or set(before) != set(after):
        raise ValueError('Matched nonempty task sets required')
    changes = {k: number(after[k], 0, 1) - number(before[k], 0, 1) for k in before}
    return {'task_changes': changes, 'mean_change': sum(changes.values()) / len(changes)}


def allocate(capacity, requests):
    """Autopoiesis analogue: deterministic severity-first allocation of finite aid."""
    left = number(capacity)
    if len({r['id'] for r in requests}) != len(requests):
        raise ValueError('Request IDs must be unique')
    for r in requests:
        number(r['need'])
        number(r['severity'], 0, 5)
    results = []
    for r in sorted(requests, key=lambda x: (-x['severity'], x['id'])):
        given = min(left, r['need'])
        left -= given
        results.append({'id': r['id'], 'allocated': given, 'unmet': r['need'] - given})
    return {'allocations': results, 'remaining': left}


def trusted_replicas(copies, trusted_digest):
    """Homeostasis analogue: locate ordinary copies matching an external baseline."""
    if not isinstance(trusted_digest, str) or len(trusted_digest) != 64 or any(c not in '0123456789abcdef' for c in trusted_digest):
        raise ValueError('Expected lowercase SHA-256 digest')
    return [i for i, data in enumerate(copies) if hashlib.sha256(data).hexdigest() == trusted_digest]


def phase_fraction(energy_j, mass_kg, latent_heat_j_kg):
    """Metabolic plastique analogue: idealized melt fraction at transition temperature.

    Assumes zero thermal loss and no sensible heating. Not a materials design tool.
    """
    energy = number(energy_j)
    mass = number(mass_kg)
    latent = number(latent_heat_j_kg)
    if mass == 0 or latent == 0:
        raise ValueError('Mass and latent heat must be positive')
    return min(1.0, energy / (mass * latent))


def memory_index(events):
    """Identity analogue: reversible category index; originals never rewritten."""
    groups = {}
    for position, event in enumerate(events):
        if not isinstance(event, dict) or not isinstance(event.get('category'), str):
            raise ValueError('Events need a text category')
        groups.setdefault(event['category'], []).append(position)
    encoded = json.dumps(events, sort_keys=True).encode()
    return {'groups': groups, 'original_sha256': hashlib.sha256(encoded).hexdigest(), 'original_count': len(events)}


def repetition_decode(bits):
    """Entropic dissociation analogue: classical three-copy error correction."""
    if len(bits) != 3 or any(type(b) is not int or b not in (0, 1) for b in bits):
        raise ValueError('Exactly three binary integer bits required')
    return int(sum(bits) >= 2)


def ecosystem_step(stocks, flows):
    """Hyper-flora analogue: conservative finite-resource transfer model.

    Incoming resources cannot be spent again during the same time step.
    """
    result = {k: number(v) for k, v in stocks.items()}
    outgoing = Counter()
    for flow in flows:
        source, target, amount = flow
        if source not in stocks or target not in stocks or source == target:
            raise ValueError('Distinct known source and target required')
        outgoing[source] += number(amount)
    if any(total > stocks[source] for source, total in outgoing.items()):
        raise ValueError('Insufficient source resources')
    for source, target, amount in flows:
        result[source] -= amount
        result[target] += amount
    return result
