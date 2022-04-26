class TreeNode:
    def __init__(self,key):
        self.parrent = None
        self.left = None
        self.right = None
        self.key = key
        self.data = None
        self.size = 1

    def __next__(self):
        if not self.left == None:
            return self.left
        elif not self.right == None:
            return self.right
        else:
            return self.parrent

    def __iter__(self):
        ptr = self
        while not ptr == None:
            yield ptr
            ptr = ptr.__next__()


    def inOrder(self):
        ptr = self
        for i in range(self.size):
            yield 
            ptr = ptr.
        pass

    def preOrder(self):
        pass

    def postOrder(self):
        pass
        
    


    def insert(self,key):
        if key > self.key:
            if self.right == None:
                self.right = TreeNode(key)
                return
            else:
                self.right.insert()
        else:
            if self.left == None:
                self.left = TreeNode(key)
                return
            else:
                self.left.insert()

    def print_levels(self):


            

class BinarySearchTree:
    
    def insert(self,newKey):
        pass
