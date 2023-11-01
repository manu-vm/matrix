import numpy as np

def cofactor(matrix, i, j):
    """Compute the cofactor of the matrix at the given row and column."""
    minor = np.delete(np.delete(matrix, i, 0), j, 1)
    return (-1)**(i + j) * np.linalg.det(minor)

def adjugate(matrix):
    """Compute the adjugate of the matrix."""
    adj = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            adj[j][i] = cofactor(matrix, i, j)  # Transposition is achieved by swapping i and j
    return adj

# Example
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

adj_A = adjugate(A)
print(adj_A)
