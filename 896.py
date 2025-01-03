class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        if nums[-1] < nums[0]:
            nums = nums[::-1]
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
