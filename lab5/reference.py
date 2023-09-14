
from math import sqrt

def findTriangle(point1,point2,point3,table,keepPoint,result):
    if table[point1][point2]==0:      
        if table[point2][point3]==0: 
            return result
        else:
            result.append(keepPoint[point2][point3])
            findTriangle(keepPoint[point2][point3][0],keepPoint[point2][point3][1],keepPoint[point2][point3][2],table,keepPoint,result)
            return result
        
    if table[point2][point3]==0:
        result.append(keepPoint[point1][point2])
        findTriangle(keepPoint[point1][point2][0],keepPoint[point1][point2][1],keepPoint[point1][point2][2],table,keepPoint,result)
        return result
    
    if table[point1][point2]>table[point2][point3]:
        result.append(keepPoint[point2][point3])      
        findTriangle(keepPoint[point2][point3][0],keepPoint[point2][point3][1],keepPoint[point2][point3][2],table,keepPoint,result) 
        return result
    
    elif table[point1][point2]<table[point2][point3]:
        result.append(keepPoint[point1][point2])      
        findTriangle(keepPoint[point1][point2][0],keepPoint[point1][point2][1],keepPoint[point1][point2][2],table,keepPoint,result)       
        return result
    
    elif table[point1][point2]==table[point2][point3] :      
        result.append(keepPoint[point2][point3])      
        findTriangle(keepPoint[point2][point3][0],keepPoint[point2][point3][1],keepPoint[point2][point3][2],table,keepPoint,result)       
        return result
    
    else:     
        return result

def distance(p1, p2): # calculate distance from point1 to point2
    return sqrt((float(p1[0]) - float(p2[0]))*(float(p1[0]) - float(p2[0])) + (float(p1[1]) - float(p2[1]))*(float(p1[1]) - float(p2[1]))) 
  
def cost(pointData, startPoint, middleP, lastPoint): # calculate cost
    p1 = pointData[startPoint]
    p2 = pointData[middleP]
    p3 = pointData[lastPoint] 
    return distance(p1, p2) + distance(p2, p3) + distance(p3, p1)

def minPolyCost(pointData,point):   
    if point<3:       
        return 0  
    table = [] 
    keepPoint = []
    # create two dimension table (point x point) for keeping point    
    for i in range(point):
        keepPoint.append([])       
        keepPoint[i] = []     
        for j in range(point):          
            keepPoint[i].append([])
    # create two dimension table (point x point) for keeping cost 
    for i in range(point):        
        table.append(0.0)        
        table[i] = []
        for j in range(point):           
            table[i].append(0.0)            
    
    for gap in range(point):      
        startPoint = 0 
        for lastPoint in range(gap,point): # find point pair 
           if lastPoint<startPoint+2: 
               table[startPoint][lastPoint] = 0.0
               startPoint+=1     
           else:
              table[startPoint][lastPoint] = None 
              
              for middlePoint in range(startPoint+1,lastPoint): 
                  # find cost and keep in table
                  value = table[startPoint][middlePoint] + table[middlePoint][lastPoint] + cost(pointData,startPoint,middlePoint,lastPoint)
                  value = round(value,4)
                  if table[startPoint][lastPoint] == None:
                      table[startPoint][lastPoint] = value
                      keepPoint[startPoint][lastPoint] = [startPoint,middlePoint,lastPoint]
                   # if the cost in table is more than value then cost in that position equals value
                  elif table[startPoint][lastPoint] > value :
                      table[startPoint][lastPoint] = value                     
                      keepPoint[startPoint][lastPoint] = [startPoint,middlePoint,lastPoint]
                      
              startPoint+=1
    result=[keepPoint[0][point-1]]
#   # keep the table to display
    sol = findTriangle(keepPoint[0][point-1][0],keepPoint[0][pointAmount-1][1],keepPoint[0][point-1][2],table,keepPoint,result)    
    answer=[table,sol]    # return two dimensions array
              
    return answer

inputFile = open("lab5/test_case/5 Extra.txt","r")
pointAmount = int(inputFile.readline())
pointData = []
for i in range(pointAmount):
    pointData.append(inputFile.readline().strip().split(" "))
inputFile.close()

report = minPolyCost(pointData,pointAmount)                     

print("Table")

for i in range(pointAmount):
    for j in range(pointAmount):
        if j==pointAmount-1:            
            print(report[0][i][j])
        else:
            print(report[0][i][j], end = '       ')

print('')
print("minimun cost is :",report[0][0][pointAmount-1])
print("triangles : ",report[1])
#print(pointData)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        