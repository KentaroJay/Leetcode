from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else: # nums[mid] == nums[right]
                # There is a duplication in the given array
                raise ValueError
        return nums[left]

