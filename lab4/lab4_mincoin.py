from math import inf

file_path = "lab4/test_case/4.1.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = set(file.readline().strip().split(sep = " "))
    

def min_coin_change(amount: int, denominations: set) -> int:
    lookup = dict()
    return _min_coin_change(amount, denominations, lookup)


def _min_coin_change(amount: int, denominations: set, lookup: dict) -> int:
    if amount in lookup:
        return lookup[amount]
    
    if amount in denominations:
        lookup[amount] = 1
        return 1
    elif amount < min(denominations):
        lookup[amount] = inf
        return inf
    else:
        candidates = []
        for i in range(1, int(amount/2 + 1)):
            candidate = _min_coin_change(i, denominations, lookup) + _min_coin_change(amount - i, denominations, lookup)
            candidates.append(candidate)
        lookup[amount] = min(candidates)
        return min(candidates)
        
print(min_coin_change(10, {2,3,9}))