class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        fre = {}
        count = 0

        for num in nums:
            if num - k in fre:
                count += fre[num - k]
            if num + k in fre:
                count += fre[num + k]

            if num in fre:
                fre[num] += 1
            else:
                fre[num] = 1
        
        return count
