from dataclasses import dataclass


@dataclass
class Node:
    index: int
    prev_node: "Node | None"
    next_node: "Node | None"

    def __init__(self, index: int):
        self.index = index
        self.prev_node = None
        self.next_node = None


class UniqueCharacterTracker:
    def __init__(self):
        self.character_to_node: dict[str, Node] = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def put(self, *, index: int, character: str):
        if character in self.character_to_node:
            node = self.character_to_node[character]
            self.remove_or_do_nothing(node)
            return
        node = Node(index)
        self.append(node)
        self.character_to_node[character] = node

    def remove_or_do_nothing(self, node: Node):
        if node.prev_node is None and node.next_node is None:
            return

        prev_node = node.prev_node
        next_node = node.next_node
        assert prev_node is not None
        assert next_node is not None

        prev_node.next_node = next_node
        next_node.prev_node = prev_node

        node.prev_node = None
        node.next_node = None

    def append(self, node: Node):
        prev_tail = self.tail.prev_node
        assert prev_tail is not None

        prev_tail.next_node = node
        node.prev_node = prev_tail

        self.tail.prev_node = node
        node.next_node = self.tail

    def is_empty(self):
        return self.head.next_node.index == -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = UniqueCharacterTracker()
        for index, character in enumerate(s):
            tracker.put(index=index, character=character)
        if tracker.is_empty():
            return -1
        return tracker.head.next_node.index


if __name__ == "__main__":
    solution = Solution()
    assert 0 == solution.firstUniqChar("leetcode")
    assert 2 == solution.firstUniqChar("loveleetcode")
    assert -1 == solution.firstUniqChar("aaabb")
    assert -1 == solution.firstUniqChar("adaccdcda")
