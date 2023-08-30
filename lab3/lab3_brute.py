import itertools
from progress.bar import IncrementalBar

file_path = "lab3/test_case/3.5.1.txt"

with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

#separate data into two lists: passenger and car, each element in lists is the position of P/G in the data
passenger = [i for i in range(len(data)) if data[i] == 'P'] 
car = [i for i in range(len(data)) if data[i] == 'G'] 

def configuration_is_possible(configuration, distance): #function to check if configuration is possible
    for pair in configuration:
        if abs(pair[0] - pair[1]) > distance: #if the distance between car and passenger is greater than distance provided
            return False 
    return True

bar = IncrementalBar('Processing', max = len(car))

solutions = [] #list of solutions

for i in range(1, len(car) + 1): #generate all possible configurations
    car_i_permutations = list(itertools.permutations(car, i)) #generate all possible permutations of cars when choose i cars
    passenger_i_combinations = list(itertools.combinations(passenger, i)) #generate all possible combinations of passengers when choose i passengers
    for car_i_choice in car_i_permutations: 
        for passenger_i_choice in passenger_i_combinations: #for each permutation of cars and each combination of passengers
            configuration = [(car_i_choice[k], passenger_i_choice[k]) for k in range(len(car_i_choice))] #create configuration
            if configuration_is_possible(configuration, distance): #check if the configuration is possible
                solutions.append(configuration) #add the configuration to list of solutions
    bar.next()
bar.finish()
        
print("----------------------------------------------------------------------------")                
if solutions == []: 
    print("No possible solution")  #if there is no solution, print "No possible solution"
else:
    for solution in solutions:
        print(f"One of the solutions is {solution}") #print all solutions
    max_passenger_value = len((max(solutions, key=len))) #find max number of passengers
    number_max_solution = sum(1 for solution in solutions if len(solution) == max_passenger_value) #count number of solutions with max number of passengers
    print(f"Number of all maximum solutions: {number_max_solution}, Maximum number of passenger: {max_passenger_value}") #print number of solutions with max number of passengers
print("----------------------------------------------------------------------------")