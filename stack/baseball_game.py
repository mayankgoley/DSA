def score(s):
    stack = []

    for char in s:
        if char is 'C':
            stack.pop()
        
        elif char is 'D':
            stack.append(stack[-1] * 2)
        
        elif char is '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(char))
    
    return sum(stack)

char = ["5","2","C","D","+"]
print(score(char))