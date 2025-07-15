from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        n_array = len(nums1) + len(nums2)
        n_half = (n_array) // 2
        median_index = n_array // 2

        def get_foo(
            range_start_1: int = 0,
            range_end_1: int = len(nums1) - 1,
            range_start_2: int = 0,
            range_end_2: int = len(nums2) - 1,
        ):
            if 