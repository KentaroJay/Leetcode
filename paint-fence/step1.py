class Solution:
    def countWays(self, n, k):
        second_previous = k
        previous = k * k
        number_of_ways = second_previous if n == 1 else previous
        for _ in range(2, n):
            same_color = second_previous * (k - 1)
            different_color = previous * (k - 1)
            number_of_ways = same_color + different_color
            second_previous = previous
            previous = number_of_ways
        return number_of_ways


if __name__ == "__main__":
    solution = Solution()
    assert 6 == solution.countWays(3, 2)
    assert 16 == solution.countWays(2, 4)

