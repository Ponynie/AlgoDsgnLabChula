class Graph:
    # Constructor
    def __init__(self, edges, N):

        # A List of Lists to represent an adjacency list
        self.N = N
        self.edges = edges
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
        

    def printAllPathsUtil(self, u, d, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d: 
            print(path) 
        else: 
            # If current vertex is not destination 
            # Recur for all the vertices adjacent to this vertex 
            for i in self.adjList[u]: 
                if visited[i]== False: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self, s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.N) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d, visited, path) 

def printAllHamiltonianPaths(g, v, visited, path, N):

    # if all the vertices are visited, then hamiltonian path exists
    if len(path) == N:
        # print hamiltonian path
        print(path)
        return

    # Check if every edge starting from vertex v leads to a solution or not
    for w in g.adjList[v]:

        # process only unvisited vertices as hamiltonian
        # path visits each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)

            # check if adding vertex w to the path leads to solution or not
            printAllHamiltonianPaths(g, w, visited, path, N)
            
            # Backtrack
            visited[w] = False
            path.pop()

# main

f = open("lab2/test_case/2.1.1.txt","r")  
N = 0
edges = []
for i in f:
    i = i.strip().split(" ")
    for j in range(len(i)):
        if i[j] != "0":
            edges.append((N,j))
    N+=1
g = Graph(edges, N) # create object g which is Graph class  
# find path(u,v)
s = 0 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.printAllPaths(s, d)

  
print("Hamiltonion path: ")
# find Hamiltonion path
for start in range(N):
    path = [start] # keep the 
    visited = [False] * N
    visited[start] = True
    printAllHamiltonianPaths(g, start, visited, path, N)  

f.close()


 



