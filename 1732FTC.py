class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        maxAltitutde  = current

        left = 0
        n = len(gain)

        for i in range(n):
            if current + gain[i] > maxAltitutde:
                current = current + gain[i]
                maxAltitutde  = current
                i += 1
            return maxAltitutde

        
