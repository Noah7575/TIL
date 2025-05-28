import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [1] * (N)

for i in range(1, N):
    if A[i] > A[i-1]:
        dp[i] += dp[i - 1]
    else:
        continue

print(dp)