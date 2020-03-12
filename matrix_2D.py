# mat = [list(map(int,input().split())) for _ in range(row)]
row = int(input())
col = int(input())
a = [list(map(int,input().split()))for _ in range(row)]
b = [list(map(int,input().split())) for _ in range(row)]
c = [[str for i in range(col)] for _ in range(row)]
for i in range(row):
    for j in range(col):
        c[i][j] = a[i][j]+b[i][j]
print(c)