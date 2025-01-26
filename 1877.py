class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
      
        sum_all = []

        l = 0 
        r = len(nums) - 1

        while l < r:
            current_sum = nums[l] + nums[r]
            sum_all.append(current_sum)
            l += 1
            r -= 1
        return max(sum_all)
        
