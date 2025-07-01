def valid_parentheses(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or stack[-1] !=parentheses[char]:
                return False
            stack.pop()
    
    return not stack

s = '([{}])'
print(valid_parentheses(s))