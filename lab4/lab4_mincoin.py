from math import inf
import numpy as np

file_path = "lab4/test_case/4.3.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = set(map(int, file.readline().strip().split(sep = " ")))

#?MAIN------------------------------------------------------------------------------------------

def min_coin_change_topdown(amount: int, denominations: set) -> int:
    if amount < min(denominations):
        return inf
    
    amount_index = amount + 1
    min_value = np.full(amount_index, None)
    return _min_coin_change(amount, denominations, min_value)

def _min_coin_change(amount: int, denominations: set, min_value: np.array) -> int:
    if min_value[amount] != None:
        return min_value[amount]
    
    if amount in denominations:
        min_value[amount] = 1
        return 1
    elif amount < min(denominations):
        min_value[amount] = inf
        return min_value[amount]
    else:
        candidates = []
        for i in range(1, int(amount/2 + 1)):
            candidate = _min_coin_change(i, denominations, min_value) + _min_coin_change(amount - i, denominations, min_value)
            candidates.append(candidate)
        min_value[amount] = min(candidates)
        return min_value[amount]

def min_coin_change_bottomup(amount: int, denominations: set) -> int:
    if amount < min(denominations): 
        return inf
    
    min_solution = np.full(amount + 1, None)
    min_value = np.full(amount + 1, None)
    
    for k in range(1, amount + 1):
        if k < min(denominations):
            min_value[k] = inf
        elif k in denominations:
            min_value[k] = 1
            min_solution[k] = [k,]
        else:
            candidates_value = []
            candidates_solution = []
            for i in range(1, int(k/2 + 1)):
                candidate = min_value[i] + min_value[k - i]
                candidates_value.append(candidate)
                
                if min_solution[i] is None or min_solution[k - i] is None:
                    continue
                else:
                    candidate = min_solution[i] + min_solution[k - i]
                    candidates_solution.append(candidate)
                
            min_value[k] = min(candidates_value)
            
            if len(candidates_solution) == 0: 
                min_solution[k] = None
            else:
                min_solution[k] = [solution for solution in candidates_solution if len(solution) == min_value[k]][0]
    print("The min solution is", min_solution[amount], "(using bottom-up approach)")        
    return min_value[amount]
            

#?MAIN--------------------------------------------------------------------------------------------- 

try: 
    print("Minimum coins is" ,min_coin_change_topdown(amount, denominations), "(using top-down approach)")
    print("Minimum coins is" ,min_coin_change_bottomup(amount, denominations), "(using bottom-up approach)")
except RecursionError:
    print("Minimum coins is" ,min_coin_change_bottomup(amount, denominations), "(using bottom-up approach)")