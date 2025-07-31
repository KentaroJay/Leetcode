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
            if k >= n_array:
                return float('infinity')
            if k < 0:
                return float('-infinity')
            return array[k]

        def get_partitions(
            partition1: int = 0,
        ) -> tuple[int, int, int, int]:
            partition2 = target - partition1

            before1 = safe_get(partition1 - 1, nums1)
            after1 = safe_get(partition1, nums1)
            before2 = safe_get(partition2 - 1, nums2)
            after2 = safe_get(partition2, nums2)

            return (before1, after1, before2, after2)

        left = 0
        right = len(nums1)
        while left <= right:
            mid = (left + right) // 2
            before1, after1, before2, after2 = get_partitions(mid)
            if max(before1, before2) <= min(after1, after2):
                break
            if before1 > after2:
                right = mid - 1
                continue
            if before2 > after1:
                left = mid + 1
                continue
            raise ValueError

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
