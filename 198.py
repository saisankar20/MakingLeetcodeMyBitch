class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # Choose max between house 0 and 1
        
        # Iterate up to n - 1 because the last valid house is at index n - 1
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The maximum profit is at the last element of dp
        return dp[n - 1]
