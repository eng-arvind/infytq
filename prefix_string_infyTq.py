s = input()
n=len(s)
for i in range(len(s)//2,0,-1):
    prefix = s[0:i]
    suffix = s[n-i:n]
    if prefix == suffix:
        print(i)


