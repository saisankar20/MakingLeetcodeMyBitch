class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        result = []

        left = 0
        n = len(s)

        for right in range(k,n):
            current = sum(1 for ch in s[:k] if ch in vowels)
        result.append(current)

        return max(result)


