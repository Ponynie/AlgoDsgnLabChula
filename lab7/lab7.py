from graph import Lab7graph as Graph

def lab7():
    
    def main():
        with open("lab7/test_case/7_extra2.txt", "r") as f:
            lines = f.readlines()
            num_vertex, num_edge = [int(i) for i in lines[0].strip().split()][0:2]
            edge_array = [tuple(map(int, line.strip().split())) for line in lines[1:num_edge+1]]
            query_array = [tuple(map(int, line.strip().split())) for line in lines[num_edge+1:]]
            graph_obj = Graph.construct_graph(num_vertex, edge_array)
            for query in query_array:
                print("------------------------------------------------------------")
                print(f"{query}: {graph_obj.get_shortest_distance(*query)} {graph_obj.get_shortest_path(*query)}")
                #print(graph_obj)
                print(graph_obj.string_dist())
                print(graph_obj.string_prev())
                print("------------------------------------------------------------")
                
                
    main()
    print("Run successfully")
    
lab7()