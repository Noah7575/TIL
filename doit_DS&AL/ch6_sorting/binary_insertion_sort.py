# 이진 삽입 정렬 알고리즘 구현

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    # 이진 삽입 정렬
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0     # 맨 앞 인덱스
        pr = i - 1 # 맨 끝 인덱스

    