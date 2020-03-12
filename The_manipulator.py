s1 = input()
s2 = input()
l1 = list(s1)
l2 = list(s2)
for i in range(len(l1)):
    if l1[i] == '#':
        for j in range(i, -1, -1):
            if l1[j] != '#':
                a = ord(l1[j])
                a += 1
                a = chr(a)
                l1[j] = a
                break

for i in range(len(l2)):
    if l2[i] == '#':
        for j in range(i, -1, -1):
            if l2[j] != '#':
                a = ord(l2[j])
                a += 1
                a = chr(a)
                l2[j] = a
                break

s1 = ''
s2 = ''
for i in l1:
    if i != '#':
        s1 += i

for i in l2:
    if i != '#':
        s2 += i

print(s1,s2)

if s1 == s2:
    print("Yes")
else:
    print("No")
