from typing import Optional


class ListNode:
    def __init__(self, x: int, next: "ListNode | None"):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        for slow, fast in self.iterate_pointers(head):
            if slow == fast:
                return True
        return False

    def iterate_pointers(self, head: ListNode):
        slow = head
        fast = head.next

        while slow and fast and fast.next:
            yield slow, fast
            slow = slow.next
            fast = fast.next.next

