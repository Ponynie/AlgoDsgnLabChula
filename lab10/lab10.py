from graph import Lab10graph
import numpy as np

def lab10_1(path: str):
    
    def main(path: str):
        #path = "lab10/test_case/test.txt"
        vertexCover_size, matrix = read_input(path)
        graph_obj = Lab10graph(matrix)
        solution = graph_obj.k_vertexCover_bruteforce(vertexCover_size)
        print_output(solution)
        graph_obj.shown_graph()
        
    def read_input(path: str) -> tuple:
        with open(path, 'r') as file:
            vertexCover_size = int(file.readline().strip())
            matrix = [list(map(int, line.strip().split())) for line in file]
        return (vertexCover_size, matrix)
    
    def print_output(solution: tuple) -> None:
        print("-"*50)
        if solution == ():
            print("No")
        else:
            print("Yes")
            for i in solution:
                print(*i)
        print("-"*50)
    
    main(path)

def lab10_2(path: str):
    
    def main(path: str):
        #path = "lab10/test_case/test.txt"
        matrix = read_input(path)
        graph_obj = Lab10graph(matrix)
        solution = graph_obj.min_vertexCover_approximation()
        print_output(solution)
        #print(graph_obj.is_vertexCover(solution))
        #graph_obj.shown_graph()
    
    def read_input(path: str):
        with open(path, 'r') as file:
            matrix = [list(map(int, line.strip().split())) for line in file]
        return matrix
    
    def print_output(solution: tuple) -> None:
        print("-"*50)
        print(*solution)
        print(len(solution))
        print("-"*50)

    main(path)

def lab10_3(path: str):
    
    def main(path: str):
        #path = "lab10/test_case/test.txt"
        num_clause, clause_matrix = read_input(path)
        solution = threeSAT_to_vertexCover(num_clause, clause_matrix)
        print_output(*solution)

    def read_input(path: str):
        with open(path, 'r') as file:
            num_clause = int(file.readline().strip())
            clause_matrix = [list(map(int, line.strip().split())) for line in file]    
        return (num_clause, clause_matrix)
    
    def print_output(num_vertex: int, vertexCover_size: int, graph: Lab10graph, have_solution: bool) -> None:
        print("-"*50)
        print(num_vertex)
        print(vertexCover_size)
        print(graph)
        print(have_solution)
        print("-"*50)
    
    def count_variable(clause_matrix: list) -> int:
        return len(set([abs(i) for clause in clause_matrix for i in clause]))
    
    def threeSAT_to_vertexCover(num_clause: int, clause_matrix: list) -> tuple:
        num_variable = count_variable(clause_matrix)
        num_vertex = 2*num_variable + 3*num_clause
        vertexCover_size = num_variable + 2*num_clause
        
        matrix = np.zeros((num_vertex, num_vertex), dtype = int)
        
        for i in range(0, 2*num_variable, 2):
            matrix[i][i+1] = 1
        for i in range(1, 2*num_variable, 2):
            matrix[i][i-1] = 1  
        
        for i in range(2*num_variable, num_vertex, 3):
            clause_gadget = np.ones((3, 3), dtype = int)
            np.fill_diagonal(clause_gadget, 0)
            matrix[i:i+3, i:i+3] = clause_gadget
        
        j = 0
        for i in range(2*num_variable, num_vertex, 3):
            for k in range(3):
                variable_idx = 2*abs(clause_matrix[j][k]) - 2
                if clause_matrix[j][k] > 0:
                    matrix[variable_idx][i+k] = 1
                    matrix[i+k][variable_idx] = 1
                else:
                    matrix[variable_idx+1][i+k] = 1
                    matrix[i+k][variable_idx+1] = 1
            j += 1
        
        graph_obj = Lab10graph(matrix)
        if graph_obj.k_vertexCover_bruteforce(vertexCover_size) != ():
            have_solution = True
        else :
            have_solution = False
            
        return (num_vertex, vertexCover_size, graph_obj, have_solution)
    
    main(path)
   
for i in range(1,10):    
    lab10_2("lab10/test_case/test.txt")
