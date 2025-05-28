# 백준 11660 구간합구하기 5
import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
# 표
data = [list(map(int, input().split())) for _ in range(N)]

result = []
def prefix(x1, x2, y1, y2):
    # 특수 케이스
    if x1 == y1 and x2 == y2:
        result.append(data[x1][x2])
        return 0

    temp = copy.deepcopy(data)
    # 각 줄별 합 구하기
    for i in range(x1, x2 +1):
        temp[i][y2] = sum(temp[i])
    # 전체합 구하기
    for i in range(x1, x2):
        temp[x2][y2] += temp[i][y2]
    result.append(temp[x2][y2])

for _ in range(M):
    x1, x2, y1, y2 = map(int, input().split())
    prefix(x1 -1, x2 -1, y1 -1, y2 -1)

print(result)