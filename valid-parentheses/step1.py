class Solution:
    OPEN = ['(', '{', '[']
    CLOSE = [')', '}', ']']
    VALID_CHARS = OPEN + CLOSE

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char not in self.VALID_CHARS:
                raise ValueError
            if char in self.OPEN:
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            recent = stack.pop()
            if recent == "(" and char == ")":
                continue
            if recent == "{" and char == "}":
                continue
            if recent == "[" and char == "]":
                continue
            return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    assert True is solution.isValid("[]")
    assert True is solution.isValid("()")
    assert True is solution.isValid("{}")
    assert True is solution.isValid("()({})({[]}){}{()}{([])}[][()][({})]")
    assert False is solution.isValid("(()")
