from ast import Lambda
from tempfile import tempdir


class TreeNode:
    def __init__(self,key):
        self.level = 0
        self.parrent = None
        self.left = None
        self.right = None
        self.key = key
        self.data = None


    def __repr__(self):
        return f"[{self.key}, {self.level}]"

    def __bool__(self):
        if isinstance(self.key,int):
            return True
        else:
            return False


    def inorder(self, left = True):
        '''generator to recursively iterate over the tree in the inorder fasion. yeilds a TreeNode.
        if left is False the tree is iterated over in reverse'''
        def director(left):
            '''simple director for the inorder function that switches the direction based on a boolean value'''
            if left:
                return self.left
            else:
                return self.right
        if not director(left) == None:
            yield from director(left).inorder(left)

        yield self

        if not director(not left) == None:
            yield from director(not left).inorder(left)


    def insert(self,key, depth = 1):
        '''recursively iterates over the tree in order to insert the key into the proper place '''
        if key > self.key:
            if self.right == None:
                self.right = TreeNode(key)
                self.right.level=depth
                self.right.parrent=self
                return
            else:
                self.right.insert(key,depth+1)
        else:
            if self.left == None:
                self.left = TreeNode(key)
                self.left.level=depth
                self.left.parrent=self
                return
            else:
                self.left.insert(key,depth+1)
                
    def find_successor(self):
        '''returns the succesor node of the tree'''
        return next(self.inorder())

    def find_min(self):
        '''returns the min key'''
        return next(self.inorder()).key

    def find_max(self):
        '''returns the max key'''
        return next(self.inorder(False)).key

    def inorder_print_tree(self):
        for node in self.inorder():
            print(node.key, end = " ")
        print()

    def print_levels(self):
            
        for node in self.inorder():
            temp = node
            count = 0
            while not temp.parrent == None:
                temp = temp.parrent
                count+= 1
            node.level=count
        for node in self.inorder():
            print(f"[{node.key}, {node.level}]", end = " ")
        print()


            

class BinarySearchTree:

    def __init__(self,rootKey=None) -> None:
        if not rootKey == None:
            self.root = TreeNode(rootKey)
        else:
            self.root= rootKey

    def find(self,key):
        for node in self.root.inorder():
            if node.key == key:
                return True
        return False
    
    def delete(self,key):
        for node in self.root.inorder():
            if node.key == key:
                if node == self.root:
                    if node.left and node.right:    
                        replace = next(node.right.inorder())
                        
                        if replace.parrent == self.root:
                            self.root.right = replace.right
                        else:
                            replace.parrent.left = replace.right
                            if replace.parrent.left:
                                replace.parrent.left.parrent = replace.parrent
                        self.root.key = replace.key
                        self.root.data = replace.data

                            
                    elif (node.right == None) ^ (node.left == None):
                        self.root = node.left if node.left else node.right
                        self.root.parrent = None

                    else:
                        self.root = None




                elif node.left and node.right:
                    if node.parrent.left == node:
                        replace = next(node.right.inorder(False))
                        if node.right == replace:
                            node.right = replace.left
                        else:
                            replace.parrent.right = replace.left
                            if replace.parrent.right:
                                replace.parrent.right.parrent=replace.parrent

                        node.key = replace.key
                        node.data = replace.data
                    else:
                        replace = next(node.left.inorder(True))
                        if node.left == replace:
                            node.left = replace.right
                        else:
                            replace.parrent.left = replace.right
                            if replace.parrent.left:
                                replace.parrent.left.parrent=replace.parrent

                        node.key = replace.key
                        node.data = replace.data

                    # else:
                    #     replace = next(node.inorder())
                    #     replace.left = node.left
                    #     replace.right = node.right if not node.right == replace else None
                    #     node.parrent.right = replace
                        

                elif (node.right == None) ^ (node.left == None):
                    if node.parrent.left == node:
                        node.parrent.left = node.left if node.left else node.right
                        node.parrent.left.parrent = node.parrent
                    else:
                        node.parrent.right = node.left if node.left else node.right
                        node.parrent.right.parrent = node.parrent
                else:
                    if node.parrent.left == node:
                        node.parrent.left = None
                    else:
                        node.parrent.right = None
                return
        


    def insert(self,newKey):
        if self.root==None:
            self.root = TreeNode(newKey)
            return
        self.root.insert(newKey)

    def is_empty(self):
        return self.root == None

    def print_tree(self):
        self.root.inorder_print_tree()


    



if __name__ == '__main__': 
    a=BinarySearchTree(10)
    a.insert(3)
    a.insert(14)
    a.insert(15)
    a.insert(11)
    a.insert(13)
    a.insert(12)
    a.insert(16)
    a.insert(1)
    a.insert(7)
    a.insert(2)
    a.print_tree()
    a.delete(15)
    a.print_tree()
    a.delete(3)
    a.print_tree()
    a.delete(7)
    a.print_tree()
    a.delete(1)
    a.print_tree()
    a.delete(14)
    a.print_tree()



