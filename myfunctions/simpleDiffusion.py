from scipy.integrate import ode
from numpy import *
import matplotlib.pyplot as plt


###################
# this is for a constant current application:


def dcdt(c, t, r, D, current):
    """
    This function finds the dcdt. It takes as inputs the parameters a time and parameters
    :param u:
    :param t:
    :param grid:
    :param D:
    :param current:
    :return:
    """
    dr = r[1]-r[0]

    q = - D r[1:-1] ** 2. * (c[:, 1:] - c[:, 0:-1]) / dr
    q_surf = -current
    q = np.concatenate([0], q, q_surf)

    dcdt_out = - (2. / (r[1:] + r[0:-1])) ** 2. \
             * (qn[:, 1:] - qn[:, 0:-1]) / dr
    return dcdt_out


# Set up grid
r = np.linspace(0, 1, 100)  # neg, sep, pos, particle, grid

# Initial conditions
c0 = ones(size(r))  # neg, pos, electrolyte, grid

# Solve ODEs
t = np.linspace(0, tmax, tsteps)
c = odeint(dcdt, c0, t, args=(r, D, current))


################

