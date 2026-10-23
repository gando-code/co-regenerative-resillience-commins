# Co-Regenerative Resilience Commons

Open-source evidence triage, recovery planning, and ten bounded research demonstrators inspired by speculative resilience concepts. Maintainer: Gerard Ando / gando-code. MIT licensed. Experimental and AI-assisted.

**Status:** software demonstrations and proposal portfolio. No evidence of immortality, biological time reversal, consciousness transfer, thermodynamic exemption, or non-spatial storage is claimed. Current tests verify code behavior, not physical or biological effectiveness.

## Start here

- [Ten new proposals and evidence boundaries](proposals/README.md)
- [Research, sponsor shortlist, and pilot plan](docs/STRATEGY.md)
- [Professional outreach drafts — not sent](docs/OUTREACH.md)
- [Contribution guide](CONTRIBUTING.md) and [security limitations](SECURITY.md)

## Run from source

Install Python 3.10 or newer, then run from the repository root. No third-party packages, API keys, containers, network connection, or administrative privileges are needed for these demonstrations.

```sh
git clone https://github.com/gando-code/co-regenerative-resillience-commins.git
cd co-regenerative-resillience-commins
python resilience.py triage examples/assets.json
python resilience.py checksum examples/assets.json
python -m labs.demo
python -m unittest discover -s tests -v
```

On Windows use `py` if needed; on macOS/Linux use `python3` if needed. Commands print JSON to your terminal. No recovery action or physical intervention is performed.

## Implemented

- Evidence triage: severity ordering, unknown states, conflicting observations, file checksums.
- Ten small research demonstrations: historical-state distance, quorum reads, finite energy accounting, retention metrics, finite-resource allocation, trusted-copy matching, idealized phase fraction, reversible event indexing, classical repetition decoding, and conservative ecosystem transfers.
- Synthetic examples, regression tests, proposal catalog, sponsor plan, and GitHub Actions test configuration.

Not implemented: biological rejuvenation, clinical diagnostics, consciousness models, real quantum correction, sensors, full digital twins, production distributed consensus, automatic repair, secure archive custody, or a GUI. Each toy model documents its assumptions and limits. A passing observation never becomes verified recovery in the triage core.

## Develop

Open a scoped issue covering the user problem, baseline, permitted data, acceptance test, and failure modes. Work in a feature branch, run tests, and submit a pull request. Keep personal data and credentials outside this public repository. Existing third-party tools, datasets, and model weights retain their own licenses; none are bundled here. The original uploaded PDFs are not redistributed.

## Funding

Start with a small independently reviewed pilot. The sponsor plan distinguishes customers, collaborators, grantmakers, and funding platforms, and documents eligibility restrictions. No funding, endorsement, or outreach response is claimed. Open-source licensing grants reuse rights; it does not automatically generate royalties.
