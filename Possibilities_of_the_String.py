from itertools import permutations

st=input()
length=len(st)
for i in range(1,length+1):
    for j in permutations(st,i):
        print(''.join(j))