class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1 = {}
        freq2 = {}

        # 1) Build frequency map for nums1
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
        
        # 2) Build frequency map for nums2
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1
        
        # 3) Find distinct values in nums1 that aren't in nums2
        result1 = []
        for key in freq1:
            if key not in freq2:
                result1.append(key)
        
        # 4) Find distinct values in nums2 that aren't in nums1
        result2 = []
        for key in freq2:
            if key not in freq1:
                result2.append(key)
        
        return [result1, result2]
