import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    v = np.asarray(v)
    w = np.asarray(w)
    v_norm = np.linalg.norm(v, ord = 2)
    w_norm = np.linalg.norm(w, ord = 2)
    cos_theta = np.dot(v,w.T)/(v_norm*w_norm)
    return np.arccos(cos_theta)
