s = input()
l = len(s)
for i in range(l // 2, 0, -1):
    prefix = s[0:i]
    suffix = s[l - i:l]
    if prefix == suffix:
        print(i)
        break
