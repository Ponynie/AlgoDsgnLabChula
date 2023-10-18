visitedOrder=[]
def reverseOrder(graph): #เก็บการเดินไปด้านหน้าโดยวื่งไปด้านหน้าแล้วเก็บตัวหลัง  
    global visitedOrder
    for i in graph.keys():
        if (i not in visitedOrder):
            fillOrder(i,graph)
    visitedOrder=[]
 
orderStack=[]
def fillOrder(v, graph):
    global orderStack 
    global visitedOrder
    visitedOrder.append(v)
    for i in graph[v]: 
        if i not in visitedOrder: 
            fillOrder(i,graph) 
    orderStack.append(v)
    


def graphTranspose(graph):
    trans_graph={}
    for i in graph.keys():
        trans_graph[i]=[]
    for i in graph.keys():
        for j in graph[i]:
            trans_graph[j].append(i)
    return trans_graph
    
def SCCs(graph):
    global orderStack
    reverseOrder(graph) #ไล่วื่งไปด้านหน้า
    stack=orderStack #stack เก็บการกลับหลัง
    Tgraph=graphTranspose(graph)
    visited=[] #travelled point
    SCCs_graph={} #SCCgraph
    SCCs_node=[] #group of points in SCCgraph
    while stack: 
        node=stack.pop() 
        if (node not in visited):
            temp_stack=[]   #สร้างเพื่อให้stackไม่ปนกัน
            temp_stack.append(node)
            new_SCC_node=[]
            while temp_stack: 
                subnode=temp_stack.pop() 
                if (subnode not in visited): 
                    visited.insert(0,subnode) #mark ว่าvisit
                    new_SCC_node.append(subnode) #สร้างgroup scc ใหม่
                    temp_stack.extend(Tgraph[subnode]) #ดูว่าsubnode นี้เชื่อมเป็นSCC ตัวไหน
                else:
                    continue
            SCCs_node.append(new_SCC_node) #เก็บ group ของ SCC ไว้
            
    for nodes in SCCs_node:
        SCCs_graph[tuple(nodes)]=[]
    for nodes in SCCs_node:
        for node in nodes: # nodesคือ 1 group ของSCC
            for dest in graph[node]:
                for chk_nodes in SCCs_node:
                    if (dest in chk_nodes and dest not in nodes):
                        SCCs_graph[tuple(nodes)].append(tuple(chk_nodes)) #สร้างSCC_graph
    orderStack=[]
    return SCCs_graph

            

def do_fill(filename):
    #create graph
    with open(filename,"r") as p:
        while (True):
            num_place,num_road=tuple(map(int,p.readline().split()))
            if ((num_place,num_road)==(0,0)):
                return
            graph={}
            for i in range(1,num_place+1):
                graph[i]=[]
            for i in range(num_road):
                from_,to_,road=tuple(map(int,p.readline().split()))
                if (road==1):
                    graph[from_].append(to_)
                elif (road==2):
                    graph[from_].append(to_)
                    graph[to_].append(from_)
               
            scc_graph=SCCs(graph) #create SCC graph   
            finish=False
            addline=0
            while(not finish):
                finish=True
                min_=1000
                min_lst=[]   #ตัวที่เก็บdfsครั้งแรกไล่ดูว่ามีจุดไหนเชื่อมกันได้น้อยสุด
                for i in scc_graph.keys():
                    stack=[i]
                    visited=[]
                    while (stack):
                        node=stack.pop()
                        if (node not in visited):
                            visited.append(node)
                            stack.extend(scc_graph[node])
                    if (len(visited)<min_):
                        min_=len(visited)
                        min_lst=visited
                        start_node=i
                max_=0
                include_node=0    # nodeที่เชื่อมกับจุดที่อยู่ในmin listได้มากสุด
                not_connected=False      # check max=0 :ตัวที่ไม่อยู่ในmin listเป็นจุดโดดเดี่ยวหรือเปล่า
                for i in scc_graph.keys():
                    cnt=0
                    temp_lst=[i for i in list(scc_graph.keys()) if (i not in min_lst)]
                    for j in temp_lst:
                        if (j in scc_graph[i]):
                            cnt+=1
                    if (cnt>max_):
                        not_connected=True
                        finish=False
                        max_=cnt
                        include_node=i
                              
                if (not not_connected):  
                    temp_lst=[i for i in list(scc_graph.keys()) if (i not in min_lst)]                    
                    for i in temp_lst:
                        addline=addline+1                                             
                        print (min_lst[-1],end="")
                        print ("==>",end="")
                        print (i)
                        scc_graph[min_lst[-1]].append(i)
                        finish=False
                #ตัวที่ไม่อยู่ในmin listเป็นจุดโดดเดี่ยว       
                if (include_node!=0 and not_connected):
                    addline=addline+1      
                    print (min_lst[-1],end="")
                    print ("==>",end="")
                    print (include_node)
                    scc_graph[min_lst[-1]].append(include_node)
            print("Number of addline : ",addline)        
            print ("------------------------------")

file_n="lab6/test_case/Extra6.5.txt"
do_fill(file_n)


