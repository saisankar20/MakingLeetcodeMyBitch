class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        l , r = 0 , 1
        count = 0
        n = len(nums)

        while r < n:
            if nums[r] - nums[l] < diff:
                r += 1

            elif nums[r] - nums[l] > diff:
                l += 1
            
            else:
                if nums[r] + diff in nums:
                    count += 1

                l += 1
                r += 1

        return count

        
