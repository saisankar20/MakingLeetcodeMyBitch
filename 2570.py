from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        nums3 = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:  # Matching IDs
                sumval = nums1[i][1] + nums2[j][1]
                nums3.append([nums1[i][0], sumval])
                i += 1
                j += 1  # Move both pointers
            elif nums1[i][0] < nums2[j][0]:  # Unique ID in nums1
                nums3.append(nums1[i])
                i += 1
            else:  # Unique ID in nums2
                nums3.append(nums2[j])
                j += 1

        # Add remaining elements from nums1 or nums2
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1

        return nums3
