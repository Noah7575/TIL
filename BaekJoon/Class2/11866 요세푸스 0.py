from collections import deque

N, K = map(int, input().split())

data = deque()
result = []
for i in range(1, N+1):
    data.append(i)


while data:
    data.rotate(-K+1)
    temp = data.popleft()
    result.append(temp)

print("<", end = '')

for i in range(len(result)-1):
    print(result[i], end = ', ')

print(result.pop(), end = '')

print(">", end = '')
        
    
