from typing import List


# [1,2,3,4,5,6,9,8,7]
#            1 2 3 4 5                   6
# pivot_idx: 7 6 5 
#  swap_idx:       8 
#      nums: s       [1,2,3,4,5,7,9,8,6] [1,2,3,4,5,7,6,8,9]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot_idx = len(nums) - 2

        while pivot_idx > -1 and nums[pivot_idx] >= nums[pivot_idx + 1]:
            pivot_idx -= 1

        if pivot_idx == -1:
            return nums.reverse()

        swap_idx = len(nums) - 1
        while nums[swap_idx] <= nums[pivot_idx]:
            swap_idx -=1

        nums[swap_idx], nums[pivot_idx] = nums[pivot_idx], nums[swap_idx]

        nums[pivot_idx + 1:] = reversed(nums[pivot_idx + 1:])

