import re
s = input()
s_l = re.findall("[a-zA-Z1-2]",s)
s_l.reverse()
for i in range(len(s)):
    if (not s[i].isalpha() )and (not s[i].isdigit()):
        s_l.insert(i,s[i])
print(''.join(s_l))



