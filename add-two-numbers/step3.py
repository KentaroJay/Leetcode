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
        return True if node1 is not None or node2 is not None else False

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        answer_pointer_node = ListNode()
        response_dummy = answer_pointer_node

        node1 = l1
        node2 = l2
        incremental = False
        while self.either_node_exists(node1, node2) or incremental:
            total_two_nodes = 1 if incremental else 0

            if node1 is not None:
                total_two_nodes += node1.val
                node1 = node1.next
            if node2 is not None:
                total_two_nodes += node2.val
                node2 = node2.next
            answer_pointer_node.next = ListNode(total_two_nodes % 10)
            incremental = True if total_two_nodes // 10 == 1 else False

            answer_pointer_node = answer_pointer_node.next

        return response_dummy.next
