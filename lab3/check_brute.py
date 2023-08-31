from itertools import chain, combinations
def reachable(arr,k):
    pickup_able = {}
    for i in range(len(arr)):
        if arr[i] == 'G':
            pickup_able[i] = []
            j = i - k
            if (j < 0): j = 0
            while j < i+k+1:
                if not (j < len(arr)): break
                if i == j: 
                    j+=1
                    continue
                if arr[j] == 'P':
                    pickup_able[i].append(j)
                j+=1
    return pickup_able

def generatePair(adj):
    pairs = {}
    for i in list(adj):
        pairs[i] = []
        if(len(adj[i]) > 0):
            for j in adj[i]:
                tmp = (i,j)
                pairs[i].append(tmp)
    return pairs

def cartesianProduct(arr):
    result = [[]]
    for a in arr:
        result = [x+[y] for x in result for y in a]
    return result

def powerset(arr):
    return list(chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1)))

def generatePossibility(pairs):
    lst = [pairs[x] for x in list(pairs) if len(pairs[x]) > 0]
    possibility = cartesianProduct(lst)
    #print(possibility)
    truePossibility = {}
    tmp = []
    for i in possibility:
        p = [x[1] for x in i]
        q = set(p)
        if(len(p) != len(q)): 
            ps = powerset(i)
            ps2 = [list(x) for x in ps if len(list(x)) == (len(lst) - 1)]
            for psx in ps2:
                pp = [x[1] for x in psx]
                qq = set(pp)
                if(len(pp) == len(qq)): tmp.append(psx)
                else: recursiveCut(tmp,psx,len(lst) - 2)
        else:
            tmp.append(i)
    tmp2 = []
    for i in tmp:
        if(i not in tmp2): tmp2.append(i)
    for i in tmp2:
        if len(i) not in truePossibility: truePossibility[len(i)] = []
        truePossibility[len(i)].append(i)
    return truePossibility

def recursiveCut(arr,e,size):
    if(size < 1): return 
    ps = [list(x) for x in powerset(e) if len(list(x)) == size]
    for psx in ps:
        pp = [x[1] for x in psx]
        qq = set(pp)
        if(len(pp) == len(qq)): arr.append(psx)
        else: return recursiveCut(arr,psx,size-1)

def grabNgub(arr,k):
    adj = reachable(arr,k)
    #print(adj)
    pairs = generatePair(adj)
    #print(pairs)
    possibility = generatePossibility(pairs)
    print(possibility)
    if len(list(possibility)) > 0 : return max(list(possibility))
    else: return 0
    
file_path = "lab3/test_case/3.5.3.txt"
with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

print(grabNgub(data, distance))