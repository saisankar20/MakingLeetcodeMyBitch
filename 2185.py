class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for char in words:
            if char.startswith(pref):
                count += 1
        return count
        
