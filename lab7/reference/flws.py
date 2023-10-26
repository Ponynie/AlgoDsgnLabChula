import sys

def getInput(fileName,directed = False):
    f = open(fileName)
    inp = [x.replace("\n","").split(" ") for x in f.readlines()]
    f.close()
    maxint = sys.maxsize
    info = inp.pop(0)
    verticles = int(info[0])
    edges = int(info[1])
    numTest = int(info[2])
    tmpPath = [maxint for x in range(verticles)]
    graph = [tmpPath.copy() for x in range(verticles)]
    for x in range(verticles) : graph[x][x] = 0
    for y in range(edges): 
        x = inp.pop(0)
        graph[int(x[0])-1][int(x[1])-1] = int(x[2])
        if not directed : graph[int(x[1])-1][int(x[0])-1] = int(x[2])
    checkList = []
    for y in range(numTest): 
        x = inp.pop(0)
        checkList.append([int(x[0])-1, int(x[1])-1])
    return [graph, checkList]

def apsp(w):
    numVertexs = len(w)
    d = w
    maxint = sys.maxsize
    tmpmax = [maxint for j in range(numVertexs)] 
    p = [tmpmax.copy() for i in range(numVertexs)]
    for i in range(numVertexs):
        for j in range(numVertexs):
            if(i!=j and d[i][j] < maxint): p[i][j] = i 
    for k in range(numVertexs):
        dx = [[] for x in range(numVertexs)]
        px = [[] for x in range(numVertexs)]
        for i in range(numVertexs):
            for j in range(numVertexs):
                if i!=j : 
                    md = min(d[i][j], max(d[i][k],d[k][j]))
                else: 
                    md = 0
                dx[i].append(md)
                if(i!=j):
                    if(d[i][j] > max(d[i][k],d[k][j])): px[i].append(p[k][j]) 
                    else: px[i].append(p[i][j])
                else: 
                    px[i].append(maxint)
        d = dx
        p = px
    return [d,p]

def minNoise(w,s,d,a = 0):
    if a == 0: a = apsp(w)
    if a[0][s][d] == sys.maxsize: return "no path"
    else : return a[0][s][d]
    
def showMinNoisePath(w,s,d,a = 0):
    if a == 0: a = apsp(w)
    if minNoise(w,s,d,a = 0) == "no path" : return []
    if s == d : return [s+1]
    info = a[1]
    lst = [s+1,d+1]
    i = s
    j = d
    while i != j and i != info[i][j]:
        lst.insert(1,info[i][j]+1)
        j = info[i][j]
    return lst

def allMinNoisePath(w):
    lst = [[], []]
    a = apsp(w)
    for i in range(len(w)):
        for j in range(len(w)):
            lst[0].append([i+1,j+1])
            lst[1].append(showMinNoisePath(w,i,j,a))
    return lst

def allMinNoise(w):
    lst = [[], []]
    a = apsp(w)
    for i in range(len(w)):
        for j in range(len(w)):
            lst[0].append([i+1,j+1])
            lst[1].append(minNoise(w,i,j,a))
    return lst

def getAnswerNoise(graph,checkList, a = 0):
    if a == 0 : a = apsp(graph)
    ans = []
    for x in checkList: ans.append(minNoise(graph,x[0],x[1],a))
    return ans
    
def getAnswerPath(graph,checkList, a = 0):
    if a == 0 : a = apsp(graph)
    ans = []
    for x in checkList: ans.append(showMinNoisePath(graph,x[0],x[1],a))
    return ans