class Solution:
    def firstUniqChar(self, s: str) -> int:
        n_str = len(s)
        occurences = [0] * n_str
        char_to_idx = dict()
        for ith in range(n_str):
            char = s[ith]
            if char in char_to_idx:
                idx = char_to_idx[char]
                occurences[idx] += 1
                continue
            char_to_idx[char] = ith
            occurences[ith] = 1
        for idx, occurence in enumerate(occurences):
            if occurence == 1:
                return idx
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert 0 == solution.firstUniqChar("leetcode")
    assert 2 == solution.firstUniqChar("loveleetcode")
    assert -1 == solution.firstUniqChar("aaabb")

