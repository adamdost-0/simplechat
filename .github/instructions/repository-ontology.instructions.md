---
applyTo: '**'
---

# Repository ontology guidance

Use `docs/_data/repository_ontology.yml` as the authoritative architecture map for change planning in this repository.

- Identify the owning component before editing code, tests, or deployment assets.
- Trace both upstream dependencies and downstream dependents before introducing new modules or moving logic across subsystems.
- Treat auth, settings, retrieval, document ingestion, workspace access, and deployment as cross-cutting boundaries that can affect multiple components.
- If a change spans more than one component, update the ontology entry and the relevant documentation rather than leaving ownership ambiguous.
- Prefer preserving existing component boundaries over creating a new parallel module unless the architecture clearly warrants it.
