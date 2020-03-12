m = int(input())
matrix = [list(map(int, input().split())) for i in range(m)]
flag = False
for i in range(0, m - 1):
    for j in range(0, m - 1):
        d1 = str(matrix[i][j])
        d2 = str(matrix[i][j + 1])
        d3 = str(matrix[i + 1][j])
        d4 = str(matrix[i + 1][j + 1])
        d1_sum = 0
        d2_sum = 0
        d3_sum = 0
        d4_sum = 0
        for k in d1:
            d1_sum = d1_sum + int(k)
        for k in d2:
            d2_sum = d2_sum + int(k)
        for k in d3:
            d3_sum = d3_sum + int(k)
        for k in d4:
            d4_sum = d4_sum + int(k)
        if d1_sum!=0 and d2_sum!=0 and  d3_sum!=0 and d4_sum!=0:
            if int(d1) % d1_sum == 0 and d1_sum!=0 and int(d2) % d2_sum == 0
                    and int(d3) % d3_sum == 0 and int(d4) % d4_sum == 0:
                print(d1, d2)
                print(d3, d4)
                flag = True
if not flag:
    print("-1")

