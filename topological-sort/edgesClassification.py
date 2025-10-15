global edgesType 
global verticesStatus
global discoverVertexTime
global endVertexTime
global time


time = 0
verticesStatus = {}
discoverVertexTime = {}
endVertexTime = {}
edgesType = {}


# vertices status are = unknow, visiting, visited in the same sense of white, gray and black
        
def edgesClassification(adjacencyList):
    # initalizing all vertices as unknow
    global graph
    graph = adjacencyList
    
    
    initializeVerticesStatus()
        
    for vertex in graph:
        if verticesStatus[vertex] == 'unknow':
            dfsVisit(vertex)
            
    print(edgesType)
    
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
            edgesType[f'{vertex}-{v}'] = 'tree'
            dfsVisit(v)
            
        elif verticesStatus[v] == 'visiting':
            edgesType[f'{vertex}-{v}'] = 'back'
            
        else:
            
           if  discoverVertexTime[vertex] < discoverVertexTime[v]:
                edgesType[f'{vertex}-{v}'] = 'forward'
                
           else:
               edgesType[f'{vertex}-{v}'] = 'cross'
    
    verticesStatus[vertex] = 'visited'
    time += 1
    endVertexTime[vertex] = time
    
edgesClassification({
    0: [1, 3],
    1: [4],
    2: [5],
    3: [4],
    4: [3],
    5: [5] 
})