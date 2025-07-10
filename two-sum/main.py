from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map: dict[int, int] = dict()
        for current_index, current_item in enumerate(nums):
            desired_value = target - current_item
            mapped_index = value_index_map.get(desired_value)
            if mapped_index is None:
                value_index_map[current_item] = current_index
                continue
            return [current_index, mapped_index]

