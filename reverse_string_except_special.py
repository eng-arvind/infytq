import re
s = input()
l = re.findall("[a-zA-z0-9]",s)
l.reverse()

for i in range(len(s)):
    if s[i].isalpha() or s[i].isdigit():
        pass
    else:
        l.insert(i,s[i])

m_s =''.join(l)
print(m_s)
