ms = "FIRSTCHARSTRING"
s = input()
l = list(s)
q = int(input())
ss = ''
for _ in range(q):
    r, n = input().split()
    n = int(n)
    if r == "R":
        for i in range(n):
            t = l.pop()
            l.insert(0,t)
    if r == "L":
        for i in range(n):
            t = l.pop(0)
            l.append(t)
    ss += l[0]
if ss.upper() in ms:
    print("YES")
else:
    print("NO")
