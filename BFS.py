import networkx as nx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint


from collections import defaultdict 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        
        visited = [False] * (len(self.graph)) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            s = queue.pop(0) 
            print (s, end = " ") 
 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

p = Graph() 
l1=[]
n=int(input("Enter the number of edges : "))
for i in range(n):
    a, b = input("Enter edge "+str((i+1))+ " co-ordinates:").split() 
    a=int(a)
    b=int(b)
    #a=randint(0,100)
    #b=randint(0,100)
    l2=[a,b]
    l1.append(l2)
   # np.append(A, [[a,b]],axis = 0)
    p.addEdge(a,b)
k=int(input("Enter the starting vertex : "))
print ("Following is Breadth First Traversal of "+str(k)) 
p.BFS(k)

G = nx.Graph()
G.add_edges_from(l1)
nx.draw_networkx(G)
plt.show()


