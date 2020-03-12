# input:3,2,6,5,1,4,8,9
# output:5168 -> (3+2+6+9)+5148
s = input()
l = s.split(',')
s1_index = l.index('5')
s2_index = l.index('8')
num1 = l[0:s1_index]
num1.extend(l[s2_index+1:])
sum_num1 = 0
for i in num1:
    sum_num1 += int(i)
print(sum_num1+int(''.join(l[s1_index:s2_index+1])))