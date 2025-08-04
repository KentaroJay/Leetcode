from typing import List
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def can_split(index: int):
            if index == len(s):
                return True
            for word in wordDict:
                if s[index:index + len(word)] != word:
                    continue
                if can_split(index + len(word)):
                    return True
            return False

        return can_split(0)


if __name__ == "__main__":
    solution = Solution()
    assert True is solution.wordBreak("leetcode", ["leet", "code"])
    assert True is solution.wordBreak("leetcode", ["leet", "leetc",  "ode"])
    assert True is solution.wordBreak("applepenapple", ["apple", "pen"])
    assert False is solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
