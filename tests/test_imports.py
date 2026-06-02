def test_public_imports():
    from qihd import MIQP, MIQPSolver, PDQP, PhiMIQP, QIHD

    assert MIQP is not None
    assert MIQPSolver is not None
    assert PhiMIQP is MIQPSolver
    assert QIHD is not None
    assert PDQP is not None
