class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        total_water = 0

        while left < right:
            if height[left] < height[right]:
            # Water depends on leftMax
                if height[left] >= leftMax:
                    leftMax = height[left]  # Update leftMax
                else:
                    total_water += leftMax - height[left]  # Water trapped
                left += 1  # Move left pointer right
            else:
            # Water depends on rightMax
                if height[right] >= rightMax:
                    rightMax = height[right]  # Update rightMax
                else:
                    total_water += rightMax - height[right]  # Water trapped
                right -= 1  # Move right pointer left

        return total_water




        
