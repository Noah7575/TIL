import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

max_num = -1000000
min_num = 1000000

for i in range(N):
    if max_num <= num_list[i]:
        max_num = num_list[i]

    if min_num >= num_list[i]:
        min_num = num_list[i]

print(f'{min_num} {max_num}')