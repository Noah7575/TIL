import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [-1] * (N+1)

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp[0], dp[1], dp[2] = 0, 1, 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 10007)

