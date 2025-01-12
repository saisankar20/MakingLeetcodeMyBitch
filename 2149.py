class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = []
        negitive = []
        op = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                postive.append(nums[i])
            if nums[i] < 0:
                negitive.append(nums[i])

        for i in range(len(postive)):
            op.append(postive[i])
            op.append(negitive[i])
           

        return op
                

            
