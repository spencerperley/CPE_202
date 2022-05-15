
import random
import time


def selection_sort(alist):
    '''uses the selection sort algorithm to sort the list and returns the number of comparisons'''
    count=0
    for i in range(len(alist)-1):
        count=count+i+1
        minima = min(enumerate(alist[i:]), key = lambda a: a[1])
        alist[i] , alist[minima[0]+i] = minima[1],alist[i]
    return count

# def selection_sort(alist):
#     '''uses the selection sort algorithm to sort the list and returns the number of comparisons'''
#     return sum([0 if alist.insert(i,alist.pop(min(enumerate(alist[i:]), key = lambda a: a[1])[0]+i)) else i+1  for i in range(len(alist)-1)])




def insertion_sort(alist):
    '''uses the insertion sort algorithm to sort the list and returns the number of comparisons'''
    comps = 0
    for i in range(1,len(alist)):
        for j in range(i):
            comps+=1
            if alist[i-j] < alist[i-j-1]:
                (alist[i-j], alist[i-j-1]) = (alist[i-j-1] , alist[i-j])
            else:
                break
    return(comps)

   
def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1235) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 16000)
    insertrands = randoms.copy()
    temprands = randoms.copy()
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    # instart_time = time.time() 
    # incomps = insertion_sort(insertrands)
    # instop_time = time.time()
    print("selection sort")
    print(sorted(temprands) == randoms)
    print(comps, stop_time - start_time)
    # print("insertion sort")
    # print(sorted(temprands) == insertrands)
    # print(incomps, instop_time - instart_time)

if __name__ == '__main__': 
    main()

