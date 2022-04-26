

class Node:
    def __init__(self,val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

    def insert(self,val):
        self.next = Node(val,self,self.next)
        self.next.next.prev = self.next
    def remove(self,block=False):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self.val if not block else None
        

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val
    
    # def __repr__(self):
    #     return str(self.val)    


class OrderedList:
    def __init__(self):
        """construnctor takes nothing and returns an empty list with two sentry nodes"""

        self.head = Node(None)
        self.tail = Node(None,self.head)
        self.head.next = self.tail
        self.current= None
        self.length = 0
        

    def __repr__(self) -> str:
        """ print out the list in the same maner as a python list """  
        temp = [x for x in self.iterate()]
        return str(temp)
    
    def iterate(self , forward = True): # i did not know how to do the iterator magic method when I wrote this but this works
        """generator to iterate over the list. yeilds the value of the
         current node every time it is called. takes one argument that
          dictates starting position"""
        if forward:
            self.current = self.head.next
            while not self.current == self.tail:
                yield self.current.val 
                self.current = self.current.next
        else:
            self.current = self.tail.prev
            while not self.current == self.head:
                yield self.current.val
                self.current = self.current.prev


    # def search(item):
    #     for i in 

    def is_empty(self):
        """returns true if the list is empty"""
        return not self.length
    def size(self):
        """returns size of the list"""
        return self.length
    

    def search(self,item , forward = True):
        """iterates over the list and returns
         the index of the item that is being 
         searched for or -1 if it is not in the list
         takes an item that is being searched for as
          well as boolean that dictates the direction of the search"""
        index = 0
        for i in self.iterate(forward):
            if i == item:
                return index 
            index+= 1
            
        return -1


    def search_forward(self,item):
        """searches the list in the forward direction for the item.
         Returns true if the item is in the list and false otherwise."""
        return self.search(item) >= 0
    def search_backward(self,item):
        """searches the list in the backward direction for the item.
         Returns true if the item is in the list and false otherwise."""
        return self.search(item,False) >= 0
    def index(self,item):
        """searches the list in the forward direction for the item.
         Returns the index of the item if the item is in the list and -1 otherwise."""
        return self.search(item)
    def remove(self,item):
        """searches the list in the forward direction for the item and removes the item from the list."""
        self.search(item)
        self.current.remove()
        self.length-=1

    def pop(self, pos = -1):
        """returns and removes the item at the given index or the last item if no idex is given"""
        if pos == -1:
            self.length-=1
            return self.tail.prev.remove()
        if self.length/2>=pos:
            index = 0
            for i in self.iterate():
                if index == pos:
                    self.length-=1
                    return self.current.remove()

                index += 1
            self.length-=1
            return self.current.val
        else:
            index = self.length-1
            for i in self.iterate(False):
                if index == pos:
                    self.length-=1
                    return self.current.remove()

                index -= 1
            self.length-=1
            return self.current.val

    # def pop(self):
    #     return self.tail.prev.val



    def add(self,item):
        '''Adds an item to the list in the appropriate possition
            takes any integer'''
        if not isinstance(item,int):
            raise TypeError("Only integers are allowed")
        if self.is_empty():
            self.head.insert(item)
            self.length +=1
            return
        
        for val in self.iterate():
            if val > item:
                self.current.prev.insert(item)
                self.length +=1
                return
        self.current.prev.insert(item)
        self.length +=1
        
       

if __name__ == '__main__': 
    # a = OrderedList()
    # b = []
    # for i in range(0,100):
    #     x = randint(0,100)
    #     a.add(x)
    #     b.append(x)
    # b.sort()
    # print(str(b)==str(a))
    # c = 80
    # print(a.pop(c))
    # print(b[c])
    # b.remove
    # print(a)

    # print(a.size())

    a = OrderedList()
    for i in range(0,10):
        a.add(i+3)
    a.remove(5)
    a.remove(8)
    print(a)