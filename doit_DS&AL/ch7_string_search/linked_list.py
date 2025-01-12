# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    # 연결 리스트용 노드 클래스

    def __init__(self, data: Any = None, next: Node = None):
        # 초기화
        self.data = data
        self.next = next # 뒤쪽 포인터


class LinkedList:
    # 연결 리스트 클래스

    def __init__(self) -> None:
        # 초기화
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드

    def __len__(self) -> int:
        # 노드 개수 반환
        return self.no
    
    
    def search(self, data: Any) -> int:
        # data와 값이 같은 노드를 검색
        cnt = 0
        ptr = self.head
        while ptr is not None: # 끝이 아닌 동안...
            if ptr.data == data: # 만약 같은 값을 찾으면...
                self.current = ptr # 주목 포인터에 ptr
                return cnt # 찾은 노드의 위치 반환
            cnt += 1 # 다르면 다음 노드로
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        # 연결 리스트에 data가 포함되어 있는지 확인
        return self.search(data) >= 0
            # 0 이상이면 찾은 거니깐 True, -1이면 False
    
    def add_first(self, data: Any) -> None:
        # 맨 앞에 노드를 삽입
        ptr = self.head # 이전 머리 노드
        self.head = self.current = Node(data, ptr)
        # 새로운 머리 노드
        self.no += 1

   def add_last(self, data: Any):
        # 맨 끝에 노드를 삽입
        if self.head is None: # 리스트가 비어 있으면
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next # 끝에 갈 때까지...
            ptr.next = self.current = Node(data, None)
            self.no += 1


    def remove_first(self) -> None:
        # 머리 노드를 삭제하기
        if self.head is not None: # 리스트가 비어 있지 않으면
             self.head = self.current = self.head.next
        self.no -= 1