from collections import deque

N = int(input().strip())

datas = []
for i in range(N):
    temp = list(input().split())
    datas.append(temp)

# VPS인지 판정하는 함수
def VPS(data):
    if data[0] == ')':
        return False
    
    queue = deque()
    for d in data:
        queue.append(d)
    
    left = 0
    while queue:
        temp = queue.popleft()
        if temp == '(':
            left += 1
        # 오른쪽이 나오면 짝 맞춰보기
        if temp == ')':
            left -= 1
            if left == 0:
                continue
            else:
                for _ in range(left):
                    temp2 = queue.popleft()
                    if temp2 == ')':
                        left -= 1
                        if left == 0:
                            break
                    else:
                        return False
    
    if left == 0:
        return True
    else:
        return False


for i in range(N):
    if VPS(datas[i]):
        print("YES")
    else:
        print("NO")