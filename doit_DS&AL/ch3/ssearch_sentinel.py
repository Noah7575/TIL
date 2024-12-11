from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int :
    # key와 일치하는 원소 보초법으로 찾기
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True: 
        if a[i] == key:
            break
        i += 1
    # 원래 데이터인지 보초인지 판단
    # i 값이 len과 같으면 보초를 찾은 것
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    ky = int(input("검색할 값: "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("원소가 존재하지 않습니다.")
    else:
        print(f"검색값 위치: x[{idx}]")