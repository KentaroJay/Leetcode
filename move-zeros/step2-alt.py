from typing import List

# [0,1,0,3,12]
#       1  2            3 4            5            6            7
# fixed -1 0            0 1            2
#     i 0  1            2 3            4            3            4
#   num 0  1            0 3            12
#  nums S  [1,1,0,3,12] S [1,3,0,3,12] [1,3,2,3,12] [1,3,2,0,12] [1,3,2,0,0]


# [1]
#       1     2
# fixed -1->0 
#     i 0     
#   num 1
#  nums S

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fixed = -1

        for i, num in enumerate(nums):
            if num != 0:
                fixed += 1
                nums[fixed] = num
        for i in range(fixed + 1, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()
    ans = solution.moveZeroes([0,1,0,3,12])
    breakpoint()
                
