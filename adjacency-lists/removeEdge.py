def removeEdge(list,originVertex,destinationVertex):
    if isDirected(list):
        list[originVertex].remove(destinationVertex)
        list[originVertex].sort()
    else:
        list[originVertex].remove(destinationVertex)
        list[originVertex].sort()
        list[destinationVertex].remove(originVertex)
        list[destinationVertex].sort()
    print(list)
    
def isDirected(list):
    for u in list:
        for v in list[u]:
            if u not in list.get(v):
                return True
    return False


removeEdge({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]}, 0, 2)