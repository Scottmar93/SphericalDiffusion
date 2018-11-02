from derivs import diffusion_spherical_FV

from scipy.integrate import odeint
import numpy as np

def spherical_solver(r, t, params):
    """
        This function uses an ODE solver to integrate the finite volume disretisation provided
        by diffusion_spherical_FV

        Parameters
        ----------
        r: array_like
        Radial mesh.

        t: float
            Time.
        params: list
            List of parameters: radius, R; maximum concentration, c_max; initial concentration, c0;
             flux density, j0; diffusion coefficient, D.

        Returns
        -------
        array_like
            The concentration

        """
    R, c_max, c0, j0, D = params

    c = odeint(diffusion_spherical_FV, c0*np.ones(np.size(r) - 1), t, args=(r, R, D, j0))
    return c
