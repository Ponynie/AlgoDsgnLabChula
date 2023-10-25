# Floyd Warshall Algorithm in python

INF = 9999999
# Algorithm implementation
def floyd_warshall(G,Lam,vertexNum):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    preprocessor = list(map(lambda i: list(map(lambda j: j, i)), Lam))

    # Adding vertices individually
    for k in range(vertexNum):
        for i in range(vertexNum):
            for j in range(vertexNum):
                #distance[i][j] = min(distance[i][j], max(distance[i][k] , distance[k][j]))
                if(distance[i][j] <= max(distance[i][k] , distance[k][j])):
                    distance[i][j] = distance[i][j]
                    preprocessor[i][j] = preprocessor[i][j]
                else:
                    distance[i][j] = max(distance[i][k] , distance[k][j])
                    preprocessor[i][j] = k+1
                
    print_solution(distance,preprocessor,vertexNum)


# Printing the solution
def print_solution(distance,preprocessor,vertexNum):
    for i in range(vertexNum):
        for j in range(vertexNum):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")
    print("")
    
    for i in range(vertexNum):
        for j in range(vertexNum):
            if i == j:
                print("NIL", end = " ")
            else:
                print(preprocessor[i][j], end="  ")
        print(" ")

file = open("7.1.txt","r")
inputData = file.readline().split() 
vertexNum = int(inputData[0])
EdgeNum = int(inputData[1])
kNum = int(inputData[2])
decibel = [[0 for v in range(vertexNum)] for row in range(vertexNum)]
Lamb = [["NIL" for v in range(vertexNum)] for row in range(vertexNum)]
    
for i in range(EdgeNum):
    inputData = file.readline().split()
    u = int(inputData[0])
    v = int(inputData[1])
    w = int(inputData[2])
    decibel[u-1][v-1] = w
    #decibel[v-1][u-1] = w
    Lamb[u-1][v-1] = u
    #Lamb[v-1][u-1] = v
    
for i in range(vertexNum):
    for j in range(vertexNum):
        if (i != j and decibel[i][j] == 0):
            decibel[i][j] = INF
            
print(decibel)                
print(Lamb)
floyd_warshall(decibel,Lamb,vertexNum)

file.close() 
