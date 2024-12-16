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

    def pop(self) -> Any:
        # 스택에서 데이터 팝
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        # 피크: 꼭대기 데이터 관찰
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        # 스택 비우기
        self.ptr = 0

    def find(self, value: Any) -> Any:
        # 스택에서 value 찾아 인덱스 반환
        for i in range(self.ptr -1, -1, -1):
            # (시작, 끝, 간격)
            if self.stk[i] == value:
                return i # 검색 성공
        return -1 # 검색 실패

    def count(self, value: Any) -> int:
        # 스택에 있는 value의 개수 반환
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                cnt += 1
        return cnt

    def __contains__(self, value: Any) -> bool:
        # 스택에 value가 있는지 확인
        return self.count(value) > 0
        # count는 문자의 개수를 세줌(이터러블에서)

    def dump(self) -> None:
        if self.is_empty():
            print("스택이 비어 있습니다. ")
        else:
            print(self.stk[:self.ptr])
            # 리스트 처음부터 끝까지

    