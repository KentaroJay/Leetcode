from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length_nums = len(nums)

        last_non_zero_idx = None
        def get_right_side_value_from(idx: int):
            nonlocal last_non_zero_idx

            if last_non_zero_idx:
                start = last_non_zero_idx + 1
            else:
                start = idx + 1

            for i in range(start, length_nums):
                if nums[i] != 0:
                    last_non_zero_idx = i
                    return i
            return None

        for i in range(length_nums):
            val = nums[i]
            if val != 0:
                continue
            # nums[i] == 0
            # 1. find the left-most non-zero value on the right side
            # 2. swap them
            if left_most := get_right_side_value_from(i):
                nums[i], nums[left_most] = nums[left_most], nums[i]
            else: 
                break


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    solution = Solution()
    ans = solution.moveZeroes(nums)
    breakpoint()
