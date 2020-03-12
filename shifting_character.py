l = input().split(",")
for i in l:
    k =i.split(':')
    word = k[0]
    num = k[1]
    digit_sum=0
    for j in num:
        digit_sum+=(int(j)**2)
    if digit_sum%2==0:
        word= word[-2::]+word[0:len(word)-2]
    else:
        word = word[1::]+word[0]
    print(word,end=" ")

