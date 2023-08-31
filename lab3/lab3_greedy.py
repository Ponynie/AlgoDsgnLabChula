
file_path = "lab3/test_case/3.4.4.txt"

with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

max_passenger = 0
for element in range(len(data)):
    if data[element] == "G":
        car = element
        passenger_found = False
        if car - distance < 0: left_bound = 0
        if car + distance > len(data) - 1: right_bound = len(data) - 1
        left_bound = car - distance
        right_bound = car + distance
        
        while passenger_found == False and left_bound != car:
            if data[left_bound] == "P":
                data[left_bound] = "X"
                data[car] = "X"
                passenger_found = True
                max_passenger += 1
            elif data[left_bound] == "G" or data[left_bound] == "X":
                left_bound += 1
        
        while passenger_found == False and right_bound != car:
            if data[right_bound] == "P":
                data[right_bound] = "X"
                data[car] = "X"
                passenger_found = True
                max_passenger += 1
            elif data[right_bound] == "G" or data[right_bound] == "X":
                right_bound -= 1
                
print(max_passenger)


    