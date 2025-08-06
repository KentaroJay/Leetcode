class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        previous_number_of_ways = k
        current_number_of_ways = k * k
        for _ in range(2, n):
            same_color = previous_number_of_ways * (k - 1)
            different_color = current_number_of_ways * (k - 1)
            next_number_of_ways = same_color + different_color
            previous_number_of_ways = current_number_of_ways
            current_number_of_ways = next_number_of_ways
        return current_number_of_ways


if __name__ == "__main__":
    solution = Solution()
    assert 6 == solution.countWays(3, 2)
    assert 16 == solution.countWays(2, 4)

