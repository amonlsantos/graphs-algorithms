import numpy as np
def createAdjacencyList(matrix):
    nRows, nColumns = np.shape(matrix)
    adjacencList = {}
    
    for i in range(0,nRows):
        auxList = []
        for j in range(0,nColumns):
            if matrix[i][j] != 0:
                    auxList.extend([j]*matrix[i][j])
        adjacencList[i] = auxList

    print(adjacencList)
createAdjacencyList([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
