from Stacks import Stack



def infix_to_postfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression """

    """Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    
    oprS = StackArray(30)


    validOpr = "+-*/^"
    def rank(oper):
        if oper in "+-":
            return 0
        elif oper in "*-":
            return 1
        elif oper in "^":
            return 2

    def isNum(s):
        dotfirst = True
        for i in s:
            if not (i.isdigit() or (i == "." and dotfirst)):
                return False
            if (i == "." and dotfirst):
                dotfirst = False

        return True


    oprRank = ("+-","*/","^","(")
    oprLeftDom = "+-"
    oprRightDom = "()"

    tokenList = infixexpr.split(" ")
    postfixList =  []

    for token in tokenList:
        if isNum(token):
            postfixList.append(token)
        elif len(token) == 1 and (token in validOpr):
            if token == ")":
                    pass
            else:
                if oprS.is_empty():
                    oprS.push(token)
                else:
                    prevRank = None
                    rank = None
                    for i in range(0,4):
                        if token in oprRank[i]:
                            rank = i
                        if oprS.peek


        else:
            raise ValueError
            

    return " ".join(postfixList)


def postfix_eval(postfixExpr):
    """  Evaluates a postfix expresion given as a string and returns its value as a float """
    vals = Stack()
def doMath(op, op1, op2):
    """  evaluates a single operator of
     a postfix expression and returns its value 
     if the """
    if op == "-":
        return op1-op2
    elif op == "+":
        return op1+op2
    elif op == "*":
        return op1*op2
    elif op == "/":
        return op1/op2
    elif op == "^":
        return op1**op2
    else:
        raise ValueError
def postfix_valid(postfixexpr):
    """ Purpose """
