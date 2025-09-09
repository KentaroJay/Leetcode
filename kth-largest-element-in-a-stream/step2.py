from heapq import heappush, heappop
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        for value in nums:
            self.add(value)


    def add(self, val: int) -> int:
        heappush(self.stream, val)
        if len(self.stream) > self.k:
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


