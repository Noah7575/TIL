import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def solution(x, y, N):
    color = paper[x][y]
    half = N // 2
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(x, y, half)
                solution(x + half, y, half)
                solution(x, y + half, half)
                solution(x + half, y + half, half)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))