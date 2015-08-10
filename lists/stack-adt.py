class Stack(object):
    """ A simple stack ADT with top as the end of a list """
    def __init__(self):
        self.items = []

    def __str__(self):
        return ("Stack of size: %d" % len(self.items))

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if self.isEmpty(): return None
        return self.items[-1]

def string_reverse(s):
    stack = Stack()
    rev = []
    for c in s: stack.push(c)
    while not stack.isEmpty():
        rev.append(stack.pop())
    return "".join(rev)

def match_paren(parens):
    """ returns true or false if parenthesis
    expression passed is matching"""
    stack = Stack()
    for b in parens:
        if b == "(":
            stack.push(1)
        else: # b == ")"
            if not stack.isEmpty():
                stack.pop()
            else:
                return False
    return stack.isEmpty()

def infix_to_postfix(infixexpr):
    prec = { '+': 2, '-': 2, '*': 3, '/': 3,'(': 1 } # denoting precedence
    operator_stack = Stack()
    operators = "+-*/()"
    output_list = []
    for token in infixexpr.split():
        if token not in operators:
            output_list.append(token)
        elif token == "(":
            operator_stack.push("(")
        elif token == ")":
            topToken = operator_stack.pop()
            while topToken != "(":
                output_list.append(topToken)
                topToken = operator_stack.pop()
        else: # an operator
            while (not operator_stack.isEmpty()) and \
                (prec[operator_stack.top()] >= prec[token]):
                output_list.append(operator_stack.pop())
            operator_stack.push(token)

    # tokens exhausted - empty out the stack
    while not operator_stack.isEmpty():
        output_list.append(operator_stack.pop())
    return " ".join(output_list)


if __name__ == "__main__":
    expr = ["A * B + C * D", "( A + B ) * C - ( D - E ) * ( F + G )"]
    for e in expr:
        print infix_to_postfix(e)
