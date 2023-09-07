
file_path = "lab4/test_case/4.3.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = set(file.readline().strip().split(sep = " "))
    
def coin_change_ways(amount: int, denominations: set) -> int:
    pass


coin_change_ways(amount, list(denominations))