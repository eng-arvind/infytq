t = int(input())
for i in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    sum = 0
    for j in range(n+1):
        s =''
        while j>0:
            s +=(str(j%k))
            j  = j//k
        sum += len(s)
    print(sum+1)

