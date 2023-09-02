def count(coins, Arraylength, amount): 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    table = [[0 for x in range(Arraylength)] for y in range(amount+1)] 
    # Fill the entries for 0 value case (n = 0) 
    for i in range(Arraylength): 
        table[0][i] = 1
        
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, amount+1): 
        for j in range(Arraylength): 
            # Count of solutions including S[j] 
            x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
            # total count 
            table[i][j] = x + y 
           
    return table[amount][Arraylength-1] 
# Driver program to test above function 
f = open("4.1.txt","r")  
coins = []
amount = int(f.readline())
a = f.readline().strip().split(" ")
for i in a:
    coins.append(int(i))
f.close()

length = len(coins) 
result = count(coins, length, amount)
if result > 0:
    print(result)
else:  
    print("Cannot give coin change")