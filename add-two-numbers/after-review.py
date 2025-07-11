from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def either_node_exists(
        node1: Optional[ListNode],
        node2: Optional[ListNode],
    ) -> bool:
        return node1 is not None or node2 is not None

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        answer_pointer_node = ListNode()
        response_dummy = answer_pointer_node

        node1 = l1
        node2 = l2
        carry = 0
        while self.either_node_exists(node1, node2) or carry == 1:
            sum_vals = carry

            if node1 is not None:
                sum_vals += node1.val
                node1 = node1.next
            if node2 is not None:
                sum_vals += node2.val
                node2 = node2.next
            answer_pointer_node.next = ListNode(sum_vals % 10)
            carry = sum_vals // 10

            answer_pointer_node = answer_pointer_node.next

        return response_dummy.next
