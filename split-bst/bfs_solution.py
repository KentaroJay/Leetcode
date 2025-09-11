"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
from typing import Optional, List, Tuple
from enum import Enum

class TreeType(Enum):
    SMALLER = "smaller"
    LARGER = "larger"

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        
        smaller_tree = None
        larger_tree = None
        queue = deque()
        
        if root.val <= target:
            smaller_tree = root
            self._enqueue_child(queue, TreeType.SMALLER, root, root.right, is_right=True)
        else:
            larger_tree = root
            self._enqueue_child(queue, TreeType.LARGER, root, root.left, is_right=False)
        
        while queue:
            current_tree, parent, node, is_right_child = queue.popleft()
            
            if self._should_move_to_smaller(node.val, target, current_tree):
                if current_tree == TreeType.LARGER:
                    parent.left = None
                smaller_tree = self._merge_trees(smaller_tree, node)
                self._enqueue_child(queue, TreeType.SMALLER, node, node.right, is_right=True)
                
            elif self._should_move_to_larger(node.val, target, current_tree):
                if current_tree == TreeType.SMALLER:
                    parent.right = None
                larger_tree = self._merge_trees(larger_tree, node)
                self._enqueue_child(queue, TreeType.LARGER, node, node.left, is_right=False)
                
            else:
                self._continue_traversal(queue, current_tree, node, node.val <= target)
        
        return [smaller_tree, larger_tree]
    
    def _should_move_to_smaller(self, val: int, target: int, current_tree: TreeType) -> bool:
        return val <= target and current_tree == TreeType.LARGER
    
    def _should_move_to_larger(self, val: int, target: int, current_tree: TreeType) -> bool:
        return val > target and current_tree == TreeType.SMALLER
    
    def _continue_traversal(self, queue: deque, tree_type: TreeType, node: TreeNode, is_smaller: bool) -> None:
        if is_smaller and node.right:
            queue.append((tree_type, node, node.right, True))
        elif not is_smaller and node.left:
            queue.append((tree_type, node, node.left, False))
    
    def _enqueue_child(self, queue: deque, tree_type: TreeType, parent: TreeNode, 
                       child: Optional[TreeNode], is_right: bool) -> None:
        if child:
            queue.append((tree_type, parent, child, is_right))
    
    def _merge_trees(self, root: Optional[TreeNode], subtree: TreeNode) -> TreeNode:
        if not root:
            return subtree
        self._insert_subtree(root, subtree)
        return root
    
    def _insert_subtree(self, root: TreeNode, subtree: TreeNode) -> None:
        current = root
        while current:
            if subtree.val < current.val:
                if not current.left:
                    current.left = subtree
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = subtree
                    break
                current = current.right