from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generatedParentheses: List[str] = []
        def generate(numOpenBrackets: int, numCloseBrackets: int, parentheses: List[str]):
            if numOpenBrackets == numCloseBrackets == 0:
                generatedParentheses.append("".join(parentheses))
                return
            if numOpenBrackets > 0:
                parentheses.append("(")
                generate(numOpenBrackets - 1, numCloseBrackets, parentheses)
                parentheses.pop()
            if numCloseBrackets > numOpenBrackets:
                parentheses.append(")")
                generate(numOpenBrackets, numCloseBrackets - 1, parentheses)
                parentheses.pop()
        generate(n, n, [])
        return generatedParentheses


if __name__ == "__main__":
    solution = Solution()
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(2) == ["(())", "()()"]
