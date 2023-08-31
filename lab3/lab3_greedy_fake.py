
file_path = "lab3/test_case/3.1.3.txt"

with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

greedy_solution = []
max_passenger = 0
for element in range(len(data)):
    if data[element] == "G":
        car = element
        passenger_found = False
        if car - distance < 0: left_bound = 0
        else: left_bound = car - distance
        if car + distance > len(data) - 1: right_bound = len(data) - 1
        else: right_bound = car + distance
        
        while passenger_found == False and left_bound != car:
            if data[left_bound] == "P":
                data[left_bound] = "X"
                data[car] = "X"
                pair = (car, left_bound)
                greedy_solution.append(pair)
                passenger_found = True
                max_passenger += 1
            elif data[left_bound] == "G" or data[left_bound] == "X":
                left_bound += 1
        
        while passenger_found == False and right_bound != car:
            if data[right_bound] == "P":
                data[right_bound] = "X"
                data[car] = "X"
                pair = (car, right_bound)
                greedy_solution.append(pair)
                passenger_found = True
                max_passenger += 1
            elif data[right_bound] == "G" or data[right_bound] == "X":
                right_bound -= 1
          
print("----------------------------------------------------------------------------")        
print(f"Greedy solution: {greedy_solution}\nMax: {max_passenger} passengers")
print("----------------------------------------------------------------------------")  


    