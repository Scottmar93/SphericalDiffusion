import numpy as np

def current(t, j0, current_type='step'):
    """Calculate the input current.

    Parameters
    ----------
    t : float or array_like
        Times at which input current is to be calculated.
    j0 : int or float
        Size of the current.
    current_type : string, optional
        Type of current wanted (step or constant)

    Returns
    -------
    array_like
        The input current.

    """
    if current_type == 'step':
        if t < 1800:
            j = j0
        elif t < 5400:
            j = 0
        else:
            j = -j0

        return j
    elif current_type == 'constant':
        return j0
