test_list = ['cdab', 'gfeh', 'kjil']
#res = ["".join(sorted(j, reverse = i % 2)) for i, j in enumerate(test_list)]
#print(str(res))
for i,j in enumerate(test_list):
    if i%2 == 0:
        print(''.join(sorted(j)),end=" ")
    else:
        print(''.join(sorted(j,reverse=True)),end=" ")
