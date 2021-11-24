def to_postfix (infix):
    """Convert infix to postfix"""
    optstack = []
    result = []
    ops = ['*', '/', '-', '+', '^']
    operator = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': 3, ')': 3}
    for x in infix:
        if x not in operator.keys():
            result.append(x)
        elif len(optstack) == 0 and x in ops:
            optstack.append(x)
        elif (x in ops and (operator[x] > operator[optstack[-1]] 
            or optstack[-1] == '(')):
            optstack.append(x)
        elif x in ops:
            while (operator[x] <= operator[optstack[-1]] 
                and optstack[-1] != '('):
                if (x == '^' and optstack[-1] == '^'):
                    break
                result.append(optstack.pop())
                if len(optstack) == 0:
                    break
            optstack.append(x)
        elif x == '(':
            optstack.append(x)
        elif x == ')':
            while optstack[-1] != '(':
                result.append(optstack.pop())
            optstack.pop()
            
    for x in reversed(optstack):
        result.append(x)
    result = ''.join(result)
    return result


if __name__ == '__main__':
    if to_postfix("2+7*5") == "275*+":
        print("OK")
    if to_postfix("3*3/(7+1)") == "33*71+/":
        print("OK")
    if to_postfix("5+(6-2)*9+3^(7-1)") == "562-9*+371-^+":
        print("OK")
    if to_postfix("(5-4-1)+9/5/2-7/1/7") == "54-1-95/2/+71/7/-":
        print("OK")
    if to_postfix("1^2^3") == "123^^":
        print("OK")