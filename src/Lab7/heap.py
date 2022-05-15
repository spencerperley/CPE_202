
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.__size = 0
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                       # empty heap

    def __repr__(self) -> str:
        return str(self.heap)

    def children(self,i,includeIndex = False):
        return [val if not includeIndex else (index,val) for index,val in [(i*2,self.left(i),),(i*2+1,self.right(i))] if not val == None]

    def safe(self,i):
        if i > self.capacity():
            return None
        else:
            return self.heap[i]
        


    def left(self,i):
        return self.safe(i*2)
    
    def right(self,i):
        return self.safe(i*2+1)
    
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
        Raises IndexError if there is no room in the heap"""
        if self.is_full():
            raise IndexError
        else:
            self.heap[self.__size] = item
            self.perc_up(self.__size)
            self.size+=1

    def peek(self):
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        return(self.heap[1])

    def dequeue(self):
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        
        newLength = len(alist)
        self.size = newLength

        for index,val in enumerate( None if i >= newLength else alist[i] for i in range(max(newLength, self.capacity()))):
            if index < self.capacity():
                self.heap[index+1] = val
            else:
                self.heap.append(val)

        for i in range((newLength//2),0,-1):
            self.perc_down(i)
        


    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return not self.safe(1)==None
            

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return not self.safe(self.capacity())==None

    def capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap)-1
    
    def size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.__size

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

        

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""

a = MaxHeap(8)
a.build_heap([6,4,3,10,3,9,2])
a.enqueue(11)
print(a)
