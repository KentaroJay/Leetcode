from dataclasses import dataclass


@dataclass
class Node:
    index: int
    prev: "Node | None"
    next: "Node | None"

    def __init__(self, index: int):
        self.index = index
        self.prev = None
        self.next = None


class UniqueCharacterTracker:
    def __init__(self):
        self.char_to_node: dict[str, Node] = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, character: str, index: int):
        if character in self.char_to_node:
            node = self.char_to_node[character]
            self.remove_or_do_nothing(node)
            return
        node = Node(index)
        self.append(node)
        self.char_to_node[character] = node

    def remove_or_do_nothing(self, node: Node) -> None:
        if node.next is None and node.prev is None:
            return

        prev_node = node.prev
        next_node = node.next
        assert prev_node is not None
        assert prev_node is not None

        prev_node.next = node.next
        next_node.prev = node.prev
        node.next = None
        node.prev = None

    def append(self, node: Node) -> None:
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def is_empty(self) -> bool:
        return self.head.next.index == -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = UniqueCharacterTracker()
        for idx, char in enumerate(s):
            tracker.put(char, idx)
        if tracker.is_empty():
            return -1
        return tracker.head.next.index


if __name__ == "__main__":
    solution = Solution()
    assert 0 == solution.firstUniqChar("leetcode")
    assert 2 == solution.firstUniqChar("loveleetcode")
    assert -1 == solution.firstUniqChar("aaabb")
    assert -1 == solution.firstUniqChar("adaccdcda")
