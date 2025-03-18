class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 1)
        ways[0] = 1  # One way to climb zero steps (consider this as a starting 
        ways[1] = 1  # One way to climb one step

        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        
        return ways[n]
