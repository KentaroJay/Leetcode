from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses: List[str] = []
        def generate(numLeft: int, numRight: int):
            if numLeft == 0 and numRight == 0:
                yield "".join(parentheses)
                return
            if numLeft > 0:
                parentheses.append("(")
                yield from generate(
                    numLeft - 1,
                    numRight, 
                )
                parentheses.pop()
            if numLeft < numRight:
                parentheses.append(")")
                yield from generate(
                    numLeft,
                    numRight - 1,
                )
                parentheses.pop()
        return list(generate(n, n))


if __name__ == "__main__":
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(2) == ["(())", "()()"]
