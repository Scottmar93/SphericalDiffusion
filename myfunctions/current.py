import numpy as np

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
