from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])

    def Dijkstra(self, s): 
        
        nodes = [i for i in range(0,len(g.graph))]  # 所有節點
        visited=[]  # 已經到最短路徑的節點集合
        
        if s in nodes:
            visited.append(s)
            nodes.remove(s)
        else:
            return None
        
        distance={s:0}  # 記錄到各點距離
        dict = {str(s):0} #字典形式
        for i in nodes:
            distance[i]=g.graph[s][i]  #s開始到各點

        k=pre=s
        
        while nodes:
            mid_distance=float('inf')
            for v in visited:
                for d in nodes:
                    new_distance = g.graph[s][v]+g.graph[v][d] #再累積上去
                    if new_distance < mid_distance and g.graph[v][d]!=0:
                        mid_distance=new_distance
                        g.graph[s][d]=new_distance  # 更新
                        k=d
                        pre=v
            distance[k]=mid_distance  # 最短路徑
            # 
            visited.append(k)
            nodes.remove(k)
            
            
            for i in range (0,self.V):
                dict[str(i)] = distance[i]
        return dict
    
    
