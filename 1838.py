class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        t = 0
        maxfrq = 0

        for right in range(len(nums)):
            t += nums[right]

            while (nums[right] * (right - l + 1)) > (t + k ):
                t -= nums[l]
                l += 1

            maxfrq = max(maxfrq , right - l + 1)

        
        return maxfrq

        
