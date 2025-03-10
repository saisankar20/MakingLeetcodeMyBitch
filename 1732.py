class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        maxAltitutde  = current

        left = 0
        n = len(gain)

        for i in range(n):
            current += gain[i]
            if current > maxAltitutde:
                maxAltitutde = current
        return maxAltitutde

        
