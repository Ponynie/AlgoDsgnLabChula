from itertools import combinations 
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
    
file = open("1.5.txt","r")
K = int(file.readline())
inputData = file.readline().split()
length = len(inputData)
adjacencyMatrix = [[0 for col in range(length)] for row in range(length)]
for i in range(length):
    for j in range(length):
        adjacencyMatrix[i][j] = int(inputData[j])
    inputData = file.readline().split()
#print(adjacencyMatrix)
#print(K)
vertexCover(adjacencyMatrix,K)
file.close()
