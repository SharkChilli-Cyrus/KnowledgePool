# Python 3.x

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


if __name__ == "__main__":

    # --------------------------------------------------
    # Test 1
    symbol_string = "(asd(sda(sdw(s(sd(a))))"

    checker = Stack()
    continue_option = True
    index = 0

    while index < len(symbol_string) and continue_option:
        symbol = symbol_string[index]
        if symbol == "(":
            checker.push(symbol)
        elif symbol == ")":
            if checker.is_empty():
                continue_option = False
            else:
                checker.pop()
        
        index += 1
    
    if continue_option and checker.is_empty():
        print(True)
    else:
        print(False)


    # --------------------------------------------------
    # Test 2
    symbol_string = "{as{sd[sda(as(sd)sa)]}}" # '{'=>'}', '['=>']', '('=>')'
    
    match_dict = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    checker = Stack()
    continue_option = True
    index = 0

    while index < len(symbol_string) and continue_option:
        symbol = symbol_string[index]
        # update
        if symbol in "{[(": 
            checker.push(symbol)
        elif symbol in ")]}":
            if checker.is_empty():
                continue_option = False
            else:
                top_element = checker.pop()
                if match_dict[top_element] != symbol:
                    continue_option = False
        
        index += 1
    
    if continue_option and checker.is_empty():
        print(True)
    else:
        print(False)
    

    # --------------------------------------------------
    # Test 3
    # ^10: 233 = 2x10^2 + 3x10^1 + 3x10^0 = 10x(10x2+3)+3 ==> \10 ==> 3, 3, 2
    # ^2: 11101001 = 1x2^7 + 1x2^6 + 1x2^5 + 0x2^4 + 1x2^3 +0x2^2 + 0x2^1 + 1x2^0
    number = 42

    binary_stack = Stack()
    while number > 0:
        remainder = number % 2
        binary_stack.push(remainder)
        number = number // 2

    binary_string = ""
    while not binary_stack.is_empty():
        binary_string = binary_string + str(binary_stack.pop())
    
    print(binary_string)
