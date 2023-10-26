import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
class Lab7graph():
    
    def __init__(self, matrix: np.ndarray, dist: np.ndarray = None, prev: np.ndarray = None, tran: np.ndarray = None):
        if isinstance(matrix, np.ndarray): 
            self.matrix = matrix
        else:
            self.matrix = np.array(matrix) 
        self.dist = dist
        self.prev = prev   
        self.tran = tran
        self.size = self.matrix.shape[0]
        self.floyd_warshall_filled()
    
    
    #!This method is for graph in lab7 specifically (USE ONLY FOR LAB7)
    @classmethod
    def construct_graph(cls, num_vertex: int, edge_array: list):
        matrix = np.full((num_vertex, num_vertex), np.inf)
        prev = np.full((num_vertex, num_vertex), np.nan)
        tran = np.zeros((num_vertex, num_vertex))
        for edge in edge_array:
            matrix[edge[0]-1][edge[1]-1] = edge[2]
            matrix[edge[1]-1][edge[0]-1] = edge[2]
            prev[edge[0]-1][edge[1]-1] = edge[0]
            prev[edge[1]-1][edge[0]-1] = edge[1]
            tran[edge[0]-1][edge[1]-1] = 1
            tran[edge[1]-1][edge[0]-1] = 1
        np.fill_diagonal(matrix, 0)
        np.fill_diagonal(prev, np.nan)
        np.fill_diagonal(tran, 1)
        dist = matrix.copy()
        return cls(matrix, dist, prev, tran)
        
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
         
    def floyd_warshall_filled(self):
        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.prev[i][j] = self.prev[k][j]
        
    def get_shortest_path(self, vertex1: int, vertex2: int) -> list:
        if self.prev[vertex1-1][vertex2-1] == np.nan:
            return "no path"
        path = [vertex2]
        while vertex1 != vertex2:
            vertex2 = int(self.prev[vertex1-1][vertex2-1])
            path.append(vertex2)
        return path[::-1]
    
    def get_shortest_distance(self, vertex1: int, vertex2: int) -> int:
        return self.dist[vertex1-1][vertex2-1]
    
    def get_max_decibel_from_shortest_path(self, vertex1: int, vertex2: int) -> int:
        path = self.get_shortest_path(vertex1, vertex2)
        if path == "no path":
            return "no path"
        return max([self.get_edge(path[i], path[i+1]) for i in range(len(path)-1)])