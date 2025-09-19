def insertEdge(list, originVertex,destinationVertex):
    if isDirected(list):
        list[originVertex].append(destinationVertex)
        list[originVertex].sort()
    else:
        list[originVertex].append(destinationVertex)
        list[originVertex].sort()
        list[destinationVertex].append(originVertex)
        list[destinationVertex].sort()
    print(list)


def isDirected(list):
    for u in list:
        for v in list[u]:
            if u not in list.get(v):
                return True
    return False
insertEdge({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 2)