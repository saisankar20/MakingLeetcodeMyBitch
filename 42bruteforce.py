class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        agua = 0


        for i in range(n):

            max_left = max(height[:i+1])

            max_right = max(height[i:])

            agua_at_i = min(max_left , max_right) - height[i]

            agua += max(agua_at_i, 0)
        
        return agua

        
