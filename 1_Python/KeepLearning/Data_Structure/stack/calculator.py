from stack import Stack

"""
    A+B*C
==> (A+(B*C))
==> Prefix: +A*BC
==> Postfix: ABC*+
"""

def add_space(expression):
    # only consider 0-9 number
    new_expression = ""

    if " " not in expression:
        for character in expression:
            new_expression += character + " "
        # for character in expression:
        #     if character == "(":
        #         new_expression += character
        #     elif character == ")":
        #         new_expression = new_expression.rstrip(" ") + character + " "
        #     else:
        #         new_expression += character + " "

    else:
        new_expression = expression
    
    new_expression = new_expression.rstrip(" ")
    return new_expression


def to_postfix(expression):
    expression = add_space(expression)

    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    opt_stack = Stack()
    postfix_list = []
    token_list = expression.split(" ")

    for token in token_list:
        if token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            opt_stack.push(token)

        elif token == ")":
            top_token = opt_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = opt_stack.pop()
        
        else:
            while (opt_stack.is_empty() == False) and (prec[opt_stack.peek()] >= prec[token]):
                postfix_list.append(opt_stack.pop())

            opt_stack.push(token)
        
    while opt_stack.is_empty() == False:
        postfix_list.append(opt_stack.pop())
    
    postfix_string = " ".join(postfix_list)
    return postfix_string


def do_math(opt, num1, num2):
    if opt == "*":
        return num1 * num2
    elif opt == "/":
        return num1 / num2
    elif opt == "+":
        return num1 + num2
    else:
        return num1 - num2


def calculate_postfix(postfix_string):
    num_stack = Stack()
    token_list = postfix_string.split(" ")

    for token in token_list:
        if token in "0123456789":
            num_stack.push(int(token))
        else:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            result = do_math(token, num1, num2)
            num_stack.push(result)
    
    return num_stack.pop()




if __name__ == "__main__":

    expression = u"(6+2)*3-(5-4)*(6+7)"
    # test add_space
    print(add_space(expression))

    # test to_postfix
    print(to_postfix(expression))
    postfix_expression = to_postfix(expression)

    # test calculator
    print(calculate_postfix(postfix_expression))