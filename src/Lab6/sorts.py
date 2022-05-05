from cgitb import enable
import random
import time


def selection_sort(alist):
    count=0
    for i in range(len(alist)-1):
        count+=i+1
        minima = min(enumerate(alist[i:]), key = lambda a: a[1])
        alist[i],alist[minima[0]+i] = minima[1],alist[i]
    return count


# def insertion_sort(alist):
#     alist = [insert() for i in range(len(alist)-1)]
   
def atist():
    a = [5,7,3,7]
    print(selection_sort(a))
    print(a)

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    atist()

