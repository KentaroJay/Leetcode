from heapq import heappush, heappop
from typing import List

# [], -3, -2, -4, 0, 4
# 1

#           1, 2, 3,   4,      5,   6,      7,   8,     9,  10,   11
# stream    []    [-3] [-3,-2] [-2] [-4,-2] [-2] [-2,0] [0] [0,4] [4]
# removable    -1

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        for value in nums:
            heappush(self.stream, value)
        removable = len(nums) - k
        if removable <= 0:
            return
        for _ in range(removable):
            heappop(self.stream)
        assert len(self.stream) == k


    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heappush(self.stream, val)
            return self.stream[0]
        heappush(self.stream, val)
        heappop(self.stream)
        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    param_1 = obj.add(3)
    param_2 = obj.add(5)
    param_3 = obj.add(10)
    param_4 = obj.add(9)
    param_5 = obj.add(4)
    breakpoint()

