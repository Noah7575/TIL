# 행과 열에 퀸을 1개 배치하는 조합을 재귀적 나열

pos = [0] * 8
flag = [False] * 8

def put() -> None:
    # 각 열에 배치한 퀸의 위치 출력
    for i in range(8):
        print(f"{pos[i]:2}", end='')
    print()

def set(i: int) -> None:
    # i열의 알맞은 위치에 퀸을 배치
    for j in range(8):
        if not flag[j]: # j행에 퀸이 없을 때(즉 False일 때)
            pos[i] = j # 퀸(i, j)
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i + 1) # 다음열 퀸 배치
                flag[j] = False

set(0)
