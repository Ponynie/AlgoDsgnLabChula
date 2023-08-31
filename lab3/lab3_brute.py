import itertools
from progress.bar import IncrementalBar
from math import factorial

file_path = "lab3/test_case/3.1.2.txt"

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
        #if the distance between car and passenger is greater than distance provided
        if abs(pair[0] - pair[1]) > distance: 
            return False 
    return True

num_operation = 0
for i in range(1, len(cars) + 1):
    ng = len(cars)
    np = len(passengers)
    if np - i < 0: continue
    num_operation += (factorial(ng)/factorial(ng-i)) * (factorial(np)/(factorial(np-i) * factorial(i)))

bar = IncrementalBar('Processing', max = num_operation)
#list of solutions
solutions = [] 
#generate all possible configurations
for i in range(1, len(cars) + 1): 
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
            bar.next()
bar.finish()
        
print("----------------------------------------------------------------------------")                
if solutions == []: 
    #if there is no solution, print "No possible solution"
    print("No possible solution")  
else:
    for solution in solutions:
        #print all solutions
        print(f"One of the solutions is {solution}") 
    #find max number of passengers
    max_passenger_value = len((max(solutions, key=len))) 
    #count number of solutions with max number of passengers
    number_max_solution = sum(1 for solution in solutions if len(solution) == max_passenger_value) 
    #print number of solutions with max number of passengers
    print(f"Number of all maximum solutions: {number_max_solution}, Maximum number of passenger: {max_passenger_value}") 
print("----------------------------------------------------------------------------")