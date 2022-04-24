class Node:
    def __init__(self,val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

    def insert(self,val):
        self.next = Node(val,self,self.next)
        self.next.next.prev = self.next

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val
    
    def __repr__(self):
        return str(self.val)    

class OrderedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None,self.head)
        self.head.next = self.tail
        self.current = self.head
        self.currentIndex = None
        self.length = 0
        return self

    def is_empty(self):
        return not self.length

    def insertAfterCurrent(self,val):
        self.current.insert(val)
        self.current = self.current.next
        self.currentIndex += 1

    def shiftCurrentUp(self):
        self.current = self.current.next
        self.currentIndex += 1
            

    def add(self,item):
        '''Adds an item to the list 
            takes any value that can be compared and returns noting '''

        if self.is_empty():
            self.head.next = Node(item,self.head,self.tail)
            self.current = self.head.next
            self.currentIndex = 0
            self.length = 1
            return
        
        
        while  item > self.current.value:
            if self.current.next == self.tail:
                self.insertAfterCurrent(item)
                return
            self.current = self.current.next
            self.currentIndex += 1
        self.current.insert(item)

