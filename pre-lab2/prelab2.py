import numpy as np
import pandas as pd

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
    def vertices_adjacent_to(self, vertex):
        if not self.undirected:
            return [i for i in range(self.size) if self.matrix[vertex][i] != 0]
        else:
            return [i for i in range(vertex + 1, self.size) if self.matrix[vertex][i] != 0]
        
    #?main-method----------------------------------------------------------------------------
    

g = Graph([[1,0,1,0],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
print(g)
print(g.vertices_adjacent_to(1))
