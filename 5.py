class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around the center
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        # Initialize the longest palindrome variable
        longest = ""
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # Odd-length palindrome (single center)
            palindrome1 = expand_around_center(s, i, i)
            # Even-length palindrome (center is between i and i+1)
            palindrome2 = expand_around_center(s, i, i + 1)
            
            # Track the longest palindrome
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest


        
