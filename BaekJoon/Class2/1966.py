import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

def printer():
    N, M = map(int, input().split())
    # 중요도 입력
    temp = list(map(int, input().split()))
    print_queue = deque()
    # 큐: (번호, 중요도)
    for i in range(N):
        print_queue.append((i, temp[i]))
    # 큐 시뮬
    count = 1
    while print_queue:
        num, imp = print_queue.popleft()
        flag = 1 # 1이면 프린트(중요도가 제일 큼)
        # 플래그 판정
        temp_comp = list(print_queue)
        for t in temp_comp:
            if imp < t[1]:
                flag = 0
                break
        # 중요도가 가장 크다면 프린트한다
        if flag == 1:
            if num == M:
                break
            else:
                count += 1
        # 그렇지 않다면 다시 집어넣는다
        elif flag == 0:
            print_queue.append((num, imp))

    print(count)

for _ in range(T):
    printer()