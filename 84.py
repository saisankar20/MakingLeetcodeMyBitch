from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store indices of bars
        max_area = 0  # Variable to store max area
        heights.append(0)  # Append a zero height to force final computation
        
        for i in range(len(heights)):
            # While the stack is not empty and the current height is smaller than the last stacked height
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar being removed
                w = i if not stack else i - stack[-1] - 1  # Calculate width
                max_area = max(max_area, h * w)  # Update max area
            
            stack.append(i)  # Push the current bar index to stack
        
        return max_area
