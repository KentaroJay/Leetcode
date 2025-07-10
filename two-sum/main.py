from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_map: dict[int, int] = dict()
        for index, item in enumerate(nums):
            desired_value = target - item
            mapped_index = value_index_map.get(desired_value)
            if mapped_index is None:
                value_index_map[item] = index
                continue
            return [index, mapped_index]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.twoSum([3, 3], 6)
    print(ans)
