from current import current

import numpy as np

def diffusion_spherical_FV(c, t, r, R, D, j0):
    """
    This function calculates a finite volume discretisation of the spherically symmetric diffusion equation using a
    fixed mesh. It takes as inputs the parameters a time and parameters

    Parameters
    ----------
    c: array_like
        Array of concentration in each volume.
    t: float
        Time.
    r: array_like
        Radial mesh.
    D: float
        Diffusion coefficient
    j0: float
        Magnitude of applied current

    Returns
    -------
    array_like
        The finite volume discretisation of dc/dt

    """

    # Compute spacing
    dr = r[1]-r[0]

    # Evaluate j
    j = current(t, j0)

    # Set maximum concentration

    # Compute fluxes
    q = - D*r[1:-1] ** 2. * (c[1:] - c[0:-1]) / dr
    q_surf = -j*R**2

    # Append boundary conditions
    q = np.append(0, q)
    q = np.append(q, q_surf)

    # Compute discretised dc/dt
    dcdt_out = - (2. / (r[1:] + r[0:-1])) ** 2. \
             * (q[1:] - q[0:-1]) / dr

    return dcdt_out
