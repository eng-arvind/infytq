from  itertools import permutations
s = input()
l = list(s)
p = permutations(l)
for i in list(p):
    print(''.join(i))