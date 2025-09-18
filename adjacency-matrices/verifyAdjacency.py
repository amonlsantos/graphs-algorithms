import numpy as np

def verifyAdjacency(matrix, vI, vJ):
    formatedMatrix = np.array(matrix)
    if formatedMatrix[vI][vJ] != 0 and formatedMatrix[vI][vJ] != None:
        return True
    
    return False
    
print(verifyAdjacency([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 0, 3))