global visited
visited = list()

def DFS(graphDict, vertexIndex):
    visited.append(vertexIndex)
    
    for vertex in graphDict[vertexIndex]:
        if vertex not in visited:
            DFS(graphDict,vertex)
    
    if len(visited) == len(graphDict):
        print(visited)
        quit()
        
        
DFS({0: [1, 2, 6], 1: [0, 3, 4], 2: [0, 6, 7], 3: [1, 4, 5], 4: [1, 3, 5], 5: [3, 4], 6: [0, 2, 7], 7: [2, 6]}, 0)