import numpy as np

def insertVertex(matrix):
    formatedMatrix = np.array(matrix)
    nRows, nColumns = formatedMatrix.shape
    stack2Add = np.zeros(nRows)

    np.r_[formatedMatrix,[stack2Add]]
    np.c_[formatedMatrix, [stack2Add]]
    print(formatedMatrix)

insertVertex([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])