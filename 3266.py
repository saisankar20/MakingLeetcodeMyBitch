from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10**9 + 7 
        
        for _ in range(k):
            
            min_index = nums.index(min(nums))
            
            nums[min_index] = (nums[min_index] * multiplier) % MOD
        
        return nums
