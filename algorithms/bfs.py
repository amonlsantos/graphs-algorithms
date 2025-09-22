def BFS(graphDict, nodeIndex):
    analisedNodes = []
    queue = []
    FIRST_POSITION = 0
    queue.append(nodeIndex)
    
    notVisited = list(graphDict.keys())
    notVisited.remove(nodeIndex)
    
    while len(queue) != 0:
        for node in graphDict[queue[FIRST_POSITION]]:           
            
            if node not in queue and node not in analisedNodes:
                queue.append(node)
                notVisited.remove(node)
            
        analisedNodes.append(queue[FIRST_POSITION])
        queue.pop(FIRST_POSITION)
    analisedNodes.extend(notVisited)
        
        
            
    print(analisedNodes)
    
BFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0)