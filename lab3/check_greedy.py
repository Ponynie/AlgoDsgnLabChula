def grabNgub(arr, k):
    i = 0
    l = 0
    r = 0
    res = 0
    Pass = []
    Grab = []
 
    while i < len(arr):
        if arr[i] == 'G':
            Grab.append(i)
        elif arr[i] == 'P':
            Pass.append(i)
        i += 1
 
    while l < len(Pass) and r < len(Grab):

        if (abs( Pass[l] - Grab[r] ) <= k):
            res += 1
            l += 1
            r += 1

        elif Pass[l] < Grab[r]:
            l += 1
        else:
            r += 1
 
    return res


file_path = "lab3/test_case/3.5.3.txt"
with open(file_path, 'r') as file: #read file
    first_line = file.readline().strip() 
    data = list(first_line) 
    second_line = file.readline().strip()  
    distance = int(second_line) 

print(grabNgub(data, distance))