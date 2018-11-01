from myfunctions import *


# Test
def test_sphericalSolver():
    x0, t0, C = spherical_Solver(j, r, t, params)
    assert temp.max() > 10 and temp.min() < 50
