class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        combo = int("".join(map(str, digits))) + 1
        new_digits = [int(d) for d in str(combo)]
        return new_digits

        
