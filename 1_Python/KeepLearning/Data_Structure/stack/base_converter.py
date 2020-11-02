from stack import Stack

def base_converter(digital_number, base):
    digits = "0123456789ABCDEF"

    result_stack = Stack()

    while digital_number > 0:
        rem = digital_number % base
        result_stack.push(rem)

        digital_number = digital_number // base
    
    result_string = ""
    while result_stack.is_empty() == False:
        result_string = result_string + digits[result_stack.pop()]
    
    return result_string


if __name__ == "__main__":
    print(base_converter(157, 16))