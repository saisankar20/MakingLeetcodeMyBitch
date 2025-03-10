class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result1, result2 = [] , []
        for i in nums1:
            if i not in nums2:
                result1.append(i)
                i += 1
        #return result1
        

        for j in nums2:
            if j not in nums1:
                result2.append(j)
                j += 1
        #return result2

        result = [result1, result2]
        return result
        
