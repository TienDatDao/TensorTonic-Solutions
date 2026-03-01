import numpy as np

def vector_norm_3d(v):
    
    v = np.asarray(v)
    if(v.ndim == 1):
        v = v[np.newaxis, : ]
    ans = np.sqrt(np.sum(v**2, axis = 1))
    if(len(ans) == 1):
        return ans[0]
    return ans