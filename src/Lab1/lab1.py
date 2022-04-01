# CPE 202 Lab 1

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if type(int_list) == list:
      if int_list:
         max = int_list[0]
         for i in int_list:
            if i > max:
               max = i
         return max
      return None

   raise ValueError #seems like this should be a TypeError or some sort of null pointer error
   
   
   
         

# Maybe_List -> Maybe_List
def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if type(int_list) == list:
      if len(int_list) == 0:
         return []
      else:
         return reverse_rec(int_list[1:]) + [int_list[0]]
      
   raise ValueError #again seems like this should be a TypeError or some sort of null pointer error

# integer, integer, integer, Maybe_List -> integer
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if low > high:
      raise ValueError
   
   if type(int_list) == list:
      mid = (high - low)//2 + low
      if int_list[mid] == target:
         return mid
      
      elif high - low == 0:
         return None
      
      elif int_list[mid] > target:
         return bin_search(target, low, mid, int_list)
      
      elif int_list[mid] < target:
         return bin_search(target, mid+1, high, int_list)
      
      
   raise ValueError #again seems like this should be a TypeError or some sort of null pointer error