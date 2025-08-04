from dataclasses import dataclass
from enum import Enum


class Shape(Enum):
    ROUND = "round"
    CURLY = "curly"
    SQUARE = "square"


class Type(Enum):
    OPEN = "open"
    CLOSE = "close"


@dataclass
class Parenthesis:
    OPEN = ["(", "{", "["]
    CLOSE = [")", "}", "]"]

    shape: Shape
    type: Type

    def __init__(self, char: str):
        if char in self.OPEN:
            self.type = Type.OPEN
            if char == "(":
                self.shape = Shape.ROUND
            elif char == "{":
                self.shape = Shape.CURLY
            elif char == "[":
                self.shape = Shape.SQUARE
            else:
                raise ValueError  # unreachable
        elif char in self.CLOSE:
            self.type = Type.CLOSE
            if char == ")":
                self.shape = Shape.ROUND
            elif char == "}":
                self.shape = Shape.CURLY
            elif char == "]":
                self.shape = Shape.SQUARE
            else:
                raise ValueError  # unreachable
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
            if previous.type is not Type.OPEN:
                return False
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
