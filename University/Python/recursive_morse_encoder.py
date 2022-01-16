class Tree:
    """A rooted binary tree"""
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

def is_empty(tree: Tree) -> bool:
        """Return True if and only if tree is empty."""
        return tree.root == tree.left == tree.right == None

def join(item: object, left: Tree, right: Tree) -> Tree:
    """Return a tree with the given root and subtrees."""
    tree = Tree()
    tree.root = item
    tree.left = left
    tree.right = right
    return tree

EMPTY = Tree()
H = join('H',EMPTY,EMPTY)
V = join('V',EMPTY,EMPTY)
F = join('F',EMPTY,EMPTY)
L = join('L',EMPTY,EMPTY)
P = join('P',EMPTY,EMPTY)
J = join('J',EMPTY,EMPTY)
B = join('B',EMPTY,EMPTY)
X = join('X',EMPTY,EMPTY)
C = join('C',EMPTY,EMPTY)
Y = join('Y',EMPTY,EMPTY)
Z = join('Z',EMPTY,EMPTY)
Q = join('Q',EMPTY,EMPTY)
S = join('S',H,V)
U = join('U',F,EMPTY)
R = join('R',L,EMPTY)
W = join('W',P,J)
D = join('D',B,X)
K = join('K',C,Y)
G = join('G',Z,Q)
O = join('O',EMPTY,EMPTY)
I = join('I',S,U)
A = join('A',R,W)
N = join('N',D,K)
M = join('M',G,O)
E = join('E',I,A)
T = join('T',N,M)
MORSE = join('START',E,T)

#*My contribution starts here*

def encode_letter(tree : Tree, letter : str) -> str:
    """
    Takes the provided letter and encodes to MORSE code
    
    Function: encode_letter
    Inputs: tree, a tree structure representing Morse code, and letter, a single character string
    Preconditions: letter is not empty and is an upper case letter A..Z, tree is not empty.
    Output: code, a string.
    Postconditions: code is 0 characters long if the code was invalid, else consists of a single uppercase character corresponding to the Morse code given.
    """
    
    """
    if we have found the character specified by letter, return data in letter- we use the first char in the string 
    as letter is used to carry over data from previous recursions
    
    this will return the goal char plus the symbol representing the direction we found the char
    """
    
    if letter[0] == tree.root and "START" not in letter:
        return letter
     
    """
    This is my rather 'hacky' solution- it works for every possible character so it is a valid solution
    
    To my understanding, a recursive function has to utilize a function parameter in order to carry unique
    data over to further recursions of the function- as it didn't specify whether we could add further
    parameters, I decided to make do with utilizing what was here
    
    I'll be honest- I'm quite proud of this even though I'm aware there was probably a better, more efficient
    way to approach things! Regardless, it works.
    
    It uses pre-order traversal
    """
    
    # START being present in the letter means the function has recursed back to the top of the tree and will
    # thus hold the MORSE encoding of the original character
    if 'START' in letter and ('.' in letter or '-' in letter):
        return "".join([char for char in letter[::-1] if char in '.-'])
   
    # The requested preconditions- function will exit if letter is empty, the current tree is empty or
    # the specified character is not uppercase
    if (not (len(letter))) or (is_empty(tree)) or (not letter[0].isupper()): 
        return ""
    
    # travel left initially, saving the return value to a variable
    l_search = encode_letter(tree.left, letter)
    # if there was no luck searching left, search right instead
    if not l_search: r_search = encode_letter(tree.right, letter)
    
    # bool needed for the morse encoding block of our function- true if we've found the desired character
    is_found = True if l_search or r_search else False
    
    if is_found:
        # determine if the character was in a left subtree or a right subtree and append code with the corresponding dot or dash 
        code = tree.root + l_search + "." if l_search else tree.root + r_search + "-"
       
        # recurse with data from previous recursions until we reach the start of the tree and see evidence of our desired MORSE code
        # when we reach the start, simply return the results of the function, else continue recursion using the prepended tree.root in code
        if 'START' not in letter and '.' not in letter and '-' not in letter:
            return encode_letter(MORSE, code)
        else:
            return letter

# checking the function returns the morse string by storing the return value in var
var = encode_letter(MORSE, 'C')
print(var)
