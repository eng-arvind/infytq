s = input()
def validator(s):
    stack = []
    count = 0
    for b in s:
        if b == '(' or b == '{' or b == '[':
            stack.append(b)
            count += 1
            continue
        if len(stack) == 0:
            return 0
        x = stack.pop()
        if b == ')' and x == '(':
            count += 1
        elif b == '}' and x == '{':
            count += 1
        elif b == ']' and x == '[':
            count += 1
        else:
            return count + 1
    if len(stack) == 0:
        return 0
    else:
        return count + 1


print(validator(s))
