class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for  i in arr:
            freq[i] = freq.get(i , 0) + 1

        seen = set()
        
        for key, count in freq.items():
            if count in seen:
                return False
            seen.add(count)
        return True

        
