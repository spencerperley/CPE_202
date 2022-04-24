
from Stacks import *


def isNum(s : str) -> bool: 
    """parses trough a string and valaidates whether or not it is a valid number
    meaning it has only one '.' and has only digets other than that"""
    """Signature: takes a string and returns true if it is a valid number """
    dotfirst = True
    for i in s:
        if not (i.isdigit() or (i == "." and dotfirst)):
            return False
        if (i == "." and dotfirst):
            dotfirst = False

    return True




def infix_to_postfix(infixexpr : str) -> str:
    """Converts an infix expression to an equivalent postfix expression """

    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
    oprS = StackArray(30)


    validOpr = ["+","-","*","/","^","(",")"]

    def rank(oper : str) -> int :
        """ used to evaluate what to pop from the operator stack """
        """Signature:  takes a valid operator as a string and returns its order of operation rank as a int with special classification for parrenthasis"""
        if oper in "+-":
            return 0
        elif oper in "*-":
            return 1
        elif oper in "^":
            return 2
        elif oper in "()":
            return -1


    tokenList = ["("] + infixexpr.split(" ") + [")"] # split the string and add parrenthisis to in for ease of use
    postfixList =  []

    for token in tokenList: # parse through each token and ither add it to the operator stack or add it to the 
        if isNum(token):
            postfixList.append(token)
        elif len(token) == 1 and (token in validOpr):
            if token == "(":
                oprS.push(token)
            elif token == ")":
                while not (oprS.peek() =="("):
                    postfixList.append(oprS.pop())
                oprS.pop()
            elif token == "^":
                while rank(token) < rank(oprS.peek()): # handel exponentiation
                    postfixList.append(oprS.pop())
                oprS.push(token)
            else:
                while rank(token) <= rank(oprS.peek()):
                    postfixList.append(oprS.pop())
                oprS.push(token)

        else: # error out if an operator is incorrect
            raise ValueError("invalid operator or number")

            

    return " ".join(postfixList)


def postfix_eval(postfixExpr : str) -> float :
    """  Evaluates a postfix expresion given as a string and returns its value as a float """
    """Signature : takes a posfix expression as a string and returns a float that is the result of the expression.
    raises ValueError if the expression is not valid"""
    vals = Stack()
    if postfix_valid(postfixExpr):

        tokenList = postfixExpr.split(" ")
        for token in tokenList:
            if token in "+-*/^":
                first = vals.pop()
                next = vals.pop()
                vals.push(str(doMath(token,next,first)))
            else:
                vals.push(token)
        return float(vals.pop())
    raise ValueError
 
    
def doMath(op : str, op1 : str, op2 : str) -> float :
    
    """  evaluates a single operator of
     a postfix expression and returns its value 
     if the operator is valid"""
    """Signature: takes an opperator and two operands as strings returns the result of the corisponding math opperation as a float"""

    op1num = float(op1)
    op2num = float(op2)
    if op == "-":
        return op1num-op2num
    elif op == "+":
        return op1num+op2num
    elif op == "*":
        return op1num*op2num
    elif op == "/":
        if op2num == 0: # handed undefined
            raise ValueError("devide by zero")
        return op1num/op2num
    elif op == "^":
        return op1num**op2num
    else: # unessassary but good to be safe
        raise ValueError
def postfix_valid(postfixexpr : str) -> bool:
    """takes a string seperated by spaces and determins if it is a valid postfix expression"""
    """Signature: takes a possible posfix expersion as a string seperated by spaces and returns true if it is a valid posfix expression and false otherwise"""
    if not postfixexpr:
        return False
    tokenList = postfixexpr.split(" ")
    numC = 0
    oprC = 0
    for token in tokenList: # parsese through each character and evaluatese whether it is a valid token and if has a valid placement given each operator takes two armumenmts
        if isNum(token):
            numC += 1
        elif (token in "+-*/^"):
            oprC += 1
        else:
            return False
        if not (numC > oprC):
            return False

    if numC == oprC+1:
        return True
    return False




