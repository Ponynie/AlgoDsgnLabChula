import numpy as np

file_path = "lab4/test_case/4.3.txt"

with open(file_path, 'r') as file: 
    
    amount = int(file.readline().strip())
    denominations = sorted(list(map(int, file.readline().strip().split(sep = " "))))
    
def ways_coin_change_topdown(amount: int, denominations: list) -> int:
    ways_value = np.full((len(denominations), amount + 1), None)
    pass

def _ways_coin_change(denomidex: int, amount: int, denominations: list, ways_value: np.array, ways_solution: np.array) -> int:
    if amount == 0 and denomidex >= 0:
        return 1
    elif denomidex < 0 or amount < 0:
        return 0
    else:
        if ways_value[denomidex][amount] != None:
            return ways_value[denomidex][amount]
        else:
            ways_value[denomidex][amount] = _ways_coin_change(denomidex - 1, amount, denominations, ways_value, ways_solution) + _ways_coin_change(denomidex, amount - denominations[denomidex], denominations, ways_value, ways_solution)
            return ways_value[denomidex][amount]

print(denominations[0])