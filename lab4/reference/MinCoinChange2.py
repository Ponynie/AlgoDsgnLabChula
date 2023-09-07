import sys
def minCoins(coins, coinsLength, amount): 
    
    table = [0 for i in range(amount + 1)] 
  
    # Base case (If given value V is 0) 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, amount + 1): 
        table[i] = sys.maxsize 
  
    # Compute minimum coins required  
    # for all values from 1 to V 
    for i in range(1, amount + 1): 
        # Go through all coins smaller than i 
        for j in range(coinsLength): 
            if (coins[j] <= i): 
                sub = table[i - coins[j]]  # sub = amount - coin value, which is min coin amount that use for change table[i-coins[j]] baht
                if (sub != sys.maxsize and sub + 1 < table[i]): # sub + 1 is use sub 
                    table[i] = sub + 1
    return table[amount] 

f = open("lab4/test_case/4.3.txt","r")  
coins = []
amount = int(f.readline())
a = f.readline().strip().split(" ")
for i in a:
    coins.append(int(i))
f.close()
coinsLength = len(coins) 

print("Minimum coins required is ",minCoins(coins, coinsLength, amount))