s = input()
l = s.split(',')
for i in l:
    l_st = i.split(':')
    word = l_st[0]
    num = l_st[1]
    sp = ''.join(num)
    ln = len(word)
    sk = str(ln)
    if sk in sp:
        print(word[ln - 1],end="")
    else:
        mn = 0
        for j in num:
            j = int(j)
            if mn < j < ln:
                mn = j
        if mn == 0:
            print("X",end="")
        else:
            print(word[mn - 1],end="")
