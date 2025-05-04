from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input().strip())

data = list(map(int, input().split()))
temp = list(set(data))
S = sorted(temp)
result = []

for d in data:
    result.append(bisect_left(S, d))

for r in result:
    print(r, end = ' ')