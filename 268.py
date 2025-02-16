class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):

            if (i != num):
                return num - 1

            if num == len(nums) - 1:
                return num + 1


        
