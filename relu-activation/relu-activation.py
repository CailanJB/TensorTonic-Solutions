import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    relu is used as an activaton in a nuerla network that shus a neuron on or off.
    after the matric multiplication is computd wiht the weights and the vector/matric it is passed into an activation fuction that activates the weight if its psoitive which gives us th enon linear shape
    """
    x = np.asarray(x,dtype=float)
    relu = np.maximum(0.0,x)
    return np.array(relu)
    # Write code here
    