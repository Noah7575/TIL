from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())

queue = deque()

# 1부터 N까지 넣는다
for i in range(1, N+1):
    queue.append(i)

while queue:
    # 큐에 1장만 있으면 바로 종료
    if len(queue) == 1:
        break
    # 맨 위 카드 버리기
    queue.popleft()
    # 버리고 나서 1장 남았으면 종료
    if len(queue) == 1:
        break
    # 그다음 카드를 빼서 맨 뒤에 넣는다
    temp = queue.popleft()
    queue.append(temp)

num = queue.popleft()
print(num)