# 07. Phase-Shifting Metabolic Plastique

## Adaptive Material State Simulator

### Original vision

Transform a living body between solid tissue, liquid arrays, and a coherent energy field.

### Evidence boundary

Liquid/solid changes in engineered materials do not demonstrate a living body becoming an energy field or preserving identity through that change.

### Buildable proposal

Compute an idealized latent-heat phase fraction at a transition temperature; expose energy, mass, and model assumptions.

### Testable hypothesis

A visible energy budget prevents a shape-changing materials concept from ignoring heat requirements.

### Baseline comparison

Binary phase switch with no energy cost.

### Measurements

Energy conservation, transition-time prediction error after calibration, hysteresis, losses, and cycle durability.

### Next implementation steps

Add sensible heat, losses, and hysteresis; reproduce a published material dataset before proposing any bench apparatus.

### Failure modes

Idealized assumptions, burns, leakage, fatigue, and invalid extrapolation to implants or biological tissue.

### Sponsor or collaborator fit

Soft-robotics or materials laboratory; seek literature reproduction and numerical-model review, not a consumer body-transformation device.

### Runnable source

`labs.core.phase_fraction` in `labs/core.py`. Run all examples with `python -m labs.demo`; inspect `tests/test_labs.py`.

### Six-week milestone proposal

Weeks 1–2: specify data and assumptions with an independent reviewer. Weeks 3–4: extend the demonstrator and run a preregistered baseline comparison. Weeks 5–6: publish reproducible results, failure cases, and a go/no-go recommendation. This schedule is a planning estimate, not a commitment or evidence of feasibility beyond the bounded software task.

Success means a reproducible result and honest limitations, including a null or negative result. No lab, clinical, animal, radiation, or environmental intervention is authorized by this proposal.

### Commercial/public-interest structure

Keep the reusable evaluation core open under MIT; negotiate payment for specific engineering, integration, or review milestones. No automatic royalty is implied. A real sponsor budget requires scoped labor and any institution-specific approvals. See `docs/STRATEGY.md` for professional contact routes and funding restrictions.
