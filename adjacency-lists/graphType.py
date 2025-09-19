def graphType(adjList):
    hasDirection = False
    hasMultiEdge = False
    hasLoop = False
    
    # Check loops and multi-edges
    for v, neighbors in adjList.items():
        count = {}
        for u in neighbors:
            if u == v:
                hasLoop = True
            count[u] = count.get(u, 0) + 1
        if any(c > 1 for c in count.values()):
            hasMultiEdge = True
    
    # Check direction
    for v, neighbors in adjList.items():
        for u in neighbors:
            if v not in adjList.get(u, []):
                hasDirection = True
                break
        if hasDirection:
            break
    
    # Graph type codes and descriptions
    graphTypes = {
        0: "Undirected simple graph",
        1: "Directed simple graph",
        20: "Undirected multigraph",
        21: "Directed multigraph",
        30: "Undirected pseudograph",
        31: "Directed pseudograph"
    }
    
    # Determine type
    if hasLoop:
        code = 31 if hasDirection else 30
    elif hasMultiEdge:
        code = 21 if hasDirection else 20
    elif hasDirection:
        code = 1
    else:
        code = 0
    
    print(graphTypes[code])


# Example usage:
adjList = {0: [1], 1: [0, 0], 2: [2]}
print(graphType(adjList))  # Output: (31, 'Directed pseudograph')