class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unums1 = set(nums1)    # avoids handling '3' twice
        unums2 = set(nums2)
        result1, result2 = [], []

        for i in unums1:
            if i not in nums2:
                result1.append(i)
                
        for j in unums2:
            if j not in nums1:
                result2.append(j)
                

        return [result1, result2]
