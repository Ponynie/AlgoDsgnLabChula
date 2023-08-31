import itertools
from progress.bar import IncrementalBar
from math import factorial

file_path = "lab3/test_case/3.3.1.txt"

with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

#separate data into two lists: passenger and car, each element in lists is the position of P/G in the data
passengers = [i for i in range(len(data)) if data[i] == 'P'] 
cars = [i for i in range(len(data)) if data[i] == 'G'] 

#function to check if configuration is possible
def configuration_is_possible(configuration, distance):
    for pair in configuration:
        if abs(pair[0] - pair[1]) > distance: 
            return False 
    return True

solutions = []

#generate all possible configurations from the top down maner
for i in range(len(cars), 0, -1): 
    #generate all possible permutations of cars when choose i cars
    car_i_permutations = list(itertools.permutations(cars, i)) 
    #generate all possible combinations of passengers when choose i passengers
    passenger_i_combinations = list(itertools.combinations(passengers, i)) 
    for car_i_choice in car_i_permutations: 
        #for each permutation of cars and each combination of passengers
        for passenger_i_choice in passenger_i_combinations: 
            #create configuration
            configuration = [(car_i_choice[k], passenger_i_choice[k]) for k in range(len(car_i_choice))] 
            #check if the configuration is possible
            if configuration_is_possible(configuration, distance): 
                #add the configuration to list of solutions
                solutions.append(configuration) 
    #if there is at least one solution, break the loop (the solutions will be the solution with max number of passengers)
    if solutions != []: break
    
        
print("----------------------------------------------------------------------------")                
if solutions == []: 
    print("No possible solution")  
else:
    for solution in solutions:
        print(f"One of the max solutions is {solution}") 
    #find max number of passengers
    max_passenger_value = len(solutions[0]) 
    #number of solutions with max number of passengers
    number_max_solution = len(solutions) 
    print(f"Number of all maximum solutions: {number_max_solution}, Maximum number of passenger: {max_passenger_value}") 
print("----------------------------------------------------------------------------")