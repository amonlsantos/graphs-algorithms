global sortedVertices 
global verticesStatus
global discoverVertexTime
global endVertexTime
global time


time = 0
verticesStatus = {}
discoverVertexTime = {}
endVertexTime = {}
sortedVertices = []


# vertices status are = unknow, visiting, visited in the same sense of white, gray and black
        
def topologicalSortWithDFS(adjacencyList):
    # initalizing all vertices as unknow
    global graph
    graph = adjacencyList
    
    initializeVerticesStatus()
        
    for vertex in graph:
        if verticesStatus[vertex] == 'unknow':
            dfsVisit(vertex)
            
    print(sortedVertices)
    
    print('Vertex times:')
    for vertex in graph:
        print(f'{vertex}: {discoverVertexTime[vertex]}/{endVertexTime[vertex]}')
        
# initalizing all vertices as unknow
def initializeVerticesStatus():
    for vertex in graph:
        verticesStatus[vertex] = 'unknow'
            
def dfsVisit(vertex):
    verticesStatus[vertex] = 'visiting'
    global time
    time += 1
    discoverVertexTime[vertex] = time
    
    
    for v in graph[vertex]:
        if verticesStatus[v] == 'unknow':
            dfsVisit(v)
    
    verticesStatus[vertex] = 'visited'
    time += 1
    endVertexTime[vertex] = time
    sortedVertices.insert(0,vertex)
    
topologicalSortWithDFS({0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]})