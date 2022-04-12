# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    '''returns a list of string permutations of the origanal strings orderded acording to when the each character apears in the string'''
    if len(str_in) == 1: #If the string contains a single character return a list containing that string
        return [str_in]
    else:
        added_perms = []
        for letter in str_in: # loop through each character 
            perms = perm_gen_lex(str_in.replace(letter,'')) # remove said char and generate all permutations of the smaller string
            for perm in perms:
                added_perms.append(letter + perm) # add the permutations to the char

        return added_perms

print(perm_gen_lex('abcd'))
