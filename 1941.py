class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return len(set(char_count.values())) == 1


        
