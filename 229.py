class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        major = n//3
        res = []

        for num in count:
            if count[num] > major:
                res.append(num)
        return res

