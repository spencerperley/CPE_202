
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def pairs(self):
        for i in self.hash_table:
            if i:
                for j in i:
                    yield j

    def keyLook(self,key):
        for i,val in enumerate(self.hash_table[key%self.table_size]):
            if val[0]==key:
                return key%self.table_size , i
            
        return key%self.table_size , None


    def insert(self, key, value):
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        def noDInsert(mTup):
            self.hash_table[mTup[0]%self.table_size].append(mTup)

        if key < 0:
            raise ValueError

        

        place , duplicate = self.keyLook(key)
        if duplicate==None:
            self.num_items+=1

            if self.load_factor()> 1.5:
                old = [i for i in self.pairs()]
                self.hash_table = [[]]*(self.table_size*2+1)
                self.table_size = len(self.hash_table)

                for i in old:
                    self.hash_table[i[0]%self.table_size].append(i)

            if self.hash_table[place]:
                self.num_collisions += 1
            self.hash_table[place].append((key,value))
        else:
            self.hash_table[place][duplicate] = (key,value)
        


        return


    def get_item(self, key):
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        major,minor=self.keyLook(key)
        if minor == None:
            raise LookupError
        return self.hash_table[major][minor][1]
        

    def remove(self, key):
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        major,minor=self.keyLook(key)
        if minor == None:
            raise LookupError
        self.num_items-=1
        return self.hash_table[major].pop(minor)



    def load_factor(self):
        """Returns the current load factor of the hash table"""
        return self.num_items/self.table_size

    def size(self):
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self):
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions

