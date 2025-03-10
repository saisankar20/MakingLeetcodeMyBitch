class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #SumOfk = []

        n = len(nums)

        currentSum = sum(nums[:k])
        maxSum = currentSum

        left = 0
        for right in range(k,n):
            currentSum = currentSum - nums[left] + nums[right]
            if currentSum > maxSum:
                maxSum = currentSum
            left += 1

        return maxSum / k





       

        
