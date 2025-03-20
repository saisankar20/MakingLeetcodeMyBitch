class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # helper function (reusing your existing DP logic)
        def rob_linear(houses: List[int]) -> int:
            dp = [0] * len(houses)
            dp[0] = houses[0]
            if len(houses) > 1:
                dp[1] = max(houses[0], houses[1])
                for i in range(2, len(houses)):
                    dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]

        # Consider two scenarios separately:
        # Scenario 1: Rob first house, don't rob last
        scenario1 = rob_linear(nums[:-1])
        # Scenario 2: Rob last house, don't rob first
        scenario2 = rob_linear(nums[1:])

        return max(scenario1, scenario2)
