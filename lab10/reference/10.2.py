from collections import defaultdict 

class Graph:
 
    def __init__(self, vertices):
         
        # No. of vertices
        self.V = vertices 
         
        # Default dictionary to store graph
        self.graph = defaultdict(list) 
 
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # The function to print vertex cover 
    def printVertexCover(self):
        K = 0
        # Initialize all vertices as not visited. 
        visited = [False] * (self.V)
         
        # Consider all edges one by one 
        for u in range(self.V):
             
            # An edge is only picked when 
            # both visited[u] and visited[v] 
            # are false
            if not visited[u]:
                 
                # Go through all adjacents of u and 
                # pick the first not yet visited 
                # vertex (We are basically picking
                # an edge (u, v) from remaining edges. 
                for v in self.graph[u]:
                    if not visited[v]:
                         
                        # Add the vertices (u, v) to the
                        # result set. We make the vertex
                        # u and v visited so that all 
                        # edges from/to them would 
                        # be ignored 
                        visited[v] = True
                        visited[u] = True
                        break
        # Print the vertex cover 
        for j in range(self.V):
            if visited[j]:
                print(j+1, end = ' ')
                K = K+1
        print()
        print(K)
        

file = open("2.4.txt","r")
inputData = file.readline().split()
length = len(inputData)
g = Graph(length)
adjacencyMatrix = [[0 for col in range(length)] for row in range(length)]
for i in range(length):
    for j in range(length):
        adjacencyMatrix[i][j] = int(inputData[j])
    inputData = file.readline().split()
for i in range(length):
    for j in range(length):
        if adjacencyMatrix[i][j] == 1:
            g.addEdge(i,j)
g.printVertexCover()
file.close()


 
