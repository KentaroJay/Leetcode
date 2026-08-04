class Solution:
    GRAMMAR = {0: (0, 1), 1: (1, 0)}

    def kthGrammar(self, n: int, k: int) -> int:
        # Consider the bit array as a binary tree.
        # The parent node could be found at:
        # 1. i-1 th row
        # 2. (k + 1) // 2 position
        # suppose the child is located at k in ith row.
        if n == 1:
            return 0

        # Note that k is 1-indexed, k + 1 is to get the right
        # parent index
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return self.GRAMMAR[parent][(k - 1) % 2]

