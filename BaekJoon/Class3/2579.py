import sys
input = sys.stdin.readline

N = int(input().strip())
stairs = [int(input().strip()) for _ in range(N)]

dp = [-1] * (N + 1)

result = stairs[N]

