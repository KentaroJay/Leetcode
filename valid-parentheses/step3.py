from dataclasses import dataclass
from enum import Enum


class Type(Enum):
    OPEN = "open"
    CLOSE = "close"


class Shape(Enum):
    ROUND = "round"
    SQUARE = "square"
    CURLY = "curly"


@dataclass
class Parenthesis:
    OPEN = ["(", "[", "{"]
    CLOSE = [")", "]", "}"]

    type: Type
    shape: Shape

    def __init__(self, char: str):
        if char in self.OPEN:
            self.type = Type.OPEN
            if char == "(":
                self.shape = Shape.ROUND
            elif char == "[":
                self.shape = Shape.SQUARE
            elif char == "{":
                self.shape = Shape.CURLY
            else:
                raise ValueError
        elif char in self.CLOSE:
            self.type = Type.CLOSE
            if char == ")":
                self.shape = Shape.ROUND
            elif char == "]":
                self.shape = Shape.SQUARE
            elif char == "}":
                self.shape = Shape.CURLY
            else:
                raise ValueError
        else:
            raise ValueError


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            current = Parenthesis(char)

            if current.type is Type.OPEN:
                stack.append(current)
                continue
            if len(stack) == 0:
                return False
            previous = stack.pop()
            if previous.shape is not current.shape:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    assert True is solution.isValid("[]")
    assert True is solution.isValid("()")
    assert True is solution.isValid("{}")
    assert True is solution.isValid("()({})({[]}){}{()}{([])}[][()][({})]")
    assert False is solution.isValid("(()")
