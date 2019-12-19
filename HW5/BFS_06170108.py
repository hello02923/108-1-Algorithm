from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue=[s]
        seen = [s]##一開始要先放
        while queue:##先進先出
            vertex=queue.pop(0)##把第一個拿出來
            for w in self.graph[vertex]:##
                if w not in seen:
                    queue.append(w)
                    seen.append(w)
        return seen


    def DFS(self, s):
        stack=[s]
        seen=[]##
        while stack:##先進後出
            vertex=stack.pop()
            seen.append(vertex)
            for w in self.graph[vertex]:##
                if w not in seen:
                    stack.append(w)
                    
        return seen


