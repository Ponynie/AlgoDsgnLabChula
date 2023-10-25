import numpy as np
import pandas as pd
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import random
class Graph():
    
    def __init__(self, matrix: np.ndarray):
        if isinstance(matrix, np.ndarray): 
            self.matrix = matrix
        else:
            self.matrix = np.array(matrix)         
        self.size = self.matrix.shape[0]
    
    
    #!This method is for graph in lab6 specifically (USE ONLY FOR LAB6)
    @classmethod
    def construct_graph(cls, num_vertex: int, edge_array: list):
        matrix = np.zeros((num_vertex, num_vertex), dtype = int)
        for edge in edge_array:
            if edge[2] == 1:
                matrix[edge[0]-1][edge[1]-1] = 1
            elif edge[2] == 2:
                matrix[edge[0]-1][edge[1]-1] = 1
                matrix[edge[1]-1][edge[0]-1] = 1
        return cls(matrix)
        
    def __str__(self):
        data = pd.DataFrame(self.matrix, index = ["V" + str(i) for i in range(1, self.size+1)], columns = ["V" + str(i) for i in range(1, self.size+1)])
        return "Adjacency Matrix of the graph:\n" + data.to_string() + "\n"
    
    def __len__(self):
        return self.size
    
    def shown_graph(self):
        G = nx.DiGraph(self.matrix)
        labels = {i: i + 1 for i in G.nodes()}
        pos = nx.spring_layout(G)
        colors = plt.cm.Set3(np.linspace(0, 1, G.number_of_nodes()))
        random.shuffle(colors)
        plt.figure(figsize=(15, 7))
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size = 800, labels = labels)
        nx.draw_networkx_edges(G, pos, edge_color='lightgray')
        plt.show()
    
    def get_edge(self, vertex1: int, vertex2: int) -> int:
        return self.matrix[vertex1-1][vertex2-1]
    
    def vertices_adjacent_to(self, vertex: int) -> list: 
        return [i for i in range(1, self.size+1) if self.get_edge(vertex, i) != 0] #return a list of vertices adjacent to the given vertex
         
    def all_pairs_connected(self) -> int: #return 1 if all pairs of vertices are connected, 0 otherwise
        connected_to_all = [] #list of vertices that are connected to all other vertices
        for vertex in range(1, self.size+1): 
            found = [False] * (self.size+1); found[0] = True
            found[vertex] = True
            queue = deque()
            queue.append(vertex)
            
            flag = False 
            
            while queue and not flag:
                v = queue.popleft()
                for i in self.vertices_adjacent_to(v):
                    if not found[i]:
                        found[i] = True
                        if i in connected_to_all:
                            connected_to_all.append(vertex)
                            flag = True
                            break
                        queue.append(i)
            if flag == True:
                continue
            elif all(found):
                connected_to_all.append(vertex)
            else:
                return 0
        return 1
    
    def kosaraju(self):
        def dfs_first_pass(node):
            visited[node] = True
            for neighbor in range(self.matrix.shape[0]):
                if not visited[neighbor] and self.matrix[node, neighbor] == 1:
                    dfs_first_pass(neighbor)
            stack.append(node)

        def dfs_second_pass(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in range(self.transposed_matrix.shape[0]):
                if not visited[neighbor] and self.transposed_matrix[node, neighbor] == 1:
                    dfs_second_pass(neighbor, component)

        num_nodes = self.matrix.shape[0]

        visited = [False] * num_nodes
        stack = []
        for node in range(num_nodes):
            if not visited[node]:
                dfs_first_pass(node)

        # Transpose the matrix for the second pass
        self.transposed_matrix = np.transpose(self.matrix)

        visited = [False] * num_nodes
        strongly_connected_components = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                dfs_second_pass(node, component)
                strongly_connected_components.append(component)

        return strongly_connected_components