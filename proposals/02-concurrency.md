# 02. Holo-Morphological Concurrency

## Distributed Embodiment Continuity Sandbox

### Original vision

A single conscious identity exists simultaneously across biological and synthetic bodies.

### Evidence boundary

Replica consistency is an engineering property; it does not establish shared consciousness or personal survival.

### Buildable proposal

Simulate three independent software nodes, quorum reads, node loss, and divergent states; start without physical robots.

### Testable hypothesis

Explicit quorum handling prevents a surviving minority from silently overwriting a newer agreed state.

### Baseline comparison

Single local state file and last-response-wins replica reads.

### Measurements

Stale-read rate, unavailable reads, conflict rate, and recovery latency during repeatable injected failures.

### Next implementation steps

Add versioned events and network partitions; test leader loss and replay; later integrate one simulated robot with explicit operator control.

### Failure modes

Common-mode failures, lost updates, identity confusion, and unauthorized control of physical devices.

### Sponsor or collaborator fit

Distributed-systems research collaborator or robotics lab; sponsor a failure-injection benchmark rather than mind uploading.

### Runnable source

`labs.core.replica_read` in `labs/core.py`. Run all examples with `python -m labs.demo`; inspect `tests/test_labs.py`.

### Six-week milestone proposal

Weeks 1–2: specify data and assumptions with an independent reviewer. Weeks 3–4: extend the demonstrator and run a preregistered baseline comparison. Weeks 5–6: publish reproducible results, failure cases, and a go/no-go recommendation. This schedule is a planning estimate, not a commitment or evidence of feasibility beyond the bounded software task.

Success means a reproducible result and honest limitations, including a null or negative result. No lab, clinical, animal, radiation, or environmental intervention is authorized by this proposal.

### Commercial/public-interest structure

Keep the reusable evaluation core open under MIT; negotiate payment for specific engineering, integration, or review milestones. No automatic royalty is implied. A real sponsor budget requires scoped labor and any institution-specific approvals. See `docs/STRATEGY.md` for professional contact routes and funding restrictions.
