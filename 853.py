class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort (position, speed) pairs by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd  # Compute time correctly
            
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)  # This part is just computing time, not fleets yet
