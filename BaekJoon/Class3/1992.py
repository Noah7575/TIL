import sys
input = sys.stdin.readline

N = int(input().strip())
data = [list(map(int, list(input().strip()))) for _ in range(N)]


result = []

def sol(x, y, n):
    color = data[x][y]
    half = n // 2
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != data[i][j]:
                result.append('(')
                sol(x, y, half)
                sol(x, y + half, half)
                sol(x + half, y, half)
                sol(x + half, y + half, half)
                result.append(')')
                return
    if color == 0:
        result.append('0')
    else:
        result.append('1')

sol(0, 0, N)
print("".join(result))