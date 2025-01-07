class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        output = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[output]:

                output += 1
                nums[output] =nums[i]
        
        return output + 1
            
