from collections import defaultdict 
  
class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s): 
        queue=[s]
        seen = [s]
        while queue:
            vertex=queue.pop()
            for w in self.graph[vertex]:
                if w not in seen:
                    queue.append(w)
                    seen.append(w)
        return seen


    def DFS(self, s):
        stack=[s]
        seen=[]
        while stack:
            vertex=stack.pop()
            seen.append(vertex)
            for w in self.graph[vertex]:
                if w not in seen:
                    stack.append(w)
                    
        return seen


