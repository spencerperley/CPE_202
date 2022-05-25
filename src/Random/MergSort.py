import random
import time


def merge(a,b):
    def puke(alist,i):
        while i < len(alist):
            yield alist[i]
            i+=1
    newList = []
    aPlace = 0
    bPlace = 0
    while aPlace < len(a) and bPlace < len(b):
        if a[aPlace] <= b[bPlace]:
            newList.append(a[aPlace])
            aPlace+=1
        else:
            newList.append(b[bPlace])
            bPlace+=1
    
    for i in puke(a,aPlace):
        newList.append(i)
    for i in puke(b,bPlace):
        newList.append(i)
    return newList




def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = mergeSort(alist[:mid])
        right = mergeSort(alist[mid:])

        return merge(left,right)
    
    else:
        return alist

        
# # Give the random number generator a seed, so the same sequence of 
# # random numbers is generated at each run
# random.seed(1235) 

# # Generate 5000 random numbers from 0 to 999,999
# randoms = random.sample(range(10000), 1000)
# insertrands = randoms.copy()
# temprands = randoms.copy()
# start_time = time.time() 
# comps = mergeSort(randoms)
# stop_time = time.time()
# # instart_time = time.time() 
# # incomps = insertion_sort(insertrands)
# # instop_time = time.time()
# print("merge")
# print(sorted(temprands) == comps)
# print( stop_time - start_time)
# # print("insertion sort")
# # print(sorted(temprands) == insertrands)
# # print(incomps, instop_time - instart_time)
print(mergeSort([13,12,2]))