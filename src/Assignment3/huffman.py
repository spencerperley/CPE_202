from cgitb import reset


class HuffmanNode:
    def __init__(self, char_ascii, freq):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right
    
    def __repr__(self) -> str:
        return (f"ansii: {self.char_ascii} freq: {self.freq}")

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def leaves(self, prevCode = ''):
        '''generator to recursively iterate over the leaves of the tree and return the associated code and ansii character'''
        
        if self.left or self.right:
            yield from self.left.leaves(prevCode + '0')
            yield from self.right.leaves(prevCode + '1')
        
        else:
            yield prevCode , self.char_ascii


            

        




                

def comes_before(a, b):
    """Returns True if node a comes before node b, False otherwise"""
    if a.freq < b.freq:
        return True

    elif (a.freq == b.freq) and (a.char_ascii < b.char_ascii):
        return True

    else:
        return False


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    new = HuffmanNode(min(a.char_ascii,b.char_ascii),a.freq + b.freq)
    if a < b:
        new.right=b
        new.left=a
    else:
        new.right=a
        new.left=b
    return  new

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    charFq = [0]*256
    with open(filename,"r",newline='') as file:
        for line in file:
            for char in line:
                charFq[ord(char)] += 1
        return charFq



def create_huff_tree(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    freqSort = sorted([HuffmanNode(index,val) for index,val in enumerate(freq_list) if not val==0])
    def create(hufList):
        if len(hufList)==1:
            return hufList[0]
        else:
            
            temp = combine(hufList[0],hufList[1])
            hufList.pop(0)
            hufList.pop(0)
            hufList.append(temp)
            temp = sorted(hufList)
            return create(temp)
    return create(freqSort)


        
        

def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    code = [""]*256
    for val, ancii in node.leaves():
        code[ancii]=val
    return code

def create_header(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    out = []
    for index ,val in enumerate(freq_list):
        if not val == 0:
            out.append(f"{index} {val}")
    return ' '.join(out)


def huffman_encode(in_file, out_file):
    
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""

    freq = cnt_freq(in_file)
    head = create_header(freq)

 

    with open(out_file,"w",newline='') as file:
        if len(head)==0:
            return
            
        
        elif head.count(" ") == 1:

            file.write(head)
            return
        else:
            code = create_code(create_huff_tree(freq))
            result=''
            with open(in_file,"r",newline='') as input:
                for line in input:
                    for char in line:
                        result += code[ord(char)]
                file.write(head + '\n')
                file.write(result)


huffman_encode("testEmpty.txt",'testoutmulti.txt')



