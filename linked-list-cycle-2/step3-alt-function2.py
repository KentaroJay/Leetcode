from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "ListNode | None"):
        self.val = x
        self.next = next


class Solution:
    def safeGetCollisionNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return fast
        return None

    def detectCycle(self, head: Optional[ListNode]):
        collision = self.safeGetCollisionNode(head)
        if not collision:
            return None
        from_head = head
        from_collision = collision
        while from_head is not from_collision:
            from_head = from_head.next
            from_collision = from_collision.next
        return from_head
