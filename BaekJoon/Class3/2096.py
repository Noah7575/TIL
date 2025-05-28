# 2096 내려가기
import sys
import copy
input = sys.stdin.readline

N = int(input().strip())
data = [list(map(int, input().split())) for _ in range(N)]

# 최대 dp
max_dp = copy.deepcopy(data)
for i in range(1, N):
    for j in range(3):
        if j == 0:
            max_dp[i][j] += max(max_dp[i-1][j], max_dp[i-1][j+1])
        elif j == 1:
            max_dp[i][j] += max(max_dp[i-1][j], max_dp[i-1][j+1], max_dp[i-1][j-1])
        else:
            max_dp[i][j] += max(max_dp[i-1][j], max_dp[i-1][j-1])

# 최소 dp
min_dp = copy.deepcopy(data)
for i in range(1, N):
    for j in range(3):
        if j == 0:
            min_dp[i][j] += min(min_dp[i-1][j], min_dp[i-1][j+1])
        elif j == 1:
            min_dp[i][j] += min(min_dp[i-1][j], min_dp[i-1][j+1], min_dp[i-1][j-1])
        else:
            min_dp[i][j] += min(min_dp[i-1][j], min_dp[i-1][j-1])


print(max(max_dp[N-1]), min(min_dp[N-1]))