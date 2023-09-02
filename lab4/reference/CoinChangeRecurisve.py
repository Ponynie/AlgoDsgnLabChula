
def CoinChange(result, amount, coins, currentCoin):

    if amount == 0: 
        way.append(result)
        return 
    
    if amount < 0:
        return 
    
    for i in range(currentCoin,len(coins)):
        if (coins[i] <= amount):
            CoinChange(str(coins[i]) + " " + result, amount - coins[i], coins, i)

f = open("4.13.txt","r")  
coins = []
amount = int(f.readline())
a = f.readline().strip().split(" ")
for i in a:
    coins.append(int(i))
f.close()           

result = ""
currentCoin = 0
way = []   

CoinChange(result, amount, coins, currentCoin)
print("Ways to make change =",len(way))
print(way)

  