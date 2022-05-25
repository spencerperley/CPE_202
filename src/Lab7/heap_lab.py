from math import log


class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                       # empty heap

    def __repr__(self) -> str:
        return str(self.heap)

    # def prt(self):
    #     hight = int(log(self.num_items,2))+1
    #     width=hight*2*4
    #     basis = ["1"]*width
    #     Levels = [["".join(basis)]]*(hight)
    #     gen = (self.heap[i+1] for i in range(self.num_items))
        
    #     for i,val in enumerate(gen): 
    #         Levels[int(log(i+1))][int(log(i+1))]

            

    def children(self,i,includeIndex = False):
        return [val if not includeIndex else (index,val) for index,val in [(i*2,self.left(i),),(i*2+1,self.right(i))] if not val == None]

    def safe(self,i):
        if i > self.capacity():
            return None
        else:
            return self.heap[i]

    def popEnd(self):
        
        self.num_items -=  1
        end , self.heap[self.num_items + 1] = self.heap[self.num_items + 1], None
        return end


    def left(self,i):
        return self.safe(i*2) if i*2 <= self.num_items else None
    
    def right(self,i):
        return self.safe(i*2+1) if i*2+1 <= self.num_items else None
    
    def parrent(self,i):
        return self.heap[i//2] if not i == 1 else None

    def valid(self,i):
        b = ((not(self.left(i) == None)) or (self.right(i) == None))
        # return b == self.safe(i)
        return max(self.miniTraverse(i)) == self.safe(i) and b 

    

    def miniTraverse(self,i,includeIndex = False):
        for i,val in [(i,self.safe(i)),(i*2,self.left(i)),(i*2+1,self.right(i))]:
            if not val == None:
                yield val if not includeIndex else (i,val)


    def enqueue(self, item):
        """inserts "item" into the heap
        Returns True if it is succsesfull and otherwise False if there is no room in the heap"""
        if self.is_full():
            return False
        else:
            self.heap[self.num_items] = item
            self.perc_up(self.num_items)
            self.num_items+=1
        return True

    def peek(self):
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        return(self.heap[1])

    def dequeue(self):
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        top,self.heap[1] = self.heap[1],self.popEnd()
        self.perc_down(1)
        return top

        
        

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        return self.heap[1:self.num_items+1]

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        
        newLength = len(alist)
        

        if newLength >= len(self.heap):
            return False

        self.num_items = newLength

        for index,val in enumerate(alist):
            self.heap[index+1]=val

        for i in range((newLength//2),0,-1):
            self.perc_down(i)

        return True
        


    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.safe(1)==None
            

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return not self.safe(self.capacity())==None

    def capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap)-1
    
    def size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if self.valid(i):
            return
        pos,temp = max(self.children(i,True),key=lambda a:a[1])
        (self.heap[i],self.heap[pos]) = (temp,self.heap[i])
        self.perc_down(pos)

            


    def perc_up(self,i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        if not self.parrent(i)==None:
            if self.parrent(i) < self.safe(i):
                (self.heap[i],self.heap[i//2])=(self.parrent(i),self.safe(i))
                self.perc_up(i//2)

        

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        save = self.num_items

        for i in range(self.num_items):
            temp = self.dequeue()
            self.heap[self.num_items+1] = temp
        self.num_items = save
        return self.contents()

# a = MaxHeap(30)
# a.build_heap([1,3,5,4,3,2,34,2,3,5,4,3,2,34,2,3,5,4,3,2,34,2,3,5,4,3,2,34,2])
# print(a)
# a.prt()


