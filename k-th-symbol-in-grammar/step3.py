class Solution:
    GRAMMAR = {0: (0, 1), 1: (1, 0)}

    def kthGrammar(self, n: int, k: int) -> int:
        # The bit array is a binary tree.
        # The parent node is found at (k + 1) // 2 in the n - 1 row.
        if n == 1:
            return 0

        # Note that k is 1-indexed and (k + 1) is needed
        # to get the right parent index
        # ex.) k = 3 then you want to get the parent at 2
        #      (3 + 1) // 2 will give 2
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return self.GRAMMAR[parent][(k - 1) % 2] 
