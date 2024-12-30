# 버블 정렬 알고리즘 구현(개선1)

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    # 셰이커 정렬
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            # 제일 작은 걸 앞쪽으로 보내는 정렬
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
            left = last
    
        for j in range(left, right):
            # 제일 큰 걸 뒤쪽으로 보내는 정렬
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
            right = last


if __name__ == "__main__":
    print("셰이커 정렬을 수행합니다.")
    num = int(input("원소 수: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    shaker_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")