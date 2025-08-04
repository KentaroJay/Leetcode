class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = pointer_t = 0
        s_length = len(s)
        t_length = len(t)

        while pointer_s < s_length and pointer_t < t_length:
            s_at = s[pointer_s]
            t_at = t[pointer_t]

            if s_at == t_at:
                pointer_s += 1
                pointer_t += 1
                continue
            pointer_t += 1
        if pointer_s == s_length:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    assert True is solution.isSubsequence("ace", "abcde")
    assert False is solution.isSubsequence("bae", "abcde")
