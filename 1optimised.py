class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            dff = target - num
            if dff in lookup:
                return [lookup[dff], i]
            lookup[num] = i
        return []
        
