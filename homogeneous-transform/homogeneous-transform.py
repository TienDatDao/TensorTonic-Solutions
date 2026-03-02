import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    points = np.asarray(points)
    dim = points.ndim
    points = np.atleast_2d(points)
    points = np.insert(points, points.shape[1], 1, axis = 1)
    res =  np.dot(T,points.T).T
    res = np.delete(res, 3, axis = 1)
    if dim == 1:
        return res[0]
    return res