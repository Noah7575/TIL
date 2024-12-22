# 하노이의 탑 구현

def move(no: int, x: int, y:int) -> None: 
    # 원반 no개를 x기둥에서 y기둥으로 옮긴다
    if no > 1:
        move(no - 1, x, 6-x-y)
        # no - 1개 그룹을 중간 기둥으로 옮김

    print(f"원반 [{no}]를 {x}기둥에서 {y} 기둥으로 옮김")

    if no > 1:
        move(no - 1, 6-x-y, y)
        # no - 1개 그룹을 중간 기둥에서 끝 기둥으로 옮김

print("하노이의 탑.")
n = int(input("원반 개수: "))

move(n, 1, 3)