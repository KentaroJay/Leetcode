from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses: List[str] = []
        def generate(numLeft: int, numRight: int, generatedParentheses: List[str]):
            if numLeft == 0 and numRight == 0:
                parentheses.append("".join(generatedParentheses))
                return
            if numLeft > 0:
                generatedParentheses.append("(")
                generate(
                    numLeft - 1,
                    numRight,
                    generatedParentheses,
                )
                generatedParentheses.pop()
            if numLeft < numRight:
                generatedParentheses.append(")")
                generate(
                    numLeft,
                    numRight - 1,
                    generatedParentheses,
                )
                generatedParentheses.pop()
        generate(n, n, [])
        return parentheses


if __name__ == "__main__":
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(2) == ["(())", "()()"]
