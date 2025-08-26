from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generatedParentheses: List[str] = []
        def generate(numUnclosedBracket: int, numRightBracket: int, parentheses: List[str]):
            if numRightBracket == 0:
                generatedParentheses.append("".join(parentheses))
                return
            if numUnclosedBracket > 0:
                parentheses.append(")")
                generate(
                    numUnclosedBracket - 1,
                    numRightBracket - 1,
                    parentheses,
                )
                parentheses.pop()
            if numUnclosedBracket < numRightBracket:
                parentheses.append("(")
                generate(
                    numUnclosedBracket + 1,
                    numRightBracket,
                    parentheses,
                )
                parentheses.pop()
        generate(0, n, [])
        return generatedParentheses


if __name__ == "__main__":
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(2) == ["()()", "(())"]
