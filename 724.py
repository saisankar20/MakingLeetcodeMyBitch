class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = sum(nums)
        leftsum = 0

        for i in range(n):
            #leftsum = leftsum + nums[i]
            rightsum = Tsum - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
