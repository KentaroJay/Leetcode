from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fixed = -1

        for i, num in enumerate(nums):
            if num != 0:
                fixed += 1
                nums[fixed] = num
        for i in range(fixed + 1, len(nums)):
            nums[i] = 0

