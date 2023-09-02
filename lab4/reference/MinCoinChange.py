import sys
def count(coins, Arraylength, amount): 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    table = [[0 for x in range(amount+1)] for y in range(Arraylength+1)] 
    # Fill the entries for 0 value case (n = 0) 
    for i in range(1,amount+1): 
        table[0][i] = sys.maxsize
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, Arraylength+1): 
        for j in range(1, amount+1): 
           if (j >= coins[i-1]): 
               table[i][j] = min(table[i-1][j], 1 + table[i][j-coins[i-1]])
           else: 
               table[i][j] = table[i-1][j]

    #display combination which is min
    minResult = []
    i = Arraylength
    j = amount
    while i != 0 and j != 0:
        if (j >= coins[i-1]): 
            Min = min(table[i-1][j], table[i][j-coins[i-1]])
            if  table[i][j-coins[i-1]] <= table[i-1][j]:
                Min = table[i][j-coins[i-1]]
                j = j-coins[i-1]
                minResult.append(str(coins[i-1]))
            else:
                Min = table[i-1][j]
                i = i-1
        else:
            i = i-1     
    minResult.reverse()     
    print(table[5][18])
    print("Minimum of Coin is " + str(table[Arraylength][amount]))
    print(minResult)
# Driver program to test above function 
f = open("4.7.txt","r")  
coins = []
amount = int(f.readline())
a = f.readline().strip().split(" ")
for i in a:
    coins.append(int(i))
f.close()
length = len(coins) 

count(coins, length, amount)
