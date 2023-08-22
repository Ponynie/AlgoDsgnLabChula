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
        
    def __str__(self):
        data = pd.DataFrame(self.matrix, index = ["V" + str(i) for i in range(self.size)], columns = ["V" + str(i) for i in range(self.size)])
        return data.to_string() + "\n" + f"Undirected: {self.undirected}"
    
    def __len__(self):
        return self.size
    
    #?helper-method--------------------------------------------------------------------------
    def _vertices_adjacent_to(self, vertex: int) -> list:
        if not self.undirected:
            return [i for i in range(self.size) if self.matrix[vertex][i] != 0]
        else:
            return [i for i in range(vertex + 1, self.size) if self.matrix[vertex][i] != 0]
        
    #?main-method----------------------------------------------------------------------------
    def find_all_path(self, source: int, dest: int) -> list:
        all_paths = []
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
                    all_paths.append(path)
                    was_visited[current_vertex] = False
                    stack.pop()
                    path.pop()
                elif len(adjacent_vertices) == 0:
                    stack.pop()
                    path.pop()
                    was_visited[current_vertex] = False
                else:
                    for vertex in adjacent_vertices:
                        if not was_visited[vertex]: 
                            stack.append(vertex)
            else:
                stack.pop()
                path.pop()
                was_visited[current_vertex] = False


g = Graph([[1,0,1,0],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
print(g)
#print(g.vertices_adjacent_to(1))
