

import time 
from numpy.random import randint 
import matplotlib.pyplot as plt 
  
  
CountHS=[]
c=0
def heapify(arr, n, i): 
    global c
    largest = i
    l = 2 * i + 1     
    r = 2 * i + 2    
    if l < n and arr[i] < arr[l]: 
        c=c+1
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        c=c+1
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
   
        heapify(arr, n, largest) 
 
def heapSort(arr): 
    n = len(arr) 
  
     
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0) 
        
elements=[]
times_HS=[]

for i in range(1,11):
    a=randint(0,i*10,10000*i)
    start=time.clock()
    heapSort(a)
    end=time.clock()
    times_HS.append(end-start)
    CountHS.append(c)
    
    elements.append(len(a))
  
plt.xlabel('List length:No of elements')
plt.ylabel('Time Complexity of Heap Sort')
plt.plot(elements,times_HS)
plt.grid()
plt.legend(['Heap Sort'],loc='upper left') 
plt.show()

plt.xlabel('List length:No of elements')
plt.ylabel('Number of comparisons')
plt.plot(elements,CountHS)
plt.grid()
plt.legend(['Heap Sort'],loc='upper left') 
plt.show()
