# 2026-10-11 — Overnight campaign pass: unit suite verified green, frontend type-check clean, SCIP indexed

Facts established during the overnight completion pass (verified on primo):

- Python unit suite: `PYTHONPATH=src python3 -m pytest tests/unit`
  collects 675 tests and **all 675 pass** (5.1s, system Python 3.14 with
  project deps present). The `src/` prefix matters: without it,
  collection fails with `No module named 'radar'`.
- Three test files are gated on optional deps absent from a bare system
  Python and were excluded from that run: `tests/unit/restapi`
  (`injector` — a declared pyproject dependency, present in the tox
  venv), `tests/unit/pyplugs/test_plugins.py` and
  `tests/unit/task_plugins/radar_builtins/artifacts/test_mlflow.py`
  (`mlflow`). Under the project's tox route (`py311-pytest`) these are
  expected to collect; that route was not run this pass.
- Frontend (`src/frontend`): `npm install` (271 packages) then
  `npm run type-check` (vue-tsc) — clean, no errors. The frontend has
  no test script and no tracked lockfile; neither was changed.
- README documented badges and references but nothing about running
  anything. A Development section was appended with the verified test
  commands above, the frontend type-check, and SCIP regeneration.
- SCIP: `npx @sourcegraph/scip-python index` generated a 6.0 MB
  `index.scip` at the repo root; it is gitignored as a generated
  artifact, not committed.
- `current.md` carried the language-mirror template; refreshed to
  describe RADAR itself.
