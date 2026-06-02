def test_legacy_solver_aliases():
    from qihd import MIQPSolver, PhiMIQP
    from qihd.phi_miqp import PhiMIQP as LegacyPhiMIQP

    assert PhiMIQP is MIQPSolver
    assert LegacyPhiMIQP is MIQPSolver
