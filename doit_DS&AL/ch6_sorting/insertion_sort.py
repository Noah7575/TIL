# 단순 삽입 정렬 알고리즘 구현

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    # 단순 삽입 정렬
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == "__main__":
    print("단순 삽입 정렬.")
    num = int(input("원소 수: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    insertion_sort(x)

    print("오름차순 정렬 완료.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")