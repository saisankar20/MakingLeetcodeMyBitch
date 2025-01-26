from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 1. Sort nums in ascending order
        sorted_nums = sorted(nums)
        
        # 2. Create a prefix sum array
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + sorted_nums[i - 1]
        
        # 3. For each query, use binary search on the prefix sums
        #    to find the maximum k such that prefix[k] <= query
        result = []
        for q in queries:
            # bisect_right(prefix, q) gives the insertion position 
            # where q would be placed to keep prefix sorted.
            # So it returns 1 index *past* the largest prefix <= q.
            # Hence, we subtract 1 to get the largest valid k.
            k = bisect.bisect_right(prefix, q) - 1
            result.append(k)
        
        return result
