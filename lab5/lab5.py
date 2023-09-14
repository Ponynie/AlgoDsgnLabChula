import numpy as np
from math import atan2

def ensure_positive_oriented(pointsArray: list, point_num: int):
    central_x = sum([point[0] for point in pointsArray])/point_num
    central_y = sum([point[1] for point in pointsArray])/point_num
    pointsArray.sort(key = lambda point: atan2(point[1] - central_y, point[0] - central_x))
        
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def weight(pointsArray, p1_idx, p2_idx, p3_idx): #calculate weight
    p1 = pointsArray[p1_idx]
    p2 = pointsArray[p2_idx]
    p3 = pointsArray[p3_idx] 
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1)

def cost_triangulate(i: int, k: int ,pointsArray: list, value_table: np.ndarray, solution_table: np.ndarray):
    if value_table[i][k] > 0:
        return value_table[i][k]
    
    if k < i + 2:
        return 0
    else:
        candidate = [cost_triangulate(i, j, pointsArray, value_table, solution_table) + cost_triangulate(j, k, pointsArray, value_table, solution_table) + weight(pointsArray, i, j, k) for j in range(i + 1, k)]
        value_table[i][k] = min(candidate)
        solution_table[i][k] = candidate.index(min(candidate)) + i + 1
        return value_table[i][k]

def print_solution(i: int, k: int, solution_table: np.ndarray):
    if i + 2 > k:
        return
    else:
        print(i, solution_table[i][k], k)
        print_solution(i, solution_table[i][k], solution_table)
        print_solution(solution_table[i][k], k, solution_table)

def main(path):
    with open(path, 'r') as f:
        point_num = int(f.readline())
        points = [tuple(map(float, f.readline().strip().split(" "))) for _ in range(point_num)]
        
        value_table = np.zeros((point_num, point_num))
        value_solution = np.full((point_num, point_num), None)
        
        ensure_positive_oriented(points, point_num)
        print(points)
        cost_triangulate(0, point_num - 1, points, value_table, value_solution)
        
        print(value_table[0][point_num - 1])
        print_solution(0, point_num - 1, value_solution)

file_path = "lab5/test_case/4.txt"
main(file_path)
