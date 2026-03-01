import numpy as np

def vector_norm_3d(v):
    
    v = np.atleast_2d(v)
    ans = np.linalg.norm(v, ord=2, axis=1)
    if(len(ans) == 1):
        return ans[0]
    return ans