s = input()
otp = ''
for i in range(1, len(s), 2):
    otp += str(int(s[i]) ** 2)
print(otp[0:4])
