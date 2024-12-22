# 8퀸 문제 알고리즘 구현하기

pos = [0] * 8
flagA = [False] * 8 # 행 중복 체크
flagB = [False] * 15 # 오른쪽 대각선 중복체크
flagC = [False] * 15 # 왼쪽 대각선 중복체크

def put() -> None:
    # 퀸의 위치 출력
    for i in range(8):
        for j in range(8):
            print("X" if pos[i] == j else "O", end = '')
        print()
    print()

def set(i: int) -> None:
    # i열의 알맞은 위치에 퀸을 배치
    for j in range(8):
        if(    not flagA[j]
           and not flagB[i + j]
           and not flagC[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flagA[j] = flagB[i + j] = flagC[i - j + 7] = True
                set(i + 1)
                flagA[j] = flagB[i + j] = flagC[i - j + 7] = False

set(0)
