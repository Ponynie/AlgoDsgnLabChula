import numpy as np
import pandas as pd
from collections import deque

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
        return data.to_string() + "\n" + f"Undirected: {self.undirected}"
    
    def __len__(self):
        return self.size
    
    #?utility-method-------------------------------------------------------------------------
    def _vertices_adjacent_to(self, vertex: int) -> list:
        if not self.undirected:
            return [i for i in range(self.size) if self.matrix[vertex][i] != 0]
        else:
            return [i for i in range(vertex + 1, self.size) if self.matrix[vertex][i] != 0]
    
    #?recursive-hepler-method----------------------------------------------------------------
    def _print_paths_RCS(self):
        pass
    
    def _print_hamiltonians(self):
        pass
        
    #?main-method----------------------------------------------------------------------------
    def print_paths_DFS(self, source: int, dest: int) -> None:
        was_visited = np.zeros(self.size, dtype = bool)
        path = deque()
        stack = deque()
        stack.append(source)
        while len(stack) > 0:
            current_vertex = stack[-1]
            if not was_visited[current_vertex]: 
                path.append(current_vertex)
                was_visited[current_vertex] = True
                adjacent_vertices = self._vertices_adjacent_to(current_vertex)
                if current_vertex == dest: 
                    print(f"One of the path from V{source} to V{dest} is {tuple(path)}")
                    was_visited[current_vertex] = False
                    stack.pop()
                    path.pop()
                else:
                    neighbors_count = 0
                    for vertex in adjacent_vertices:
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

    def print_paths_RCS(self):
        pass
    
    def print_hamiltonians(self):
        pass
    
    

g = Graph.read_matrix("lab2/test_case/2.1.2.txt")
print(g)
g.print_paths_DFS(0,3)
