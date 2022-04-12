# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

    def __copy__(self):
        '''returns a new node that is a copy of self'''
        return Node(self.value,self.rest)

    # def __str__(self): 
    #     return ({!r}, {!r}.format(self.value, str(self.rest))) # this threw an error but it is not needed
    
    def addinfront(self,other):
        '''adds the value of other to the begining of the recursive list
            replaces any nodes in the form Node(None,None)'''
        if self.value == None:
            self.value  = other
        else:
            self.rest = self.__copy__()
            self.value  = other
        

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    if strlist: # catch None cases

        if not isinstance(strlist,Node): # catch any unexpected values
            raise TypeError
        
        if not strlist.rest: #return the value of the last node
            return strlist.value
        else: 
            return min(strlist.value,first_string(strlist.rest)) # compaire and return the lowest
    return None
    

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist):
    ''' returns a tuple with thre new string lists clasified by these rules: \n
         the first one with strings from the input list that start with a vowel,\n
         the second with strings from the input list that start with a consonant,\n
         the third with strings that don't start with an alpha character '''
        
    if strlist == None: # once the end of the recursive list is found
        return (Node(None,None),Node(None,None),Node(None,None)) # instantiate the tuple that gets passed up the recursive chain
    
    elif not isinstance(strlist,Node): # catch any unexpected values
        raise TypeError

    else: 
        myT = split_list(strlist.rest) 
        val = strlist.value
        if val:  # baced on the value of the first character return the respectively changed tuple 
            fc = val[0]
            if fc in 'aeiouAEIOU':
                myT[0].addinfront(val)
                return myT
            elif fc.isalpha():
                myT[1].addinfront(val)
                return myT
        myT[2].addinfront(val)
        return myT



#temp = ["Yellow", ["abc", ["$7.25"]]]
# temp = ["Yellow", "abc", "$7.25", "lime", "42", "Ethan"]
# print(repr(temp))
# print(temp)
# mylist = Node("dog",  None)
# mylist = Node("cat" , mylist)
# mylist = Node("fish", mylist)
# mylist.addinfront(1)
# print(mylist)
# print(repr(mylist))
# print(str(mylist))