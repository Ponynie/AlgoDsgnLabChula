import numpy as np
import copy

file_path = "lab4/test_case/4.0.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = sorted(list(map(int, file.readline().strip().split(sep = " "))))

ways_solution = [[None for _ in range(amount + 2)] for _ in range(len(denominations))]
for denomidex in range(len(denominations)):
    ways_solution[denomidex][0] = [[],]

def solution_filled(denomidex: int, amount: int) -> None:
    right_solutions = ways_solution[denomidex][amount - denominations[denomidex]]
    left_solutions = ways_solution[denomidex - 1][amount]
    if right_solutions != None:
        right_solutions = copy.deepcopy(ways_solution[denomidex][amount - denominations[denomidex]])
        for solution in right_solutions: solution.append(denominations[denomidex])
    if  left_solutions != None:
        left_solutions = copy.deepcopy(ways_solution[denomidex - 1][amount]) 
    if right_solutions != None and left_solutions != None:
        ways_solution[denomidex][amount] = right_solutions + left_solutions
    elif right_solutions != None and left_solutions == None:
        ways_solution[denomidex][amount] = right_solutions
    elif right_solutions == None and left_solutions != None:
        ways_solution[denomidex][amount] = left_solutions


#?MAIN---------------------------------------------------------------------------------------------------

def ways_coin_change_topdown(amount: int, denominations: list) -> int:
    ways_value = np.full((len(denominations), amount + 1), None)
    return _ways_coin_change(len(denominations) - 1, amount, denominations, ways_value)

def _ways_coin_change(denomidex: int, amount: int, denominations: list, ways_value: np.array) -> int:
    if amount == 0 and denomidex >= 0:
        ways_solution[denomidex][amount] = [[],]
        return 1
    elif denomidex < 0 or amount < 0:
        return 0
    else:
        if ways_value[denomidex][amount] != None:
            return ways_value[denomidex][amount]
        else:
            ways_value[denomidex][amount] = _ways_coin_change(denomidex - 1, amount, denominations, ways_value) + _ways_coin_change(denomidex, amount - denominations[denomidex], denominations, ways_value)
            #construct the solution and saved in global variable
            solution_filled(denomidex, amount)
            return ways_value[denomidex][amount]

def ways_coin_change_bottomup(amount: int, denominations: list) -> int:
    ways_value = np.zeros((len(denominations), amount + 1))
    for denomidex in range(len(denominations)):
        ways_value[denomidex][0] = 1
    for denomidex in range(len(denominations)):
        for m in range(1, amount + 1):
            ways_value[denomidex][m] = ways_value[denomidex - 1][m] + ways_value[denomidex][m - denominations[denomidex]]
            #construct the solution and saved in global variable
            #solution_filled(denomidex, m)
    return int(ways_value[len(denominations) - 1][amount])

#?MAIN---------------------------------------------------------------------------------------------------


print(f"Runing {file_path} ...")
choice = input("Do you want to print the solution? (y/n): ")
print("------------------------------------------------------------------------------------------------")
if choice == "y":
    print(f"The number of ways to make change for {amount} units given {denominations} is {ways_coin_change_topdown(amount, denominations)} (usign topdown approach)")
    if ways_solution[len(denominations) - 1][amount] != None: 
        for i in ways_solution[len(denominations) - 1][amount]: 
            if sum(i) <= amount: print(i)
else:
    print(f"The number of ways to make change for {amount} units given {denominations} is {ways_coin_change_bottomup(amount, denominations)} (usign bottomup approach)")
    if ways_solution[len(denominations) - 1][amount] != None: 
        for i in ways_solution[len(denominations) - 1][amount]: 
            if sum(i) <= amount: print(i)
print("------------------------------------------------------------------------------------------------")