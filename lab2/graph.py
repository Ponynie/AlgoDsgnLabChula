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
    def _vertices_adjacent_to(self, vertex: int) -> list:
        return [i for i in range(self.size) if self.matrix[vertex][i] != 0]
    
    def _path_exist(self, path: tuple) -> bool:
        for i in range(len(path)-1):
            if self.matrix[path[i]][path[i+1]] == 0:
                return False
        return True
            
    #?recursive-hepler-method----------------------------------------------------------------
    def _print_paths_RCS(self, current: int, dest: int) -> None:
        self.path.append(current)
        self.was_visited[current] = True
        if current == dest: 
            print(f"{tuple(self.path)}")
            self.paths_count += 1
            self.path.pop()
            self.was_visited[current] = False
            return
        
        for vertex in self._vertices_adjacent_to(current):
            if not self.was_visited[vertex]:
                self._print_paths_RCS(vertex, dest)
        
        self.path.pop()
        self.was_visited[current] = False
        return
        
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
    
    def print_paths_RCS(self, source: int, dest: int) -> None: #O((n-2)!)
        print(f"All paths from V{source} to V{dest} using Recursive method: ")
        if source == dest:
            print(f"0 paths, already in V{source}")
            return
        self.was_visited = np.zeros(self.size, dtype = bool)
        self.paths_count = 0
        self.path = deque()
        self._print_paths_RCS(source, dest)
        if self.paths_count == 0: 
            print("No possible paths")
        else: 
            print(f"{self.paths_count} paths")
        del self.was_visited; del self.paths_count; del self.path
        
    def print_hamilton_paths(self) -> None: #O(n*n!)
        print(f"All Hamiltonian paths: ")
        paths_count = 0
        possible_hamilton_paths = itertools.permutations(range(self.size))
        for path in possible_hamilton_paths:
            if self._path_exist(path): 
                print(path)
                paths_count += 1
                
        if paths_count == 0: 
            print("No Hamiltonian paths exist in the graph")
        else: 
            print(f"{paths_count} Hamiltonian paths")
            
    def print_hamilton_paths_RCS(self) -> None: #O(n*n!):
        print(f"All Hamiltonian paths: ")
        self.paths_count = 0
        self.was_visited = np.zeros(self.size, dtype = bool)
        self.path = deque()
        
        for start_vertex in range(self.size):
            self._print_hamilton_paths_RCS(start_vertex)
            
        if self.paths_count == 0: 
            print("No possible paths")
        else: 
            print(f"{self.paths_count} paths")
        del self.was_visited; del self.paths_count; del self.path