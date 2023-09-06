import os

def greedy_solution(file_path):
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
                
                while passenger_found == False and left_bound <= right_bound: 
                    if data[left_bound] == "P":
                        data[left_bound] = "X"
                        data[car] = "X"
                        pair = (car, left_bound)
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[left_bound] == "G" or data[left_bound] == "X":
                        left_bound += 1
                        
        print("----------------------------------------------------------------------------------------------------------------")        
        print(f"Greedy solution: {greedy_solution}\nMax: {max_passenger} passengers")
        print("----------------------------------------------------------------------------------------------------------------")  

def greedy_solution_right_scan(file_path):
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
                
                while passenger_found == False and left_bound <= right_bound: 
                    if data[right_bound] == "P":
                        data[right_bound] = "X"
                        data[car] = "X"
                        pair = (car, right_bound)
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[right_bound] == "G" or data[right_bound] == "X":
                        right_bound -= 1
                        
        print("----------------------------------------------------------------------------------------------------------------")        
        print(f"Greedy solution: {greedy_solution}\nMax: {max_passenger} passengers")
        print("----------------------------------------------------------------------------------------------------------------")  

def greedy_solution_left_first_outward_scan(file_path):
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
                pointer = car
                if car - distance < 0: left_bound = 0 
                else: left_bound = car - distance
                if car + distance > len(data) - 1: right_bound = len(data) - 1
                else: right_bound = car + distance
                
                while passenger_found == False and pointer >= left_bound: 
                    if data[pointer] == "P":
                        data[pointer] = "X"
                        data[car] = "X"
                        pair = (car, pointer)
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[pointer] == "G" or data[pointer] == "X":
                        pointer -= 1
                pointer = car
                while passenger_found == False and pointer <= right_bound: 
                    if data[pointer] == "P":
                        data[pointer] = "X"
                        data[car] = "X"
                        pair = (car, pointer)
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[pointer] == "G" or data[pointer] == "X":
                        pointer += 1
                        
        print("----------------------------------------------------------------------------------------------------------------")        
        print(f"Greedy solution: {greedy_solution}\nMax: {max_passenger} passengers")
        print("----------------------------------------------------------------------------------------------------------------")  

def greedy_solution_left_first_inward_scan(file_path):
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
                
                while passenger_found == False and  left_bound <= car: 
                    if data[left_bound] == "P":
                        data[left_bound] = "X"
                        data[car] = "X"
                        pair = (car, )
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[left_bound] == "G" or data[left_bound] == "X":
                        left_bound += 1
                while passenger_found == False and right_bound >= car: 
                    if data[right_bound] == "P":
                        data[right_bound] = "X"
                        data[car] = "X"
                        pair = (car, right_bound)
                        greedy_solution.append(pair)
                        passenger_found = True
                        max_passenger += 1
                    elif data[right_bound] == "G" or data[right_bound] == "X":
                        right_bound -= 1
                        
        print("----------------------------------------------------------------------------------------------------------------")        
        print(f"Greedy solution: {greedy_solution}\nMax: {max_passenger} passengers")
        print("----------------------------------------------------------------------------------------------------------------")  
                        

#'''
path = "lab3/test_case/normal"
time_run = []
test_files = sorted(os.listdir(path))[:]
for test_file in test_files:
    file_path = f"{path}/{test_file}"
    print("Running", test_file, "...")
    greedy_solution(file_path) #*select which function to run here !!
    greedy_solution_right_scan(file_path)
    greedy_solution_left_first_outward_scan(file_path)
    greedy_solution_left_first_inward_scan(file_path)
#'''
    
#greedy_solution("lab3/test_case/3.3.1.txt")