f = open("lab3/test.txt","r")  
array = []
a = f.readline().strip()
for i in a:
    array.append(i)
k = int(f.readline())
f.close()

# Brute Force technique
def BruteForce(ar,output):
    global count
      
    for i in range(len(ar)):
        if ar[i] == 'G':
            if i-k < 0:
                a = 0
            else:
                a = i-k
            if i+k > len(array)-1:
                b = len(array)-1
            else:
                b = i+k
            while a <= b:
                if a != i: 
                    if ar[a] == 'P':
                        ar[a] = None
                        ar[i] = None
                        output = output+1
                        BruteForce(ar,output)
                        ar[a] == 'P'
                        ar[i] == 'G'
                a=a+1
    if output > maxnum:
        output = maxnum
    if output == maxnum:
        count = count + 1      

ar = array
maxnum = 0
output = 0
count = 0
BruteForce(ar,output)
print("count max:", count)    
    