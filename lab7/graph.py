import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
class Lab7graph():
    
    def __init__(self, matrix: np.ndarray):
        if isinstance(matrix, np.ndarray): 
            self.matrix = matrix
        else:
            self.matrix = np.array(matrix)         
        self.size = self.matrix.shape[0]
        self.floyd_warshall()
    
    
    #!This method is for graph in lab7 specifically (USE ONLY FOR LAB6)
    @classmethod
    def construct_graph(cls, num_vertex: int, edge_array: list):
        matrix = np.full((num_vertex, num_vertex), np.inf)
        np.fill_diagonal(matrix, 0)
        for edge in edge_array:
            matrix[edge[0]-1][edge[1]-1] = edge[2]
            matrix[edge[1]-1][edge[0]-1] = edge[2]
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
         
    def floyd_warshall(self):
        dist = self.matrix.copy()
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        self.dist = dist