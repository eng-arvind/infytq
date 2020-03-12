def p_balanced(exp):
    l = []
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            l.append(exp[i])
            continue
        if len(exp) == 0:
            return False
        if exp[i] == ')':
            x = l.pop()
            if x == '{' or x == '[':
                return False
        elif exp[i] == '}':
            x = l.pop()
            if x == '(' or x == '[':
                return False
        elif exp[i] == ']':
            x = l.pop()
            if x == '{' or x == '(':
                return False
    if len(l):
        return True
    else:
        return False


if __name__ == "__main__":
    exp1 = "{[()]{}{[()()]()}"
    if p_balanced(exp1):
        print("Balanced")
    else:
        print("Not balanced")
