class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        major = n//2

        for num in count:
            if count[num] > major:
                return num

