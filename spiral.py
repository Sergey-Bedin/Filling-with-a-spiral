n, m = [int(c) for c in input().split()]
matrix = [[0] * m for _ in range(n)]
matrix[0][0] = 1

i, j, num, cnt = 0, 0, 1, 0
while True:

    while j < m - cnt - 1:
        num += 1
        j += 1
        matrix[i][j] = num

    if num >= m * n:
        break

    while i < n - cnt - 1:
        num += 1
        i += 1
        matrix[i][j] = num

    if num >= m * n:
        break

    while j > cnt:
        num += 1
        j -= 1
        matrix[i][j] = num

    if num >= m * n:
        break

    while i > cnt + 1:
        num += 1
        i -= 1
        matrix[i][j] = num

    cnt += 1
    if num >= m * n:
        break

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
