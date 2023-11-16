import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations

class Lab10graph():
    
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
        self.list = [[j for j in range(1, self.size+1) if self.get_edge(i, j) != 0] for i in range(1, self.size+1)]
    
    #!This method is for graph in lab10 specifically (USE ONLY FOR LAB10)
    def shown_graph(self):
        if self.undirected:
            G = nx.Graph(self.matrix)
        else:
            G = nx.DiGraph(self.matrix)
        labels = {i: i + 1 for i in G.nodes()}
        pos = nx.spring_layout(G)
        colors = plt.cm.Set3(np.linspace(0, 1, G.number_of_nodes()))
        random.shuffle(colors)
        plt.figure(figsize=(8, 7))
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size = 800, labels = labels)
        nx.draw_networkx_edges(G, pos, edge_color='lightgray')
        plt.show()
    
    def get_edge(self, vertex1: int, vertex2: int) -> int:
        return self.matrix[vertex1-1][vertex2-1]
    
    def vertices_adjacent_to(self, vertex: int) -> list: 
        return self.list[vertex-1] if self.list[vertex-1] != [] else None
    
    def __str__(self):
        data = pd.DataFrame(self.matrix, index = ["V" + str(i) for i in range(1, self.size+1)], columns = ["V" + str(i) for i in range(1, self.size+1)])
        return "Adjacency Matrix of the graph:\n" + data.to_string() + "\n"
    
    def __len__(self):
        return self.size

    def is_vertexCover(self, set_to_test: tuple) -> bool:
        for i in range(1, self.size+1):
            if self.vertices_adjacent_to(i) != None and i not in set_to_test:
                for j in self.vertices_adjacent_to(i):
                    if j not in set_to_test:
                        return False
        return True
             
    def k_vertexCover_bruteforce(self, size_to_find: int) -> tuple:
        result = []
        k_element_subsets = list((combinations(range(1, self.size+1), size_to_find)))
        for subset in k_element_subsets:
            if self.is_vertexCover(subset):
                result.append(subset)
        return tuple(result)

    
    def min_vertexCover_approximation(self) -> tuple:
        result = set()
        set_of_edges = set()
        for i in range(1, self.size+1):
            for j in range(i+1, self.size+1):
                if self.get_edge(i, j) != 0:
                    set_of_edges.add(frozenset({i, j}))
                    
        while set_of_edges != set():
            edge = set_of_edges.pop()
            result.update(edge)
            set_of_edges -= {i for i in set_of_edges if edge.intersection(i) != set()}
    
        return tuple(result)