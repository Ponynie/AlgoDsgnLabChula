f = open("lab3/test.txt","r")  
array = []
a = f.readline().strip()
for i in a:
    array.append(i)
k = int(f.readline())
f.close()

# Greedy technique
output = 0
for i in range(len(array)):
    n = 0
    found = False
    if array[i] == 'G':
        if i-k < 0:
            a = 0
        else:
            a = i-k
        if i+k > len(array)-1:
            b = len(array)-1
        else:
            b = i+k
        r = b-a
        while n < r and found == False: 
             
            if n % 2 == 0 and a != i: 
                if array[a] == 'P':
                    array[a] = None
                    output=output+1
                    found = True  # if 'G' can find 'P' then break
                a=a+1
            elif n % 2 != 0 and a!= i:
                if array[a] == 'P':
                    array[a] = None
                    output=output+1
                    found = True  
                a=a+1
            elif n % 2 == 0 and b!= i:
                if array[b] == 'P':
                    array[b] = None
                    output=output+1
                    found = True
                b=b-1
            elif n % 2 != 0 and b!= i:
                if array[b] == 'P':
                    array[b] = None
                    output=output+1
                    found = True
                b=b-1 
             
            n=n+1       
print("output:",output)