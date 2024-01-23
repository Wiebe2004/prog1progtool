def sum_input():
    input_value = int(input("Enter integer: "))
    sum = input_value
    while input_value != 0:
        input_value = int(input("Enter integer: "))
        sum += input_value
    print(sum)


# sum_input()


def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# print(valid_parentheses(''))

def remove_backspaces(string):
    result = ""
    for k in string:
        if k == '\b':
            result = result[:-1]
        else:
            result += k
    print(result)
    
