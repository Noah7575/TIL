import sys
input = sys.stdin.readline

N = int(input().strip())
datas = map(int, input().split())

cnt = 0

for data in datas: 
    flag = 1

    if data == 1:
        continue

    if data == 2:
        cnt += 1
        continue
    
    # 나누어 떨어진다면 합성수
    for i in range(2, data):
        if data % i == 0:
            flag = 0
            break
    
    if flag == 1:
        cnt += 1

print(cnt)
