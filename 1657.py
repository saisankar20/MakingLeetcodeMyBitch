class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        freq1 , freq2 = {} , {}

        for word in word1:
            freq1[word] = freq1.get(word, 0) + 1
        
        for word in word2:
            freq2[word] = freq2.get(word, 0) + 1

        return sorted(freq1.values()) == sorted(freq2.values())
        
