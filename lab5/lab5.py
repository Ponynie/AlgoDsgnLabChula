file_path = "lab5/test_case/1.1.txt"

with open(file_path, 'r') as f:
    point_num = int(f.readline())
    points = []
    for i in range(point_num):
        points.append(tuple(map(int, f.readline().strip().split(" "))))
        
def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def weight(pointsArray, p1_idx, p2_idx, p3_idx): #calculate weight
    p1 = pointsArray[p1_idx]
    p2 = pointsArray[p2_idx]
    p3 = pointsArray[p3_idx] 
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1)

print(points)