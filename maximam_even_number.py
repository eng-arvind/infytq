import re

s = input()
l = re.findall("[0-9]", s)
l = list(set(l))
l.sort(reverse=True)
for i in range(len(l) - 1, 0, -1):
    if int(l[i]) % 2 == 0:
        x = l.pop(i)
        l.append(x)
        break
num = ''.join(l)
num = int(num)
if num % 2 == 0:
    print(num)
else:
    print("-1")
