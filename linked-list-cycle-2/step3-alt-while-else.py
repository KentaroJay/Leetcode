from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "ListNode | None"):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        else:
            return None
        assert head is not None
        assert fast is not None
        from_head = head
        from_collision = fast
        while from_head is not from_collision:
            from_head = from_head.next
            from_collision = from_collision.next
        return from_head
