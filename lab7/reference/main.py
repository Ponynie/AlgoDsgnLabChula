import flws
inp = flws.getInput("lab7/test_case/test.txt",True)
a = flws.apsp(inp[0])
weight = flws.getAnswerNoise(inp[0],inp[1],a)
path = flws.getAnswerPath(inp[0],inp[1],a)
for x in range(len(inp[1])): print(inp[1][x][0]+1,inp[1][x][1]+1,":",weight[x],path[x])