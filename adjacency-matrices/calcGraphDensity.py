import numpy as np

def calcDensity(matrix):
    formatedMatrix = np.array(matrix)
    nV = formatedMatrix.shape[0]  # number of vertices
    nE = np.count_nonzero(formatedMatrix)  # number of edges
    density = nE/(nV*(nV - 1))
    print(f'{density:.3f}')

calcDensity([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])