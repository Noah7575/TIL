from collections import deque

K_queue = deque()
L_queue = deque()

N = int(input().strip())
K = int(input().strip())

# 사과좌표 입력받기
for _ in range(K):
    appl_x, appl_y = map(int, input().split())
    K_queue.append((appl_x, appl_y))

L = int(input().strip())

# 방향전환 정보 입력받기
for _ in range(L):
    move_x, move_c = input().split()
    L_queue.append((int(move_x), move_c))


# 맵 생성
board = [[0] * (N + 1) for _ in range(N + 1)]
board[1][1] = 1

# 맵에 사과 표시
for _ in range(K):
    i, j = K_queue.popleft()
    board[i][j] = 99

# head 시작 좌표
head_x = 0
head_y = 0

# 좌표 이동: 우 하 좌 상(오른쪽 90도 회전)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
move_index = 0

# 시간 카운트
time_count = 0

# 회전시간, 회전방향 카운트
if L_queue:
    direction = L_queue.popleft()

while True:
    time_count += 1
    # 회전 시간이 된 경우
    if time_count == direction[0]:
        if direction[1] == 'D': # 오른쪽 90도 회전
            move_index += 1
        elif direction[1] == 'L': # 왼쪽 90도 회전
            move_index -= 1
        
        # 다음 회전
        if L_queue:
            direction = L_queue.popleft()

        if move_index > 3:
            move_index = 0
        elif move_index < 0:
            move_index = 3

    # 이동시키며 사과 or 벽/몸통 체크
    nx = head_x + move[move_index][0]
    ny = head_y + move[move_index][1]

    # 벽 만나면 종료
    if nx > N or ny > N or nx <= 0 or ny <= 0:
        break

    # 몸통 만나면 종료
    if board[nx][ny] == 1:
        break

    # 사과를 만나는 경우
    if board[nx][ny] == 99:
        head_x, head_y = nx, ny
        board[head_x][head_y] = 1

    elif board[nx][ny] == 0: # 일반적인 경우
        board[nx][ny] = 1
        board[head_x][head_y] = 0
        head_x, head_y = nx, ny

print(time_count)

    

