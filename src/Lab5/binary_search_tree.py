


class TreeNode:
    def __init__(self,key):
        self.level = 0
        self.parrent = None
        self.left = None
        self.right = None
        self.key = key
        self.data = None
        self.size = 1

    def __repr__(self):
        return f"[{self.key}, {self.level}]"


    def director(self,leftDom):
        if leftDom:
            return self.left
        else:
            return self.right

    def inorder(self, left = True):
        if not self.director(left) == None:
            yield from self.director(left).inorder(left)

        if not self.director(not left) == None:
            yield self
            yield from self.director(not left).inorder(left)
        else:
            yield self

    def insert(self,key, depth = 1):
        if key > self.key:
            if self.right == None:
                self.right = TreeNode(key)
                self.right.level=depth
                return
            else:
                self.right.insert(key,depth+1)
        else:
            if self.left == None:
                self.left = TreeNode(key)
                self.left.level=depth
                return
            else:
                self.left.insert(key,depth+1)

    def find_min(self):
        return next(self.inorder()).key
    def find_max(self):
        return next(self.inorder(False)).key

    def inorder_print_tree(self):
        for node in self.inorder():
            print(node.key, end = " ")

    def print_levels(self,left = True):
        for node in self.inorder(left):
            print(f"[{node.key}, {node.level}]", end = " ")
        print()


            

class BinarySearchTree:
    
    def insert(self,newKey):
        pass

a=TreeNode(5)
a.insert(1)
a.insert(6)
a.insert(5)
a.insert(7)
a.insert(8)
a.print_levels()
a.print_levels(False)
print(a.find_min())
print(a.find_max())

