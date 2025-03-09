class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Covers uppercase & lowercase
        chars = list(s)            # Convert string to list
        left, right = 0, len(chars) - 1

        while left < right:
            # Move left pointer until it hits a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            # Move right pointer until it hits a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]
            
            # Move both pointers
            left += 1
            right -= 1

        return ''.join(chars)  # Convert list back to string
