import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    X = np.asarray(x,dtype=float)
    y = np.asarray(y,dtype=float)
    return float(np.dot(X,y))
    # Write code here
    pass