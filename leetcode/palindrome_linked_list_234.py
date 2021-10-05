# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List, Deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        q: List = []
        if not head:
            return False

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        return q == q[::-1]

    # deque 이용
    def isPalindrome_use_deque(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()
        if not head:
            return False

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop() != q.popleft():
                return False

        return True
