# Current Work

RADAR — Qompass AI Risk Analysis Diagnostic Assessment Resolver: a
Flask + Vue application for NIST-framework AI risk assessment
(task engine, REST API, pluggable metrics/tasks; XML assessment data
under `nist/`).

## Status

- Python unit suite verified 2026-10-11: 675/675 pass via
  `PYTHONPATH=src python3 -m pytest tests/unit` (3 files gated on
  optional deps — injector, mlflow — collect under the tox venv
  route instead). Canonical runner: `tox -e py311-pytest`.
- Frontend type-check (vue-tsc) clean 2026-10-11.
- `index.scip` is a generated, gitignored artifact at the repo root
  (regen: `npx @sourcegraph/scip-python index`).

## Standing rules

- License files: LICENSE-QCDA is the repo's license (see repo root);
  do not normalize without Matt's direction.
- Code changes are pushed only under Matt's explicit direction
  (the 2026-10-11 overnight campaign authorization covered this pass).
