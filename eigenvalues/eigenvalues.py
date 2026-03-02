import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    num_rows = len(matrix)
    if all(isinstance(row, list) and len(row) == num_rows for row in matrix) and num_rows > 0:
        matrix = np.array(matrix)
        res = np.linalg.eigvals(matrix)
        real_parts = res.real
        imag_parts = res.imag
        res = res[np.lexsort((real_parts, imag_parts))]
        return res
    else:
        return None

matrix=[[1, 2, 3], [4, 5]]
print(calculate_eigenvalues(matrix))