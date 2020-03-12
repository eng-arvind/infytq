s = input()
s1 = s.split(" ")
s2 = str()
for i in s1:
    s2 = s2 + "".join(reversed(i)) + " "
print(s2)
