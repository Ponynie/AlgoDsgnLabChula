import numpy as np
import pandas as pd
from collections import deque
import itertools

class Graph():
    
    #?class-default-method----------------------------------------------------------------
    def __init__(self, matrix: np.ndarray):
        if isinstance(matrix, np.ndarray): 
            self.matrix = matrix
        else:
            self.matrix = np.array(matrix)
            
        if np.array_equal(self.matrix, self.matrix.T):
            self.undirected = True
        else:
            self.undirected = False
            
        self.size = self.matrix.shape[0]
        
    @classmethod
    def read_matrix(cls, file_path: str):
        matrix = []
        with open(file_path, 'r') as file:
            for line in file:
                row = list(map(int, line.strip().split()))
                matrix.append(row)
        return cls(matrix)
        
    def __str__(self):
        data = pd.DataFrame(self.matrix, index = ["V" + str(i) for i in range(self.size)], columns = ["V" + str(i) for i in range(self.size)])
        return "Adjacency Matrix of the graph:\n" + data.to_string() + "\n" + f"Undirected: {self.undirected}"
    
    def __len__(self):
        return self.size
    
    #?utility-method-------------------------------------------------------------------------
    def _vertices_adjacent_to(self, vertex: int) -> list: #*HELPLER (P1)
        return [i for i in range(self.size) if self.matrix[vertex][i] != 0] #return a list of vertices adjacent to the given vertex
    
    def _path_exist(self, path: tuple) -> bool: #*HEPLER (P2)
        for i in range(len(path)-1): #for each pair of vertices in the path
            if self.matrix[path[i]][path[i+1]] == 0:  #if there is no edge between the pair of vertices
                return False 
        return True 
            
    #?recursive-hepler-method----------------------------------------------------------------
    def _print_paths_RCS(self, current: int, dest: int) -> None: #*RECURSIVE HEPLER (P1)
        self.path.append(current) #add current vertex to the path
        self.was_visited[current] = True #mark current vertex as visited
        if current == dest: #if current vertex is the destination vertex
            print(f"{tuple(self.path)}")
            self.paths_count += 1 
            self.path.pop()
            self.was_visited[current] = False
            return #return to the previous call
        
        for vertex in self._vertices_adjacent_to(current): #for each vertex adjacent to current vertex
            if not self.was_visited[vertex]: #if the vertex has not been visited
                self._print_paths_RCS(vertex, dest) #recursively call the method
        
        self.path.pop() #remove current vertex from the path
        self.was_visited[current] = False #mark current vertex as unvisited
        return #return to the previous call
        
    def _print_hamilton_paths_RCS(self, current: int) -> None:
        self.path.append(current)
        self.was_visited[current] = True
        if len(self.path) == self.size:
            print(f"{tuple(self.path)}")
            self.paths_count += 1
            self.path.pop()
            self.was_visited[current] = False
            return
        
        for vertex in self._vertices_adjacent_to(current):
            if not self.was_visited[vertex]:
                self._print_hamilton_paths_RCS(vertex)
                
        self.path.pop()
        self.was_visited[current] = False
        return
        
    #?main-method----------------------------------------------------------------------------
    def print_paths_DFS(self, source: int, dest: int) -> None: #O((n-2)!)
        print(f"All paths from V{source} to V{dest} using Depth-first-search method: ")
        if source == dest:
            print(f"0 paths, already in V{source}")
            return
        was_visited = np.zeros(self.size, dtype = bool)
        paths_count = 0
        path = deque()
        stack = deque()
        stack.append(source)
        while len(stack) > 0:
            current_vertex = stack[-1]
            if not was_visited[current_vertex]: 
                path.append(current_vertex)
                was_visited[current_vertex] = True
                if current_vertex == dest: 
                    print(f"{tuple(path)}")
                    paths_count += 1
                    stack.pop()
                    path.pop()
                    was_visited[current_vertex] = False
                else:
                    neighbors_count = 0
                    for vertex in self._vertices_adjacent_to(current_vertex):
                        if not was_visited[vertex]: 
                            stack.append(vertex)
                            neighbors_count  += 1
                    if neighbors_count == 0:
                        stack.pop()
                        path.pop()
                        was_visited[current_vertex] = False  
            else:
                stack.pop()
                path.pop()
                was_visited[current_vertex] = False
        if paths_count == 0: 
            print("No possible paths")
        else: 
            print(f"{paths_count} paths")
    
    def print_paths_RCS(self, source: int, dest: int) -> None: #O((n-2)!) #*MAIN (P1)
        print(f"All paths from V{source} to V{dest} using Recursive method: ")
        if source == dest:
            print(f"0 paths, already in V{source}")
            return
        self.was_visited = np.zeros(self.size, dtype = bool) #boolean array to check if a vertex has been visited [False, False, ...]
        self.paths_count = 0
        self.path = deque() #use stack to track the path
        self._print_paths_RCS(source, dest)
        if self.paths_count == 0: 
            print("No possible paths")
        else: 
            print(f"{self.paths_count} paths")
        del self.was_visited; del self.paths_count; del self.path
        
    def print_hamiltons(self) -> None: #O(n*n!) #*MAIN (P2)
        print(f"All Hamiltonian paths/cycle: ")
        paths_count = 0
        cycle_count = 0
        possible_hamilton_paths = itertools.permutations(range(self.size)) #all possible permutations of vertices [(1, 2, 0), (2, 1, 0), ...]
        for path in possible_hamilton_paths: 
            if self._path_exist(path):
                if path[0] in self._vertices_adjacent_to(path[-1]) or  path[-1] in self._vertices_adjacent_to(path[0]):
                    print(f"Cycle: {path}")
                    cycle_count += 1
                else:
                    print(f"Path: {path}")
                    print(f"Suggested edge to complete the cycle: ({path[0]}, {path[-1]})")
                    paths_count += 1
        if paths_count == 0: 
            print("No Hamiltonian paths exist in the graph")
        else: 
            print(f"{paths_count} Hamiltonian paths")
            
        if cycle_count == 0:
            print("No Hamiltonian cycle exist in the graph")
        else:
            print(f"{cycle_count} Hamiltonian cycle")
            
    def print_hamilton_paths_RCS(self) -> None: #O(n*n!):
        
        print(f"All Hamiltonian paths: ")
        self.paths_count = 0
        self.was_visited = np.zeros(self.size, dtype = bool) #boolean array to check if a vertex has been visited [False, False, ...]
        self.path = deque()
        
        for start_vertex in range(self.size):
            self._print_hamilton_paths_RCS(start_vertex)
            
        if self.paths_count == 0: 
            print("No possible paths")
        else: 
            print(f"{self.paths_count} paths")
        del self.was_visited; del self.paths_count; del self.path
        
        