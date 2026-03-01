import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v_arr = np.asarray(v)
    orig_ndim = v_arr.ndim
    v_2d = np.atleast_2d(v_arr)
    norms = np.linalg.norm(v_2d, ord = 2, axis=1, keepdims=True)
    res = np.where(norms != 0, v_2d / norms, 0.)
    if orig_ndim == 1:
        return res[0]
    return res