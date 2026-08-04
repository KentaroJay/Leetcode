# n=4, k=3
#         1 2 3 4
#      n: 4 3 2 1
#      k: 3 2 1 1
# returns 1 1 0 0

class Solution:
    RULE = {0: (0, 1), 1: (1, 0)}

    def kthGrammar(self, n: int, k: int) -> int:
        # Consider the bit array as a binary tree.
        # The parent node could be found at:
        # 1. i-1 th row
        # 2. (k + 1) // 2 position
        # suppose the child is located at k in ith row.
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return self.RULE[parent][(k - 1) % 2]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.kthGrammar(2,1)
    breakpoint()

