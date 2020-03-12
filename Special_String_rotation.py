import re

def square(nm):
    k = str(nm)
    sm = 0
    for i in k:
        sm = sm + int(i) * int(i)
    return int(sm)
s = input()

s_l = s.split(',')
for i in s_l:
    s1_l = i.split(':')
    word = s1_l[0]
    num = int(s1_l[1])
    total = square(num)
    if total % 2 == 0:
        word = word[-1] + word[0:-1]
    else:
        word = word[2:] + word[0:2]
    print(word, end=" ")
