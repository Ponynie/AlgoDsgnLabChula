from itertools import combinations 
def vertexCover(adjacencyMatrix):
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
    for K in range(2,length):
        combination = combinations(tmp,K) # create all possible answer to check O(n) = n^K
        tmp2 = []
        for i in edge:
            tmp2.append(i)
        for c in combination: # run every set of combination to check what answer is true
            for i in c:
                for j in edge:
                    if i == j[0] or i == j[1]:
                        if j in tmp2:
                            tmp2.remove(j)
            if len(tmp2) == 0: # if there is an answer (every edges have discovered)
                p = ""
                for o in c:
                    p = p + str(o+1) + " "
                print(p)
                print(K)
                return None
            tmp2.clear()
            for i in edge:
                tmp2.append(i)
   
file = open("10.2.txt","r")
inputData = file.readline().split()
length = len(inputData)
adjacencyMatrix = [[0 for col in range(length)] for row in range(length)]
for i in range(length):
    for j in range(length):
        adjacencyMatrix[i][j] = int(inputData[j])
    inputData = file.readline().split()
#print(adjacencyMatrix)
#print(K)
vertexCover(adjacencyMatrix)
file.close()
