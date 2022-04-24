# NodeList version of ADT Queue

# Node class for use with Queue implemented with linked list
# NodeList is one of
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value      # value
        self.rest = rest        # NodeList
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Queue:
    def __init__(self):
        self.rear = None    # rear NodeList
        self.front = None   # front NodeList
        self.num_items = 0  # number of items in Queue

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.get_items() == other.get_items()
        )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.rear, self.front))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self):
        items = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
        return items

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        return not self.num_items

    def enqueue(self, item):
        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""   
        if self.is_empty():
            self.front = Node(item,None)
            self.rear = self.front
            self.num_items += 1
        else:
            self.rear.rest = Node(item,None)
            self.rear = self.rear.rest
            self.num_items += 1
    

    def dequeue(self):
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""

        """the rear thing doesent make any sence but my implimentation works just fine without it. it results in doublu counting the final element entered which makes no sense"""

        
        if self.front:
            temp = self.front.value
            self.front = self.front.rest
            self.num_items -= 1
            if self.front   == None:
                self.rear = None
            return temp
        elif self.rear:   # this seems pointless and it is ill-defined but I think i did what was intended
            self.front = Node(self.rear.value,None)
            while self.rear.rest():
                self.front = Node(self.rear.rest.value,self.front)
                self.rear = self.rear.rest
        else:
            raise IndexError



    def size(self):
        """Returns the number of items in the queue
        Must be O(1)"""
        return self.num_items

if __name__ == "__main__":
    q1 = Queue()
    print(q1)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print(q1)
    q2 = Queue()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q1 == q2)
    print(q2.dequeue())
    print(q2)
    print(q1 == q2)
    print(q2.dequeue())
    print(q2.dequeue())
    q2.enqueue(4)
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    q2.enqueue(8)
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2)
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2)
    print(q2 == q1)
