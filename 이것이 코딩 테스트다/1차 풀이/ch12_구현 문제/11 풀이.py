from collections import deque

K_queue = deque()
L_queue = deque()

N = int(input().strip())
K = int(input().strip())

# 사과좌표 입력받기
for _ in range(K):
    appl_x, appl_y = map(int(input().split()))
    K_queue.append((appl_x, appl_y))

L = int(input().strip())

# 방향전환 정보 입력받기
for _ in range(L):
    move_x, move_c = map(input().split())
    L_queue.append((int(move_x), move_c))


# 맵 생성
board = [[0] for _ in range(N)]
board[0][0] = 1

# 맵에 사과 표시
for _ in range(K):
    i, j = K_queue.popleft()
    board[i][j] = 99

# head 시작 좌표
head_row = 0
head_col = 0

# 좌표 이동: 우 하 좌 상(오른쪽 90도 회전)
move = {(0, 1), (1, 0), (0, -1), (-1, 0)}
move_index = 0

# 시간 카운트
time_count = 0

# 회전시간, 회전방향 카운트
direction = L_queue.popleft()

while True:
    # 회전 시간이 된 경우
    if time_count == direction[0]:
        if direction[1] == 'D': # 오른쪽 90도 회전
            move_index += 1
        elif direction[1] == 'C': # 왼쪽 90도 회전
            move_index -= 1
            
        if move_index > 3:
            move_index = 0
        elif move_index < 0:
            move_index = 4
