#KMP Search
def KMPSearch(pat, txt, mode): 
    M = len(pat) 
    N = len(txt[0]) 
    indexFound = ""
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
    
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
    stringtxt = ""
    for k in range(len(txt)):
        for o in txt[k]:
            stringtxt = stringtxt + o
        
        i = 0 # index for txt[] 
        while i < N+M: 
            if pat[j%M] == stringtxt[i%N]: 
                i += 1
                j += 1

            if j == M: 
                if mode == "LR":
                    indexFound = indexFound + str(k+1) + " " + str(i-j+1) + " " + mode + "\n"
                elif mode == "RL":
                    indexFound = indexFound + str(k+1) + " " + str((N+1)-(i-j+1)) + " " + mode + "\n"
                elif mode == "UB":
                    indexFound = indexFound + str(i-j+1) + " " + str(k+1) + " " + mode + "\n"
                elif mode == "BU":
                    indexFound = indexFound + str(N-(i-j+1)+1) + " " + str(k+1) + " " + mode + "\n"
                j = lps[(j%M)-1] 

            # mismatch after j matches 
            elif i < N+M and pat[j%M] != stringtxt[i%N]: 
                # Do not match lps[0..lps[j-1]] characters, 
                # they will match anyway 
                if j != 0: 
                    j = lps[(j%M)-1] 
                else: 
                    i += 1
        
        stringtxt = ""
        j = 0
    return lps, indexFound
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1

file = open("9.3.2.txt","r")
inputData = file.readline()
inputData = file.readline().split()
row = int(inputData[0])
column = int(inputData[1])
textLR = []
textRL = []
textUB = []
textBU = []
for i in range(row):   
    inputData = file.readline().strip(" ").split()  
    textLR.append(inputData)

file.seek(0)
inputData = file.readline()
inputData = file.readline()
for i in range(row): 
    inputData = file.readline().strip(" ").split()  
    inputData.reverse()
    textRL.append(inputData)

pattern = file.readline()
pattern = pattern.replace(" ","")

mode = "LR"
lps, indexFound = KMPSearch(pattern, textLR, mode) 
string = ""
for i in lps:
    string = string + str(i) + " "
string = string.rstrip(" ")
print(string)
indexFound = indexFound.rstrip("\n")
if len(indexFound) != 0:
    print(indexFound)

mode = "RL"
lps, indexFound = KMPSearch(pattern, textRL, mode) 
indexFound = indexFound.rstrip("\n")
if len(indexFound) != 0:
    print(indexFound) 

mode = "UB"
tmp = []
for i in range(column):
    for j in range(row):
        tmp.append(textLR[j][i])
    textUB.append(tmp)
    tmp = []    
lps, indexFound = KMPSearch(pattern, textUB, mode) 
indexFound = indexFound.rstrip("\n")
if len(indexFound) != 0:
    print(indexFound)

mode = "BU"
tmp2 = []
for i in range(column):
    tmp2 = textUB[i]
    tmp2.reverse()
    textBU.append(tmp2)
    tmp2 = []
lps, indexFound = KMPSearch(pattern, textBU, mode) 
indexFound = indexFound.rstrip("\n")
if len(indexFound) != 0:
    print(indexFound)

file.close()