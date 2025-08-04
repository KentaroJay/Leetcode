from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                from_head = head
                from_collision = fast
                while from_head is not from_collision:
                    from_head = from_head.next
                    from_collision = from_collision.next
                return from_head
        return None
