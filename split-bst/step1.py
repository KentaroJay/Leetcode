from typing import List, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: "None | TreeNode" = None
        self.right: "None | TreeNode" = None


class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int):
        if not root:
            return [None, None]
        
        if root.val <= target:
            # means there should be the split somewhere on the right side
            smaller, larger = self.splitBST(root.right, target)
            root.right = smaller
            return [root, larger]

        # means there should be the split somewhere on the left side
        smaller, larger = self.splitBST(root.left, target)
        root.left = larger  
        return [smaller, root]

