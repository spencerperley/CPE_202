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

    def __str__(self):
        return ({!r}, {!r}.format(self.value, str(self.rest)))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    pass

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist):
    pass

#temp = ["Yellow", ["abc", ["$7.25"]]]
temp = ["Yellow", "abc", "$7.25", "lime", "42", "Ethan"]
print(repr(temp))
print(temp)
mylist = Node("dog", [])
mylist = Node("cat" , mylist)
mylist = Node("fish", mylist)
print(mylist)
print(repr(mylist))
print(str(mylist))