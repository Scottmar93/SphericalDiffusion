from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

###################
# this is for a constant current application:

def current(t, j0):
    """Calculate the input current.

    Parameters
    ----------
    t : float or array_like
        Times at which input current is to be calculated.
    j0 : int or float
        Size of the current.

    Returns
    -------
    array_like
        The input current.

    """
    # Return a np array with the same shape as t
    return j0*np.ones_like(t)


def diffusion_spherical_FV(c, t, r, D, j0):
    """
    This function finds the right hand side of dcdt. It takes as inputs the parameters a time and parameters
    :param u:
    :param t:
    :param grid:
    :param D:
    :param j:
    :return:
    """
    dr = r[1]-r[0]

    j = current(t, j0)
    q = - D*r[1:-1] ** 2. * (c[1:] - c[0:-1]) / dr
    q_surf = -j
    q = np.append(0, q)
    q = np.append(q, q_surf)

    dcdt_out = - (2. / (r[1:] + r[0:-1])) ** 2. \
             * (q[1:] - q[0:-1]) / dr
    return dcdt_out


def spherical_solver(j, r, t, params):
    R, c_max, c0, j0, D = params
    return odeint(diffusion_spherical_FV, c0*np.ones(np.size(r) - 1), t, args=(r, D, j0))


# Set up grid
R = 10*10**(-6)
Nr = 100
r = np.linspace(0., R, Nr)

# Set up time
tmax = 100
tsteps = 100
t = np.linspace(0, tmax, tsteps)

# Parameters
c_max = 12000
c0 = 9500
j0 = 9.5*10**(-6)
D = 10**(-14)

c = spherical_solver(current, r, t, [R, c_max, c0, j0, D])

for i in range(1, np.size(t)):
    plt.clf()
    plt.plot(r[:-1], c[i, :])
    plt.pause(0.1)
################

