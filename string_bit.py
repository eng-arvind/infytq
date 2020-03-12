t = int(input())
while t != 0:
    n = int(input())
    s = input()
    s = list(s)
    ct = s.count("1")
    tol = ct*(ct-1)
    print(tol//2)
    t -= 1
