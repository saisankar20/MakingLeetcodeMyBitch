from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)  
            for char, freq in word_count.items():
                max_freq[char] = max(max_freq[char], freq) 
       
        result = []
        for word in words1:
            word_count = Counter(word) 
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
