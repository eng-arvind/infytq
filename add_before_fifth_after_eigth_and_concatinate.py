l = input().split(',')
five_index =l.index('5')
eigth_index = l.index('8')
add_num = l[0:five_index]+l[eigth_index+1::]
between_num = int(''.join(l[five_index:eigth_index+1]))
sum_num=0
for i in add_num:
    sum_num+=int(i)
print(sum_num+between_num)