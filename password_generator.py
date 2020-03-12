l =input().split(",")
for i in l:
    t =i.split(':')
    word =t[0]
    num = t[1]
    ln =len(word)
    sk = str(ln)
    if sk in num:
        print(word[-1],end="")
    else:
        n=0
        for j in num:
            j = int(j)
            if n<j<ln:
                n=j
        if n==0:
            print("x")
        else:
            print(word[n-1],end="")
