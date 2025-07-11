from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index: dict[int, int] = dict()
        for index, num in enumerate(nums):
            desired_value = target - num
            mapped_index = value_to_index.get(desired_value)
            if mapped_index is None:
                value_to_index[num] = index
                continue
            return [index, mapped_index]

