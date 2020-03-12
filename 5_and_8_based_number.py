s = input()
l = s.split(',')
firsti = l.index('5')
lasti = l.index('8')
num1 = l[0:firsti] + l[lasti+1:]
num2 = l[firsti:lasti+1]
sm1 = 0
for i in num1:
    sm1 += int(i)
sm2 = int(''.join(num2))
print(sm1+sm2)
