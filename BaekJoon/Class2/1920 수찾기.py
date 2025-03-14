N = int(input().strip())
N_set = set(map(int, input().split()))

M = int(input().strip())
M_list = list(map(int, input().split()))

for i in range(M):
    if M_list[i] in N_set:
        print(1)
    else:
        print(0)
    
