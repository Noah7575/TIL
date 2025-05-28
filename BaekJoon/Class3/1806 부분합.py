# 1806 부분합

import sys
input = sys.stdin.readline

N, target = map(int, input().split())
arr = list(map(int, input().split()))

INF = int(10e9)
left = 0
result = INF
total = 0
length = INF

for right in range(N):
    total += arr[right]

    while total >= target:
        length = right - left + 1
        total -= arr[left]
        left += 1
        
    result = min(result, length)

if result == INF:
    print(0)
else:
    print(result)
