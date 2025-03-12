from collections import deque
import sys
input = sys.stdin.readline

# 데이터 입력
queue = deque()
while True:
    temp = input().strip()
    if temp == '0':
        break
    else:
        queue.append(temp)

# 판정 출력
while queue:
    a = queue.popleft()
    temp_b = list(reversed(a))
    b = "".join(temp_b)

    if a == '0':
        break
    elif a == b:
        print("yes")
    else:
        print("no")