import timeit
import matplotlib.pyplot as plt
from math import sqrt

def FindGCD1(m, n):
    t = min(m, n)
    while True:
        if m % t == 0 and n % t == 0:
            return t
        t = t - 1

def FindGCD2(m, n):
    m_factor = _prime_factorization(m)
    n_factor = _prime_factorization(n)
    common_factor = m_factor.intersection(n_factor)
    product = 1
    for i in common_factor:
        product *= i
    return product

def FindGCD3(m, n):
    if m > n:
        return FindGCD3(m - n, n)
    elif m < n:
        return FindGCD3(m, n - m)
    else:
        return m 

def _prime_factorization(n):
    factor = set()
    for i in range(2, n + 1):
        if n % i == 0: 
            factor.add(i)
    for i in list(factor):
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                factor.remove(i)
                break
    return factor

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