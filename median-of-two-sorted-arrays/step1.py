from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        n_array = len(nums1) + len(nums2)
        target = n_array // 2

        def safe_get(k: int, array: List[int]) -> int | float:
            n_array = len(array)
            if k < 0:
                return float('-infinity')
            if n_array <= k:
                return float('infinity')
            return array[k]

        def get_values(
            left: int = 0,
            right: int = len(nums1),
        ) -> tuple[int, int, int, int]:
            partition1 = (right + left) // 2
            partition2 = target - partition1

            before1 = safe_get(partition1 - 1, nums1)
            after1 = safe_get(partition1, nums1)
            before2 = safe_get(partition2 - 1, nums2)
            after2 = safe_get(partition2, nums2)

            if max(before1, before2) <= min(after1, after2):
                return (before1, after1, before2, after2)
            elif before1 > after2:
                return get_values(left, partition1 - 1)
            elif before2 > after1:
                return get_values(partition1 + 1, right)
            raise ValueError

        before1, after1, before2, after2 = get_values()
        if n_array % 2 == 0:
            return (
                max(before1, before2) + min(after1, after2)
            ) / 2
        return min(after1, after2)


if __name__ == "__main__":
    solution = Solution()
    assert 2 == solution.findMedianSortedArrays([1, 3], [2])
    assert 2.5 == solution.findMedianSortedArrays([1, 3], [2, 4])
    assert 2.5 == solution.findMedianSortedArrays([1, 2], [3, 4])
    assert 3 == solution.findMedianSortedArrays([2,3,4,5], [1])
