import sys
input = sys.stdin.readline

N = int(input().strip())
data = []
for _ in range(N):
    data.append(int(input().strip()))
dp = [0] * (N)

if N == 1:
    print(data[0])
elif N == 2:
    print(data[0] + data[1])
else:
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(data[0] + data[2], data[1] + data[2])

    for i in range(3, N):
        dp[i] = max(
            dp[i-2] + data[i], 
            dp[i-1] + dp[i-3] + data[i]
        )
    
    print(max(dp))
