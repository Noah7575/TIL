import sys
input = sys.stdin.readline

def add():
    N = int(input().strip())

    dp = [0] * (N+1)
    if N >= 4:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    elif N == 1:
        dp[1] = 1
    elif N == 2:
       dp[1], dp[2] = 1, 2
    elif N == 3:
       dp[1], dp[2], dp[3] = 1, 2, 4

    print(dp[N])

T = int(input().strip())

for _ in range(T):
    add()