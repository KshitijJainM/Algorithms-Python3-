import time
from numpy.random import randint
import matplotlib.pyplot as plt

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:] 
        
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
  
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
elements=[]
times_ms=[]
for i in range(1,101):
    a=randint(0,i*1000,1000*i)
    
    start=time.clock()
    mergeSort(a)
    end=time.clock()
    times_ms.append(end-start)
    elements.append(len(a))
    
plt.xlabel('List Length: No of elements')
plt.ylabel('Time complexity of merge sort')
plt.plot(elements,times_ms)
plt.grid()
plt.legend(['Merge Sort'],loc='upper left')
plt.show()


