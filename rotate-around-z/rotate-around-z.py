import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    array_dims = np.asarray(points).ndim
    points = np.atleast_2d(np.array(points))
    R_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    res = (R_matrix @ points.T).T
    if array_dims == 1:
        return res[0]
    return res
