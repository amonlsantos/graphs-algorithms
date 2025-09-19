def calcGraphDensityByList(list):
    nVertex = len(list);
    counterEdges = 0
    for i in list:
        counterEdges += len(list[i])
             
    if isDirected(list):
        density = counterEdges/(nVertex*(nVertex-1))
    else:
        nEdges = counterEdges/2
        density = (2*nEdges)/(nVertex*(nVertex-1))

    print(f'{density:.3f}')

def isDirected(list):
    for u in list:
        for v in list[u]:
            if u not in list.get(v):
                return True
    return False
calcGraphDensityByList({0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]})