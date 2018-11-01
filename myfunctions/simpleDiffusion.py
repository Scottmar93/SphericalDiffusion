from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#### Note that c exceeds c_max

def current(t, j0):
    """Calculate the input current.

    Parameters
    ----------
    t: float
        Time at which input current is to be calculated.
    j0: int or float
        Size of the current.

    Returns
    -------
    float
        The input current.

    """
    if t < 1800:
        j = j0
    elif t < 5400:
        j = 0
    else:
        j = -j0

    return j


def diffusion_spherical_FV(c, t, r, D, j0):
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

    c = odeint(diffusion_spherical_FV, c0*np.ones(np.size(r) - 1), t, args=(r, D, j0))
    return c


# Set up grid
R = 10*10**(-6)
Nr = 100
r = np.linspace(0., R, Nr)

# Set up time
tmax = 7200
tsteps = 100
t = np.linspace(0, tmax, tsteps)

# Parameters
c_max = 12000
c0 = 9500
j0 = 9.5*10**(-6)
D = 10**(-14)

# Call solver
c = spherical_solver(r, t, [R, c_max, c0, j0, D])

# Plot at each timestep
for i in range(1, np.size(t)):
    plt.clf()
    plt.plot(r[:-1]/R, c[i, :]/c_max)
    plt.ylim([0.5, 1.5])
    plt.xlabel('r/R')
    plt.ylabel('c/c_max')
    plt.title('Time = {} seconds'.format(t[i]))
    plt.pause(1)

