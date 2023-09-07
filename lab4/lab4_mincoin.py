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
     #If amount is less than the smallest denomination, then it is impossible to make change
    if amount < min(denominations):
        return inf
    #Store the solution for each amount
    min_solution = np.full(amount + 1, None) 
    #Store the minimum number of coins for each amount
    min_value = np.full(amount + 1, None) 
    
    #Iterate through each amount
    for k in range(1, amount + 1): 
        #If amount is less than the smallest denomination, then it is impossible to make change
        if k < min(denominations): 
            min_value[k] = inf
        #If amount is a denomination, then the minimum number of coins is 1
        elif k in denominations: 
            #Store the minimum number of coins for each amount
            min_value[k] = 1 
            #Store the solution for each amount
            min_solution[k] = [k,]
        #If amount is not a denomination, then the minimum number of coins is the minimum number of coins for the sum of two sub-amounts
        else: 
            candidates_value = [] 
            candidates_solution = []
            #Iterate through each sub-amount less than k
            for i in range(1, int(k/2 + 1)): 
                #Calculate the minimum number of coins for the sum of two sub-amounts
                candidate = min_value[i] + min_value[k - i] 
                #Store the minimum number of coins for the sum of two sub-amounts
                candidates_value.append(candidate) 
                #If there is no solution for one of the sub-amounts, then there is no solution for the sum of two sub-amounts
                if min_solution[i] is None or min_solution[k - i] is None: 
                    continue
                #Store the solution for the sum of two sub-amounts
                else:
                    candidate = min_solution[i] + min_solution[k - i] 
                    candidates_solution.append(candidate)
            #Store the minimum number of coins for each amount    
            min_value[k] = min(candidates_value) 
            #If there is no solution for the sum of two sub-amounts, then there is no solution for the amount
            if len(candidates_solution) == 0: 
                min_solution[k] = None
            #If there is a solution for the sum of two sub-amounts, then store the minimun solution for the amount
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