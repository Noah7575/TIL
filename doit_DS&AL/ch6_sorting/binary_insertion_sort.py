# 이진 삽입 정렬 알고리즘 구현

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    # 이진 삽입 정렬
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0     # 맨 앞 인덱스
        pr = i - 1 # 맨 끝 인덱스

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            break
        elif a[pc] < key: # 중간값이 key보다 작으면
            pl = pc + 1 # 검색 범위를 뒤쪽 절반으로
        else: # 중간값이 key보다 크거나 같으면
            pr = pc - 1 # 검색 범위를 앞쪽 절반으로
        
        if pl > pr:
            break

        if pl <= pr:
            pd = pc + 1
        else:
            pd = pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key