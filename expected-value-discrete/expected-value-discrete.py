import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x)
    p = np.asarray(p)
    
    if np.abs(np.sum(p) - 1) > 10**(-6):
        raise ValueError("ValueError")
    return (x @ p.T)
