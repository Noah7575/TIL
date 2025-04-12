import sys
input = sys.stdin.readline

N = int(input().strip())

data = [list(map(int, input().split())) for _ in range(N)]

result_1 = 0
result_2 = 0
result_3 = 0

def sol(x, y, N):
    global result_1, result_2, result_3
    third = N // 3
    colour = data[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if colour != data[i][j]:
                sol(x, y, third)
                sol(x, y + third, third)
                sol(x, y + third * 2, third)
                sol(x + third, y, third)
                sol(x + third, y + third, third)
                sol(x + third, y + third * 2, third)
                sol(x + third * 2, y, third)
                sol(x + third * 2, y + third, third)
                sol(x + third * 2, y + third * 2, third)
                return

    if colour == -1:
        result_1 += 1
    elif colour == 0:
        result_2 += 1
    elif colour == 1:
        result_3 += 1

    return

sol(0, 0, N)

print(result_1)
print(result_2)
print(result_3)
