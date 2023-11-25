from itertools import combinations 

def reduce3SATtoVertexCover(clause,clauseNum,vertexNum):
    newVertexNum = 2*vertexNum + 3*clauseNum
    vertexCoverNum = vertexNum + 2*clauseNum
    print(newVertexNum)
    print(vertexCoverNum)
    vertex = []
    i = 1
    while i < vertexNum*2: # create vertex paired like 1, -1, 2, -2, 3, -3, etc.
        vertex.append(i)
        vertex.append(-i)
        i = i+1
    #print(vertex)
    adjacencyMatrix = [[0 for col in range(newVertexNum)] for row in range(newVertexNum)]
    # connect the x1 to x1 complement
    i = 0
    while i < vertexNum*2:
        adjacencyMatrix[i][i+1] = 1
        adjacencyMatrix[i+1][i] = 1
        i = i+2
    # connect clause
    n = i # keep the index that start clause vertex
    cnt = 0
    while cnt < clauseNum:
        adjacencyMatrix[i][i+1] = 1
        adjacencyMatrix[i+1][i] = 1
        adjacencyMatrix[i+1][i+2] = 1
        adjacencyMatrix[i+2][i+1] = 1
        adjacencyMatrix[i][i+2] = 1
        adjacencyMatrix[i+2][i] = 1
        cnt = cnt+1
        i=i+3
    # connect clause to paired vertex 
    index = 0
    for i in clause:
        for j in i:
            for k in vertex:
                if int(j) == k:
                    adjacencyMatrix[index][n] = 1
                    adjacencyMatrix[n][index] = 1
                    break
                index = index+1
            index = 0
            n = n+1
    string = ""
    for i in adjacencyMatrix:
        for j in i:
            print(j, end = ' ')
        print()
    return vertexCoverNum, adjacencyMatrix

def vertexCover(adjacencyMatrix, K):
    length = len(adjacencyMatrix)
    edge = []
    tmp = []
    foundVertexCover = False
    vertex = [False] * length
    cnt = 0
    # add edge which is not repeated
    for i in range(length): 
        for j in range(0+cnt,length):
            if adjacencyMatrix[i][j] != 0:
                edge.append([i,j])
        cnt = cnt+1
        tmp.append(i)
    #print(edge)
    combination = combinations(tmp,K) # create all possible answer to check
    tmp = []
    for i in edge:
        tmp.append(i)
    for c in combination: # run every set of combination to check what answer is true
        for i in c:
            for j in edge:
                if i == j[0] or i == j[1]:
                    if j in tmp:
                        tmp.remove(j)
        if len(tmp) == 0: # if there is an answer (every edges have discovered)
            if foundVertexCover == False:
                print("Yes")
                foundVertexCover = True
            p = ""
            for o in c:
                p = p + str(o+1) + " "
            print(p)
        tmp.clear()
        for i in edge:
            tmp.append(i)
    if foundVertexCover == False:
        print("No")


file = open("lab10/test_case/3.2.txt","r")
clauseNum = int(file.readline())
clause = []
vertexNum = 0
for i in range(clauseNum):
    inputData = file.readline().split()
    clause.append(inputData)
    for j in inputData:
        if int(vertexNum) < abs(int(j)):
            vertexNum = abs(int(j))
vertexNum = int(vertexNum)             
vertexCoverNum, adjacencyMatrix  = reduce3SATtoVertexCover(clause,clauseNum,vertexNum)
vertexCover(adjacencyMatrix,vertexCoverNum)
file.close()