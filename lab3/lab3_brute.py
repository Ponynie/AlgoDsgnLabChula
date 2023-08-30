import itertools

file_path = "lab3/test.txt"

with open(file_path, 'r') as file:
    first_line = file.readline().strip()
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

passenger = [i for i in range(len(data)) if data[i] == 'P']
car = [i for i in range(len(data)) if data[i] == 'G']

def configuration_is_possible(configuration, distance):
    for pair in configuration:
        if abs(pair[0] - pair[1]) > distance:
            return False
    return True

solutions = []
for i in range(1, len(car) + 1):
    car_i_permutations = list(itertools.permutations(car, i))
    passenger_i_combinations = list(itertools.combinations(passenger, i))
    for car_i_permutation in car_i_permutations:
        for passenger_i_combination in passenger_i_combinations:
            configuration = [(car_i_permutation[i], passenger_i_combination[i]) for i in range(len(car_i_permutation))]
            if configuration_is_possible(configuration, distance): 
                solutions.append(configuration)
            
                
for solution in solutions:
    print(f"One of the solutions is {solution}")

number_of_max_solution = len(max(solutions, key=len))
print(f"Number of all maximum solutions: {number_of_max_solution}")
