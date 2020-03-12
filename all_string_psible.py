from itertools import permutations

s = input()
l = list(s)
p = list(permutations(l))
for i in p:
    print(''.join(i))
