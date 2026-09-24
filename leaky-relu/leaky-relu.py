import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    np.where applies a condiitonal to a numpy array.
    """
    x = np.asarray(x,dtype=float)
    a = np.where(x>=0,x,alpha*x)
    return a
   
    
    # Write code here
    