import numpy as np

file_path = "lab4/test_case/4.7.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = sorted(list(map(int, file.readline().strip().split(sep = " "))))
    
def ways_coin_change_topdown(amount: int, denominations: list) -> int:
    ways_value = np.full((len(denominations), amount + 1), None)
    return _ways_coin_change(len(denominations) - 1, amount, denominations, ways_value)

def _ways_coin_change(denomidex: int, amount: int, denominations: list, ways_value: np.array) -> int:
    if amount == 0 and denomidex >= 0:
        return 1
    elif denomidex < 0 or amount < 0:
        return 0
    else:
        if ways_value[denomidex][amount] != None:
            return ways_value[denomidex][amount]
        else:
            ways_value[denomidex][amount] = _ways_coin_change(denomidex - 1, amount, denominations, ways_value) + _ways_coin_change(denomidex, amount - denominations[denomidex], denominations, ways_value)
            return ways_value[denomidex][amount]

def ways_coin_change_bottomup(amount: int, denominations: list) -> int:
    ways_value = np.zeros((len(denominations), amount + 1))
    for denomidex in range(len(denominations)):
        ways_value[denomidex][0] = 1
    for denomidex in range(len(denominations)):
        for m in range(1, amount + 1):
            ways_value[denomidex][m] = ways_value[denomidex - 1][m] + ways_value[denomidex][m - denominations[denomidex]]
    return int(ways_value[len(denominations) - 1][amount])

#print(f"The number of ways to make change for {amount} units given {denominations} is {ways_coin_change_topdown(amount, denominations)} (usign topdown approach)")
print(f"The number of ways to make change for {amount} units given {denominations} is {ways_coin_change_bottomup(amount, denominations)} (usign bottomup approach)")