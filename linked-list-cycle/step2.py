from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        for slow, fast in self.iterate_pointers(head):
            if fast.next is None:
                return False
            if fast == slow:
                return True
        return False

    def iterate_pointers(self, head: Optional[ListNode]):
        slow = head
        fast = head.next

        while fast is not None and slow is not None:
            yield slow, fast
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next
