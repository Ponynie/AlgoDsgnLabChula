from graph import Graph
import os
import timeit
import matplotlib.pyplot as plt

#?MAIN-PROGRAM----------------------------------------------------------------------
def run(file_path: str):
    print("------------------------------------------------------------------")
    graph = Graph.read_matrix(file_path)
    print(graph)
    #graph.print_paths_RCS(0,5)
    graph.print_hamiltons()
    print("------------------------------------------------------------------")
#?For-execution-time----------------------------------------------------------------
path = "lab2/test_case/Regular"
time_run = []
test_files = sorted(os.listdir(path))[:-1]
for test_file in test_files:
    file_path = f"{path}/{test_file}"
    print("Running", test_file, "...")
    time_run.append(timeit.timeit("run(file_path)", globals=globals(), number=1))
    
x_axis = [i + 1 for i in range(len(test_files))]
fig, ax = plt.subplots()
ax.plot(x_axis, time_run, color = "green", marker = "o")
ax.set_title("Find Path Execution Time")
ax.set_xlabel("Input Sequences")
ax.set_ylabel("Execution Time")
plt.show()