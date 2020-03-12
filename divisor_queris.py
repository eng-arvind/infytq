from functools import reduce
n,m = input().split()
lst =list(map(int,input().split()))
n = int(n)
m = int(m)
k = 10**9 + 7
for t in range(m):
    p=0
    l,r = input().split()
    l = int(l)
    r = int(r)
    if l<0 or r>n:
        break
    p = reduce(lambda x,y : x*y,lst[l:r+1])
    print(p%k)
