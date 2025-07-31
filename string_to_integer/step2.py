class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        if not s:
            return ans

        pointer = 0
        s_length = len(s)

        while pointer < s_length and s[pointer] == " ":
            pointer += 1

        if pointer == s_length:
            return ans

        sign = 1
        if s[pointer] == "-":
            sign = -1
            pointer += 1
        elif s[pointer] == "+":
            pointer += 1

        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        while pointer < s_length:
            s_at = s[pointer]
            if not s_at.isdigit():
                return ans
            ans = ans * 10 + sign * int(s_at)
            pointer += 1

            if ans >= int_max:
                return int_max
            if ans <= int_min:
                return int_min
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert 42 == solution.myAtoi("42")
    assert -42 == solution.myAtoi("   -042")
    assert 1337 == solution.myAtoi("1337c0d3")
    assert 0 == solution.myAtoi("0-1")
    assert 0 == solution.myAtoi("words 879")
    assert -2147483648 == solution.myAtoi("-2147483649")
    assert 2147483647 == solution.myAtoi("2147483648")
    assert 0 == solution.myAtoi(" ")
