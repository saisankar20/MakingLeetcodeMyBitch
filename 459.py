class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for j in range(1, len(s)):  
            if len(s) % j == 0: 
                substr = s[:j]  
                if substr * (len(s) // j) == s:
                    return True

        return False  
