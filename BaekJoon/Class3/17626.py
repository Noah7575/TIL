import sys
import math

input = sys.stdin.readline

N = int(input().strip())

count = 0
while N != 0:
    temp = math.floor(math.sqrt(N))
    N -= temp ** 2
    count += 1

print(count)