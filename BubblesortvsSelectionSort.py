# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:56:53 2020

@author: USER
"""

import time
from numpy.random import randint
import matplotlib.pyplot as plt



BSCount=[]
def bubblesort(arr):
    n=len(arr)
    countbs=0
    for i in range(n):
        for j in range(0,n-i-1):
            countbs=countbs+1
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    BSCount.append(countbs)

SSCount=[]
def selectionsort(arr):
    n=len(arr)
    countss=0
    for i in range(n):
        min=i
        for j in range(i+1,n):
            countss=countss+1
            if arr[min]>arr[j]:
                min=j
        
        arr[i],arr[min]=arr[min],arr[i]
        
    SSCount.append(countss)
    
elements=[]
times_bs=[]
times_ss=[]

for i in range(1,11):
    a=randint(0,i*1000,1000*i)
    
    start=time.clock()
    bubblesort(a)
    end=time.clock()
    times_bs.append(end-start)
    
    
    st=time.clock()
    selectionsort(a)
    en=time.clock()
    times_ss.append(en-st)
    
    elements.append(len(a))


plt.xlabel('List Length: No of elements')
plt.ylabel('Time complexity of bubble and selection sort')
plt.plot(elements,times_bs,elements,times_ss)
plt.grid()
plt.legend(['Bubble sort','Selection Sort'],loc='upper left')
plt.show()

plt.xlabel('List length: No of Elements')
plt.ylabel('Time complexity of bubble sort')
plt.plot(elements,times_bs)
plt.grid()
plt.legend(['BubbleSort'],loc='upper left')
plt.show()

plt.xlabel('List Length: No of elements')
plt.ylabel('Time complexity of selection sort')
plt.plot(elements,times_ss)
plt.grid()
plt.legend(['Selection Sort'],loc='upper left')
plt.show()

plt.xlabel('List length: No of Elements')
plt.ylabel('No of comparisons of bubble sort')
plt.plot(elements,BSCount)
plt.grid()
plt.legend(['Bubble Sort'],loc='upper left')
plt.show()

plt.xlabel('List length: No of Elements')
plt.ylabel('No of comparisons of selection sort')
plt.plot(elements,SSCount)
plt.grid()
plt.legend(['Selection Sort'],loc='upper left')
plt.show()
















