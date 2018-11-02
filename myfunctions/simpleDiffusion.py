from solvers import spherical_solver

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#### Note that c exceeds c_max

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
