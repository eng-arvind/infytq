s = input()
l = list(s)
otp = ''
for i in l:
    i = int(i)
    if i % 2 != 0:
        otp += str(i * i)
print(otp[0:4])
