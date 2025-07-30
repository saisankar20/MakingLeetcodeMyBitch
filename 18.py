class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates for i
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:  # Skip duplicates for j
                    continue
                l, r = j+1, n-1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:  # Skip duplicates for l
                            l += 1
                        while l < r and nums[r] == nums[r+1]:  # Skip duplicates for r
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res
