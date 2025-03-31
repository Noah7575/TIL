import sys
input = sys.stdin.readline

N = int(input().strip())

count = 0
while True:
    if N == 0:
        break
    elif N < 0:
        count = -1
        break
    elif N % 5 == 0:
        a = N // 5
        count += a
        N = 0
    else:
        N -= 3
        count += 1

print(count)