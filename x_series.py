l = input().split(',')
l = [int(i) for i in l]
l.sort()
ln = len(l)
t_list = []
for i in range(ln):
    for x in range(i + 1, ln):
        f = l[i]
        s = l[x]
        fb = [f, s]
        for y in range(x + 1, ln):
            if f + s == l[y]:
                fb.append(l[y])
                f = s
                s = l[y]
        if len(t_list) < len(fb):
            t_list = fb
if len(t_list) > 2:
    print(t_list)
else:
    print("-1")
