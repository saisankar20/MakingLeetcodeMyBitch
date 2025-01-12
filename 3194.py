class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = float('inf')
        l , r = 0 , len(nums) - 1

        while l < r:
            avg =(nums[l]+ nums[r])/ 2
            min_avg = min(min_avg, avg)
            l += 1
            r -= 1

        return min_avg
            
