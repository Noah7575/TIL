# 책의 풀이

import sys
input = sys.stdin.readline

n = int(input().strip())
x, y = 1, 1
plans = input().strip().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

print(x, y)
