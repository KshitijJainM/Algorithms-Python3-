import networkx as nx
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint

class Graph: 

    def __init__(self): 

        self.graph = defaultdict(list) 
 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
 
    def DFSUtil(self, v, visited): 
  
        visited[v] = True
        print(v, end = ' ') 
   
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    def DFS(self, v): 
  
        visited = [False] * (len(self.graph)) 
  
        self.DFSUtil(v, visited) 

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
    p.addEdge(a,b)
k=int(input("Enter the starting vertex : "))
print ("Following is Depth First Traversal of "+str(k)) 
p.DFS(k)

G = nx.Graph()
G.add_edges_from(l1)
nx.draw_networkx(G)
plt.show()

