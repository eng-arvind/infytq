from  itertools import permutations
t =int(input())
for _ in range(t):
    s = input()
    l = list(s)
    lst = []
    p = permutations(l)
    for i in list(p):
        lst.append(''.join(i))
    lst.sort()
    for i in lst:
        print(i,"",end="")
    print()