m,= input()
m = int(m)
matrix = [list(map(int, input().split())) for i in range(m)]
if m < 4:
    print("-1")
    exit(0)
l = []
for i in range(0, m - 2):
    for j in range(0, m):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j]==matrix[i+3][j]:
            l.append(matrix[i][j])
for i in range(0, m):
    for j in range(0, m - 2):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2]==matrix[i][j+3]:
            l.append(matrix[i][j])
for i in range(0, m - 2):
    for j in range(m- 1, -1, -1):
        if i + j == m - 1:
            if matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2]==matrix[i+3][j-3]:
                l.append(matrix[i][j])

for i in range(0, m - 2):
    for j in range(0, m - 2):
        if i == j:
            if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2]==matrix[i+3][j+3]:
                l.append(matrix[i][j])

l.sort()
if len(l) == 0:
    print("-1")
else:
    print(l[0])
