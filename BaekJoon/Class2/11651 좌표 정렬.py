N = int(input())

data = []
# 데이터 입력받기
for i in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

data.sort(key = lambda x: (x[1], x[0]))

for i in range(N):
    print(data[i][0], data[i][1])