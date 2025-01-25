class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the list first
        sorted_nums = sorted(nums)
        
        # Collect indices where the number equals the target
        ans = []
        for i, num in enumerate(sorted_nums):
            if num == target:
                ans.append(i)
        
        # Return the list of indices
        return ans
