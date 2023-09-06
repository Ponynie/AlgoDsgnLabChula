
file_path = "lab4/test_case/4.1.txt"

with open(file_path, 'r') as file: 
    amount = int(file.readline().strip())
    denominations = set(file.readline().strip().split(sep = " "))
    
