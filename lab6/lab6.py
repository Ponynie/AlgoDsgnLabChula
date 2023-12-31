from graph import Lab6graph as Graph

def lab6():
    
    def main():
        with open("lab6/test_case/Extra6.5.txt", "r") as f:
            lines = f.readlines()
            case_start_index = [i for i in range(len(lines)) if len(lines[i].strip().split(" ")) == 2 and lines[i].strip() != "0 0"]
            for i in range(len(case_start_index)):
                num_vertex, num_edge = map(int, lines[case_start_index[i]].strip().split(" "))
                edge_array = [tuple(map(int, e.strip().split(" "))) for e in lines[case_start_index[i]+1:case_start_index[i]+num_edge+1]]
                graph_obj = Graph.construct_graph(num_vertex, edge_array)
                print("------------------------------------")
                print(graph_obj.all_pairs_connected())
                print(graph_obj)
                print(graph_obj.kosaraju())
                graph_obj.shown_graph()
                print("------------------------------------")
                
    main()
    
lab6()