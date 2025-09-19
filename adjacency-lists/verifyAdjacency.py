def verifyAdjacency(list, originVertex, destinationVertex):
    validation = False
    if isDirected(list):
        if destinationVertex in list.get(originVertex):
            validation = True
    else:
        if originVertex in list.get(destinationVertex) and destinationVertex in list.get(originVertex):
            validation = True
            
    print(validation)
    
def isDirected(list):
    for u in list:
        for v in list[u]:
            if u not in list.get(v):
                return True
    return False

verifyAdjacency({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}, 0, 3)
