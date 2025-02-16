class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        return sum(range(len(nums)+ 1)) - sum(nums)
