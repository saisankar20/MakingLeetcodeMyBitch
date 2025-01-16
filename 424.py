class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_count = Counter()
        max_length = 0


        for right in range(len(s)):

            char_count[s[right]] += 1

            max_freq = max(max_freq , char_count[s[right]])

            while (right - left + 1) - max_freq > k:
                # Shrink the window from the left
                char_count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length




        
