N = int(input().strip())
N_list = list(map(int, input().split()))

M = int(input().strip())
M_list = list(map(int, input().split()))

count_list = []
for i in range(M):
    temp = N_list.count(M_list[i])
    count_list.append(temp)

for i in range(M):
    print(count_list[i], end = ' ')
