import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []

for _ in range(N):
    temp = list(input().strip())
    board.append(temp)

result = 9999

ex_col = M - 7
ex_row = N - 7

WB_line = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
BW_line = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

# 시작점 좌표 x, y
for x in range(ex_row):
    for y in range(ex_col):
        
        # 시작점 값 그대로 가져가는 경우
        change_count1 = 0
        # 시작점 바꾸고 가는 경우
        change_count2 = 0

        # 시작점의 값이 W인 경우
        if board[x][y] == 'W':
            # 8칸 내 좌표 i, j
            for i in range(8):
                for j in range(8):
                    # 시작점 값을 안 바꾸고 그대로 가는 경우
                    # i행이 짝수이면 WB 라인과 비교, 다르면 +1
                    if (i % 2) == 0 or i == 0: 
                        if board[x + i][y + j] != WB_line[j]:
                            change_count1 += 1
                    # i행이 홀수이면 BW 라인과 비교
                    if (i % 2) == 1:
                        if board[x + i][y + j] != BW_line[j]:
                            change_count1 += 1
                    # 시작점 값을 바꾸고 가는 경우
                    # i행이 짝수이면 BW 라인과 비교, 다르면 +1
                    if (i % 2) == 0 or i == 0: 
                        if board[x + i][y + j] != BW_line[j]:
                            change_count2 += 1
                    # i행이 홀수이면 WB 라인과 비교
                    if (i % 2) == 1:
                        if board[x + i][y + j] != WB_line[j]:
                            change_count2 += 1


        # 시작점의 값이 B인 경우
        if board[x][y] == 'B':
            # 8칸 내 좌표 i, j
            for i in range(8):
                for j in range(8):
                    # 시작점을 안 바꾸는 경우 
                    # i행이 짝수이면 BW 라인과 비교, 다르면 +1
                    if (i % 2) == 0 or i == 0: 
                        if board[x + i][y + j] != BW_line[j]:
                            change_count1 += 1
                    # i행이 홀수이면 WB 라인과 비교
                    if (i % 2) == 1:
                        if board[x + i][y + j] != WB_line[j]:
                            change_count1 += 1
                    # 시작점을 바꾸고 가는 경우
                    # i행이 짝수이면 WB 라인과 비교, 다르면 +1
                    if (i % 2) == 0 or i == 0: 
                        if board[x + i][y + j] != WB_line[j]:
                            change_count2 += 1
                    # i행이 홀수이면 BW 라인과 비교
                    if (i % 2) == 1:
                        if board[x + i][y + j] != BW_line[j]:
                            change_count2 += 1

        result = min(result, change_count1, change_count2)

print(result)




