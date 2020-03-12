import math
from itertools import permutations

n = input()
l = []
ln = len(n)
for i in range(ln):
    for j in range(i,ln):
        k = int(n[i:j+1])
        l.append(k)

l_set = list(set((l)))
l_set.sort()
for i in l_set:
    x = int(math.sqrt(i))
    if x*(x+1)==i:
        print(i,end=" ")
