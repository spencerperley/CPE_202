
import random
import time


# def selection_sort(alist):
#     count=0
#     for i in range(len(alist)-1):
#         count=count+i+1
#         minima = min(enumerate(alist[i:]), key = lambda a: a[1])
#         alist[i],alist[minima[0]+i] = minima[1],alist[i]
#     return count

def selection_sort(alist):
    '''uses the selection sort algorithm to sort the list and returns the number of comparisons'''
    return sum([0 if alist.insert(i,alist.pop(min(enumerate(alist[i:]), key = lambda a: a[1])[0]+i)) else i+1  for i in range(len(alist)-1)])

# def insertion_sort(alist):
#     return sum([0 if alist.insert(min(enumerate(alist), key = lambda a: a[1] < alist[i] )[0],alist.pop(i)) else 1 for i in range(1,len(alist))])

   
# def atist():
#     a = [5,7,3,7]
#     print(insertion_sort(a))
#     print(a)

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1235) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    temprands = randoms.copy()
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(sorted(temprands) == randoms)
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

