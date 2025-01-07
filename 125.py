class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ''.join(char for char in s if char.isalnum())
        
        if result == result[::-1]:
            return True
        else:
            return False
