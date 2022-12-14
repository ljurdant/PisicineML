
import numpy as np

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for loop.
    The three arrays must have compatible shapes.
    Args:
        x: has to be a numpy.array, a matrix of shape m * 1.
        y: has to be a numpy.array, a vector of shape m * 1.
        theta: has to be a numpy.array, a 2 * 1 vector.
    Return:
        The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
        None if x, y, or theta is an empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
    Raises:
        This function should not raise any Exception.
    """
    try:
        np.reshape(x, (max(x.shape), 1))
        np.reshape(y, (max(x.shape), 1))
        np.reshape(theta, (2,1))
    except:
        return None
    else:
        x_prime = np.insert(x,0,1,axis=1)
        
        return 1 / max(x.shape) * np.matmul(x_prime.transpose(),np.matmul(x_prime,theta) - y)