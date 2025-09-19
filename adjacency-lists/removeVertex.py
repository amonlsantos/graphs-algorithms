def removeVertex(list, vertexToDelete):
    for i in list:
        while vertexToDelete in list.get(i):
            list[i].remove(vertexToDelete)


removeVertex({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 2)