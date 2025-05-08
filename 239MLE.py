class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sumofK = []
        l = 0 

        while l + k  <= len(nums):
            s = sum(nums[l:l+k])
            sumofK.append(nums[l:l+k])
            l += 1

        maxes = [max(w) for w in sumofK]   # gives [3, 3, 5, 5, 6, 7]


        return maxes
        
