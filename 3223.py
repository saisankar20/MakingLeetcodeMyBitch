from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        minus = 0
        for x in count.values():
            while x >= 3:
                minus += 2
                x -= 2
        return len(s) - minus
