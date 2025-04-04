import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

target = deque([int(input().strip()) for _ in range(N)])

stack = []
result = []
next = 1

for n in range(1, N+1):
    if n != target[0]:
        stack.append(n)
        result.append("+")
    else: # 같으면 pop 시작
        stack.append(n)
        result.append("+")

        while stack:
            p = stack.pop()
            if p == target[0]:
                target.popleft()
                result.append("-")
            else:
                stack.append(p)
                break

if not target:
    for r in result:
        print(r)
else:
    print("NO")



