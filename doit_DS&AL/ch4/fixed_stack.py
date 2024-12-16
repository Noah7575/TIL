# 고정 길이 스택 클래스 구현하기

from typing import Any

class FixedStack:
    # 고정 길이 스택 클래스

    class Empty(Exception):
        # 비어 있는 스택에서, 팝 또는 피크할 때 내보내는 예외처리
        # Exception 클래스를 상속
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        # 스택 초기화
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        # 스택에 쌓여 있는 데이터 개수를 반환
        return self.ptr

    def is_empty(self) -> bool:
        # 스택이 비어 있는지 파단
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    def push(self, value: Any) -> None:
        # 스택에 value를 푸시
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self)
    