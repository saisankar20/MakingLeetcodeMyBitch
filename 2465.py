class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        average = set()
        
        while nums:
            small = nums.pop(0)
            large = nums.pop(-1)
            avg  = (small + large) / 2
            average.add(avg)

        return len(average)
            
