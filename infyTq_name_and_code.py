input_string = input()
list_input = []
finalStr = ''
list_input = input_string.split(',')
for i in list_input:
    temp = i.split(':')
    name = temp[0]
    number = temp[1]
    length = len(name)
    ma_x = 0
    for digit in number:
        if int(digit) <= length:
            if ma_x < int(digit):
                ma_x = int(digit)
    if ma_x == 0:
        finalStr += 'X'
    else:
        finalStr += name[ma_x - 1]
print(finalStr)
