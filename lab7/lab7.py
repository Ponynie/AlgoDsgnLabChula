from graph import Lab7graph as Graph

def lab7():
    
    def main():
        with open("lab7/test_case/7.1.txt", "r") as f:
            lines = f.readlines()
            num_vertex, num_edge, num_query = [int(i) for i in lines[0].strip().split()]
            edge_array = [tuple(map(int, line.strip().split())) for line in lines[1:num_edge+1]]
            query_array = [tuple(map(int, line.strip().split())) for line in lines[num_edge+1:]]
            graph_obj = Graph.construct_graph(num_vertex, edge_array)
            for query in query_array:
                print(graph_obj.get_edge(*query))


                
    main()
    
lab7()