# 나의 풀이
    # 답은 맞는 것 같은데 조건문이 너무많음

import sys
input = sys.stdin.readline

n = int(input().strip())
x, y = 1, 1
plans = input().strip().split()

count = len(plans)
for i in range(count):
    if (plans[i] == "R") and (y < n):
        y += 1
    elif (plans[i] == "L") and (y > 1):
        y -= 1
    elif (plans[i] == "U") and (x > 1):
        x -= 1
    elif (plans[i] == "D") and (x < n):
        x += 1
    else:
        continue

print(x, y)

