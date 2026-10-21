import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    manhattan_distance = np.sum(np.abs(x-y))
    return manhattan_distance
    # Write code here
    pass