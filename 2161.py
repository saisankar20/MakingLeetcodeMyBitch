class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        equal = []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                great.append(i)
                


            
                
            
        result = less + equal + great
        return result

        
