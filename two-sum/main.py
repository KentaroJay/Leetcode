from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map: dict[int, int] = dict()
        for index, num in enumerate(nums):
            desired_value = target - num
            mapped_index = value_index_map.get(desired_value)
            if mapped_index is None:
                value_index_map[num] = index
                continue
            return [index, mapped_index]

