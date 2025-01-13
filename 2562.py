class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        con = []

        while l < r:
            con_val = int(str(nums[l]) + str(nums[r]))
            con.append(con_val)
            l += 1
            r -= 1

        if l == r:
            con.append(nums[l])

        return sum(con)


        
        
