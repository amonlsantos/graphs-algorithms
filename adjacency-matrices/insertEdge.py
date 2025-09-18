import numpy as np

def insertEdge(matrix, v_i, v_j):
    matrix[v_i][v_j] += 1
    matrix[v_j][v_i] += 1
    print(matrix)

insertEdge([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 0, 2)