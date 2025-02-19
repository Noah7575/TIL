import sys
input = sys.stdin.readline

S = input().strip()

sorted_S = sorted(S)

sum = 0
for i in sorted_S:
    if (i <= '9') and (i >= '0'):
        sum += int(i)
    else:
        print(i, end = '')

print(sum)