import time
from numpy.random import randint
import matplotlib.pyplot as plt

LScount=[]
def linearSearch(arr_num):
    num=len(arr_num)
    key=randint(0,100000)
    j=1
    countLS=0
    
    for i in range(0,num):
        countLS = countLS + 1
        if arr_num[i]==key:
            j=1
            break
    
    if j==1:
        print("Element found")
    else:
        print("Element not found")
        
    LScount.append(countLS)
    
BScount=[]
def binarySearch(alist):
    n=len(alist)
    item=randint(0,100000)
    first=0
    count=0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first+last)//2
        count = count + 1
        if alist[midpoint] == item:
            found=True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
            
    if found==True:
        print("Element found")
    else:
        print("Element not found")
    
    BScount.append(count)
    
elements = []
times_LS = []
times_BS = []

for i in range (1,11):
    a=randint(0,1000*i,10000*i)

    start=time.clock()
    linearSearch(a)
    end=time.clock()
    times_LS.append(end-start)
    a=sorted(a)
    start=time.clock()
    binarySearch(a)
    end=time.clock()
    times_BS.append(end-start)
    
    elements.append(len(a))
    
plt.xlabel('List Length: No of Elements') 
plt.ylabel('Time Complexity of LS and BS')
plt.plot(elements,times_LS,elements,times_BS)
plt.grid()
plt.legend(['Linear Search','Binary Search'],loc='upper left')
plt.show()
   
plt.xlabel('List Length: No of Elements') 
plt.ylabel('Time Complexity of LS ')
plt.plot(elements,times_LS)
plt.grid()
plt.legend('Linear Search',loc='upper left')
plt.show()


plt.xlabel('List Length: No of Elements') 
plt.ylabel('Time Complexity of BS ')
plt.plot(elements,times_BS)
plt.grid()
plt.legend('Binary Search',loc='upper left')
plt.show()


plt.xlabel('List Size: No of Elements') 
plt.ylabel('No. of comparisions of LS')
plt.plot(elements,LScount)
plt.grid()
plt.legend('Linear Search',loc='upper left')
plt.show()


plt.xlabel('List Size: No of Elements') 
plt.ylabel('No. of comparisions of BS')
plt.plot(elements,BScount)
plt.grid()
plt.legend('Binary Search',loc='upper left')
plt.show()