class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        Gcount = 0
        Lcount = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1 , n):
                if nums[i] > nums[j]:
                    Gcount += 1

        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                Lcount += 1
        
        if Gcount == Lcount:
            return True
        else:
             return False
        
