# 2차원 리스트의 90도 회전
def rotate_a_matrix_by_90(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result

def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 회전시키면서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90(key) # 열쇠 회전
        # 한칸씩 이동시키며 확인한다
        # x와 y는 열쇠의 좌상단 꼭짓점
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    new_lock[x + i][y + i] += key[i][j]
                # 자물쇠에 열쇠가 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 열쇠 빼기
                for i in range(m):
                    new_lock[x + i][y + j] -= key[i][j]

    return False
