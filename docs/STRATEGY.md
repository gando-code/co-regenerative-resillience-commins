# From speculative resilience to a testable public-interest portfolio

Research checked October 23, 2026. Rankings, proposed budgets, timelines, and performance targets below are planning judgments, not award offers, measured outcomes, or novelty findings. Sources are primary organizational pages; funding terms can change. No sponsor was contacted and no application was submitted.

## Assessment of the uploaded PDFs

The first PDF proposes ten architectures; v2 expands the portfolio to 25. Neither supplies experimental data, reproducible calculations, engineering drawings, working code, energy budgets, or falsification criteria. The opening debug/trace messages and the concluding PASSED in the first document are generated prose, not evidence of tests. Its septillions-of-eons horizon cannot be established by available validation.

Entanglement does not provide faster-than-light messaging. IBM explains the no-communication constraint: https://www.ibm.com/quantum/blog/networked-quantum-computers . Claims of satellite quantum repair, wireless entanglement power, or instantaneous gravitational-wave messaging therefore lack the proposed communication mechanism. Neither PDF demonstrates net power extraction from vacuum fluctuations, heat disposal into extra dimensions, consciousness preservation through cosmic cycles, or construction using dark matter. Treat those as speculative questions, not capabilities for a sponsor pitch.

Magnetic pulses that dissolve population trauma, inherited photosynthetic human skin, and harmless airborne engineered symbionts have not been validated by these documents. Remove treatment claims and environmental-release proposals from the initial program. Plastic degradation and removal of metals are different chemical problems; ordinary chemistry does not convert elemental metals into carbon or nitrogen. Passive biological spread would also undermine consent and containment.

Preserve the social goals: fewer failures, recoverable records, transparent decisions, healthy environments, and affordable access. Replace unlimited promises with bounded service levels. Open licensing improves access, but does not eliminate hardware, maintenance, connectivity, or staffing costs.

## Ten stronger project proposals

### 1. Recovery Evidence Commons — build first

Replaces regenerative cognitive twins and universal repair broadcasts with an evidence-linked recovery workflow. Each asset has a fault record, observation provenance, proposed intervention, human approval, and independent post-intervention test. Begin with synthetic IT backup failures; expand only after a real pilot. Compare against the same team's spreadsheet/checklist workflow on matched cases.

First 30-day target: 30 synthetic cases, all missing evidence visibly flagged, no conflicting case labelled recovered, and a time-to-triage comparison. A later pilot should preregister what counts as restored service, record failed recoveries, and separate reviewer judgment from tool output. Proposed differentiator: one portable evidence package crossing repair and IT workflows. This combination is a hypothesis about usefulness, not a claim of invention. The included Python tool implements only a tiny deterministic triage core.

### 2. Contradiction-Aware Decision Ledger

Replaces axiom-free engines with ordinary, explicit handling of inconsistent evidence. A sensor can report healthy while a human reports failure; preserve both and request review. No claim of heat-free computation. Add timestamps, source identity, expiry rules, and a review queue. Test stale, missing, duplicate, and conflicting observations. Target: zero false verified-recovery results across an adversarial fixture set. Start with transparent rules before introducing machine learning.

### 3. Community Restore Drill Kit

Replaces cosmic memory anchors with encrypted backups, multiple failure domains, documented custody, and scheduled restoration drills. Build a reporting adapter around restic rather than another backup engine. Restic is an existing cross-platform backup project, BSD-2-Clause: https://github.com/restic/restic . Hash comparisons demonstrate byte integrity against a trusted baseline, not proof of truth or long-term availability.

Pilot target: restore a small synthetic collection from a separate backup location and report elapsed time, missing objects, and user effort. Later test key loss and unavailable custodians. Libraries, community organizations, and small businesses are practical design partners. Never promise permanence or automatically publish personal archives.

### 4. Repair-to-Reuse Evidence Passport

Turns universal self-repair into a portable history of diagnosis, parts, repair actions, and functional checks. Align export fields with the Open Repair Data Standard rather than inventing an incompatible format: https://standard.openrepair.org/standard.html . A successful repair is distinct from electrical certification, medical device clearance, or warranty.

Pilot target: document 20 noncritical donated electronics with before/after checks, failed attempts, parts cost, and handoff instructions. Measure avoided replacement only when supported by the owner's actual alternative. Ask a repair group for schema feedback and a volunteer technician for acceptance criteria. Build anonymized public examples and keep ownership records private.

### 5. Climate-Safe Room Monitor

Replaces atmospheric energy blankets with calibrated indoor environmental monitoring and actionable maintenance. Begin with existing temperature/humidity data; evaluate sensor drift against a reference instrument. Present trends and missing data without diagnosing illness or declaring a building safe. Physical ventilation changes need competent local review.

Pilot target: two rooms, two weeks, reference comparisons, alert frequency, false alarms, and maintenance burden. Hardware planning envelope: $50–$250 per small pilot depending on existing equipment; obtain actual quotes. User-controlled logs and offline export distinguish the proposed service from a mandatory cloud subscription.

### 6. Ecological Signal Observatory

Replaces interspecies mind translation with bounded acoustic classification and habitat observations. BirdNET-Analyzer provides a real starting point: https://github.com/birdnet-team/BirdNET-Analyzer . Its source-code license differs from model licenses; the model documentation lists noncommercial restrictions: https://birdnet-team.github.io/BirdNET-Analyzer/stable/models.html . Do not assume a paid service can use those weights without permission.

Pilot target: a consented dataset, expert-labelled reference subset, precision/recall by species and site, and explicit unknown classes. Remove intelligible human speech and protect sensitive species locations. Partner with an ecologist; identifying a call is not translating an animal's intent. Start with public recordings where licensing permits, not automatic deployment in public spaces.

### 7. Community Energy Scheduling Sandbox

Replaces vacuum-energy transceivers with forecast-aware load scheduling. EMHASS is an existing MIT-licensed energy optimization project: https://github.com/davidusb-geek/emhass . Compare simulations against a fixed schedule using identical demand, weather, tariffs, and equipment constraints. Begin in read-only simulation; do not switch critical equipment.

Pilot target: show modeled energy cost, peak demand, unmet service constraints, and sensitivity to wrong forecasts. Benefits may be zero or negative at some sites. Actual savings require metering, installation review, and an agreed baseline. A local solar installer can be a design partner or paid pilot buyer, not necessarily a grantmaker.

### 8. Contamination Evidence Notebook

Replaces in-body plastic-eating symbionts and handheld transmutation with sample provenance, laboratory-result tracking, uncertainty, and remediation follow-up. It is a software coordination tool, not a DIY assay or biological intervention. Work with qualified laboratories and environmental professionals.

Pilot target: synthetic records supporting units, detection limits, sample IDs, duplicate checks, and missing chain-of-custody warnings. Later evaluate agreement with professional reports. A laboratory's result is not automatically evidence of human exposure or clinical injury. No organisms, treatment instructions, or environmental release mechanisms are included.

### 9. Radiation and Disruption Readiness Explorer

Replaces universal cosmic shields with educational modeling of shielding tradeoffs, error correction, redundancy, and operational interruption. NASA's OLTARIS is an established radiation assessment resource: https://oltaris.nasa.gov/ . Access conditions and model assumptions must be checked before integration. NASA discusses shielding as a systems problem, not an absolute protective field: https://ddtrb.larc.nasa.gov/radiation/ .

Pilot target: reproduce a documented reference scenario and report assumptions, uncertainty, and limits. Start with software bit-flip fault injection rather than radiation experiments. Do not represent an educational result as a human-flight safety certification.

### 10. Public Benefit and Maintenance Ledger

Replaces automatic universal access with explicit governance: service costs, repair completion, maintainer hours, accessibility issues, and allocation decisions. Aggregate only necessary data; let communities choose priorities and challenge errors. Make the cost of keeping the system alive visible.

Pilot target: publish a monthly report covering labor, costs, failed cases, and service reach, with no identifying personal data. Do not equate users, downloads, or estimated carbon savings with proven social impact. The potential contribution is a shared evidence format linking technical performance to maintenance funding.

## Portfolio architecture and source strategy

Use one repository at first. Keep a small deterministic core; add adapters as independently tested modules. Schema fields should include asset ID, observation, timestamp, source, consent scope, units, uncertainty, evidence digest, intervention record, reviewer, and retest result. Separate sensitive evidence storage from public code. An append-only application log still needs authentication, backups, and an access-control model; it is not automatically tamper-proof.

Prefer contributing to restic, Open Repair, or existing energy tooling where the change naturally belongs. Do not fork an entire stack just to establish a brand. Record upstream URLs, pinned versions, licenses, dataset rights, and model terms before adding dependencies. Keep speculative essays under a clearly labelled research section, separate from implemented features. A local web GUI is a later deliverable after the schema works; never silently expose it to the internet.

For a release: run tests, inspect sample output, document limitations, tag v0.1.0, attach a source archive, record test environment and commit SHA, and verify the remote commit. Configure branch review and a contribution guide. Use an OSI-approved software license; the starter uses MIT. Publicly visible unlicensed source is not enough to grant normal open-source reuse rights. Avoid a noncommercial clause if describing the software as open source.

## Sponsor and collaborator shortlist

These routes serve different purposes. A fiscal host processes funds; a collaborator contributes expertise; a customer buys a pilot; a grantmaker awards funds. None implies acceptance. Ranking is based on this portfolio's present stage, not prestige.

| Route | Best project fit | Professional route and initial request | Gate / current status |
|---|---|---|---|
| Local repair nonprofit, library, or small business | 1, 3, 4 | Find its official operational contact, confirm they own the problem, request a 20-minute discovery call and one synthetic workflow | Highest practical first step; no specific organization or funding commitment verified |
| GitHub Sponsors | Maintaining the open-source core | Enroll through https://github.com/sponsors ; publish a demonstrable milestone and transparent funding use | Donation platform, not a grant or guaranteed audience; check account and country eligibility |
| Open Repair Alliance | 4 | Use https://openrepair.org/ and its official contact route; ask for schema review and introductions to repair groups | Technical collaborator; no open grant was verified |
| Conservation X Labs | 6, potentially 5 or 8 | Review https://www.conservationxlabs.com/open-innovation ; respond only to a matching active challenge or ask about a bounded field trial | Challenge/partner route; no matching currently open award or deadline verified |
| Earth Species Project | 6 | Use https://earthspecies.org/about-us/ ; ask about research collaboration or published tools and datasets | Research collaborator; receiving grants does not make it an open grantmaker for outside ideas |
| NSF America's Seed Fund | Novel research within 1, 2, or 7 | https://seedfund.nsf.gov/project-pitch/ ; describe technical uncertainty, experiments, customer need, and team | Eligible US small business and solicitation requirements; routine integration alone is weak fit; invitation needed before relevant full proposal |
| Sloan Open Source in Science | 3 or 10 with a research institution | Read https://sloan.org/programs/digital-technology/open-source-in-science ; use program's two-page inquiry route | Program emphasizes institutions, incentives, and research software stewardship, not simply a solo product build |
| NLnet Restack | Potential non-AI infrastructure component of 1 or 3 | https://nlnet.nl/restack/ and https://nlnet.nl/propose/ ; first assess eligibility and AI policy honestly | Current form lists Nov 3, 2026 noon CET deadline, strong European dimension, and restrictions on AI-generated proposals/projects; not recommended for submitting this AI-assisted package unchanged |
| Sovereign Tech Fund | Mature widely depended-on infrastructure derived from 1–3 | https://www.sovereign.tech/programs/fund ; portal only | Explicitly excludes prototypes and currently user-facing applications; work budget must exceed €50,000; later-stage option |
| NumFOCUS Small Development Grants | Relevant work contributed through an accepted scientific project | https://numfocus.org/programs/small-development-grants ; work with sponsored/affiliated project maintainers | Restricted to its sponsored/affiliated projects; not a general grant for a new unaffiliated repository; page's older rounds are not a verified 2026 call |

NLnet warning: its current application page says it is not interested in AI-generated projects or proposals, asks for own-word answers and disclosure/logs where assistance was needed. Restack also excludes AI-related projects except a narrow widely-used category. A superficial rewrite does not solve project provenance or eligibility. Do not conceal assistance or invent European collaborators. Any inquiry should be your own and address the actual policy.

Sovereign warning: it asks applicants not to send supplemental material outside the portal, and does not provide advance fit advice. Do not send it the cold email draft. Its stated process is roughly six months, so it is not immediate pilot financing.

## A concrete first sponsor offer

Proposed paid pilot: $7,500 over six weeks for one organization, up to 20 noncritical assets or synthetic recovery scenarios. This is a suggested price to negotiate, not a market quote. Exclude infrastructure procurement, travel, certification, and emergency support. Deliver an agreed evidence schema, a documented workflow, baseline comparison, a reproducible demonstration, and a final report covering failures as well as successes. Sponsor provides a point person, approved data, and weekly review access. Publish only agreed anonymized findings; sponsors receive no control over scientific conclusions.

Illustrative labor budget: discovery 15h, schema/adapters 35h, workflow/UI prototype 30h, pilot/retest analysis 25h, documentation/release 15h: 120h at $50/h = $6,000. Accessibility/security review allowance $1,000 and contingency $500 bring the total to $7,500. Validate the actual workload before signing. Third-party reviewer availability and equipment are not secured. Pay by defined milestones, for example 30% on signed scope, 40% on demonstrator acceptance, and 30% on final delivery; negotiate terms in writing.

Success gates: zero unsupported recovery claims, complete evidence on agreed cases, an independently repeated demonstration, and measured user effort against the existing process. Preregister a desired 20% median triage-time improvement, but report uncertainty and accept a null result. A small convenience sample cannot establish universal effectiveness. Agree the decision rule and stop conditions before the pilot starts.

## Outreach process and schedule

Week 1: choose project 1; personally review the source; run the demo; recruit one domain reviewer; create a one-page brief with problem, current prototype, unimplemented features, six-week experiment, and exact request. Verify each recipient's current role on the official organization site. Avoid guessed email patterns and personal inbox scraping.

Week 2: contact three to five selected prospects individually through their published business route. For portals, follow the portal and its instructions. State exactly why the recipient fits and what evidence exists. Include a repository link once genuinely published, otherwise say 'source archive available.' Do not insert a fictional URL as proof of a live project. Track date, recipient, consent, response, next step, and funding restrictions in a private tracker.

Follow up once after seven business days and optionally once more a week later if appropriate. Then close the loop politely. No mass outreach, fabricated endorsements, claims of scientific breakthroughs, or invented test outcomes. A warm introduction from a repair group, researcher, or actual pilot customer is more useful than a long speculative deck.

Weeks 3–6: conduct discovery, agree one pilot, collect baseline data, implement only agreed scope, and demonstrate failure cases. If prospects do not identify a problem worth solving after ten substantive conversations, revise the problem or contribute upstream rather than adding more features.

Weeks 7–12: publish an anonymized evaluation, invite a second independent site, obtain a maintainer review, and pursue a matching grant only when eligibility and provenance fit. Do not open ten separate projects before one gets repeated use.

## Sustainability beyond a grant

Keep the reusable core open and charge for setup, integrations, training, maintenance, hosted convenience, and sponsor-defined improvements that benefit everyone. Sponsors can fund a named milestone without owning the commons. Open source does not automatically pay royalties, and recipients of MIT-licensed code do not owe you a use fee. Any separate royalty or commercial agreement must be explicitly negotiated and compatible with rights already granted. Do not promise passive income: support and upkeep require labor.

Later options include a maintainer cooperative, fiscal sponsorship, a paid support plan, and a public evaluation consortium. A fiscal host may reduce administrative burden but normally brings eligibility checks and fees; verify current terms before choosing one. Keep a reserve for maintenance and publish what donated money supports. Avoid outcome guarantees and exclusivity that prevent public-interest reuse.

## Evidence map and limitations

Primary sources supporting the infrastructure and licensing comparisons: restic repository; Open Repair Data Standard; BirdNET source and model documentation; EMHASS repository; IBM quantum communication explanation; NASA OLTARIS and radiation analysis pages. Funding and contact routes are the official pages linked above, checked for this research. No patent search, systematic literature review, clinical validation, organizational endorsement, grant pre-approval, or proof of worldwide originality was performed. The strongest claim today is that the proposed portfolio is testable and the tiny included core passes its local tests.
