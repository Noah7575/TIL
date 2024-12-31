# 셸 정렬 알고리즘 구현

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    # 셸 정렬
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j = j - h
            a[j + h] = tmp
        h = h // 2

        