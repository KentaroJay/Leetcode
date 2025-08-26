from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses: List[str] = []
        def generate(numLeft: int, numRight: int, generatedParentheses: str):
            if numLeft == numRight == 0:
                parentheses.append(generatedParentheses)
                return
            if numLeft > 0:
                generate(
                    numLeft - 1,
                    numRight,
                    generatedParentheses + "(",
                )
            if numLeft < numRight:
                generate(
                    numLeft,
                    numRight - 1,
                    generatedParentheses + ")",
                )
        generate(n, n, "")
        return parentheses


if __name__ == "__main__":
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(2) == ["(())", "()()"]
