import sys
input = sys.stdin.readline

T = int(input().strip())

def fashion():
    N = int(input().strip())
    # 옷 입력
    set_name_list = []
    for _ in range(N):
        cloth, kind = input().split()
        if kind not in set_name_list:
            kind = set()
            set_name_list.append(kind)
            kind.add(cloth)
        else:
            kind.add(cloth)

for _ in range(T):
    fashion()