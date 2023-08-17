deprecated

input_list = [(5, 7), (7, 10), (10, 20)]
time_list_I = []
time_list_II = []
time_list_III = []

for input in input_list:
    execution_time_I = timeit.timeit("FindGCD1(input[0], input[1])", globals=globals(), number=1)
    execution_time_II = timeit.timeit("FindGCD2(input[0], input[1])", globals=globals(), number=1)
    execution_time_III = timeit.timeit("FindGCD3(input[0], input[1])", globals=globals(), number=1)
    time_list_I.append(execution_time_I)
    time_list_II.append(execution_time_II)
    time_list_III.append(execution_time_III)

x_axis = [1,2,3]
fig, ax = plt.subplots()
ax.plot(x_axis, time_list_I, marker = "o", color = "green", label = "GCD1")
ax.plot(x_axis, time_list_II, marker = "o", color = "red", label = "GCD2")
ax.plot(x_axis, time_list_III, marker = "o", color = "blue", label = "GCD3")
ax.set_title("GCD Execution Time")
ax.set_xlabel("Input Value")
ax.set_ylabel("Execution Time ($\\mu$s)")
#ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.7f}'))
ax.grid(True)
ax.legend()
plt.show()