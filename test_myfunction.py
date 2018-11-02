from myfunctions import *
import pytest

# Test
@pytest.mark.skip(reason="not sure how this is supposed to work")
def test_sphericalSolver():
    x0, t0, C = solvers.spherical_solver(j, r, t, params)
    assert temp.max() > 10 and temp.min() < 50
