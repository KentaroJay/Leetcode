from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while right - left >= 1:
            if right - left == 1 and nums[right] < nums[left]:
                left = right
                continue
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else: # nums[mid] == nums[right]
                # There is a duplication in the given array
                raise ValueError
        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMin([0,1,2,4,5,6,7]) == 0

