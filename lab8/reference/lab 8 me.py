
def FindNewSequence(n):
    x = []
    allPair = []
    #initial array x keep all x
    for i in range(0,n+1):
        x.append(i)
    # divide    
    for i in range(1,n):
        border = min((len(x)-1)-i, i-0)
        for j in range(1,border+1):
            s = x[i]
            if s == (x[i-j] + x[i+j])/2:
                allPair.append((s,x[i-j],x[i+j]))
    print(allPair)
FindNewSequence(4)
'''
file = open("8.1.txt","r")
inputData = int(file.readline().split())
FindNewSequence(InputData)
file.close()
'''