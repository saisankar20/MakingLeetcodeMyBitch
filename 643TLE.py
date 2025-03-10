class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        SumOfk = []

        l ,n = 0 , len(nums)

        while l + k <= n:
            currentSum = sum(nums[l:l+k])
            SumOfk.append(currentSum)
            l += 1

        maxsumOfk = max(SumOfk)
        maxavg = maxsumOfk / k

        return maxavg

        
