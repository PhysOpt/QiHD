# Migrating from OpenPhiSolve to QiHD

QiHD is the successor to OpenPhiSolve. It keeps the same core solver pipeline while moving the project to a clearer package namespace and public API.

## What changed

| OpenPhiSolve | QiHD |
| --- | --- |
| `phisolve` package namespace | `qihd` package namespace |
| `PhiMIQP` primary solver name | `MIQPSolver` primary solver name |
| `OpenPhiSolve` project identity | `QiHD` project identity |

## Import updates

Update imports from `phisolve` to `qihd`.

```python
# OpenPhiSolve
from phisolve import PhiMIQP, MIQP, QIHD, PDQP
```

```python
# QiHD
from qihd import MIQPSolver, MIQP, QIHD, PDQP
```

## Solver name update

`PhiMIQP` has been renamed to `MIQPSolver` because the class orchestrates the full solve pipeline:

- problem compilation
- QIHD sample generation
- optional classical refinement
- response construction

```python
# OpenPhiSolve
model = PhiMIQP(problem, backend, refiner)
result = model.solve()
```

```python
# QiHD
solver = MIQPSolver(problem, backend, refiner)
result = solver.solve()
```

## Compatibility

The old `PhiMIQP` name remains available as a compatibility alias during the migration window:

```python
from qihd import PhiMIQP
```

The old module path also remains available:

```python
from qihd.phi_miqp import PhiMIQP
```

Deprecation warnings may be added in a later release after downstream users have had time to migrate.

## Package installation

The package name is now `qihd`.

```bash
pip install qihd
```

For local development:

```bash
pip install -e .
```

## Provenance

QiHD is derived from OpenPhiSolve, originally developed by Artephi Computing. See `NOTICE` and `LICENSE` for attribution and license details.
